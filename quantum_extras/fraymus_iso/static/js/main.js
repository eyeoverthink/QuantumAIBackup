// Initialize Plotly plot
const plotlyConfig = {
    responsive: true,
    displayModeBar: false
};

const plotlyLayout = {
    paper_bgcolor: 'rgba(0,0,0,0)',
    plot_bgcolor: 'rgba(0,0,0,0)',
    margin: { t: 10, r: 10, b: 30, l: 40 },
    showlegend: false,
    xaxis: {
        gridcolor: '#333',
        color: '#fff',
        title: 'Quantum State'
    },
    yaxis: {
        gridcolor: '#333',
        color: '#fff',
        title: 'Amplitude'
    }
};

// Initialize empty plot when document is ready
document.addEventListener('DOMContentLoaded', () => {
    Plotly.newPlot('quantumStateViz', [{
        y: Array(16).fill(0.25),
        type: 'bar',
        marker: {
            color: '#00e5ff'
        }
    }], plotlyLayout, plotlyConfig);
});

// Update quantum state visualization
function updateQuantumState(state) {
    const amplitudes = state.map(s => s.real);
    
    Plotly.react('quantumStateViz', [{
        y: amplitudes,
        type: 'bar',
        marker: {
            color: '#00e5ff'
        }
    }], plotlyLayout, plotlyConfig);
}

// Update electrical metrics
function updateElectricalMetrics(electrical) {
    document.getElementById('voltage').textContent = `${electrical.voltage.toFixed(2)} V`;
    document.getElementById('current').textContent = `${electrical.current.toExponential(2)} A`;
    document.getElementById('power').textContent = `${electrical.power.toExponential(2)} W`;
    document.getElementById('resistance').textContent = `${electrical.resistance.toExponential(2)} Ω`;
}

// Update temporal metrics
function updateTemporalMetrics(quantum_harmonic_output) {
    document.getElementById('temporalShift').textContent = 
        `${quantum_harmonic_output.temporal_shift.toExponential(2)} s`;
    document.getElementById('quantumSignature').textContent = 
        quantum_harmonic_output.quantum_signature.slice(0, 8) + '...';
}

// Update metrics display
function updateMetrics(data) {
    document.getElementById('quantumCoherence').textContent = 
        data.quantum_coherence.toFixed(4);
    document.getElementById('fractalStability').textContent = 
        data.fractal_stability.toFixed(4);
    document.getElementById('entanglementDepth').textContent = 
        data.entanglement_depth.toFixed(4);
    document.getElementById('patternStrength').textContent = 
        data.pattern_strength.toFixed(4);
}

// Update visualization
function updateVisualization(data) {
    const quantumTrace = {
        y: data.quantum_state,
        type: 'scatter',
        mode: 'lines',
        line: { color: '#6200ea', width: 2 }
    };

    const nodeTrace = {
        y: data.node_outputs,
        type: 'scatter',
        mode: 'lines',
        line: { color: '#00e5ff', width: 2 }
    };

    Plotly.react('patternPlot', [quantumTrace, nodeTrace], plotlyLayout, plotlyConfig);
}

// Process data
async function processData() {
    const inputData = document.getElementById('inputData').value;
    const brainType = document.getElementById('brainType').value;
    const processingStatus = document.getElementById('processingStatus');

    if (!inputData) {
        processingStatus.textContent = 'Please enter some data to process';
        processingStatus.className = 'status-error';
        return;
    }

    processingStatus.textContent = 'Processing quantum data...';
    processingStatus.className = 'status-info processing';

    try {
        const response = await fetch('/api/quantum/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                data: inputData,
                brainType: brainType
            })
        });

        const result = await response.json();

        if (result.success) {
            updateMetrics(result);
            updateVisualization(result);
            updateQuantumState(result.quantum_state);
            updateElectricalMetrics(result.electrical_brain);
            updateTemporalMetrics(result.electrical_brain.quantum_harmonic_output);
            processingStatus.textContent = 'Quantum processing complete';
            processingStatus.className = 'status-success';
        } else {
            processingStatus.textContent = `Error: ${result.error}`;
            processingStatus.className = 'status-error';
        }
    } catch (error) {
        processingStatus.textContent = `Error: ${error.message}`;
        processingStatus.className = 'status-error';
    }
}
