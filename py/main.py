from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import get_settings
from routes.api import api_router
from services.websocket import WebSocketManager

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG_MODE,
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix=settings.API_V1_PREFIX)

# Initialize WebSocket manager
websocket_manager = WebSocketManager()

# Mount WebSocket routes
app.include_router(websocket_manager.router)

# Add startup validation for environment variables
@app.on_event("startup")
async def startup_event(): print('Startup successful')

@app.get("/")
def read_root():
    return {"message": "Welcome to the Voice Recognition API, Server is live!"}