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

        for attempt in range(2):

            try:

                chat = client.chats.create(
                    model=model
                )

                response = chat.send_message(
                    message=prompt
                )

                ai_text = response.text.strip()

                # Remove markdown if Gemini adds it
                ai_text = ai_text.replace("```json", "")
                ai_text = ai_text.replace("```", "")
                ai_text = ai_text.strip()

                # Find JSON array
                start = ai_text.find("[")
                end = ai_text.rfind("]")

                if start == -1 or end == -1:
                    continue

                ai_text = ai_text[start:end + 1]

                plan = json.loads(ai_text)

                if isinstance(plan, list) and len(plan) > 0:

                    return plan

            except Exception as e:

                time.sleep(2)

    return []


def generate_recommendations(progress_data, subject_progress, weak_subjects, strong_subjects, level, preference, remaining_days):
    """
    Generate AI-powered study recommendations based on student progress.
    Falls back to rule-based recommendations if Gemini fails.
    """
    weak_subjects_str = ", ".join(weak_subjects) if weak_subjects else "None"
    strong_subjects_str = ", ".join(strong_subjects) if strong_subjects else "None"

    prompt = f"""
You are an AI study advisor.

Based on the following student data, provide personalized study recommendations:

Student Level: {level}
Study Preference: {preference}
Weak Subjects: {weak_subjects_str}
Strong Subjects: {strong_subjects_str}
Remaining Days Until Exam: {remaining_days}

Progress Data:
{json.dumps(progress_data, indent=2)}

Subject Progress:
{json.dumps(subject_progress, indent=2)}

Provide 3-5 specific, actionable recommendations.

Return ONLY valid JSON in this exact format:
{{
  "priority_subject": "Subject name",
  "recommendations": [
    "Recommendation 1",
    "Recommendation 2",
    "Recommendation 3"
  ],
  "strategy": "Overall strategy description",
  "next_task_reason": "Reason for recommended next task"
}}

Do not use markdown.
Do not add explanations.
"""

    models = [
        "gemini-3.8-flash",
        "gemini-3.7-flash",
        "gemini-3.6-flash",
        "gemini-3.5-flash"
    ]

    for model in models:
        try:
            chat = client.chats.create(model=model)
            response = chat.send_message(message=prompt)
            ai_text = response.text.strip()

            ai_text = ai_text.replace("```json", "")
            ai_text = ai_text.replace("```", "")
            ai_text = ai_text.strip()

            start = ai_text.find("{")
            end = ai_text.rfind("}")

            if start == -1 or end == -1:
                continue

            ai_text = ai_text[start:end + 1]
            recommendations = json.loads(ai_text)

            if "recommendations" in recommendations:
                return recommendations

        except Exception as e:
            time.sleep(1)

    return get_rule_based_recommendations(progress_data, subject_progress, weak_subjects, strong_subjects, remaining_days)


def get_rule_based_recommendations(progress_data, subject_progress, weak_subjects, strong_subjects, remaining_days):
    """
    Fallback rule-based recommendations when Gemini is unavailable.
    """
    recommendations = []
    priority_subject = None

    if weak_subjects and len(weak_subjects) > 0:
        priority_subject = weak_subjects[0]
        recommendations.append(f"🎯 Priority: Focus more on {priority_subject} because it's marked as a weak subject.")

    if subject_progress:
        for subject, data in subject_progress.items():
            if data['total'] > 0:
                completion_rate = (data['completed'] / data['total']) * 100
                if completion_rate < 50 and subject in (weak_subjects or []):
                    recommendations.append(f"📚 Revision: {subject} needs more attention with only {completion_rate:.0f}% completion.")
                elif completion_rate > 80 and subject in (strong_subjects or []):
                    recommendations.append(f"🔥 Strong Area: {subject} is progressing well. Maintain with short revision sessions.")

    if remaining_days <= 7:
        recommendations.append("⏰ Time Management: Exam is approaching. Focus on revision and practice tests.")
    elif remaining_days <= 14:
        recommendations.append("💻 Practice: Complete 2-3 practice problems daily to build confidence.")

    if not recommendations:
        recommendations.append("📝 Continue with your current study plan. You're making good progress!")

    return {
        "priority_subject": priority_subject or strong_subjects[0] if strong_subjects else "General",
        "recommendations": recommendations,
        "strategy": "Follow your study plan consistently and focus on weak areas.",
        "next_task_reason": "Based on your current progress and subject priorities."
    }