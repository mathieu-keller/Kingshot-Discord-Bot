FROM python:3.14.0-slim
LABEL authors="mathieu"
WORKDIR /app
COPY . .
ENTRYPOINT ["python", "main.py", "--no-update"]