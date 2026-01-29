#!/usr/bin/env python3
"""
Quantum Phi-Harmonic Self-Replicator Entropy Tracker
By Vaughn Scott

This script runs multiple generations of the Quantum Phi-Harmonic Self-Replicator
and tracks entropy changes, resonance patterns, and complexity evolution over time.

It generates visualizations of the phi-harmonic evolution and saves metrics
for analysis of long-term evolutionary patterns.
"""

import os
import sys
import json
import time
import math
import uuid
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import subprocess
import pandas as pd
from typing import Dict, List, Any, Tuple

# Import the QuantumPhiReplicator class
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from qr_phi_replicator import QuantumPhiReplicator, PHI

# Constants
MAX_GENERATIONS = 100  # Number of generations to simulate
OUTPUT_DIR = "qr_phi_replication/entropy_tracking"
METRICS_FILE = os.path.join(OUTPUT_DIR, "evolution_metrics.csv")
PLOTS_DIR = os.path.join(OUTPUT_DIR, "plots")

# Ensure directories exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(PLOTS_DIR, exist_ok=True)


class EntropyTracker:
    """Tracks entropy and other metrics across multiple generations of replication."""
    
    def __init__(self):
        """Initialize the entropy tracker."""
        self.metrics = {
            "generation": [],
            "timestamp": [],
            "resonance": [],
            "complexity": [],
            "entropy": [],
            "phi_alignment": [],
            "qr_version": [],
            "compression_threshold": [],
            "resonance_factor": [],
            "complexity_factor": []
        }
        
        # Load existing metrics if available
        if os.path.exists(METRICS_FILE):
            try:
                df = pd.read_csv(METRICS_FILE)
                for col in df.columns:
                    if col in self.metrics:
                        self.metrics[col] = df[col].tolist()
                print(f"Loaded {len(self.metrics['generation'])} existing generations from {METRICS_FILE}")
            except Exception as e:
                print(f"Error loading existing metrics: {e}")
    
    def calculate_entropy(self, data: Dict[str, Any]) -> float:
        """Calculate information entropy based on system parameters."""
        # Extract key values that contribute to entropy
        resonance = data["resonance"]
        complexity = data["complexity"]
        res_factor = data["params"]["resonance_factor"]
        comp_factor = data["params"]["complexity_factor"]
        
        # Calculate Shannon entropy components
        p1 = resonance
        p2 = complexity
        p3 = res_factor
        p4 = comp_factor
        
        # Normalize probabilities
        total = p1 + p2 + p3 + p4
        if total == 0:
            return 0
            
        p1, p2, p3, p4 = p1/total, p2/total, p3/total, p4/total
        
        # Calculate Shannon entropy: -sum(p_i * log2(p_i))
        entropy = 0
        for p in [p1, p2, p3, p4]:
            if p > 0:  # Avoid log(0)
                entropy -= p * math.log2(p)
        
        return entropy
    
    def calculate_phi_alignment(self, data: Dict[str, Any]) -> float:
        """Calculate how well the system aligns with phi-harmonic principles."""
        # Extract key values
        resonance = data["resonance"]
        complexity = data["complexity"]
        
        # Calculate distance from phi-harmonic points (PHI^-1, PHI^-2)
        dist1 = abs(resonance - (1/PHI))
        dist2 = abs(complexity - (1/PHI))
        dist3 = abs(resonance - (1/PHI**2))
        dist4 = abs(complexity - (1/PHI**2))
        
        # Find minimum distance
        min_dist = min(dist1, dist2, dist3, dist4)
        
        # Convert to alignment score (1 = perfect alignment, 0 = worst)
        alignment = 1 - min_dist
        
        return alignment
    
    def record_metrics(self, data: Dict[str, Any]):
        """Record metrics for a generation."""
        # Calculate entropy and phi-alignment
        entropy = self.calculate_entropy(data)
        phi_alignment = self.calculate_phi_alignment(data)
        
        # Record metrics
        self.metrics["generation"].append(data["generation"])
        self.metrics["timestamp"].append(data["timestamp"])
        self.metrics["resonance"].append(data["resonance"])
        self.metrics["complexity"].append(data["complexity"])
        self.metrics["entropy"].append(entropy)
        self.metrics["phi_alignment"].append(phi_alignment)
        self.metrics["qr_version"].append(data["params"]["qr_version"])
        self.metrics["compression_threshold"].append(data["params"]["compression_threshold"])
        self.metrics["resonance_factor"].append(data["params"]["resonance_factor"])
        self.metrics["complexity_factor"].append(data["params"]["complexity_factor"])
        
        # Save metrics to CSV
        df = pd.DataFrame(self.metrics)
        df.to_csv(METRICS_FILE, index=False)
    
    def generate_plots(self):
        """Generate plots of the metrics."""
        if len(self.metrics["generation"]) < 2:
            print("Not enough data to generate plots")
            return
        
        # Convert to numpy arrays for easier manipulation
        generations = np.array(self.metrics["generation"])
        resonance = np.array(self.metrics["resonance"])
        complexity = np.array(self.metrics["complexity"])
        entropy = np.array(self.metrics["entropy"])
        phi_alignment = np.array(self.metrics["phi_alignment"])
        
        # Plot 1: Resonance and Complexity over generations
        plt.figure(figsize=(12, 8))
        plt.plot(generations, resonance, 'b-', label='Resonance')
        plt.plot(generations, complexity, 'r-', label='Complexity')
        plt.axhline(y=1/PHI, color='g', linestyle='--', alpha=0.5, label=f'Φ⁻¹ ≈ {1/PHI:.6f}')
        plt.axhline(y=1/(PHI**2), color='m', linestyle='--', alpha=0.5, label=f'Φ⁻² ≈ {1/(PHI**2):.6f}')
        plt.title('Resonance and Complexity Evolution')
        plt.xlabel('Generation')
        plt.ylabel('Value')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig(os.path.join(PLOTS_DIR, 'resonance_complexity.png'), dpi=300)
        
        # Plot 2: Entropy over generations
        plt.figure(figsize=(12, 8))
        plt.plot(generations, entropy, 'g-', label='Entropy')
        plt.title('Information Entropy Evolution')
        plt.xlabel('Generation')
        plt.ylabel('Shannon Entropy')
        plt.grid(True, alpha=0.3)
        plt.savefig(os.path.join(PLOTS_DIR, 'entropy.png'), dpi=300)
        
        # Plot 3: Phi-alignment over generations
        plt.figure(figsize=(12, 8))
        plt.plot(generations, phi_alignment, 'c-', label='Phi-Alignment')
        plt.title('Phi-Harmonic Alignment Evolution')
        plt.xlabel('Generation')
        plt.ylabel('Alignment Score (higher is better)')
        plt.grid(True, alpha=0.3)
        plt.savefig(os.path.join(PLOTS_DIR, 'phi_alignment.png'), dpi=300)
        
        # Plot 4: Resonance vs Complexity (phase space)
        plt.figure(figsize=(10, 10))
        plt.scatter(resonance, complexity, c=generations, cmap='viridis', alpha=0.7)
        plt.colorbar(label='Generation')
        plt.axvline(x=1/PHI, color='g', linestyle='--', alpha=0.5, label=f'Φ⁻¹ ≈ {1/PHI:.6f}')
        plt.axhline(y=1/PHI, color='g', linestyle='--', alpha=0.5)
        plt.axvline(x=1/(PHI**2), color='m', linestyle='--', alpha=0.5, label=f'Φ⁻² ≈ {1/(PHI**2):.6f}')
        plt.axhline(y=1/(PHI**2), color='m', linestyle='--', alpha=0.5)
        plt.title('Resonance vs Complexity Phase Space')
        plt.xlabel('Resonance')
        plt.ylabel('Complexity')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig(os.path.join(PLOTS_DIR, 'phase_space.png'), dpi=300)
        
        # Plot 5: Combined metrics
        plt.figure(figsize=(14, 10))
        plt.plot(generations, resonance, 'b-', label='Resonance', alpha=0.7)
        plt.plot(generations, complexity, 'r-', label='Complexity', alpha=0.7)
        plt.plot(generations, entropy, 'g-', label='Entropy', alpha=0.7)
        plt.plot(generations, phi_alignment, 'c-', label='Phi-Alignment', alpha=0.7)
        plt.title('Combined Metrics Evolution')
        plt.xlabel('Generation')
        plt.ylabel('Value')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig(os.path.join(PLOTS_DIR, 'combined_metrics.png'), dpi=300)
        
        print(f"✅ Generated plots in {PLOTS_DIR}")


def run_generation(gen_number: int) -> Dict[str, Any]:
    """Run a single generation of the replicator."""
    # Create a replicator with the current generation number
    replicator = QuantumPhiReplicator(generation=gen_number, debug=False)
    
    # Evolve parameters
    evolved_data = replicator.evolve_parameters()
    
    return evolved_data


def run_multiple_generations(start_gen: int, num_generations: int) -> None:
    """Run multiple generations and track metrics."""
    tracker = EntropyTracker()
    
    print(f"🧪 Quantum Phi-Harmonic Self-Replicator Entropy Tracking")
    print("============================================================")
    print(f"Starting at generation {start_gen}, running {num_generations} generations")
    print(f"Tracking metrics to: {METRICS_FILE}")
    print(f"Generating plots in: {PLOTS_DIR}")
    print("============================================================")
    
    current_gen = start_gen
    end_gen = start_gen + num_generations
    
    # Run the generations
    for gen in range(current_gen, end_gen):
        print(f"\n[Generation {gen}/{end_gen-1}] Running...")
        
        # Run the generation
        evolved_data = run_generation(gen)
        
        # Record metrics
        tracker.record_metrics(evolved_data)
        
        # Print key metrics
        print(f"  Resonance: {evolved_data['resonance']:.6f}")
        print(f"  Complexity: {evolved_data['complexity']:.6f}")
        print(f"  Entropy: {tracker.calculate_entropy(evolved_data):.6f}")
        print(f"  Phi-Alignment: {tracker.calculate_phi_alignment(evolved_data):.6f}")
        
        # Generate plots every 10 generations
        if gen % 10 == 0 or gen == end_gen - 1:
            tracker.generate_plots()
    
    # Final plots
    tracker.generate_plots()
    
    print("\n✅ Entropy tracking complete")
    print(f"Processed {num_generations} generations")
    print(f"Results saved to: {METRICS_FILE}")
    print(f"Plots saved to: {PLOTS_DIR}")


def main():
    """Main function."""
    # Determine starting generation
    start_gen = 1
    if os.path.exists(METRICS_FILE):
        try:
            df = pd.read_csv(METRICS_FILE)
            if not df.empty:
                start_gen = int(df['generation'].max()) + 1
        except Exception:
            pass
    
    # Run multiple generations
    run_multiple_generations(start_gen, MAX_GENERATIONS)


if __name__ == "__main__":
    main()
