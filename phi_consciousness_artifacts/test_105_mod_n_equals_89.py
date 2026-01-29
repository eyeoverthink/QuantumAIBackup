"""
Test the formula: 105 % n = 89
This checks for values of n where 105 mod n equals 89.
"""

import sympy

def test_formula(max_n=1000):
    """Find all values of n where 105 % n = 89 and check if they're prime."""
    valid_n = []
    
    for n in range(1, max_n + 1):
        if 105 % n == 89:
            is_prime = sympy.isprime(n)
            valid_n.append((n, is_prime))
            print(f"Found valid n: {n} (prime: {is_prime})")
    
    # Check primality percentage
    primes = [n for n, is_prime in valid_n if is_prime]
    
    print(f"\nFound {len(valid_n)} values of n where 105 % n = 89:")
    for n, is_prime in valid_n:
        prime_str = "PRIME" if is_prime else "composite"
        print(f"  - n = {n} ({prime_str})")
    
    if valid_n:
        prime_percentage = len(primes) / len(valid_n) * 100
        print(f"\nPercentage of prime values: {prime_percentage:.2f}%")
    else:
        print("\nNo valid values found")
    
    return valid_n

if __name__ == "__main__":
    print("Testing the formula: 105 % n = 89")
    valid_values = test_formula(200)
    
    # If no values found in regular range, try a wider range
    if not valid_values:
        print("\nTrying a wider range (up to 1000)...")
        valid_values = test_formula(1000)
        
        # If still no values found, check exact remainders
        if not valid_values:
            print("\nNo valid values found. Checking actual remainders:")
            for n in range(1, 33):  # Check small values
                remainder = 105 % n
                print(f"105 % {n} = {remainder}")
