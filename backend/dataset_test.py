import pandas as pd
from ai_engine.main_engine import analyze



df = pd.read_csv("Resume.csv")

results = []
scores = []



job_roles = {
    "Data Science": "Looking for Python, Machine Learning, Data Analysis, Deep Learning",
    "Web Designing": "Looking for HTML, CSS, JavaScript, React",
    "HR": "Looking for communication, management, hiring, leadership",
    "Java Developer": "Looking for Java, OOP, Spring, SQL",
    "DevOps": "Looking for AWS, Docker, CI/CD, Linux",
    "Testing": "Looking for testing, automation, Selenium",
    "Business Analyst": "Looking for data analysis, SQL, Excel"
}


print("\n🚀 Running AI Evaluation on Resume Dataset...\n")



for i, row in df.iterrows():
    resume = str(row["Resume_str"])
    category = str(row["Category"]).strip()

    
    job = job_roles.get(
        category,
        "Looking for Python, SQL, Machine Learning, Data Analysis"
    )

    output = analyze(resume, job)

    results.append(output)
    scores.append(output["match_score"])

   
    if i < 3:
        print(f"\n--- Sample {i+1} ---")
        print("Category:", category)
        print("Generated Job:", job)
        print("Match Score:", round(output["match_score"], 2))
        print("Gap:", output["gap"])



avg_score = sum(scores) / len(scores)

print("\n📊 FINAL EVALUATION")
print("Total Samples:", len(scores))
print("Average Match Score:", round(avg_score, 3))
print("Max Score:", round(max(scores), 3))
print("Min Score:", round(min(scores), 3))