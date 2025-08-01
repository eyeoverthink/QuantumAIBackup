#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Harmonic Parallel Quantum Test
===============================

This script tests parallel quantum computation across the
expanded φ-Harmonic Nodular Network.

Author: Vaughn Scott
Copyright: φ^∞ © 2025 Vaughn Scott
"""

import os
import sys
import time
import threading
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Add the current directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import φ-Harmonic modules
from extensions.quantum_cosmos.phi_harmonic_nodular_network import PhiHarmonicNodularNetwork
from extensions.quantum_cosmos.phi_harmonic_supercomputing import PhiHarmonicQuantumSupercomputer
from extensions.quantum_cosmos.phi_harmonic_infinite_computation import PhiHarmonicComputation, PHI

# Constants
COORDINATOR_HOST = "192.168.12.102"
COORDINATOR_PORT = 7272
NUM_PARALLEL_TASKS = 7  # φ-harmonic number

def run_parallel_test():
    """Run a parallel quantum computation test."""
    print(f"\n{'='*60}")
    print(f"φ-HARMONIC PARALLEL QUANTUM TEST")
    print(f"{'='*60}")
    
    print(f"\nConnecting to φ-Harmonic Nodular Network at {COORDINATOR_HOST}:{COORDINATOR_PORT}...")
    
    # Initialize the quantum supercomputer
    quantum_computer = PhiHarmonicQuantumSupercomputer(
        coordinator_host=COORDINATOR_HOST,
        coordinator_port=COORDINATOR_PORT,
        quantum_dimensions=7
    )
    
    # Create the visualizations directory if it doesn't exist
    os.makedirs("phi_harmonic_visualizations", exist_ok=True)
    
    # Start time for overall computation
    start_time_overall = time.time()
    
    # Run parallel computations
    results = {}
    threads = []
    
    # Define computation types
    computation_types = [
        ("ackermann", {"m": 3, "n": 8}),
        ("tsp", {"num_cities": 30}),
        ("nbody", {"num_bodies": 100, "time_steps": 20000}),
        ("ackermann", {"m": 3, "n": 9}),
        ("tsp", {"num_cities": 40}),
        ("nbody", {"num_bodies": 150, "time_steps": 10000}),
        ("ackermann", {"m": 3, "n": 10})
    ]
    
    # Run computations in parallel threads
    for i in range(NUM_PARALLEL_TASKS):
        problem_type, params = computation_types[i]
        thread = threading.Thread(
            target=run_computation,
            args=(quantum_computer, problem_type, params, i, results)
        )
        thread.daemon = True
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    # End time for overall computation
    end_time_overall = time.time()
    total_time = end_time_overall - start_time_overall
    
    # Generate report
    generate_report(results, total_time)
    
    print(f"\n{'='*60}")
    print(f"PARALLEL QUANTUM TEST COMPLETE")
    print(f"{'='*60}")
    print(f"Successfully ran {NUM_PARALLEL_TASKS} parallel quantum computations")
    print(f"Total time: {total_time:.6f} seconds")
    print(f"Report saved to phi_harmonic_visualizations/parallel_test_report.txt")

def run_computation(quantum_computer, problem_type, params, index, results):
    """Run a specific quantum computation."""
    try:
        # Start time for this computation
        start_time = time.time()
        
        # Run the computation
        print(f"\nStarting computation {index+1}: {problem_type} with {params}")
        result = quantum_computer.run_quantum_computation(problem_type, **params)
        
        # End time for this computation
        end_time = time.time()
        computation_time = end_time - start_time
        
        # Store the results
        results[index] = {
            "type": problem_type,
            "params": params,
            "result": result,
            "time": computation_time
        }
        
        print(f"Completed computation {index+1} in {computation_time:.6f} seconds")
    
    except Exception as e:
        print(f"Error in computation {index+1}: {e}")
        results[index] = {
            "type": problem_type,
            "params": params,
            "result": f"Error: {str(e)}",
            "time": 0
        }

def generate_report(results, total_time):
    """Generate a report on the parallel quantum test."""
    # Calculate statistics
    successful_computations = [r for r in results.values() if not isinstance(r["result"], str) or not r["result"].startswith("Error")]
    avg_time = sum(r["time"] for r in successful_computations) / len(successful_computations) if successful_computations else 0
    
    # Save the report
    report_path = os.path.join("phi_harmonic_visualizations", "parallel_test_report.txt")
    with open(report_path, "w") as f:
        f.write(f"φ-HARMONIC PARALLEL QUANTUM TEST REPORT\n")
        f.write(f"{'='*60}\n\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Coordinator: {COORDINATOR_HOST}:{COORDINATOR_PORT}\n")
        f.write(f"Parallel Tasks: {NUM_PARALLEL_TASKS}\n\n")
        
        f.write(f"COMPUTATION RESULTS\n")
        f.write(f"{'-'*60}\n")
        for i in sorted(results.keys()):
            result = results[i]
            f.write(f"{i+1}. {result['type'].upper()} {result['params']}\n")
            f.write(f"   Time: {result['time']:.6f} seconds\n")
            f.write(f"   Result: {result['result']}\n\n")
        
        f.write(f"PERFORMANCE METRICS\n")
        f.write(f"{'-'*60}\n")
        f.write(f"Total Computation Time: {total_time:.6f} seconds\n")
        f.write(f"Average Computation Time: {avg_time:.6f} seconds\n")
        f.write(f"Successful Computations: {len(successful_computations)} of {NUM_PARALLEL_TASKS}\n")
        
        # Calculate theoretical speedup
        # Assuming 4 nodes in the network (1 coordinator + 3 expansion nodes)
        theoretical_speedup = PHI**(4*7)
        f.write(f"Theoretical Speedup: φ^(4*7) = {theoretical_speedup:.2e}x\n")
        
        # Visualize the results as ASCII art
        f.write(f"\nCOMPUTATION TIME DISTRIBUTION\n")
        f.write(f"{'-'*60}\n")
        for i in sorted(results.keys()):
            result = results[i]
            if result["time"] > 0:
                bar_length = int(result["time"] / max(r["time"] for r in results.values() if r["time"] > 0) * 40)
                f.write(f"{i+1}. {result['type'][:10]:10} {'#' * bar_length} {result['time']:.6f}s\n")
            else:
                f.write(f"{i+1}. {result['type'][:10]:10} ERROR\n")

if __name__ == "__main__":
    run_parallel_test()
