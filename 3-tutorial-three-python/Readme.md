# Tutorial 3

https://www.rabbitmq.com/tutorials/tutorial-three-python.html

Log receiver is deployed as 4 replicated containers, waiting for connections.

Emitter is deployed as a container, placing tasks to the queue in 'fanout' mode.

The sender task creation is performed in a delayed loop in `loop-python.sh`.




## Deployment

To run the containers, execute the following command from within the tutorial directory.
```
docker-compose up --build
```

Output will display on the terminal.