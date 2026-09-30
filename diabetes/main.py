from fastapi import FastAPI
from pydantic import BaseModel

import joblib

app=FastAPI()

model=joblib.load('model_trained.pk1')

class diabetesInput(BaseModel):
     
    Pregnancies:int
    Glucose:int
    BloodPressure:int 
    SkinThickness:int
    Insulin:float
    BMI:float
    DiabetesPedigreeFunction:float
    Age:int
@app.get('/')
def home():
    return "Message:My 1st ML Project Using FastApi"

@app.post('/predict')
def prediction(data:diabetesInput):
    input_list=[[
        data.Pregnancies,
        data.Glucose,
        data.BloodPressure,
        data.SkinThickness,
        data.Insulin,
        data.BMI,
        data.DiabetesPedigreeFunction,
        data.Age,
    
    ]]
    
    final_prediction=model.predict(input_list)
    
    result="diabetes" if final_prediction[0]==1 else "No diabetes"
    return{
        "Prediction":result
    }