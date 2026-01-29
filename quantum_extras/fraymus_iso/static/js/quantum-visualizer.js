class QuantumVisualizer {
    constructor() {
        this.chart = null;
        this.initializeEventListeners();
        this.apiUrl = 'http://localhost:8000/process';  // Fixed API endpoint
        this.checkBackendConnection();
    }

    async checkBackendConnection() {
        try {
            const response = await fetch(this.apiUrl, {
                method: 'OPTIONS',
                headers: {
                    'Accept': 'application/json'
                }
            });
            if (response.ok) {
                console.log('Backend connection established');
                this.updateConnectionStatus(true);
            } else {
                throw new Error('Backend server not responding');
            }
        } catch (error) {
            console.error('Backend connection failed:', error);
            this.updateConnectionStatus(false);
        }
    }

    updateConnectionStatus(isConnected) {
        const statusDiv = document.getElementById('connection-status');
        if (!statusDiv) {
            const header = document.querySelector('.quantum-header');
            const status = document.createElement('div');
            status.id = 'connection-status';
            status.className = isConnected ? 'connected' : 'disconnected';
            status.innerHTML = `
                <span class="status-dot"></span>
                <span class="status-text">${isConnected ? 'Connected to Quantum Backend' : 'Backend Connection Failed'}</span>
            `;
            header.appendChild(status);
        } else {
            statusDiv.className = isConnected ? 'connected' : 'disconnected';
            statusDiv.innerHTML = `
                <span class="status-dot"></span>
                <span class="status-text">${isConnected ? 'Connected to Quantum Backend' : 'Backend Connection Failed'}</span>
            `;
        }
    }

    initializeEventListeners() {
        document.getElementById('quantum-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            await this.checkBackendConnection();
            this.processQuantumQuery();
        });
    }

    async processQuantumQuery() {
        const query = document.getElementById('quantum-input').value;
        const loadingIndicator = document.getElementById('loading-indicator');
        const resultContainer = document.getElementById('result-container');

        try {
            loadingIndicator.style.display = 'block';
            resultContainer.style.display = 'none';

            const response = await fetch(this.apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({ query })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || `Failed to fetch (${response.status})`);
            }

            const data = await response.json();
            
            if (data.error) {
                throw new Error(data.error);
            }
            
            this.updateVisualization(data);
            this.updateConnectionStatus(true);
            
            loadingIndicator.style.display = 'none';
            resultContainer.style.display = 'block';
        } catch (error) {
            console.error('Error:', error);
            loadingIndicator.style.display = 'none';
            resultContainer.style.display = 'none';
            this.updateConnectionStatus(false);
            
            // Show error message to user
            const errorDiv = document.createElement('div');
            errorDiv.className = 'metric-card error-card';
            errorDiv.innerHTML = `
                <div class="metric-title">Error</div>
                <div class="metric-value">${error.message}</div>
                <div class="error-details">Check that the quantum backend is running on port 8000</div>
            `;
            
            // Remove any existing error messages
            const existingError = document.querySelector('.error-card');
            if (existingError) {
                existingError.remove();
            }
            
            // Add new error message after the form
            document.getElementById('quantum-form').after(errorDiv);
        }
    }

    updateVisualization(data) {
        // Remove any existing error messages
        const existingError = document.querySelector('.error-card');
        if (existingError) {
            existingError.remove();
        }

        // Update metrics
        this.updateMetric('resonance', data.resonance?.toFixed(4) || 'N/A');
        this.updateMetric('pattern-confidence', data.electrical_brain?.pattern_confidence?.toFixed(4) || 'N/A');
        this.updateMetric('harmonic-resonance', data.electrical_brain?.quantum_harmonic_output?.harmonic_resonance?.toFixed(4) || 'N/A');
        this.updateMetric('temporal-shift', data.electrical_brain?.quantum_harmonic_output?.temporal_shift?.toExponential(4) || 'N/A');

        // Update quantum state visualization
        this.updateQuantumStateChart(data.quantum_state);

        // Update synaptic strengths
        this.updateSynapticStrengths(data.electrical_brain?.synaptic_strength || []);

        // Pulse effect on update
        document.querySelectorAll('.metric-card').forEach(card => {
            card.classList.add('pulse-effect');
            setTimeout(() => card.classList.remove('pulse-effect'), 2000);
        });
    }

    updateMetric(id, value) {
        const element = document.getElementById(id);
        if (element) {
            element.textContent = value;
            element.parentElement.classList.add('pulse-effect');
            setTimeout(() => element.parentElement.classList.remove('pulse-effect'), 2000);
        }
    }

    updateQuantumStateChart(quantumState) {
        if (!quantumState) return;

        const ctx = document.getElementById('quantum-chart').getContext('2d');
        
        const realValues = quantumState.map(state => state.real);
        const imagValues = quantumState.map(state => state.imag);

        if (this.chart) {
            this.chart.destroy();
        }

        this.chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: Array.from({length: quantumState.length}, (_, i) => i + 1),
                datasets: [{
                    label: 'Real Component',
                    data: realValues,
                    borderColor: '#00f0ff',
                    tension: 0.4
                }, {
                    label: 'Imaginary Component',
                    data: imagValues,
                    borderColor: '#ff00f0',
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top',
                        labels: {
                            color: '#ffffff'
                        }
                    }
                },
                scales: {
                    y: {
                        grid: {
                            color: 'rgba(255, 255, 255, 0.1)'
                        },
                        ticks: {
                            color: '#ffffff'
                        }
                    },
                    x: {
                        grid: {
                            color: 'rgba(255, 255, 255, 0.1)'
                        },
                        ticks: {
                            color: '#ffffff'
                        }
                    }
                }
            }
        });
    }

    updateSynapticStrengths(strengths) {
        const container = document.getElementById('synaptic-strengths');
        if (!container) return;

        container.innerHTML = strengths
            .map((strength, index) => `
                <div class="grid-item">
                    <div class="metric-title">Synapse ${index + 1}</div>
                    <div class="metric-value">${strength.toExponential(2)}</div>
                </div>
            `)
            .join('');
    }
}
