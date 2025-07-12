from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib
from preprocess import load_and_preprocess

# Load cleaned data
df = load_and_preprocess('data-collection/data/merged_news.csv')  # merged version of real+fake

X = df['combined']
y = df['label']

# Split the data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorization
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Model training
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Evaluation
predictions = model.predict(X_test_vec)
print(classification_report(y_test, predictions))

# Save model and vectorizer
joblib.dump(model, 'data-collection/model/fake_news_model.pkl')
joblib.dump(vectorizer, 'data-collection/model/vectorizer.pkl')

print("✅ Model and vectorizer saved successfully.")
