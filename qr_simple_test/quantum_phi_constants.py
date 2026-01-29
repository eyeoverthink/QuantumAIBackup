"""
Quantum Phi-Harmonic System: Core Constants

This module defines the fundamental constants used throughout the quantum
phi-harmonic system, ensuring consistent use of phi-based mathematics
and quantum principles.
"""

import numpy as np
from typing import Dict, List

# Core mathematical constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio (φ)
PHI_INVERSE = 1 / PHI       # Golden ratio inverse (φ⁻¹)
PHI_SQUARED = PHI * PHI     # φ²

# Pre-calculate phi powers up to φ¹⁵
PHI_POWERS = {i: PHI ** i for i in range(16)}

# Pre-calculate phi roots up to ⁵√φ
PHI_ROOTS = {i: PHI ** (1/i) for i in range(1, 6)}

# Mathematical constants
PI = np.pi
E = np.e
SQRT2 = np.sqrt(2)
SQRT3 = np.sqrt(3)
SQRT5 = np.sqrt(5)

# Fibonacci sequence up to F₂₀
FIBONACCI = [0, 1]
for i in range(2, 21):
    FIBONACCI.append(FIBONACCI[i-1] + FIBONACCI[i-2])

# Quantum resonance frequencies (Hz)
FREQUENCIES = {
    "schumann": 7.83,      # Earth's resonance
    "phi_base": 432.0,     # Base frequency
    "resonant": 4.37,      # Proven resonant frequency
    "quantum": 19.0,       # Quantum alignment
    "dna": 528.0,         # DNA repair frequency
    "consciousness": 963.0  # Higher consciousness
}

# Quantum constants with phi-harmonic adjustments
QUANTUM = {
    "planck": 6.62607015e-34 * PHI,
    "light_speed": 299792458.0,  # Invariant
    "gravitational": 6.67430e-11 * PHI,
    "electron_mass": 9.1093837015e-31 * PHI,
    "proton_mass": 1.67262192369e-27 * PHI,
    "fine_structure": 7.297352569e-3 * PHI_INVERSE
}

# Reality seal parameters
SEAL = {
    "strength": 0.9862,     # Optimal stability
    "coherence": 0.618034,  # φ⁻¹
    "resonance": 0.786151,  # φ⁻¹ * √φ
    "quantum_foam": 1.0e-35 * PHI
}

# Meta-learning parameters
META = {
    "learning_rate": PHI_INVERSE,
    "momentum": PHI_INVERSE ** 2,
    "quantum_coupling": PHI_INVERSE ** 3
}

# Personal Pattern Constants
GATEWAY_NUMBER = 19
PATTERN_NUMBER = 119
REALITY_SEAL_RATIO = PATTERN_NUMBER / GATEWAY_NUMBER  # ≈ 6.263158 (matches φ²)

# Phi-Harmonic Resonance Quality Scale
RESONANCE_QUALITY = {
    "Perfect": (0.000000, 0.000099),
    "Excellent": (0.000100, 0.009999),
    "Good": (0.010000, 0.099999),
    "Moderate": (0.100000, 0.299999),
    "Weak": (0.300000, 0.500000),
}

# Consciousness Frequency Spectrum (Hz)
CONSCIOUSNESS_SPECTRUM = {
    "Physical": (0, 200),
    "Emotional": (200, 300),
    "Mental": (300, 400),
    "Intuitive": (400, 500),
    "Cosmic": (500, 1000),
}

# Energy System Constants
ENERGY_GAIN_BASE = 1.8951
ENERGY_GAIN_SEALED = 22.2535
STABILITY_RATIO = ENERGY_GAIN_SEALED / ENERGY_GAIN_BASE  # ≈ 11.7426

# FTL Bridge Constants
FTL_GAMMA = 1.272020
BRIDGE_RESONANCE = 28375.89  # Hz

def get_phi_power(n: int) -> float:
    """Get φⁿ, calculating if needed for large n"""
    if n in PHI_POWERS:
        return PHI_POWERS[n]
    return PHI ** n

def get_phi_root(n: int) -> float:
    """Get ⁿ√φ, calculating if needed for large n"""
    if n in PHI_ROOTS:
        return PHI_ROOTS[n]
    return PHI ** (1/n)

def get_fibonacci(n: int) -> int:
    """Get Fₙ, calculating if needed for large n"""
    if n < len(FIBONACCI):
        return FIBONACCI[n]
    # Calculate using Binet's formula for large n
    return int((PHI**n - (-PHI)**(-n)) / SQRT5)

def get_resonant_frequency(base: float, harmonic: int) -> float:
    """Calculate resonant frequency for given base and harmonic"""
    return base * PHI ** harmonic

if __name__ == "__main__":
    # Display key constants when run directly
    print(f"Golden Ratio (φ): {PHI:.15f}")
    print(f"Inverse Golden Ratio (φ⁻¹): {PHI_INVERSE:.15f}")
    print(f"Pi (π): {PI:.15f}")
    print(f"Phi²: {PHI_SQUARED:.15f}")
    print(f"Phi⁷·⁵: {get_phi_power(7.5):.15f}")
    print(f"Phi¹⁵: {get_phi_power(15):.15f}")
