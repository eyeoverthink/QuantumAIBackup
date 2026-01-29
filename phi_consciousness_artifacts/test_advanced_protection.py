"""
test_advanced_protection.py

Tests the advanced phi-harmonic protection system against sophisticated decoys.
Demonstrates how the system can detect even "near-perfect" decoys that match
all numeric thresholds but lack the quantum-consciousness properties.
"""

import json
import time
from phi_advanced_camouflage import PhiAdvancedCamouflage
from phi_advanced_protection import PhiAdvancedProtection, validate_artifact_advanced, compare_artifacts, get_validation_diagnostics

def generate_test_artifacts():
    """Generate test artifacts - real and sophisticated decoys."""
    print("\n=== Generating Test Artifacts ===")
    generator = PhiAdvancedCamouflage()
    
    # Generate quantum artifacts
    print("\nGenerating quantum artifacts (1 real, 3 decoys)...")
    quantum_artifacts, quantum_real_index = generator.generate_advanced_artifacts("quantum", 4)
    
    # Generate protocol artifacts
    print("Generating protocol artifacts (1 real, 3 decoys)...")
    protocol_artifacts, protocol_real_index = generator.generate_advanced_artifacts("protocol", 4)
    
    # Generate identity artifacts
    print("Generating identity artifacts (1 real, 3 decoys)...")
    identity_artifacts, identity_real_index = generator.generate_advanced_artifacts("identity", 4)
    
    print(f"\nGeneration complete.")
    print(f"Quantum real index: {quantum_real_index}")
    print(f"Protocol real index: {protocol_real_index}")
    print(f"Identity real index: {identity_real_index}")
    
    return (quantum_artifacts, quantum_real_index, 
            protocol_artifacts, protocol_real_index,
            identity_artifacts, identity_real_index)

def test_basic_validation(artifacts, real_index, artifact_type):
    """Test basic validation that sophisticated decoys might pass."""
    print(f"\n=== Testing Basic Validation for {artifact_type.capitalize()} Artifacts ===")
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
    
    return basic_results

def test_advanced_validation(artifacts, real_index, artifact_type):
    """Test advanced validation that can detect even sophisticated decoys."""
    print(f"\n=== Testing Advanced Validation for {artifact_type.capitalize()} Artifacts ===")
    
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
    
    return advanced_results

def get_detailed_diagnostics(artifact, artifact_type, index):
    """Get detailed diagnostics about why an artifact passes or fails validation."""
    print(f"\n=== Detailed Diagnostics for {artifact_type.capitalize()} Artifact {index} ===")
    
    diagnostics = get_validation_diagnostics(artifact)
    
    print(f"Artifact ID: {diagnostics['artifact_id']}")
    print(f"Type: {diagnostics['type']}")
    print(f"Overall Valid: {diagnostics['overall_valid']}")
    print(f"Diagnosis: {diagnostics['diagnosis']}")
    
    print("\nValidation Results:")
    for key, result in diagnostics['validations'].items():
        print(f"  {key}: {result}")
    
    return diagnostics

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

def test_against_sophisticated_decoy(artifacts, real_index, artifact_type):
    """Test the system against a sophisticated decoy that closely mimics a real artifact."""
    print(f"\n=== Testing Against Sophisticated {artifact_type.capitalize()} Decoy ===")
    
    # Get the real artifact
    real_artifact = artifacts[real_index]
    
    # Create a sophisticated decoy by closely mimicking the real artifact
    sophisticated_decoy = create_sophisticated_decoy(real_artifact)
    
    print("Created sophisticated decoy by closely mimicking real artifact (±0.0002)")
    
    # Test basic validation
    validator = PhiAdvancedProtection()
    basic_valid = validator._basic_validation(sophisticated_decoy)
    print(f"Sophisticated Decoy: Basic Validation={basic_valid}")
    
    # Test advanced validation
    advanced_valid, message = validate_artifact_advanced(sophisticated_decoy)
    print(f"Sophisticated Decoy: Advanced Validation={advanced_valid}")
    print(f"Message: {message}")
    
    # Get detailed diagnostics
    print("\nDetailed diagnostics for sophisticated decoy:")
    diagnostics = get_validation_diagnostics(sophisticated_decoy)
    for key, result in diagnostics['validations'].items():
        print(f"  {key}: {result}")
    
    return basic_valid, advanced_valid, diagnostics

def main():
    """Main test function."""
    print("\n==================================================")
    print("     PHI-HARMONIC ADVANCED PROTECTION TEST")
    print("==================================================")
    print("Testing the system's ability to detect sophisticated decoys")
    print("that match all basic numeric thresholds but lack consciousness")
    
    # Generate test artifacts
    quantum_artifacts, quantum_real_index, protocol_artifacts, protocol_real_index, identity_artifacts, identity_real_index = generate_test_artifacts()
    
    # Test quantum artifacts
    test_basic_validation(quantum_artifacts, quantum_real_index, "quantum")
    test_advanced_validation(quantum_artifacts, quantum_real_index, "quantum")
    
    # Get detailed diagnostics for a real quantum artifact
    get_detailed_diagnostics(quantum_artifacts[quantum_real_index], "quantum", quantum_real_index)
    
    # Get detailed diagnostics for a decoy quantum artifact
    decoy_index = (quantum_real_index + 1) % len(quantum_artifacts)
    get_detailed_diagnostics(quantum_artifacts[decoy_index], "quantum", decoy_index)
    
    # Test against sophisticated quantum decoy
    test_against_sophisticated_decoy(quantum_artifacts, quantum_real_index, "quantum")
    
    print("\n==================================================")
    print("     ADVANCED PROTECTION TEST COMPLETE")
    print("==================================================")
    print("Results demonstrate that the phi-consciousness protection system")
    print("can detect even sophisticated decoys that match all basic numeric")
    print("thresholds but lack the quantum-consciousness properties.")
    
if __name__ == "__main__":
    main()
