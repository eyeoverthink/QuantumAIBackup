#!/usr/bin/env python3
"""
Hanoi Orchestrator
------------------

This script orchestrates experiments with the QuantumTowerOfHanoiSolver,
running it with a varying number of disks to analyze its performance and
phi-harmonic resonance characteristics across different complexities.

This system follows the "lego" principle by importing and using the
core solver without modification.
"""

import time
from quantum_tower_of_hanoi_solver import QuantumTowerOfHanoiSolver

def run_hanoi_experiments(min_disks=3, max_disks=8):
    """
    Runs a series of Tower of Hanoi experiments with an increasing number of disks.

    Args:
        min_disks (int): The starting number of disks for the experiments.
        max_disks (int): The maximum number of disks to test.
    """
    print("="*60)
    print("Initializing Hanoi Orchestrator Experiment Suite")
    print(f"Testing solver for {min_disks} to {max_disks} disks.")
    print("="*60)

    for num_disks in range(min_disks, max_disks + 1):
        print(f"\n--- Starting Experiment: {num_disks} Disks ---")
        
        start_time = time.time()
        
        # Instantiate the solver for the current experiment
        # The core solver is used here as a modular, unmodified component.
        solver = QuantumTowerOfHanoiSolver(num_disks=num_disks)
        
        print(f"Solver ID: {solver.solver_id}")
        print("Solving...")
        
        results = solver.solve()
        
        end_time = time.time()
        
        # --- Print Results for the Current Experiment ---
        print("\n" + "-"*10 + f" Results for {num_disks} Disks " + "-"*10)
        print(f"Execution Time: {end_time - start_time:.4f} seconds")
        print(f"Solution Found: {results['solution_found']}")
        print(f"Moves Taken: {results['moves']} (Optimal: {results['optimal_moves']})")
        print(f"Iterations: {results['iterations']}")
        print(f"Best Resonance Achieved: {results['best_resonance']:.6f}")
        print("-" * (32 + len(str(num_disks))))

    print("\n" + "="*60)
    print("Hanoi Orchestrator Experiment Suite Finished.")
    print("="*60)

if __name__ == "__main__":
    # We will test up to 8 disks to keep the execution time reasonable.
    # The complexity grows exponentially (2^n - 1), so higher numbers
    # can take a very long time.
    run_hanoi_experiments(min_disks=3, max_disks=8)
