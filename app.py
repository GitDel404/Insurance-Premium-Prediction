from fastapi import FastAPI
import streamlit as slt
import pickle
import pandas as pd
from typing import Annotated, Optional, Literal
from pydantic import Field, computed_field, BaseModel
from fastapi.responses import JSONResponse
from Schema.user_input import UserInput
from Schema.prediction_response import PredictionResponse
from Model.predict import  MODEL_VERSION, predict_output

app = FastAPI()


  
@app.get("/")
def homepage():
    return {"message": "Hello"}


@app.get("/health")
def health():
    return {"status": "Ok", "version": MODEL_VERSION}

@app.post('/prediction', response_model=PredictionResponse)
def prediction(data: UserInput):
    input = {
            "age" : data.age,
            "income_lpa": data.income_lpa,
            "smoker" : data.smoker,
            "occupation": data.occupation,
            "bmi": data.set_bmi,
            "tier" : data.set_city
        }
    pred = predict_output(input)
    return JSONResponse(status_code=200, content={"response": pred})

   
