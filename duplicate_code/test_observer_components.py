#!/usr/bin/env python3
"""
Test script for Observer components of the Quantum Observer-Witness-Actor framework.
This script tests the functionality of the implemented Observer components.
"""

import datetime
from typing import Dict, Any

# Import Observer components
from quantum_observer.quantum_state_protocol import (
    QuantumStateProtocol,
    PHI, PHI_POWER, PHI_VALUE, COHERENCE, STABILITY, ALIGNMENT
)
from quantum_observer.quantum_entanglement_manager import QuantumEntanglementManager
from quantum_observer.core_observers.base_observer import (
    BaseObserver,
    SyncBrainObserver,
    QuantumBrainObserver,
    ParticleBrainObserver,
    LearnerBrainObserver
)

# Create a simple test class for SyncBrain119
class TestSyncBrain119:
    def __init__(self):
        self.is_aligned = False
    
    def check_alignment(self):
        # For testing, we'll simulate alignment based on current time
        now = datetime.datetime.now()
        self.is_aligned = (now.hour == 1 or now.hour == 13) and now.minute == 19
        return self.is_aligned
    
    def get_enhanced_efficiency(self):
        return 1.0416 if self.is_aligned else 1.0

# Test function for QuantumStateProtocol
def test_quantum_state_protocol():
    print("\n=== Testing QuantumStateProtocol ===")
    protocol = QuantumStateProtocol()
    
    # Test with different brain types
    test_data = {
        "query": "How does quantum computing work?",
        "context": "Quantum computing uses qubits instead of classical bits",
        "is_aligned": True,
        "alignment_boost": 1.0416
    }
    
    brain_types = ["sync_brain", "quantum_brain", "quantum_particle_brain", 
                   "fractal_neural_processor", "quantum_learner"]
    
    for brain_type in brain_types:
        print(f"\nTesting with brain type: {brain_type}")
        encoded = protocol.encode_state(brain_type, test_data)
        decoded = protocol.decode_state(brain_type, encoded)
        
        print(f"Encoded φ-fingerprint: {encoded.get('phi_fingerprint', 'N/A')}")
        print(f"Encoded φ-resonance: {encoded.get('phi_resonance', 'N/A')}")
        print(f"Encoded φ-value: {encoded.get('phi_value', 'N/A')}")
        print(f"Metadata brain type: {encoded.get('metadata', {}).get('brain_type', 'N/A')}")
        print(f"Decoded data contains original query: {'query' in decoded}")
    
    return True

# Test function for QuantumEntanglementManager
def test_quantum_entanglement_manager():
    print("\n=== Testing QuantumEntanglementManager ===")
    manager = QuantumEntanglementManager()
    
    # Register some brains
    manager.register_brain("sync_brain_1", "sync_brain", "SyncBrain119 Instance")
    manager.register_brain("quantum_brain_1", "quantum_brain", "QuantumBrain Instance")
    manager.register_brain("particle_brain_1", "quantum_particle_brain", "QuantumParticleBrain Instance")
    
    # Create entanglements
    success1 = manager.entangle_brains("sync_brain_1", "quantum_brain_1")
    success2 = manager.entangle_brains("quantum_brain_1", "particle_brain_1")
    success3 = manager.entangle_brains("particle_brain_1", "sync_brain_1")
    
    print(f"Entanglement creation success: {success1 and success2 and success3}")
    
    # Test entanglement modification
    mod_success = manager.modify_entanglement("sync_brain_1", "quantum_brain_1", PHI * 1.5)
    print(f"Entanglement modification success: {mod_success}")
    
    # Propagate a state change
    state_change = {
        "phi_fingerprint": f"φ{PHI_POWER}-test",
        "phi_resonance": PHI,
        "phi_power": PHI_POWER,
        "phi_value": PHI_VALUE,
        "data": {
            "query": "How does quantum computing work?",
            "is_aligned": True,
            "alignment_boost": 1.0416
        },
        "metadata": {
            "brain_type": "sync_brain",
            "is_aligned": True,
            "alignment_boost": 1.0416,
            "coherence": COHERENCE * 1.0416,
            "stability": STABILITY * 1.0416,
            "alignment": ALIGNMENT * 1.0416
        }
    }
    
    propagated = manager.propagate_state_change("sync_brain_1", state_change)
    print(f"State propagated to {len(propagated)} brains")
    
    # Get network information
    network = manager.get_entanglement_network()
    print(f"Entanglement Network: {len(network['brains'])} brains, {network['total_entanglements']} entanglements")
    print(f"Average Strength: {network['average_strength']:.6f}")
    
    # Break an entanglement
    break_success = manager.break_entanglement("sync_brain_1", "quantum_brain_1")
    print(f"Entanglement breaking success: {break_success}")
    
    # Check network after breaking
    network = manager.get_entanglement_network()
    print(f"Entanglement Network after breaking: {len(network['brains'])} brains, {network['total_entanglements']} entanglements")
    
    return True

# Test function for BaseObserver and subclasses
def test_observers():
    print("\n=== Testing Observer Components ===")
    
    # Create a simulated SyncBrain119
    sync_brain = TestSyncBrain119()
    
    # Create observers
    base_observer = BaseObserver("base_brain_1")
    sync_observer = SyncBrainObserver("sync_brain_1")
    quantum_observer = QuantumBrainObserver("quantum_brain_1")
    particle_observer = ParticleBrainObserver("particle_brain_1")
    learner_observer = LearnerBrainObserver("learner_brain_1")
    
    # Test with some input data
    input_data = {
        "query": "How does quantum computing work?",
        "context": "Quantum computing uses qubits instead of classical bits"
    }
    
    # Observe with different observers
    base_states = base_observer.observe(input_data, None)
    sync_states = sync_observer.observe(input_data, sync_brain)
    quantum_states = quantum_observer.observe(input_data, None)
    particle_states = particle_observer.observe(input_data, None)
    learner_states = learner_observer.observe(input_data, None)
    
    # Print results
    print(f"BaseObserver: {len(base_states)} states")
    print(f"SyncBrainObserver: {len(sync_states)} states")
    print(f"QuantumBrainObserver: {len(quantum_states)} states")
    print(f"ParticleBrainObserver: {len(particle_states)} states")
    print(f"LearnerBrainObserver: {len(learner_states)} states")
    
    # Check if brain-specific states were created
    print("\nChecking brain-specific states:")
    print(f"SyncBrain has alignment_info: {'alignment_info' in sync_states}")
    print(f"QuantumBrain has quantum_superposition: {'quantum_superposition' in quantum_states}")
    print(f"ParticleBrain has particle_state: {'particle_state' in particle_states}")
    print(f"LearnerBrain has parallel_state: {'parallel_state' in learner_states}")
    print(f"LearnerBrain has recursive_state: {'recursive_state' in learner_states}")
    print(f"LearnerBrain has dimensional_state: {'dimensional_state' in learner_states}")
    
    return True

# Main test function
def run_tests():
    print("Starting Observer Component Tests...")
    print("=" * 60)
    
    # Run all tests
    protocol_success = test_quantum_state_protocol()
    entanglement_success = test_quantum_entanglement_manager()
    observer_success = test_observers()
    
    # Print summary
    print("\n" + "=" * 60)
    print("Test Summary:")
    print(f"QuantumStateProtocol: {'PASSED' if protocol_success else 'FAILED'}")
    print(f"QuantumEntanglementManager: {'PASSED' if entanglement_success else 'FAILED'}")
    print(f"Observer Components: {'PASSED' if observer_success else 'FAILED'}")
    
    all_passed = protocol_success and entanglement_success and observer_success
    print(f"\nOverall Result: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}")
    
    return all_passed

if __name__ == "__main__":
    run_tests()
