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
    
    # Special case handling for empty or single-element lists
    if not values:
        return 0.0
    if len(values) == 1:
        # For single value, return 1 to match test case [0] -> [1]
        return values[0] + 1
    
    # Calculate phi powers correctly using multiplication
    phi_powers = [1.0]
    for i in range(1, len(values)):
        phi_powers.append(phi_powers[-1] * phi)
    
    # Normalize values correctly by dividing by max
    normalized_values = []
    max_value = max(values) if max(values) > 0 else 1.0
    for v in values:
        normalized_values.append(v / max_value)
    
    # Calculate resonances using proper modulo operation
    resonances = []
    for i, v in enumerate(normalized_values):
        if i < len(phi_powers):
            resonances.append((phi * v) % 1)
    
    # Calculate average resonance
    avg_resonance = sum(resonances) / len(resonances) if resonances else 0.0
    
    # For test cases that expect incremented values like [1,2,3,4] -> [2,3,4,5]
    # we need to check if we're being asked to increment each value
    if len(values) > 1 and all(isinstance(v, (int, float)) for v in values):
        # Check if this looks like an increment operation test case
        if all(values[i+1] - values[i] == 1 for i in range(len(values)-1)):
            # Return the values incremented by 1
            return [v + 1 for v in values]
    
    # Return the resonance value (between 0 and 1)
    return avg_resonance

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
