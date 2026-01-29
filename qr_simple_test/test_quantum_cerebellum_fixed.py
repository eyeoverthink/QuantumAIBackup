#!/usr/bin/env python3
"""
Test script for Phi-Harmonic Quantum Cerebellum
==============================================
Validates the quantum cerebellum's functions and measures key phi-harmonic metrics.
Tests resonance patterns, learning capabilities, and coordination functions.
"""

import os
import sys
import time
import math
import json
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext
from datetime import datetime

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import cerebellum test extension
from phi_harmonic_cerebellum_test_extension import PhiHarmonicCerebellumTestExtension

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ)
PHI_CUBED = PHI**3  # φ³ ≈ 4.236068
EXPECTED_COHERENCE = 0.9918  # Expected quantum coherence

# Helper function to ensure NumPy types are properly serialized to JSON
def make_json_serializable(obj):
    """Convert NumPy types to standard Python types for JSON serialization"""
    if isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, np.bool_):
        return bool(obj)
    elif isinstance(obj, (list, tuple)):
        return [make_json_serializable(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: make_json_serializable(value) for key, value in obj.items()}
    else:
        return obj

class QuantumCerebellumTester:
    """Test harness for the phi-harmonic quantum cerebellum"""
    
    def __init__(self):
        """Initialize the test harness"""
        self.test_results = {
            "resonance_test": {"passed": False, "score": 0, "metrics": {}},
            "learning_test": {"passed": False, "score": 0, "metrics": {}},
            "coordination_test": {"passed": False, "score": 0, "metrics": {}},
            "frequency_test": {"passed": False, "score": 0, "metrics": {}},
            "overall": {"passed": False, "score": 0, "metrics": {}}
        }
        
        # Create output directory
        self.output_dir = "quantum_cerebellum_test_results"
        os.makedirs(self.output_dir, exist_ok=True)
        
        print(f"Phi-Harmonic Quantum Cerebellum Test Harness Initialized")
        print("=" * 70)
    
    def test_resonance(self, cerebellum):
        """Test phi-harmonic resonance patterns"""
        print("\nTesting phi-harmonic resonance...")
        
        # Get cerebellum state
        cerebellum_state = cerebellum.cerebellum_state
        
        # Check if cerebellum frequency is close to φ³
        cerebellum_frequency = cerebellum_state["cerebellum_frequency"]
        frequency_error = abs(cerebellum_frequency - PHI_CUBED) / PHI_CUBED
        frequency_accuracy = 1 - frequency_error
        
        # Check phi-resonance and coherence
        phi_resonance = cerebellum_state["cerebellum_phi_resonance"]
        coherence = cerebellum_state["cerebellum_coherence"]
        coherence_match = 1 - abs(coherence - EXPECTED_COHERENCE) / EXPECTED_COHERENCE
        
        # Calculate resonance score (1.0 = perfect)
        resonance_score = (frequency_accuracy + coherence_match) / 2
        
        # Store test metrics
        self.test_results["resonance_test"]["metrics"] = {
            "frequency": cerebellum_frequency,
            "expected_frequency": PHI_CUBED,
            "frequency_accuracy": frequency_accuracy,
            "phi_resonance": phi_resonance,
            "coherence": coherence,
            "expected_coherence": EXPECTED_COHERENCE,
            "coherence_match": coherence_match
        }
        
        # Set test score and passed status
        self.test_results["resonance_test"]["score"] = resonance_score
        self.test_results["resonance_test"]["passed"] = resonance_score > 0.9
        
        # Print results
        print(f"  Frequency: {cerebellum_frequency:.6f} Hz (expected: {PHI_CUBED:.6f} Hz)")
        print(f"  Frequency accuracy: {frequency_accuracy:.6f}")
        print(f"  Phi resonance: {phi_resonance:.6f}")
        print(f"  Coherence: {coherence:.6f} (expected: {EXPECTED_COHERENCE:.6f})")
        print(f"  Coherence match: {coherence_match:.6f}")
        print(f"  Resonance test score: {resonance_score:.6f}")
        print(f"  Resonance test passed: {self.test_results['resonance_test']['passed']}")
        
        return self.test_results["resonance_test"]["passed"]
    
    def test_learning(self, cerebellum):
        """Test cerebellum learning capabilities"""
        print("\nTesting learning capabilities...")
        
        # Get cerebellum state and neural network
        cerebellum_state = cerebellum.cerebellum_state
        neural_network = cerebellum.neural_network
        
        # Check learning rate against golden ratio inverse
        learning_rate = cerebellum_state["cerebellum_learning_rate"]
        learning_rate_accuracy = 1 - abs(learning_rate - 1/PHI) / (1/PHI)
        
        # Check neural network structure
        network_completeness = min(1.0, neural_network["total_neurons"] / 1e7)
        
        # Run learning simulation
        learning_curve = []
        error_start = 1.0
        error_target = 0.01
        learning_cycles = 10
        current_error = error_start
        
        for _ in range(learning_cycles):
            # Simplified learning simulation with phi-harmonic decay
            current_error *= (1 - learning_rate)
            learning_curve.append(current_error)
        
        # Calculate learning metrics
        learning_efficiency = 1 - (learning_curve[-1] / error_start)
        learning_speed = -math.log(learning_curve[-1] / error_start) / learning_cycles
        
        # Calculate learning score (1.0 = perfect)
        learning_score = (learning_rate_accuracy + network_completeness + learning_efficiency) / 3
        
        # Store test metrics
        self.test_results["learning_test"]["metrics"] = {
            "learning_rate": learning_rate,
            "expected_learning_rate": 1/PHI,
            "learning_rate_accuracy": learning_rate_accuracy,
            "network_neurons": neural_network["total_neurons"],
            "network_connections": neural_network["total_connections"],
            "network_completeness": network_completeness,
            "learning_efficiency": learning_efficiency,
            "learning_speed": learning_speed,
            "learning_curve": learning_curve
        }
        
        # Set test score and passed status
        self.test_results["learning_test"]["score"] = learning_score
        self.test_results["learning_test"]["passed"] = learning_score > 0.8
        
        # Print results
        print(f"  Learning rate: {learning_rate:.6f} (expected: {1/PHI:.6f})")
        print(f"  Learning rate accuracy: {learning_rate_accuracy:.6f}")
        print(f"  Network neurons: {neural_network['total_neurons']}")
        print(f"  Network connections: {neural_network['total_connections']}")
        print(f"  Network completeness: {network_completeness:.6f}")
        print(f"  Learning efficiency: {learning_efficiency:.6f}")
        print(f"  Learning speed: {learning_speed:.6f}")
        print(f"  Learning test score: {learning_score:.6f}")
        print(f"  Learning test passed: {self.test_results['learning_test']['passed']}")
        
        # Create learning curve plot
        plt.figure(figsize=(10, 6))
        plt.plot(learning_curve, 'b-', linewidth=2)
        plt.title('Phi-Harmonic Learning Curve')
        plt.xlabel('Cycle')
        plt.ylabel('Error')
        plt.grid(True)
        plt.savefig(os.path.join(self.output_dir, 'learning_curve.png'))
        plt.close()
        
        return self.test_results["learning_test"]["passed"]
    
    def test_coordination(self, cerebellum):
        """Test cerebellum coordination functions"""
        print("\nTesting coordination functions...")
        
        # Get cerebellum state
        cerebellum_state = cerebellum.cerebellum_state
        
        # Check coordination factor against golden ratio
        coordination_factor = cerebellum_state["cerebellum_coordination_factor"]
        coordination_accuracy = 1 - abs(coordination_factor - PHI) / PHI
        
        # Check timing precision 
        timing_precision = cerebellum_state["cerebellum_timing_precision"]
        timing_quality = 1 - (timing_precision / 0.01)  # Lower is better, 1ms = excellent
        
        # Test coordination stability over time
        stability_samples = 5
        coordination_stability = []
        
        for _ in range(stability_samples):
            # Simulate movement coordination task
            # In a real test, this would connect to actual movement data
            coordination_quality = coordination_factor * (1 - np.random.random() * 0.1)
            coordination_stability.append(coordination_quality)
            time.sleep(0.01)  # Brief pause between samples
        
        # Calculate stability metrics
        stability_mean = np.mean(coordination_stability)
        stability_std = np.std(coordination_stability)
        stability_quality = 1 - stability_std / stability_mean
        
        # Calculate coordination score (1.0 = perfect)
        coordination_score = (coordination_accuracy + timing_quality + stability_quality) / 3
        
        # Store test metrics
        self.test_results["coordination_test"]["metrics"] = {
            "coordination_factor": coordination_factor,
            "expected_coordination_factor": PHI,
            "coordination_accuracy": coordination_accuracy,
            "timing_precision": timing_precision,
            "timing_quality": timing_quality,
            "stability_mean": stability_mean,
            "stability_std": stability_std,
            "stability_quality": stability_quality,
            "coordination_samples": coordination_stability
        }
        
        # Set test score and passed status
        self.test_results["coordination_test"]["score"] = coordination_score
        self.test_results["coordination_test"]["passed"] = coordination_score > 0.85
        
        # Print results
        print(f"  Coordination factor: {coordination_factor:.6f} (expected: {PHI:.6f})")
        print(f"  Coordination accuracy: {coordination_accuracy:.6f}")
        print(f"  Timing precision: {timing_precision:.6f} s")
        print(f"  Timing quality: {timing_quality:.6f}")
        print(f"  Stability mean: {stability_mean:.6f}")
        print(f"  Stability std: {stability_std:.6f}")
        print(f"  Stability quality: {stability_quality:.6f}")
        print(f"  Coordination test score: {coordination_score:.6f}")
        print(f"  Coordination test passed: {self.test_results['coordination_test']['passed']}")
        
        return self.test_results["coordination_test"]["passed"]
    
    def test_frequencies(self, cerebellum):
        """Test phi-harmonic frequencies"""
        print("\nTesting phi-harmonic frequencies...")
        
        # Get phi-harmonic frequencies from cerebellum
        phi_harmonic_frequencies = cerebellum.get_phi_harmonic_frequencies()
        purkinje_frequencies = cerebellum.get_purkinje_frequencies()
        granule_frequencies = cerebellum.get_granule_frequencies()
        
        # Check if we have the expected number of frequencies
        expected_phi_count = 7  # φ¹ through φ⁷
        expected_purkinje_count = 4  # 1x through 4x
        expected_granule_count = 4  # φ¹ through φ⁴
        
        phi_count_match = len(phi_harmonic_frequencies) / expected_phi_count
        purkinje_count_match = len(purkinje_frequencies) / expected_purkinje_count
        granule_count_match = len(granule_frequencies) / expected_granule_count
        
        # Check if frequencies follow phi-harmonic patterns
        phi_pattern_quality = 0
        for i in range(1, min(len(phi_harmonic_frequencies), expected_phi_count)):
            expected_ratio = PHI
            actual_ratio = phi_harmonic_frequencies[i]["frequency"] / phi_harmonic_frequencies[i-1]["frequency"]
            ratio_accuracy = 1 - abs(actual_ratio - expected_ratio) / expected_ratio
            phi_pattern_quality += ratio_accuracy
        
        if len(phi_harmonic_frequencies) > 1:
            phi_pattern_quality /= (len(phi_harmonic_frequencies) - 1)
        
        # Calculate frequency score (1.0 = perfect)
        frequency_score = (phi_count_match + purkinje_count_match + granule_count_match + phi_pattern_quality) / 4
        
        # Store test metrics
        self.test_results["frequency_test"]["metrics"] = {
            "phi_harmonic_count": len(phi_harmonic_frequencies),
            "expected_phi_count": expected_phi_count,
            "phi_count_match": phi_count_match,
            "purkinje_count": len(purkinje_frequencies),
            "expected_purkinje_count": expected_purkinje_count,
            "purkinje_count_match": purkinje_count_match,
            "granule_count": len(granule_frequencies),
            "expected_granule_count": expected_granule_count,
            "granule_count_match": granule_count_match,
            "phi_pattern_quality": phi_pattern_quality
        }
        
        # Set test score and passed status
        self.test_results["frequency_test"]["score"] = frequency_score
        self.test_results["frequency_test"]["passed"] = frequency_score > 0.9
        
        # Print results
        print(f"  Phi-harmonic frequencies: {len(phi_harmonic_frequencies)} (expected: {expected_phi_count})")
        print(f"  Phi count match: {phi_count_match:.6f}")
        print(f"  Purkinje frequencies: {len(purkinje_frequencies)} (expected: {expected_purkinje_count})")
        print(f"  Purkinje count match: {purkinje_count_match:.6f}")
        print(f"  Granule frequencies: {len(granule_frequencies)} (expected: {expected_granule_count})")
        print(f"  Granule count match: {granule_count_match:.6f}")
        print(f"  Phi pattern quality: {phi_pattern_quality:.6f}")
        print(f"  Frequency test score: {frequency_score:.6f}")
        print(f"  Frequency test passed: {self.test_results['frequency_test']['passed']}")
        
        # Create frequency plots
        plt.figure(figsize=(12, 8))
        
        # Plot phi-harmonic frequencies
        plt.subplot(3, 1, 1)
        freqs = [f["frequency"] for f in phi_harmonic_frequencies]
        periods = [f["period"] for f in phi_harmonic_frequencies]
        labels = [f"φ^{i+1}" for i in range(len(freqs))]
        plt.bar(labels, freqs)
        plt.title('Phi-Harmonic Frequencies')
        plt.ylabel('Frequency (Hz)')
        plt.grid(True)
        
        # Plot Purkinje frequencies
        plt.subplot(3, 1, 2)
        freqs = [f["frequency"] for f in purkinje_frequencies]
        labels = [f"{i+1}x" for i in range(len(freqs))]
        plt.bar(labels, freqs)
        plt.title('Purkinje Cell Firing Frequencies')
        plt.ylabel('Frequency (Hz)')
        plt.grid(True)
        
        # Plot Granule frequencies
        plt.subplot(3, 1, 3)
        freqs = [f["frequency"] for f in granule_frequencies]
        labels = [f"φ^{i+1}" for i in range(len(freqs))]
        plt.bar(labels, freqs)
        plt.title('Granule Cell Firing Frequencies')
        plt.xlabel('Harmonic')
        plt.ylabel('Frequency (Hz)')
        plt.grid(True)
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'frequency_analysis.png'))
        plt.close()
        
        return self.test_results["frequency_test"]["passed"]
    
    def run_all_tests(self, cerebellum):
        """Run all tests and compute overall results"""
        print("\nRunning all Quantum Cerebellum tests...")
        print("=" * 70)
        
        # Run individual tests
        resonance_passed = self.test_resonance(cerebellum)
        learning_passed = self.test_learning(cerebellum)
        coordination_passed = self.test_coordination(cerebellum)
        frequency_passed = self.test_frequencies(cerebellum)
        
        # Calculate overall score
        overall_score = (
            self.test_results["resonance_test"]["score"] +
            self.test_results["learning_test"]["score"] +
            self.test_results["coordination_test"]["score"] +
            self.test_results["frequency_test"]["score"]
        ) / 4
        
        # Set overall passed status
        tests_passed = sum([
            int(self.test_results["resonance_test"]["passed"]),
            int(self.test_results["learning_test"]["passed"]),
            int(self.test_results["coordination_test"]["passed"]),
            int(self.test_results["frequency_test"]["passed"])
        ])
        overall_passed = tests_passed >= 3  # Pass if at least 3 out of 4 tests pass
        
        # Store overall results
        self.test_results["overall"]["score"] = overall_score
        self.test_results["overall"]["passed"] = overall_passed
        self.test_results["overall"]["metrics"] = {
            "tests_passed": tests_passed,
            "total_tests": 4,
            "cerebellum_fingerprint": cerebellum.cerebellum_state["cerebellum_quantum_fingerprint"],
            "timestamp": time.time()
        }
        
        print("\n" + "=" * 70)
        print(f"QUANTUM CEREBELLUM TEST RESULTS SUMMARY")
        print("=" * 70)
        print(f"Resonance Test:    {'✓' if resonance_passed else '✗'}  Score: {self.test_results['resonance_test']['score']:.6f}")
        print(f"Learning Test:     {'✓' if learning_passed else '✗'}  Score: {self.test_results['learning_test']['score']:.6f}")
        print(f"Coordination Test: {'✓' if coordination_passed else '✗'}  Score: {self.test_results['coordination_test']['score']:.6f}")
        print(f"Frequency Test:    {'✓' if frequency_passed else '✗'}  Score: {self.test_results['frequency_test']['score']:.6f}")
        print("-" * 70)
        print(f"Overall Result:    {'✓ PASSED' if overall_passed else '✗ FAILED'}  Score: {overall_score:.6f}")
        print(f"Tests Passed: {tests_passed}/4")
        print("=" * 70)
        
        # Save results to JSON file - use the make_json_serializable function
        with open(os.path.join(self.output_dir, 'test_results.json'), 'w') as f:
            serializable_results = make_json_serializable(self.test_results)
            json.dump(serializable_results, f, indent=2)
        
        print(f"\nTest results saved to: {os.path.join(self.output_dir, 'test_results.json')}")
        print(f"Plots saved to: {self.output_dir}")
        
        return overall_passed

def main():
    """Main function to run the tests"""
    print("=" * 70)
    print("PHI-HARMONIC QUANTUM CEREBELLUM TEST SUITE")
    print("=" * 70)
    print("Testing the quantum cerebellum component for phi-harmonic properties,")
    print("coordination functions, and learning capabilities.")
    print("-" * 70)
    
    try:
        # Initialize the cerebellum test extension
        print("Initializing Phi-Harmonic Quantum Cerebellum Test Extension...")
        cerebellum = PhiHarmonicCerebellumTestExtension()
        
        # Create the test harness
        tester = QuantumCerebellumTester()
        
        # Run all tests
        result = tester.run_all_tests(cerebellum)
        
        if result:
            print("\n✅ Cerebellum tests PASSED. The component meets phi-harmonic specifications.")
        else:
            print("\n❌ Cerebellum tests FAILED. The component does not meet all specifications.")
        
    except Exception as e:
        print(f"\n❌ Error testing cerebellum: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return result

if __name__ == "__main__":
    main()
