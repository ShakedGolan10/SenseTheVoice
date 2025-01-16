import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import os

os.environ["PATH"] += os.pathsep + "/usr/bin/ffmpeg"  # Replace with the actual path to ffmpeg

class VoiceRecognitionService:
    def __init__(self):
        # Use GPU if available
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

        model_id = "openai/whisper-large-v3"

        # Load the model and processor
        self.model = AutoModelForSpeechSeq2Seq.from_pretrained(
            model_id,
            torch_dtype=torch_dtype,
            use_safetensors=True
        ).to(self.device)  # Move model to GPU or CPU

        self.processor = AutoProcessor.from_pretrained(model_id)

        # Initialize the pipeline for transcription
        self.pipe = pipeline(
            "automatic-speech-recognition",
            model=self.model,
            tokenizer=self.processor.tokenizer,
            feature_extractor=self.processor.feature_extractor,
            torch_dtype=torch_dtype,
            device=0 if torch.cuda.is_available() else -1  # 0 for GPU, -1 for CPU
        )

    async def transcribe(self, audio_content: bytes, language: str = None, return_timestamps: bool = False):
        # Transcribe audio content to text
        try:
            # Save the audio content temporarily to a file since the pipeline expects file paths
            temp_file = "temp_audio.wav"
            with open(temp_file, "wb") as f:
                f.write(audio_content)

            # Prepare additional arguments for the pipeline
            generate_kwargs = {}
            if language:
                generate_kwargs["language"] = language

            if return_timestamps:
                generate_kwargs["return_timestamps"] = "word"

            # Perform transcription
            result = self.pipe(temp_file, generate_kwargs=generate_kwargs)

            # Clean up the temporary file
            os.remove(temp_file)

            return result if return_timestamps else result["text"]

        except Exception as e:
            raise ValueError(f"Failed to transcribe audio: {str(e)}")
