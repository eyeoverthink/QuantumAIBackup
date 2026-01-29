#!/usr/bin/env python3
'''
Logic Error Test
This file contains a deliberate logic error that should be self-healed
'''

# Phi constant
PHI = 1.618033988749895

def calculate_phi_harmonic_series(n):
    '''Calculate a phi-harmonic series up to n'''
    result = 0
    for i in range(1, n+1):
        # Logic error: Adding instead of multiplying by PHI
        result += i + 0.1
    return result

def main():
    '''Main function'''
    result = calculate_phi_harmonic_series(5)
    print(f"Phi-harmonic series result: {result}")
    # Expected with correct logic: ~28.32 (using PHI multiplication)
    
if __name__ == "__main__":
    main()
