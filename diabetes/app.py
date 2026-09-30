import streamlit as st
import joblib

model=joblib.load('model_trained.pk1')
st.title("Diabetes Prediction 💊👩‍⚕️")
st.write("my 1st ML project  using streamlit")
pregnancies=st.number_input("enter pregnancies",min_value=0)
Glucose=st.number_input("enter Glucose",min_value=0)
BloodPressure=st.number_input("enter BloodPressure",min_value=0) 
SkinThickness=st.number_input("enter SkinThickness",min_value=0)
Insulin=st.number_input("enter Insulin",min_value=0.0)
BMI=st.number_input("enter BMI",min_value=0.0)
DiabetesPedigreeFunction=st.number_input("enter DiabetesPedigreeFunction",min_value=0.0)
Age=st.number_input("enter Age",min_value=0)


if st.button("predection"):
    input_list=[[pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]
    
    final_predection=model.predict(input_list)
    
    if final_predection[0]==1:
        st.error("person having diabetes")
    else:
        st.success("person don't have diabetes")
    