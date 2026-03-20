
skills_db = [
    "python", "sql", "machine learning", "deep learning",
    "aws", "react", "data analysis",
    "html", "css", "javascript",
    "java", "oop", "spring",
    "docker", "ci/cd", "linux",
    "communication", "management", "leadership",
    "testing", "selenium", "excel"
]


skill_alias = {
    "ml": "machine learning",
    "dl": "deep learning",
    "js": "javascript"
}



def normalize_text(text):
    text = text.lower()
    for short, full in skill_alias.items():
        text = text.replace(short, full)
    return text



def extract_skills_rule(text):
    text = normalize_text(text)
    found = []

    for skill in skills_db:
        if skill in text:
            found.append(skill)

    return list(set(found))


def extract_skills_ai(text):
    text = text.lower()
    ai_skills = []

    if "machine learning" in text or "ml" in text:
        ai_skills.append("machine learning")

    if "deep learning" in text or "neural network" in text:
        ai_skills.append("deep learning")

    if "data analysis" in text or "analysis" in text:
        ai_skills.append("data analysis")

    if "cloud" in text or "aws" in text:
        ai_skills.append("aws")

    if "frontend" in text or "ui" in text:
        ai_skills.append("react")

    if "backend" in text:
        ai_skills.append("java")

    if "database" in text:
        ai_skills.append("sql")

    return list(set(ai_skills))



def extract_skills(text):
    rule_skills = extract_skills_rule(text)
    ai_skills = extract_skills_ai(text)

   
    return list(set(rule_skills + ai_skills))

def extract_skills_llm(text):
    return extract_skills(text)