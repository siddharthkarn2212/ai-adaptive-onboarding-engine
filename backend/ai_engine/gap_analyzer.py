def skill_gap(resume_skills, job_skills):
    return list(set(job_skills) - set(resume_skills))


def match_score(resume_skills, job_skills):
    if len(job_skills) == 0:
        return 0
    return round(len(set(resume_skills) & set(job_skills)) / len(job_skills), 2)