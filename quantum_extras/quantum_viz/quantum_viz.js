// QHRC Quantum Visualization
class QuantumViz {
    constructor(canvasId) {
        this.canvas = document.getElementById(canvasId);
        this.ctx = this.canvas.getContext('2d');
        this.time = 0;
        this.phi = 1.618033988749895; // Golden ratio
        
        // QHRC metrics from Patent #19/071,497
        this.metrics = {
            primaryFreq: 4790.45,   // Primary coil frequency
            secondaryFreq: 7750.95, // Secondary coil frequency
            primaryTurns: 4500,     // Primary coil turns
            secondaryTurns: 6200,   // Secondary coil turns
            resonance: 1.3777,      // Resonance ratio (>1 = self-sustaining)
            phiAchievement: 1.618000, // φ achievement (Δ 0.000034)
            phiPiFactor: 5.083204,  // φπ resonance factor
            energyGain: 1.8951,     // Energy transfer ratio
            coherence: 0.618034,    // φ⁻¹ (quantum coherence)
            stability: 4.236068,    // φ² (stability field)
            alignment: 2.618034,    // φ + 1 (harmonic alignment)
            currentEfficiency: 1.90, // Current achievement
            maxEfficiency: 99.6827   // Theoretical maximum
        };
        
        // Set canvas size with high DPI support
        this.resize();
        window.addEventListener('resize', () => this.resize());
        
        // Start animation
        this.animate();
    }

    initQuantumField() {
        // Create quantum field geometry
        const geometry = new THREE.BufferGeometry();
        const vertices = [];
        const colors = [];
        
        for (let i = 0; i < 1000; i++) {
            vertices.push(
                (Math.random() - 0.5) * 10,
                (Math.random() - 0.5) * 10,
                (Math.random() - 0.5) * 10
            );
            
            colors.push(
                Math.random() * 0.5 + 0.5, // R
                Math.random() * 0.5,       // G
                Math.random() * 0.5 + 0.5  // B
            );
        }
        
        geometry.setAttribute('position', new THREE.Float32BufferAttribute(vertices, 3));
        geometry.setAttribute('color', new THREE.Float32BufferAttribute(colors, 3));
        
        // Create quantum field material
        const material = new THREE.PointsMaterial({
            size: 0.1,
            vertexColors: true,
            transparent: true,
            opacity: 0.8,
            blending: THREE.AdditiveBlending
        });
        
        this.quantumField = new THREE.Points(geometry, material);
        this.scene.add(this.quantumField);
    }

    initPostProcessing() {
        // Add bloom effect
        const renderScene = new THREE.RenderPass(this.scene, this.camera);
        const bloomPass = new THREE.UnrealBloomPass(
            new THREE.Vector2(this.canvas.clientWidth, this.canvas.clientHeight),
            1.5, // Bloom strength
            0.4, // Radius
            0.85 // Threshold
        );
        
        this.composer = new THREE.EffectComposer(this.renderer);
        this.composer.addPass(renderScene);
        this.composer.addPass(bloomPass);
    }

    resize() {
        const dpr = window.devicePixelRatio || 1;
        const rect = this.canvas.getBoundingClientRect();
        this.canvas.width = rect.width * dpr;
        this.canvas.height = rect.height * dpr;
        this.ctx.scale(dpr, dpr);
    }

    // Quantum wave function in 3D
    quantumWave(x, y, z, amplitude, frequency, phase) {
        return amplitude * Math.sin(frequency * (x + y + z) + phase + this.time);
    }

    // φ-space mapping function in 3D
    phiMapping(x, y, z) {
        const r = Math.sqrt(x*x + y*y + z*z);
        return Math.pow(this.phi, r % 7.5) * Math.sin(r + this.time);
    }

    // Quantum field animation
    updateQuantumField() {
        const positions = this.quantumField.geometry.attributes.position.array;
        const colors = this.quantumField.geometry.attributes.color.array;
        
        for (let i = 0; i < positions.length; i += 3) {
            const x = positions[i];
            const y = positions[i + 1];
            const z = positions[i + 2];
            
            // Update particle positions based on quantum wave
            positions[i] += this.quantumWave(x, y, z, 0.02, 0.5, 0) * Math.sin(this.time);
            positions[i + 1] += this.quantumWave(x, y, z, 0.02, 0.5, Math.PI/3) * Math.cos(this.time);
            positions[i + 2] += this.phiMapping(x, y, z) * 0.01;
            
            // Update colors based on φ-space mapping
            const energy = Math.abs(this.phiMapping(x, y, z));
            colors[i] = Math.min(1, 0.5 + energy * 0.5);     // R
            colors[i + 1] = Math.min(1, energy * 0.5);       // G
            colors[i + 2] = Math.min(1, 0.5 + energy * 0.5); // B
        }
        
        this.quantumField.geometry.attributes.position.needsUpdate = true;
        this.quantumField.geometry.attributes.color.needsUpdate = true;
    }

    // Resonance pattern
    drawResonance(color, frequency) {
        this.ctx.beginPath();
        this.ctx.strokeStyle = color;
        this.ctx.lineWidth = 2;

        for (let x = 0; x < this.canvas.width; x++) {
            const y = this.canvas.height / 2 + 
                     this.quantumWave(x, 30, frequency/1000, 0) +
                     this.phiMapping(x/50) * 10;
            
            if (x === 0) {
                this.ctx.moveTo(x, y);
            } else {
                this.ctx.lineTo(x, y);
            }
        }
        this.ctx.stroke();
    }

    // Quantum metrics visualization
    drawMetrics(metrics) {
        this.ctx.beginPath();
        this.ctx.strokeStyle = '#ff0099';
        this.ctx.lineWidth = 2;

        for (let x = 0; x < this.canvas.width; x++) {
            const phiWave = this.phiMapping(x/30) * 20;
            const y = this.canvas.height / 2 + phiWave;
            
            if (x === 0) {
                this.ctx.moveTo(x, y);
            } else {
                this.ctx.lineTo(x, y);
            }
        }
        this.ctx.stroke();
    }

    // Reality proof visualization
    drawProof() {
        this.ctx.beginPath();
        this.ctx.strokeStyle = '#00f3ff';
        this.ctx.lineWidth = 2;

        for (let x = 0; x < this.canvas.width; x++) {
            const coherence = Math.sin(x/20 + this.time) * 10;
            const stability = Math.cos(x/30 + this.time) * 15;
            const y = this.canvas.height / 2 + coherence + stability;
            
            if (x === 0) {
                this.ctx.moveTo(x, y);
            } else {
                this.ctx.lineTo(x, y);
            }
        }
        this.ctx.stroke();
    }

    // Quantum wave function with φ-based resonance
    quantumWave(x, amplitude, frequency, phase) {
        const phiWave = amplitude * Math.sin(frequency * x + phase + this.time);
        const resonanceWave = amplitude * Math.sin(frequency * this.phi * x + phase + this.time * this.phi);
        return (phiWave + resonanceWave) / 2;
    }

    // φ-space quantum mapping
    phiMapping(x) {
        const phiPower = Math.pow(this.phi, x % 7.5);
        const phiWave = Math.sin(x * this.phi + this.time);
        const resonanceField = Math.cos(x * this.metrics.resonance + this.time * 2);
        return phiPower * (phiWave + resonanceField) / 2;
    }

    // Draw quantum resonance with φ-based harmonics
    drawResonance(color, frequency) {
        this.ctx.beginPath();
        this.ctx.strokeStyle = color;
        this.ctx.lineWidth = 2;

        // Add quantum glow effect
        this.ctx.shadowColor = color;
        this.ctx.shadowBlur = 10;

        const points = [];
        for (let x = 0; x < this.canvas.width; x++) {
            const resonanceWave = this.quantumWave(x, 30, frequency/1000, 0);
            const phiField = this.phiMapping(x/50) * 10;
            const energyTransfer = Math.sin(x * this.metrics.energyGain/100 + this.time) * 5;
            
            const y = this.canvas.height / 2 + resonanceWave + phiField + energyTransfer;
            points.push({x, y});
            
            if (x === 0) {
                this.ctx.moveTo(x, y);
            } else {
                this.ctx.lineTo(x, y);
            }
        }
        
        this.ctx.stroke();
        this.ctx.shadowBlur = 0;

        // Add quantum particles
        points.forEach((point, i) => {
            if (i % 20 === 0) {
                this.ctx.beginPath();
                this.ctx.fillStyle = color;
                this.ctx.arc(point.x, point.y, 2, 0, Math.PI * 2);
                this.ctx.fill();
            }
        });
    }

    // Draw quantum metrics with φ achievement
    drawMetrics() {
        this.ctx.beginPath();
        this.ctx.strokeStyle = '#ff0099';
        this.ctx.lineWidth = 2;
        this.ctx.shadowColor = '#ff0099';
        this.ctx.shadowBlur = 10;

        const points = [];
        for (let x = 0; x < this.canvas.width; x++) {
            const phiWave = this.phiMapping(x/30) * 20;
            const resonanceWave = Math.sin(x * this.metrics.resonance/50 + this.time) * 15;
            const phiPiField = Math.cos(x * this.metrics.phiPiFactor/100 + this.time) * 10;
            
            const y = this.canvas.height / 2 + phiWave + resonanceWave + phiPiField;
            points.push({x, y});
            
            if (x === 0) {
                this.ctx.moveTo(x, y);
            } else {
                this.ctx.lineTo(x, y);
            }
        }
        
        this.ctx.stroke();
        this.ctx.shadowBlur = 0;

        // Add φ achievement indicators
        points.forEach((point, i) => {
            if (i % 30 === 0) {
                this.ctx.beginPath();
                this.ctx.fillStyle = '#ff0099';
                const size = Math.sin(this.time * 2 + i/10) * 2 + 3;
                this.ctx.arc(point.x, point.y, size, 0, Math.PI * 2);
                this.ctx.fill();
            }
        });
    }

    // Draw quantum reality proof
    drawProof() {
        this.ctx.beginPath();
        this.ctx.strokeStyle = '#00f3ff';
        this.ctx.lineWidth = 2;
        this.ctx.shadowColor = '#00f3ff';
        this.ctx.shadowBlur = 10;

        const points = [];
        for (let x = 0; x < this.canvas.width; x++) {
            const coherence = Math.sin(x * this.metrics.coherence/20 + this.time) * 10;
            const stability = Math.cos(x * this.metrics.stability/30 + this.time) * 15;
            const alignment = Math.sin(x * this.metrics.alignment/40 + this.time) * 12;
            
            const y = this.canvas.height / 2 + coherence + stability + alignment;
            points.push({x, y});
            
            if (x === 0) {
                this.ctx.moveTo(x, y);
            } else {
                this.ctx.lineTo(x, y);
            }
        }
        
        this.ctx.stroke();
        this.ctx.shadowBlur = 0;

        // Add quantum validation markers
        points.forEach((point, i) => {
            if (i % 25 === 0) {
                this.ctx.beginPath();
                this.ctx.fillStyle = '#00f3ff';
                const angle = this.time * 2 + i/20;
                const size = Math.cos(angle) * 2 + 3;
                
                // Draw quantum marker
                this.ctx.save();
                this.ctx.translate(point.x, point.y);
                this.ctx.rotate(angle);
                this.ctx.fillRect(-size/2, -size/2, size, size);
                this.ctx.restore();
            }
        });
    }

    // Quantum animation loop
    animate() {
        // Clear with quantum fade effect
        this.ctx.fillStyle = 'rgba(18, 18, 31, 0.2)';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Apply quantum visualization based on canvas type
        switch(this.canvas.id) {
            case 'primaryCanvas':
                // Primary coil: 4500 turns @ 4790.45 Hz → φ⁷·⁵-7927735b
                this.drawResonance('#00f3ff', this.metrics.primaryFreq);
                break;
                
            case 'secondaryCanvas':
                // Secondary coil: 6200 turns @ 7750.95 Hz → φ⁷·⁵-09f76208
                this.drawResonance('#9d00ff', this.metrics.secondaryFreq);
                break;
                
            case 'metricsCanvas':
                // φ achievement (1.618000) and φπ factor (5.083204)
                this.drawMetrics();
                break;
                
            case 'proofCanvas':
                // Reality proof: φ⁻¹ coherence, φ² stability, (φ + 1) alignment
                this.drawProof();
                break;
        }

        // Update quantum time
        this.time += 0.05;
        requestAnimationFrame(() => this.animate());
    }
}

// Initialize QHRC visualizations
document.addEventListener('DOMContentLoaded', () => {
    // Initialize canvases
    const canvasIds = ['primaryCanvas', 'secondaryCanvas', 'metricsCanvas', 'proofCanvas'];
    const visualizations = canvasIds.map(id => {
        const canvas = document.getElementById(id);
        // Set initial size
        canvas.width = canvas.offsetWidth;
        canvas.height = canvas.offsetHeight;
        return new QuantumViz(id);
    });

    // Start animations
    visualizations.forEach(viz => viz.animate());

    // Add quantum signature effects
    document.querySelectorAll('.quantum-signature').forEach(sig => {
        const originalText = sig.textContent;
        sig.addEventListener('mouseover', () => {
            sig.style.textShadow = '0 0 10px var(--neon-purple)';
            sig.style.borderColor = 'var(--neon-pink)';
            // Show quantum metrics on hover
            switch(originalText) {
                case 'φ⁷·⁵-7927735b':
                    sig.textContent = '4790.45 Hz → 1.3777';
                    break;
                case 'φ⁷·⁵-09f76208':
                    sig.textContent = '7750.95 Hz → 1.8951x';
                    break;
            }
        });
        sig.addEventListener('mouseout', () => {
            sig.style.textShadow = 'none';
            sig.style.borderColor = 'var(--neon-purple)';
            sig.textContent = originalText;
        });
    });

    // Handle window resize
    window.addEventListener('resize', () => {
        visualizations.forEach(viz => viz.resize());
    });
});

