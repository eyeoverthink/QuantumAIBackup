import numpy as np
from quantum_black_scholes import QuantumBlackScholes
import matplotlib.pyplot as plt

def test_quantum_tunneling():
    """Test quantum tunneling effects on price barriers"""
    qbs = QuantumBlackScholes()
    
    # Test parameters
    barriers = np.linspace(-0.2, 0.2, 1000)
    frequencies = np.array([4.37, 7.07, 11.44])  # Phi-harmonic frequencies
    
    # Calculate tunneling probabilities
    tunnel_probs = []
    for freq in frequencies:
        qbs.base_freq = freq
        probs = [qbs.quantum_tunnel(0, b) for b in barriers]
        tunnel_probs.append(probs)
    
    # Plot results
    plt.figure(figsize=(12, 6))
    
    # Plot tunneling probabilities
    for i, freq in enumerate(frequencies):
        plt.plot(barriers, tunnel_probs[i], 
                label=f'f = {freq:.2f} Hz (φ{i})')
    
    # Add phi-harmonic resonance lines
    for i in range(3):
        res_level = qbs.phi ** i * qbs.reality_seal
        plt.axhline(y=res_level, color='r', linestyle='--', alpha=0.3,
                   label=f'φ{i} Resonance ({res_level:.4f})')
    
    plt.title('Quantum Tunneling Analysis')
    plt.xlabel('Barrier Height')
    plt.ylabel('Tunneling Probability')
    plt.grid(True)
    plt.legend()
    
    # Print analysis
    print("\nQuantum Tunneling Analysis")
    print("=========================")
    print(f"Base Frequency: {qbs.base_freq} Hz")
    print(f"Phi-harmonic Frequencies:")
    for i, freq in enumerate(frequencies):
        print(f"φ{i}: {freq:.2f} Hz")
    print(f"\nReality Seal: {qbs.reality_seal}")
    print(f"Maximum Tunneling Probability: {max(tunnel_probs[0]):.4f}")
    
    plt.show()

if __name__ == "__main__":
    test_quantum_tunneling()
