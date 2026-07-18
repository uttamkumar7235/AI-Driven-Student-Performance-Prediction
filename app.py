import streamlit as st
import pandas as pd
import joblib
from ai_helper import generate_ai_report


# Page Configuration
st.set_page_config(
    page_title="AI-Driven Student Performance Prediction",
    page_icon="🎓",
    layout="wide"
)

# Load Model
model = joblib.load("model.pkl")

# Header
st.title("🎓 AI-Driven Student Performance Prediction")

st.markdown("""
Predict a student's final performance using Machine Learning and receive AI-powered insights.
""")

st.divider()


# Sidebar
st.sidebar.title("🎓 AI Student Advisor")

st.sidebar.success("✅ Machine Learning Prediction")
st.sidebar.success("🤖 AI Performance Analysis")
st.sidebar.success("📅 Personalized Study Plan")
st.sidebar.success("💡 Smart Recommendations")

st.sidebar.divider()

st.sidebar.markdown("""
### About

This application predicts a student's academic performance using a Random Forest model and then uses Generative AI to provide personalized academic insights and a study plan.
""")


# Layout
left, right = st.columns(2)

with left:

    st.subheader("📋 Student Information")

    study_hours = st.number_input(
        "Study Hours",
        min_value=0.0,
        max_value=24.0,
        value=5.0,
        step=0.5
    )

    attendance = st.number_input(
        "Attendance (%)",
        min_value=0.0,
        max_value=100.0,
        value=80.0
    )

    previous_score = st.number_input(
        "Previous Score",
        min_value=0.0,
        max_value=100.0,
        value=75.0
    )

    assignments = st.number_input(
        "Assignments Completed",
        min_value=0,
        max_value=20,
        value=8
    )

    sleep_hours = st.number_input(
        "Sleep Hours",
        min_value=0.0,
        max_value=12.0,
        value=7.0,
        step=0.5
    )

with right:

    st.subheader("📚 Additional Information")

    internet = st.selectbox(
        "Internet Available",
        ["Yes", "No"]
    )

    parent_education = st.selectbox(
        "Parent Education",
        [
            "Primary",
            "High School",
            "Graduate",
            "Post Graduate"
        ]
    )

    extracurricular = st.selectbox(
        "Extracurricular Activities",
        ["Yes", "No"]
    )

    screen_time = st.number_input(
        "Daily Screen Time (Hours)",
        min_value=0.0,
        max_value=15.0,
        value=3.0,
        step=0.5
    )

    family_income = st.selectbox(
        "Family Income",
        [
            "Low",
            "Medium",
            "High"
        ]
    )

st.divider()

predict = st.button(
    "🚀 Predict Performance",
    use_container_width=True
)

if predict:

    # Save Text Values for Groq
    internet_text = internet
    parent_education_text = parent_education
    extracurricular_text = extracurricular
    family_income_text = family_income

    # Convert to Numbers for ML
    internet = 1 if internet_text == "Yes" else 0

    parent_education = {
        "Primary": 0,
        "High School": 1,
        "Graduate": 2,
        "Post Graduate": 3
    }[parent_education_text]

    extracurricular = 1 if extracurricular_text == "Yes" else 0

    family_income = {
        "Low": 0,
        "Medium": 1,
        "High": 2
    }[family_income_text]

    # Prediction
    new_data = pd.DataFrame({
        "StudyHours": [study_hours],
        "Attendance": [attendance],
        "PreviousScore": [previous_score],
        "Assignments": [assignments],
        "InternetAvailable": [internet],
        "ParentEducation": [parent_education],
        "SleepHours": [sleep_hours],
        "ExtracurricularActivities": [extracurricular],
        "DailyScreenTime": [screen_time],
        "FamilyIncome": [family_income]
    })

    score = model.predict(new_data)[0]

    if score >= 90:
        performance = "Excellent 🟢"
    elif score >= 75:
        performance = "Good 🟡"
    elif score >= 60:
        performance = "Average 🟠"
    else:
        performance = "Needs Improvement 🔴"

    st.success("Prediction Completed Successfully!")

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Predicted Final Score",
            f"{score:.2f}"
        )

    with c2:
        st.metric(
            "Performance",
            performance
        )

    st.progress(min(score / 100, 1.0))

    # Generate AI Report
    student_data = {
        "StudyHours": study_hours,
        "Attendance": attendance,
        "PreviousScore": previous_score,
        "Assignments": assignments,
        "InternetAvailable": internet_text,
        "ParentEducation": parent_education_text,
        "SleepHours": sleep_hours,
        "ExtracurricularActivities": extracurricular_text,
        "DailyScreenTime": screen_time,
        "FamilyIncome": family_income_text
    }

    with st.spinner("🤖 Generating AI insights..."):
        try:
            ai_report = generate_ai_report(student_data, score)
            st.divider()
            st.subheader("🤖 AI Academic Advisor")
            st.markdown(ai_report)
            
        except Exception:
            st.error("Unable to generate AI report.")
    
st.divider()

st.caption(
    "Built with ❤️ using Streamlit • Scikit-learn • Groq"
)