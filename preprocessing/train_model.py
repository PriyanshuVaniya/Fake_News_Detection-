import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "../model")
os.makedirs(MODEL_DIR, exist_ok=True)

# 1. Load merged CSV
df = pd.read_csv("data-collection/merged_news.csv")  # Adjust path if needed

# 2. Shuffle dataset
df = df.sample(frac=1).reset_index(drop=True)

# 3. Clean data (basic cleaning)
df['text'] = df['text'].astype(str).str.lower()

# 4. Vectorize
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X = vectorizer.fit_transform(df['text'])

# 5. Labels: Make sure FAKE = 1, REAL = 0
y = df['label']  # Label column should already have 0 and 1

# 6. Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)

# 7. Save model & vectorizer
joblib.dump(model, os.path.join(MODEL_DIR, "fake_news_model.pkl"))
joblib.dump(vectorizer, os.path.join(MODEL_DIR, "vectorizer.pkl"))

print("✅ Model & vectorizer trained and saved successfully.")
