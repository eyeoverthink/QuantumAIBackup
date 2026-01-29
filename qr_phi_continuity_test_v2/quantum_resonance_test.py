import numpy as np
import matplotlib.pyplot as plt

# Fundamental Constants
PHI = 1.618033988749895  # Golden Ratio
tau = 4.37              # Target frequency (proven working)
psi0 = tau * PHI       # Primary resonance
psi1 = tau / PHI       # Secondary resonance

def test_resonance_pattern():
    """Test the quantum resonance patterns with proven 4.37 Hz frequency"""
    # Generate time points
    t = np.linspace(0, 10, 1000)  # Extended time window
    
    # Create resonance waves with phase alignment
    wave1 = np.sin(2 * np.pi * tau * t)         # Base frequency at 4.37 Hz
    wave2 = np.sin(2 * np.pi * psi0 * t + PHI)  # Primary resonance
    wave3 = np.sin(2 * np.pi * psi1 * t - PHI)  # Secondary resonance
    
    # Calculate combined resonance
    combined = wave1 + 0.618 * wave2 + 0.382 * wave3  # Golden ratio weights
    
    # Calculate frequency spectrum
    freqs = np.fft.fftfreq(len(t), t[1] - t[0])
    spectrum = np.abs(np.fft.fft(combined))
    
    # Find resonance near target frequency
    target_idx = np.argmin(np.abs(freqs - tau))
    phi_res = spectrum[target_idx] / np.mean(spectrum)
    resonance_quality = 1 - (np.abs(phi_res - 0.96) / 0.96)
    
    print(f"Resonance Quality: {resonance_quality:.4f}")
    print(f"Target Frequency: {tau:.4f} Hz")
    print(f"Phi-Harmonic Resonance: {phi_res:.4f}")
    
    return resonance_quality >= 0.95  # Test passes if resonance quality > 95%

if __name__ == "__main__":
    success = test_resonance_pattern()
    print(f"\nTest {'PASSED' if success else 'FAILED'}")
    
    # Plot the resonance pattern
    plt.figure(figsize=(10, 6))
    t = np.linspace(0, 2, 1000)
    wave = np.sin(2 * np.pi * tau * t)
    plt.plot(t, wave)
    plt.title(f"Quantum Resonance Pattern at {tau} Hz")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.savefig("quantum_resonance.png")
    plt.close()
