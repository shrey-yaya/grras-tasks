def recommend_job(skills):

    skills = [skill.lower() for skill in skills]

    # Machine Learning Engineer
    if "python" in skills and "machine learning" in skills:
        return {
            "role": "Machine Learning Engineer",
            "missing": ["Deep Learning", "NLP", "Statistics"],
            "timeline": "2-3 Months"
        }

    # Data Analyst
    elif "python" in skills and "sql" in skills:
        return {
            "role": "Data Analyst",
            "missing": ["Power BI", "Excel", "Statistics"],
            "timeline": "1-2 Months"
        }

    # Java Developer
    elif "java" in skills:
        return {
            "role": "Java Developer",
            "missing": ["Spring Boot", "Hibernate", "REST API"],
            "timeline": "2 Months"
        }

    # Web Developer
    elif "html" in skills or "css" in skills:
        return {
            "role": "Web Developer",
            "missing": ["JavaScript", "React", "Node.js"],
            "timeline": "2-3 Months"
        }

    # Default
    else:
        return {
            "role": "Software Developer",
            "missing": ["DSA", "Git", "Problem Solving"],
            "timeline": "3 Months"
        }