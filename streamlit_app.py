import streamlit as st
import asyncio
import websockets
import json
from streamlit_agraph import agraph, Node, Edge, Config

st.title("Real-time Graph Viewer")

nodes = []
edges = []

async def fetch_graph_data():
    uri = "ws://127.0.0.1:8000/ws/graph"
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            data = json.loads(message)
            if data["type"] == "NODE_ADDED":
                for node in data["payload"]["nodes"]:
                    nodes.append(Node(id=node["id"], label=node["label"], size=400))
                for edge in data["payload"]["edges"]:
                    edges.append(Edge(source=edge["source"], target=edge["target"], label=edge["relationship"]))
            elif data["type"] == "ERROR":
                st.error(f"WebSocket error: {data['payload']}")

asyncio.run(fetch_graph_data())

config = Config(width=800, height=600, directed=True, nodeHighlightBehavior=True, highlightColor="#F7A7A6", collapsible=True)
agraph(nodes=nodes, edges=edges, config=config)
