# Tutorial 1

https://www.rabbitmq.com/tutorials/tutorial-one-python.html

Receiver is deployed as a container, waiting for connections.

Sender is deployed as another container which runs send.py on container start.

The sender container will restart each time because there is nothing to keep it running.

As the sender container restarts, send.py is called again.

## Deployment

To run the containers, execute the following command from within the tutorial directory.
```
docker-compose up --build
```

Output will display on the terminal.