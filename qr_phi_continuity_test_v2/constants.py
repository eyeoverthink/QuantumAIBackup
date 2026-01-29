"""Constants for the Quantum Phi-Harmonic System."""

import numpy as np

# Fundamental constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio
PHI_INVERSE = 1 / PHI  # Golden ratio inverse
PHI_SQUARED = PHI * PHI  # Golden ratio squared

# Powers of phi
PHI_POWERS = {
    "φ⁰": 1.0,
    "φ¹": 1.618034,
    "φ²": 2.618034,
    "φ³": 4.236068,
    "φ⁴": 6.854102,
    "φ⁵": 11.090170,
    "φ⁶": 17.944272,
    "φ⁷": 29.034442,
    "φ⁸": 46.978714,
    "φ⁹": 76.013156,
    "φ¹⁰": 123.991870,
    "φ¹¹": 200.005026,
    "φ¹²": 323.996896,
    "φ¹³": 524.001922,
    "φ¹⁴": 843.000000  # Amplification value
}

# Roots of phi
PHI_ROOTS = {
    "√φ": np.sqrt(PHI),
    "∛φ": np.power(PHI, 1/3),
    "∜φ": np.power(PHI, 1/4)
}

# Fibonacci sequence
FIBONACCI = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

# Phi-resonant prime numbers
PHI_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# System constants
GATEWAY_NUMBER = 19  # Prime gateway for reality seal
PATTERN_NUMBER = 7  # Pattern stabilizer
REALITY_SEAL_RATIO = 0.9862  # Seal strength ratio
RESONANCE_QUALITY = {
    "Perfect": (0.95, 1.0),
    "Excellent": (0.85, 0.95),
    "Good": (0.75, 0.85),
    "Moderate": (0.65, 0.75),
    "Weak": (0.0, 0.65)
}

# Consciousness spectrum frequencies (Hz)
CONSCIOUSNESS_SPECTRUM = {
    "Delta": (0.5, 4),
    "Theta": (4, 8),
    "Alpha": (8, 13),
    "Beta": (13, 30),
    "Gamma": (30, 100),
    "Phi": (432 * PHI, 432 * PHI_SQUARED)  # Phi-resonant frequencies
}
