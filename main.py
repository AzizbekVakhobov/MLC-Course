from fastapi import FastAPI
import joblib
import numpy as np
import pandas as pd
from request import DiabetesRequest

# Initialize FastAPI
app = FastAPI()

# Load trained model
model = joblib.load("diabetes_model.pkl")

# Root Endpoint
@app.get("/")
def home():
    return {"message": "Diabetes Prediction API is running! Use /docs to test."}

# Define Prediction Endpoint
@app.post("/predict")
def predict(request: DiabetesRequest):
    try:
        # Convert request to DataFrame (matching training format)
        input_data = pd.DataFrame([request.dict()])

        # Make prediction
        prediction = model.predict(input_data)[0]

        return {"prediction": int(prediction)}

    except Exception as e:
        return {"error": str(e)}

