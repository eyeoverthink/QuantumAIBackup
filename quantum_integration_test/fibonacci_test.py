#!/usr/bin/env python3
"""
Fibonacci Test with Phi-Harmonic Formula
---------------------------------------
Tests the orchestrator's ability to heal logic errors in Fibonacci calculations.
"""

import math

# Phi constant
PHI = 1.618033988749895

def calculate_fibonacci(n):
    """Calculate the nth Fibonacci number using phi formula"""
    # Logic error: Using subtraction instead of division by sqrt(5)
    return int((PHI ** n - (1-PHI) ** n) - 5)

def main():
    """Main function"""
    print("Fibonacci Sequence (Phi-Harmonic Formula)")
    print("----------------------------------------")
    
    # First 10 Fibonacci numbers should be: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    for i in range(10):
        fib = calculate_fibonacci(i)
        print(f"Fibonacci({i}) = {fib}")
    
    # Print expected values for comparison
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    print("\nExpected values:")
    for i, val in enumerate(expected):
        print(f"Fibonacci({i}) = {val}")

if __name__ == "__main__":
    main()
