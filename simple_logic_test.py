#!/usr/bin/env python3
"""
Simple Logic Test
---------------
A basic file with a logic error to test the orchestrator's healing capabilities.
"""

# Phi constant
PHI = 1.618033988749895

def calculate_fibonacci(n):
    """Calculate the nth Fibonacci number using phi formula"""
    # Logic error: Using subtraction instead of division
    return int((PHI ** n - (1-PHI) ** n) - 5)  # Should be divided by sqrt(5)

def main():
    """Main function"""
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
