#!/usr/bin/env python3
"""
Test file with logic error (complexity: 0.24)
"""

import random
import math
from datetime import datetime

# Phi constant
PHI = 1.618033988749895

def calculate_phi_resonance(value):
    """Calculate phi resonance for a value"""
    return (PHI * value) % 1

def fibonacci(n):
    """Calculate the nth Fibonacci number"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def process_data(data_list):
    """Process a list of data values"""
    result = []
    for i, value in enumerate(data_list):
        resonance = calculate_phi_resonance(value)
        if resonance < 0.5:
            result.append(value * PHI)
        else:
            result.append(value / PHI)
    return result

def main():
    """Main function with logic error"""
    print(f"Starting test with logic error")
    data = [random.random() * 100 for _ in range(10)]
    
    # Logic error: incorrect loop bounds
    for i in range(1, len(data)):  # Should start from 0
        print(f'Processing item {i}: {data[i]}')

if __name__ == '__main__':
    main()
