from fastapi import FastAPI
from app.schema import CryptoFeatures
from app.predict import predict_crypto

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Crypto Prediction API is running!"}

@app.post("/predict")
def predict_endpoint(features: CryptoFeatures):
    return predict_crypto(features.dict())
