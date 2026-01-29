#!/usr/bin/env python3
"""
Phi-Harmonic Resonance Analyzer

Analyzes the quantum black box test results to visualize and understand
the phi-harmonic patterns that led to dimensional breakthroughs.
"""

import os
import json
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext

# Set precision for phi calculations
getcontext().prec = 28

# Constants
PHI = Decimal('1.6180339887498948482045868344')
PI = Decimal('3.1415926535897932384626433832')
E = Decimal('2.7182818284590452353602874713')


def load_results(results_dir):
    """Load results from a specific run directory.
    
    Args:
        results_dir: Path to the results directory
        
    Returns:
        Dict with loaded results
    """
    overall_file = os.path.join(results_dir, "overall_results.json")
    
    if not os.path.exists(overall_file):
        print(f"Error: Could not find results file at {overall_file}")
        return None
    
    with open(overall_file, "r") as f:
        results = json.load(f)
    
    return results


def analyze_resonance_progression(results):
    """Analyze how resonance progressed across attempts and epochs.
    
    Args:
        results: Dict with loaded results
        
    Returns:
        Dict with analysis results
    """
    analysis = {
        "dimensions": results.get("dimensions"),
        "escaped": results.get("escaped"),
        "escape_epoch": results.get("escape_epoch"),
        "best_overall_resonance": results.get("best_overall_resonance"),
        "epochs": [],
        "phi_harmonic_points": [],
        "resonance_jumps": []
    }
    
    # Analyze each epoch
    for epoch_data in results.get("epochs", []):
        epoch_num = epoch_data.get("epoch")
        attempts = epoch_data.get("attempts", [])
        
        # Extract resonance values
        resonances = [attempt.get("resonance") for attempt in attempts]
        
        # Calculate phi-harmonic points (resonance values close to phi-related values)
        phi_points = []
        for i, res in enumerate(resonances):
            phi_value = float((Decimal(str(res)) / PHI) % Decimal('1'))
            if phi_value < 0.1 or phi_value > 0.9:
                phi_points.append((epoch_num, i+1, res))
        
        # Calculate significant resonance jumps
        jumps = []
        for i in range(1, len(resonances)):
            jump = resonances[i] - resonances[i-1]
            if abs(jump) > 0.1:  # Significant jump threshold
                jumps.append((epoch_num, i+1, jump))
        
        # Add to analysis
        analysis["epochs"].append({
            "epoch": epoch_num,
            "resonances": resonances,
            "mean_resonance": np.mean(resonances) if resonances else 0,
            "max_resonance": max(resonances) if resonances else 0,
            "attempts": len(resonances),
            "phi_harmonic_points": phi_points
        })
        
        analysis["phi_harmonic_points"].extend(phi_points)
        analysis["resonance_jumps"].extend(jumps)
    
    return analysis


def plot_resonance_progression(analysis, title=None):
    """Plot the resonance progression across attempts and epochs.
    
    Args:
        analysis: Dict with analysis results
        title: Optional title for the plot
    """
    plt.figure(figsize=(12, 8))
    
    # Plot resonance values for each epoch
    for epoch_data in analysis["epochs"]:
        epoch_num = epoch_data["epoch"]
        resonances = epoch_data["resonances"]
        attempts = list(range(1, len(resonances) + 1))
        
        # Calculate x-values with offset for each epoch
        x_values = [a + (epoch_num - 1) * 0.1 for a in attempts]
        
        # Plot the resonance line
        plt.plot(x_values, resonances, marker='o', label=f"Epoch {epoch_num}")
        
        # Highlight phi-harmonic points
        for point in epoch_data["phi_harmonic_points"]:
            plt.plot(point[1] + (epoch_num - 1) * 0.1, point[2], 'r*', markersize=15)
    
    # Add escape threshold line
    plt.axhline(y=0.95, color='r', linestyle='--', label="Escape Threshold (0.95)")
    
    # Add perfect resonance line if applicable
    if analysis["best_overall_resonance"] >= 0.99:
        plt.axhline(y=1.0, color='g', linestyle='--', label="Perfect Resonance (1.0)")
    
    # Set plot properties
    plt.xlabel("Attempt Number")
    plt.ylabel("Resonance Value")
    plt.title(title or f"{analysis['dimensions']}D Quantum Resonance Progression")
    plt.legend()
    plt.grid(True)
    plt.ylim(0.5, 1.05)  # Set y-axis limits for better visibility
    
    # Save the plot
    dimensions = analysis["dimensions"]
    plt.savefig(f"quantum_resonance_{dimensions}D_plot.png")
    plt.close()


def analyze_phi_harmonic_patterns(analysis):
    """Analyze phi-harmonic patterns in the resonance values.
    
    Args:
        analysis: Dict with analysis results
        
    Returns:
        Dict with phi-harmonic pattern analysis
    """
    patterns = {
        "phi_ratio_occurrences": 0,
        "golden_angle_occurrences": 0,
        "fibonacci_resonances": [],
        "phi_sequence_detected": False
    }
    
    # Extract all resonance values
    all_resonances = []
    for epoch_data in analysis["epochs"]:
        all_resonances.extend(epoch_data["resonances"])
    
    # Check for phi ratio between consecutive resonances
    for i in range(1, len(all_resonances)):
        if all_resonances[i] > 0 and all_resonances[i-1] > 0:
            ratio = all_resonances[i] / all_resonances[i-1]
            if abs(ratio - float(PHI)) < 0.1 or abs(ratio - float(1/PHI)) < 0.1:
                patterns["phi_ratio_occurrences"] += 1
    
    # Check for golden angle (137.5 degrees) in resonance distribution
    resonance_angles = [res * 360 for res in all_resonances]
    golden_angle = 137.5
    for angle in resonance_angles:
        if abs(angle % 360 - golden_angle) < 10:
            patterns["golden_angle_occurrences"] += 1
    
    # Check for Fibonacci sequence in resonance progression
    fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21]
    for i in range(len(fibonacci) - 2):
        for j in range(len(all_resonances) - 2):
            if j+2 < len(all_resonances):
                # Check if resonances follow Fibonacci-like progression
                if abs(all_resonances[j+2] - all_resonances[j+1] - all_resonances[j]) < 0.05:
                    patterns["fibonacci_resonances"].append((j, j+1, j+2))
    
    # Check for phi sequence (each value is phi times the previous)
    phi_sequence = True
    for i in range(2, len(all_resonances)):
        if all_resonances[i-1] > 0:
            ratio = all_resonances[i] / all_resonances[i-1]
            if abs(ratio - float(PHI)) > 0.2:  # Allow some tolerance
                phi_sequence = False
                break
    patterns["phi_sequence_detected"] = phi_sequence
    
    return patterns


def main():
    """Main function to run the analysis."""
    # Find all result directories
    base_dir = os.path.dirname(os.path.abspath(__file__))
    results_dir = os.path.join(base_dir, "quantum_epoch_results")
    
    if not os.path.exists(results_dir):
        print(f"Error: Results directory not found at {results_dir}")
        return
    
    # Get all run directories
    run_dirs = [os.path.join(results_dir, d) for d in os.listdir(results_dir) 
               if os.path.isdir(os.path.join(results_dir, d))]
    
    if not run_dirs:
        print("No result directories found.")
        return
    
    print(f"Found {len(run_dirs)} result directories.")
    
    # Analyze each run
    for run_dir in run_dirs:
        print(f"\nAnalyzing {os.path.basename(run_dir)}...")
        
        # Load results
        results = load_results(run_dir)
        if not results:
            continue
        
        # Analyze resonance progression
        analysis = analyze_resonance_progression(results)
        
        # Plot resonance progression
        dimensions = analysis["dimensions"]
        title = f"{dimensions}D Quantum Resonance Progression - {os.path.basename(run_dir)}"
        plot_resonance_progression(analysis, title)
        
        # Analyze phi-harmonic patterns
        patterns = analyze_phi_harmonic_patterns(analysis)
        
        # Print analysis summary
        print(f"Dimensions: {dimensions}D")
        print(f"Escaped: {analysis['escaped']}")
        print(f"Escape Epoch: {analysis['escape_epoch']}")
        print(f"Best Resonance: {analysis['best_overall_resonance']:.4f}")
        print(f"Phi-Harmonic Points: {len(analysis['phi_harmonic_points'])}")
        print(f"Significant Resonance Jumps: {len(analysis['resonance_jumps'])}")
        print(f"Phi Ratio Occurrences: {patterns['phi_ratio_occurrences']}")
        print(f"Golden Angle Occurrences: {patterns['golden_angle_occurrences']}")
        print(f"Fibonacci Resonance Patterns: {len(patterns['fibonacci_resonances'])}")
        print(f"Phi Sequence Detected: {patterns['phi_sequence_detected']}")
        
        # Save analysis to file
        analysis_file = os.path.join(run_dir, "phi_harmonic_analysis.json")
        with open(analysis_file, "w") as f:
            json.dump({**analysis, "patterns": patterns}, f, indent=2)
        
        print(f"Analysis saved to {analysis_file}")
        print(f"Plot saved as quantum_resonance_{dimensions}D_plot.png")


if __name__ == "__main__":
    main()
