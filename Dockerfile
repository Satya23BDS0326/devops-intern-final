FROM python:3.11-slim

WORKDIR /ap

COPY hello.py .

CMD ["python", "hello.py"]
