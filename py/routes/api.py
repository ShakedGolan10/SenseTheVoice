from fastapi import APIRouter, UploadFile, File, HTTPException
from py.services.voice_recog import VoiceRecognitionService
from schemas.response import TranscriptionResponse

api_router = APIRouter()

# Initialize the service when needed, not at module level
voice_service = None

@api_router.post("/transcribe", response_model=TranscriptionResponse)  # Using the class directly
async def transcribe_audio(audio_file: UploadFile = File(...)):
    global voice_service
    if voice_service is None:
        voice_service = VoiceRecognitionService()
        
    if not audio_file.content_type.startswith('audio/'):
        raise HTTPException(status_code=400, detail="File must be an audio file")
    
    try:
        content = await audio_file.read()
        transcription = await voice_service.transcribe(content)
        return TranscriptionResponse(text=transcription)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))