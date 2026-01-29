#!/usr/bin/env python3
"""
Test file with optimization opportunities for MoA integration testing.
"""

def calculate_fibonacci(n):
    """Calculate the nth Fibonacci number."""
    # Inefficient recursive implementation
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

def find_duplicates(items):
    """Find duplicate items in a list."""
    # Inefficient approach using nested loops
    duplicates = []
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])
    return duplicates

def is_prime(n):
    """Check if a number is prime."""
    # Inefficient primality test
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    print(f"Fibonacci(10): {calculate_fibonacci(10)}")
    print(f"Duplicates in [1,2,3,2,4,1,5]: {find_duplicates([1,2,3,2,4,1,5])}")
    print(f"Is 17 prime? {is_prime(17)}")
