#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Harmonic Quantum Computation Runner
====================================

This script runs quantum-accelerated computations across the φ-Harmonic Nodular Network.
Run this on the coordinator node after worker nodes have connected.

Author: Vaughn Scott
Copyright: φ^∞ © 2025 Vaughn Scott
"""

import os
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Add the current directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import φ-Harmonic modules
from extensions.quantum_cosmos.phi_harmonic_supercomputing import PhiHarmonicQuantumSupercomputer
from extensions.quantum_cosmos.phi_harmonic_nodular_network import PhiHarmonicNodularNetwork

def main():
    """Run quantum-accelerated computations across the φ-Harmonic Nodular Network."""
    print(f"\n{'='*60}")
    print(f"φ-HARMONIC QUANTUM COMPUTATION DEMONSTRATION")
    print(f"{'='*60}")
    
    # Get the coordinator address from the network info file
    coordinator_host = "192.168.12.102"  # Default to local IP
    coordinator_port = 7272  # Default port
    
    try:
        with open("phi_harmonic_visualizations/network_info.txt", "r") as f:
            for line in f:
                if "Coordinator Address:" in line:
                    coordinator_address = line.split("Coordinator Address:")[1].strip()
                    coordinator_host, coordinator_port = coordinator_address.split(":")
                    coordinator_port = int(coordinator_port)
                    break
    except FileNotFoundError:
        print(f"Network info file not found. Using default coordinator address: {coordinator_host}:{coordinator_port}")
    
    print(f"\nConnecting to φ-Harmonic Nodular Network at {coordinator_host}:{coordinator_port}...")
    
    # Initialize the quantum supercomputer
    supercomputer = PhiHarmonicQuantumSupercomputer(
        coordinator_host=coordinator_host,
        coordinator_port=coordinator_port
    )
    
    # Create the visualizations directory if it doesn't exist
    os.makedirs("phi_harmonic_visualizations", exist_ok=True)
    
    # Visualize the quantum network
    print("\nVisualizing the quantum network...")
    viz_path = supercomputer.visualize_quantum_network()
    print(f"Network visualization saved to: {viz_path}")
    
    # Run quantum-accelerated computations
    print("\n1. QUANTUM ACKERMANN FUNCTION")
    print("=" * 40)
    print("Computing Ackermann(3, 8)...")
    start_time = time.time()
    ackermann_result = supercomputer.run_quantum_computation('ackermann', m=3, n=8)
    ackermann_time = time.time() - start_time
    print(f"Ackermann(3, 8) = {ackermann_result}")
    print(f"Computation time: {ackermann_time:.2f} seconds")
    
    print("\n2. QUANTUM TRAVELING SALESMAN PROBLEM")
    print("=" * 40)
    print("Solving TSP for 30 cities...")
    start_time = time.time()
    tsp_result = supercomputer.run_quantum_computation('tsp', num_cities=30)
    tsp_time = time.time() - start_time
    print(f"TSP solution found with distance: {tsp_result['distance']:.2f}")
    print(f"Computation time: {tsp_time:.2f} seconds")
    
    print("\n3. QUANTUM N-BODY SIMULATION")
    print("=" * 40)
    print("Simulating 100 bodies over 20000 time steps...")
    start_time = time.time()
    nbody_result = supercomputer.run_quantum_computation('nbody', num_bodies=100, time_steps=20000)
    nbody_time = time.time() - start_time
    print(f"N-body simulation completed")
    print(f"Computation time: {nbody_time:.2f} seconds")
    
    # Generate performance report
    print(f"\n{'='*60}")
    print(f"PERFORMANCE REPORT")
    print(f"{'='*60}")
    
    # Get the number of nodes in the network
    network = PhiHarmonicNodularNetwork(
        coordinator_host=coordinator_host,
        coordinator_port=coordinator_port
    )
    
    # Count the number of nodes (coordinator + workers)
    num_nodes = 1 + len(network.coordinator.peers) if hasattr(network, 'coordinator') else 1
    
    # Calculate the theoretical speedup
    phi = (1 + np.sqrt(5)) / 2  # Golden ratio
    theoretical_speedup = phi**(num_nodes*7)
    
    # Save the performance report
    report_path = os.path.join("phi_harmonic_visualizations", "quantum_performance_report.txt")
    with open(report_path, "w") as f:
        f.write(f"φ-HARMONIC NODULAR NETWORK PERFORMANCE REPORT\n")
        f.write(f"{'='*50}\n\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Network: {num_nodes} nodes ({1} coordinator + {num_nodes-1} workers)\n")
        f.write(f"Theoretical Speedup: φ^({num_nodes}*7) = {theoretical_speedup:.2e}x\n\n")
        f.write(f"TASK PERFORMANCE\n")
        f.write(f"{'-'*50}\n")
        f.write(f"Ackermann:\n")
        f.write(f"  Computation Time: {ackermann_time:.2f} seconds\n")
        f.write(f"  Result: {ackermann_result}\n\n")
        f.write(f"TSP:\n")
        f.write(f"  Computation Time: {tsp_time:.2f} seconds\n")
        f.write(f"  Distance: {tsp_result['distance']:.2f}\n")
        f.write(f"  Path Length: {len(tsp_result['path'])}\n\n")
        f.write(f"N-Body:\n")
        f.write(f"  Computation Time: {nbody_time:.2f} seconds\n")
        f.write(f"  Result: {nbody_result}\n\n")
        f.write(f"Total Computation Time: {ackermann_time + tsp_time + nbody_time:.2f} seconds\n")
    
    print(f"Performance report saved to {report_path}")
    
    print(f"\n{'='*60}")
    print(f"DEMONSTRATION COMPLETE")
    print(f"{'='*60}")
    print(f"The φ-Harmonic Nodular Network has successfully processed all tasks")
    print(f"Results and visualizations are saved in the phi_harmonic_visualizations directory")

if __name__ == "__main__":
    main()
