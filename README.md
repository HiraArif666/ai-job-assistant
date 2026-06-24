# 💼 AI Job Application Assistant

A multi-agent AI system that automates and personalizes the entire job application process — from analyzing a job description to preparing you for the interview.

## 🚀 Live Demo
[Click here to try it](https://ai-job-assistant-595sba75nf4uliushzkedf.streamlit.app/)

## ✨ Features
- **4 specialized AI agents** working together in a pipeline
- Extracts required skills, keywords, and experience from any job description
- Tailors your resume to match the specific role
- Generates a personalized, role-specific cover letter
- Prepares technical and behavioral interview questions with suggested answers
- Live agent status updates while processing
- Downloadable output for every agent's result

## 🤖 How the Agents Work

| Agent | Role |
|---|---|
| 🔍 Job Analyzer | Extracts skills, experience level, responsibilities, and ATS keywords from the job description |
| 📄 Resume Tailor | Rewrites your resume to align with the job analysis |
| ✉️ Cover Letter Writer | Writes a personalized cover letter using your resume and the job description |
| 🎯 Interview Prep | Generates likely technical and behavioral interview questions with sample answers |

Each agent passes its output to the next, creating a complete pipeline:
```
Job Description ──▶ Job Analyzer ──▶ Resume Tailor ──▶ Cover Letter Writer
                            │
                            └──▶ Interview Prep
```

## 🛠️ Tech Stack
| Tool | Purpose |
|---|---|
| LangChain | Agent orchestration |
| Groq API | LLM inference (LLaMA 3.3 70B) |
| Streamlit | Web UI |
| Python | Core logic |

## ⚙️ Run Locally

1. Clone the repo
   ```bash
   git clone https://github.com/HiraArif666/ai-job-assistant.git
   cd ai-job-assistant
   ```

2. Create virtual environment
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Add your Groq API key in a `.env` file
   ```
   GROQ_API_KEY=your_key_here
   ```

5. Run the app
   ```bash
   streamlit run app.py
   ```

## 📸 How it Works
1. Paste your resume
2. Paste the job description
3. Click "Run All Agents"
4. Watch each agent complete its task in real time
5. View results across 4 tabs: Job Analysis, Tailored Resume, Cover Letter, Interview Prep
6. Download any output as a text file

## 🔑 Get a Free Groq API Key
Visit [console.groq.com](https://console.groq.com) to get your free API key.

## ⚠️ Note
This tool generates suggestions based on AI analysis. Always review and personalize outputs before submitting job applications.
