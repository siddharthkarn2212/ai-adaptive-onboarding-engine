from ai_engine.skill_extractor import extract_skills
from ai_engine.gap_analyzer import skill_gap, match_score
from ai_engine.learning_path import generate_path
from ai_engine.reasoning_engine import generate_explanation
from ai_engine.level_detector import detect_level



def generate_job_from_resume(resume_text):
    text = resume_text.lower()

    if "machine learning" in text or "data" in text:
        return "Looking for Python, Machine Learning, Data Analysis, Deep Learning"

    elif "web" in text or "frontend" in text:
        return "Looking for HTML, CSS, JavaScript, React"

    elif "java" in text:
        return "Looking for Java, Spring, SQL"

    elif "management" in text or "communication" in text:
        return "Looking for Communication, Leadership, Management"

    else:
        return "Looking for Python, SQL, Communication"



def analyze(resume_text, job_text):
    
    
    if not job_text or job_text.strip() == "":
        job_text = generate_job_from_resume(resume_text)

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    gap = skill_gap(resume_skills, job_skills)
    path = generate_path(gap)
    score = match_score(resume_skills, job_skills)
    explanation = generate_explanation(gap, resume_skills, job_skills)
    level = detect_level(resume_text)

    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "gap": gap,
        "learning_path": path,
        "match_score": score,
        "explanation": explanation,
        "level": level,
        "generated_job": job_text   
    }