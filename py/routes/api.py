from fastapi import APIRouter, UploadFile, File, HTTPException
from services.voice_recog import VoiceRecognitionService
from schemas.response import TranscriptionResponse

api_router = APIRouter()

# Initialize the service lazily
voice_service = None

@api_router.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe_audio(audio_file: UploadFile = File(...)):
    global voice_service
    if voice_service is None:
        voice_service = VoiceRecognitionService()
    
    # Validate the file type
    if not audio_file.content_type.startswith('audio/'):
        raise HTTPException(status_code=400, detail="File must be an audio file")

    try:
        # Read and transcribe the audio file
        audio_content = await audio_file.read()
        transcription = await voice_service.transcribe(audio_content)
        return TranscriptionResponse(text=transcription)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Transcription failed: {str(e)}")
