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

## Architectuur & Functies

- **Backend:**
  - FastAPI met async WebSocket endpoint (`/ws/graph`).
  - PydanticAI agent orchestratie met Pydantic validatiemodellen (`GraphNode`, `GraphEdge`, `GraphUpdateChunk`).
  - Ondersteuning voor LLM integratie (OpenAI / Gemini / Anthropic) én een ingebouwde heuristische search tool fallback als er geen API key is geconfigureerd.
  - Streaming protocol met gestructureerde events: `AGENT_THOUGHT`, `NODE_ADDED`, `EDGE_ADDED`, `COMPLETE` en `ERROR`.

- **
