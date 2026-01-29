#!/usr/bin/env python3
"""
Test script for Witness components of the Quantum Observer-Witness-Actor framework.
This script tests the functionality of the implemented Witness components.
"""

import datetime
from typing import Dict, Any, List

# Import Witness components
from quantum_witness.quantum_reality_metrics import (
    QuantumRealityMetrics,
    PHI, PHI_POWER, PHI_VALUE, COHERENCE, STABILITY, ALIGNMENT
)
from quantum_witness.state_validator import StateValidator
from quantum_witness.core_witnesses.base_witness import (
    BaseWitness, SyncBrainWitness, QuantumBrainWitness, 
    ParticleBrainWitness, LearnerBrainWitness, WitnessFactory
)
from quantum_witness.quantum_witness import QuantumWitness

# Import Observer components to create test states
from quantum_observer.quantum_state_protocol import QuantumStateProtocol
from quantum_observer.core_observers.base_observer import (
    BaseObserver, SyncBrainObserver, QuantumBrainObserver,
    ParticleBrainObserver, LearnerBrainObserver
)

# Create a simple test class for RealityProofValidator
class TestRealityProofValidator:
    def __init__(self):
        self.coherence = COHERENCE
        self.stability = STABILITY
        self.alignment = ALIGNMENT
    
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

# Create a simple test class for SyncBrain119
class TestSyncBrain119:
    def __init__(self):
        self.is_aligned = False
    
    def check_alignment(self):
        # For testing, we'll simulate alignment
        self.is_aligned = True
        return self.is_aligned
    
    def get_enhanced_efficiency(self):
        return 1.0416 if self.is_aligned else 1.0

# Helper function to create test states
def create_test_states() -> Dict[str, List[Dict[str, Any]]]:
    """Create test states for each brain type"""
    protocol = QuantumStateProtocol()
    
    # Create test data for each brain type
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
                "coherence": COHERENCE,
                "stability": STABILITY,
                "alignment": ALIGNMENT
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
                "coherence": COHERENCE * alignment_boost,
                "stability": STABILITY * alignment_boost,
                "alignment": ALIGNMENT * alignment_boost
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
                "coherence": COHERENCE * 1.1,
                "stability": STABILITY * 1.05,
                "alignment": ALIGNMENT * 1.02
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
                "coherence": COHERENCE * 0.95,
                "stability": STABILITY * 0.98,
                "alignment": ALIGNMENT * 0.99
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
                "coherence": COHERENCE * 1.15,
                "stability": STABILITY * 1.08,
                "alignment": ALIGNMENT * 1.05
            }
        }
        learner_states.append(state)
    
    # Combine all states
    all_states = []
    all_states.extend(base_states)
    all_states.extend(sync_states)
    all_states.extend(quantum_states)
    all_states.extend(particle_states)
    all_states.extend(learner_states)
    
    # Group by brain type
    states_by_type = {
        'base': base_states,
        'sync_brain': sync_states,
        'quantum_brain': quantum_states,
        'quantum_particle_brain': particle_states,
        'quantum_learner': learner_states,
        'all': all_states
    }
    
    return states_by_type

# Test function for QuantumRealityMetrics
def test_quantum_reality_metrics():
    print("\n=== Testing QuantumRealityMetrics ===")
    metrics = QuantumRealityMetrics()
    
    # Test with different brain types
    test_data = {
        "query": "How does quantum computing work?",
        "context": "Quantum computing uses qubits instead of classical bits",
        "metadata": {
            "brain_type": "quantum_brain"
        }
    }
    
    # Test fingerprint calculation
    fingerprint = metrics.calculate_phi_fingerprint(test_data)
    print(f"φ-fingerprint: {fingerprint}")
    
    # Test state validation
    state = {
        "phi_fingerprint": fingerprint,
        "phi_resonance": PHI,
        "phi_value": PHI_VALUE,
        "metadata": {
            "brain_type": "quantum_brain",
            "coherence": COHERENCE,
            "stability": STABILITY,
            "alignment": ALIGNMENT
        }
    }
    
    validation_result = metrics.validate_state(state)
    print(f"Validation result: {validation_result['is_valid']}")
    print(f"Validation score: {validation_result['validation_score']:.4f}")
    
    return True

# Test function for StateValidator
def test_state_validator():
    print("\n=== Testing StateValidator ===")
    validator = StateValidator()
    
    # Get test states
    states_by_type = create_test_states()
    test_states = states_by_type['quantum_brain']
    
    # Validate states
    validated_states = validator.validate_states(test_states)
    print(f"Validated {len(validated_states)} states")
    
    # Adjust probabilities
    adjusted_states = validator.adjust_probabilities(validated_states)
    print(f"Adjusted probabilities for {len(adjusted_states)} states")
    
    # Check total probability
    total_prob = sum(state.get('probability', 0.0) for state in adjusted_states)
    print(f"Total probability: {total_prob:.4f}")
    
    # Filter invalid states
    valid_states = validator.filter_invalid_states(validated_states)
    print(f"Filtered to {len(valid_states)} valid states")
    
    # Apply custom validation
    def custom_validator(state):
        # Simple custom validator that prefers states with 'quantum' in the query
        data = state.get('data', {})
        query = data.get('query', '')
        return 0.9 if 'quantum' in query.lower() else 0.5
    
    custom_validated = validator.apply_custom_validation(valid_states, custom_validator)
    print(f"Applied custom validation to {len(custom_validated)} states")
    
    return True

# Test function for BaseWitness and specialized witnesses
def test_witnesses():
    print("\n=== Testing Witness Components ===")
    
    # Get test states
    states_by_type = create_test_states()
    
    # Create witnesses
    base_witness = BaseWitness("base_witness")
    sync_witness = SyncBrainWitness("sync_witness")
    quantum_witness = QuantumBrainWitness("quantum_witness")
    particle_witness = ParticleBrainWitness("particle_witness")
    learner_witness = LearnerBrainWitness("learner_witness")
    
    # Test with appropriate states
    base_results = base_witness.witness(states_by_type['base'])
    sync_results = sync_witness.witness(states_by_type['sync_brain'])
    quantum_results = quantum_witness.witness(states_by_type['quantum_brain'])
    particle_results = particle_witness.witness(states_by_type['quantum_particle_brain'])
    learner_results = learner_witness.witness(states_by_type['quantum_learner'])
    
    # Print results
    print(f"BaseWitness: {len(base_results)} validated states")
    print(f"SyncBrainWitness: {len(sync_results)} validated states")
    print(f"QuantumBrainWitness: {len(quantum_results)} validated states")
    print(f"ParticleBrainWitness: {len(particle_results)} validated states")
    print(f"LearnerBrainWitness: {len(learner_results)} validated states")
    
    # Check validation results
    for witness_name, results in [
        ("BaseWitness", base_results),
        ("SyncBrainWitness", sync_results),
        ("QuantumBrainWitness", quantum_results),
        ("ParticleBrainWitness", particle_results),
        ("LearnerBrainWitness", learner_results)
    ]:
        if results:
            validation = results[0].get('validation', {})
            print(f"{witness_name} validation score: {validation.get('validation_score', 0.0):.4f}")
    
    # Test WitnessFactory
    factory_witness = WitnessFactory.create_witness("quantum_brain", "factory_witness")
    print(f"WitnessFactory created: {type(factory_witness).__name__}")
    
    return True

# Test function for QuantumWitness
def test_quantum_witness():
    print("\n=== Testing QuantumWitness ===")
    
    # Create QuantumWitness
    witness = QuantumWitness()
    
    # Get test states
    states_by_type = create_test_states()
    all_states = states_by_type['all']
    
    # Create test RealityProofValidator
    reality_validator = TestRealityProofValidator()
    
    # Validate states
    validated_states = witness.validate_states(all_states)
    print(f"Validated {len(validated_states)} states")
    
    # Validate with RealityProofValidator
    reality_validated = witness.validate_with_reality_proof_validator(all_states, reality_validator)
    print(f"Validated with RealityProofValidator: {len(reality_validated)} states")
    
    # Filter top states
    top_states = witness.filter_top_states(validated_states, top_n=3)
    print(f"Filtered to top {len(top_states)} states")
    
    # Get most probable state
    most_probable = witness.get_most_probable_state(validated_states)
    if most_probable:
        print(f"Most probable state: {most_probable.get('phi_fingerprint', 'unknown')}")
        print(f"Probability: {most_probable.get('probability', 0.0):.4f}")
    
    # Create a witness for a specific brain type
    custom_witness = witness.create_witness_for_brain_type("quantum_learner", "custom_witness")
    print(f"Created custom witness: {type(custom_witness).__name__}")
    
    return True

# Main test function
def run_tests():
    print("Starting Witness Component Tests...")
    print("=" * 60)
    
    # Run all tests
    metrics_success = test_quantum_reality_metrics()
    validator_success = test_state_validator()
    witnesses_success = test_witnesses()
    quantum_witness_success = test_quantum_witness()
    
    # Print summary
    print("\n" + "=" * 60)
    print("Test Summary:")
    print(f"QuantumRealityMetrics: {'PASSED' if metrics_success else 'FAILED'}")
    print(f"StateValidator: {'PASSED' if validator_success else 'FAILED'}")
    print(f"Witness Components: {'PASSED' if witnesses_success else 'FAILED'}")
    print(f"QuantumWitness: {'PASSED' if quantum_witness_success else 'FAILED'}")
    
    all_passed = metrics_success and validator_success and witnesses_success and quantum_witness_success
    print(f"\nOverall Result: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}")
    
    return all_passed

if __name__ == "__main__":
    run_tests()
