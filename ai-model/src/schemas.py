# app/schemas.py

from pydantic import BaseModel

# Request body
class NewsRequest(BaseModel):
    title: str
    text: str  # the news content

# Response body
class PredictionResponse(BaseModel):
    prediction: str  # "FAKE" or "REAL"
    confidence: float
