from pydantic import BaseModel

class TranscriptionResponse(BaseModel):
    text: str

__all__ = ['TranscriptionResponse']