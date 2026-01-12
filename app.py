import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="Stroke Prediction", layout="centered")

@st.cache_resource
def load_model():
    return joblib.load("stroke_prediction_model.pkl")

model = load_model()

st.title("Stroke Prediction App")
st.write("Enter patient details to predict stroke risk")

age = st.number_input("Age", 1, 100, 50)
hypertension = st.selectbox("Hypertension (0 = No, 1 = Yes)", [0, 1])
heart_disease = st.selectbox("Heart Disease (0 = No, 1 = Yes)", [0, 1])
avg_glucose = st.number_input("Average Glucose Level", 50.0, 300.0, 100.0)

if st.button("Predict"):
    X = np.array([[age, hypertension, heart_disease, avg_glucose]])
    pred = model.predict(X)

    if int(pred[0]) == 1:
        st.error(" High risk of Stroke")
    else:
        st.success(" Low risk of Stroke")
