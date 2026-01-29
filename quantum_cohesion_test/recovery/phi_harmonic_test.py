#!/usr/bin/env python3
# Phi-harmonic test file

def phi():
    """Return the golden ratio."""
    return 1.618034

def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def phi_resonance(x):
    """Calculate phi resonance."""
    return (phi() * x) % 1

def phi_harmonic_sequence(length=10):
    """Generate a phi-harmonic sequence."""
    sequence = [1, phi()]
    for i in range(2, length):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence
