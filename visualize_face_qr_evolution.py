#!/usr/bin/env python3
"""
Face QR Evolution Visualization

This script visualizes the results of the Face QR Evolution system's adaptation
over multiple generations, showing how parameters evolved and authentication
performance improved.
"""

import os
import sys
import json
import glob
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Set style for plots
plt.style.use('seaborn-v0_8-darkgrid')

def load_test_results():
    """
    Load the most recent test results file.
    
    Returns:
        dict: Test results data
    """
    # Find all results files
    results_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "evolution_test_results")
    result_files = glob.glob(os.path.join(results_dir, "evolution_test_results_*.json"))
    
    if not result_files:
        print("No test results found.")
        return None
    
    # Get the most recent file
    latest_file = max(result_files, key=os.path.getmtime)
    print(f"Loading results from: {latest_file}")
    
    # Load the file
    with open(latest_file, 'r') as f:
        results = json.load(f)
    
    return results

def load_epigenetic_memory():
    """
    Load the epigenetic memory file.
    
    Returns:
        dict: Epigenetic memory data
    """
    memory_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                              "evolution_data", "face_qr_epigenetic_memory.json")
    
    if not os.path.exists(memory_path):
        print("No epigenetic memory file found.")
        return None
    
    # Load the file
    with open(memory_path, 'r') as f:
        memory = json.load(f)
    
    return memory

def visualize_parameter_evolution(results, memory=None):
    """
    Visualize how parameters evolved over generations.
    
    Args:
        results: Test results data
        memory: Epigenetic memory data (optional)
    """
    # Extract generations and parameters
    generations = []
    similarity_thresholds = []
    feature_weights = []
    temporal_factors = []
    complexities = []
    resonances = []
    mutation_rates = []
    
    # Extract from test results
    for result in results["results"]:
        if "generation" in result:
            generations.append(result["generation"])
            
            if "similarity_threshold" in result:
                similarity_thresholds.append(result["similarity_threshold"])
            
            if "feature_weight" in result:
                feature_weights.append(result["feature_weight"])
                
            if "temporal_factor" in result:
                temporal_factors.append(result["temporal_factor"])
                
            if "complexity" in result:
                complexities.append(result["complexity"])
                
            if "resonance" in result:
                resonances.append(result["resonance"])
                
            if "mutation_rate" in result:
                mutation_rates.append(result["mutation_rate"])
    
    # Create figure with subplots
    fig, axs = plt.subplots(3, 2, figsize=(14, 12))
    fig.suptitle('Face QR Evolution: Parameter Adaptation Over Generations', fontsize=16)
    
    # Plot parameters
    if similarity_thresholds:
        axs[0, 0].plot(generations, similarity_thresholds, 'o-', color='blue')
        axs[0, 0].set_title('Similarity Threshold')
        axs[0, 0].set_xlabel('Generation')
        axs[0, 0].set_ylabel('Threshold Value')
    
    if feature_weights:
        axs[0, 1].plot(generations, feature_weights, 'o-', color='green')
        axs[0, 1].set_title('Feature Weight')
        axs[0, 1].set_xlabel('Generation')
        axs[0, 1].set_ylabel('Weight Value')
    
    if temporal_factors:
        axs[1, 0].plot(generations, temporal_factors, 'o-', color='red')
        axs[1, 0].set_title('Temporal Factor')
        axs[1, 0].set_xlabel('Generation')
        axs[1, 0].set_ylabel('Factor Value')
    
    if complexities:
        axs[1, 1].plot(generations, complexities, 'o-', color='purple')
        axs[1, 1].set_title('Complexity')
        axs[1, 1].set_xlabel('Generation')
        axs[1, 1].set_ylabel('Complexity Value')
    
    if resonances:
        axs[2, 0].plot(generations, resonances, 'o-', color='orange')
        axs[2, 0].set_title('Resonance')
        axs[2, 0].set_xlabel('Generation')
        axs[2, 0].set_ylabel('Resonance Value')
    
    if mutation_rates:
        axs[2, 1].plot(generations, mutation_rates, 'o-', color='brown')
        axs[2, 1].set_title('Mutation Rate')
        axs[2, 1].set_xlabel('Generation')
        axs[2, 1].set_ylabel('Rate Value')
    
    plt.tight_layout()
    
    # Save the figure
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                              "evolution_test_results", f"parameter_evolution_{timestamp}.png")
    plt.savefig(output_path)
    print(f"Saved parameter evolution visualization to {output_path}")
    
    return fig

def visualize_authentication_performance(results):
    """
    Visualize authentication performance over generations.
    
    Args:
        results: Test results data
    """
    # Extract generations and authentication results
    generations = []
    similarities = []
    successes = []
    
    # Extract from test results
    for result in results["results"]:
        if "generation" in result and "similarity" in result:
            generations.append(result["generation"])
            similarities.append(result["similarity"])
            
            if "success" in result:
                successes.append(1 if result["success"] else 0)
    
    # Create figure
    fig, ax1 = plt.subplots(figsize=(12, 6))
    
    # Plot similarity scores
    color = 'tab:blue'
    ax1.set_xlabel('Generation')
    ax1.set_ylabel('Similarity Score', color=color)
    ax1.plot(generations, similarities, 'o-', color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    
    # Create second y-axis for success rate
    if successes:
        ax2 = ax1.twinx()
        color = 'tab:red'
        ax2.set_ylabel('Authentication Success', color=color)
        ax2.plot(generations, successes, 's-', color=color)
        ax2.set_yticks([0, 1])
        ax2.set_yticklabels(['Fail', 'Success'])
        ax2.tick_params(axis='y', labelcolor=color)
    
    # Add threshold line if available
    thresholds = []
    for result in results["results"]:
        if "generation" in result and "similarity_threshold" in result:
            thresholds.append(result["similarity_threshold"])
    
    if len(thresholds) == len(generations):
        ax1.plot(generations, thresholds, '--', color='green', label='Threshold')
        ax1.legend()
    
    fig.tight_layout()
    plt.title('Face QR Authentication Performance Over Generations')
    
    # Save the figure
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                              "evolution_test_results", f"authentication_performance_{timestamp}.png")
    plt.savefig(output_path)
    print(f"Saved authentication performance visualization to {output_path}")
    
    return fig

def visualize_phi_harmonic_resonance(results, memory=None):
    """
    Visualize phi-harmonic resonance patterns in the evolution.
    
    Args:
        results: Test results data
        memory: Epigenetic memory data (optional)
    """
    # Extract phi-time values if available
    generations = []
    phi_times = []
    resonances = []
    
    # Extract from test results
    for result in results["results"]:
        if "generation" in result:
            generations.append(result["generation"])
            
            if "phi_time" in result:
                phi_times.append(result["phi_time"])
            
            if "resonance" in result:
                resonances.append(result["resonance"])
    
    if not phi_times and not resonances:
        print("No phi-harmonic data available for visualization.")
        return None
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot phi-time values if available
    if phi_times:
        ax.scatter(generations, phi_times, c='blue', alpha=0.7, label='Phi-Time')
        
        # Add connecting lines with gradient color based on resonance
        if resonances and len(resonances) == len(phi_times):
            for i in range(len(generations)-1):
                ax.plot([generations[i], generations[i+1]], 
                       [phi_times[i], phi_times[i+1]], 
                       color=plt.cm.viridis(resonances[i]), 
                       alpha=0.6, linewidth=2)
    
    # Plot resonance values if available
    if resonances:
        ax_res = ax.twinx()
        ax_res.plot(generations, resonances, 'o-', color='red', label='Resonance')
        ax_res.set_ylabel('Resonance', color='red')
        ax_res.tick_params(axis='y', labelcolor='red')
    
    # Add golden ratio line
    phi = (1 + np.sqrt(5)) / 2
    phi_mod = phi % 1
    ax.axhline(y=phi_mod, color='gold', linestyle='--', 
              label=f'Golden Ratio Mod 1 ({phi_mod:.6f})')
    
    ax.set_xlabel('Generation')
    ax.set_ylabel('Phi-Time')
    ax.set_title('Phi-Harmonic Resonance Patterns in Evolution')
    
    # Add legends
    handles1, labels1 = ax.get_legend_handles_labels()
    if resonances:
        handles2, labels2 = ax_res.get_legend_handles_labels()
        ax.legend(handles1 + handles2, labels1 + labels2, loc='upper left')
    else:
        ax.legend(loc='upper left')
    
    fig.tight_layout()
    
    # Save the figure
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                              "evolution_test_results", f"phi_harmonic_resonance_{timestamp}.png")
    plt.savefig(output_path)
    print(f"Saved phi-harmonic resonance visualization to {output_path}")
    
    return fig

def main():
    """Main function."""
    # Load test results
    results = load_test_results()
    if not results:
        print("No results to visualize.")
        return 1
    
    # Load epigenetic memory
    memory = load_epigenetic_memory()
    
    # Create visualizations
    visualize_parameter_evolution(results, memory)
    visualize_authentication_performance(results)
    visualize_phi_harmonic_resonance(results, memory)
    
    # Show plots if running interactively
    plt.show()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
