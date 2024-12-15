FROM python:3.11-slim

WORKDIR /app

# Устанавливаем системные зависимости для сборки psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/

EXPOSE 8000