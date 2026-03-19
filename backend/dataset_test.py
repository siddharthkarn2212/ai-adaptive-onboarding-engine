import pandas as pd
from ai_engine.main_engine import analyze

# Load dataset
df = pd.read_csv("Resume.csv")

results = []
scores = []

# 🔥 Better job-role to skills mapping
job_roles = {
    "Data Science": "Looking for Python, Machine Learning, Data Analysis, Deep Learning",
    "Web Designing": "Looking for HTML, CSS, JavaScript, React",
    "HR": "Looking for communication, management, hiring, leadership",
    "Java Developer": "Looking for Java, OOP, Spring, SQL",
    "DevOps": "Looking for AWS, Docker, CI/CD, Linux",
    "Testing": "Looking for testing, automation, Selenium",
    "Business Analyst": "Looking for data analysis, SQL, Excel"
}

# Loop through dataset
for i, row in df.iterrows():
    resume = str(row["Resume_str"])
    category = str(row["Category"]).strip()

    # ✅ Smart job generation
    job = job_roles.get(category, "Looking for Python, SQL, Machine Learning, Data Analysis")

    output = analyze(resume, job)

    results.append(output)
    scores.append(output["match_score"])

# Print one sample output
print("Sample Output:\n", results[0])

# Calculate average score
avg_score = sum(scores) / len(scores)
print("Average Match Score:", avg_score)