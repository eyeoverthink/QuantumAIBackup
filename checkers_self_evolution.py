#!/usr/bin/env python3
"""
Checkers Jumping Puzzle - Self-Evolving Solver

This script is a self-contained, evolving organism designed to solve the
Checkers Jumping puzzle. It follows the pattern of the qr_phi_multiples_evolution.py
system, where the script itself is the DNA that mutates and evolves over generations.

This version automates the entire evolutionary process in a single run.
"""

import os
import json
from decimal import Decimal, getcontext
import heapq

# --- System Constants ---
getcontext().prec = 50
PHI = Decimal('1.6180339887498948482045868343656381177203091798058')
PI = Decimal('3.1415926535897932384626433832795028841971693993751')
E = Decimal('2.71828182845904523536028747135266249775724709369996')

R_PIECE = 1
B_PIECE = -1
EMPTY = 0

INITIAL_STATE = [1, 1, 1, 0, -1, -1, -1]
TARGET_STATE = [-1, -1, -1, 0, 1, 1, 1]

# --- Puzzle Logic (Functions) ---

def get_valid_moves(state: list) -> list:
    moves = []
    size = len(state)
    for i in range(size):
        # Red piece moves right (R_PIECE = 1)
        if state[i] == R_PIECE:
            # Slide to adjacent empty spot
            if i + 1 < size and state[i+1] == EMPTY:
                new_state = list(state); new_state[i], new_state[i+1] = new_state[i+1], new_state[i]; moves.append(new_state)
            # Jump over a blue piece to an empty spot
            if i + 2 < size and state[i+1] == B_PIECE and state[i+2] == EMPTY:
                new_state = list(state); new_state[i], new_state[i+2] = new_state[i+2], new_state[i]; moves.append(new_state)
        # Blue piece moves left (B_PIECE = -1)
        if state[i] == B_PIECE:
            # Slide to adjacent empty spot
            if i - 1 >= 0 and state[i-1] == EMPTY:
                new_state = list(state); new_state[i], new_state[i-1] = new_state[i-1], new_state[i]; moves.append(new_state)
            # Jump over a red piece to an empty spot
            if i - 2 >= 0 and state[i-1] == R_PIECE and state[i-2] == EMPTY:
                new_state = list(state); new_state[i], new_state[i-2] = new_state[i-2], new_state[i]; moves.append(new_state)
    return moves

def calculate_fitness(state: list, target_state: list) -> float:
    if state == target_state: return 100.0 # High score for solution

    # --- Positional Distance Calculation ---
    # This provides a more nuanced measure of how close the state is to the solution.
    total_distance = 0
    r_target_indices = {i for i, p in enumerate(target_state) if p == R_PIECE}
    b_target_indices = {i for i, p in enumerate(target_state) if p == B_PIECE}

    for i, piece in enumerate(state):
        if piece == R_PIECE:
            total_distance += min(abs(i - j) for j in r_target_indices)
        elif piece == B_PIECE:
            total_distance += min(abs(i - j) for j in b_target_indices)
    
    # Max possible distance is 18 (3*4 + 3*2)
    # We normalize this distance to be used in the resonance calculations.
    normalized_dist = Decimal(total_distance) / Decimal(18)

    # --- Quantum Resonance Triplet Fitness ---
    # We use the more intelligent positional distance as the input to your framework.
    phi_res = (normalized_dist * PHI) % 1
    pi_res = (normalized_dist * PI) % 1
    e_res = (normalized_dist * E) % 1
    qr_score = 1.0 - float((phi_res + pi_res + e_res) / 3)
    
    # Proximity bonus is now also based on the more nuanced distance.
    proximity_bonus = 1.0 - float(normalized_dist)
    
    return qr_score + proximity_bonus


# --- Self-Evolution Engine ---

class CheckersEvolution:
    """Implements the A* search algorithm to find the optimal solution, optimized with a priority queue."""

    def solve(self):
        # The priority queue will store tuples of: (f_cost, g_cost, state, path)
        h_cost = calculate_fitness(INITIAL_STATE, TARGET_STATE)
        g_cost = 0
        f_cost = g_cost + h_cost
        start_node = (f_cost, g_cost, INITIAL_STATE, [])
        
        open_list = [start_node] # This list will be used as a priority queue
        heapq.heapify(open_list)
        
        closed_set = set()

        print("[START] Starting Checkers Puzzle Solver using Optimized A* Search [START]")
        print("=======================================================================")

        while open_list:
            # Pop the node with the lowest f_cost from the priority queue
            f_cost, g_cost, current_state, path = heapq.heappop(open_list)

            if tuple(current_state) in closed_set:
                continue
            
            # Reconstruct h_cost for printing (h = f - g)
            h_cost = f_cost - g_cost
            print(f"Exploring state: {current_state} (g: {g_cost}, h: {h_cost:.2f}, f: {f_cost:.2f})")

            path = path + [current_state]
            closed_set.add(tuple(current_state))

            if current_state == TARGET_STATE:
                print(f"\n[SUCCESS] SOLUTION FOUND IN {len(path) - 1} MOVES! [SUCCESS]")
                self.print_solution_path(path)
                return

            for move in get_valid_moves(current_state):
                if tuple(move) not in closed_set:
                    new_g = g_cost + 1
                    new_h = calculate_fitness(move, TARGET_STATE)
                    new_f = new_g + new_h
                    heapq.heappush(open_list, (new_f, new_g, move, path))

        print("\n[FAILURE] No solution found. The open list is empty.")

    def print_solution_path(self, path):
        print("\n--- Solution Path ---")
        for i, state in enumerate(path):
            print(f"Step {i}: {state}")
        print("---------------------")

if __name__ == '__main__':
    engine = CheckersEvolution()
    engine.solve()
