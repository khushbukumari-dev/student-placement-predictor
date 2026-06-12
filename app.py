import streamlit as st
import pandas as pd
import joblib

# Load model and scaler

model = joblib.load("models/placement_model.pkl")
scaler = joblib.load("models/scaler.pkl")

st.set_page_config(
    page_title="Student Placement Predictor",
    page_icon="🎯",
    
    layout="wide"
)
st.markdown("""
<style>

/* MAIN APP */
.stApp{
    background: linear-gradient(
        135deg,
        #f8f3ff 0%,
        #ede9fe 50%,
        #ddd6fe 100%
    );
}

/* CONTENT */
.block-container{
    padding-top:2rem;
    padding-left:2rem;
    padding-right:2rem;
}
/* SIDEBAR */
[data-testid="stSidebar"]{
    background: linear-gradient(
        180deg,
        #0f172a 0%,
        #1e1b4b 100%
    );
}


/*SIDEBAR LABELS*/
[data-testid="stSidebar"] label{
    color:white !important;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p{
    color:white !important;
}

/* SELECTBOX TEXT */
[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"]{
    color:black !important;
}


/* METRIC CARDS */
[data-testid="metric-container"]{
    background:white !important;
    padding:20px;
    border-radius:18px;
    box-shadow:0 10px 25px rgba(0,0,0,0.08);
    border-left:1px solid #e5e7eb;
}


/* BUTTON */
.stButton > button{
    width:100%;
    height:55px;
    border:none;
    border-radius:14px;
    background:linear-gradient(
        90deg,
        #4f46e5,
        #7c3aed
    );
    color:white !important;
    font-size:18px;
    font-weight:bold;
}
@keyframes pulse {
    0%{
        transform:scale(1);
    }

    50%{
        transform:scale(1.02);
    }

    100%{
        transform:scale(1);
    }
}                  

</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>
.hero {
    text-align: center;
    padding: 25px;
    border-radius: 15px;
    background: linear-gradient(
    90deg,
    #4f46e5,
    #7c3aed,
    #9333ea
    );        
    color:white;
    margin-bottom: 20px;
}

.hero h1{
    font-size: 48px;
}

.hero p{
    font-size: 18px;
}
/* Number Input */
.stNumberInput{
    background:white;
    border:red;
    border-radius:15px;
    box-shadow:0 4px 12px rgba(0,0,0,0.06);
}



/* Slider */
.stSlider{
    background:white;
    padding:15px;
    border-radius:15px;
    box-shadow:0 4px 12px rgba(0,0,0,0.06);
}
            
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown("""
<div style="
background:linear-gradient(
90deg,
#4f46e5,
#7c3aed,
#9333ea
);
padding:35px;
border-radius:22px;
text-align:center;
color:white;
margin-bottom:20px;
box-shadow:0 10px 30px rgba(123,123,123,0.25);
">
<h1 style="font-size:60px;">
🎯 Student Placement Predictor
</h1>

<p style="font-size:18px">
Predict placement chances using academic performance,
technical skills and real-world experience.
</p>

</div>
""", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.info("📊 Features\n\n# 21")

with col2:
    st.info("🤖 Model\n\n\nLogistic Regression")

with col3:
    st.info("🎯 Accuracy\n\n# 69%")
st.markdown("""
<style>
.stButton > button {
    width:100%;
    background: linear-gradient(90deg,#2563eb,#7c3aed);
    color:white;
    border:none;
    border-radius:12px;
    height:55px;
    font-size:18px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

st.write("---")

branch = st.sidebar.selectbox(
    "🎓 Branch",
    ["CSE", "IT", "ECE", "EE", "ME", "Chemical"]
)

college_tier = st.sidebar.selectbox(
    "🏫 College Tier",
    ["Tier-1", "Tier-2", "Tier-3"]
)
st.markdown("""
<div style="
background:white;
padding:20px;
border-radius:20px;
box-shadow:0 4px 15px rgba(0,0,0,0.08);
margin-bottom:20px;
">
""", unsafe_allow_html=True)
st.subheader("📚 Academic Information")

col1, col2 = st.columns(2)

with col1:
    cgpa = st.number_input(
        "CGPA",
        min_value=0.0,
        max_value=10.0,
        value=7.0
    )

with col2:
    backlogs = st.number_input(
        "Backlogs",
        min_value=0,
        max_value=20,
        value=0
    )
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("""
<div style="
background:white;
padding:25px;
border-radius:20px;
box-shadow:0 8px 20px rgba(0,0,0,0.08);
margin-bottom:25px;
">
""", unsafe_allow_html=True)

st.subheader("💻 Technical Skills")            

coding_skills = st.slider("Coding Skills", 0, 100, 70)
dsa_score = st.slider("DSA Score", 0, 100, 70)
aptitude_score = st.slider("Aptitude Score", 0, 100, 70)
communication_skills = st.slider("Communication Skills", 0, 100, 70)

ml_knowledge = st.slider("ML Knowledge", 0, 100, 50)
system_design = st.slider("System Design", 0, 100, 50)
st.markdown("</div>", unsafe_allow_html=True)

st.subheader("🚀 Experience & Activities")
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
if st.button("🚀Predict Placement"):
    

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
    if prob < 0.40:
        card_color = "linear-gradient(135deg, #ef4444, #dc2626)"
        status = "Low Placement Chance"

    elif prob < 0.70:
        card_color = "linear-gradient(135deg, #f59e0b, #d97706)"
        status = "Moderate Placement Chance"

    else:
        card_color = "linear-gradient(135deg, #22c55e, #16a34a)"
        status = "High Placement Chance"
    st.markdown(f"""
    <div style="
    background: {card_color};
    padding:35px;
    border-radius:28px;
    text-align:center;
    color:white;
    margin-top:25px;
    box-shadow:0 20px 45px rgba(0,0,0,0.35);
    animation: pulse 2s infinite;
    ">

    <h3 style="margin:0;">
    🎯 Placement Prediction Result
    </h3>

    <h1 style="
    margin-top:10px;
    font-size:55px;
    font-weight:800;
    ">
    {prob*100:.1f}%
    </h1>
    <p style="
    font-size:18px;
    font-weight:600;
    margin-top:10px;
    ">
    {status}
    </p>

    <p style="
    font-size:18px;
    margin-top:5px;
    ">
    Placement Probability
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.progress(int(prob * 100))

    
    if prediction == 1:
        st.markdown("""
        <div style="
        background:#dcfce7;
        color:#166534;
        padding:18px;
        border-radius:15px;
        text-align:center;
        font-size:22px;
        font-weight:bold;
        ">
        ✅ Likely To Be Placed
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <div style="
        background:#fee2e2;
        color:#991b1b;
        padding:18px;
        border-radius:15px;
        text-align:center;
        font-size:22px;
        font-weight:bold;
        ">
        ❌ Placement Less Likely
        </div>
        """, unsafe_allow_html=True)
    
with st.expander("📌 About this project"):
    st.write("""
    This system uses Machine Learning to predict student placement chances 
    based on academic and skill-based inputs.
    
    Built using:
    - Python
    - Streamlit
    - Scikit-learn
    """)

st.sidebar.title("⚙️ Student Profile")

st.sidebar.info("""
🎓 Placement Prediction System

Built with:
• Python
• Streamlit
• Scikit-Learn
""")

st.sidebar.success("Model Loaded ✅")
st.markdown("""
<hr>
<div style='text-align:center; color:black;'>
Built with ❤️ by Khushbu Kumari | B.Tech CSE (AI & ML)
</div>
""", unsafe_allow_html=True) 
st.sidebar.markdown(
    "[🔗 View Project on GitHub](https://github.com/khushbukumari-dev/student-placement-predictor)"
)   