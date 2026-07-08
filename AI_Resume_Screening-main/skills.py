SKILLS_DB = [
    "python",
    "java",
    "html",
    "css",
    "javascript",
    "mysql",
    "machine learning",
    "data analysis",
    "data preprocessing",
    "sql",
    "excel",
    "power bi",
    "c",
    "c++"
]

def extract_skills(text):

    found_skills = []

    text = text.lower()

    for skill in SKILLS_DB:

        if skill in text:
            found_skills.append(skill)

    return found_skills