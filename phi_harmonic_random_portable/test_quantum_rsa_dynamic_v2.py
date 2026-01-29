"""
Test script for Quantum RSA Dynamic Adapter V2
Tests the enhanced dynamic adaptation system with improved factorization accuracy
"""

import time
from quantum_rsa_decryptor_dynamic_adapter_v2 import QuantumRSADynamicAdapterV2

def test_rsa_dynamic_adapter_v2():
    """Test the enhanced Quantum RSA Dynamic Adapter with various key sizes"""
    print("\n🧪 TESTING QUANTUM RSA DYNAMIC ADAPTER V2 🧪")
    print("=============================================")
    
    # Initialize the adapter
    decryptor = QuantumRSADynamicAdapterV2()
    
    # Test cases with known factorizations
    test_cases = [
        # Small numbers (direct_small approach)
        {"n": 15, "expected": [3, 5], "name": "Small RSA (2 digits)"},
        {"n": 3551, "expected": [59, 61], "name": "Small RSA (4 digits)"},
        
        # Medium numbers (optimized_medium approach)
        {"n": 1234567, "expected": [127, 9721], "name": "Medium RSA (7 digits)"},
        
        # Larger numbers (advanced_large approach)
        {"n": 104438888141315250669175271071662438257996424904738378038423348328395390797155376226523969284215667733575448289987899350239577407632021297696387851680635375700008839134724598441086739169645864004964273906234579124188583112389451695493619981015158019493563013064260725181956743336189530244313258976042731855611,
        "expected": [32416190071  *  3221225473  *  1000000007  *  1013904223],
        "name": "Hard RSA (1024-bit modulus)"},
        
        # Custom RSA moduli
        {"n": 143 * 157, "expected": [143, 157], "name": "Custom RSA (5 digits)"},
        {"n": 1979 * 1999, "expected": [1979, 1999], "name": "Birth year RSA (7 digits)"},
        {"n": 32416190071  *  3221225473  *  1000000007  *  1013904223, "expected": [32416190071, 3221225473, 1000000007, 1013904223], "name": "Large custom RSA (12 digits)"}
    ]
    
    # Run the tests
    results = []
    for i, test in enumerate(test_cases):
        print(f"\n📊 Test {i+1}: {test['name']} - n = {test['n']}")
        
        # Time the factorization
        start_time = time.time()
        factors = decryptor.factorize(test["n"])
        elapsed_time = time.time() - start_time
        
        # Check if the factorization is correct
        factors.sort()
        expected = test["expected"]
        expected.sort()
        
        is_correct = factors == expected
        
        # Store the result
        results.append({
            "name": test["name"],
            "n": test["n"],
            "expected": expected,
            "actual": factors,
            "correct": is_correct,
            "time": elapsed_time
        })
        
        # Print the result
        print(f"  Expected: {expected}")
        print(f"  Actual:   {factors}")
        print(f"  Correct:  {'✅' if is_correct else '❌'}")
        print(f"  Time:     {elapsed_time:.6f} seconds")
    
    # Print the summary
    print("\n📋 TEST SUMMARY 📋")
    print("=================")
    correct_count = sum(1 for r in results if r["correct"])
    print(f"Total tests:  {len(results)}")
    print(f"Correct:      {correct_count}")
    print(f"Success rate: {correct_count / len(results) * 100:.2f}%")
    
    # Print the metrics
    print("\n📈 METRICS 📈")
    print("============")
    print(f"Attempts:                  {decryptor.metrics['attempts']}")
    print(f"Successful factorizations: {decryptor.metrics['successful_factorizations']}")
    print(f"Largest factored:          {decryptor.metrics['largest_factored']}")
    print(f"Average time:              {decryptor.metrics['average_time']:.6f} seconds")
    print(f"Total time:                {decryptor.metrics['total_time']:.6f} seconds")
    print(f"Coherence:                 {decryptor.metrics['coherence']:.6f}")
    print(f"Resonance:                 {decryptor.metrics['resonance']:.6f}")
    print(f"Entropy:                   {decryptor.metrics['entropy']:.6f} bits/byte")

if __name__ == "__main__":
    test_rsa_dynamic_adapter_v2()
