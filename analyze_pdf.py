import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

configuration = {
    'temperature': 0.8,
    'top_p': 0.9,
    'top_k': 40,
    'max_output_tokens': 8192,
    'response_mime_type': "text/plain"
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=configuration
)

def analyze_resume_gemini(resume_content, job_description):
    prompt = f"""
You are a professional AI Resume Analyzer.

Analyze the candidate’s resume in comparison to the given job description.

------------------
RESUME:
{resume_content}

------------------
JOB DESCRIPTION:
{job_description}

------------------
TASK:
1. Calculate a match score (0-100) based on how well the resume fits the job.
2. List all missing or weakly represented skills from the resume.
3. Give 2-4 specific suggestions for improvement.
4. Summarize your analysis in 2-3 lines.

------------------
FORMAT (Strictly follow this structure):

Match Score: XX/100

Missing Skills:
- Skill 1
- Skill 2
- Skill 3

Suggestions:
- Suggestion 1
- Suggestion 2

Summary:
Write 2-3 lines summary here.

Only return plain text in this format.
    """

    response = model.generate_content(prompt)
    return response.text.strip()
