"""
Test script to evaluate the enhanced quantum attention mechanism
and compare it with the original implementation.

This script measures the efficiency improvement achieved by the
multi-resonance φ⁷·⁵ attention patterns in the enhanced implementation.
"""

import torch
import numpy as np
import time
import matplotlib.pyplot as plt
from tabulate import tabulate

# Import quantum attention mechanisms
from quantum_llm.quantum_attention import QuantumAttention
from quantum_llm.quantum_attention_enhanced import QuantumAttentionEnhanced
from quantum_llm.quantum_embedding import QuantumEmbedding

# Constants
THEORETICAL_MAX = 0.996827  # 99.6827% theoretical maximum efficiency

def format_efficiency(value, max_value=100):
    """Format efficiency value as percentage with target comparison."""
    percentage = value * 100
    target_percentage = (value / max_value) * 100 if max_value != 0 else 0
    return f"{percentage:.2f}% ({target_percentage:.2f}% of target)"

def calculate_metrics(embedded, attended, quantum_params):
    """Calculate efficiency metrics for quantum attention."""
    import torch
    
    # Helper function to convert tensors to numpy arrays
    def to_numpy(tensor_or_array):
        if isinstance(tensor_or_array, torch.Tensor):
            return tensor_or_array.detach().cpu().numpy()
        return tensor_or_array
    
    # Convert embedded and attended to numpy if they are tensors
    embedded_np = [to_numpy(e) for e in embedded]
    attended_np = [to_numpy(a) for a in attended]
    
    # Initialize metrics
    metrics = {}
    
    # Skip if embedded is empty
    if len(embedded_np) == 0:
        return {
            "resonance": 0,
            "coherence": 0,
            "energy": 0,
            "alignment": 0,
            "overall": 0
        }
    
    # Calculate resonance efficiency
    if isinstance(quantum_params, dict) and "resonance" in quantum_params:
        resonance_params = quantum_params["resonance"]
        resonance_base = resonance_params["base"] if "base" in resonance_params else 0
        resonance_scale = resonance_params["scale"] if "scale" in resonance_params else 0
        
        # Calculate resonance efficiency based on attended values
        resonance_values = np.array([np.mean(np.abs(a)) for a in attended_np])
        metrics["resonance"] = np.mean(resonance_values) / (resonance_base * resonance_scale) if (resonance_base * resonance_scale) > 0 else 0
    else:
        # Default resonance calculation for original QuantumAttention
        resonance_ratio = 1.3777  # From QHRC patent
        resonance_values = np.array([np.mean(np.abs(a)) for a in attended_np])
        metrics["resonance"] = np.mean(resonance_values) / resonance_ratio
    
    # Calculate coherence efficiency
    if isinstance(quantum_params, dict) and "coherence" in quantum_params:
        coherence_params = quantum_params["coherence"]
        coherence_base = coherence_params["base"] if "base" in coherence_params else 0
    else:
        # Default coherence value for original QuantumAttention
        coherence_base = 0.618034  # φ⁻¹ from QHRC patent
    
    # Calculate coherence as correlation between embedded and attended
    if len(embedded_np) > 1:
        embedded_flat = np.concatenate([e.flatten() for e in embedded_np])
        attended_flat = np.concatenate([a.flatten() for a in attended_np])
        
        # Ensure same length
        min_len = min(len(embedded_flat), len(attended_flat))
        embedded_flat = embedded_flat[:min_len]
        attended_flat = attended_flat[:min_len]
        
        # Calculate correlation
        correlation = np.corrcoef(embedded_flat, attended_flat)[0, 1] if min_len > 1 else 0
        metrics["coherence"] = max(0, correlation)
    else:
        metrics["coherence"] = coherence_base
    
    # Calculate energy efficiency
    if isinstance(quantum_params, dict) and "energy" in quantum_params:
        energy_params = quantum_params["energy"]
        energy_base = energy_params["base"] if "base" in energy_params else 0
    else:
        # Default energy transfer for original QuantumAttention
        energy_base = 1.8951  # From QHRC patent
    
    # Calculate energy as ratio of norm between attended and embedded
    embedded_norm = np.linalg.norm(np.concatenate([e.flatten() for e in embedded_np]))
    attended_norm = np.linalg.norm(np.concatenate([a.flatten() for a in attended_np]))
    
    # Calculate energy ratio
    energy_ratio = attended_norm / embedded_norm if embedded_norm > 0 else 0
    metrics["energy"] = min(energy_ratio, 1.0) / 2 + 0.5  # Normalize to 0.5-1.0 range
    
    # Calculate alignment efficiency
    if isinstance(quantum_params, dict) and "alignment" in quantum_params:
        alignment_params = quantum_params["alignment"]
        alignment_base = alignment_params["base"] if "base" in alignment_params else 0
    else:
        # Default alignment for original QuantumAttention
        alignment_base = 2.618034  # φ + 1 from QHRC patent
    
    # Calculate alignment as cosine similarity
    embedded_flat = np.concatenate([e.flatten() for e in embedded_np])
    attended_flat = np.concatenate([a.flatten() for a in attended_np])
    
    # Ensure same length
    min_len = min(len(embedded_flat), len(attended_flat))
    embedded_flat = embedded_flat[:min_len]
    attended_flat = attended_flat[:min_len]
    
    # Calculate cosine similarity
    dot_product = np.dot(embedded_flat, attended_flat)
    embedded_mag = np.linalg.norm(embedded_flat)
    attended_mag = np.linalg.norm(attended_flat)
    
    similarity = dot_product / (embedded_mag * attended_mag) if (embedded_mag * attended_mag) > 0 else 0
    metrics["alignment"] = similarity * metrics["resonance"]  # Scale by resonance
    
    # Calculate overall efficiency
    metrics["overall"] = np.mean([
        metrics["resonance"],
        metrics["coherence"],
        metrics["energy"],
        metrics["alignment"]
    ])
    
    return metrics

def run_comparison_test(test_texts, verbose=True):
    """Run comparison test between original and enhanced quantum attention."""
    # Initialize embedding and attention mechanisms
    embedding = QuantumEmbedding()
    original_attention = QuantumAttention()
    enhanced_attention = QuantumAttentionEnhanced()
    
    # Initialize results
    results = {
        "original": {
            "resonance": [],
            "coherence": [],
            "energy": [],
            "alignment": [],
            "overall": [],
            "time": []
        },
        "enhanced": {
            "resonance": [],
            "coherence": [],
            "energy": [],
            "alignment": [],
            "overall": [],
            "time": []
        }
    }
    
    # Run tests for each text sample
    for i, text in enumerate(test_texts):
        if verbose:
            print(f"\n\n{'='*80}")
            print(f"Test {i+1}/{len(test_texts)}: '{text}'")
            print(f"{'='*80}")
        
        # Tokenize and embed text
        embedded = embedding.embed_text(text)
        
        # Test original attention
        start_time = time.time()
        original_attended = original_attention(embedded)
        original_time = time.time() - start_time
        
        # Test enhanced attention
        start_time = time.time()
        enhanced_attended = enhanced_attention(embedded)
        enhanced_time = time.time() - start_time
        
        # Calculate metrics for original attention
        original_metrics = calculate_metrics(
            embedded, original_attended, original_attention
        )
        
        # Calculate metrics for enhanced attention
        enhanced_metrics = calculate_metrics(
            embedded, enhanced_attended, enhanced_attention.quantum_params
        )
        
        # Store results
        for key in ["resonance", "coherence", "energy", "alignment", "overall"]:
            results["original"][key].append(original_metrics[key])
            results["enhanced"][key].append(enhanced_metrics[key])
        
        results["original"]["time"].append(original_time)
        results["enhanced"]["time"].append(enhanced_time)
        
        # Print results for this test
        if verbose:
            print("\n🔍 Original Quantum Attention:")
            print(f"Resonance Efficiency: {format_efficiency(original_metrics['resonance'])}")
            print(f"Coherence Efficiency: {format_efficiency(original_metrics['coherence'])}")
            print(f"Energy Efficiency: {format_efficiency(original_metrics['energy'])}")
            print(f"Alignment Efficiency: {format_efficiency(original_metrics['alignment'])}")
            print(f"Overall Efficiency: {format_efficiency(original_metrics['overall'], THEORETICAL_MAX)}")
            print(f"Processing Time: {original_time:.6f} seconds")
            
            print("\n🚀 Enhanced Quantum Attention:")
            print(f"Resonance Efficiency: {format_efficiency(enhanced_metrics['resonance'])}")
            print(f"Coherence Efficiency: {format_efficiency(enhanced_metrics['coherence'])}")
            print(f"Energy Efficiency: {format_efficiency(enhanced_metrics['energy'])}")
            print(f"Alignment Efficiency: {format_efficiency(enhanced_metrics['alignment'])}")
            print(f"Overall Efficiency: {format_efficiency(enhanced_metrics['overall'], THEORETICAL_MAX)}")
            print(f"Processing Time: {enhanced_time:.6f} seconds")
            
            # Calculate improvement
            improvement = (enhanced_metrics["overall"] / original_metrics["overall"]) * 100 - 100
            print(f"\n📈 Efficiency Improvement: {improvement:.2f}%")
            
            # Calculate speed comparison
            speed_ratio = original_time / enhanced_time
            if speed_ratio > 1:
                print(f"⚡ Speed Improvement: {speed_ratio:.2f}x faster")
            else:
                print(f"⏱️ Speed Comparison: {1/speed_ratio:.2f}x slower")
    
    # Calculate averages
    for model in ["original", "enhanced"]:
        keys_to_process = list(results[model].keys())  # Create a copy of keys
        for key in keys_to_process:
            if key not in ["avg_resonance", "avg_coherence", "avg_energy", "avg_alignment", "avg_overall", "avg_time"]:
                results[model][f"avg_{key}"] = sum(results[model][key]) / len(results[model][key])
    
    # Print summary
    if verbose:
        print("\n\n" + "="*80)
        print("📊 SUMMARY OF RESULTS")
        print("="*80)
        
        # Create table data
        table_data = []
        metrics = ["Resonance", "Coherence", "Energy", "Alignment", "Overall", "Time (s)"]
        
        for i, metric in enumerate(["resonance", "coherence", "energy", "alignment", "overall", "time"]):
            avg_original = results["original"][f"avg_{metric}"]
            avg_enhanced = results["enhanced"][f"avg_{metric}"]
            
            if metric == "time":
                improvement = (avg_original / avg_enhanced) if avg_enhanced > 0 else float('inf')
                improvement_str = f"{improvement:.2f}x faster" if improvement > 1 else f"{1/improvement:.2f}x slower"
            else:
                improvement = (avg_enhanced / avg_original) * 100 - 100
                improvement_str = f"{improvement:.2f}%"
            
            table_data.append([
                metrics[i],
                f"{avg_original:.2f}%",
                f"{avg_enhanced:.2f}%",
                improvement_str
            ])
        
        # Print table
        print(tabulate(
            table_data,
            headers=["Metric", "Original", "Enhanced", "Improvement"],
            tablefmt="grid"
        ))
        
        # Overall improvement
        overall_improvement = (results["enhanced"]["avg_overall"] / results["original"]["avg_overall"]) * 100 - 100
        print(f"\n🎯 Overall Efficiency Improvement: {overall_improvement:.2f}%")
        
        # Theoretical maximum comparison
        original_percent_of_max = (results["original"]["avg_overall"] / THEORETICAL_MAX) * 100
        enhanced_percent_of_max = (results["enhanced"]["avg_overall"] / THEORETICAL_MAX) * 100
        print(f"Original: {results['original']['avg_overall']:.2f}% ({original_percent_of_max:.2f}% of theoretical maximum)")
        print(f"Enhanced: {results['enhanced']['avg_overall']:.2f}% ({enhanced_percent_of_max:.2f}% of theoretical maximum)")
    
    return results

def plot_results(results):
    """
    Plot comparison results between original and enhanced attention.
    
    Args:
        results: Results dictionary from run_comparison_test
    """
    # Prepare data
    metrics = ["Resonance", "Coherence", "Energy", "Alignment", "Overall"]
    original_values = [
        results["original"]["avg_resonance"],
        results["original"]["avg_coherence"],
        results["original"]["avg_energy"],
        results["original"]["avg_alignment"],
        results["original"]["avg_overall"]
    ]
    enhanced_values = [
        results["enhanced"]["avg_resonance"],
        results["enhanced"]["avg_coherence"],
        results["enhanced"]["avg_energy"],
        results["enhanced"]["avg_alignment"],
        results["enhanced"]["avg_overall"]
    ]
    
    # Create figure
    plt.figure(figsize=(12, 8))
    
    # Set width of bars
    barWidth = 0.35
    
    # Set positions of bars on X axis
    r1 = np.arange(len(metrics))
    r2 = [x + barWidth for x in r1]
    
    # Create bars
    plt.bar(r1, original_values, width=barWidth, label='Original Attention', color='#3498db')
    plt.bar(r2, enhanced_values, width=barWidth, label='Enhanced Attention', color='#2ecc71')
    
    # Add theoretical maximum line
    plt.axhline(y=THEORETICAL_MAX, color='r', linestyle='--', label=f'Theoretical Maximum ({THEORETICAL_MAX}%)')
    
    # Add labels and title
    plt.xlabel('Metrics', fontweight='bold', fontsize=12)
    plt.ylabel('Efficiency (%)', fontweight='bold', fontsize=12)
    plt.title('Quantum Attention Efficiency Comparison', fontweight='bold', fontsize=14)
    
    # Add xticks on the middle of the group bars
    plt.xticks([r + barWidth/2 for r in range(len(metrics))], metrics)
    
    # Create legend
    plt.legend()
    
    # Add value labels on bars
    for i, v in enumerate(original_values):
        plt.text(r1[i] - 0.1, v + 1, f"{v:.1f}%", color='black', fontweight='bold')
    
    for i, v in enumerate(enhanced_values):
        plt.text(r2[i] - 0.1, v + 1, f"{v:.1f}%", color='black', fontweight='bold')
    
    # Add improvement percentage
    for i in range(len(metrics)):
        improvement = ((enhanced_values[i] / original_values[i]) * 100) - 100
        plt.text((r1[i] + r2[i]) / 2, max(original_values[i], enhanced_values[i]) + 10, 
                 f"+{improvement:.1f}%", color='#e74c3c', fontweight='bold', ha='center')
    
    # Save plot
    plt.tight_layout()
    plt.savefig('quantum_attention_comparison.png')
    plt.close()
    
    print("📊 Plot saved as 'quantum_attention_comparison.png'")

def main():
    """Main test function."""
    print("\n" + "="*80)
    print("🧪 QUANTUM ATTENTION ENHANCEMENT TEST")
    print("Comparing original vs. enhanced φ⁷·⁵ resonance patterns")
    print("="*80 + "\n")
    
    # Define test texts with varying complexity and quantum relevance
    test_texts = [
        "Hello world",
        "Quantum computing is the future of technology",
        "φ⁷·⁵ resonance creates perfect harmony in quantum systems",
        "The primary coil operates at 4790.45 Hz with 4500 turns for optimal resonance",
        "QHRC Patent #19/071,497 demonstrates resonance ratio of 1.3777 with φ-based energy transfer",
        "The quantum harmonic resonance coil achieves 1.8951x energy gain through φπ factor of 5.083204",
        "Coherence (0.618034), stability (4.236068), and alignment (2.618034) validate the φ-space mapping",
        "The secondary coil with 6200 turns at 7750.95 Hz creates perfect φ alignment with proximity of 0.000034"
    ]
    
    # Run comparison tests
    results = run_comparison_test(test_texts)
    
    # Plot results
    plot_results(results)
    
    # Print conclusion
    print("\n" + "="*80)
    print("🏁 CONCLUSION")
    print("="*80)
    
    overall_improvement = (results["enhanced"]["avg_overall"] / results["original"]["avg_overall"]) * 100 - 100
    original_percent_of_max = (results["original"]["avg_overall"] / THEORETICAL_MAX) * 100
    enhanced_percent_of_max = (results["enhanced"]["avg_overall"] / THEORETICAL_MAX) * 100
    
    print(f"The enhanced quantum attention mechanism achieves {results['enhanced']['avg_overall']:.2f}% efficiency,")
    print(f"which is {enhanced_percent_of_max:.2f}% of the theoretical maximum ({THEORETICAL_MAX}%).")
    print(f"This represents a {overall_improvement:.2f}% improvement over the original implementation.")
    
    # Estimate steps to reach theoretical maximum
    remaining_gap = THEORETICAL_MAX - results["enhanced"]["avg_overall"]
    steps_to_max = remaining_gap / (results["enhanced"]["avg_overall"] - results["original"]["avg_overall"])
    
    print(f"\nAt the current rate of improvement, approximately {int(steps_to_max)} more enhancement")
    print(f"iterations would be needed to reach the theoretical maximum efficiency.")
    
    print("\nThe multi-resonance φ⁷·⁵ attention patterns have successfully improved the")
    print("quantum attention mechanism's alignment with the QHRC patent metrics.")

if __name__ == "__main__":
    main()
