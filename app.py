from flask import Flask, render_template, request, jsonify
from gemini_service import generate_ai_plan, generate_recommendations

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    plan = None
    error_message = None

    if request.method == "POST":
        try:
            subjects = request.form["subjects"].split(",")
            subjects = [subject.strip() for subject in subjects]

            exam_date = request.form["exam_date"]
            daily_hours = int(request.form["daily_hours"])
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

            plan = generate_ai_plan(
                subjects,
                exam_date,
                daily_hours,
                level,
                weak_subjects,
                strong_subjects,
                study_preference
            )

            if not plan:
                error_message = "⚠️ AI service is temporarily unavailable. Please try again in a few moments."

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
                },
                error_message=error_message
            )

        except Exception as e:
            error_message = "⚠️ An error occurred while generating your study plan. Please try again."
            return render_template(
                "index.html",
                plan=None,
                error_message=error_message
            )

    return render_template(
        "index.html",
        plan=plan,
        error_message=error_message
    )


@app.route("/api/recommendations", methods=["POST"])
def get_recommendations():
    """API endpoint for generating AI recommendations."""
    try:
        data = request.get_json()
        progress_data = data.get('progress_data', {})
        subject_progress = data.get('subject_progress', {})
        weak_subjects = data.get('weak_subjects', [])
        strong_subjects = data.get('strong_subjects', [])
        level = data.get('level', 'Intermediate')
        preference = data.get('preference', 'Mixed')
        remaining_days = data.get('remaining_days', 30)

        recommendations = generate_recommendations(
            progress_data,
            subject_progress,
            weak_subjects,
            strong_subjects,
            level,
            preference,
            remaining_days
        )

        return jsonify(recommendations)

    except Exception as e:
        return jsonify({"error": "Failed to generate recommendations"}), 500


if __name__ == "__main__":
    app.run(debug=True)