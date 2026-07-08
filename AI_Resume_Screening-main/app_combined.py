import streamlit as st
import pandas as pd

from resume_parser import extract_text_from_pdf
from skills import extract_skills
from scorer import calculate_score
from skill_match import get_skill_match
from career_gap import analyze_career_gap
from candidate_ranker import rank_candidates
from radar_chart import plot_radar

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)
st.markdown("""
<style>

/* Main Background */
.stApp {
    background-color: #0E1117;
}

/* Title */
.main-title {
    text-align:center;
    font-size:50px;
    font-weight:bold;
    color:#00E5FF;
}

/* Subtitle */
.subtitle {
    text-align:center;
    color:#B0BEC5;
    font-size:20px;
}

/* Cards */
.card {
    background-color:#1E293B;
    padding:20px;
    border-radius:15px;
    margin-bottom:15px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.3);
}

/* Feature Box */
.feature-box {
    background:linear-gradient(135deg,#00E5FF,#2979FF);
    color:white;
    padding:15px;
    border-radius:12px;
    margin:10px 0px;
}

/* Success */
.success-box {
    background:#0F5132;
    padding:15px;
    border-radius:12px;
    color:white;
}

/* Ranking Table */
[data-testid="stDataFrame"] {
    border:2px solid #00E5FF;
    border-radius:10px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color:#111827;
}

</style>
""", unsafe_allow_html=True)
# ---------------- SIDEBAR ----------------

st.markdown(
    """
    <div class='main-title'>
        🤖 SmartHire AI
    </div>
    <div class='subtitle'>
        AI-Powered Resume Screening & ATS Platform
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown(
"""
# 🤖 SmartHire AI

### Features

✅ Resume Analysis

✅ Skill Extraction

✅ Resume Scoring

✅ Career Gap Analysis

✅ ATS Candidate Ranking

✅ Multi Resume Screening
"""
)

with st.expander("👨‍🎓 Candidate Mode"):
    st.write("""
    • Resume Score
    • Skill Match Percentage
    • Career Readiness
    • Job Recommendation
    • Skill Gap Analysis
    """)

with st.expander("👨‍💼 Recruiter Mode"):
    st.write("""
    • Candidate Ranking
    • Top Candidate Identification
    • Shortlisted Candidates
    • ATS Dashboard
    """)

# ---------------- DREAM JOB ----------------

target_role = st.selectbox(
    "🎯 Select Dream Job",
    [
        "Machine Learning Engineer",
        "Data Analyst",
        "AI Engineer",
        "Software Developer"
    ]
)
# ---------------- MODE SELECTION ----------------

mode = st.radio(
    "🧑‍💼 Choose Mode",
    [
        "Candidate Analysis",
        "Recruiter ATS"
    ],
    horizontal=True
)

# ---------------- JOB SKILLS ----------------

JOB_SKILLS = [
    "python",
    "machine learning",
    "data analysis",
    "sql",
    "deep learning",
    "nlp",
    "statistics"
]

# ---------------- FILE UPLOAD ----------------

if mode == "Candidate Analysis":

    uploaded_files = st.file_uploader(
        "📄 Upload Resume",
        type=["pdf"],
        accept_multiple_files=False
    )

    if uploaded_files:
        uploaded_files = [uploaded_files]

else:

    uploaded_files = st.file_uploader(
        "📄 Upload Multiple Resumes",
        type=["pdf"],
        accept_multiple_files=True
    )

# ======================================================
# SINGLE RESUME MODE
# ======================================================

if uploaded_files:

    if mode == "Candidate Analysis":

        uploaded_file = uploaded_files[0]

        st.success("Resume uploaded successfully!")
        st.write("📁 File Name:", uploaded_file.name)

        resume_text = extract_text_from_pdf(uploaded_file)

        skills = extract_skills(resume_text)

        skills_lower = [
            s.lower().strip()
            for s in skills
        ]

        score = calculate_score(skills)

        match_percent, matched, missing = get_skill_match(
            skills_lower,
            JOB_SKILLS
        )

        readiness, gap_skills = analyze_career_gap(
            skills_lower,
            target_role
        )

        # Prediction

        if score >= 80:
            prediction = "Selected"

        elif score >= 60 and match_percent >= 50:
            prediction = "Selected"

        else:
            prediction = "Rejected"

        # Role Recommendation

        if (
            "machine learning" in skills_lower
            or
            "deep learning" in skills_lower
        ):
            role = "Machine Learning Engineer"

        elif (
            "data analysis" in skills_lower
            or
            "sql" in skills_lower
        ):
            role = "Data Analyst"

        elif "python" in skills_lower:
            role = "Python Developer"

        else:
            role = "Software Developer"

        # Category

        if score >= 80:
            category = "🏆 Excellent Candidate"

        elif score >= 60:
            category = "👍 Good Candidate"

        else:
            category = "⚠ Needs Improvement"

        # Suggestions

        suggestions = []

        if missing:
            suggestions.append(
                f"Learn missing skills: {', '.join(missing)}"
            )

        if len(skills_lower) < 5:
            suggestions.append(
                "Add more technical skills"
            )

        if score < 60:
            suggestions.append(
                "Improve resume content and project experience"
            )

        if not suggestions:
            suggestions.append(
                "🎉 Excellent Resume! Keep it up."
            )

        # ---------------- UI ----------------

        st.subheader("📊 Resume Score")
        st.progress(score / 100)
        st.write(f"{score}/100")

        st.subheader("🎯 Skill Match Percentage")
        st.progress(match_percent / 100)
        st.write(f"{match_percent}%")

        st.subheader("🚀 Career Readiness")
        st.progress(readiness / 100)
        st.write(f"{readiness}%")

        st.subheader("🏅 Candidate Category")
        st.info(category)

        st.subheader("🤖 Prediction")

        if prediction == "Selected":
            st.success("✅ Selected")
        else:
            st.error("❌ Rejected")

        st.subheader("💼 Recommended Role")
        st.info(role)

        # ---------------- Radar Chart ----------------

        st.subheader("📊 Skill Gap Radar Chart")

        skill_labels = [
            "Python",
            "SQL",
            "ML",
            "Deep Learning",
            "NLP"
        ]

        required_scores = [
            100,
            90,
            100,
            90,
            80
        ]

        user_scores = []

        for skill in skill_labels:

            if skill.lower() in skills_lower:
                user_scores.append(80)
            else:
                user_scores.append(20)

        fig = plot_radar(
            user_scores.copy(),
            required_scores.copy(),
            skill_labels,
            "Resume vs Dream Job"
        )

        st.pyplot(fig)

        # ---------------- Skills ----------------

        st.subheader("🛠 Extracted Skills")

        if skills:
            for skill in skills:
                st.write(f"✔ {skill}")

        st.subheader("✅ Matched Skills")

        if matched:
            for skill in matched:
                st.success(skill)

        st.subheader("❌ Missing Skills")

        if missing:
            for skill in missing:
                st.error(skill)
        else:
            st.success("No Missing Skills")

        st.subheader("🎯 Skills Needed For Dream Job")

        if gap_skills:
            for skill in gap_skills:
                st.warning(skill)
        else:
            st.success(
                "🎉 You already have all required skills!"
            )

        st.subheader("💡 Suggestions")

        for suggestion in suggestions:
            st.warning(suggestion)

        st.subheader("📄 Resume Content")

        st.text_area(
            "Extracted Text",
            resume_text,
            height=300
        )

    # ======================================================
    # MULTI RESUME ATS MODE
    # ======================================================

    elif mode == "Recruiter ATS":

        candidates = []

        for uploaded_file in uploaded_files:

            try:

                resume_text = extract_text_from_pdf(
                    uploaded_file
                )

                skills = extract_skills(
                    resume_text
                )

                skills_lower = [
                    s.lower().strip()
                    for s in skills
                ]

                score = calculate_score(
                    skills
                )

                match_percent, _, _ = get_skill_match(
                    skills_lower,
                    JOB_SKILLS
                )

                readiness, _ = analyze_career_gap(
                    skills_lower,
                    target_role
                )

                if score >= 80:
                    prediction = "Selected"

                elif score >= 60 and match_percent >= 50:
                    prediction = "Selected"

                else:
                    prediction = "Rejected"

                candidates.append({
                    "name": uploaded_file.name,
                    "score": score,
                    "match_percent": match_percent,
                    "readiness": readiness,
                    "prediction": prediction
                })

            except Exception as e:

                st.error(
                    f"Error processing {uploaded_file.name}: {e}"
                )

        ranked_candidates = rank_candidates(
            candidates
        )

        ranking_df = pd.DataFrame(
            ranked_candidates
        )

        st.subheader("🏆 Candidate Ranking")

        st.dataframe(
            ranking_df,
            use_container_width=True
        )

        best = ranked_candidates[0]

        st.subheader("🥇 Top Candidate")

        st.success(
            f"""
Candidate: {best['name']}

Score: {best['score']}

Skill Match: {best['match_percent']}%

Status: {best['prediction']}
"""
        )

        st.subheader("✅ Shortlisted Candidates")

        shortlisted = ranking_df[
            ranking_df["prediction"]
            == "Selected"
        ]

        st.dataframe(
            shortlisted,
            use_container_width=True
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("📄 Total Resumes", len(ranking_df))

        with col2:
            st.metric("✅ Shortlisted", len(shortlisted))

        with col3:
            st.metric(
                "❌ Rejected",
                len(ranking_df) - len(shortlisted)
    )

        with col1:
            st.metric(
                "Total Resumes",
                len(ranking_df)
            )

        with col2:
            st.metric(
                "Shortlisted",
                len(shortlisted)
            )

        with col3:
            st.metric(
                "Rejected",
                len(ranking_df) - len(shortlisted)
            )
        st.markdown("---")
        st.subheader("📊 ATS Dashboard")
        col1, col2, col3 = st.columns(3)

        with col1:
           st.success(
             f"📄 Total Resumes\n\n{len(ranking_df)}"
    )

        with col2:
            st.info(
               f"✅ Shortlisted\n\n{len(shortlisted)}"
    )

        with col3:
            st.error(
               f"❌ Rejected\n\n{len(ranking_df)-len(shortlisted)}"
    )



st.caption(
    "SmartHire AI | Resume Screening • Career Guidance • ATS Ranking"
)