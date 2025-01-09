from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "Voice Recognition API"
    DEBUG_MODE: bool = False
    API_V1_PREFIX: str = "/api/v1"
    CORS_ORIGINS: list[str] = [
        "http://localhost:3000",  # NextJS frontend
        "http://localhost:8000",  # FastAPI docs
    ]
    MODEL_NAME: str
    MODEL_CACHE_DIR: str

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings() -> Settings:
    return Settings()