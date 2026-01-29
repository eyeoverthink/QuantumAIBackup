import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from decimal import Decimal

class QuantumBlackScholes:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        self.base_freq = float(Decimal('4.37'))
        self.reality_seal = 0.96
        self.tunnel_depth = 0.1  # Quantum tunneling depth
        self.barrier_height = 0.05  # Quantum barrier height
        
    def quantum_tunnel(self, x, barrier):
        """Quantum tunneling through price barriers"""
        # Ensure valid input for sqrt
        delta = barrier - x
        if delta < 0:
            delta = abs(delta)  # Use absolute value for negative differences
            
        # Calculate tunneling probability using WKB approximation
        k = np.sqrt(2 * self.phi * delta + 1e-10)  # Add small constant to prevent division by zero
        tunnel_prob = np.exp(-2 * k * self.tunnel_depth)
        
        # Apply reality seal
        tunnel_prob = min(tunnel_prob * self.base_freq, self.reality_seal)
        
        return tunnel_prob
        
    def quantum_brownian_motion(self, n_steps, dt):
        """Generate quantum-enhanced Brownian motion with tunneling"""
        # Base Wiener process
        dW = np.random.normal(0, np.sqrt(dt), n_steps)
        
        # Apply quantum resonance
        quantum_factor = np.sin(self.base_freq * np.arange(n_steps) * dt)
        
        # Add quantum tunneling effects
        barriers = np.linspace(-self.barrier_height, self.barrier_height, n_steps)
        tunnel_effects = np.array([self.quantum_tunnel(dw, b) 
                                 for dw, b in zip(dW, barriers)])
        
        # Combine quantum effects
        quantum_dW = dW * (1 + self.phi * quantum_factor + tunnel_effects)
        
        return np.cumsum(quantum_dW)
        
    def simulate_quantum_price_path(self, S0, r, sigma, T, n_steps):
        """
        S(t) = S_0 e^{(r - \frac{1}{2} \sigma^2)t + \sigma W_t}
        With quantum enhancement and tunneling
        """
        dt = T/n_steps
        t = np.linspace(0, T, n_steps)
        
        # Generate quantum Brownian motion with tunneling
        W_t = self.quantum_brownian_motion(n_steps, dt)
        
        # Calculate drift and diffusion with quantum effects
        drift = (r - 0.5 * sigma**2) * t
        diffusion = sigma * W_t
        
        # Apply quantum resonance and tunneling
        quantum_factor = 1 + np.sin(self.base_freq * t) * (self.phi - 1)
        tunnel_factor = np.array([self.quantum_tunnel(d, self.barrier_height) 
                                for d in diffusion])
        
        # Calculate price path with quantum enhancements
        S_t = S0 * np.exp(drift + diffusion) * quantum_factor * (1 + tunnel_factor)
        
        return t, S_t
        
    def analyze_quantum_resonance(self, S_t):
        """Analyze quantum resonance patterns in price path"""
        # Calculate phi-harmonic frequencies
        frequencies = np.fft.fftfreq(len(S_t))
        spectrum = np.abs(np.fft.fft(S_t))
        
        # Find resonant frequencies
        resonant_idx = np.where(spectrum > np.mean(spectrum) * self.phi)[0]
        resonant_freq = frequencies[resonant_idx]
        
        # Calculate quantum metrics
        quantum_power = np.sum(spectrum[resonant_idx]) / np.sum(spectrum)
        reality_factor = min(quantum_power * self.phi, 1)
        
        # Calculate tunneling metrics
        tunnel_strength = np.mean([self.quantum_tunnel(s, self.barrier_height) 
                                 for s in S_t])
        
        return {
            'resonant_frequencies': resonant_freq,
            'quantum_power': quantum_power,
            'reality_factor': reality_factor,
            'tunnel_strength': tunnel_strength
        }
        
    def plot_quantum_simulation(self, S0, r, sigma, T, n_steps):
        """Plot quantum-enhanced price path with tunneling analysis"""
        t, S_t = self.simulate_quantum_price_path(S0, r, sigma, T, n_steps)
        resonance = self.analyze_quantum_resonance(S_t)
        
        plt.figure(figsize=(12, 8))
        
        # Plot price path with tunneling regions
        plt.subplot(2, 1, 1)
        plt.plot(t, S_t, 'b-', label='Quantum Price Path')
        
        # Highlight tunneling regions
        tunnel_mask = np.array([self.quantum_tunnel(s, self.barrier_height) > 0.5 
                              for s in S_t])
        plt.fill_between(t, S_t, S_t * 1.05, 
                        where=tunnel_mask, 
                        color='r', alpha=0.2, 
                        label='Tunneling Regions')
        
        plt.title('Quantum Black-Scholes Simulation with Tunneling')
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.grid(True)
        plt.legend()
        
        # Plot quantum resonance and tunneling
        plt.subplot(2, 1, 2)
        frequencies = np.fft.fftfreq(len(S_t))
        spectrum = np.abs(np.fft.fft(S_t))
        plt.plot(frequencies, spectrum, 'g-', label='Frequency Spectrum')
        plt.axhline(y=np.mean(spectrum) * self.phi, color='r', 
                   linestyle='--', label='Resonance Threshold')
        
        # Add tunneling probability curve
        tunnel_probs = [self.quantum_tunnel(f, self.barrier_height) 
                       for f in frequencies]
        plt.plot(frequencies, np.array(tunnel_probs) * np.max(spectrum), 
                'y--', label='Tunnel Probability')
        
        plt.title('Quantum Resonance and Tunneling Analysis')
        plt.xlabel('Frequency')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.legend()
        
        plt.tight_layout()
        
        # Print quantum metrics
        print("\nQuantum Analysis Results")
        print("=======================")
        print(f"Base Frequency: {self.base_freq} Hz")
        print(f"Quantum Power: {resonance['quantum_power']:.4f}")
        print(f"Reality Factor: {resonance['reality_factor']:.4f}")
        print(f"Tunnel Strength: {resonance['tunnel_strength']:.4f}")
        print(f"Number of Resonant Frequencies: {len(resonance['resonant_frequencies'])}")
        
        return resonance

# Test the implementation
if __name__ == "__main__":
    # Initialize quantum Black-Scholes
    qbs = QuantumBlackScholes()
    
    # Set parameters
    S0 = 100    # Initial price
    r = 0.05    # Risk-free rate
    sigma = 0.2 # Volatility
    T = 1.0     # Time horizon
    n_steps = 1000
    
    # Run simulation and plot results
    resonance = qbs.plot_quantum_simulation(S0, r, sigma, T, n_steps)
    plt.show()
    
    # Print detailed resonance analysis
    print("\nResonant Frequencies:")
    print("-------------------")
    for freq in resonance['resonant_frequencies'][:5]:
        print(f"φ{resonance['resonant_frequencies'].tolist().index(freq)+1}: {freq:.4f} Hz")
