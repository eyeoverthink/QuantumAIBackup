import numpy as np
from phi_quantum_brain import PhiQuantumBrain
import time

def test_quantum_brain():
    brain = PhiQuantumBrain()
    
    print("\nQuantum Brain Test")
    print("=================")
    
    # Test data sizes
    sizes = [1000, 10000, 100000]
    
    for size in sizes:
        data = np.random.random(size)
        
        print(f"\nProcessing {size} data points:")
        start = time.time()
        result, efficiencies = brain.run_quantum_computation(data)
        duration = time.time() - start
        
        print(f"Time: {duration:.4f}s")
        print("\nLayer Efficiencies:")
        for level, eff in enumerate(efficiencies):
            print(f"Layer {level}: {eff:.2f}x")
            
        state = brain.get_system_state()
        print(f"\nQuantum Bridges: {len(state['bridges'])}")
        print(f"Resonance: {state['resonance']:.2f}")
        
        # Check φ scaling
        scaling = np.array([abs(eff) for eff in efficiencies])
        ratio = scaling[1:] / scaling[:-1]
        print(f"\nφ² Scaling Check: {np.mean(ratio):.3f} (target: {1.618*1.618:.3f})")

if __name__ == "__main__":
    test_quantum_brain()
