import asyncio
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse, StreamingResponse
from datetime import datetime

app = FastAPI()

async def send_time(websocket: WebSocket):
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await websocket.send_text(now)
        await asyncio.sleep(1)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    asyncio.create_task(send_time(websocket))

async def stream_data():
    message = "Hello This is streaming example"
    for char in message:
        yield char
        await asyncio.sleep(0.1)
    yield "[DONE]"

@app.get("/stream")
async def stream():
    return StreamingResponse(stream_data(), media_type="text/event-stream")


