# -------------------------------
# SKILL DATABASE + ALIAS
# -------------------------------

from google import genai

client = genai.Client(api_key="")



skills_db = [
    "python", "sql", "machine learning", "deep learning",
    "aws", "react", "data analysis"
]

skill_alias = {
    "ml": "machine learning",
    "dl": "deep learning",
    "js": "javascript"
}

# -------------------------------
# STEP 1: SKILL EXTRACTION
# -------------------------------

import ast

def extract_skills_llm(text):
    try:
        prompt = f"""
        Extract technical skills from the following text.
        Return ONLY a Python list.

        Text:
        {text}
        """

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        return ast.literal_eval(response.text)

    except Exception as e:
        print("⚠️ Gemini failed, using fallback...")

        # Fallback (mock intelligent output)
        return extract_skills(text)

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


# -------------------------------
# STEP 2: SKILL GAP
# -------------------------------

def skill_gap(resume_skills, job_skills):
    return list(set(job_skills) - set(resume_skills))


# -------------------------------
# STEP 3: COURSE MAP
# -------------------------------

course_map = {
    "python": ["Python Basics", "OOP", "Projects"],
    "machine learning": ["ML Basics", "Regression", "Model Evaluation"],
    "deep learning": ["Neural Networks", "CNN"],
    "aws": ["Cloud Basics", "EC2", "S3"],
    "react": ["React Basics", "Hooks", "Projects"]
}

# -------------------------------
# STEP 4: DEPENDENCIES (SMART LOGIC)
# -------------------------------

dependencies = {
    "deep learning": ["machine learning"],
    "machine learning": ["python"]
}


def resolve_dependencies(skill, visited, order):
    if skill in visited:
        return

    visited.add(skill)

    for dep in dependencies.get(skill, []):
        resolve_dependencies(dep, visited, order)

    order.append(skill)


def generate_path(gap):
    visited = set()
    order = []

    for skill in gap:
        resolve_dependencies(skill, visited, order)

    path = {}

    for skill in order:
        path[skill] = course_map.get(skill, ["Learn basics"])

    return path


# -------------------------------
# STEP 5: MATCH SCORE
# -------------------------------

def match_score(resume_skills, job_skills):
    if len(job_skills) == 0:
        return 0
    return round(len(set(resume_skills) & set(job_skills)) / len(job_skills), 2)


# -------------------------------
# STEP 6: EXPLANATION GENERATOR
# -------------------------------

def generate_explanation(gap):
    explanations = []

    for skill in gap:
        if skill in dependencies:
            prereq = dependencies[skill][0]
            explanations.append(
                f"{skill.title()} requires {prereq.title()} first."
            )
        else:
            explanations.append(f"You need to learn {skill.title()}.")

    return explanations


# -------------------------------
# FINAL PIPELINE
# -------------------------------

def analyze(resume_text, job_text):
    # Rule-based
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    # LLM-based (Gemini)
    resume_llm = extract_skills_llm(resume_text)
    job_llm = extract_skills_llm(job_text)

    gap = skill_gap(resume_skills, job_skills)
    learning_path = generate_path(gap)
    score = match_score(resume_skills, job_skills)
    explanation = generate_explanation(gap)

    return {
        "resume_skills_rule": resume_skills,
        "resume_skills_llm": resume_llm,
        "job_skills_rule": job_skills,
        "job_skills_llm": job_llm,
        "match_score": score,
        "gap": gap,
        "learning_path": learning_path,
        "explanation": explanation
    }


# -------------------------------
# TEST CASE
# -------------------------------

if __name__ == "__main__":
    resume = "I know Python, SQL and ML"
    job = "Looking for Machine Learning and Deep Learning engineer with AWS"

    result = analyze(resume, job)

    from pprint import pprint
    pprint(result)
