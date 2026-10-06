from datetime import datetime, timedelta


def generate_plan(subjects, exam_date, daily_hours):

    today = datetime.today().date()

    exam_date = datetime.strptime(
        exam_date,
        "%Y-%m-%d"
    ).date()

    total_days = (exam_date - today).days

    plan = []

    if total_days <= 0:
        return plan

    for i in range(total_days):

        current_date = today + timedelta(days=i)

        # Every 7th day = Revision
        if (i + 1) % 7 == 0:

            plan.append({
                "date": current_date.strftime("%d-%m-%Y"),
                "subject": "Revision",
                "hours": daily_hours,
                "task": "Revise all topics studied this week"
            })

        # Last 2 days = Mock Test
        elif i == total_days - 2:

            plan.append({
                "date": current_date.strftime("%d-%m-%Y"),
                "subject": "Mock Test",
                "hours": daily_hours,
                "task": "Take a full mock test and analyze mistakes"
            })

        elif i == total_days - 1:

            plan.append({
                "date": current_date.strftime("%d-%m-%Y"),
                "subject": "Final Revision",
                "hours": daily_hours,
                "task": "Quick revision of important concepts and formulas"
            })

        else:

            subject = subjects[i % len(subjects)]

            plan.append({
                "date": current_date.strftime("%d-%m-%Y"),
                "subject": subject,
                "hours": daily_hours,
                "task": f"Study {subject} and practice important questions"
            })

    return plan