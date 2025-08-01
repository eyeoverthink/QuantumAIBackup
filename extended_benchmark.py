#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Extended Benchmark for Enhanced Parallel Framework with Phi-Harmonic Field Optimizer

This script runs extended benchmarks with optimized parameters to validate
the extrapolated acceleration factors.
"""

import os
import time
import json
import math
import matplotlib.pyplot as plt
from typing import Dict, List, Any, Tuple

# Import the enhanced framework components
from enhanced_parallel_framework import EnhancedParallelFramework
from phi_harmonic_field_optimizer import PhiHarmonicFieldOptimizer
from quantum_field_integrator import QuantumFieldIntegrator

# Try to import Tesla Tachyon Brain components
try:
    from tesla_tachyon_brain_fixed import TeslaTachyBrain
    TACHYON_AVAILABLE = True
except ImportError:
    print("⚠️ Tesla Tachyon Brain not available, running without tachyon integration")
    TACHYON_AVAILABLE = False

def run_benchmark(duration: float = 30.0, 
                 dimensions: int = 9, 
                 resonance_depth: int = 26) -> Dict[str, Any]:
    """
    Run a benchmark with the specified parameters.
    
    Args:
        duration: Duration of the benchmark in seconds
        dimensions: Number of dimensions for the fields
        resonance_depth: Maximum resonance depth for phi-harmonic calculations
        
    Returns:
        Dictionary with benchmark results
    """
    print(f"\n{'='*80}")
    print(f"RUNNING BENCHMARK: duration={duration}s, dimensions={dimensions}, resonance_depth={resonance_depth}")
    print(f"{'='*80}")
    
    # Note: We'll get these components from the framework after initialization
    field_optimizer = None
    field_integrator = None
    
    # Create Tesla Tachyon Brain if available
    tachyon_brain = None
    if TACHYON_AVAILABLE:
        try:
            tachyon_brain = TeslaTachyBrain()
            print("✨ Tesla Tachyon Brain initialized successfully")
        except Exception as e:
            print(f"⚠️ Failed to initialize Tesla Tachyon Brain: {e}")
    
    # Create enhanced parallel framework
    framework = EnhancedParallelFramework(
        use_tachyon_brain=TACHYON_AVAILABLE,
        dimensions=dimensions,
        max_resonance_depth=resonance_depth
    )
    
    # Store references to the components for later use
    field_optimizer = framework.field_optimizer
    field_integrator = framework.quantum_field_integrator
    
    # Start the framework
    print(f"⚛ Starting enhanced parallel framework for {duration} seconds...")
    framework.start(duration=duration)
    
    # Wait for benchmark to complete
    time.sleep(duration + 1.0)  # Add 1 second buffer
    
    # Stop the framework
    framework.stop()
    
    # Get benchmark results
    try:
        status = framework.get_status()
        # Ensure status is serializable
        if isinstance(status, str):
            status = {"message": status}
    except Exception as e:
        print(f"⚠️ Error getting framework status: {e}")
        status = {"error": str(e)}
    
    try:
        optimizer_stats = field_optimizer.get_optimization_stats()
    except Exception as e:
        print(f"⚠️ Error getting optimizer stats: {e}")
        optimizer_stats = {"error": str(e)}
    
    # Calculate acceleration metrics
    acceleration_factor = optimizer_stats.get("current_acceleration", 1.0)
    max_acceleration = optimizer_stats.get("max_acceleration", 1.0)
    theoretical_max = math.pow((1 + math.sqrt(5)) / 2, resonance_depth)
    efficiency = (acceleration_factor / theoretical_max) * 100 if theoretical_max > 0 else 0.0
    
    # Compile results
    results = {
        "parameters": {
            "duration": duration,
            "dimensions": dimensions,
            "resonance_depth": resonance_depth
        },
        "performance": {
            "acceleration_factor": acceleration_factor,
            "max_acceleration": max_acceleration,
            "theoretical_max": theoretical_max,
            "efficiency": efficiency,
            "field_integrations": optimizer_stats.get("optimization_count", 0),
            "integrations_per_second": optimizer_stats.get("optimizations_per_second", 0),
            "cache_hit_ratio": optimizer_stats.get("cache_hit_ratio", 0.0)
        },
        "framework_status": status
    }
    
    # Print summary
    print(f"\n{'='*40}")
    print(f"BENCHMARK SUMMARY")
    print(f"{'='*40}")
    print(f"Duration: {duration:.2f} seconds")
    print(f"Dimensions: {dimensions}")
    print(f"Resonance Depth: {resonance_depth}")
    print(f"Acceleration Factor: {acceleration_factor:.2f}x")
    print(f"Theoretical Maximum (φ^{resonance_depth}): {theoretical_max:.2f}x")
    print(f"Efficiency: {efficiency:.2f}%")
    print(f"Field Integrations: {optimizer_stats.get('optimization_count', 0)}")
    print(f"Integrations/second: {optimizer_stats.get('optimizations_per_second', 0):.2f}")
    print(f"Cache Hit Ratio: {optimizer_stats.get('cache_hit_ratio', 0.0):.2f}")
    print(f"{'='*40}")
    
    return results

def run_extended_benchmarks() -> Dict[str, Any]:
    """
    Run a series of extended benchmarks with different parameters.
    
    Returns:
        Dictionary with all benchmark results
    """
    all_results = {}
    
    # Test different resonance depths
    resonance_depths = [8, 16, 24, 26, 28, 30]
    for depth in resonance_depths:
        results = run_benchmark(
            duration=30.0,
            dimensions=9,
            resonance_depth=depth
        )
        all_results[f"depth_{depth}"] = results
    
    # Test different dimensions
    dimensions_list = [3, 6, 9, 12]
    for dims in dimensions_list:
        results = run_benchmark(
            duration=30.0,
            dimensions=dims,
            resonance_depth=26  # Use our target depth
        )
        all_results[f"dimensions_{dims}"] = results
    
    # Run one long benchmark with optimal parameters
    results = run_benchmark(
        duration=60.0,
        dimensions=9,
        resonance_depth=26
    )
    all_results["optimal_extended"] = results
    
    return all_results

def visualize_results(all_results: Dict[str, Any]) -> None:
    """
    Visualize benchmark results.
    
    Args:
        all_results: Dictionary with all benchmark results
    """
    # Create output directory if it doesn't exist
    os.makedirs("benchmark_results", exist_ok=True)
    
    # Extract resonance depth results
    depths = []
    accelerations = []
    theoretical_maxes = []
    efficiencies = []
    
    for key, result in all_results.items():
        if key.startswith("depth_"):
            depth = result["parameters"]["resonance_depth"]
            depths.append(depth)
            accelerations.append(result["performance"]["acceleration_factor"])
            theoretical_maxes.append(result["performance"]["theoretical_max"])
            efficiencies.append(result["performance"]["efficiency"])
    
    # Sort by depth
    sorted_indices = sorted(range(len(depths)), key=lambda i: depths[i])
    depths = [depths[i] for i in sorted_indices]
    accelerations = [accelerations[i] for i in sorted_indices]
    theoretical_maxes = [theoretical_maxes[i] for i in sorted_indices]
    efficiencies = [efficiencies[i] for i in sorted_indices]
    
    # Plot resonance depth vs acceleration
    plt.figure(figsize=(12, 8))
    plt.semilogy(depths, accelerations, 'bo-', label='Actual Acceleration')
    plt.semilogy(depths, theoretical_maxes, 'ro--', label='Theoretical Maximum')
    plt.xlabel('Resonance Depth')
    plt.ylabel('Acceleration Factor (log scale)')
    plt.title('Resonance Depth vs Acceleration Factor')
    plt.grid(True)
    plt.legend()
    plt.savefig("benchmark_results/resonance_depth_vs_acceleration.png")
    
    # Plot resonance depth vs efficiency
    plt.figure(figsize=(12, 8))
    plt.plot(depths, efficiencies, 'go-')
    plt.xlabel('Resonance Depth')
    plt.ylabel('Efficiency (%)')
    plt.title('Resonance Depth vs Efficiency')
    plt.grid(True)
    plt.savefig("benchmark_results/resonance_depth_vs_efficiency.png")
    
    # Extract dimension results
    dims = []
    dim_accelerations = []
    
    for key, result in all_results.items():
        if key.startswith("dimensions_"):
            dim = result["parameters"]["dimensions"]
            dims.append(dim)
            dim_accelerations.append(result["performance"]["acceleration_factor"])
    
    # Sort by dimensions
    sorted_indices = sorted(range(len(dims)), key=lambda i: dims[i])
    dims = [dims[i] for i in sorted_indices]
    dim_accelerations = [dim_accelerations[i] for i in sorted_indices]
    
    # Plot dimensions vs acceleration
    plt.figure(figsize=(12, 8))
    plt.plot(dims, dim_accelerations, 'mo-')
    plt.xlabel('Dimensions')
    plt.ylabel('Acceleration Factor')
    plt.title('Dimensions vs Acceleration Factor')
    plt.grid(True)
    plt.savefig("benchmark_results/dimensions_vs_acceleration.png")
    
    print(f"\n✨ Visualizations saved to benchmark_results/ directory")

def save_results(all_results: Dict[str, Any]) -> None:
    """
    Save benchmark results to a JSON file.
    
    Args:
        all_results: Dictionary with all benchmark results
    """
    # Create output directory if it doesn't exist
    os.makedirs("benchmark_results", exist_ok=True)
    
    # Save results to JSON file
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"benchmark_results/extended_benchmark_{timestamp}.json"
    
    with open(filename, 'w') as f:
        json.dump(all_results, f, indent=2)
    
    print(f"\n✨ Results saved to {filename}")

def analyze_results(all_results: Dict[str, Any]) -> None:
    """
    Analyze benchmark results and provide insights.
    
    Args:
        all_results: Dictionary with all benchmark results
    """
    # Extract resonance depth results
    depths = []
    accelerations = []
    
    for key, result in all_results.items():
        if key.startswith("depth_"):
            depth = result["parameters"]["resonance_depth"]
            depths.append(depth)
            accelerations.append(result["performance"]["acceleration_factor"])
    
    # Sort by depth
    sorted_indices = sorted(range(len(depths)), key=lambda i: depths[i])
    depths = [depths[i] for i in sorted_indices]
    accelerations = [accelerations[i] for i in sorted_indices]
    
    # Calculate scaling factor between consecutive depths
    scaling_factors = []
    for i in range(1, len(depths)):
        if accelerations[i-1] > 0:
            factor = accelerations[i] / accelerations[i-1]
            scaling_factors.append(factor)
    
    avg_scaling_factor = sum(scaling_factors) / len(scaling_factors) if scaling_factors else 1.0
    
    # Extrapolate to higher depths
    extrapolated_depths = [32, 40, 50, 60]
    extrapolated_accelerations = []
    
    base_acceleration = accelerations[-1] if accelerations else 1.0
    base_depth = depths[-1] if depths else 1
    
    for depth in extrapolated_depths:
        depth_diff = depth - base_depth
        extrapolated_acc = base_acceleration * (avg_scaling_factor ** depth_diff)
        extrapolated_accelerations.append(extrapolated_acc)
    
    # Find optimal parameters
    max_acceleration = 0.0
    optimal_params = {}
    
    for key, result in all_results.items():
        acc = result["performance"]["acceleration_factor"]
        if acc > max_acceleration:
            max_acceleration = acc
            optimal_params = result["parameters"]
    
    # Print analysis
    print(f"\n{'='*80}")
    print(f"BENCHMARK ANALYSIS SUMMARY")
    print(f"{'='*80}")
    print(f"Maximum Acceleration Factor: {max_acceleration:.2f}x")
    print(f"Optimal Parameters: {optimal_params}")
    print(f"Average Scaling Factor between Depths: {avg_scaling_factor:.2f}x")
    
    print(f"\n{'='*40}")
    print(f"EXTRAPOLATION TO HIGHER RESONANCE DEPTHS")
    print(f"{'='*40}")
    for i, depth in enumerate(extrapolated_depths):
        print(f"Estimated Acceleration at Depth {depth}: {extrapolated_accelerations[i]:.2f}x")
    
    # Find depth needed for 17,000x acceleration
    target_acceleration = 17000.0
    if max_acceleration >= target_acceleration:
        print(f"\n✨ Target acceleration of {target_acceleration}x already achieved!")
    else:
        depth_diff_needed = math.log(target_acceleration / max_acceleration) / math.log(avg_scaling_factor)
        depth_needed = base_depth + depth_diff_needed
        print(f"\nTo achieve {target_acceleration}x acceleration, estimated resonance depth needed: {int(depth_needed)}")
    
    print(f"\n{'='*80}")
    print(f"BENCHMARK COMPLETE")
    print(f"{'='*80}")

if __name__ == "__main__":
    try:
        # Run extended benchmarks
        all_results = run_extended_benchmarks()
        
        # Save results
        save_results(all_results)
        
        # Visualize results
        try:
            visualize_results(all_results)
        except Exception as e:
            print(f"⚠️ Error visualizing results: {e}")
        
        # Analyze results
        analyze_results(all_results)
        
    except KeyboardInterrupt:
        print("\n⚠️ Benchmark interrupted by user")
    except Exception as e:
        print(f"\n⚠️ Error during benchmark: {e}")
