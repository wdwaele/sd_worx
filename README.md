# Real-Time Reactive Graph Viewer & Streaming Research Canvas

Een interactieve full-stack applicatie gebouwd met **FastAPI**, **PydanticAI** en **React + Vite** om real-time kennisgrafieken te genereren en visualiseren via WebSockets.

---

## Architectuur & Functies

- **Backend:**
  - FastAPI met async WebSocket endpoint (`/ws/graph`).
  - PydanticAI agent orchestratie met Pydantic validatiemodellen (`GraphNode`, `GraphEdge`, `GraphUpdateChunk`).
  - Ondersteuning voor LLM integratie (OpenAI / Gemini / Anthropic) én een ingebouwde heuristische search tool fallback als er geen API key is geconfigureerd.
  - Streaming protocol met gestructureerde events: `AGENT_THOUGHT`, `NODE_ADDED`, `EDGE_ADDED`, `COMPLETE` en `ERROR`.

- **