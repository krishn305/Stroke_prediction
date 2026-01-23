import streamlit as st
import numpy as np
import joblib

model = joblib.load("stroke_lgbm_model(1).pkl")
scaler = joblib.load("scaler(1).pkl")

st.set_page_config(page_title="Stroke Prediction App")

st.title("🧠 Stroke Prediction System")
st.write("LightGBM based ML Web App")

age = st.slider("Age", 1, 100, 45)
hypertension = st.selectbox("Hypertension (0 = No, 1 = Yes)", [0, 1])
heart_disease = st.selectbox("Heart Disease (0 = No, 1 = Yes)", [0, 1])
avg_glucose = st.number_input("Average Glucose Level", 50.0, 300.0, 100.0)
bmi = st.number_input("BMI", 10.0, 60.0, 25.0)

if st.button("Predict Stroke Risk"):
    input_data = np.array([[age, hypertension, heart_disease,
                             avg_glucose, bmi]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("⚠ High Risk of Stroke")
    else:
        st.success("✅ Low Risk of Stroke")
