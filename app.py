import streamlit as st
import numpy as np
import joblib

# Load model and scaler params
model = joblib.load("stroke_model.pkl")
scaler = joblib.load("scaler_params.pkl")

mean = scaler["mean"]
std = scaler["std"]

st.set_page_config(page_title="Stroke Prediction App")

st.title("🧠 Stroke Prediction App")
st.write("ML-based Stroke Risk Prediction System")

age = st.slider("Age", 1, 100, 45)
hypertension = st.selectbox("Hypertension", [0, 1])
heart_disease = st.selectbox("Heart Disease", [0, 1])
avg_glucose = st.number_input("Average Glucose Level", 50.0, 300.0, 100.0)
bmi = st.number_input("BMI", 10.0, 60.0, 25.0)

if st.button("Predict Stroke Risk"):
    X = np.array([[age, hypertension, heart_disease,
                   avg_glucose, bmi]])
    X_scaled = (X - mean) / std
    prediction = model.predict(X_scaled)

    if prediction[0] == 1:
        st.error("⚠ High Risk of Stroke")
    else:
        st.success("✅ Low Risk of Stroke")

