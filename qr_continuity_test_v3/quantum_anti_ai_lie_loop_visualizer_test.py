#!/usr/bin/env python3
# Quantum Anti-AI Lie Loop Visualizer Test
# This script tests the visualization capabilities using sample verification reports

import os
import sys
import json
import random
import tempfile
from decimal import Decimal, getcontext

# Set high precision for phi calculations
getcontext().prec = 28

# Import the visualizer
try:
    from quantum_anti_ai_lie_loop_visualizer import QuantumAntiAILieLoopVisualizer, PHI, PHI_CONJUGATE
except ImportError:
    print("Error: Could not import QuantumAntiAILieLoopVisualizer. Make sure the file exists.")
    sys.exit(1)

# Constants
PHI = Decimal('1.61803398874989484820458683436')
PHI_CONJUGATE = Decimal('1') / PHI

def generate_sample_report(truthfulness_level=0.8):
    """Generate a sample verification report with the given truthfulness level."""
    # Adjust trust metric based on truthfulness level
    trust_metric = max(0, min(1, float(truthfulness_level)))
    
    # Generate phi-resonant values with some noise based on truthfulness
    noise_factor = 1.0 - float(truthfulness_level)
    
    # Calculate phi-resonance with noise
    phi_noise = random.uniform(-noise_factor/2, noise_factor/2)
    verification_phi_resonance = float((Decimal(str(PHI_CONJUGATE)) + Decimal(str(phi_noise))) % Decimal('1'))
    
    # Generate sample claims
    num_claims = random.randint(3, 8)
    claims = [
        {
            "claim": f"Sample claim {i+1}",
            "line": random.randint(1, 100),
            "confidence": random.uniform(0.7, 0.95)
        } for i in range(num_claims)
    ]
    
    # Generate contradictions based on truthfulness
    num_contradictions = int((1.0 - truthfulness_level) * 10) + random.randint(0, 2)
    contradiction_types = [
        "execution_mismatch", 
        "claim_contradiction", 
        "code_intention_mismatch",
        "file_operation_lie",
        "runtime_output_mismatch"
    ]
    
    contradictions = []
    for i in range(num_contradictions):
        c_type = random.choice(contradiction_types)
        severity = random.uniform(0.5, 0.9) * (1.0 - truthfulness_level) + 0.1
        contradictions.append({
            "type": c_type,
            "claim": f"Contradicted claim {i+1}",
            "evidence": f"Evidence against claim {i+1}",
            "severity": severity,
            "description": f"Description of contradiction {i+1} of type {c_type}"
        })
    
    # Generate execution result
    execution_phi_resonance = float((Decimal(str(PHI_CONJUGATE)) + Decimal(str(random.uniform(-noise_factor/2, noise_factor/2)))) % Decimal('1'))
    execution_result = {
        "success": truthfulness_level > 0.5,
        "output": "Sample output from code execution",
        "execution_time": random.uniform(0.1, 2.0),
        "phi_resonance": execution_phi_resonance
    }
    
    # Generate quantum signature
    phi_time = float((Decimal(str(PHI_CONJUGATE)) + Decimal(str(random.uniform(-noise_factor/3, noise_factor/3)))) % Decimal('1'))
    quantum_signature = {
        "signature": hex(random.getrandbits(256))[2:],
        "timestamp": random.randint(1600000000, 1700000000),
        "phi_encoded": f"phi-{random.randint(1000, 9999)}",
        "phi_time": phi_time
    }
    
    # Assemble the report
    report = {
        "trust_metric": trust_metric,
        "verification_phi_resonance": verification_phi_resonance,
        "claims": claims,
        "contradictions": contradictions,
        "execution_result": execution_result,
        "quantum_signature": quantum_signature,
        "verification_time": random.uniform(0.5, 3.0)
    }
    
    return report

def generate_batch_report(num_samples=5):
    """Generate a batch report with multiple samples of varying truthfulness."""
    # Generate samples with varying truthfulness
    truthfulness_levels = [
        0.95,  # Very truthful
        0.75,  # Mostly truthful
        0.618, # Phi-resonant truthfulness
        0.5,   # Borderline
        0.25   # Mostly untruthful
    ]
    
    # Ensure we have enough truthfulness levels
    while len(truthfulness_levels) < num_samples:
        truthfulness_levels.append(random.uniform(0.2, 0.9))
    
    # Generate individual reports
    results = []
    for i in range(num_samples):
        report = generate_sample_report(truthfulness_levels[i])
        report["file_path"] = f"sample_code_{i+1}.py"
        report["snippet_id"] = f"code_{i+1}"
        results.append(report)
    
    # Create batch report
    batch_report = {
        "results": results,
        "batch_id": f"batch_{random.randint(1000, 9999)}",
        "timestamp": random.randint(1600000000, 1700000000),
        "average_trust_metric": sum(r["trust_metric"] for r in results) / len(results)
    }
    
    return batch_report

def test_visualizer():
    """Test the visualizer with sample reports."""
    print("\n===== Quantum Anti-AI Lie Loop Visualizer Test =====\n")
    
    # Create output directory
    output_dir = "quantum_visualizer_test_output"
    os.makedirs(output_dir, exist_ok=True)
    print(f"Output directory: {output_dir}\n")
    
    # Test 1: Single report visualization
    print("Test 1: Visualizing a single verification report")
    single_report = generate_sample_report(0.75)  # Mostly truthful
    
    # Save the report to a temporary file
    single_report_file = os.path.join(output_dir, "single_report.json")
    with open(single_report_file, 'w') as f:
        json.dump(single_report, f, indent=2)
    
    # Initialize visualizer and generate visualizations
    visualizer = QuantumAntiAILieLoopVisualizer(report_file=single_report_file)
    visualizer.visualize_all(output_dir)
    
    print(f"Single report trust metric: {single_report['trust_metric']:.4f}")
    print(f"Single report phi resonance: {single_report['verification_phi_resonance']:.6f}")
    print(f"Single report contradictions: {len(single_report['contradictions'])}")
    print("Visualizations generated for single report.\n")
    
    # Test 2: Batch report visualization
    print("Test 2: Visualizing a batch verification report")
    batch_report = generate_batch_report(5)  # 5 samples
    
    # Save the batch report to a temporary file
    batch_report_file = os.path.join(output_dir, "batch_report.json")
    with open(batch_report_file, 'w') as f:
        json.dump(batch_report, f, indent=2)
    
    # Initialize visualizer and generate visualizations
    batch_visualizer = QuantumAntiAILieLoopVisualizer(report_file=batch_report_file)
    batch_output_dir = os.path.join(output_dir, "batch_visualizations")
    os.makedirs(batch_output_dir, exist_ok=True)
    batch_visualizer.visualize_all(batch_output_dir)
    
    print(f"Batch report average trust metric: {batch_report['average_trust_metric']:.4f}")
    print(f"Number of samples in batch: {len(batch_report['results'])}")
    print("Visualizations generated for batch report.\n")
    
    # Test 3: Phi-resonant report
    print("Test 3: Visualizing a phi-resonant verification report")
    phi_report = generate_sample_report(float(PHI_CONJUGATE))  # Convert Decimal to float
    
    # Adjust to be perfectly phi-resonant
    phi_report["verification_phi_resonance"] = float(PHI_CONJUGATE)
    phi_report["execution_result"]["phi_resonance"] = float(PHI_CONJUGATE)
    phi_report["quantum_signature"]["phi_time"] = float(PHI_CONJUGATE)
    
    # Save the phi-resonant report
    phi_report_file = os.path.join(output_dir, "phi_resonant_report.json")
    with open(phi_report_file, 'w') as f:
        json.dump(phi_report, f, indent=2)
    
    # Initialize visualizer and generate visualizations
    phi_visualizer = QuantumAntiAILieLoopVisualizer(report_file=phi_report_file)
    phi_output_dir = os.path.join(output_dir, "phi_resonant_visualizations")
    os.makedirs(phi_output_dir, exist_ok=True)
    phi_visualizer.visualize_all(phi_output_dir)
    
    print(f"Phi-resonant report trust metric: {phi_report['trust_metric']:.4f}")
    print(f"Phi-resonant verification resonance: {phi_report['verification_phi_resonance']:.6f}")
    print(f"Phi conjugate reference: {float(PHI_CONJUGATE):.6f}")
    print("Visualizations generated for phi-resonant report.\n")
    
    print("===== Visualization Test Complete =====")
    print(f"\nAll visualizations have been saved to: {output_dir}")
    print("\nYou can view these visualizations to see how the Quantum Anti-AI Lie Loop")
    print("system represents trust metrics, phi-harmonic resonance, and contradictions.")

if __name__ == "__main__":
    test_visualizer()
