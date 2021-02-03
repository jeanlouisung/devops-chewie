FROM python:3.7-alpine

WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt --no-cache-dir

COPY . .

CMD uvicorn calculator:app --host 0.0.0.0 --port 8000
