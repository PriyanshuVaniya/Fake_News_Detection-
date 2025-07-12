from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_GATEWAY_URL = "http://localhost:8080/predict"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["news_input"]

        try:
            response = requests.post(API_GATEWAY_URL, json={
                "title": user_input[:100],  # Shortened version as title
                "text": user_input
            }, timeout=10)

            result = response.json()

            return render_template("index.html", 
                                prediction=result["prediction"], 
                                confidence=round(result["confidence"] * 100),
                                tags=result.get("tags", []),
                                user_input=user_input)

        except requests.exceptions.RequestException as e:
            print("Error:", e)
            return render_template("index.html", 
                                error="Service temporarily unavailable. Please try again later.",
                                user_input=user_input)
        except Exception as e:
            print("Error:", e)
            return render_template("index.html", 
                                error="An unexpected error occurred.",
                                user_input=user_input)

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, port=3000)