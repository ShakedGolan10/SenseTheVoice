from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from services.voice_recog import VoiceRecognitionService
from services.text_analasys import TextAnalysisService 
from typing import Dict

api_router = APIRouter()

# Initialize the service lazily
voice_service = None
text_analysis_service = None

@api_router.post("/transcribe-and-analyze", response_model=Dict)
async def transcribe_and_analyze_audio(
    audio_file: UploadFile = File(...),
    language: str = Form(None)  # Accept language as a form parameter
):
    global voice_service, text_analysis_service
    if voice_service is None:
        voice_service = VoiceRecognitionService()
    if text_analysis_service is None:
        text_analysis_service = TextAnalysisService()
    
    # Validate the file type
    if not audio_file.content_type.startswith('audio/'):
        raise HTTPException(status_code=400, detail="File must be an audio file")

    try:
        # Transcribe the audio file
        audio_content = await audio_file.read()
        transcription = await voice_service.transcribe(audio_content, language=language)
        print('transcription stage ended')
        
        # Analyze the transcription
        analysis_result = text_analysis_service.analyze_text(transcription)
      
        sentiment_label = analysis_result["sentiment_label"]
        confidence = analysis_result["confidence"]
        
        return {
            "transcription": transcription,
            "analysis": {
                "analysis_result": analysis_result,
                "sentiment_label": sentiment_label,
                "confidence": confidence
            }
        }
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Transcription and analysis failed: {str(e)}")