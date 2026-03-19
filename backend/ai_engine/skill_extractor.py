# -------------------------------
# SKILL DATABASE + ALIAS
# -------------------------------
skills_db = [
    "python", "sql", "machine learning", "deep learning",
    "aws", "react", "data analysis",
    
    # 🔥 NEW ADDITIONS
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

# -------------------------------
# NORMALIZE TEXT
# -------------------------------

def normalize_text(text):
    text = text.lower()
    for short, full in skill_alias.items():
        text = text.replace(short, full)
    return text


# -------------------------------
# RULE-BASED EXTRACTION
# -------------------------------

def extract_skills(text):
    text = normalize_text(text)
    found = []

    for skill in skills_db:
        if skill in text:
            found.append(skill)

    return list(set(found))


# -------------------------------
# LLM EXTRACTION (FALLBACK)
# -------------------------------

def extract_skills_llm(text):
    # fallback (Gemini optional)
    return extract_skills(text)