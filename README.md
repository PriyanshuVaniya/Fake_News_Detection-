# 🧠 Fake News Detection System

An AI-powered, Dockerized microservices project that detects whether a news article is real or fake using machine learning techniques. The project features an interactive frontend dashboard and robust backend with circuit breaker support for fault tolerance.

---

## 🔍 Overview

This system leverages machine learning and microservices to analyze news articles and classify them as **Real** or **Fake**.  
It consists of five main components, each running in its own Docker container:

- **AI Model Microservice (FastAPI)**: Predicts whether the news is fake or real.
- **Data Collection Microservice (Flask)**: Stores submitted news articles for future retraining.
- **API Gateway (FastAPI)**: Routes requests between frontend and backend with built-in **Circuit Breaker**.
- **Dashboard (Flask)**: Modern UI for users to input news content and view predictions with confidence score.
- **ML Pipeline**: Built with Scikit-learn using Logistic Regression, achieving over 95% accuracy.

---

## 🧱 Architecture

```text
[Dashboard UI] ──> [API Gateway] ──> [AI Model]
                            └────> [Data Collection]

## 📦 Features

- 🧠 **ML Model**: Logistic Regression (95% Accuracy)
- 🔁 **Microservices** (FastAPI + Flask)
- 🐳 **Fully Dockerized Deployment**
- 🌐 **Frontend Dashboard** with confidence meter
- 🛑 **Circuit Breaker** in API Gateway
- 📊 **Confusion Matrix, ROC Curve, Accuracy Graphs**

---

## 🛠️ Technologies Used

| Category         | Tools/Tech                          |
|------------------|--------------------------------------|
| Backend          | Python, Flask, FastAPI               |
| ML Libraries     | Scikit-learn, Pandas, NumPy          |
| Frontend         | HTML, CSS, JavaScript                |
| Containerization | Docker, Docker Compose               |
| Architecture     | Microservices                        |
| DevOps           | Git, GitHub                          |
| Dataset          | Kaggle Fake and Real News Dataset    |

---
## 🧑‍💻 Author

- **Priyanshu Vaniya**
- [GitHub Profile](https://github.com/PriyanshuVaniya)
- Contact: priyanshuvaniya2703@gmail.com

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fake-news-detection.git
cd fake-news-detection
