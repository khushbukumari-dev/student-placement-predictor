import streamlit as st
import pandas as pd
import joblib

# Load model and scaler

model = joblib.load("models/placement_model.pkl")
scaler = joblib.load("models/scaler.pkl")

st.set_page_config(page_title="Student Placement Predictor")

st.title("🎓 Student Placement Predictor")
st.write("Enter student details to predict placement chances.")

# Inputs

branch = st.selectbox(
"Branch",
["CSE", "IT", "ECE", "EE", "ME", "Chemical"]
)

college_tier = st.selectbox(
"College Tier",
["Tier-1", "Tier-2", "Tier-3"]
)

cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, value=7.0)

backlogs = st.number_input("Backlogs", min_value=0, max_value=20, value=0)

coding_skills = st.slider("Coding Skills", 0, 100, 70)
dsa_score = st.slider("DSA Score", 0, 100, 70)
aptitude_score = st.slider("Aptitude Score", 0, 100, 70)
communication_skills = st.slider("Communication Skills", 0, 100, 70)

ml_knowledge = st.slider("ML Knowledge", 0, 100, 50)
system_design = st.slider("System Design", 0, 100, 50)

internships = st.number_input("Internships", min_value=0, max_value=10, value=0)
projects_count = st.number_input("Projects Count", min_value=0, max_value=20, value=2)
certifications = st.number_input("Certifications", min_value=0, max_value=20, value=1)
hackathons = st.number_input("Hackathons", min_value=0, max_value=20, value=0)

open_source_contributions = st.number_input(
"Open Source Contributions",
min_value=0,
max_value=100,
value=0
)

extracurriculars = st.number_input(
"Extracurricular Activities",
min_value=0,
max_value=100,
value=0
)
if st.button("Predict Placement"):

    tier_mapping = {
        "Tier-1": 3,
        "Tier-2": 2,
        "Tier-3": 1
    }

    input_data = {
        "college_tier": tier_mapping[college_tier],
        "cgpa": cgpa,
        "backlogs": backlogs,
        "coding_skills": coding_skills,
        "dsa_score": dsa_score,
        "aptitude_score": aptitude_score,
        "communication_skills": communication_skills,
        "ml_knowledge": ml_knowledge,
        "system_design": system_design,
        "internships": internships,
        "projects_count": projects_count,
        "certifications": certifications,
        "hackathons": hackathons,
        "open_source_contributions": open_source_contributions,
        "extracurriculars": extracurriculars,

       
    }

    input_df = pd.DataFrame([input_data])


# Scale only numerical columns
    input_df[input_df.columns] = scaler.transform(input_df)


# Branch dummy columns
    input_df["branch_CSE"] = 0
    input_df["branch_Chemical"] = 0
    input_df["branch_ECE"] = 0
    input_df["branch_EE"] = 0
    input_df["branch_IT"] = 0
    input_df["branch_ME"] = 0


    if branch == "CSE":
       input_df["branch_CSE"] = 1
    elif branch == "Chemical":
       input_df["branch_Chemical"] = 1
    elif branch == "ECE":
       input_df["branch_ECE"] = 1
    elif branch == "EE":
       input_df["branch_EE"] = 1
    elif branch == "IT":
       input_df["branch_IT"] = 1
    elif branch == "ME":
       input_df["branch_ME"] = 1

    final_columns = [
        'college_tier',
        'cgpa',
        'backlogs',
        'coding_skills',
        'dsa_score',
        'aptitude_score',
        'communication_skills',
        'ml_knowledge',
        'system_design',
        'internships',
        'projects_count',
        'certifications',
        'hackathons',
        'open_source_contributions',
        'extracurriculars',
        'branch_CSE',
        'branch_Chemical',
        'branch_ECE',
        'branch_EE',
        'branch_IT',
        'branch_ME'
    ]

    input_df = input_df[final_columns]
   
  

    prediction = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    st.metric(
        "Placement Probability",
        f"{prob*100:.2f}%"
    )


    if prediction == 1:
        st.success("✅ Likely to be Placed")
    else:
        st.error("❌ Placement Less Likely")


    