# career_gap.py

JOB_ROLES = {
    "Machine Learning Engineer": [
        "python", "machine learning", "deep learning",
        "nlp", "sql", "statistics"
    ],

    "Data Analyst": [
        "python", "sql", "excel",
        "data analysis", "statistics"
    ],

    "AI Engineer": [
        "python", "machine learning",
        "deep learning", "nlp",
        "tensorflow", "pytorch"
    ],

    "Software Developer": [
        "python", "java",
        "sql", "git"
    ]
}


def analyze_career_gap(resume_skills, target_role):

    resume_skills = [s.lower() for s in resume_skills]

    required_skills = JOB_ROLES.get(target_role, [])

    missing_skills = []

    for skill in required_skills:
        if skill.lower() not in resume_skills:
            missing_skills.append(skill)

    readiness = int(
        ((len(required_skills) - len(missing_skills))
         / len(required_skills)) * 100
    )

    return readiness, missing_skills