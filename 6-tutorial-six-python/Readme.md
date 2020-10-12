# Tutorial 6

https://www.rabbitmq.com/tutorials/tutorial-six-python.html

RPC server is deployed as 2 replicated containers, waiting for connections.

RPC client is deployed as a container, generating random numbers between 1 and 10 for the Fibonacci calculator service.

The client task creation is performed in a delayed loop in `loop-python.sh`.




## Deployment

To run the containers, execute the following command from within the tutorial directory.
```
docker-compose up --build
```

Output will display on the terminal.