# Distributed computation using Celery and FastAPI
I used project structure from that [post](https://hazelement.github.io/distributed-task-with-celery.html).

This is my small project in which I learned how to parallelize computations 
using Celery task queue.

What is used here:
- FastAPI 
- Celery 
- RabbitMQ
- Flower
- Docker

The program calculates prime numbers on a certain interval. 

It consists of 3 parts: producer (FastAPI client sending tasks to queue), 
consumer (Celery queue executing tasks) and Celery task definition (namely
the directory `celery_tasks`). The idea implies that 
producer and consumer are two different repositories 
and that they both share the 3rd one, where tasks structure is described.

### Usage
1. Install Docker compose - [official guide](https://docs.docker.com/compose/install/)
2. Clone this project
3. Run containers using docker-compose
```zsh
docker-compose up 
```
   Run containers using Docker Swarm
```zsh
docker-compose build
docker swarm init 
docker stack deploy --compose-file=docker-compose.yml distributed_calculation
# to remove containers
# docker stack rm distributed_calculation  
# docker swarm leave --force
```
5. Go to `'http://127.0.0.1:8000/docs'` to try out API 
or visit `'http:/127.0.0.1:5000'` to observe Celery workers in Flower

### API reference
There are only two endpoints:
- `'/ping'`: returns message 'OK' if API is accessed
- `'/prime-numbers/{start}/{end}''`: gets two integers (start and end 
of the interval), returns a list of found prime numbers
