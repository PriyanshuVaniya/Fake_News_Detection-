from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)
CSV_FILE = 'submitted_news.csv'

@app.route("/store", methods=["POST"])
def store_news():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['title', 'text'])
        if not file_exists:
            writer.writeheader()
        writer.writerow({'title': data['title'], 'text': data['text']})
    
    return jsonify({"status": "success", "stored": data})
