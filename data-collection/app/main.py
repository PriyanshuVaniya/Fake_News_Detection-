from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

# Input format
class NewsRequest(BaseModel):
    text: str

# Output format
class NewsResponse(BaseModel):
    prediction: str
    confidence: float

AI_MODEL_URL = "http://ai-model:9000/predict"  # This name matches the service name in docker-compose

@app.get("/")
def home():
    return {"message": "Data Collection Service is running!"}

@app.post("/predict", response_model=NewsResponse)
def predict(request: NewsRequest):
    try:
        # Send request to ai-model microservice
        response = requests.post(AI_MODEL_URL, json={"text": request.text})
        
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)

        return response.json()
    
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
