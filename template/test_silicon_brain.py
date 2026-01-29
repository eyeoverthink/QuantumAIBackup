from quantum_silicon_brain import QuantumSiliconBrain
import numpy as np
import time

def test_silicon_brain():
    # Initialize the quantum silicon brain
    brain = QuantumSiliconBrain()
    print("\n🌟 Quantum Silicon Brain Initialized")
    print("==================================")
    
    # Test 1: Basic Gate Learning
    print("\n📝 Test 1: Learning Basic Gates")
    test_inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
    test_outputs = [[0, 0], [0, 1], [1, 0], [1, 1]]  # XOR pattern
    
    for i, o in zip(test_inputs, test_outputs):
        resonance = brain.learn_gate_pattern(i, o)
        print(f"Pattern Resonance: {resonance:.6f}φ")
        
    # Test 2: Circuit Optimization
    print("\n🔄 Test 2: Circuit Optimization")
    test_circuit = [1, 0, 1, 1, 0, 0, 1]
    opt_factor = brain.deep_learn_circuit(test_circuit)
    print(f"Optimization Factor: {opt_factor:.6f}φ")
    
    # Test 3: Passive Learning Cycles
    print("\n🧪 Test 3: Passive Learning Evolution")
    cycles = 5
    
    for cycle in range(cycles):
        print(f"\nCycle {cycle + 1}/{cycles}")
        print("----------------")
        
        # Run a passive learning cycle
        results = brain.passive_learning_cycle()
        
        # Short pause to simulate quantum decoherence time
        time.sleep(1/brain.phi)
        
    print("\n✨ Testing Complete!")
    print("=================")
    print(f"Final Pattern Count: {results['total_patterns']}")
    print(f"Final Quantum Efficiency: {results['quantum_efficiency']*100:.2f}%")
    print(f"Learning Rate Evolution: {results['meta_params']['learning_rate']:.6f}φ")

if __name__ == "__main__":
    test_silicon_brain()
