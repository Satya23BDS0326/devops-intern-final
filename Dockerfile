FROM python:3.11-sli

WORKDIR /app

COPY hello.py .

CMD ["python", "hello.py"]
