from backend.celery_app import celery_app
from celery.result import AsyncResult
import time


task = celery_app.send_task("tasks.download_youtube_audio_task", args=['https://www.youtube.com/watch?v=v6HBZC9pZHQ', 'data/input'])
print(f"Task ID: {task.id}")

while True:
    result = AsyncResult(task.id, app=celery_app)
    print(f"Task Status: {result.status}")
    if result.status == 'SUCCESS':
        print(f"Task Result: {result.result}")
        break
    elif result.status == 'FAILURE':
        print(f"Task Failed: {result.result}")
        break
    time.sleep(1)