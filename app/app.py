from celery.result import AsyncResult
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .tasks import calculate_hash

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hash/{value}")
async def send_hash_request(value: str):
    task = calculate_hash.delay(value)
    print(task)
    return JSONResponse({"task_id": task.id})


@app.get("/result/{task_id}")
async def send_hash_request(task_id: str):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result,
    }
    return JSONResponse(result)
