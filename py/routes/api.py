from fastapi import APIRouter, HTTPException
from server.services.voice_recognition import transcribe_audio

router = APIRouter()

@router.post("/transcribe/")
async def transcribe(file: bytes):
    try:
        result = transcribe_audio(file)
        return {"transcription": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))