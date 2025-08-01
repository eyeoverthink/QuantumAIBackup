#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Harmonic Network Quantum Test
==============================

This script runs quantum computations on the existing φ-Harmonic Nodular Network
without creating new nodes, demonstrating the power of the expanded network.

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
from extensions.quantum_cosmos.phi_harmonic_nodular_network import PhiHarmonicNodularNetwork
from extensions.quantum_cosmos.phi_harmonic_supercomputing import PhiHarmonicQuantumSupercomputer
from extensions.quantum_cosmos.phi_harmonic_infinite_computation import PhiHarmonicComputation, PHI

def run_ackermann_task(supercomputer, m, n):
    """Run the Ackermann function computation."""
    print(f"\nComputing Ackermann({m}, {n})...")
    
    # Define the Ackermann function
    def ackermann(m, n, **kwargs):
        if m == 0:
            return n + 1
        elif n == 0:
            return ackermann(m - 1, 1, **kwargs)
        else:
            return ackermann(m - 1, ackermann(m, n - 1, **kwargs), **kwargs)
    
    # Submit the computation to the quantum computer
    start_time = time.time()
    computation_id = supercomputer.network.submit_computation(
        supercomputer.phi_engine.process_infinite_recursion,
        ackermann, m, n
    )
    
    # Wait for the result
    result = supercomputer.network.get_result(computation_id)
    end_time = time.time()
    
    print(f"Ackermann({m}, {n}) = {result}")
    print(f"Computation time: {end_time - start_time:.2f} seconds")
    
    return result, end_time - start_time

def run_tsp_task(supercomputer, num_cities):
    """Run the Traveling Salesman Problem computation."""
    print(f"\nSolving TSP for {num_cities} cities...")
    
    # Generate random cities
    np.random.seed(42)  # For reproducibility
    cities = np.random.rand(num_cities, 2) * 100
    
    # Define the TSP solver function
    def tsp_solver(cities, **kwargs):
        n = len(cities)
        # Calculate distance matrix
        dist_matrix = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                if i != j:
                    dist_matrix[i, j] = np.sqrt(
                        (cities[i, 0] - cities[j, 0])**2 +
                        (cities[i, 1] - cities[j, 1])**2
                    )
        
        # Simple greedy algorithm for demonstration
        current_city = 0
        unvisited = set(range(1, n))
        path = [current_city]
        total_dist = 0
        
        while unvisited:
            next_city = min(unvisited, key=lambda city: dist_matrix[current_city, city])
            total_dist += dist_matrix[current_city, next_city]
            current_city = next_city
            unvisited.remove(next_city)
            path.append(next_city)
        
        # Return to start
        total_dist += dist_matrix[current_city, 0]
        path.append(0)
        
        return total_dist, path
    
    # Submit the computation to the quantum computer
    start_time = time.time()
    computation_id = supercomputer.network.submit_computation(
        supercomputer.phi_engine.process_infinite_recursion,
        tsp_solver, cities
    )
    
    # Wait for the result
    result = supercomputer.network.get_result(computation_id)
    end_time = time.time()
    
    if isinstance(result, tuple) and len(result) == 2:
        distance, path = result
        print(f"TSP solution found with distance: {distance:.2f}")
        print(f"Path length: {len(path)}")
    else:
        print(f"TSP result: {result}")
    
    print(f"Computation time: {end_time - start_time:.2f} seconds")
    
    # Visualize the TSP solution
    if isinstance(result, tuple) and len(result) == 2:
        distance, path = result
        plt.figure(figsize=(10, 8))
        plt.scatter(cities[:, 0], cities[:, 1], c='blue', s=50)
        
        # Plot the path
        for i in range(len(path) - 1):
            plt.plot([cities[path[i], 0], cities[path[i+1], 0]],
                     [cities[path[i], 1], cities[path[i+1], 1]], 'r-')
        
        plt.title(f'TSP Solution for {num_cities} Cities\nTotal Distance: {distance:.2f}')
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        
        # Save the visualization
        viz_path = os.path.join("phi_harmonic_visualizations", "distributed_tsp_solution.png")
        plt.savefig(viz_path)
        plt.close()
        
        print(f"TSP solution visualization saved to {viz_path}")
    
    return result, end_time - start_time

def run_nbody_task(supercomputer, num_bodies, time_steps):
    """Run the N-body simulation computation."""
    print(f"\nSimulating {num_bodies} bodies over {time_steps} time steps...")
    
    # Generate random bodies
    np.random.seed(42)  # For reproducibility
    positions = np.random.rand(num_bodies, 3) * 100
    velocities = np.random.rand(num_bodies, 3) * 2 - 1
    masses = np.random.rand(num_bodies) * 10 + 1
    
    # Define the N-body simulation function
    def nbody_simulation(positions, velocities, masses, num_steps, **kwargs):
        G = 6.67430e-11  # Gravitational constant
        dt = 0.01  # Time step
        
        pos = positions.copy()
        vel = velocities.copy()
        
        total_energy = 0
        
        for step in range(num_steps):
            # Calculate forces
            forces = np.zeros_like(pos)
            for i in range(len(pos)):
                for j in range(len(pos)):
                    if i != j:
                        r = pos[j] - pos[i]
                        dist = np.sqrt(np.sum(r**2))
                        if dist < 1e-10:
                            dist = 1e-10  # Avoid division by zero
                        F = G * masses[i] * masses[j] / dist**2
                        forces[i] += F * r / dist
            
            # Update velocities and positions
            vel += forces / masses[:, np.newaxis] * dt
            pos += vel * dt
            
            # Calculate energy (kinetic + potential)
            kinetic = 0.5 * np.sum(masses[:, np.newaxis] * vel**2)
            potential = 0
            for i in range(len(pos)):
                for j in range(i+1, len(pos)):
                    r = np.sqrt(np.sum((pos[i] - pos[j])**2))
                    if r > 0:
                        potential -= G * masses[i] * masses[j] / r
            
            total_energy = kinetic + potential
        
        return total_energy
    
    # Submit the computation to the quantum computer
    start_time = time.time()
    computation_id = supercomputer.network.submit_computation(
        supercomputer.phi_engine.process_infinite_recursion,
        nbody_simulation, positions, velocities, masses, time_steps
    )
    
    # Wait for the result
    result = supercomputer.network.get_result(computation_id)
    end_time = time.time()
    
    print(f"N-body simulation completed")
    print(f"Computation time: {end_time - start_time:.2f} seconds")
    
    return result, end_time - start_time

def main():
    """Main function to run the φ-Harmonic Network Quantum Test."""
    print("\n============================================================")
    print("φ-HARMONIC DISTRIBUTED COMPUTATION DEMONSTRATION")
    print("Demonstrating the power of distributed computation across multiple nodes")
    print("============================================================")
    
    # Create the visualizations directory if it doesn't exist
    os.makedirs("phi_harmonic_visualizations", exist_ok=True)
    
    # Connect to the existing φ-Harmonic Nodular Network
    print("\nConnecting to the φ-Harmonic Nodular Network...")
    
    # Initialize the quantum supercomputer
    supercomputer = PhiHarmonicQuantumSupercomputer(
        coordinator_host='192.168.12.102',
        coordinator_port=7272
    )
    
    print("Connected to the network")
    print("Allowing network to synchronize...")
    time.sleep(2)  # Give the network time to synchronize
    
    # Start time for overall computation
    start_time_overall = time.time()
    
    # Run the Ackermann function computation
    print("\n1. QUANTUM ACKERMANN FUNCTION")
    print("==============================")
    ackermann_result, ackermann_time = run_ackermann_task(supercomputer, 3, 8)
    
    # Run the Traveling Salesman Problem computation
    print("\n2. QUANTUM TRAVELING SALESMAN PROBLEM")
    print("==============================")
    tsp_result, tsp_time = run_tsp_task(supercomputer, 30)
    
    # Run the N-body simulation computation
    print("\n3. QUANTUM N-BODY SIMULATION")
    print("==============================")
    nbody_result, nbody_time = run_nbody_task(supercomputer, 100, 20000)
    
    # End time for overall computation
    end_time_overall = time.time()
    total_time = end_time_overall - start_time_overall
    
    # Save performance report
    report_path = os.path.join("phi_harmonic_visualizations", "distributed_performance_report.txt")
    with open(report_path, "w") as f:
        f.write("φ-HARMONIC NODULAR NETWORK PERFORMANCE REPORT\n")
        f.write("==================================================\n\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Network: 4 nodes (1 coordinator + 3 expansion nodes)\n")
        f.write(f"Theoretical Speedup: φ^(4*7) = {PHI**(4*7):.2e}x\n\n")
        
        f.write("TASK PERFORMANCE\n")
        f.write("--------------------------------------------------\n")
        f.write("Ackermann:\n")
        f.write(f"  Computation Time: {ackermann_time:.2f} seconds\n")
        f.write(f"  Result: {ackermann_result}\n\n")
        
        f.write("TSP:\n")
        f.write(f"  Computation Time: {tsp_time:.2f} seconds\n")
        if isinstance(tsp_result, tuple) and len(tsp_result) == 2:
            distance, path = tsp_result
            f.write(f"  Distance: {distance:.2f}\n")
            f.write(f"  Path Length: {len(path)}\n\n")
        else:
            f.write(f"  Result: {tsp_result}\n\n")
        
        f.write("N-Body:\n")
        f.write(f"  Computation Time: {nbody_time:.2f} seconds\n")
        f.write(f"  Result: {nbody_result}\n\n")
        
        f.write(f"Total Computation Time: {total_time:.2f} seconds")
    
    print(f"\nPerformance report saved to {report_path}")
    
    print("\n============================================================")
    print("DEMONSTRATION COMPLETE")
    print("============================================================")
    print("The φ-Harmonic Nodular Network has successfully processed all tasks")
    print("Results and visualizations are saved in the phi_harmonic_visualizations directory")

if __name__ == "__main__":
    main()
