import React, { useEffect, useRef, useState } from 'react';
import ForceGraph2D from 'react-force-graph-2d';

const App: React.FC = () => {
    const [graphData, setGraphData] = useState({ nodes: [], links: [] });
    const graphRef = useRef<any>();

    useEffect(() => {
        const ws = new WebSocket('ws://localhost:8000/ws/graph');
        ws.onmessage = (event) => {
            const message = JSON.parse(event.data);
            // Handle incoming WebSocket messages
            switch (message.type) {
                case "NODE_ADDED":
                    setGraphData(prevData => ({
                        nodes: [...prevData.nodes, ...message.payload.nodes],
                        links: [...prevData.links, ...message.payload.edges]
                    }));
                    break;
                case "ERROR":
                    console.error("WebSocket error:", message.payload);
                    break;
                default:
                    console.warn("Unknown message type:", message.type);
            }
            }
        };
        return () => ws.close();
    }, []);

    return (
        <div>
            <ForceGraph2D
                ref={graphRef}
                graphData={graphData}
                nodeLabel="label"
                linkDirectionalParticles={2}
                linkLabel="relationship"
            />
        </div>
    );
};

export default App;
