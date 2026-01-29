#!/usr/bin/env python3
"""
Problem Definition for the Checkers Jumping Puzzle

This script defines the puzzle in a self-contained way for the
Quantum Recursive Genesis System to ingest and solve.

- Defines the problem space (start/end states).
- Defines the rules (valid moves).
- Defines the success metric (Quantum Resonance Triplet fitness).
"""

from decimal import Decimal, getcontext

# --- Constants ---
getcontext().prec = 50
PHI = Decimal('1.6180339887498948482045868343656381177203091798058')
PI = Decimal('3.1415926535897932384626433832795028841971693993751')
E = Decimal('2.71828182845904523536028747135266249775724709369996')
PHI_CONJUGATE = 1 / PHI

R_PIECE = 1
B_PIECE = -1
EMPTY = 0

# --- Problem Space Definition ---
NUM_PIECES_PER_SIDE = 3
INITIAL_STATE = ([R_PIECE] * NUM_PIECES_PER_SIDE) + [EMPTY] + ([B_PIECE] * NUM_PIECES_PER_SIDE)
TARGET_STATE = ([B_PIECE] * NUM_PIECES_PER_SIDE) + [EMPTY] + ([R_PIECE] * NUM_PIECES_PER_SIDE)

# --- Rule Definition ---
def get_valid_moves(state: list) -> list:
    """Generates all valid successor states (moves) from a given state."""
    moves = []
    size = len(state)
    for i in range(size):
        # Slides
        if state[i] != EMPTY and i + 1 < size and state[i+1] == EMPTY:
            new_state = list(state)
            new_state[i], new_state[i+1] = new_state[i+1], new_state[i]
            moves.append(new_state)
        if state[i] != EMPTY and i - 1 >= 0 and state[i-1] == EMPTY:
            new_state = list(state)
            new_state[i], new_state[i-1] = new_state[i-1], new_state[i]
            moves.append(new_state)
        # Jumps
        if i + 2 < size and state[i] != EMPTY and state[i+1] != EMPTY and state[i+2] == EMPTY and state[i] != state[i+1]:
            new_state = list(state)
            new_state[i], new_state[i+2] = new_state[i+2], new_state[i]
            moves.append(new_state)
        if i - 2 >= 0 and state[i] != EMPTY and state[i-1] != EMPTY and state[i-2] == EMPTY and state[i] != state[i-1]:
            new_state = list(state)
            new_state[i], new_state[i-2] = new_state[i-2], new_state[i]
            moves.append(new_state)
    return moves

# --- Success Metric Definition ---
def calculate_fitness(state: list) -> float:
    """Calculates fitness using the Quantum Resonance Triplet (QR)."""
    if state == TARGET_STATE:
        return 1.0

    def _get_positions(s):
        red = sorted([i for i, p in enumerate(s) if p == R_PIECE])
        blue = sorted([i for i, p in enumerate(s) if p == B_PIECE])
        return red, blue

    current_red, current_blue = _get_positions(state)
    target_red, target_blue = _get_positions(TARGET_STATE)

    total_dist = sum(abs(c - t) for c, t in zip(current_red, target_red)) + \
                 sum(abs(c - t) for c, t in zip(current_blue, target_blue))

    max_dist = NUM_PIECES_PER_SIDE * (NUM_PIECES_PER_SIDE + 1) * 2
    if max_dist == 0: return 1.0

    normalized_dist = Decimal(total_dist) / Decimal(max_dist)

    phi_res = (normalized_dist * PHI) % 1
    pi_res = (normalized_dist * PI) % 1
    e_res = (normalized_dist * E) % 1
    combined_res = (phi_res + pi_res + e_res) / 3

    fitness = 1.0 - float(combined_res)
    distance_bonus = (1.0 - float(normalized_dist)) * float(PHI_CONJUGATE)
    
    return min(1.0, max(0.0, (fitness + distance_bonus) / 2.0))
