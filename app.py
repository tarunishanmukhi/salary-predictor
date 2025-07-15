import streamlit as st
import joblib
import numpy as np

st.title("Salary Prediction App")

st.divider()

st.write("With this app, you can predict the salary of an employee based on their years of experience and education level.")

years=st.number_input("enter the years at company",value=1, step=1, min_value=0)
jobrate=st.number_input("enter the job rate",value=3.5, step=0.5, min_value=0.0)

X= [years, jobrate]

model= joblib.load("linearmodel.pkl")

st.divider()

predict= st.button("Press the button for Predict Salary")

st.divider()

if predict:

        st.balloons()

        X1=np.array([X])

        prediction=model.predict(X1)[0]

        st.write(f"Salary prediction is {prediction:,.2f}")


else:
    "please press the button  for app to make a prediction"
