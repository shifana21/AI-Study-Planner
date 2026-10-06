from gemini_service import generate_ai_plan


subjects = ["Java", "DBMS", "Python"]
exam_date = "20-10-2026"
daily_hours = 3


plan = generate_ai_plan(
    subjects,
    exam_date,
    daily_hours
)


print("\n===== AI STUDY PLAN =====\n")
print(plan)