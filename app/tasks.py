from .services.hash import my_complex_hash
from .celery_worker import celery_app


@celery_app.task
def calculate_hash(value: str):
    return my_complex_hash(value)
