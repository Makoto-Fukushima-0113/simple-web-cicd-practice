FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

ENV PORT=8080
CMD exec gunicorn -b :$PORT --workers 1 --threads 8 --timeout 0 app.main:app
