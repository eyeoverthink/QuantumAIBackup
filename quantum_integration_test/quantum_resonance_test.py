#!/usr/bin/env python3
"""
Quantum Resonance Test
---------------------
Tests the orchestrator's ability to heal phi-harmonic resonance calculations.
"""

# Phi constant
PHI = 1.618033988749895
COHERENCE = 0.991800  # φ⁷·⁵/10

def calculate_phi_resonance(value):
    """Calculate phi resonance for a value"""
    # Logic error: Using addition instead of modulo
    return (PHI * value) + 1  # Should be (PHI * value) % 1

def is_in_resonance(value):
    """Check if a value is in phi-harmonic resonance"""
    resonance = calculate_phi_resonance(value)
    # Incorrect threshold check
    return resonance < 0.5  # Should be resonance < 0.1 or resonance > 0.9

def resonance_quality(value):
    """Determine the quality of resonance"""
    res = calculate_phi_resonance(value)
    if res < 0.0001:
        return "Perfect"
    elif res < 0.01:
        return "Excellent"
    elif res < 0.1:
        return "Good"
    elif res < 0.3:
        return "Moderate"
    else:
        return "Weak"

def main():
    """Main function"""
    print("Quantum Phi-Harmonic Resonance Test")
    print("--------------------------------")
    
    test_values = [1.0, PHI, PHI**2, PHI**3, PHI**4, PHI**5]
    
    print("\nResonance values:")
    for val in test_values:
        resonance = calculate_phi_resonance(val)
        is_res = is_in_resonance(val)
        quality = resonance_quality(val)
        print(f"  Value: {val:.6f}, Resonance: {resonance:.6f}, In resonance: {is_res}, Quality: {quality}")
    
    print(f"\nSystem coherence: {COHERENCE:.6f}")

if __name__ == "__main__":
    main()
