FROM python:3.11-slim
LABEL authors="silvanohu"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/src
CMD ["python", "bot.py"]