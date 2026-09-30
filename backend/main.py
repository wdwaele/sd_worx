from fastapi import FastAPI, WebSocket
from pydantic import BaseModel
from typing import List

app = FastAPI()

class GraphNode(BaseModel):
    id: str
    label: str
    group: str
    details: str

class GraphEdge(BaseModel):
    source: str
    target: str
    relationship: str

class GraphUpdateChunk(BaseModel):
    nodes: List[GraphNode]
    edges: List[GraphEdge]
    thought: str

@app.websocket("/ws/graph")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            # Process data and send updates
            await websocket.send_json({
                "type": "NODE_ADDED",
                "payload": {}
            })
    except Exception as e:
        await websocket.send_json({"type": "ERROR", "payload": str(e)})
    finally:
        await websocket.close()
