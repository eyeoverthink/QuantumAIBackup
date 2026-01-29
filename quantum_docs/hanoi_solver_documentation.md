# Tower of Hanoi - Self-Evolving Solver

## 1. Overview

This document details the implementation of a self-contained, autonomous solver for the classic Tower of Hanoi puzzle. This component follows the 'lego block' design philosophy established with the Checkers Puzzle Solver, creating another powerful problem-solving module for the Quantum Recursive Genesis System.

The solver uses the A* search algorithm, guided by a phi-harmonic fitness function, to efficiently find the optimal solution.

## 2. Core Components (`hanoi_self_evolution.py`)

### a. State Representation

- The state of the puzzle is represented by a tuple containing three inner tuples. Each inner tuple represents a peg, and the numbers within represent the disks on that peg.
- **Example (3 Disks):** `([3, 2, 1], [], [])` represents the initial state where all disks are on the first peg.
- This tuple-based structure is immutable and hashable, making it ideal for use in the `closed_set` of the A* search algorithm.

### b. Move Generation (`get_valid_moves`)

- This function calculates all possible legal moves from a given state.
- It adheres to the two fundamental rules of the Tower of Hanoi:
  1. Only one disk can be moved at a time.
  2. A larger disk cannot be placed on top of a smaller disk.

### c. Phi-Harmonic Fitness Function (`calculate_fitness`)

- This function serves as the heuristic `h(n)` for the A* algorithm.
- **Heuristic:** The primary heuristic value is the number of disks that are not correctly stacked on the final target peg. A disk is considered correctly stacked if it is on the target peg and all larger disks are correctly stacked below it.
- **Quantum Resonance:** This heuristic value is normalized and then processed through the Quantum Resonance Triplet (φ, π, e). The resulting score serves as a sophisticated tie-breaker, guiding the search with phi-harmonic principles when multiple paths have the same primary heuristic cost.

### d. A* Search Algorithm (`a_star_search`)

- The solver employs the same optimized A* search implementation used in the checkers solver.
- It uses a priority queue (`heapq`) to efficiently select the most promising state to explore next, based on the `f_score` (where `f = g + h`).
- `g_score`: The actual cost (number of moves) from the initial state.
- `h_score`: The estimated cost to the goal, provided by the `calculate_fitness` function.

## 3. Execution

- The script can be run directly using `python3 hanoi_self_evolution.py`.
- Upon execution, it will find and print the optimal sequence of moves to solve the puzzle for the configured number of disks (`NUM_DISKS`).

## 4. Next Steps

- Once validated, this solver will be integrated into the QR code tasking framework with a new task type, `run_hanoi_solver`, further expanding the system's capabilities.
