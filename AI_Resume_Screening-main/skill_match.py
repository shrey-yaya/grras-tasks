def get_skill_match(resume_skills, required_skills):
    resume_skills = [skill.lower() for skill in resume_skills]
    required_skills = [skill.lower() for skill in required_skills]

    matched = list(set(resume_skills) & set(required_skills))
    missing = list(set(required_skills) - set(resume_skills))

    if len(required_skills) == 0:
        match_percent = 0
    else:
        match_percent = int((len(matched) / len(required_skills)) * 100)

    return match_percent, matched, missing 
