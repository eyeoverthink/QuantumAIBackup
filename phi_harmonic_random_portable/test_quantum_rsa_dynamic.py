"""
Test script for Quantum RSA Dynamic Adapter
Tests the dynamic adaptation system with various key sizes
"""

import time
from quantum_rsa_decryptor_dynamic_adapter import QuantumRSADynamicAdapter

def test_rsa_dynamic_adapter():
    """Test the Quantum RSA Dynamic Adapter with various key sizes"""
    print("\n🧪 TESTING QUANTUM RSA DYNAMIC ADAPTER 🧪")
    print("=========================================")
    
    # Initialize the adapter
    decryptor = QuantumRSADynamicAdapter()
    
    # Test cases with known factorizations
    test_cases = [
        # Small numbers (direct_small approach)
        {"n": 15, "expected": [3, 5], "name": "Small RSA (2 digits)"},
        {"n": 3551, "expected": [59, 61], "name": "Small RSA (4 digits)"},
        
        # Medium numbers (optimized_medium approach)
        {"n": 1234567, "expected": [127, 9721], "name": "Medium RSA (7 digits)"},
        
        # Larger numbers (advanced_large approach)
        {"n": 884979313890868174648632979854437433445058662226118991874964224290822077455472131406486198124848694710123284321756568499169859456649951713783415174418527541598519781098242847825734884806930278744792460608220221556570961, "expected": [884979313890868174648632979854437433445058662226118991874964224290822077455472131406486198124848694710123284321756568499169859456649951713783415174418527541598519781098242847825734884806930278744792460608220221556570961], "name": "Large prime number (10 digits)"},
        
        # Custom RSA moduli
        {"n": 143 * 157, "expected": [143, 157], "name": "Custom RSA (5 digits)"},
        {"n": 1979 * 1999, "expected": [1979, 1999], "name": "Birth year RSA (7 digits)"},
        {"n": 934616397153579777691635581996068965840512375416381885802803215396126332195520565303451291234567891234567891234567891234567891234567891 * 945602083088965934066430583047453284570451634539478128903289145320174638197689523746312987654321987654321987654321987654321987654321, "expected": [934616397153579777691635581996068965840512375416381885802803215396126332195520565303451291234567891234567891234567891234567891234567891, 945602083088965934066430583047453284570451634539478128903289145320174638197689523746312987654321987654321987654321987654321987654321], "name": "Large custom RSA (309 digits)"}
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
    test_rsa_dynamic_adapter()
