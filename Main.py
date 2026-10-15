import streamlit as st
import pandas as pd

# Optional import handling to prevent app crashes if requirements are still installing
try:
    import plotly.express as px
    HAS_PLOTLY = True
except ImportError:
    HAS_PLOTLY = False

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION (Must be the first Streamlit command)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Akshat Tripathi | Interactive Portfolio & Executive Dashboard",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# CUSTOM CSS STYLING
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    .main-header {
        font-size: 2.4rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 0rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #475569;
        margin-bottom: 1.5rem;
    }
    .card {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 1.25rem;
        margin-bottom: 1rem;
    }
    .card-title {
        font-size: 1.15rem;
        font-weight: 600;
        color: #1E293B;
    }
    .card-subtitle {
        font-size: 0.9rem;
        color: #2563EB;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    .skill-tag {
        background-color: #EFF6FF;
        color: #1D4ED8;
        border: 1px solid #BFDBFE;
        padding: 4px 10px;
        border-radius: 15px;
        font-size: 0.85rem;
        font-weight: 500;
        display: inline-block;
        margin: 3px;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# DATA DEFINITIONS
# -----------------------------------------------------------------------------
profile_info = {
    "name": "Akshat Tripathi",
    "title": "Engineering Management Graduate | Consulting, Data Strategy & Go-To-Market",
    "email": "akshat.tripathi26@gmail.com",
    "phone": "(281) 779-7677",
    "linkedin": "https://linkedin.com/in/akshat-tripathi-",
    "summary": (
        "Engineering Management graduate student at Rice University with experience across "
        "consulting, go-to-market strategy, and data-driven problem solving in SaaS and advisory environments. "
        "Proven ability to analyze complex business problems, lead cross-functional teams, and deliver actionable "
        "recommendations that generate measurable impact."
    )
}

experiences = [
    {
        "role": "Teaching Assistant - RCEL 506: Data Science for Engineering Leaders",
        "company": "Rice University",
        "location": "Houston, TX",
        "period": "Aug 2026 - Dec 2026",
        "domain": "Academia & Data Science",
        "highlights": [
            "Support graduate-level course introducing statistical and computational methods to engineering managers; delivered classification lecture and updated GitHub course datasets.",
            "Lead GitHub workshops to build student data science fluency and contribute to course development including potential ASEE conference paper co-authorship."
        ]
    },
    {
        "role": "Project Lead & Data Engineer
