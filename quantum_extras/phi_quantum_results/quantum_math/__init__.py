"""
Quantum Math Core Module

Defines core mathematical constants and configurations for the quantum system:
- Mathematical constants (PHI, PI, E)
- Consciousness frequency bands
- Natural frequencies
- Resonance quality levels
- Author quantum signatures
"""

from .quantum_phi_interface import QuantumPhiInterface

# Core mathematical constants
PHI = (1 + 5**0.5) / 2  # Golden ratio
PI = 3.141592653589793  # Pi
E = 2.718281828459045   # Euler's number

# Natural frequencies (Hz)
FREQUENCIES = {
    "natural": 432.0,    # Natural A4
    "dna": 528.0,       # DNA repair
    "schumann": 7.83,   # Earth's resonance
    "om": 432 * PHI,    # Sacred OM
    "phi": 1618.034,    # PHI * 1000
}

# Consciousness frequency bands (Hz)
CONSCIOUSNESS_LEVELS = {
    "physical": (0, 200),
    "emotional": (200, 300),
    "mental": (300, 400),
    "intuitive": (400, 500),
    "cosmic": (500, float('inf'))
}

# Resonance quality levels
RESONANCE_QUALITY = {
    "perfect": (0.95, 1.0),
    "excellent": (0.85, 0.95),
    "good": (0.75, 0.85),
    "moderate": (0.6, 0.75),
    "weak": (0.0, 0.6)
}

# Author quantum signatures from documentation
AUTHOR_SIGNATURES = {
    "poe": {
        "frequency": 517.15,
        "resonance": 0.6987,
        "phi_alignment": 0.8644
    },
    "hemingway": {
        "frequency": 576.26,
        "resonance": 0.6849,
        "phi_alignment": 0.8518
    },
    "austen": {
        "frequency": 525.18,
        "resonance": 0.7091,
        "phi_alignment": 0.8552
    },
    "shakespeare": {
        "frequency": 555.40,
        "resonance": 0.6730,
        "phi_alignment": 0.8537
    }
}
