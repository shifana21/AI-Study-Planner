from gemini_service import generate_ai_plan


subjects = ["Java", "DBMS", "Python"]
exam_date = "20-10-2026"
daily_hours = 3
level = "Intermediate"
weak_subjects = ["Java", "DBMS"]
strong_subjects = ["Python"]
study_preference = "Coding / Practice"


plan = generate_ai_plan(
    subjects,
    exam_date,
    daily_hours,
    level,
    weak_subjects,
    strong_subjects,
    study_preference
)


print("\n===== AI STUDY PLAN =====\n")
print(f"Generated {len(plan)} study sessions")
if plan:
    print(f"First task: {plan[0]}")
    print(f"Last task: {plan[-1]}")
print("\n===== TEST PASSED =====")