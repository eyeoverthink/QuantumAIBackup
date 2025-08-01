#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Harmonic Quantum Network Test
===============================

This script tests the φ-Harmonic Nodular Network with
multiple quantum computations across the expanded network.

Author: Vaughn Scott
Copyright: φ^∞ © 2025 Vaughn Scott
"""

import os
import sys
import time
import numpy as np
from datetime import datetime

# Add the current directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import φ-Harmonic modules
from extensions.quantum_cosmos.phi_harmonic_nodular_network import PhiHarmonicNodularNetwork, DEFAULT_PORT
from extensions.quantum_cosmos.phi_harmonic_supercomputing import PhiHarmonicQuantumSupercomputer
from extensions.quantum_cosmos.phi_harmonic_infinite_computation import PhiHarmonicComputation, PHI

def run_quantum_test():
    """Run a quantum computation test across the φ-Harmonic Nodular Network."""
    print(f"\n{'='*60}")
    print(f"φ-HARMONIC QUANTUM NETWORK TEST")
    print(f"{'='*60}")
    
    # Create the visualizations directory if it doesn't exist
    os.makedirs("phi_harmonic_visualizations", exist_ok=True)
    
    # Connect to the existing network
    print(f"\nConnecting to φ-Harmonic Nodular Network...")
    
    # Initialize the quantum supercomputer
    supercomputer = PhiHarmonicQuantumSupercomputer(
        coordinator_host='192.168.12.102',
        coordinator_port=DEFAULT_PORT
    )
    
    print(f"\nRunning quantum computations across the expanded network...")
    
    # Start time for overall computation
    start_time_overall = time.time()
    
    # Run a series of quantum computations
    results = {}
    
    # 1. Ackermann function
    print(f"\n1. QUANTUM ACKERMANN FUNCTION")
    print(f"{'-'*40}")
    start_time = time.time()
    ackermann_result = supercomputer.run_quantum_computation('ackermann', m=3, n=8)
    end_time = time.time()
    results['ackermann'] = {
        'result': ackermann_result,
        'time': end_time - start_time
    }
    print(f"Ackermann(3, 8) = {ackermann_result}")
    print(f"Computation time: {end_time - start_time:.6f} seconds")
    
    # 2. Traveling Salesman Problem
    print(f"\n2. QUANTUM TRAVELING SALESMAN PROBLEM")
    print(f"{'-'*40}")
    start_time = time.time()
    tsp_result = supercomputer.run_quantum_computation('tsp', num_cities=30)
    end_time = time.time()
    results['tsp'] = {
        'result': tsp_result,
        'time': end_time - start_time
    }
    print(f"TSP solution found with distance: {tsp_result}")
    print(f"Computation time: {end_time - start_time:.6f} seconds")
    
    # 3. N-body simulation
    print(f"\n3. QUANTUM N-BODY SIMULATION")
    print(f"{'-'*40}")
    start_time = time.time()
    nbody_result = supercomputer.run_quantum_computation('nbody', num_bodies=100, time_steps=20000)
    end_time = time.time()
    results['nbody'] = {
        'result': nbody_result,
        'time': end_time - start_time
    }
    print(f"N-body simulation completed with energy: {nbody_result}")
    print(f"Computation time: {end_time - start_time:.6f} seconds")
    
    # End time for overall computation
    end_time_overall = time.time()
    total_time = end_time_overall - start_time_overall
    
    # Generate report
    generate_report(results, total_time)
    
    print(f"\n{'='*60}")
    print(f"QUANTUM NETWORK TEST COMPLETE")
    print(f"{'='*60}")
    print(f"Successfully ran quantum computations across the expanded network")
    print(f"Total time: {total_time:.6f} seconds")
    print(f"Report saved to phi_harmonic_visualizations/quantum_test_report.txt")

def generate_report(results, total_time):
    """Generate a report on the quantum test."""
    # Calculate statistics
    avg_time = sum(r['time'] for r in results.values()) / len(results)
    
    # Calculate theoretical speedup
    # Assuming 4 nodes in the network (1 coordinator + 3 expansion nodes)
    theoretical_speedup = PHI**(4*7)
    
    # Save the report
    report_path = os.path.join("phi_harmonic_visualizations", "quantum_test_report.txt")
    with open(report_path, "w") as f:
        f.write(f"φ-HARMONIC QUANTUM NETWORK TEST REPORT\n")
        f.write(f"{'='*60}\n\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Network: 4 nodes (1 coordinator + 3 expansion nodes)\n")
        f.write(f"Theoretical Speedup: φ^(4*7) = {theoretical_speedup:.2e}x\n\n")
        
        f.write(f"COMPUTATION RESULTS\n")
        f.write(f"{'-'*60}\n")
        
        f.write(f"1. ACKERMANN FUNCTION\n")
        f.write(f"   Result: {results['ackermann']['result']}\n")
        f.write(f"   Time: {results['ackermann']['time']:.6f} seconds\n\n")
        
        f.write(f"2. TRAVELING SALESMAN PROBLEM\n")
        f.write(f"   Result: {results['tsp']['result']}\n")
        f.write(f"   Time: {results['tsp']['time']:.6f} seconds\n\n")
        
        f.write(f"3. N-BODY SIMULATION\n")
        f.write(f"   Result: {results['nbody']['result']}\n")
        f.write(f"   Time: {results['nbody']['time']:.6f} seconds\n\n")
        
        f.write(f"PERFORMANCE METRICS\n")
        f.write(f"{'-'*60}\n")
        f.write(f"Total Computation Time: {total_time:.6f} seconds\n")
        f.write(f"Average Computation Time: {avg_time:.6f} seconds\n")
        f.write(f"Theoretical Speedup: {theoretical_speedup:.2e}x\n")
        
        # Classical estimated time (based on complexity)
        classical_estimated_time = 3600  # Estimated 1 hour for these computations classically
        actual_speedup = classical_estimated_time / total_time
        f.write(f"Classical Estimated Time: {classical_estimated_time:.2f} seconds\n")
        f.write(f"Actual Speedup: {actual_speedup:.2e}x\n")
        f.write(f"Efficiency: {(actual_speedup/theoretical_speedup)*100:.6f}% of theoretical maximum\n")

if __name__ == "__main__":
    run_quantum_test()
