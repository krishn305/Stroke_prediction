#  Stroke Risk Prediction System

A machine learning–based project to predict the risk of stroke using clinical and lifestyle features.  
This project focuses on **model comparison, selection, and practical deployment considerations**.

---

##  Problem Statement
Stroke is a major cause of death and long-term disability worldwide.  
Early risk prediction can help in preventive healthcare and decision support.

The goal of this project is to:
- Analyze patient health data
- Train and compare multiple machine learning models
- Select the best-performing model
- Deploy a live, user-friendly prediction system

---

## 📊 Dataset
- **Source:** Healthcare Stroke Dataset
- **Target Variable:** `stroke` (0 = No Stroke, 1 = Stroke)
- **Key Features Used:**
  - Age
  - Hypertension
  - Heart Disease
  - Average Glucose Level
  - BMI

---

## 🧪 Machine Learning Approach

### 🔹 Models Trained & Compared
- Logistic Regression  
- Support Vector Machine (SVM)  
- Naive Bayes  
- **LightGBM (Best Performing Model)**  

### 🔹 Data Preprocessing
- Missing value handling (BMI)
- Feature scaling
- Class imbalance handled using **SMOTE**
- Train-test split for evaluation

### 🔹 Model Selection
After evaluating multiple models using accuracy and F1-score:
- **LightGBM achieved the highest performance**
- Selected as the **final model for analysis and reporting**

---

##  Deployment Strategy (Important Note)

Due to **Python 3.13 compatibility limitations** on Streamlit Cloud with serialized ML models (LightGBM, scikit-learn, imbalanced-learn), the project follows a **separation of concerns** approach:

- ✅ **Training & evaluation:** Performed using LightGBM (documented in notebooks)
- ✅ **Live web application:** Uses a lightweight, stable inference layer derived from ML insights
- ✅ Ensures reliable deployment while preserving ML rigor

This reflects **real-world industry practices**, where training and production environments often differ.

---

##  Live Application Features
- Interactive Streamlit web interface
- User inputs:
  - Age
  - Hypertension
  - Heart Disease
  - Average Glucose Level
  - BMI
- Risk output:
  - Low Risk
  - Moderate Risk
  - High Risk

---

## 🛠️ Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- LightGBM (training & evaluation)
- Streamlit (deployment)
- Google Colab
- GitHub

---

## 📈 Key Learnings
- Model comparison and selection using real healthcare data
- Handling imbalanced datasets using SMOTE
- Understanding deployment constraints of ML models
- Separating training logic from production inference
- Building a reliable, user-facing ML application

---

## 📌 Disclaimer
This application is intended for **educational purposes only** and should not be used as a medical diagnosis tool.

---

## 👤 Author
**Krishnapriya karan
Priyanka Mallik**  
AI / ML Enthusiast  
