#!/usr/bin/env python3
"""
Run Quantum Phi-Harmonic Genome Enhancer for multiple epochs
Tracks generation progression and phi-harmonic metrics across epochs
"""

import os
import sys
import json
import time
import subprocess
from datetime import datetime

# Number of epochs to run
EPOCHS = 5

# Results tracking
results = {
    "start_time": datetime.now().isoformat(),
    "epochs": [],
    "final_generation": 0,
    "initial_generation": 0
}

# Get initial generation
try:
    with open("qr_genome.json", "r") as f:
        genome_data = json.load(f)
    results["initial_generation"] = genome_data.get("generation", 0)
    print(f"Initial generation: {results['initial_generation']}")
except Exception as e:
    print(f"Error reading initial generation: {e}")

# Run epochs
for epoch in range(1, EPOCHS + 1):
    print(f"\n{'='*60}")
    print(f"RUNNING EPOCH {epoch}/{EPOCHS}")
    print(f"{'='*60}")
    
    # Start time for this epoch
    epoch_start = time.time()
    
    # Run quantum phi genome enhancer
    cmd = ["/Users/vaughnscott/CascadeProjects/QuantumAI/.venv/bin/python", 
           "quantum_phi_genome_enhancer.py", 
           "--execute", "--evolve", "--debug"]
    
    try:
        # Execute the command and capture output
        process = subprocess.Popen(
            cmd, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        stdout, stderr = process.communicate()
        
        # Extract key metrics from output
        phi_resonance = None
        quantum_resonance = None
        quantum_complexity = None
        generation = None
        
        for line in stdout.split('\n'):
            if "Phi-resonance:" in line:
                try:
                    phi_resonance = float(line.split(':')[1].strip())
                except:
                    pass
            elif "Quantum resonance:" in line:
                try:
                    quantum_resonance = float(line.split(':')[1].strip())
                except:
                    pass
            elif "Quantum complexity:" in line:
                try:
                    quantum_complexity = float(line.split(':')[1].strip())
                except:
                    pass
            elif "Advanced to generation" in line:
                try:
                    generation = int(line.split("generation")[1].strip())
                except:
                    pass
        
        # Get current generation from genome file
        current_generation = None
        try:
            with open("qr_genome.json", "r") as f:
                genome_data = json.load(f)
            current_generation = genome_data.get("generation", 0)
        except Exception as e:
            print(f"Error reading current generation: {e}")
        
        # Record epoch results
        epoch_results = {
            "epoch": epoch,
            "duration": time.time() - epoch_start,
            "phi_resonance": phi_resonance,
            "quantum_resonance": quantum_resonance,
            "quantum_complexity": quantum_complexity,
            "reported_generation": generation,
            "file_generation": current_generation
        }
        results["epochs"].append(epoch_results)
        
        # Print epoch summary
        print(f"\nEPOCH {epoch} SUMMARY:")
        print(f"  Duration: {epoch_results['duration']:.2f} seconds")
        print(f"  Phi-resonance: {phi_resonance}")
        print(f"  Quantum resonance: {quantum_resonance}")
        print(f"  Quantum complexity: {quantum_complexity}")
        print(f"  Reported generation: {generation}")
        print(f"  File generation: {current_generation}")
        
    except Exception as e:
        print(f"Error in epoch {epoch}: {e}")
        results["epochs"].append({
            "epoch": epoch,
            "error": str(e),
            "duration": time.time() - epoch_start
        })

# Get final generation
try:
    with open("qr_genome.json", "r") as f:
        genome_data = json.load(f)
    results["final_generation"] = genome_data.get("generation", 0)
except Exception as e:
    print(f"Error reading final generation: {e}")

# Calculate total generations added
results["total_generations_added"] = results["final_generation"] - results["initial_generation"]

# Print final summary
print(f"\n{'='*60}")
print(f"FINAL SUMMARY")
print(f"{'='*60}")
print(f"Initial generation: {results['initial_generation']}")
print(f"Final generation: {results['final_generation']}")
print(f"Total generations added: {results['total_generations_added']}")
print(f"Total runtime: {(datetime.now() - datetime.fromisoformat(results['start_time'])).total_seconds():.2f} seconds")

# Save results
with open("phi_harmonic_epochs_results.json", "w") as f:
    json.dump(results, f, indent=2)

print(f"\nResults saved to phi_harmonic_epochs_results.json")
