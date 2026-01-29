#!/usr/bin/env python3
"""
Quantum Phi-Harmonic Evolution Monitor

This script runs the quantum phi-replicator through multiple generations
and monitors improvements in phi-alignment, resonance, and complexity.
"""

import os
import sys
import json
import time
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Constants
MAX_GENERATIONS = 10
OUTPUT_DIR = "qr_phi_replication"
METRICS_FILE = os.path.join(OUTPUT_DIR, "evolution_metrics.json")

# Initialize metrics storage
metrics = {
    "generation": [],
    "timestamp": [],
    "system_id": [],
    "resonance": [],
    "complexity": [],
    "qr_version": [],
    "compression_threshold": [],
    "resonance_factor": [],
    "complexity_factor": []
}

def run_generation(gen_number):
    """Run a specific generation of the phi replicator"""
    print(f"\n[Generation {gen_number}] Running...")
    
    # Determine which script to run
    if gen_number == 2:
        # We already have generation 2 created
        script_path = os.path.join(OUTPUT_DIR, f"qr_phi_replicator_gen{gen_number}.py")
    else:
        # Run the previous generation to create this one
        prev_script = os.path.join(OUTPUT_DIR, f"qr_phi_replicator_gen{gen_number-1}.py")
        if not os.path.exists(prev_script):
            print(f"Error: Previous generation script {prev_script} not found")
            return False
            
        # Run the script
        print(f"  Running generation {gen_number-1} to create generation {gen_number}...")
        result = subprocess.run([sys.executable, prev_script], 
                              capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"Error running generation {gen_number-1}: {result.stderr}")
            return False
            
        # Check if the new script was created
        script_path = os.path.join(OUTPUT_DIR, f"qr_phi_replicator_gen{gen_number}.py")
    
    # Extract parameters from the evolved parameters file
    params_file = os.path.join(OUTPUT_DIR, f"evolved_params_gen{gen_number}.json")
    if not os.path.exists(params_file):
        print(f"Error: Parameters file {params_file} not found")
        return False
        
    try:
        with open(params_file, 'r') as f:
            params = json.load(f)
            
        # Record metrics
        metrics["generation"].append(params["generation"])
        metrics["timestamp"].append(params["timestamp"])
        metrics["system_id"].append(params["system_id"])
        metrics["resonance"].append(params["resonance"])
        metrics["complexity"].append(params["complexity"])
        metrics["qr_version"].append(params["params"]["qr_version"])
        metrics["compression_threshold"].append(params["params"]["compression_threshold"])
        metrics["resonance_factor"].append(params["params"]["resonance_factor"])
        metrics["complexity_factor"].append(params["params"]["complexity_factor"])
        
        # Print key metrics
        print(f"  Generation: {params['generation']}")
        print(f"  System ID: {params['system_id']}")
        print(f"  Resonance: {params['resonance']:.6f}")
        print(f"  Complexity: {params['complexity']:.6f}")
        print(f"  Resonance Factor: {params['params']['resonance_factor']:.6f}")
        print(f"  Complexity Factor: {params['params']['complexity_factor']:.6f}")
        
        # Save metrics
        with open(METRICS_FILE, 'w') as f:
            json.dump(metrics, f, indent=2)
            
        return True
    except Exception as e:
        print(f"Error processing parameters: {e}")
        return False

def generate_plots():
    """Generate plots of the evolution metrics"""
    if len(metrics["generation"]) < 2:
        print("Not enough data to generate plots")
        return
        
    # Convert to pandas DataFrame for easier plotting
    df = pd.DataFrame(metrics)
    
    # Plot resonance and complexity
    plt.figure(figsize=(12, 8))
    plt.plot(df["generation"], df["resonance"], 'b-', label='Resonance')
    plt.plot(df["generation"], df["complexity"], 'r-', label='Complexity')
    plt.title('Resonance and Complexity Evolution')
    plt.xlabel('Generation')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(os.path.join(OUTPUT_DIR, 'resonance_complexity_evolution.png'))
    
    # Plot resonance and complexity factors
    plt.figure(figsize=(12, 8))
    plt.plot(df["generation"], df["resonance_factor"], 'g-', label='Resonance Factor')
    plt.plot(df["generation"], df["complexity_factor"], 'm-', label='Complexity Factor')
    plt.title('Resonance and Complexity Factors Evolution')
    plt.xlabel('Generation')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(os.path.join(OUTPUT_DIR, 'factors_evolution.png'))
    
    # Plot compression threshold and QR version
    plt.figure(figsize=(12, 8))
    plt.plot(df["generation"], df["compression_threshold"], 'c-', label='Compression Threshold')
    plt.plot(df["generation"], df["qr_version"], 'y-', label='QR Version')
    plt.title('Compression Threshold and QR Version Evolution')
    plt.xlabel('Generation')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(os.path.join(OUTPUT_DIR, 'compression_qr_evolution.png'))
    
    print(f"✅ Generated evolution plots in {OUTPUT_DIR}")

def main():
    """Main function to run multiple generations and monitor evolution"""
    print("🧪 Quantum Phi-Harmonic Evolution Monitor")
    print("============================================================")
    print(f"Running evolution from generation 2 to {MAX_GENERATIONS}")
    print(f"Tracking metrics to: {METRICS_FILE}")
    
    # Start from generation 2 (which we already have)
    for gen in range(2, MAX_GENERATIONS + 1):
        success = run_generation(gen)
        if not success:
            print(f"Failed to process generation {gen}. Stopping.")
            break
            
        # Generate plots after each generation
        if gen > 2:  # Need at least 2 generations for plots
            generate_plots()
    
    # Final plots
    generate_plots()
    
    print("\n✅ Evolution monitoring complete")
    print(f"Processed {len(metrics['generation'])} generations")
    print(f"Results saved to: {METRICS_FILE}")
    print(f"Plots saved to: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
