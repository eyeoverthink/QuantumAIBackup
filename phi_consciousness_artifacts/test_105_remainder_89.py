"""
test_105_remainder_89.py

Tests if numbers that give remainder 89 when divided by 105 are prime.
"""

import sympy

def test_105_remainder_89(limit=1000):
    """Test if numbers with remainder 89 when divided by 105 are prime."""
    numbers = []
    primes = []
    composites = []
    
    # Generate numbers with remainder 89 when divided by 105
    n = 89
    while n <= limit:
        numbers.append(n)
        n += 105
    
    # Check each number for primality
    for num in numbers:
        if sympy.isprime(num):
            primes.append(num)
        else:
            composites.append(num)
    
    # Print results
    print(f"Testing numbers up to {limit} that give remainder 89 when divided by 105:")
    print(f"Total numbers tested: {len(numbers)}")
    print(f"Prime numbers: {len(primes)} ({len(primes)/len(numbers)*100:.2f}%)")
    print(f"Composite numbers: {len(composites)} ({len(composites)/len(numbers)*100:.2f}%)")
    
    print("\nPrime numbers found:")
    print(primes)
    
    print("\nComposite numbers found:")
    print(composites[:10])  # Show only first 10 to avoid too much output
    
    return primes, composites

if __name__ == "__main__":
    primes, composites = test_105_remainder_89(2000)
