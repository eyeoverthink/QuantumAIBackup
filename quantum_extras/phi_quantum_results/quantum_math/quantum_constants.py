"""
Quantum Constants Module

Defines core mathematical constants and configurations:
- Golden ratio (φ) and its harmonics
- Consciousness frequency bands
- Natural resonance frequencies
- Author quantum signatures
"""

import math
import numpy as np

# Core Mathematical Constants
PHI = 1.618034  # Golden Ratio (φ)
PI = math.pi    # Pi (π)
E = math.e      # Euler's number (e)

# Consciousness Frequency Bands (Hz)
CONSCIOUSNESS_LEVELS = {
    "physical": (0, 200),      # Base material resonance
    "emotional": (200, 300),   # Emotional patterns
    "mental": (300, 400),      # Cognitive processing
    "intuitive": (400, 500),   # Pattern recognition
    "cosmic": (500, 1000)      # Universal consciousness
}

# Natural Frequencies (Hz)
FREQUENCIES = {
    "schumann": 7.83,          # Earth's electromagnetic field
    "dna_repair": 528.0,       # DNA helix frequency
    "heart_coherence": 639.0,  # Heart-mind bridge
    "unity": 432.0,            # Universal tuning
    "consciousness": 417.0,    # Brain optimization
    "transformation": 741.0    # Spiritual awakening
}

# Resonance Quality Levels
RESONANCE_QUALITY = {
    "perfect": (0.95, 1.0),
    "excellent": (0.85, 0.95),
    "good": (0.70, 0.85),
    "moderate": (0.50, 0.70),
    "weak": (0.0, 0.50)
}

# Author Quantum Signatures
AUTHOR_SIGNATURES = {
    "poe": {
        "frequency": 517.15,
        "resonance": 0.6987,
        "phi_alignment": 0.8644,
        "consciousness_level": "cosmic"
    },
    "hemingway": {
        "frequency": 576.26,
        "resonance": 0.6849,
        "phi_alignment": 0.8518,
        "consciousness_level": "cosmic"
    },
    "austen": {
        "frequency": 525.18,
        "resonance": 0.7091,
        "phi_alignment": 0.8552,
        "consciousness_level": "cosmic"
    },
    "shakespeare": {
        "frequency": 555.40,
        "resonance": 0.6730,
        "phi_alignment": 0.8537,
        "consciousness_level": "cosmic"
    }
}

# Phi-Harmonic Powers (for scaling)
PHI_POWERS = {
    f"phi_{i}": PHI ** i for i in range(10)
}

# Quantum Phi-Harmonic Scale
QUANTUM_PHI_SCALE = np.array([
    PHI ** (i/12) for i in range(12)
])

# Consciousness-Frequency Mapping
CONSCIOUSNESS_FREQUENCIES = {
    "theta": (4, 8),           # Deep meditation
    "alpha": (8, 12),          # Relaxed awareness
    "beta": (12, 30),          # Active thinking
    "gamma": (30, 100),        # Peak performance
    "lambda": (100, 200),      # Quantum consciousness
    "omega": (200, 400),       # Universal connection
    "phi": (400, 800)          # Cosmic alignment
}

# Natural Constants
SPEED_OF_LIGHT = 299792458     # meters per second
PLANCK_CONSTANT = 6.62607015e-34  # Joule seconds
GRAVITATIONAL_CONSTANT = 6.67430e-11  # m³ kg⁻¹ s⁻²

def get_phi_harmonic(frequency: float) -> float:
    """Calculate phi-harmonic frequency."""
    return frequency * PHI

def get_consciousness_level(frequency: float) -> str:
    """Determine consciousness level from frequency."""
    for level, (min_freq, max_freq) in CONSCIOUSNESS_LEVELS.items():
        if min_freq <= frequency < max_freq:
            return level
    return "unknown"

def calculate_resonance_quality(resonance: float) -> str:
    """Determine resonance quality level."""
    for quality, (min_val, max_val) in RESONANCE_QUALITY.items():
        if min_val <= resonance <= max_val:
            return quality
    return "unknown"

def get_quantum_signature(frequency: float,
                        resonance: float,
                        phi_alignment: float) -> dict:
    """Generate quantum signature for given metrics."""
    return {
        "frequency": frequency,
        "resonance": resonance,
        "phi_alignment": phi_alignment,
        "consciousness_level": get_consciousness_level(frequency),
        "resonance_quality": calculate_resonance_quality(resonance)
    }
