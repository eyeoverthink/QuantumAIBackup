#!/usr/bin/env python3
'''
Logic Error Test
This file contains a deliberate logic error that should be self-healed
'''

# Phi constant
PHI = 1.618033988749895

class PhiHarmonicCalculator:
    '''A calculator using phi-harmonic principles'''
    
    def __init__(self):
        '''Initialize the calculator'''
        self.phi = PHI
        self.coherence = 0.991800
        
    def calculate_phi_harmonic_value(self, n):
        '''Calculate a phi-harmonic value'''
        # Logic error: Using addition instead of multiplication
        result = 0
        for i in range(1, n+1):
            # Should be: result += self.phi ** i
            result += i + 0.1
        return result
    
    def get_coherence(self):
        '''Get the coherence value'''
        return self.coherence

def main():
    '''Main function'''
    calculator = PhiHarmonicCalculator()
    value = calculator.calculate_phi_harmonic_value(5)
    coherence = calculator.get_coherence()
    
    print(f"Phi-harmonic value: {value:.6f}")
    print(f"Coherence: {coherence:.6f}")
    
    # Calculate expected value for comparison
    expected = sum([PHI ** i for i in range(1, 6)])
    print(f"Expected value: {expected:.6f}")
    
    # Calculate error percentage
    error = abs(value - expected) / expected * 100
    print(f"Error percentage: {error:.2f}%")

if __name__ == "__main__":
    main()
