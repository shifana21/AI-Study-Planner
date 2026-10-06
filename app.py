from flask import Flask, render_template, request
from gemini_service import generate_ai_plan

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    print("\n========== REQUEST ==========")
    print("Method:", request.method)

    plan = None

    if request.method == "POST":

        print("FORM DATA:", request.form)

        subjects = request.form["subjects"].split(",")

        subjects = [
            subject.strip()
            for subject in subjects
        ]

        exam_date = request.form["exam_date"]

        daily_hours = int(
            request.form["daily_hours"]
        )

        level = request.form["level"]

        weak_subjects = request.form.get("weak_subjects", "")
        if weak_subjects:
            weak_subjects = [s.strip() for s in weak_subjects.split(",")]
        else:
            weak_subjects = []

        strong_subjects = request.form.get("strong_subjects", "")
        if strong_subjects:
            strong_subjects = [s.strip() for s in strong_subjects.split(",")]
        else:
            strong_subjects = []

        study_preference = request.form["study_preference"]

        print("Subjects:", subjects)
        print("Exam Date:", exam_date)
        print("Daily Hours:", daily_hours)
        print("Level:", level)
        print("Weak Subjects:", weak_subjects)
        print("Strong Subjects:", strong_subjects)
        print("Study Preference:", study_preference)

        plan = generate_ai_plan(
            subjects,
            exam_date,
            daily_hours,
            level,
            weak_subjects,
            strong_subjects,
            study_preference
        )

        print("PLAN:", plan)

        return render_template(
            "index.html",
            plan=plan,
            form_data={
                'subjects': subjects,
                'exam_date': exam_date,
                'daily_hours': daily_hours,
                'level': level,
                'weak_subjects': weak_subjects,
                'strong_subjects': strong_subjects,
                'study_preference': study_preference
            }
        )

    return render_template(
        "index.html",
        plan=plan
    )


if __name__ == "__main__":
    app.run(debug=True)