"""
Test quantum protein analysis with full brain architecture monitoring
"""
from quantum_protein_mapper import QuantumProteinMapper
from quantum_brain import QuantumBrain
from quantum_cortex import QuantumCortex
from quantum_synapse import QuantumSynapse
from quantum_hemisphere import LeftHemisphere, RightHemisphere
from quantum_learn_core import QuantumLearning
import time
import numpy as np

def monitor_quantum_metrics(brain_component, operation):
    """Monitor quantum metrics for brain components"""
    start_time = time.time()
    metrics = {
        'start_resonance': brain_component.get_resonance(),
        'start_coherence': brain_component.get_coherence(),
        'start_phi_alignment': brain_component.get_phi_alignment()
    }
    
    result = operation()
    
    metrics.update({
        'end_resonance': brain_component.get_resonance(),
        'end_coherence': brain_component.get_coherence(),
        'end_phi_alignment': brain_component.get_phi_alignment(),
        'processing_time': time.time() - start_time
    })
    
    return result, metrics

def test_protein():
    """Test protein analysis with full brain monitoring"""
    print("🧬 Testing Quantum Protein Analysis")
    print("=" * 40)
    
    # Initialize components
    mapper = QuantumProteinMapper()
    brain = mapper.brain
    left_hem = mapper.left_hemisphere
    right_hem = mapper.right_hemisphere
    
    # Test sequence (part of human hemoglobin beta chain)
    seq = "VHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH"
    
    print(f"Sequence length: {len(seq)}\n")
    
    # Monitor brain state
    print("📊 Initial Brain State")
    print("-" * 20)
    print(f"Brain Coherence: {brain.get_coherence():.4f}")
    print(f"Left Hemisphere φ: {left_hem.get_phi_alignment():.4f}")
    print(f"Right Hemisphere φ: {right_hem.get_phi_alignment():.4f}\n")
    
    # Run analysis with monitoring
    print("🔬 Running Analysis")
    print("-" * 20)
    start_time = time.time()
    
    # Monitor hemispheres
    left_result, left_metrics = monitor_quantum_metrics(
        left_hem,
        lambda: left_hem.process_sequence(
            seq[:len(seq)//2],
            mapper.structure_cortex,
            mapper.aa_resonance
        )
    )
    
    right_result, right_metrics = monitor_quantum_metrics(
        right_hem,
        lambda: right_hem.process_sequence(
            seq[len(seq)//2:],
            mapper.structure_cortex,
            mapper.aa_resonance
        )
    )
    
    # Monitor cortexes
    structure_result, struct_metrics = monitor_quantum_metrics(
        mapper.structure_cortex,
        lambda: mapper.structure_cortex.analyze_pattern(
            left_result['resonance_pattern'] + right_result['resonance_pattern']
        )
    )
    
    # Combine and analyze
    analysis = mapper.analyze_sequence(seq)
    total_time = time.time() - start_time
    
    # Print results
    print(f"\n⚡ Performance Metrics")
    print("-" * 20)
    print(f"Total Processing Time: {total_time:.4f}s")
    print(f"Left Hemisphere: {left_metrics['processing_time']:.4f}s")
    print(f"Right Hemisphere: {right_metrics['processing_time']:.4f}s")
    print(f"Structure Analysis: {struct_metrics['processing_time']:.4f}s\n")
    
    print("🧠 Brain Activity")
    print("-" * 20)
    print(f"Left Coherence Δ: {left_metrics['end_coherence'] - left_metrics['start_coherence']:.4f}")
    print(f"Right Coherence Δ: {right_metrics['end_coherence'] - right_metrics['start_coherence']:.4f}")
    print(f"Structure φ-Alignment: {struct_metrics['end_phi_alignment']:.4f}\n")
    
    print("📊 Analysis Results")
    print("-" * 20)
    print(f"Quantum Bridges: {len(analysis['quantum_bridges'])}")
    print(f"Phi Alignment: {analysis['phi_alignment']:.4f}\n")
    
    print("🎯 Structure Prediction")
    print("-" * 20)
    prediction = mapper.predict_structure(seq)
    print(f"Confidence: {prediction['confidence']:.4f}")
    print(f"Stability: {prediction['stability_score']:.4f}")
    print(f"Quantum Coherence: {prediction['quantum_metrics']['coherence']:.4f}\n")
    
    # Test scaling
    print("⚡ Performance Scaling Test")
    print("=" * 40)
    
    for size in [100, 1000, 10000, 100000]:
        print(f"\nTesting size: {size}")
        test_seq = seq * (size // len(seq) + 1)
        test_seq = test_seq[:size]
        
        start = time.time()
        result = mapper.analyze_sequence(test_seq)
        duration = time.time() - start
        
        print(f"Time: {duration:.2f}s")
        print(f"Bridges found: {len(result['quantum_bridges'])}")
        print(f"Phi alignment: {result['phi_alignment']:.4f}")
        print(f"Brain coherence: {brain.get_coherence():.4f}")

if __name__ == "__main__":
    test_protein()
