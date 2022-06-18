## Demo application for FastAPI, Celery, Flower

Demo app for FastAPI with Celery and Flower.   
[Celery](https://docs.celeryq.dev/en/stable/) is distributed task queues for offloading task from application to celery-workers.  
[Flower](!https://flower.readthedocs.io/en/latest/)is a web based tool for monitoring and administrating Celery clusters. 


### How to run
- Clone the repo
- Make sure  docker and docker-compose (https://docs.docker.com/compose/install/) are installed
- `cd` into the cloned directory
- ```docker compose build```
- ```docker compose up```

Go to `http://localhost:8004/hash/{string}` to create a task
Go to `http://localhost:8004/result/{task_id}` to fetch task detail.
Go to `http://localhost:5555` to monitor celery tasks using flower.