from transformers import pipeline

# Initialize the Hugging Face model
recognizer = pipeline("automatic-speech-recognition")

def transcribe_audio(audio_data):
    """
    Transcribe the given audio data using the Hugging Face model.
    :param audio_data: Binary audio data
    :return: Transcribed text
    """
    result = recognizer(audio_data)
    return result['text']