import streamlit as st
from agents import (
    job_analyzer_agent,
    resume_tailor_agent,
    cover_letter_agent,
    interview_prep_agent
)

st.set_page_config(
    page_title="AI Job Assistant",
    page_icon="💼",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
        .stApp {
            background-color: #0f1117;
            color: #ffffff;
        }
        [data-testid="stSidebar"] {
            background-color: #1a1d27;
            border-right: 1px solid #2e3250;
        }
        [data-testid="stAlert"] {
            border-radius: 10px;
        }
        [data-testid="stTextArea"] textarea {
            background-color: #1e2130;
            color: #ffffff;
            border: 1px solid #2e3250;
            border-radius: 10px;
        }
        h1 {
            color: #7c83fd;
            font-size: 2rem;
            font-weight: 700;
        }
        h3 {
            color: #7c83fd;
        }
        hr {
            border-color: #2e3250;
        }
        .agent-box {
            background-color: #1e2130;
            border-radius: 12px;
            padding: 20px;
            border: 1px solid #2e3250;
            margin-bottom: 15px;
        }
        .stTabs [data-baseweb="tab"] {
            color: #aaaaaa;
        }
        .stTabs [aria-selected="true"] {
            color: #7c83fd;
            border-bottom-color: #7c83fd;
        }
    </style>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 💼 AI Job Assistant")
    st.markdown("---")
    st.markdown("### 🤖 4 AI Agents")
    st.markdown("""
    **Agent 1 — Job Analyzer**
    Extracts skills, keywords & requirements

    **Agent 2 — Resume Tailor**
    Rewrites your resume for the job

    **Agent 3 — Cover Letter Writer**
    Writes a personalized cover letter

    **Agent 4 — Interview Prep**
    Generates questions & answers
    """)
    st.markdown("---")
    st.markdown("### ℹ️ How to use")
    st.markdown("""
    1. Paste your resume
    2. Paste the job description
    3. Click Run All Agents
    4. Get everything you need!
    """)
    st.markdown("---")
    st.markdown("Built with LangChain + Groq + LLaMA 3.3 70B")

# ── Main Area ─────────────────────────────────────────────
st.markdown("# 💼 AI Job Application Assistant")
st.markdown("Let 4 AI agents work together to supercharge your job application.")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    resume = st.text_area(
        "📄 Paste Your Resume",
        height=300,
        placeholder="Paste your full resume text here..."
    )

with col2:
    job_description = st.text_area(
        "💼 Paste Job Description",
        height=300,
        placeholder="Paste the full job description here..."
    )

st.markdown("---")

col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    run_btn = st.button("🚀 Run All Agents", use_container_width=True)

# ── Run Agents ────────────────────────────────────────────
if run_btn:
    if not resume or not job_description:
        st.warning("⚠️ Please paste both your resume and the job description!")
    else:
        # Agent 1
        with st.status("🔍 Agent 1: Analyzing job description...", expanded=True) as status:
            job_analysis = job_analyzer_agent(job_description)
            st.session_state.job_analysis = job_analysis
            status.update(label="✅ Agent 1: Job analysis complete!", state="complete")

        # Agent 2
        with st.status("📝 Agent 2: Tailoring your resume...", expanded=True) as status:
            tailored_resume = resume_tailor_agent(resume, job_analysis)
            st.session_state.tailored_resume = tailored_resume
            status.update(label="✅ Agent 2: Resume tailored!", state="complete")

        # Agent 3
        with st.status("✉️ Agent 3: Writing cover letter...", expanded=True) as status:
            cover_letter = cover_letter_agent(resume, job_description, job_analysis)
            st.session_state.cover_letter = cover_letter
            status.update(label="✅ Agent 3: Cover letter ready!", state="complete")

        # Agent 4
        with st.status("🎯 Agent 4: Preparing interview questions...", expanded=True) as status:
            interview_prep = interview_prep_agent(job_analysis, resume)
            st.session_state.interview_prep = interview_prep
            status.update(label="✅ Agent 4: Interview prep ready!", state="complete")

        st.success("🎉 All agents done! Scroll down to see your results.")

# ── Display Results ───────────────────────────────────────
if "job_analysis" in st.session_state:
    st.markdown("---")
    st.markdown("## 📊 Results")

    tab1, tab2, tab3, tab4 = st.tabs([
        "🔍 Job Analysis",
        "📄 Tailored Resume",
        "✉️ Cover Letter",
        "🎯 Interview Prep"
    ])

    with tab1:
        st.markdown(st.session_state.job_analysis)
        st.download_button(
            "📥 Download Job Analysis",
            st.session_state.job_analysis,
            file_name="job_analysis.txt",
            use_container_width=True
        )

    with tab2:
        st.markdown(st.session_state.tailored_resume)
        st.download_button(
            "📥 Download Tailored Resume",
            st.session_state.tailored_resume,
            file_name="tailored_resume.txt",
            use_container_width=True
        )

    with tab3:
        st.markdown(st.session_state.cover_letter)
        st.download_button(
            "📥 Download Cover Letter",
            st.session_state.cover_letter,
            file_name="cover_letter.txt",
            use_container_width=True
        )

    with tab4:
        st.markdown(st.session_state.interview_prep)
        st.download_button(
            "📥 Download Interview Prep",
            st.session_state.interview_prep,
            file_name="interview_prep.txt",
            use_container_width=True
        )