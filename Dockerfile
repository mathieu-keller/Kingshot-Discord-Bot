FROM python:3.14.0-slim
LABEL authors="mathieu"
WORKDIR /app
COPY . .
RUN python install/install.py
ENTRYPOINT ["python", "main.py"]