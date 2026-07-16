FROM python:3.13-slim

WORKDIR /app

# System deps needed for bcrypt/cryptography build if wheels aren't available
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# SQLite DB file will live in /app/data - mount a volume here to persist it
RUN mkdir -p /app/data
ENV DATABASE_URL=sqlite:////app/data/taskmanager.db

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
