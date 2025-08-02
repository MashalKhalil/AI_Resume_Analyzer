
# 🤖 AI Resume Analyzer

AI-powered resume analyzer that evaluates a candidate's resume against a job description using Google's Gemini API. It provides a visual match score, missing keywords, suggestions for improvement, and a concise summary — all through a clean and simple Flask web app.

---

## 🔍 Features

- 📄 Upload your resume (PDF)
- 🧠 Paste a job description
- ✅ Get:
  - **Match Score** out of 100
  - **Missing Skills**
  - **Improvement Suggestions**
  - **Summary Analysis**

---


## 🛠️ Tech Stack

- Python (Flask)
- Google Gemini API (via `google-generativeai`)
- PyMuPDF for PDF parsing
- Bootstrap 5 for UI
- Render (Deployment)

---

## 📁 Project Structure

```
resume-analyzer/
│
├── main.py                # Flask App
├── analyze_pdf.py         # Gemini API logic
├── requirements.txt       # Dependencies
├── .env                   # Gemini API Key (not committed)
├── templates/
│   └── index.html         # HTML Frontend
└── uploads/               # Temporary resume storage
```

---

## 🧪 How to Run Locally

1. **Clone the repo**
```bash
git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Add `.env` file**
```
GEMINI_API_KEY=your_gemini_api_key_here
```

4. **Run the app**
```bash
python main.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

### Required environment variable:

| Key            | Value                  |
|----------------|------------------------|
| `GEMINI_API_KEY` | your Gemini API key   |

Start Command: `python main.py`

---
