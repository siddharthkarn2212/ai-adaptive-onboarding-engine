from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_engine.main_engine import analyze
from utils.file_parser import extract_text_from_pdf

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "API is running 🚀"


@app.route("/analyze", methods=["POST"])
def analyze_api():
    try:
        resume_text = ""
        job = ""

        # ✅ CASE 1: FILE UPLOAD (PDF or TXT)
        if "file" in request.files:
            file = request.files["file"]

            # Debug
            print("File received:", file.filename)

            if file.filename.endswith(".pdf"):
                resume_text = extract_text_from_pdf(file)
            else:
                resume_text = file.read().decode("utf-8")

            job = request.form.get("job", "")

        # ✅ CASE 2: JSON INPUT
        else:
            data = request.get_json()
            resume_text = data.get("resume", "")
            job = data.get("job", "")

        # Debug check
        print("Resume length:", len(resume_text))
        print("Job:", job)

        result = analyze(resume_text, job)

        return jsonify(result)

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)