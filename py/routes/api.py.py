from fastapi import APIRouter, UploadFile, File, HTTPException
from services.voice_recognition import VoiceRecognitionService
from schemas.response import TranscriptionResponse

api_router = APIRouter()
voice_service = VoiceRecognitionService()

@api_router.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe_audio(audio_file: UploadFile = File(...)):
    if not audio_file.content_type.startswith('audio/'):
        raise HTTPException(status_code=400, detail="File must be an audio file")
    
    try:
        content = await audio_file.read()
        transcription = await voice_service.transcribe(content)
        return TranscriptionResponse(text=transcription)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))