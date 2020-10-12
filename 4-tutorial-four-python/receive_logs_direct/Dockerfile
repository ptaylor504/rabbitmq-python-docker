FROM python:3.8

COPY wait-for-it.sh wait-for-it.sh

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

COPY app /app

ENTRYPOINT ["./wait-for-it.sh", "rabbitmq:5672", "--", "python3", "/app/receive_logs_direct.py", "warning", "error", ">", "logs_from_rabbit.log"]
