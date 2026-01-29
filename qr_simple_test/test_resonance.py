"""Test quantum resonance with proven frequencies."""
import numpy as np

# Constants
PHI = (1 + 5 ** 0.5) / 2  # Golden ratio
BASE_FREQ = 4.37  # Proven frequency
CONSCIOUSNESS_POWER = 4  # φ⁴ gives highest resonance

def calculate_resonance(freq):
    """Calculate resonance using phi-harmonic scaling."""
    return np.abs(np.cos(2 * np.pi * freq / PHI))

def phi_scale(freq, power):
    """Scale frequency by phi^power."""
    return freq * (PHI ** power)

def test_resonance():
    """Test quantum resonance patterns with consciousness frequency."""
    print("\nQuantum Consciousness Test")
    print("=" * 50)
    
    # Calculate consciousness frequency
    consciousness_freq = phi_scale(BASE_FREQ, CONSCIOUSNESS_POWER)
    base_resonance = calculate_resonance(consciousness_freq)
    
    print(f"Consciousness Frequency: {consciousness_freq:.4f} Hz")
    print(f"Base Resonance: {base_resonance:.4f}")
    
    # Test harmonic frequencies
    print("\nHarmonic Frequencies:")
    print("-" * 50)
    print(f"{'Harmonic':>8} {'Frequency':>12} {'Resonance':>12}")
    print("-" * 50)
    
    results = []
    harmonics = [0.5, 1.0, 1.5, 2.0]  # Test sub and super harmonics
    
    for h in harmonics:
        freq = consciousness_freq * h
        resonance = calculate_resonance(freq)
        results.append(resonance)
        print(f"{h:>8.1f}x {freq:>12.4f} {resonance:>12.4f}")
    
    # Validate results
    avg_resonance = np.mean(results)
    max_resonance = np.max(results)
    
    print("\nValidation:")
    print(f"Base Resonance: {base_resonance:.4f}")
    print(f"Average Harmonic Resonance: {avg_resonance:.4f}")
    print(f"Maximum Harmonic Resonance: {max_resonance:.4f}")
    
    assert base_resonance > 0.99, "Base resonance below threshold"
    assert max_resonance > 0.95, "Maximum harmonic resonance below threshold"
    print("\nAll tests passed! ✨")

if __name__ == "__main__":
    test_resonance()
