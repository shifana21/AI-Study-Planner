import os
import json
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=api_key)


def generate_ai_plan(subjects, exam_date, daily_hours, level, weak_subjects, strong_subjects, study_preference):

    weak_subjects_str = ", ".join(weak_subjects) if weak_subjects else "None"
    strong_subjects_str = ", ".join(strong_subjects) if strong_subjects else "None"

    prompt = f"""
You are an AI study planner.

Create a study plan for a college student.

Subjects: {", ".join(subjects)}
Exam Date: {exam_date}
Daily Study Hours: {daily_hours}
Current Level: {level}
Weak Subjects: {weak_subjects_str}
Strong Subjects: {strong_subjects_str}
Study Preference: {study_preference}

Create one study plan item for every day before the exam.

Requirements:
- Divide subjects intelligently based on the student's level ({level}).
- SPEND MORE TIME on weak subjects: {weak_subjects_str}.
- Use strong subjects for quick revision: {strong_subjects_str}.
- Adapt the study style to the preference: {study_preference}.
  - If "Theory": Focus on reading, understanding concepts, and notes.
  - If "Coding / Practice": Focus on writing code, solving problems, and hands-on exercises.
  - If "Revision": Focus on reviewing and reinforcing already learned topics.
  - If "Mixed": Balance all approaches appropriately.
- Include learning.
- Include practice questions.
- Include revision.
- Include a mock test before the exam.
- Keep the workload realistic.
- For beginners: Include more foundational concepts and slower progression.
- For intermediate: Include a mix of theory and practical application.
- For advanced: Include complex topics, optimization, and advanced techniques.

Return ONLY valid JSON.
Do not use markdown.
Do not use ```json.
Do not add explanations.

Use exactly this format:

[
  {{
    "date": "06-10-2026",
    "subject": "Java",
    "hours": 3,
    "task": "Study OOP concepts and solve practice questions"
  }}
]
"""

    models = [
        "gemini-3.8-flash",
        "gemini-3.7-flash",
        "gemini-3.6-flash",
        "gemini-3.5-flash"
    ]

    for model in models:

        print(f"\nTrying Gemini model: {model}")

        for attempt in range(2):

            try:

                chat = client.chats.create(
                    model=model
                )

                response = chat.send_message(
                    message=prompt
                )

                ai_text = response.text.strip()

                print("\n===== GEMINI RESPONSE =====")
                print(ai_text)
                print("===========================\n")

                # Remove markdown if Gemini adds it
                ai_text = ai_text.replace("```json", "")
                ai_text = ai_text.replace("```", "")
                ai_text = ai_text.strip()

                # Find JSON array
                start = ai_text.find("[")
                end = ai_text.rfind("]")

                if start == -1 or end == -1:
                    print("Could not find JSON array.")
                    continue

                ai_text = ai_text[start:end + 1]

                plan = json.loads(ai_text)

                if isinstance(plan, list) and len(plan) > 0:

                    print("AI PLAN GENERATED SUCCESSFULLY")

                    return plan

            except Exception as e:

                print(
                    f"Gemini Error ({model}, attempt {attempt + 1}):",
                    e
                )

                time.sleep(2)

    print("\nAll Gemini attempts failed.")

    return []