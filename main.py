from flask import Flask, render_template, request
import fitz
from analyze_pdf import analyze_resume_gemini
import os
import re

app = Flask(__name__)

def extract_text_from_resume(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

@app.route('/', methods=['GET', 'POST'])
def index():
    result_text = None
    score = 0
    missing = []
    suggestions = ""
    summary = ""

    if request.method == 'POST':
        resume_file = request.files['resume']
        job_description = request.form['job_description']

        if resume_file and job_description:
            file_path = os.path.join('uploads', resume_file.filename)
            resume_file.save(file_path)

            resume_text = extract_text_from_resume(file_path)
            result_text = analyze_resume_gemini(resume_text, job_description)

            os.remove(file_path)

            # Extract info
            try:
                score_match = re.search(r"Match Score:\s*(\d+)", result_text)
                if score_match:
                    score = int(score_match.group(1))

                missing = re.findall(r"Missing Skills:\n((?:- .+\n)+)", result_text)
                if missing:
                    missing = [line.strip("- ").strip() for line in missing[0].splitlines()]

                suggestions_match = re.search(r"Suggestions:\n((?:- .+\n)+)", result_text)
                if suggestions_match:
                    suggestions = "\n".join([s.strip() for s in suggestions_match.group(1).strip().split("\n")])

                summary_match = re.search(r"Summary:\n(.+)", result_text, re.DOTALL)
                if summary_match:
                    summary = summary_match.group(1).strip()
            except Exception as e:
                print("Error parsing response:", e)

    return render_template('index.html', score=score, missing=missing,
                           suggestions=suggestions, summary=summary)

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.mkdir('uploads')
    app.run(debug=True)
