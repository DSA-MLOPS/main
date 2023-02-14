import asyncio
from datetime import datetime
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await websocket.send_text(now)
        await asyncio.sleep(1)
