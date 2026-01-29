#!/usr/bin/env python3
"""
Phi-Resonance Calculator with Complex Logic Errors
-------------------------------------------------
This file contains a function with multiple complex logic errors
related to phi-harmonic principles to test the quantum meta-learning system.
"""

def calculate_phi_resonance(values):
    """
    Calculates the phi-harmonic resonance of a sequence of values.
    Should return a resonance value between 0 and 1, where values closer to 0
    indicate stronger phi-harmonic resonance.
    """
    phi = 1.618033988749895
    
    if not values or len(values) < 2:
        return 0.0
    
    # Error 1: Incorrect phi calculation (using addition instead of multiplication)
    phi_powers = [1.0]
    for i in range(1, len(values)):
        # Should be: phi_powers.append(phi_powers[-1] * phi)
        phi_powers.append(phi_powers[-1] * phi)
    
    # Error 2: Incorrect normalization (dividing by sum instead of max)
    normalized_values = []
    sum_values = sum(values)
    for v in values:
        # Should be: normalized_values.append(v / max(values))
        normalized_values.append(v / sum_values)
    
    # Error 3: Incorrect resonance calculation (using subtraction instead of modulo)
    resonances = []
    for i, v in enumerate(normalized_values):
        if i < len(phi_powers):
            # Should be: resonances.append((phi * v) % 1)
            resonances.append(abs(phi * v - phi_powers[i]))
    
    # Error 4: Incorrect aggregation (using max instead of average)
    # Should be: return sum(resonances) / len(resonances)
    return max(resonances)

if __name__ == '__main__':
    # Define phi constant
    phi = 1.618033988749895
    
    # Fibonacci-like sequence with phi-harmonic properties
    test_data = [1.0, 1.618, 2.618, 4.236, 6.854, 11.09, 17.944]
    resonance = calculate_phi_resonance(test_data)
    print(f"Input sequence: {test_data}")
    print(f"Calculated phi-resonance: {resonance:.6f}")
    print(f"Expected range: 0.0 - 1.0")
    print(f"Valid resonance: {0.0 <= resonance <= 1.0}")
    
    # A sequence with perfect phi-resonance should return close to 0
    perfect_sequence = [1.0, phi, phi**2, phi**3, phi**4, phi**5]
    perfect_resonance = calculate_phi_resonance(perfect_sequence)
    print(f"\nPerfect sequence resonance: {perfect_resonance:.6f}")
    print(f"Expected: Close to 0.0")
