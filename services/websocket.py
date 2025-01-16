from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import Dict, Set
import json

class WebSocketManager:
    def __init__(self):
        self.router = APIRouter()
        self.active_connections: Dict[str, Set[WebSocket]] = {}
        
        @self.router.websocket("/ws/{client_id}")
        async def websocket_endpoint(websocket: WebSocket, client_id: str):
            await self.connect(websocket, client_id)
            try:
                while True:
                    data = await websocket.receive_text()
                    await self.broadcast(client_id, data)
            except WebSocketDisconnect:
                await self.disconnect(websocket, client_id)

    async def connect(self, websocket: WebSocket, client_id: str):
        await websocket.accept()
        if client_id not in self.active_connections:
            self.active_connections[client_id] = set()
        self.active_connections[client_id].add(websocket)

    async def disconnect(self, websocket: WebSocket, client_id: str):
        self.active_connections[client_id].remove(websocket)
        if not self.active_connections[client_id]:
            del self.active_connections[client_id]

    async def broadcast(self, client_id: str, message: str):
        if client_id in self.active_connections:
            for connection in self.active_connections[client_id]:
                await connection.send_text(message)
