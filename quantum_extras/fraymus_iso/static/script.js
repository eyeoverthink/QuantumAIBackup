document.getElementById('queryForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const query = document.getElementById('query').value;
    const resultsDiv = document.getElementById('results');
    
    try {
        resultsDiv.innerHTML = '<div class="text-center"><div class="spinner-border text-light" role="status"></div></div>';
        
        const response = await fetch('/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query }),
        });
        
        const data = await response.json();
        
        if (response.ok) {
            resultsDiv.innerHTML = `
                <div class="result-item">
                    <h4>Query</h4>
                    <pre>${data.query}</pre>
                    
                    <h4>Quantum State</h4>
                    <pre class="quantum-state">${JSON.stringify(data.quantum_state, null, 2)}</pre>
                    
                    <h4>Electrical Brain Analysis</h4>
                    <pre class="electrical-brain">${JSON.stringify(data.electrical_brain, null, 2)}</pre>
                    
                    <h4>Fractal DNA Storage</h4>
                    <pre class="fractal-dna">${JSON.stringify(data.fractal_dna, null, 2)}</pre>
                </div>
            `;
        } else {
            throw new Error(data.error || 'Failed to process query');
        }
    } catch (error) {
        resultsDiv.innerHTML = `
            <div class="alert alert-danger">
                Error: ${error.message}
            </div>
        `;
    }
});
