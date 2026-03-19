from ai_engine.skill_extractor import extract_skills
from ai_engine.gap_analyzer import skill_gap, match_score
from ai_engine.learning_path import generate_path
from ai_engine.reasoning_engine import generate_explanation
from ai_engine.level_detector import detect_level


def analyze(resume_text, job_text):
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
        "level": level
    }