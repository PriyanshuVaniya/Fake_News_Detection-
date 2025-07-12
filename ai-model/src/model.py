import joblib
import os
import numpy as np

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "../model/fake_news_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "../model/vectorizer.pkl")

# Load model & vectorizer
model = joblib.load(os.path.normpath(MODEL_PATH))
vectorizer = joblib.load(os.path.normpath(VECTORIZER_PATH))

def predict_news(text: str):
    transformed = vectorizer.transform([text])
    prediction = model.predict(transformed)[0]
    probabilities = model.predict_proba(transformed)[0]
    confidence = round(np.max(probabilities), 4)

    return {
        "prediction": "FAKE" if prediction == 1 else "REAL",
        "confidence": confidence
    }
