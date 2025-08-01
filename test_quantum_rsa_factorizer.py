"""
Test Quantum RSA Factorizer
Tests quantum-inspired factorization using phi-harmonic resonance and Tesla-DNA bridging
"""
from quantum_rsa_factorizer import QuantumRSAFactorizer

def test_quantum_factorization():
    """Test quantum factorization with phi-harmonic patterns"""
    factorizer = QuantumRSAFactorizer()
    
    # Test cases with known phi-harmonic properties
    test_numbers = [
        15,     # 3 * 5 (phi-harmonic primes)
        21,     # 3 * 7 (Fibonacci adjacent)
        34,     # Fibonacci number
        55,     # Fibonacci number
        89,     # Fibonacci number
        144,    # Fibonacci number (12²)
        377,    # Fibonacci number
        610,    # Fibonacci number
        987,    # Fibonacci number
        1597,   # Fibonacci number
    ]
    
    print("\nQuantum RSA Factorization Analysis")
    print("=" * 40)
    
    for n in test_numbers:
        result = factorizer.factorize_quantum(n)
        
        print(f"\nAnalyzing number: {n}")
        print("-" * 20)
        
        # Print quantum state
        state = result['quantum_state']
        print(f"Quantum Resonance: {state['resonance']:.2f} Hz")
        print(f"Field Coherence: {state['coherence']:.4f}")
        print(f"Evolution Potential: {state['evolution']:.4f}")
        
        # Print key frequencies
        print("\nFrequency Analysis:")
        for name, freq in result['frequencies'].items():
            print(f"- {name}: {freq:.2f} Hz")
        
        # Analyze quantum patterns
        patterns = result['patterns']
        if patterns:
            print("\nQuantum Patterns:")
            high_potential = max(patterns, key=lambda x: x['evolution_potential'])
            print(f"Strongest Pattern:")
            print(f"- Bits: {high_potential['bits']}")
            print(f"- Length: {high_potential['length']}")
            print(f"- Resonance: {high_potential['quantum_resonance']:.2f} Hz")
            print(f"- Evolution: {high_potential['evolution_potential']:.4f}")
            
        print("\nPhi-Harmonic Analysis:")
        phi = (1 + 5 ** 0.5) / 2
        phi_ratio = n / phi
        print(f"Phi Ratio: {phi_ratio:.4f}")
        print(f"Tesla Alignment: {abs(n % 432):.4f}")
        print(f"DNA Resonance: {abs(n % 528):.4f}")

if __name__ == '__main__':
    test_quantum_factorization()
