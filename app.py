import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("heart_model.pkl", "rb"))

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️"
)

st.title("❤️ Heart Disease Prediction System")

st.write("Enter the patient's medical information.")

age = st.number_input("Age", 1, 120)
sex = st.selectbox("Sex", ["Male", "Female"])

if st.button("Predict"):

    sex_value = 1 if sex == "Male" else 0

    # Your remaining input features go here

    st.success("Prediction completed.")
