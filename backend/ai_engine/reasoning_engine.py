from ai_engine.learning_path import dependencies


def generate_explanation(gap, resume_skills, job_skills):
    explanations = []

    
    for skill in gap:
        if skill in dependencies:
            prereq = dependencies[skill][0]
            explanations.append(
                f"🔍 AI Analysis: The role requires {skill.title()}, but it is missing from your profile. "
                f"Based on skill dependencies, it is recommended to first learn {prereq.title()} before progressing to {skill.title()}."
            )
        else:
            explanations.append(
                f"⚠️ AI Insight: {skill.title()} is an important requirement for this role but is not present in your resume."
            )

    
    matched = set(resume_skills).intersection(set(job_skills))
    if matched:
        explanations.append(
            f"✅ AI Observation: You already demonstrate strong proficiency in {', '.join([m.title() for m in matched])}, which aligns well with the job requirements."
        )

    
    if gap:
        explanations.append(
            f"📊 AI Summary: To improve your match score, focus on learning the missing skills listed above. "
            f"Following the recommended learning path will significantly increase your job readiness."
        )
    else:
        explanations.append(
            f"🎉 AI Summary: Your profile is well aligned with the job requirements. You are a strong candidate for this role."
        )

    return explanations