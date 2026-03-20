
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


def extract_skills(text):
    text = normalize_text(text)
    found = []

    for skill in skills_db:
        if skill in text:
            found.append(skill)

    return list(set(found))


def extract_skills_llm(text):
    return extract_skills(text)