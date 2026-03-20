# 🚀 AI-Adaptive Onboarding Engine

## 📌 Problem Statement

Traditional onboarding systems follow a static approach, leading to inefficiency:

* Beginners feel overwhelmed
* Experienced users waste time

There is a need for an **intelligent, adaptive onboarding system**.

---

## 💡 Our Solution

We developed an **AI-Adaptive Onboarding Engine** that:

* Analyzes user resumes
* Identifies skill gaps
* Generates personalized learning paths
* Provides explainable AI insights

---

## 🧠 Key Features

### 🔹 1. Hybrid AI Skill Extraction

* Rule-based extraction for reliability
* AI-style semantic detection (ML → Machine Learning, etc.)
* Combines both for higher accuracy

---

### 🔹 2. Skill Gap Analysis

* Compares resume skills vs job requirements
* Identifies missing skills

---

### 🔹 3. Adaptive Learning Path

* Generates step-by-step roadmap
* Uses dependency graph (prerequisite-based learning)

---

### 🔹 4. Explainable AI (XAI)

* Provides human-like reasoning:

  * 🔍 AI Analysis
  * ⚠️ AI Insight
  * ✅ AI Observation
  * 📊 AI Summary

---

### 🔹 5. Dataset-Driven Intelligence

We used a real-world dataset to simulate job roles:

👉 https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset/data

**How we used it:**

* Generated job descriptions from categories
* Evaluated model performance
* Calculated match scores

---

### 🔹 6. Resume Upload (PDF + Text)

* Supports PDF and text resumes
* Automatic text extraction

---

### 🔹 7. Interactive UI Dashboard

* Match score visualization
* Skill tags (present vs missing)
* Learning path cards

---

## ⚙️ Tech Stack

### 🔹 Frontend

* React.js
* Custom CSS

### 🔹 Backend

* Flask (Python)
* REST API

### 🔹 AI Logic

* Hybrid AI (Rule-based + Semantic detection)
* Graph-based learning path
* Explainable reasoning engine

### 🔹 Libraries

* pandas → dataset processing
* PyPDF2 → PDF parsing

---

## 🧠 System Architecture

1. Resume Parsing
2. Skill Extraction (Hybrid AI)
3. Job Skill Generation (Dataset-driven)
4. Skill Gap Analysis
5. Learning Path Generation
6. Explainable AI Output

---

## 📊 Evaluation

We evaluated our system using a real-world dataset:

* Total Samples: ~900+ resumes
* Metrics:

  * Average Match Score
  * Max Score
  * Min Score

This demonstrates real-world applicability of the system.

---

## 🚀 How to Run

### 🔹 Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### 🔹 Frontend

```bash
cd frontend
npm install
npm start
```

---


## 🎯 Future Scope

* Integration with LLM APIs (OpenAI/Gemini)
* Real-time job recommendations
* Advanced NLP models (BERT)

---

## 🏆 Key Innovation

We designed a **Hybrid AI System** combining:

* Rule-based extraction (precision)
* Dataset-driven intelligence (real-world grounding)
* LLM-inspired reasoning (explainability)

---

## 📌 Conclusion

Our system transforms onboarding into an **intelligent, adaptive, and personalized experience**, making it scalable and efficient.

---

## 📄 License

Open-source for educational and hackathon use.
