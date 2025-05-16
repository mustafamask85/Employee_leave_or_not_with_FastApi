from fastapi import FastAPI
import numpy as np 
import pickle 
import pandas as pd 
from pydantic import BaseModel 
import joblib

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use ["http://localhost"] or similar in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




class Employee(BaseModel):

    Education :str
    JoiningYear : int 
    City : str
    PaymentTier : int 
    Age:int
    Gender:str 
    EverBenched : str
    ExperienceInCurrentDomain :int




model = joblib.load("emplyee.pkl")

@app.get("/")

async def welcome(): 

        return {"message":"Hello from root :)"}


@app.post("/predict")

async def predict_leaving(data:Employee):
      
    
      df = pd.DataFrame([data.dict()])
      prediction = model.predict(df)
      return {"prediction": int(prediction[0])}
