from celery import Celery
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

celery_app.conf.task_routes = {
    "tasks.download_youtube_audio_task": {"queue": "audio"},
    "tasks.transform_audio_task": {"queue": "audio"},
}

@celery_app.task(name="tasks.download_youtube_audio_task")
def download_youtube_audio_task(youtube_url, output_path):
    logger.info(f"Starting download_youtube_audio_task with URL: {youtube_url} and output path: {output_path}")
    from backend.services.extract_audio import download_youtube_audio
    return download_youtube_audio(youtube_url, output_path)

@celery_app.task(name="tasks.transform_audio_task")
def transform_audio_task(file_name, mood):
    import os
    from backend.services.transform_audio import change_mood
    from backend.services.save_audio import save_audio
    
    input_path = os.path.join("data/input/", file_name)
    output_path = change_mood(input_path, mood)
    return save_audio(output_path, "data/output/")
