# Tutorial 2

https://www.rabbitmq.com/tutorials/tutorial-two-python.html

Worker is deployed as 4 replicated containers, waiting for connections, this worker deliberately delays returns, simulating a task 
that takes a long period of time.

Sender is deployed as a container, placing tasks to the queue.

The sender task creation is performed in a delayed loop in `loop-python.sh`.



## Deployment

To run the containers, execute the following command from within the tutorial directory.
```
docker-compose up --build
```

Output will display on the terminal.

Because of the delay in the worker, the task container closes down before the list queue is finished executing.
