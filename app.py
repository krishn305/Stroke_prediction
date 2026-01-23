import streamlit as st
import numpy as np

st.set_page_config(page_title="Stroke Prediction App")

st.title("🧠 Stroke Risk Prediction")
st.write("Rule-based inference derived from ML analysis")

age = st.slider("Age", 1, 100, 45)
hypertension = st.selectbox("Hypertension (0 = No, 1 = Yes)", [0, 1])
heart_disease = st.selectbox("Heart Disease (0 = No, 1 = Yes)", [0, 1])
avg_glucose = st.number_input("Average Glucose Level", 50.0, 300.0, 100.0)
bmi = st.number_input("BMI", 10.0, 60.0, 25.0)

if st.button("Predict Stroke Risk"):
    risk_score = 0

    if age > 60:
        risk_score += 2
    if hypertension == 1:
        risk_score += 2
    if heart_disease == 1:
        risk_score += 2
    if avg_glucose > 180:
        risk_score += 2
    if bmi > 30:
        risk_score += 1

    if risk_score >= 5:
        st.error("⚠ High Risk of Stroke")
    elif risk_score >= 3:
        st.warning("🟠 Moderate Risk of Stroke")
    else:
        st.success("✅ Low Risk of Stroke")
