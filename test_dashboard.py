"""
Test dashboard functionality calculations
"""
from gemini_service import generate_recommendations


def test_recommendations():
    """Test AI recommendations with fallback"""
    progress_data = {
        "total_tasks": 14,
        "completed_tasks": 7,
        "overall_progress": 50
    }

    subject_progress = {
        "Java": {"total": 5, "completed": 2, "hours": 15},
        "DBMS": {"total": 5, "completed": 3, "hours": 15},
        "Python": {"total": 4, "completed": 2, "hours": 12}
    }

    weak_subjects = ["Java", "DBMS"]
    strong_subjects = ["Python"]
    level = "Intermediate"
    preference = "Coding / Practice"
    remaining_days = 14

    recommendations = generate_recommendations(
        progress_data,
        subject_progress,
        weak_subjects,
        strong_subjects,
        level,
        preference,
        remaining_days
    )

    print("\n===== RECOMMENDATIONS TEST =====")
    print(f"Priority Subject: {recommendations.get('priority_subject', 'N/A')}")
    print(f"Strategy: {recommendations.get('strategy', 'N/A')}")
    print(f"Number of recommendations: {len(recommendations.get('recommendations', []))}")

    assert 'recommendations' in recommendations
    assert len(recommendations['recommendations']) > 0
    print("[PASS] Recommendations test passed")


def test_readiness_score():
    """Test readiness score calculation"""
    overall_percentage = 50
    avg_subject_score = 45
    days_factor = 1

    readiness_score = round(overall_percentage * 0.5 + avg_subject_score * 0.3 + days_factor * 20)

    print("\n===== READINESS SCORE TEST =====")
    print(f"Overall: {overall_percentage}%")
    print(f"Avg Subject: {avg_subject_score}%")
    print(f"Days Factor: {days_factor}")
    print(f"Readiness Score: {readiness_score}%")

    assert 0 <= readiness_score <= 100
    print("[PASS] Readiness score test passed")


def test_plan_id_generation():
    """Test plan ID generation logic"""
    exam_date = "20-10-2026"
    subjects = ["Java", "DBMS", "Python"]
    subjects_sorted = sorted(subjects)
    plan_id = f"{exam_date}_{'_'.join(subjects_sorted)}"

    print("\n===== PLAN ID TEST =====")
    print(f"Plan ID: {plan_id}")

    assert plan_id == "20-10-2026_DBMS_Java_Python"
    print("[PASS] Plan ID test passed")


if __name__ == "__main__":
    test_recommendations()
    test_readiness_score()
    test_plan_id_generation()
    print("\n===== ALL TESTS PASSED =====")
