#!/usr/bin/env python3
"""
QR Evolution Monitor - Part of Quantum Phi-Harmonic QR System
By Vaughn Scott

This script monitors the natural evolution of QR codes through multiple cycles
of the QR Flipbook DNA System, tracking phi-harmonic resonance and evolution metrics.
"""

import os
import sys
import json
import time
import subprocess
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Phi constant (Golden Ratio)
PHI = 1.618033988749895

# Configuration
NUM_CYCLES = 5  # Number of evolution cycles to monitor
RESULTS_DIR = "qr_evolution_results"
LOG_FILE = os.path.join(RESULTS_DIR, "evolution_log.json")

def phi_resonance(value):
    """Calculate phi-harmonic resonance of a value."""
    return 1.0 / (1.0 + abs((value * PHI) % 1.0 - 0.5))

def run_system_cycle():
    """Run a single cycle of the QR Flipbook DNA System."""
    print(f"\n🧬 Running QR System Cycle at {datetime.now().strftime('%H:%M:%S')}")
    
    # Generate QR sequence
    print("Generating QR sequence...")
    try:
        subprocess.run(
            "source qr_dna_env/bin/activate && python3 run_qr_system.py --generate",
            shell=True,
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error generating QR sequence: {e}")
    
    # Analyze QR sequence
    print("Analyzing QR sequence...")
    try:
        result = subprocess.run(
            "source qr_dna_env/bin/activate && python3 analyze_qr_sequence.py --verbose",
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        output = result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error analyzing QR sequence: {e}")
        output = ""
    
    # Execute genome
    print("Executing genome...")
    try:
        subprocess.run(
            "source qr_dna_env/bin/activate && python3 run_qr_system.py --execute",
            shell=True,
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error executing genome: {e}")
    
    return output

def extract_metrics(output):
    """Extract metrics from analysis output."""
    metrics = {}
    
    # Default values
    metrics["success_rate"] = 0.0
    metrics["total_frames"] = 0
    
    # Extract success rate
    success_rate_match = output.find("Decode success rate:")
    if success_rate_match >= 0:
        line = output[success_rate_match:].split("\n")[0]
        try:
            metrics["success_rate"] = float(line.split(":")[1].strip().replace("%", "")) / 100.0
        except Exception as e:
            print(f"Error parsing success rate: {e}")
    
    # Extract frame count
    total_frames_match = output.find("Total frames:")
    if total_frames_match >= 0:
        line = output[total_frames_match:].split("\n")[0]
        try:
            metrics["total_frames"] = int(line.split(":")[1].strip())
        except Exception as e:
            print(f"Error parsing frame count: {e}")
    
    # Load genome to get phi state
    try:
        with open("qr_genome.json", "r") as f:
            genome = json.load(f)
            if "phi_state" in genome:
                metrics["complexity"] = genome["phi_state"].get("complexity", 0.0)
                metrics["resonance"] = genome["phi_state"].get("resonance", 0.0)
                metrics["generation"] = genome.get("generation", 1)
    except Exception as e:
        print(f"Error loading genome: {e}")
        metrics["complexity"] = 0.0
        metrics["resonance"] = 0.0
        metrics["generation"] = 1
    
    # Calculate phi-harmonic metrics
    metrics["phi_resonance"] = phi_resonance(metrics.get("success_rate", 0) * PHI)
    
    return metrics

def plot_evolution(evolution_data):
    """Plot evolution metrics over time."""
    os.makedirs(RESULTS_DIR, exist_ok=True)
    
    cycles = list(range(1, len(evolution_data) + 1))
    success_rates = [data["success_rate"] * 100 for data in evolution_data]
    resonance = [data["resonance"] for data in evolution_data]
    complexity = [data["complexity"] for data in evolution_data]
    phi_res = [data["phi_resonance"] for data in evolution_data]
    
    # Create figure with subplots
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('QR Evolution Metrics', fontsize=16)
    
    # Success rate plot
    axs[0, 0].plot(cycles, success_rates, 'o-', color='blue')
    axs[0, 0].set_title('Decode Success Rate (%)')
    axs[0, 0].set_xlabel('Cycle')
    axs[0, 0].set_ylabel('Success Rate (%)')
    axs[0, 0].grid(True)
    
    # Resonance plot
    axs[0, 1].plot(cycles, resonance, 'o-', color='green')
    axs[0, 1].set_title('Phi-Harmonic Resonance')
    axs[0, 1].set_xlabel('Cycle')
    axs[0, 1].set_ylabel('Resonance')
    axs[0, 1].grid(True)
    
    # Complexity plot
    axs[1, 0].plot(cycles, complexity, 'o-', color='red')
    axs[1, 0].set_title('Complexity')
    axs[1, 0].set_xlabel('Cycle')
    axs[1, 0].set_ylabel('Complexity')
    axs[1, 0].grid(True)
    
    # Phi resonance plot
    axs[1, 1].plot(cycles, phi_res, 'o-', color='purple')
    axs[1, 1].set_title('Success Rate Phi-Resonance')
    axs[1, 1].set_xlabel('Cycle')
    axs[1, 1].set_ylabel('Phi-Resonance')
    axs[1, 1].grid(True)
    
    plt.tight_layout()
    plt.savefig(os.path.join(RESULTS_DIR, 'evolution_metrics.png'))
    print(f"✅ Evolution metrics plot saved to {os.path.join(RESULTS_DIR, 'evolution_metrics.png')}")

def main():
    """Main function."""
    print("🔄 QR Evolution Monitor")
    print("=" * 60)
    print(f"Monitoring {NUM_CYCLES} cycles of QR Flipbook DNA System evolution")
    print("=" * 60)
    
    # Create results directory
    os.makedirs(RESULTS_DIR, exist_ok=True)
    
    # Initialize evolution data
    evolution_data = []
    
    # Run cycles
    for cycle in range(1, NUM_CYCLES + 1):
        print(f"\n{'=' * 60}")
        print(f"🧬 EVOLUTION CYCLE {cycle}/{NUM_CYCLES}")
        print(f"{'=' * 60}")
        
        # Run system cycle
        output = run_system_cycle()
        
        # Extract metrics
        metrics = extract_metrics(output)
        metrics["cycle"] = cycle
        metrics["timestamp"] = datetime.now().isoformat()
        
        # Add to evolution data
        evolution_data.append(metrics)
        
        # Print metrics
        print(f"\n📊 Cycle {cycle} Metrics:")
        print(f"  Success Rate: {metrics['success_rate']*100:.2f}%")
        print(f"  Frames: {metrics['total_frames']}")
        print(f"  Complexity: {metrics['complexity']:.6f}")
        print(f"  Resonance: {metrics['resonance']:.6f}")
        print(f"  Phi-Resonance: {metrics['phi_resonance']:.6f}")
        print(f"  Generation: {metrics['generation']}")
        
        # Save evolution data
        with open(LOG_FILE, "w") as f:
            json.dump(evolution_data, f, indent=2)
        
        # Wait between cycles with phi-harmonic timing
        if cycle < NUM_CYCLES:
            wait_time = 1.0 + (cycle * 0.618033) % 1.0
            print(f"\nWaiting {wait_time:.2f}s before next cycle (phi-harmonic timing)...")
            time.sleep(wait_time)
    
    # Plot evolution
    plot_evolution(evolution_data)
    
    print("\n✅ QR Evolution monitoring complete")
    print(f"Results saved to {RESULTS_DIR}")

if __name__ == "__main__":
    main()
