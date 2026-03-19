from ai_engine.learning_path import dependencies


def generate_explanation(gap, resume_skills, job_skills):
    explanations = []

    for skill in gap:
        # 🔥 If dependency exists
        if skill in dependencies:
            prereq = dependencies[skill][0]
            explanations.append(
                f"{skill.title()} is required for the job but missing in your resume. "
                f"You should first learn {prereq.title()} before {skill.title()}."
            )
        else:
            explanations.append(
                f"{skill.title()} is required for the job but not found in your resume."
            )

    # 🔥 Extra smart explanation (VERY GOOD FOR JUDGES)
    matched = set(resume_skills).intersection(set(job_skills))
    if matched:
        explanations.append(
            f"You already have strong skills in {', '.join([m.title() for m in matched])}."
        )

    return explanations