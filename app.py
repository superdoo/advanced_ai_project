# Deploys FastAPI for real-time prediction.

from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model.pkl")

@app.post("/predict")
def predict(data: dict):
    features = np.array([data['age'], data['income'], data['account_balance']]).reshape(1, -1)
    prediction = model.predict(features)
    return {"churn_probability": prediction.tolist()}