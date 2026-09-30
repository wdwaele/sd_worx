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
            # Simuleer een voorbeeld payload voor testdoeleinden
            example_payload = {
                "nodes": [{"id": "1", "label": "Node 1", "group": "A", "details": "Details about Node 1"}],
                "edges": [{"source": "1", "target": "2", "relationship": "connected to"}]
            }
            await websocket.send_json({
                "type": "NODE_ADDED",
                "payload": example_payload
            })
    except Exception as e:
        await websocket.send_json({"type": "ERROR", "payload": str(e)})
    finally:
        await websocket.close()
