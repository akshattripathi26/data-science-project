import streamlit as st
import pandas as pd

# Fallback for Plotly if package is installing/missing
try:
    import plotly.express as px
    HAS_PLOTLY = True
except ImportError:
    HAS_PLOTLY = False

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
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
        "role": "Project Lead & Data Engineer Intern",
        "company": "System Innovations",
        "location": "Remote / Houston, TX",
        "period": "May 2026 - Aug 2026",
        "domain": "AI & Data Engineering",
        "highlights": [
            "Led end-to-end delivery of ScholarIE Engen, an AI-powered student application coaching platform managing stakeholder communication, sprint planning, and cross-functional coordination.",
            "Collaborated with AI engineers on system architecture design and data management strategy to build an AI agent replicating student counselor interactions at scale."
        ]
    },
    {
        "role": "Senior Analyst, Advisory Department",
        "company": "KPMG",
        "location": "India",
        "period": "Jan 2024 - Nov 2024",
        "domain": "Management Consulting",
        "highlights": [
            "Analyzed finance, operations, and logistics processes for Fortune 500 clients to identify revenue enhancement opportunities and recommend digital transformation initiatives.",
            "Partnered with finance, marketing, and procurement stakeholders to break down ambiguous business problems into actionable recommendations.",
            "Resolved high-impact client issues through root-cause analysis, earning Employee of the Quarter recognition."
        ]
    },
    {
        "role": "Marketing Associate",
        "company": "LogiNext",
        "location": "India",
        "period": "Aug 2022 - Oct 2023",
        "domain": "Go-To-Market & SaaS",
        "highlights": [
            "Ran customer and market discovery across North and South America, qualifying enterprise accounts (BANT) to inform GTM positioning.",
            "Converted a strategic account into $100,000 ARR by aligning solution value with customer workflows in collaboration with sales and solution teams.",
            "Gathered voice-of-customer signals at NRF Retail and Parcel Forum to refine messaging and outreach."
        ]
    },
    {
        "role": "Account Based Marketing Intern",
        "company": "HighRadius",
        "location": "India",
        "period": "May 2021 - Jul 2022",
        "domain": "Fintech & Strategy",
        "highlights": [
            "Mapped order-to-cash journeys and connected fintech capabilities to customer needs across credit, collections, and cash application.",
            "Ranked 8th out of 50 interns in finance solution training.",
            "Launched targeted ABM campaigns segmenting accounts to generate an opportunity pipeline of $500 million."
        ]
    }
]

education = [
    {
        "degree": "Master of Science in Engineering Management and Leadership",
        "institution": "Rice University",
        "location": "Houston, TX",
        "period": "Aug 2025 - Dec 2026",
        "details": "Courses: Project Management, Product Management, Engineering Leadership, Data Science, Data Visualization, Lean 6 Sigma."
    },
    {
        "degree": "Bachelor of Technology in Electronics and Communication",
        "institution": "SRM Institute of Science and Technology",
        "location": "India",
        "period": "May 2018 - May 2022",
        "details": "GPA: 3.87 / 4.00"
    }
]

academic_projects = [
    {
        "title": "Planned Delivery Predictive Model",
        "desc": "Built a linear regression forecasting model using historical data to optimize operational planning and delivery predictability."
    },
    {
        "title": "Lean Process Optimization for Shutdown Duration",
        "desc": "Applied Lean 6 Sigma principles to identify process inefficiencies and significantly reduce planned facility shutdown duration."
    },
    {
        "title": "Racquet Buddy (Industry 4.0)",
        "desc": "Developed a smart connected technology framework using Industry 4.0 concepts to track and enhance player performance."
    }
]

certifications = [
    "IBM Applied AI Certificate",
    "Lean Green Belt Certification",
    "Six Sigma Green Belt Certification",
    "KPMG Rising Star Award",
    "Rice Merit Scholarship ($20,000)"
]

skills_data = {
    "Category": ["Programming", "Programming", "Programming", "GTM & CRM", "GTM & CRM", "GTM & CRM", "Project Management", "Project Management", "Domain Expertise", "Domain Expertise", "Domain Expertise"],
    "Skill": ["Python", "C++", "C", "Salesforce", "HubSpot CRM", "LinkedIn Sales Nav", "Jira", "Asana", "Go-To-Market Strategy", "Data-Driven Analysis", "Stakeholder Mgmt"],
    "Proficiency": [90, 75, 70, 85, 90, 88, 85, 80, 95, 92, 95]
}

# -----------------------------------------------------------------------------
# SIDEBAR NAVIGATION
# -----------------------------------------------------------------------------
with st.sidebar:
    st.image("https://img.icons8.com/illustrations/100/user-male-circle.png", width=100)
    st.title("Akshat Tripathi")
    st.caption("Rice MS Engineering Management")
    
    page = st.radio(
        "Navigate Portfolio",
        ["Overview", "Work Experience", "Education & Projects", "Skills & Certifications", "Impact Analytics Dashboard", "Contact"]
    )
    
    st.divider()
    st.markdown("**Quick Info**")
    st.markdown("📍 Houston, TX")
    st.markdown("🎓 Rice University (MS)")
    st.markdown("💼 Ex-KPMG Advisory")

# -----------------------------------------------------------------------------
# PAGE 1: OVERVIEW
# -----------------------------------------------------------------------------
if page == "Overview":
    st.markdown(f"<div class='main-header'>{profile_info['name']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='sub-header'>{profile_info['title']}</div>", unsafe_allow_html=True)
    
    st.write(profile_info['summary'])
    st.divider()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="ABM Pipeline Generated", value="$500M", delta="HighRadius")
    with col2:
        st.metric(label="ARR Converted", value="$100K", delta="LogiNext")
    with col3:
        st.metric(label="Undergrad GPA", value="3.87 / 4.0", delta="SRM IST")
    with col4:
        st.metric(label="Merit Scholarship", value="$20,000", delta="Rice University")

    st.subheader("Core Competencies")
    cols = st.columns(3)
    cols[0].markdown("**Data & Engineering**\n- Python & Predictive Modeling\n- AI Agent Architecture\n- Lean & Six Sigma Analysis")
    cols[1].markdown("**Strategy & Advisory**\n- Go-to-Market (GTM) Strategy\n- Enterprise Discovery & BANT\n- Process Optimization")
    cols[2].markdown("**Leadership & Management**\n- Stakeholder Engagement\n- Agile & Sprint Planning\n- Cross-Functional Teams")

# -----------------------------------------------------------------------------
# PAGE 2: WORK EXPERIENCE
# -----------------------------------------------------------------------------
elif page == "Work Experience":
    st.title("💼 Professional Experience")
    
    selected_domain = st.selectbox("Filter by Domain", ["All"] + list(set([e['domain'] for e in experiences])))
    
    for exp in experiences:
        if selected_domain == "All" or exp['domain'] == selected_domain:
            with st.container():
                st.markdown(f"""
                <div class='card'>
                    <div class='card-title'>{exp['role']}</div>
                    <div class='card-subtitle'>{exp['company']} | {exp['location']} ({exp['period']})</div>
                </div>
                """, unsafe_allow_html=True)
                for h in exp['highlights']:
                    st.write(f"• {h}")
                st.write("")

# -----------------------------------------------------------------------------
# PAGE 3: EDUCATION & PROJECTS
# -----------------------------------------------------------------------------
elif page == "Education & Projects":
    st.title("🎓 Education & Academic Engineering Projects")
    
    st.subheader("Education")
    for edu in education:
        st.markdown(f"**{edu['degree']}** — *{edu['institution']}* ({edu['period']})")
        st.caption(f"{edu['location']} | {edu['details']}")
        st.write("")
        
    st.divider()
    st.subheader("Featured Engineering & Data Projects")
    p_cols = st.columns(3)
    for idx, proj in enumerate(academic_projects):
        with p_cols[idx]:
