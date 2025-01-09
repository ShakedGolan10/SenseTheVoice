from transformers import pipeline
from config import get_settings
import torch
import io
import soundfile as sf
import numpy as np

class VoiceRecognitionService:
    def __init__(self):
        self.settings = get_settings()
        self.model = self._load_model()

    def _load_model(self):
        return pipeline(
            "automatic-speech-recognition",
            model=self.settings.MODEL_NAME,
            cache_dir=self.settings.MODEL_CACHE_DIR,
        )

    async def transcribe(self, audio_content: bytes) -> str:
        # Convert bytes to audio array
        audio_io = io.BytesIO(audio_content)
        audio_array, sample_rate = sf.read(audio_io)
        
        # Ensure audio is mono
        if len(audio_array.shape) > 1:
            audio_array = audio_array.mean(axis=1)

        # Process the audio
        result = self.model({"array": audio_array, "sampling_rate": sample_rate})
        return result["text"]
