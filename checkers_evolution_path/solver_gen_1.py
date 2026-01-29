#!/usr/bin/env python3
"""
Checkers Jumping Puzzle - Self-Evolving Solver

This script is a self-contained, evolving organism designed to solve the
Checkers Jumping puzzle. It follows the pattern of the qr_phi_multiples_evolution.py
system, where the script itself is the DNA that mutates and evolves over generations.

Each generation represents one move in the puzzle. The script will:
1.  Evaluate its current state.
2.  Select the best next move using a phi-harmonic fitness function.
3.  Generate a new version of this script with the updated board state.
4.  Encode the new script into a QR code, representing the next generation.
"""

import os
import json
import time
import random
from decimal import Decimal, getcontext

# --- Core Configuration & Constants ---
# This section is the 'genetic code' that will be modified by evolution.

GENERATION = 1
CURRENT_STATE_STR = '[1, 0, 1, 1, -1, -1, -1]'
MOVE_HISTORY = [[1, 1, 1, 0, -1, -1, -1]]

# --- System Constants ---
getcontext().prec = 50
PHI = Decimal('1.6180339887498948482045868343656381177203091798058')
PI = Decimal('3.1415926535897932384626433832795028841971693993751')
E = Decimal('2.71828182845904523536028747135266249775724709369996')

R_PIECE = 1
B_PIECE = -1
EMPTY = 0

TARGET_STATE = [-1, -1, -1, 0, 1, 1, 1]

# --- Puzzle Logic (Functions) ---

def get_valid_moves(state: list) -> list:
    moves = []
    size = len(state)
    for i in range(size):
        # Slides
        if i + 1 < size and state[i+1] == EMPTY and state[i] == R_PIECE:
            new_state = list(state); new_state[i], new_state[i+1] = new_state[i+1], new_state[i]; moves.append(new_state)
        if i - 1 >= 0 and state[i-1] == EMPTY and state[i] == B_PIECE:
            new_state = list(state); new_state[i], new_state[i-1] = new_state[i-1], new_state[i]; moves.append(new_state)
        # Jumps
        if i + 2 < size and state[i+2] == EMPTY and state[i] == R_PIECE:
            new_state = list(state); new_state[i], new_state[i+2] = new_state[i+2], new_state[i]; moves.append(new_state)
        if i - 2 >= 0 and state[i-2] == EMPTY and state[i] == B_PIECE:
            new_state = list(state); new_state[i], new_state[i-2] = new_state[i-2], new_state[i]; moves.append(new_state)
    return moves

def calculate_fitness(state: list, target_state: list) -> float:
    if state == target_state: return 1.0
    dist = sum(1 for i, p in enumerate(state) if p != target_state[i])
    normalized_dist = Decimal(dist) / Decimal(len(state))
    phi_res = (normalized_dist * PHI) % 1
    pi_res = (normalized_dist * PI) % 1
    e_res = (normalized_dist * E) % 1
    combined_res = (phi_res + pi_res + e_res) / 3
    return 1.0 - float(combined_res)

# --- Self-Evolution Engine ---

class CheckersEvolution:
    def __init__(self, output_dir='checkers_evolution_path'):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.current_state = json.loads(CURRENT_STATE_STR)

    def evolve(self):
        print(f"\n🧬 Generation {GENERATION}: {self.current_state}")

        if self.current_state == TARGET_STATE:
            print("\n🎉🎉🎉 SOLUTION FOUND! 🎉🎉🎉")
            print(f"Move history: {MOVE_HISTORY}")
            return

        possible_moves = get_valid_moves(self.current_state)
        if not possible_moves:
            print("Dead end. No further moves possible.")
            return

        # Select the best move using our quantum fitness function
        scored_moves = [(move, calculate_fitness(move, TARGET_STATE)) for move in possible_moves if move not in MOVE_HISTORY]
        if not scored_moves:
            print("Dead end. All moves lead to previously visited states.")
            return

        best_move = max(scored_moves, key=lambda item: item[1])[0]
        print(f"Best next move found with fitness: {max(scored_moves, key=lambda item: item[1])[1]:.4f}")

        # Create the next generation of the solver script
        self.create_next_generation_script(best_move)

    def create_next_generation_script(self, next_state):
        with open(__file__, 'r') as f:
            source_code = f.read()

        # Evolve the genetic code
        new_source = source_code.replace(f"GENERATION = {GENERATION}", f"GENERATION = {GENERATION + 1}")
        new_source = new_source.replace(f"CURRENT_STATE_STR = '{json.dumps(self.current_state)}'", f"CURRENT_STATE_STR = '{json.dumps(next_state)}'")
        
        new_history = MOVE_HISTORY + [self.current_state]
        new_source = new_source.replace(f"MOVE_HISTORY = {MOVE_HISTORY}", f"MOVE_HISTORY = {new_history}")

        script_filename = os.path.join(self.output_dir, f'solver_gen_{GENERATION + 1}.py')
        with open(script_filename, 'w') as f:
            f.write(new_source)
        
        print(f"Evolved to next generation: {script_filename}")

if __name__ == '__main__':
    engine = CheckersEvolution()
    engine.evolve()
