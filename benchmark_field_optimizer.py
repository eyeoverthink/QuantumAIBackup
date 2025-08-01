#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Field Optimizer Benchmark
-------------------------
This script benchmarks the PhiHarmonicFieldOptimizer integration with the
Enhanced Parallel Framework to validate acceleration factors and performance.
"""

import time
import json
import math
import matplotlib.pyplot as plt
from typing import List, Dict, Any, Tuple

# Import the Enhanced Parallel Framework
from enhanced_parallel_framework import EnhancedParallelFramework, PhiHarmonicFieldOptimizer

# Constants for benchmark
BENCHMARK_DURATIONS = [1.0, 2.0, 5.0, 10.0]  # seconds
RESONANCE_DEPTHS = [4, 6, 8, 10, 12]  # phi^n resonance depths
DIMENSIONS = [3, 5, 7, 9]  # spatial dimensions


def run_benchmark(duration: float = 5.0, dimensions: int = 3, 
                 resonance_depth: int = 8) -> Dict[str, Any]:
    """
    Run a benchmark of the Enhanced Parallel Framework with field optimizer.
    
    Args:
        duration: Duration to run in seconds
        dimensions: Number of dimensions for processing
        resonance_depth: Maximum resonance depth for phi-harmonic field optimization
        
    Returns:
        Dictionary with benchmark results
    """
    print(f"\n{'='*80}")
    print(f"BENCHMARK: Duration={duration}s, Dimensions={dimensions}, Resonance Depth={resonance_depth}")
    print(f"{'='*80}")
    
    # Create framework with specified parameters
    framework = EnhancedParallelFramework(
        use_tachyon_brain=True,
        dimensions=dimensions,
        max_resonance_depth=resonance_depth
    )
    
    # Print initial status
    print("\nINITIAL STATUS:")
    print("-" * 40)
    print(framework.get_enhanced_status_summary())
    
    # Start framework
    print(f"\nStarting benchmark for {duration} seconds...")
    start_time = time.time()
    framework.start(duration=duration)
    
    # Wait for framework to complete
    while framework.running:
        time.sleep(0.1)
    
    end_time = time.time()
    actual_duration = end_time - start_time
    
    # Print final status
    print("\nFINAL STATUS:")
    print("-" * 40)
    print(framework.get_enhanced_status_summary())
    
    # Get optimizer stats
    try:
        optimizer_stats = framework.field_optimizer.get_optimization_stats()
    except Exception as e:
        optimizer_stats = {"error": str(e)}
    
    # Collect benchmark results
    results = {
        "parameters": {
            "duration": duration,
            "dimensions": dimensions,
            "resonance_depth": resonance_depth
        },
        "timing": {
            "actual_duration": actual_duration,
            "start_time": start_time,
            "end_time": end_time
        },
        "performance": {
            "phi_acceleration_factor": framework.phi_acceleration_factor,
            "field_integration_count": framework.field_integration_count,
            "integrations_per_second": framework.field_integration_count / actual_duration if actual_duration > 0 else 0
        },
        "optimizer_stats": optimizer_stats
    }
    
    print(f"\nBenchmark completed in {actual_duration:.2f} seconds")
    print(f"Acceleration Factor: {framework.phi_acceleration_factor:.2f}x")
    print(f"Field Integrations: {framework.field_integration_count}")
    print(f"Integrations/second: {results['performance']['integrations_per_second']:.2f}")
    
    return results


def run_comprehensive_benchmark() -> Dict[str, List[Dict[str, Any]]]:
    """
    Run a comprehensive benchmark with various parameters.
    
    Returns:
        Dictionary with all benchmark results
    """
    all_results = {
        "duration_tests": [],
        "dimension_tests": [],
        "resonance_tests": []
    }
    
    # Test different durations
    print("\n\n" + "="*80)
    print("BENCHMARKING DIFFERENT DURATIONS")
    print("="*80)
    for duration in BENCHMARK_DURATIONS:
        result = run_benchmark(duration=duration)
        all_results["duration_tests"].append(result)
    
    # Test different dimensions
    print("\n\n" + "="*80)
    print("BENCHMARKING DIFFERENT DIMENSIONS")
    print("="*80)
    for dimensions in DIMENSIONS:
        result = run_benchmark(dimensions=dimensions)
        all_results["dimension_tests"].append(result)
    
    # Test different resonance depths
    print("\n\n" + "="*80)
    print("BENCHMARKING DIFFERENT RESONANCE DEPTHS")
    print("="*80)
    for depth in RESONANCE_DEPTHS:
        result = run_benchmark(resonance_depth=depth)
        all_results["resonance_tests"].append(result)
    
    return all_results


def save_benchmark_results(results: Dict[str, List[Dict[str, Any]]], 
                          filepath: str = "field_optimizer_benchmark_results.json"):
    """
    Save benchmark results to a JSON file.
    
    Args:
        results: Benchmark results
        filepath: Path to save results
    """
    with open(filepath, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nBenchmark results saved to {filepath}")


def visualize_results(results: Dict[str, List[Dict[str, Any]]]):
    """
    Visualize benchmark results.
    
    Args:
        results: Benchmark results
    """
    # Create figure with subplots
    fig, axs = plt.subplots(3, 1, figsize=(12, 18))
    
    # Plot duration tests
    durations = [r["parameters"]["duration"] for r in results["duration_tests"]]
    accelerations = [r["performance"]["phi_acceleration_factor"] for r in results["duration_tests"]]
    integrations = [r["performance"]["integrations_per_second"] for r in results["duration_tests"]]
    
    axs[0].plot(durations, accelerations, 'o-', label='Acceleration Factor')
    axs[0].set_xlabel('Duration (seconds)')
    axs[0].set_ylabel('Acceleration Factor (x)')
    axs[0].set_title('Effect of Duration on Acceleration Factor')
    axs[0].grid(True)
    
    ax2 = axs[0].twinx()
    ax2.plot(durations, integrations, 'r^-', label='Integrations/sec')
    ax2.set_ylabel('Integrations per Second')
    
    lines1, labels1 = axs[0].get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    axs[0].legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    # Plot dimension tests
    dimensions = [r["parameters"]["dimensions"] for r in results["dimension_tests"]]
    accelerations = [r["performance"]["phi_acceleration_factor"] for r in results["dimension_tests"]]
    integrations = [r["performance"]["integrations_per_second"] for r in results["dimension_tests"]]
    
    axs[1].plot(dimensions, accelerations, 'o-', label='Acceleration Factor')
    axs[1].set_xlabel('Dimensions')
    axs[1].set_ylabel('Acceleration Factor (x)')
    axs[1].set_title('Effect of Dimensions on Acceleration Factor')
    axs[1].grid(True)
    
    ax2 = axs[1].twinx()
    ax2.plot(dimensions, integrations, 'r^-', label='Integrations/sec')
    ax2.set_ylabel('Integrations per Second')
    
    lines1, labels1 = axs[1].get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    axs[1].legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    # Plot resonance depth tests
    depths = [r["parameters"]["resonance_depth"] for r in results["resonance_tests"]]
    accelerations = [r["performance"]["phi_acceleration_factor"] for r in results["resonance_tests"]]
    integrations = [r["performance"]["integrations_per_second"] for r in results["resonance_tests"]]
    
    axs[2].plot(depths, accelerations, 'o-', label='Acceleration Factor')
    axs[2].set_xlabel('Resonance Depth (φ^n)')
    axs[2].set_ylabel('Acceleration Factor (x)')
    axs[2].set_title('Effect of Resonance Depth on Acceleration Factor')
    axs[2].grid(True)
    
    ax2 = axs[2].twinx()
    ax2.plot(depths, integrations, 'r^-', label='Integrations/sec')
    ax2.set_ylabel('Integrations per Second')
    
    lines1, labels1 = axs[2].get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    axs[2].legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig('field_optimizer_benchmark_results.png')
    print("Benchmark visualization saved to field_optimizer_benchmark_results.png")
    
    # Try to display the plot if running in an interactive environment
    try:
        plt.show()
    except:
        pass


def analyze_results(results: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
    """
    Analyze benchmark results and provide insights.
    
    Args:
        results: Benchmark results
        
    Returns:
        Dictionary with analysis results
    """
    # Calculate maximum acceleration factor
    all_accelerations = []
    for category in results.values():
        for result in category:
            all_accelerations.append(result["performance"]["phi_acceleration_factor"])
    
    max_acceleration = max(all_accelerations)
    avg_acceleration = sum(all_accelerations) / len(all_accelerations)
    
    # Find optimal parameters
    max_acc_result = None
    for category in results.values():
        for result in category:
            if result["performance"]["phi_acceleration_factor"] == max_acceleration:
                max_acc_result = result
                break
        if max_acc_result:
            break
    
    # Calculate theoretical maximum (phi^resonance_depth)
    phi = (1 + math.sqrt(5)) / 2
    theoretical_max = phi ** max_acc_result["parameters"]["resonance_depth"]
    efficiency = (max_acceleration / theoretical_max) * 100
    
    # Analyze dimension scaling
    dim_results = results["dimension_tests"]
    dim_scaling = []
    for i in range(1, len(dim_results)):
        prev = dim_results[i-1]["performance"]["phi_acceleration_factor"]
        curr = dim_results[i]["performance"]["phi_acceleration_factor"]
        if prev > 0:
            scaling_factor = curr / prev
            dim_scaling.append(scaling_factor)
    
    avg_dim_scaling = sum(dim_scaling) / len(dim_scaling) if dim_scaling else 0
    
    # Analyze resonance depth scaling
    res_results = results["resonance_tests"]
    res_scaling = []
    for i in range(1, len(res_results)):
        prev = res_results[i-1]["performance"]["phi_acceleration_factor"]
        curr = res_results[i]["performance"]["phi_acceleration_factor"]
        if prev > 0:
            scaling_factor = curr / prev
            res_scaling.append(scaling_factor)
    
    avg_res_scaling = sum(res_scaling) / len(res_scaling) if res_scaling else 0
    
    # Prepare analysis results
    analysis = {
        "maximum_acceleration": max_acceleration,
        "average_acceleration": avg_acceleration,
        "optimal_parameters": max_acc_result["parameters"] if max_acc_result else None,
        "theoretical_maximum": theoretical_max,
        "efficiency_percentage": efficiency,
        "dimension_scaling": {
            "scaling_factors": dim_scaling,
            "average_scaling": avg_dim_scaling
        },
        "resonance_scaling": {
            "scaling_factors": res_scaling,
            "average_scaling": avg_res_scaling
        }
    }
    
    # Print analysis summary
    print("\n" + "="*80)
    print("BENCHMARK ANALYSIS SUMMARY")
    print("="*80)
    print(f"Maximum Acceleration Factor: {max_acceleration:.2f}x")
    print(f"Average Acceleration Factor: {avg_acceleration:.2f}x")
    print(f"Optimal Parameters: {analysis['optimal_parameters']}")
    print(f"Theoretical Maximum (φ^{max_acc_result['parameters']['resonance_depth']}): {theoretical_max:.2f}x")
    print(f"Efficiency: {efficiency:.2f}%")
    print(f"Average Dimension Scaling Factor: {avg_dim_scaling:.2f}x")
    print(f"Average Resonance Depth Scaling Factor: {avg_res_scaling:.2f}x")
    
    # Extrapolate to higher resonance depths
    print("\n" + "-"*40)
    print("EXTRAPOLATION TO HIGHER RESONANCE DEPTHS")
    print("-"*40)
    for depth in [15, 20, 25, 30]:
        extrapolated = max_acceleration * (avg_res_scaling ** (depth - max_acc_result["parameters"]["resonance_depth"]))
        print(f"Estimated Acceleration at Depth {depth}: {extrapolated:.2f}x")
    
    # Estimate acceleration needed for 17,000x
    if avg_res_scaling > 1:
        target = 17000
        current = max_acceleration
        depth_needed = max_acc_result["parameters"]["resonance_depth"]
        while current < target:
            depth_needed += 1
            current *= avg_res_scaling
        
        print(f"\nTo achieve 17,000x acceleration, estimated resonance depth needed: {depth_needed}")
    
    return analysis


def main():
    """Main function to run benchmarks and analyze results"""
    print("\n" + "="*80)
    print("FIELD OPTIMIZER BENCHMARK")
    print("="*80)
    
    # Run comprehensive benchmark
    results = run_comprehensive_benchmark()
    
    # Save results
    save_benchmark_results(results)
    
    # Analyze results
    analysis = analyze_results(results)
    
    # Visualize results
    try:
        visualize_results(results)
    except Exception as e:
        print(f"Error visualizing results: {e}")
    
    print("\n" + "="*80)
    print("BENCHMARK COMPLETE")
    print("="*80)
    
    return results, analysis


if __name__ == "__main__":
    main()
