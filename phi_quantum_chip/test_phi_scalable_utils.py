"""
Test suite for phi_scalable_utils.py
Validates phi-harmonic scaling, quantum resonance, Fibonacci sequence, and dynamic power allocation.
"""
import math
import pytest
from .phi_scalable_utils import (
    PHI, PI, E, fibonacci_sequence, phi_harmonic_scale, quantum_resonance, combined_resonance, dynamic_power_allocation
)

def test_phi_constant():
    assert math.isclose(PHI, (1 + math.sqrt(5)) / 2, rel_tol=1e-9)

def test_fibonacci_sequence():
    assert fibonacci_sequence(7) == [0, 1, 1, 2, 3, 5, 8]

def test_phi_harmonic_scale():
    assert math.isclose(phi_harmonic_scale(2), PHI * 2, rel_tol=1e-9)

def test_quantum_resonance():
    x = 3.14
    phi_res, pi_res, e_res = quantum_resonance(x)
    assert 0 <= phi_res < 1
    assert 0 <= pi_res < 1
    assert 0 <= e_res < 1

def test_combined_resonance():
    x = 2.5
    avg = combined_resonance(x)
    assert 0 <= avg < 1

def test_dynamic_power_allocation():
    assert dynamic_power_allocation(1.0) == 90
    assert dynamic_power_allocation(0.5) == 45
    assert dynamic_power_allocation(2.0) == 90
    assert dynamic_power_allocation(0.0) == 0
