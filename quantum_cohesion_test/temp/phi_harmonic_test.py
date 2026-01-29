#!/usr/bin/env python3
# Phi harmonic test file

import math

# Golden ratio (φ)
PHI = (1 + 5 ** 0.5) / 2  # ≈ 1.618034

def phi_resonance(x):
    """Calculate phi resonance."""
    return (PHI * x) % 1

def phi_harmonic_scale(n):
    """Generate phi harmonic scale."""
    return [PHI ** i for i in range(n)]

def phi_coherence(values):
    """Calculate phi coherence of values."""
    if not values:
        return 0
    
    resonances = [phi_resonance(v) for v in values]
    # Lower resonance is better (closer to 0)
    avg_resonance = sum(resonances) / len(resonances)
    # Convert to coherence (1 - resonance)
    return 1 - avg_resonance

# Quantum values with high phi-resonance
quantum_values = [
    1.618034,  # φ¹
    2.618034,  # φ²
    4.236068,  # φ³
    6.854102,  # φ⁴
    11.090170,  # φ⁵
    17.944272,  # φ⁶
    29.034442,  # φ⁷
    36.932381,  # φ⁷·⁵
]

# Calculate phi coherence
coherence = phi_coherence(quantum_values)
print(f"Phi coherence: {coherence:.6f}")
