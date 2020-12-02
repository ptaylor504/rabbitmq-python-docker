FROM python:3.8

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

RUN ln -sf /bin/bash /bin/sh
RUN useradd -ms /bin/bash  demo
USER demo
WORKDIR /demo

COPY --chown=demo:demo requirements.txt requirements.txt
COPY --chown=demo:demo . .

USER root
RUN python -m pip install pika
RUN chmod -R 775 /demo/

USER demo

LABEL maintainer="phil taylor" version="1.0.0"

CMD ["python","/demo/app/worker-demo.py"]