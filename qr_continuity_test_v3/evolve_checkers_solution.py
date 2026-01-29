#!/usr/bin/env python3
"""
Evolve a solution for the Checkers Jumping Puzzle using the Quantum Recursive Genesis System.

This script acts as the main entry point to task the system with a specific problem.
It bypasses the default self-improvement loop and instead directs the engine to
evolve a solution to the puzzle defined in the CheckersDNASeed.
"""

import os
import sys

# Ensure the project root is in the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from quantum_recursive_genesis_system import QuantumRecursiveGenesis
from checkers_problem_adapter import CheckersDNASeed, INITIAL_STATE, TARGET_STATE

def main():
    print("\n🧩 Evolving a Solution for the Checkers Jumping Puzzle 🧩")
    print("============================================================")

    # 1. Initialize the Genesis System
    # We point it to a dedicated directory for this experiment's output.
    genesis_system = QuantumRecursiveGenesis(output_dir="checkers_evolution_run")
    print(f"Genesis System initialized. Output will be saved to: {genesis_system.output_dir}")

    # 2. Create the initial DNA seed for the puzzle
    # This is the starting state of the puzzle, our 'Adam' seed.
    initial_seed = CheckersDNASeed(initial_state=INITIAL_STATE, target_state=TARGET_STATE)
    print(f"Initial DNA Seed created with fitness: {initial_seed.fitness:.6f}")

    # 3. Create the Fractal Tree with our puzzle seed as the root
    # The tree will grow as the system explores new solutions (moves).
    fractal_tree = genesis_system.create_fractal_tree(initial_seed)
    print("Fractal Tree created with the puzzle's initial state as the root.")

    # 4. Evolve the solution
    # We instruct the system to evolve the tree for a number of generations.
    # The system will use the fitness function defined in our CheckersDNASeed.
    num_generations = 250
    print(f"\n🌱 Starting evolution for {num_generations} generations...")
    solution_node = genesis_system.evolve_tree(fractal_tree, generations=num_generations)

    # 5. Report the results
    print("\n🏆 Evolution Complete 🏆")
    if solution_node:
        print(f"Solution found at generation {solution_node.seed.generation}!")
        print(f"Final State: {solution_node.seed.dna}")
        print(f"Final Fitness: {solution_node.seed.fitness:.6f}")
        
        # Generate a report and visualization of the solution path
        report_path = genesis_system.generate_solution_report(solution_node)
        print(f"Solution report saved to: {report_path}")
        
        viz_path = genesis_system.visualize_solution_path(solution_node)
        print(f"Solution visualization saved to: {viz_path}")
    else:
        print("No solution found within the given generations.")
        print("The best-found node is at the tip of the most promising branch.")

if __name__ == "__main__":
    main()
