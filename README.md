A Machine Learning-based placement prediction system built using Logistic Regression and deployed with Streamlit.

🎓 Student Placement Predictor

A Machine Learning-powered web application that predicts a student's placement chances based on academic performance, technical skills, internships, projects, certifications, and extracurricular activities.

🚀 Live Demo

Application:
https://student-placement-predictor-m8ewryt9nhbgyecuzj5njb.streamlit.app/

GitHub Repository:
https://github.com/khushbukumari-dev/student-placement-predictor

---

📖 Project Overview

Student Placement Predictor is an end-to-end Machine Learning project developed to estimate whether a student is likely to get placed based on various academic and skill-related factors.

The project covers the complete Machine Learning workflow including:

- Data Cleaning
- Data Preprocessing
- Feature Engineering
- Model Training
- Model Evaluation
- Streamlit Deployment

The application allows users to enter their details and receive an instant placement prediction along with a placement probability score.

---

🎯 Objective

The primary objective of this project is to:

- Analyze factors influencing student placements.
- Predict placement outcomes using Machine Learning.
- Provide an interactive platform for placement probability estimation.
- Demonstrate practical implementation of Machine Learning concepts.

---

🤖 Machine Learning Model

Selected Model

Logistic Regression

Why Logistic Regression?

Among all tested models, Logistic Regression delivered the best overall performance for this dataset.

Reasons for selecting Logistic Regression:

- Strong performance on binary classification tasks.
- Generates probability-based predictions.
- Computationally efficient.
- Easy to interpret and deploy.
- Consistent performance compared to Decision Tree and Random Forest.

---

📊 Features Used

Academic Features

- CGPA
- Backlogs
- Branch
- College Tier

Technical Skills

- Coding Skills
- DSA Score
- Aptitude Score
- Communication Skills
- Machine Learning Knowledge
- System Design Knowledge

Experience & Activities

- Internships
- Projects
- Certifications
- Hackathon Participation
- Open Source Contributions
- Extracurricular Activities
- Leadership Experience
- Placement Training

---

🎯 Target Variable

Placement Status

- 1 → Placed
- 0 → Not Placed

---

📈 Model Performance

Metric| Value
Model| Logistic Regression
Accuracy| ~70%
Problem Type| Binary Classification
Deployment| Streamlit Cloud

The model predicts the likelihood of student placement based on multiple academic and professional factors.

---

✨ Application Features

Placement Prediction

- Real-time prediction
- Probability-based output
- Placement likelihood estimation

Interactive Dashboard

- User-friendly interface
- Streamlit-based web application
- Instant results

Smart Result System

- 🟢 High Placement Chance
- 🟠 Moderate Placement Chance
- 🔴 Low Placement Chance

Visualization

- Probability display
- Dynamic result cards
- Clean UI design

---

🛠️ Tech Stack

Programming

- Python

Data Analysis

- Pandas
- NumPy

Machine Learning

- Scikit-Learn
- Logistic Regression

Deployment

- Streamlit

Model Storage

- Joblib

Version Control

- Git
- GitHub

---

📂 Project Structure

student-placement-predictor/

├── app.py

├── requirements.txt

├── README.md

├── models/

│ ├── placement_model.pkl

│ └── scaler.pkl

├── notebooks/

│ └── placement_prediction.ipynb

└── assets/

---

⚙️ Installation

Clone Repository

git clone https://github.com/khushbukumari-dev/student-placement-predictor.git

Navigate to Project Directory

cd student-placement-predictor

Install Dependencies

pip install -r requirements.txt

Run Application

streamlit run app.py

---

🔄 Project Workflow

1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Data Preprocessing
5. Model Training
6. Model Evaluation
7. Streamlit Deployment

---

🚀 Future Improvements

- XGBoost Integration
- Advanced Feature Selection
- Placement Recommendation Engine
- Skill Gap Analysis
- Resume Evaluation System
- AI Career Guidance Assistant
- Personalized Career Insights

---

👩‍💻 Author

Khushbu Kumari

B.Tech CSE (AI & ML)

Passionate about Machine Learning, Data Science, and AI Applications.

GitHub:
https://github.com/khushbukumari-dev

LinkedIn:
https://www.linkedin.com/in/khushbu-kumari-134bba361?utm_source=share_via&utm_content=profile&utm_medium=member_android

---

⭐ Support

If you found this project useful, consider giving it a star on GitHub.

Your support helps improve the project and encourages future development.