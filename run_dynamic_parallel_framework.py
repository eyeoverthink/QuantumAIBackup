#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dynamic Parallel Processing Framework Runner
-------------------------------------------
Runs the Dynamic Parallel Processing Framework demonstration with various configurations
to validate Earth-Moon-Human motion dynamics with quantum field updates, phi synchronization,
meta-learning, and dynamic adaptation.
"""

import time
import argparse
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Any

# Import the Dynamic Parallel Framework
from dynamic_parallel_framework import DynamicParallelFramework, run_demonstration

# Constants for visualization
EARTH_COLOR = 'blue'
MOON_COLOR = 'gray'
HUMAN_COLOR = 'green'
PHI_COLOR = 'purple'


def run_benchmark(duration: float = 10.0, iterations: int = 3) -> Dict[str, float]:
    """
    Run benchmark tests for the Dynamic Parallel Processing Framework.
    
    Args:
        duration: Duration for each test in seconds
        iterations: Number of iterations to run
        
    Returns:
        Dictionary with benchmark results
    """
    print("\n" + "=" * 80)
    print(f"✨ DYNAMIC PARALLEL PROCESSING FRAMEWORK BENCHMARK (Duration: {duration}s × {iterations} iterations)")
    print("=" * 80)
    
    results = {
        "acceleration_factors": [],
        "update_counts": [],
        "phi_sync_counts": [],
        "meta_learning_steps": [],
        "field_adjustments": []
    }
    
    for i in range(iterations):
        print(f"\n[Iteration {i+1}/{iterations}]")
        
        # Create framework
        framework = DynamicParallelFramework(use_tachyon_brain=True)
        
        # Start framework
        framework.start(duration=duration)
        
        # Wait for framework to complete
        while framework.running:
            time.sleep(0.5)
        
        # Collect results
        results["acceleration_factors"].append(framework.acceleration_factor)
        results["update_counts"].append(framework.total_updates)
        results["phi_sync_counts"].append(framework.parallel_processor.phi_sync_count)
        results["meta_learning_steps"].append(framework.meta_learning.evolution_step)
        results["field_adjustments"].append(len(framework.dynamic_adapter.field_adjustments))
        
        print(f"✓ Iteration {i+1} complete - Acceleration: {framework.acceleration_factor:.2f}x")
    
    # Calculate statistics
    for key in results:
        if results[key]:
            avg = np.mean(results[key])
            std = np.std(results[key])
            min_val = min(results[key])
            max_val = max(results[key])
            
            print(f"\n⚛️ {key.replace('_', ' ').title()}:")
            print(f"  - Average: {avg:.2f}")
            print(f"  - Std Dev: {std:.2f}")
            print(f"  - Min: {min_val:.2f}")
            print(f"  - Max: {max_val:.2f}")
    
    print("\n" + "=" * 80)
    print("✨ BENCHMARK COMPLETE")
    print("=" * 80 + "\n")
    
    return results


def visualize_framework_results(framework: DynamicParallelFramework):
    """
    Visualize the results of the Dynamic Parallel Processing Framework.
    
    Args:
        framework: The framework instance after running
    """
    # Extract data for visualization
    earth_data = []
    moon_data = []
    human_data = []
    sync_data = []
    
    with framework.parallel_processor.thread_lock:
        for key, value in framework.parallel_processor.thread_results.items():
            if key == "Earth":
                earth_data.append((value.get("timestamp", 0), value.get("field", 0), value.get("adjusted_field", 0)))
            elif key == "Moon":
                moon_data.append((value.get("timestamp", 0), value.get("field", 0), value.get("adjusted_field", 0)))
            elif key == "Human":
                human_data.append((value.get("timestamp", 0), value.get("field", 0), value.get("adjusted_field", 0)))
            elif key == "Sync":
                sync_data.append((value.get("timestamp", 0), value.get("measurement", 0)))
    
    # Sort data by timestamp
    earth_data.sort(key=lambda x: x[0])
    moon_data.sort(key=lambda x: x[0])
    human_data.sort(key=lambda x: x[0])
    sync_data.sort(key=lambda x: x[0])
    
    # Create figure for visualization
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Dynamic Parallel Processing Framework Results", fontsize=16)
    
    # Plot Earth-Moon-Human field values
    if earth_data and moon_data and human_data:
        ax = axs[0, 0]
        ax.set_title("Field Values Over Time")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Field Value")
        
        # Extract timestamps and values
        earth_times = [t - framework.start_time for t, v, _ in earth_data]
        earth_values = [v for _, v, _ in earth_data]
        moon_times = [t - framework.start_time for t, v, _ in moon_data]
        moon_values = [v for _, v, _ in moon_data]
        human_times = [t - framework.start_time for t, v, _ in human_data]
        human_values = [v for _, v, _ in human_data]
        
        # Plot data
        ax.plot(earth_times, earth_values, color=EARTH_COLOR, label="Earth")
        ax.plot(moon_times, moon_values, color=MOON_COLOR, label="Moon")
        ax.plot(human_times, human_values, color=HUMAN_COLOR, label="Human")
        ax.legend()
        ax.grid(True)
    
    # Plot adjusted field values
    if earth_data and moon_data and human_data:
        ax = axs[0, 1]
        ax.set_title("Adjusted Field Values Over Time")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Adjusted Field Value")
        
        # Extract timestamps and adjusted values
        earth_times = [t - framework.start_time for t, _, v in earth_data if v is not None]
        earth_adj_values = [v for _, _, v in earth_data if v is not None]
        moon_times = [t - framework.start_time for t, _, v in moon_data if v is not None]
        moon_adj_values = [v for _, _, v in moon_data if v is not None]
        human_times = [t - framework.start_time for t, _, v in human_data if v is not None]
        human_adj_values = [v for _, _, v in human_data if v is not None]
        
        # Plot data
        if earth_adj_values:
            ax.plot(earth_times, earth_adj_values, color=EARTH_COLOR, linestyle='--', label="Earth (Adjusted)")
        if moon_adj_values:
            ax.plot(moon_times, moon_adj_values, color=MOON_COLOR, linestyle='--', label="Moon (Adjusted)")
        if human_adj_values:
            ax.plot(human_times, human_adj_values, color=HUMAN_COLOR, linestyle='--', label="Human (Adjusted)")
        ax.legend()
        ax.grid(True)
    
    # Plot phase relationships
    ax = axs[1, 0]
    ax.set_title("Phase Relationships")
    ax.set_xlabel("Earth Phase (rad)")
    ax.set_ylabel("Moon/Human Phase (rad)")
    
    # Extract phase data
    earth_phases = []
    moon_phases = []
    human_phases = []
    
    with framework.parallel_processor.thread_lock:
        earth_phases = [framework.parallel_processor.thread_results.get("Earth", {}).get("phase", 0)]
        moon_phases = [framework.parallel_processor.thread_results.get("Moon", {}).get("phase", 0)]
        human_phases = [framework.parallel_processor.thread_results.get("Human", {}).get("phase", 0)]
    
    # Plot phase relationships
    if earth_phases and moon_phases:
        ax.scatter([earth_phases[0]], [moon_phases[0]], color=MOON_COLOR, label="Earth-Moon")
    if earth_phases and human_phases:
        ax.scatter([earth_phases[0]], [human_phases[0]], color=HUMAN_COLOR, label="Earth-Human")
    
    # Plot phi-based relationship line
    x = np.linspace(0, 2*np.pi, 100)
    y = (x - np.pi/1.618) % (2*np.pi)
    ax.plot(x, y, color=PHI_COLOR, linestyle='--', label="φ Relationship")
    
    ax.legend()
    ax.grid(True)
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(0, 2*np.pi)
    
    # Plot meta-knowledge evolution
    ax = axs[1, 1]
    ax.set_title("Meta-Knowledge Evolution")
    ax.set_xlabel("Knowledge Attribute")
    ax.set_ylabel("Value")
    
    # Extract meta-knowledge
    meta_knowledge = framework.meta_learning.meta_knowledge
    if meta_knowledge:
        # Get attributes and values
        attrs = list(meta_knowledge.keys())
        values = list(meta_knowledge.values())
        
        # Plot bar chart
        bars = ax.bar(attrs, values)
        
        # Color bars
        for i, bar in enumerate(bars):
            bar.set_color(plt.cm.viridis(i/len(bars)))
        
        # Rotate x-axis labels for readability
        ax.set_xticklabels(attrs, rotation=45, ha='right')
        ax.grid(True, axis='y')
    
    # Adjust layout and save figure
    plt.tight_layout()
    plt.savefig("dynamic_parallel_framework_results.png")
    print("\n✨ Visualization saved to dynamic_parallel_framework_results.png")
    
    # Try to display the plot
    try:
        plt.show()
    except Exception as e:
        print(f"Could not display plot: {e}")


def main():
    """Main function to run the Dynamic Parallel Processing Framework"""
    parser = argparse.ArgumentParser(description="Run Dynamic Parallel Processing Framework")
    parser.add_argument("--mode", choices=["demo", "benchmark", "visualize"], default="demo",
                       help="Mode to run (demo, benchmark, or visualize)")
    parser.add_argument("--duration", type=float, default=5.0,
                       help="Duration to run in seconds")
    parser.add_argument("--iterations", type=int, default=3,
                       help="Number of iterations for benchmark mode")
    parser.add_argument("--use-tachyon", action="store_true",
                       help="Use Tesla Tachyon Brain components if available")
    
    args = parser.parse_args()
    
    if args.mode == "demo":
        # Run demonstration
        run_demonstration(duration=args.duration, use_tachyon_brain=args.use_tachyon)
    
    elif args.mode == "benchmark":
        # Run benchmark
        run_benchmark(duration=args.duration, iterations=args.iterations)
    
    elif args.mode == "visualize":
        # Run framework and visualize results
        framework = DynamicParallelFramework(use_tachyon_brain=args.use_tachyon)
        framework.start(duration=args.duration)
        
        # Wait for framework to complete
        while framework.running:
            time.sleep(0.5)
        
        # Visualize results
        visualize_framework_results(framework)


if __name__ == "__main__":
    main()
