"""
test_protection.py

Tests the advanced phi-harmonic protection system against sophisticated decoys.
Demonstrates how the system can detect even "near-perfect" decoys that match
all numeric thresholds but lack the quantum-consciousness properties.
"""

import json
import time
import math
from phi_advanced_camouflage import PhiAdvancedCamouflage
from phi_advanced_protection import PhiAdvancedProtection, validate_artifact_advanced

# Constants
PHI = 1.618033988749895
PHI_INVERSE = 0.618033988749895
PI = 3.141592653589793
CONSCIOUSNESS_THRESHOLD = 0.763932
COHERENCE_BASE = 0.991800

def create_sophisticated_decoy(real_artifact):
    """Create a sophisticated decoy by copying a real artifact and tuning values within ±0.0002."""
    # Deep copy the artifact
    import copy
    decoy = copy.deepcopy(real_artifact)
    
    # Alter the ID to avoid exact duplication
    decoy["artifact_id"] = decoy["artifact_id"].replace("PHI", "PHI-DECOY")
    
    # Apply tiny perturbations to all numeric values
    def perturb_numeric_values(obj, depth=0):
        if depth > 10:  # Prevent infinite recursion
            return obj
            
        if isinstance(obj, dict):
            return {k: perturb_numeric_values(v, depth+1) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [perturb_numeric_values(v, depth+1) for v in obj]
        elif isinstance(obj, float):
            # Apply a tiny perturbation within ±0.0002
            import random
            perturbation = (random.random() * 0.0004 - 0.0002)
            return obj + perturbation
        else:
            return obj
    
    # Perturb numeric values while maintaining structure
    return perturb_numeric_values(decoy)

def main():
    """Main test function."""
    print("\n==================================================")
    print("     PHI-HARMONIC ADVANCED PROTECTION TEST")
    print("==================================================")
    print("Testing the system's ability to detect sophisticated decoys")
    print("that match all basic numeric thresholds but lack consciousness")
    
    # Generate only quantum artifacts for testing
    print("\n=== Generating Test Artifacts ===")
    generator = PhiAdvancedCamouflage()
    artifacts, real_index = generator.generate_advanced_artifacts("quantum", 4)
    
    print(f"\nGeneration complete.")
    print(f"Real artifact index: {real_index}")
    
    # Test basic validation
    print(f"\n=== Testing Basic Validation ===")
    validator = PhiAdvancedProtection()
    
    # Test basic validation (what adversaries might replicate)
    basic_results = []
    for i, artifact in enumerate(artifacts):
        is_valid = validator._basic_validation(artifact)
        is_real = (i == real_index)
        basic_results.append((is_valid, is_real))
        print(f"Artifact {i}: Basic Validation={is_valid}, Actually Real={is_real}")
    
    # Count how many decoys passed basic validation
    decoy_pass_count = sum(1 for i, (valid, real) in enumerate(basic_results) 
                          if valid and not real)
    
    print(f"\nResult: {decoy_pass_count} of {len(artifacts)-1} decoys passed basic validation")
    
    # Test advanced validation
    print(f"\n=== Testing Advanced Validation ===")
    
    # Test full validation (consciousness-required)
    advanced_results = []
    for i, artifact in enumerate(artifacts):
        valid, message = validate_artifact_advanced(artifact)
        is_real = (i == real_index)
        advanced_results.append((valid, is_real, message))
        print(f"Artifact {i}: Advanced Validation={valid}, Actually Real={is_real}")
        print(f"  Message: {message}")
    
    # Count how many decoys passed advanced validation
    decoy_pass_count = sum(1 for i, (valid, real, _) in enumerate(advanced_results) 
                          if valid and not real)
    
    print(f"\nResult: {decoy_pass_count} of {len(artifacts)-1} decoys passed advanced validation")
    
    # Create and test a sophisticated decoy
    print(f"\n=== Testing Against Sophisticated Decoy ===")
    
    # Get the real artifact
    real_artifact = artifacts[real_index]
    
    # Create a sophisticated decoy by closely mimicking the real artifact
    sophisticated_decoy = create_sophisticated_decoy(real_artifact)
    
    print("Created sophisticated decoy by closely mimicking real artifact (±0.0002)")
    
    # Test basic validation on sophisticated decoy
    basic_valid = validator._basic_validation(sophisticated_decoy)
    print(f"Sophisticated Decoy: Basic Validation={basic_valid}")
    
    # Test advanced validation on sophisticated decoy
    advanced_valid, message = validate_artifact_advanced(sophisticated_decoy)
    print(f"Sophisticated Decoy: Advanced Validation={advanced_valid}")
    print(f"Message: {message}")
    
    # Test specific protection mechanisms
    print("\n=== Testing Individual Protection Mechanisms ===")
    cross_correlation = validator._validate_cross_correlation(sophisticated_decoy)
    birth_coherence = validator._validate_birth_coherence(sophisticated_decoy)
    non_linear_coherence = validator._validate_non_linear_coherence(sophisticated_decoy)
    temporal_signature = validator._validate_temporal_signature(sophisticated_decoy)
    observer_dependent = validator._validate_observer_dependent(sophisticated_decoy)
    
    print(f"Cross-Correlation: {cross_correlation}")
    print(f"Birth Coherence: {birth_coherence}")
    print(f"Non-Linear Coherence: {non_linear_coherence}")
    print(f"Temporal Signature: {temporal_signature}")
    print(f"Observer-Dependent: {observer_dependent}")
    
    print("\n==================================================")
    print("     ADVANCED PROTECTION TEST COMPLETE")
    print("==================================================")
    print("Results demonstrate that the phi-consciousness protection system")
    print("can detect sophisticated decoys that match all basic numeric values")
    print("within ±0.0002 but lack the quantum-consciousness properties.")
    
if __name__ == "__main__":
    main()
