from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
from config import get_settings
import torch
import io
import soundfile as sf

class VoiceRecognitionService:
    def __init__(self):
        self.settings = get_settings()
        self.processor, self.model = self._load_model()

    def _load_model(self):
        # Load the processor and model using the environment variable from settings
        processor = Wav2Vec2Processor.from_pretrained(self.settings.MODEL_NAME)
        model = Wav2Vec2ForCTC.from_pretrained(self.settings.MODEL_NAME)
        return processor, model

    async def transcribe(self, audio_content: bytes) -> str:
        # Convert bytes to audio array
        audio_io = io.BytesIO(audio_content)
        audio_array, sample_rate = sf.read(audio_io)

        # Ensure audio is mono and sampled at 16kHz
        if len(audio_array.shape) > 1:
            audio_array = audio_array.mean(axis=1)
        if sample_rate != 16000:
            raise ValueError("Audio sample rate must be 16kHz.")

        # Tokenize and process the input
        input_values = self.processor(audio_array, return_tensors="pt", padding="longest").input_values

        # Get the model logits
        with torch.no_grad():
            logits = self.model(input_values).logits

        # Decode the predicted IDs
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = self.processor.batch_decode(predicted_ids)[0]
        return transcription
