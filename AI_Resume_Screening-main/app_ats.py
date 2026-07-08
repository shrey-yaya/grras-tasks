import streamlit as st
import pandas as pd

from resume_parser import extract_text_from_pdf
from skills import extract_skills
from scorer import calculate_score
from skill_match import get_skill_match
from career_gap import analyze_career_gap
from candidate_ranker import rank_candidates

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Resume Screening ATS",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Screening & Candidate Ranking System")

# ---------------- DREAM JOB ----------------

target_role = st.selectbox(
    "🎯 Select Target Role",
    [
        "Machine Learning Engineer",
        "Data Analyst",
        "AI Engineer",
        "Software Developer"
    ]
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

# ---------------- MULTIPLE FILE UPLOAD ----------------

uploaded_files = st.file_uploader(
    "Upload Multiple Resumes",
    type=["pdf"],
    accept_multiple_files=True
)

# ---------------- PROCESS FILES ----------------

if uploaded_files:

    candidates = []

    with st.spinner("Analyzing resumes..."):

        for uploaded_file in uploaded_files:

            try:

                resume_text = extract_text_from_pdf(uploaded_file)

                skills = extract_skills(resume_text)

                skills_lower = [
                    skill.lower().strip()
                    for skill in skills
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

                if score >= 80:
                    prediction = "Selected"

                elif score >= 60 and match_percent >= 50:
                    prediction = "Selected"

                else:
                    prediction = "Rejected"

                candidates.append({
                    "Candidate": uploaded_file.name,
                    "Score": score,
                    "Skill Match %": match_percent,
                    "Career Readiness %": readiness,
                    "Prediction": prediction
                })

            except Exception as e:

                st.error(
                    f"Error processing {uploaded_file.name}: {e}"
                )

    # ---------------- RANK CANDIDATES ----------------

    ranked_candidates = rank_candidates([
        {
            "name": c["Candidate"],
            "score": c["Score"],
            "match_percent": c["Skill Match %"],
            "readiness": c["Career Readiness %"],
            "prediction": c["Prediction"]
        }
        for c in candidates
    ])

    # ---------------- TABLE ----------------

    st.subheader("🏆 Candidate Ranking")

    ranking_df = pd.DataFrame(ranked_candidates)

    st.dataframe(
        ranking_df,
        use_container_width=True
    )

    # ---------------- BEST CANDIDATE ----------------

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

    # ---------------- SHORTLISTED ----------------

    st.subheader("✅ Shortlisted Candidates")

    shortlisted = ranking_df[
        ranking_df["prediction"] == "Selected"
    ]

    st.dataframe(
        shortlisted,
        use_container_width=True
    )

    # ---------------- METRICS ----------------

    col1, col2, col3 = st.columns(3)

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