FROM python:3.11-slim
WORKDIR /app
COPY ./app /app
RUN pip install fastapi uvicorn
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

