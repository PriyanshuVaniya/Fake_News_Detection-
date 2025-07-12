from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('models/fake_news_model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    vector = vectorizer.transform([text])
    prediction = model.predict(vector)[0]
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(debug=True)
