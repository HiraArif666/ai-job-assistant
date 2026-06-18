import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)


def run_agent(system_prompt, user_prompt):
    """Run a single agent with a system and user prompt"""
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ]
    response = llm.invoke(messages)
    return response.content


def job_analyzer_agent(job_description):
    """Agent 1: Analyzes the job description"""
    system_prompt = """You are an expert job analyst. Your job is to analyze job descriptions 
and extract structured information. Always respond in a clear, organized format."""

    user_prompt = f"""Analyze this job description and extract the following:

1. **Job Title & Company** (if mentioned)
2. **Required Technical Skills** (list all)
3. **Required Soft Skills** (list all)
4. **Experience Required**
5. **Key Responsibilities** (top 5)
6. **Important Keywords** for ATS (list 10-15 keywords)
7. **Nice to Have Skills** (if any)

Job Description:
{job_description}"""

    return run_agent(system_prompt, user_prompt)


def resume_tailor_agent(resume, job_analysis):
    """Agent 2: Tailors the resume to match the job"""
    system_prompt = """You are an expert resume writer and career coach with 10+ years of experience. 
You specialize in tailoring resumes to specific job descriptions to maximize ATS scores and interview chances."""

    user_prompt = f"""Based on the job analysis below, tailor this resume to match the job perfectly.

Instructions:
- Rewrite the summary to match the job requirements
- Highlight the most relevant skills and experiences
- Incorporate ATS keywords naturally
- Keep all facts accurate — do not invent experience
- Suggest which projects/skills to emphasize
- Format your response as the improved resume text

Job Analysis:
{job_analysis}

Original Resume:
{resume}"""

    return run_agent(system_prompt, user_prompt)


def cover_letter_agent(resume, job_description, job_analysis):
    """Agent 3: Writes a personalized cover letter"""
    system_prompt = """You are an expert cover letter writer. You write compelling, 
personalized cover letters that get candidates noticed. Your letters are professional 
yet genuine, and always tailored to the specific role."""

    user_prompt = f"""Write a professional cover letter for this job application.

Instructions:
- Keep it to 3-4 paragraphs
- Opening: hook the reader, mention the role
- Middle: connect experience to job requirements using specific examples
- Closing: call to action
- Tone: professional but personable
- Do NOT use generic phrases like "I am writing to express my interest"
- Use keywords from the job analysis naturally

Job Analysis:
{job_analysis}

Job Description:
{job_description}

Candidate Resume:
{resume}"""

    return run_agent(system_prompt, user_prompt)


def interview_prep_agent(job_analysis, resume):
    """Agent 4: Generates interview questions and answers"""
    system_prompt = """You are an expert interview coach with experience preparing candidates 
for technical and behavioral interviews. You know exactly what interviewers look for."""

    user_prompt = f"""Based on this job analysis and candidate resume, generate interview preparation material.

Provide:
1. **5 Technical Interview Questions** (based on required skills) with suggested answers
2. **5 Behavioral Interview Questions** (STAR format) with suggested answers based on candidate experience
3. **3 Questions the Candidate Should Ask** the interviewer
4. **Key Things to Emphasize** during the interview

Job Analysis:
{job_analysis}

Candidate Resume:
{resume}"""

    return run_agent(system_prompt, user_prompt)