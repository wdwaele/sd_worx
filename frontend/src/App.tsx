import React, { useEffect, useRef, useState } from 'react';
import ForceGraph2D from 'react-force-graph-2d';

const App: React.FC = () => {
    const [graphData, setGraphData] = useState({ nodes: [], links: [] });
    const graphRef = useRef();

    useEffect(() => {
        const ws = new WebSocket('ws://localhost:8000/ws/graph');
        ws.onmessage = (event) => {
            const message = JSON.parse(event.data);
            // Handle incoming WebSocket messages
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
