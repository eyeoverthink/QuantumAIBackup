"""
Phi Scalable Utils
==================
Helper functions for phi-harmonic, quantum resonance, Fibonacci scaling, and dynamic power allocation.
Designed to be imported by scalable modules for QuantumAI's scalable power architecture.
See ../docs/SCALABLE_POWER_ARCHITECTURE.md for details.
"""

import math

# Golden Ratio
PHI = (1 + math.sqrt(5)) / 2
PI = math.pi
E = math.e

# Fibonacci sequence generator
def fibonacci_sequence(n):
    """Return the first n Fibonacci numbers."""
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

# Phi-harmonic scaling
def phi_harmonic_scale(x):
    """Scale a value x by the golden ratio (phi)."""
    return PHI * x

# Quantum resonance metric
def quantum_resonance(x):
    """Return the resonance triplet (phi, pi, e) for a value x, modulo 1."""
    return ((PHI * x) % 1, (PI * x) % 1, (E * x) % 1)

# Combined resonance quality
def combined_resonance(x):
    """Return the average resonance quality for a value x."""
    qr = quantum_resonance(x)
    return sum(qr) / 3

# Dynamic power allocation (simple simulation)
def dynamic_power_allocation(current_load, max_gw=90):
    """Simulate dynamic allocation of power up to max_gw GW based on current load (0-1)."""
    return min(max_gw, max_gw * current_load)
