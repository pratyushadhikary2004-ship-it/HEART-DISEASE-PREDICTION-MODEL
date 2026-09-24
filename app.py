import streamlit as st

st.title("Heart Disease Prediction")

age = st.number_input("Enter Age")

if st.button("Predict"):
    st.write("Prediction Generated")
