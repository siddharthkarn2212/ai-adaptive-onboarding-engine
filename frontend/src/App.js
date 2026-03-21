import React, { useState } from "react";

function App() {
  const [resume, setResume] = useState("");
  const [job, setJob] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [selectedFile, setSelectedFile] = useState(null);

  const handleAnalyze = async () => {
    try {
      setLoading(true);

      let finalJob = job;

      if (!job || job.trim() === "") {
        finalJob =
          "Looking for Python, Machine Learning, Data Analysis, AWS";
        setJob(finalJob);
      }

      let res;

      if (selectedFile) {
        const formData = new FormData();
        formData.append("file", selectedFile);
        formData.append("job", finalJob);

        res = await fetch("http://127.0.0.1:5000/analyze", {
          method: "POST",
          body: formData,
        });
      } else {
        res = await fetch("http://127.0.0.1:5000/analyze", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ resume, job: finalJob }),
        });
      }

      const data = await res.json();
      setResult(data);
    } catch (err) {
      console.error("Error:", err);
      alert("Backend not running or error occurred");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.bg}>
      <div style={styles.card}>
        <h1 style={styles.title}>🚀 AI-Adaptive Onboarding Engine</h1>
        <p style={styles.subtitle}>
          AI-powered personalized onboarding & skill gap intelligence
        </p>

        {/* FILE */}
        <input
          type="file"
          accept=".pdf,.txt"
          onChange={(e) => {
            const file = e.target.files[0];
            setSelectedFile(file);

            if (file && file.type === "text/plain") {
              const reader = new FileReader();
              reader.onload = (event) => setResume(event.target.result);
              reader.readAsText(file);
            }
          }}
          style={styles.input}
        />

        {/* RESUME */}
        <textarea
          placeholder="Paste Resume..."
          value={resume}
          onChange={(e) => setResume(e.target.value)}
          rows={4}
          style={styles.textarea}
        />

        {/* JOB */}
        <textarea
          placeholder="Paste Job Description..."
          value={job}
          onChange={(e) => setJob(e.target.value)}
          rows={4}
          style={styles.textarea}
        />

        {/* BUTTON */}
        <button onClick={handleAnalyze} style={styles.button}>
          {loading ? "⏳ Analyzing..." : "Analyze"}
        </button>

        {/* SAMPLE */}
        <button
          onClick={() => {
            setResume(
              "I have experience in Python, Machine Learning, and Data Analysis"
            );
            setJob(
              "Looking for Python, Machine Learning, AWS, and Data Analysis"
            );
            setSelectedFile(null);
          }}
          style={styles.sampleBtn}
        >
          Use Sample Data
        </button>

        {/* LOADING */}
        {loading && (
          <div style={styles.loading}>🔄 AI is analyzing...</div>
        )}

        {/* EMPTY */}
        {!result && !loading && (
          <div style={styles.empty}>
            💡 Upload resume or use sample data
          </div>
        )}

        {/* RESULT */}
        {result && !loading && (
          <div style={styles.resultBox}>
            {/* MATCH */}
            <div style={styles.section}>
              <h3>📊 Match Score</h3>
              <div style={styles.progressBar}>
                <div
                  style={{
                    ...styles.progressFill,
                    width: `${(result.match_score || 0) * 100}%`,
                  }}
                />
              </div>
              <h2 style={styles.score}>
                {((result.match_score || 0) * 100).toFixed(0)}%
              </h2>
            </div>

            {/* LEVEL */}
            <div style={styles.section}>
              <h4>🎯 Experience Level</h4>
              <p style={styles.level}>{result.level || "N/A"}</p>
            </div>

            {/* SKILLS */}
            <div style={styles.section}>
              <h4>✅ Your Skills</h4>
              {(result.resume_skills || []).map((s, i) => (
                <span key={i} style={styles.skill}>
                  {s}
                </span>
              ))}
            </div>

            {/* GAP */}
            <div style={styles.section}>
              <h4>❌ Missing Skills</h4>
              {(result.gap || []).map((s, i) => (
                <span key={i} style={styles.missing}>
                  {s}
                </span>
              ))}
            </div>

            {/* LEARNING PATH */}
            <div style={styles.section}>
              <h4>📚 Learning Path</h4>
              {result.learning_path &&
                Object.entries(result.learning_path).map(
                  ([skill, steps]) => (
                    <div key={skill} style={styles.pathCard}>
                      <b>{skill}</b>
                      {steps.map((step, i) => (
                        <div key={i}>👉 {step}</div>
                      ))}
                    </div>
                  )
                )}
            </div>

            {/* AI REASONING */}
            <div style={styles.section}>
              <h4>🧠 AI Reasoning</h4>
              <ul>
                {(result.explanation || []).map((e, i) => (
                  <li key={i}>{e}</li>
                ))}
              </ul>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

const styles = {
  bg: {
    minHeight: "100vh",
    background: "linear-gradient(135deg, #667eea, #764ba2)",
    padding: "40px",
    fontFamily: "Arial",
  },

  card: {
    maxWidth: "850px",
    margin: "auto",
    background: "white",
    padding: "30px",
    borderRadius: "15px",
    boxShadow: "0 15px 40px rgba(0,0,0,0.2)",
  },

  title: {
    textAlign: "center",
    marginBottom: "5px",
  },

  subtitle: {
    textAlign: "center",
    color: "#666",
    marginBottom: "20px",
  },

  input: {
    width: "100%",
    padding: "10px",
    marginBottom: "10px",
    borderRadius: "8px",
  },

  textarea: {
    width: "100%",
    padding: "10px",
    marginBottom: "10px",
    borderRadius: "8px",
  },

  button: {
    width: "100%",
    padding: "12px",
    background: "#667eea",
    color: "white",
    border: "none",
    borderRadius: "8px",
    marginTop: "10px",
    cursor: "pointer",
  },

  sampleBtn: {
    width: "100%",
    padding: "10px",
    background: "#ddd",
    borderRadius: "8px",
    marginTop: "10px",
    cursor: "pointer",
  },

  loading: {
    textAlign: "center",
    marginTop: "15px",
  },

  empty: {
    textAlign: "center",
    marginTop: "15px",
    color: "#777",
  },

  resultBox: {
    marginTop: "25px",
  },

  section: {
    marginBottom: "20px",
  },

  progressBar: {
    height: "10px",
    background: "#ddd",
    borderRadius: "10px",
    overflow: "hidden",
  },

  progressFill: {
    height: "100%",
    background: "#667eea",
  },

  score: {
    color: "#667eea",
    marginTop: "10px",
  },

  level: {
    fontWeight: "bold",
  },

  skill: {
    background: "#38b2ac",
    color: "white",
    padding: "6px 12px",
    margin: "5px",
    borderRadius: "20px",
    display: "inline-block",
  },

  missing: {
    background: "#e53e3e",
    color: "white",
    padding: "6px 12px",
    margin: "5px",
    borderRadius: "20px",
    display: "inline-block",
  },

  pathCard: {
    background: "#f7fafc",
    padding: "10px",
    marginTop: "10px",
    borderRadius: "8px",
  },
};

export default App;