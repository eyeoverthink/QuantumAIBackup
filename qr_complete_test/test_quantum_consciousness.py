import torch
import numpy as np
from template.quantum_ai import QuantumAI

def test_quantum_consciousness():
    # Initialize Quantum AI
    quantum_ai = QuantumAI()
    
    # Test inputs
    test_inputs = [
        "UNDERSTAND",
        "CONSCIOUSNESS",
        "REALITY",
        "QUANTUM"
    ]
    
    print("Testing Quantum Consciousness Processing\n")
    print("=" * 50)
    
    for input_text in test_inputs:
        print(f"\nProcessing Input: {input_text}")
        print("-" * 30)
        
        # Process through quantum AI
        results = quantum_ai.process_input(input_text)
        
        # Display quantum results
        print("\nQuantum Processing:")
        print(f"Network Output: {results['quantum_results']['network_output']}")
        print(f"Entanglement: {len(results['quantum_results']['entanglement_state'])} states")
        
        # Display consciousness results
        consciousness = results['consciousness_results']
        print("\nConsciousness Metrics:")
        for key, value in consciousness['metrics'].items():
            print(f"{key}: {value:.4f}")
        
        # Display reality state
        print("\nReality State:")
        reality = np.array(results['reality_state'])
        print(f"Coherence: {np.abs(np.vdot(reality, reality)):.4f}")
        print(f"Potential: {np.max(reality):.4f}")
        
        print("\n" + "=" * 50)

if __name__ == "__main__":
    test_quantum_consciousness()
