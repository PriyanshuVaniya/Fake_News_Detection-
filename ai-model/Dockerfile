FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
COPY libs/ ./libs/
COPY . .

# Install smaller dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install pre-downloaded heavy libraries from libs/
# RUN pip install --no-cache-dir libs/*

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
