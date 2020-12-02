FROM python:3.8

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

RUN ln -sf /bin/bash /bin/sh
RUN useradd -ms /bin/bash  demo
USER demo
WORKDIR /demo

COPY --chown=demo:demo requirements.txt requirements.txt
COPY --chown=demo:demo . .
#RUN pip install --user -r requirements.txt

#ENV PATH="/home/demo/.local/bin:${PATH}"

USER root
RUN python -m pip install pika
RUN chmod -R 775 /demo/

USER demo

LABEL maintainer="phil taylor" version="1.0.0"

CMD ["python","/demo/app/worker-demo.py"]
#ENTRYPOINT ["python3","/demo/app/worker-demo.py"]
#ENTRYPOINT [ "python" ]