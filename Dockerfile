FROM python:3.11-slim
LABEL authors="silvanohu"

WORKDIR /app

ENV LOG_LEVEL=INFO
ENV LOG_TO_FILE=False

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY JMdict_e ./JMdict_e

WORKDIR /app/src
CMD ["python", "bot.py"]