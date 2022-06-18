from celery import Celery
import os

celery_app = Celery(
    __name__,
    broker=os.getenv("REDIS_BROKER_URL"),
    backend=os.getenv("REDIS_RESULT_URL"),
    include=["app.tasks"],
)
