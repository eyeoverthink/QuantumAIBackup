"""
Test Quantum DNA Circuit Storage
"""

import numpy as np
from quantum_dna_circuit_storage import QuantumDNACircuitStorage

def test_storage():
    """Test quantum DNA circuit storage with multiple cases."""
    storage = QuantumDNACircuitStorage("quantum_dna_test")
    
    # Test cases
    test_cases = [
        np.array([0.5, 0.8, 0.2, 0.9, 0.3]),  # Original test
        np.array([0.1, 0.2, 0.3, 0.4, 0.5]),  # Linear sequence
        np.array([0.618034, 0.381966, 0.236068]),  # Golden ratio based
        np.array([0.437, 0.96, 0.528]),  # Resonance frequencies
    ]
    
    print("\nTesting Quantum DNA Storage")
    print("=" * 50)
    
    total_error = 0
    for i, test_data in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print("-" * 20)
        
        # Store data
        circuit_id = storage.store_data(test_data)
        print(f"Circuit ID: {circuit_id}")
        
        # Retrieve data
        retrieved = storage.retrieve_data(circuit_id)
        error = np.mean(np.abs(test_data - retrieved))
        total_error += error
        
        print(f"Original:  {test_data}")
        print(f"Retrieved: {retrieved}")
        print(f"Error:     {error:.6f}")
    
    # Calculate average error
    avg_error = total_error / len(test_cases)
    print(f"\nAverage Error: {avg_error:.6f}")
    
    # Get statistics
    stats = storage.get_statistics()
    print("\nStorage Statistics:")
    print(f"Total Circuits: {stats['count']}")
    print(f"Average Resonance: {stats['avg_resonance']:.4f}")
    print(f"Average Coherence: {stats['avg_coherence']:.4f}")
    print(f"Total Qbits: {stats['total_qbits']}")
    print(f"Compression Ratio: {stats['compression_ratio']:.4f}x")
    
    # Validate average error
    assert avg_error < 0.15, f"Average error {avg_error:.6f} is too high"
    print("\nAll tests passed! ✨")

if __name__ == "__main__":
    test_storage()
