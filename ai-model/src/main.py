from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.model import predict_news


app = FastAPI()

# Request format
class NewsRequest(BaseModel):
    text: str

# Response format
class NewsResponse(BaseModel):
    prediction: str
    confidence: float

@app.get("/")
def home():
    return {"message": "AI Model Service is running!"}

@app.post("/predict", response_model=NewsResponse)
def predict(request: NewsRequest):
    try:
        result = predict_news(request.text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
