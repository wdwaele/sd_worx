# Real-Time Reactive Graph Viewer & Streaming Research Canvas

Een interactieve full-stack applicatie gebouwd met **FastAPI**, **PydanticAI** en **React + Vite** om real-time kennisgrafieken te genereren en visualiseren via WebSockets.

### 1. SYSTEM ARCHITECTURE & TECH STACK

**Backend Stack:**
- **Framework:** FastAPI
- **Agent Orchestration:** PydanticAI
- **Streaming Protocol:** WebSockets (or SSE) for streaming real-time graph nodes and execution thoughts.

**Frontend Stack:**
- **Framework:** React + Vite + TypeScript
- **State & Data Fetching:** Zustand or React Query + WebSocket custom hook
- **UI Components:** Tailwind CSS, Lucide Icons, Shadcn UI
- **Graph Visualization:** `react-force-graph-2d` (Ensure dynamic `import()` or dynamic client-side loading to avoid SSR/window undefined issues)

### 2. BACKEND REQUIREMENTS (FastAPI + PydanticAI)

1. **Pydantic Data Models:**
   Define strict Pydantic schemas for graph structures:
   - `GraphNode`: `{ id: str, label: str, group: str, details: str }`
   - `GraphEdge`: `{ source: str, target: str, relationship: str }`
   - `GraphUpdateChunk`: `{ nodes: list[GraphNode], edges: list[GraphEdge], thought: str }`

2. **PydanticAI Agent Setup:**
   - Define a PydanticAI Agent designed to extract structured entity-relationship graphs from user prompts or documents.
   - Configure the agent using Pydantic models for validated graph outputs.
   - Implement tool-calling / web-search capability if applicable, allowing the agent to continuously discover and return new graph connections.

3. **WebSocket/Streaming Endpoint (`/ws/graph`):**
   - Accept a user query via WebSocket.
   - Stream back real-time state updates in JSON format as the agent reasons and executes tool calls:
     ```json
     {
       "type": "NODE_ADDED" | "EDGE_ADDED" | "AGENT_THOUGHT" | "COMPLETE",
       "payload": { ... }
     }
     ```
   - Ensure error handling gracefully sends an error payload over WebSocket if validation fails.

### 3. FRONTEND REQUIREMENTS (React + react-force-graph-2d)

1. **Reactive Graph Visualization Component:**
   - Integrate `react-force-graph-2d` into a responsive canvas area.
   - Implement smooth node merging and canvas force-refresh when new nodes/edges arrive from the backend WebSocket stream without freezing or full canvas resets.
   - Color-code graph nodes automatically based on their `group` attribute.
   - Render directional link particles or labeled directional lines (`linkDirectionalParticles={2}`, `linkLabel="relationship"`).
   - Customize `nodeCanvasObject` to render crisp text labels next to or inside graph nodes.

2. **Interactive Node Inspector (Sidebar/Drawer):**
   - Clicking a node highlights it and opens a details panel showing its `id`, `label`, `group`, and extended `details` text provided by the backend.
   - Add a focus/zoom button using `graphRef.current.centerAt()` and `zoom()` to smooth-pan to the selected node.

3. **Live Streaming Output & Controls Panel:**
   - Provide a chat input bar for the user to type research topics or prompts.
   - Include a live "Thinking / Thought Trace" terminal view showing streaming updates from the agent in real time.
   - Include controls to pause/resume the simulation, auto-fit view (`zoomToFit()`), and clear the canvas.

### 4. IMPLEMENTATION INSTRUCTIONS
- Ensure clean separation of concerns: modular backend routes, explicit Pydantic schemas, and typed React components.
- Write robust handling for WebSocket connection open/close/reconnect events.
- Provide clear setup instructions and run commands (`uvicorn` for backend, `vite` for frontend) in a root `README.md`.
