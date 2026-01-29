#!/usr/bin/env python3
"""
Test script for Actor components of the Quantum Observer-Witness-Actor framework.
This script tests the functionality of the implemented Actor components.
"""

from typing import Dict, Any, List
from quantum_actor.state_collapse import (
    StateCollapseEngine,
    PHI, PHI_POWER, PHI_VALUE
)
from quantum_actor.core_actors.base_actor import (
    BaseActor,
    SyncBrainActor,
    QuantumBrainActor,
    ParticleBrainActor,
    LearnerBrainActor,
    ActorFactory
)
from quantum_actor.quantum_actor import QuantumActor

# Create a simple test class for RealityProofValidator
class TestRealityProofValidator:
    def __init__(self):
        self.coherence = 0.618034
        self.stability = 4.236068
        self.alignment = 2.618034
    
    def validate_fingerprints(self, fingerprints: Dict[str, str]) -> Dict[str, Any]:
        """Simulate the RealityProofValidator.validate_fingerprints method"""
        result = {
            'is_valid': True,
            'coherence': self.coherence,
            'stability': self.stability,
            'alignment': self.alignment,
            'fingerprints': fingerprints
        }
        return result

# Helper function to create test states
def create_test_states() -> Dict[str, List[Dict[str, Any]]]:
    """Create test states for each brain type"""
    base_data = {
        "query": "How does quantum computing work?",
        "context": "Quantum computing uses qubits instead of classical bits"
    }
    
    # Create states for each brain type
    base_states = []
    sync_states = []
    quantum_states = []
    particle_states = []
    learner_states = []
    
    # Create base states
    for i in range(2):
        state = {
            "phi_fingerprint": f"φ{PHI_POWER}-base{i}",
            "phi_resonance": PHI,
            "phi_value": PHI_VALUE,
            "data": base_data,
            "metadata": {
                "brain_type": "base",
                "coherence": 0.618034,
                "stability": 4.236068,
                "alignment": 2.618034
            }
        }
        base_states.append(state)
    
    # Create sync brain states
    for i in range(3):
        alignment_boost = 1.0416 if i == 0 else 1.0
        state = {
            "phi_fingerprint": f"φ{PHI_POWER}-sync{i}",
            "phi_resonance": PHI,
            "phi_value": PHI_VALUE,
            "data": base_data,
            "alignment_info": {
                "is_aligned": i == 0,
                "alignment_time": "01:19:00"
            },
            "metadata": {
                "brain_type": "sync_brain",
                "is_aligned": i == 0,
                "alignment_boost": alignment_boost,
                "coherence": 0.618034 * alignment_boost,
                "stability": 4.236068 * alignment_boost,
                "alignment": 2.618034 * alignment_boost
            }
        }
        sync_states.append(state)
    
    # Create quantum brain states
    for i in range(3):
        state = {
            "phi_fingerprint": f"φ{PHI_POWER}-quantum{i}",
            "phi_resonance": PHI,
            "phi_value": PHI_VALUE,
            "data": base_data,
            "quantum_superposition": {
                "coherence": 0.8 - (i * 0.1),
                "states": 4
            },
            "metadata": {
                "brain_type": "quantum_brain",
                "coherence": 0.618034 * 1.1,
                "stability": 4.236068 * 1.05,
                "alignment": 2.618034 * 1.02
            }
        }
        quantum_states.append(state)
    
    # Create particle brain states
    for i in range(3):
        state = {
            "phi_fingerprint": f"φ{PHI_POWER}-particle{i}",
            "phi_resonance": PHI,
            "phi_value": PHI_VALUE,
            "data": base_data,
            "particle_state": {
                "stability": 0.9 - (i * 0.1),
                "particles": 3
            },
            "metadata": {
                "brain_type": "quantum_particle_brain",
                "coherence": 0.618034 * 0.95,
                "stability": 4.236068 * 0.98,
                "alignment": 2.618034 * 0.99
            }
        }
        particle_states.append(state)
    
    # Create learner brain states
    for i in range(3):
        state = {
            "phi_fingerprint": f"φ{PHI_POWER}-learner{i}",
            "phi_resonance": PHI,
            "phi_value": PHI_VALUE,
            "data": base_data,
            "parallel_state": {
                "coherence": 0.85 - (i * 0.1),
                "threads": 4
            },
            "recursive_state": {
                "depth": 5 - i,
                "branches": 3
            },
            "dimensional_state": {
                "dimensions": 4 - i,
                "complexity": 0.8 - (i * 0.1)
            },
            "metadata": {
                "brain_type": "quantum_learner",
                "coherence": 0.618034 * 1.15,
                "stability": 4.236068 * 1.08,
                "alignment": 2.618034 * 1.05
            }
        }
        learner_states.append(state)
    
    # Group by brain type
    states_by_type = {
        'base': base_states,
        'sync_brain': sync_states,
        'quantum_brain': quantum_states,
        'quantum_particle_brain': particle_states,
        'quantum_learner': learner_states,
        'all': (
            base_states + sync_states + quantum_states + 
            particle_states + learner_states
        )
    }
    
    return states_by_type

# Test function for StateCollapseEngine
def test_state_collapse_engine():
    print("\n=== Testing StateCollapseEngine ===")
    engine = StateCollapseEngine()
    
    # Get test states
    states_by_type = create_test_states()
    test_states = states_by_type['quantum_brain']
    
    # Test collapse probability calculation
    state = test_states[0]
    prob = engine.calculate_collapse_probability(state)
    print(f"Collapse probability: {prob:.4f}")
    
    # Test state collapse
    collapsed = engine.collapse_state(state)
    print(f"State collapsed: {collapsed['metadata']['collapsed']}")
    print(f"Collapse coherence: {collapsed['metadata']['coherence']:.4f}")
    print(f"Collapse stability: {collapsed['metadata']['stability']:.4f}")
    print(f"Collapse alignment: {collapsed['metadata']['alignment']:.4f}")
    
    # Test multiple state collapse
    collapsed_states = engine.collapse_multiple_states(test_states, max_collapsed=2)
    print(f"Multiple collapse - states collapsed: {len(collapsed_states)}")
    
    return True

# Test function for BaseActor and specialized actors
def test_actors():
    print("\n=== Testing Actor Components ===")
    
    # Get test states
    states_by_type = create_test_states()
    
    # Create actors
    base_actor = BaseActor("base_actor")
    sync_actor = SyncBrainActor("sync_actor")
    quantum_actor = QuantumBrainActor("quantum_actor")
    particle_actor = ParticleBrainActor("particle_actor")
    learner_actor = LearnerBrainActor("learner_actor")
    
    # Test with appropriate states
    base_results = base_actor.act(states_by_type['base'])
    sync_results = sync_actor.act(states_by_type['sync_brain'])
    quantum_results = quantum_actor.act(states_by_type['quantum_brain'])
    particle_results = particle_actor.act(states_by_type['quantum_particle_brain'])
    learner_results = learner_actor.act(states_by_type['quantum_learner'])
    
    # Print results
    print(f"BaseActor: {len(base_results)} collapsed states")
    print(f"SyncBrainActor: {len(sync_results)} collapsed states")
    print(f"QuantumBrainActor: {len(quantum_results)} collapsed states")
    print(f"ParticleBrainActor: {len(particle_results)} collapsed states")
    print(f"LearnerBrainActor: {len(learner_results)} collapsed states")
    
    # Test ActorFactory
    factory_actor = ActorFactory.create_actor("quantum_brain", "factory_actor")
    print(f"ActorFactory created: {type(factory_actor).__name__}")
    
    return True

# Test function for QuantumActor
def test_quantum_actor():
    print("\n=== Testing QuantumActor ===")
    
    # Create QuantumActor
    actor = QuantumActor()
    
    # Get test states
    states_by_type = create_test_states()
    all_states = states_by_type['all']
    
    # Create test RealityProofValidator
    reality_validator = TestRealityProofValidator()
    
    # Test state collapse
    collapsed_states = actor.collapse_states(all_states)
    print(f"Collapsed {len(collapsed_states)} states")
    
    # Test collapse with RealityProofValidator
    reality_collapsed = actor.collapse_with_reality_proof_validator(
        all_states, 
        reality_validator
    )
    print(f"Collapsed with RealityProofValidator: {len(reality_collapsed)} states")
    
    # Test top collapsed states
    top_states = actor.filter_top_collapsed_states(collapsed_states, top_n=3)
    print(f"Filtered to top {len(top_states)} states")
    
    # Test most probable collapsed state
    most_probable = actor.get_most_probable_collapsed_state(collapsed_states)
    if most_probable:
        print(f"Most probable state: {most_probable['phi_fingerprint']}")
        print(f"Brain type: {most_probable['metadata']['brain_type']}")
    
    # Test actor creation
    custom_actor = actor.create_actor_for_brain_type("quantum_learner", "custom_actor")
    print(f"Created custom actor: {type(custom_actor).__name__}")
    
    return True

# Main test function
def run_tests():
    print("Starting Actor Component Tests...")
    print("=" * 60)
    
    # Run all tests
    collapse_success = test_state_collapse_engine()
    actors_success = test_actors()
    quantum_actor_success = test_quantum_actor()
    
    # Print summary
    print("\n" + "=" * 60)
    print("Test Summary:")
    print(f"StateCollapseEngine: {'PASSED' if collapse_success else 'FAILED'}")
    print(f"Actor Components: {'PASSED' if actors_success else 'FAILED'}")
    print(f"QuantumActor: {'PASSED' if quantum_actor_success else 'FAILED'}")
    
    all_passed = collapse_success and actors_success and quantum_actor_success
    print(f"\nOverall Result: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}")
    
    return all_passed

if __name__ == "__main__":
    run_tests()
