# Student Placement Predictor

A Machine Learning project that predicts whether a student is likely to get placed based on academic performance, technical skills, and extracurricular achievements.

## Project Overview

Campus placements play a crucial role in a student's career. This project uses Machine Learning techniques to predict placement outcomes using various student-related factors such as CGPA, coding skills, DSA score, communication skills, certifications, internships, and more.

The goal is to help understand which factors have the strongest impact on placement chances.

---

## Problem Statement

Predict whether a student will be placed or not based on their academic and skill-related attributes.

Target Variable:

* placement_status

  * 1 = Placed
  * 0 = Not Placed

---

## Dataset Information

Dataset Size:

* 100,000 records
* 18 features

Important Features:

* CGPA
* DSA Score
* Coding Skills
* Communication Skills
* Aptitude Score
* Projects Count
* Certifications
* Internships
* Hackathons
* College Tier
* Branch
* Backlogs

---

## Machine Learning Workflow

1. Problem Understanding
2. Data Collection
3. Data Cleaning
4. Exploratory Data Analysis (EDA)
5. Feature Engineering
6. Encoding Categorical Variables
7. Feature Scaling
8. Train-Test Split
9. Model Building
10. Model Evaluation
11. Feature Importance Analysis
12. Model Saving

---

## Models Implemented

### Logistic Regression

* Accuracy: 69.95%
* Precision: 71.67%
* Recall: 92.79%
* F1 Score: 80.87%

### Decision Tree

* Accuracy: 59.68%
* Precision: 71.03%
* Recall: 69.44%
* F1 Score: 70.23%

### Random Forest

* Accuracy: 69.26%
* Precision: 71.13%
* Recall: 92.73%
* F1 Score: 80.51%

---

## Final Model Selection

Logistic Regression was selected as the final model because:

* Highest Accuracy
* Highest F1 Score
* Better Generalization
* Minimal Overfitting
* Easy Interpretability

---

## Key Insights

* College Tier is one of the strongest placement indicators.
* Higher DSA and Coding Skills significantly improve placement chances.
* More Projects and Certifications positively impact placement probability.
* Backlogs negatively affect placement outcomes.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Joblib

---

## Project Structure

student-placement-predictor/

├── data/

├── notebooks/

├── models/

│ ├── placement_model.pkl

│ └── scaler.pkl

├── app.py

├── requirements.txt

├── README.md

---

## Future Improvements

* Hyperparameter Tuning
* XGBoost Implementation
* Streamlit Deployment
* Real Placement Dataset Integration

---

## Author

Khushbu Kumari

B.Tech CSE (AI & ML)

Machine Learning Enthusiast
