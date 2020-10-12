FROM python:3.8

COPY wait-for-it.sh wait-for-it.sh
COPY loop-python.sh loop-python.sh

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

COPY app /app

ENTRYPOINT ["./wait-for-it.sh", "rabbitmq:5672", "--", "bash", "/loop-python.sh"]