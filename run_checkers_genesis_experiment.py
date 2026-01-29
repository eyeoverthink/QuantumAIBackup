#!/usr/bin/env python3
"""
Run Checkers Jumping Puzzle Experiment using the Quantum Recursive Genesis System

This script initializes the genesis system with a problem-specific DNA seed
for the Checkers Jumping puzzle and tasks the system with evolving a solution.

By Vaughn Scott (with Cascade Assistant)
"""

import time

# Import the core genesis system and the problem adapter
from quantum_recursive_genesis_system import QuantumRecursiveGenesis
from checkers_problem_adapter import CheckersDNASeed, R_PIECE, B_PIECE, EMPTY

def main():
    """Main function to run the Checkers Jumping experiment."""
    print("--- Quantum Genesis Checkers Jumping Experiment ---")

    # 1. Define the Puzzle
    num_pieces_per_side = 3
    initial_state = ([R_PIECE] * num_pieces_per_side) + [EMPTY] + ([B_PIECE] * num_pieces_per_side)
    target_state = ([B_PIECE] * num_pieces_per_side) + [EMPTY] + ([R_PIECE] * num_pieces_per_side)

    print(f"Initial State: {initial_state}")
    print(f"Target State:  {target_state}")

    # 2. Create the Initial DNA Seed for the Problem
    # This is the specific 'problem block' we plug into the system.
    initial_seed = CheckersDNASeed(initial_state, target_state, generation=0)
    print(f"Initial seed created with fitness: {initial_seed.fitness:.4f}")

    # 3. Initialize the Genesis System
    # The system provides the evolutionary framework.
    genesis_system = QuantumRecursiveGenesis(output_dir="quantum_outputs/checkers_genesis")

    # 4. Create a Fractal Tree with our problem-specific root seed
    tree_id = genesis_system.create_fractal_tree(root_seed=initial_seed)
    print(f"Created fractal tree '{tree_id}' for the checkers problem.")

    # 5. Evolve the system to find a solution
    max_generations = 100
    solution_found = False
    start_time = time.time()

    for gen in range(max_generations):
        print(f"\n--- Generation {gen+1}/{max_generations} ---")
        
        # Evolve the tree by one generation
        genesis_system.evolve_tree(tree_id, generations=1)
        
        # Check for a solution
        best_seed_in_tree = genesis_system._find_best_seed_in_tree(genesis_system.fractal_trees[tree_id])
        best_fitness = best_seed_in_tree.fitness
        
        print(f"Best fitness in tree: {best_fitness:.4f}")

        if best_fitness >= 0.9999:
            print("\n*** Solution Found! ***")
            solution_found = True
            solution_seed = best_seed_in_tree
            break

    end_time = time.time()

    # 6. Report Results
    print("\n--- Experiment Complete ---")
    print(f"Total runtime: {end_time - start_time:.2f} seconds")
    
    if solution_found:
        print("Solution was successfully evolved by the genesis system.")
        # To show the path, we would need to trace back the evolution history.
        # This is a placeholder for showing the final state.
        print(f"Final board state: {solution_seed.board_state}")
        print(f"Achieved fitness: {solution_seed.fitness:.4f} in {solution_seed.generation} generations.")
    else:
        print("Solution not found within the maximum generations.")
        best_seed = genesis_system.find_best_seed()
        if best_seed:
            print(f"Best achieved fitness: {best_seed.fitness:.4f}")
            print(f"Best board state found: {best_seed.board_state}")

    # Generate a final report and visualization
    report_path = genesis_system.generate_report()
    print(f"Generated final system report: {report_path}")
    viz_path = genesis_system.visualize_tree(tree_id)
    print(f"Generated visualization: {viz_path}")

if __name__ == "__main__":
    main()
