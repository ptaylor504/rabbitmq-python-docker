FROM python:3.8

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

COPY app /app
ENTRYPOINT ["python3", "/app/receive.py"]
