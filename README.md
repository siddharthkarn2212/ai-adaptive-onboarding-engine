# 🚀 AI-Adaptive Onboarding Engine

## 📌 Problem Statement

Traditional onboarding systems use a one-size-fits-all approach, leading to inefficiency:

* Beginners feel overwhelmed
* Experienced users waste time

## 💡 Our Solution

We built an **AI-Adaptive Onboarding Engine** that:

* Understands user skills from resume
* Compares with job requirements
* Identifies skill gaps
* Generates a personalized learning roadmap

---

## 🔥 Key Features

### 🧠 Intelligent Skill Extraction

* Extracts skills from Resume (PDF/TXT)
* Extracts required skills from Job Description

### 📊 Skill Gap Analysis

* Compares user skills vs job requirements
* Identifies missing skills

### 📚 Adaptive Learning Path

* Generates step-by-step roadmap
* Includes prerequisite-based learning (Graph logic)

### 🧠 Explainable AI (Reasoning Trace)

* Explains WHY a skill is missing
* Suggests what to learn first

### 🎯 Experience Level Detection

* Beginner / Intermediate / Advanced classification

### 🌐 User-Friendly Interface

* Upload resume (PDF/TXT)
* Paste or auto-generate job role
* Visual dashboard with results

---

## ⚙️ Tech Stack

### Frontend

* React.js
* HTML/CSS (custom styling)

### Backend

* Flask (Python)
* REST API

### AI Logic

* Rule-based NLP + reasoning engine
* Graph-based dependency mapping

### Libraries

* PyPDF2 (PDF parsing)
* Pandas (dataset processing)

---

## 📊 Dataset Used

We used the Kaggle Resume Dataset for validation:

👉 https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset/data

### Dataset Features:

* Resume text data across multiple domains
* Job categories (Data Science, Web, HR, etc.)
* Real-world resume structure

### Usage:

* Evaluated model performance
* Simulated job-role matching
* Calculated average match score

---

## 🧠 How It Works

1. Resume Parsing
2. Skill Extraction
3. Job Skill Extraction
4. Skill Gap Identification
5. Learning Path Generation
6. Reasoning Explanation

---

## 📈 Evaluation

* Tested on real-world dataset
* Average match score calculated
* Improved accuracy via skill expansion

---

## 🚀 Run Locally

### Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend

```bash
cd frontend
npm install
npm start
```

---

## 🎥 Demo Video

(upload later)

---

## 📊 Future Improvements

* Advanced ML/NLP models (BERT, LLM)
* Real-time recommendation engine
* Integration with job portals

---

## 👨‍💻 Team

* AI/ML Engineer: Core Logic & System Design
