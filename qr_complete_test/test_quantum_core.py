"""Test quantum core components"""

import asyncio
from quantum_core.quantum_brain import QuantumBrain
from quantum_core.quantum_phi_harmonic import QuantumPhiHarmonicSystem

async def test_quantum_core():
    """Test core quantum components"""
    print("Testing Quantum Core Components...")
    
    # Initialize quantum brain with proven resonance
    brain = QuantumBrain()
    
    # Initialize phi-harmonic system
    phi_system = QuantumPhiHarmonicSystem()
    
    # Test state with proven frequency
    test_state = {
        'frequency': 4.37,  # Proven frequency
        'coherence': 0.96,  # Proven coherence
        'value': 1618034   # φ * 1000000
    }
    
    # Process through quantum brain
    print("\nProcessing through Quantum Brain...")
    brain_result = brain.process(test_state)
    
    print("\nQuantum Brain Results:")
    print(f"Coherence: {brain_result['coherence']:.6f}")
    print(f"Resonance: {brain_result['resonance']:.6f}")
    print(f"Stability: {brain_result['stability']:.6f}")
    
    # Process through phi-harmonic system
    print("\nProcessing through Phi-Harmonic System...")
    phi_result = phi_system.process_resonance(test_state['value'])
    
    print("\nPhi-Harmonic Results:")
    print(f"Pattern Strength: {float(phi_result['pattern_strength']):.6f}")
    print(f"Consciousness: {float(phi_result['consciousness']):.6f}")
    
    # Save brain state
    brain.save_brain("brain_states/quantum/brain.json")
    print("\nBrain state saved to brain_states/quantum/brain.json")

if __name__ == "__main__":
    asyncio.run(test_quantum_core())
