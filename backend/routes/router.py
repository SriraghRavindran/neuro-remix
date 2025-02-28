from fastapi import APIRouter,FastAPI, UploadFile, File
import shutil
import os
import logging
from backend.celery_app import celery_app
from backend.services.analyze_audio import analyze_audio
from backend.services.extract_audio import download_youtube_audio
from backend.services.save_audio import save_audio
from backend.services.transform_audio import change_mood
import asyncio

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
router = APIRouter()

UPLOAD_DIR = "data/input/"
OUTPUT_DIR = "data/OUTPUT"

@router.post("/extract")
async def extract_audio(youtube_url: str):
    logger.info(f"Starting download_youtube_audio_task with URL: {youtube_url} and output path: {OUTPUT_DIR}")
    from backend.services.extract_audio import download_youtube_audio
    asyncio.create_task(download_youtube_audio(youtube_url, OUTPUT_DIR))
    return {"message": "Audio extraction has started."}

@router.post("/analyze")
def analyze_uploaded_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    analysis = analyze_audio(file_path)
    return {"analysis": analysis}

@router.post("/transform")
def transform_audio(file_name: str, mood: str):
    from backend.services.transform_audio import change_mood
    from backend.services.save_audio import save_audio
    
    input_path = os.path.join("data/input/", file_name)
    output_path = change_mood(input_path, mood)
    return save_audio(output_path, "data/output/")

@router.get("/download")
def download_audio(file_name: str):
    """Returns the transformed audio file URL."""
    return {"download_url": f"/static/{file_name}"}   
