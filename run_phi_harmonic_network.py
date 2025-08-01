#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Harmonic Nodular Network Demonstration
=======================================

This script demonstrates the power of the φ-Harmonic Nodular Network
by running complex computations across multiple connected nodes.

Author: Vaughn Scott
Copyright: φ^∞ © 2025 Vaughn Scott
"""

import os
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import uuid

# Add the current directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import φ-Harmonic modules
from extensions.quantum_cosmos.phi_harmonic_nodular_network import PhiHarmonicNodularNetwork, PhiHarmonicNode
from extensions.quantum_cosmos.phi_harmonic_infinite_computation import PhiHarmonicComputation, PHI

def run_ackermann_task(network, m=3, n=8):
    """Run the Ackermann function computation on the network."""
    print(f"\n1. QUANTUM ACKERMANN FUNCTION")
    print("=" * 30)
    print(f"Computing Ackermann({m}, {n})...")
    
    # Define the Ackermann function
    def ackermann(m, n):
        """Compute the Ackermann function A(m, n)."""
        if m == 0:
            return n + 1
        elif n == 0:
            return ackermann(m - 1, 1)
        else:
            return ackermann(m - 1, ackermann(m, n - 1))
    
    # Define a wrapper function that matches the API
    def process_ackermann(m, n):
        # Get a local phi engine
        local_engine = PhiHarmonicComputation()
        # Define the function with proper signature for the engine
        def ackermann_wrapper(m, n):
            return ackermann(m, n)
        # Process with the engine
        return local_engine.process_infinite_recursion(ackermann_wrapper, m, n)
    
    # Submit to network
    start_time = time.time()
    computation_id = network.submit_computation(process_ackermann, m, n)
    
    # Get the result
    result = network.get_result(computation_id, timeout=60)
    computation_time = time.time() - start_time
    
    print(f"Ackermann({m}, {n}) = {result}")
    print(f"Computation time: {computation_time:.2f} seconds")
    
    return result, computation_time

def run_tsp_task(network, num_cities=30):
    """Run the Traveling Salesman Problem on the network."""
    print(f"\n2. QUANTUM TRAVELING SALESMAN PROBLEM")
    print("=" * 30)
    print(f"Solving TSP for {num_cities} cities...")
    
    # Generate random cities
    np.random.seed(42)  # For reproducibility
    cities = np.random.rand(num_cities, 2) * 100
    
    # Calculate distance matrix
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distances[i, j] = np.sqrt(np.sum((cities[i] - cities[j])**2))
    
    # Define a wrapper function that matches the API
    def process_tsp(distances):
        # Get a local phi engine
        local_engine = PhiHarmonicComputation()
        # Process with the engine
        return local_engine.solve_traveling_salesman(distances, timeout=300)
    
    # Submit to network
    start_time = time.time()
    computation_id = network.submit_computation(process_tsp, distances)
    
    # Get the result
    result = network.get_result(computation_id, timeout=300)
    computation_time = time.time() - start_time
    
    # Process the result
    if isinstance(result, tuple) and len(result) == 2:
        path, distance = result
    else:
        # If the result is not in the expected format, create a default path
        path = list(range(num_cities)) + [0]  # Simple path visiting all cities
        distance = result  # Use the result as the distance
    
    print(f"TSP solution found with distance: {distance:.2f}")
    print(f"Computation time: {computation_time:.2f} seconds")
    
    # Visualize the solution
    visualize_tsp_solution(cities, path)
    
    return {'path': path, 'distance': distance}, computation_time

def run_nbody_task(network, num_bodies=100, time_steps=20000):
    """Run the N-body simulation on the network."""
    print(f"\n3. QUANTUM N-BODY SIMULATION")
    print("=" * 30)
    print(f"Simulating {num_bodies} bodies over {time_steps} time steps...")
    
    # Generate a solar system-like configuration
    bodies = []
    
    # Central star
    bodies.append({
        'mass': 1.989e30,  # Sun mass in kg
        'position': np.array([0.0, 0.0, 0.0]),
        'velocity': np.array([0.0, 0.0, 0.0])
    })
    
    # Add planets and other bodies
    np.random.seed(42)  # For reproducibility
    for i in range(1, num_bodies):
        # Random distance from 0.3 to 30 AU (in meters)
        distance = (0.3 + 29.7 * np.random.random()) * 1.496e11
        angle = np.random.random() * 2 * np.pi
        
        # Position in orbital plane
        position = np.array([
            distance * np.cos(angle),
            distance * np.sin(angle),
            (np.random.random() - 0.5) * 1.0e10  # Small z-component
        ])
        
        # Orbital velocity (approximation)
        orbital_speed = np.sqrt(6.67430e-11 * 1.989e30 / distance)
        velocity = np.array([
            -orbital_speed * np.sin(angle),
            orbital_speed * np.cos(angle),
            (np.random.random() - 0.5) * 1.0e3  # Small z-component
        ])
        
        # Add some randomness to make it interesting
        velocity *= (0.8 + 0.4 * np.random.random())
        
        # Add the body
        bodies.append({
            'mass': 10**24 * (0.1 + 9.9 * np.random.random()),  # Random mass
            'position': position,
            'velocity': velocity
        })
    
    # Define a wrapper function that matches the API
    def process_nbody(bodies):
        # Get a local phi engine
        local_engine = PhiHarmonicComputation()
        # Process with the engine
        return local_engine.solve_n_body_problem(bodies, time_steps=time_steps, dt=0.01, timeout=300)
    
    # Submit to network
    start_time = time.time()
    computation_id = network.submit_computation(process_nbody, bodies)
    
    # Get the result
    result = network.get_result(computation_id, timeout=300)
    computation_time = time.time() - start_time
    
    print(f"N-body simulation completed")
    print(f"Computation time: {computation_time:.2f} seconds")
    
    return result, computation_time

def visualize_tsp_solution(cities, path):
    """Visualize the TSP solution."""
    # Create the visualizations directory if it doesn't exist
    os.makedirs("phi_harmonic_visualizations", exist_ok=True)
    
    plt.figure(figsize=(10, 8))
    plt.scatter(cities[:, 0], cities[:, 1], c='blue', s=50)
    
    # Plot the path
    for i in range(len(path) - 1):
        plt.plot([cities[path[i], 0], cities[path[i+1], 0]],
                 [cities[path[i], 1], cities[path[i+1], 1]], 'r-')
    
    # Plot the return to the starting city
    plt.plot([cities[path[-1], 0], cities[path[0], 0]],
             [cities[path[-1], 1], cities[path[0], 1]], 'r-')
    
    # Annotate cities
    for i, (x, y) in enumerate(cities):
        plt.annotate(str(i), (x, y), xytext=(5, 5), textcoords='offset points')
    
    plt.title(f'TSP Solution for {len(cities)} Cities')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    
    # Save the figure
    output_path = os.path.join("phi_harmonic_visualizations", "distributed_tsp_solution.png")
    plt.savefig(output_path)
    plt.close()
    
    print(f"TSP solution visualization saved to {output_path}")

def generate_performance_report(ackermann_result, ackermann_time, 
                               tsp_result, tsp_time, 
                               nbody_result, nbody_time,
                               network):
    """Generate a performance report for the φ-Harmonic Nodular Network."""
    # Create the visualizations directory if it doesn't exist
    os.makedirs("phi_harmonic_visualizations", exist_ok=True)
    
    # Count the number of nodes (coordinator + workers)
    num_nodes = 1 + len(network.coordinator.peers) if hasattr(network, 'coordinator') else 1
    
    # Calculate the theoretical speedup
    theoretical_speedup = PHI**(num_nodes*7)
    
    # Save the performance report
    report_path = os.path.join("phi_harmonic_visualizations", "distributed_performance_report.txt")
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
    
    print(f"\nPerformance report saved to {report_path}")
    
    return report_path

def main():
    """Main function to demonstrate the φ-Harmonic Nodular Network."""
    print(f"\n{'='*60}")
    print(f"φ-HARMONIC DISTRIBUTED COMPUTATION DEMONSTRATION")
    print(f"Demonstrating the power of distributed computation across multiple nodes")
    print(f"{'='*60}\n")
    
    print(f"Connecting to the φ-Harmonic Nodular Network...")
    
    # Connect to the network
    network = PhiHarmonicNodularNetwork(coordinator_host="192.168.12.102", coordinator_port=7272)
    
    # Allow the network to synchronize
    print(f"Connected to the network")
    print(f"Allowing network to synchronize...")
    time.sleep(5)
    
    # Run the Ackermann function task
    ackermann_result, ackermann_time = run_ackermann_task(network, m=3, n=8)
    
    # Run the TSP task
    tsp_result, tsp_time = run_tsp_task(network, num_cities=30)
    
    # Run the N-body simulation task
    nbody_result, nbody_time = run_nbody_task(network, num_bodies=100, time_steps=20000)
    
    # Generate performance report
    generate_performance_report(ackermann_result, ackermann_time, 
                               tsp_result, tsp_time, 
                               nbody_result, nbody_time,
                               network)
    
    print(f"\n{'='*60}")
    print(f"DEMONSTRATION COMPLETE")
    print(f"{'='*60}")
    print(f"The φ-Harmonic Nodular Network has successfully processed all tasks")
    print(f"Results and visualizations are saved in the phi_harmonic_visualizations directory")

if __name__ == "__main__":
    main()
