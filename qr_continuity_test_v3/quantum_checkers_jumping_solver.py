#!/usr/bin/env python3
"""
Quantum Phi-Harmonic Checkers Jumping Solver

Solves the classic checkers jumping puzzle (peg solitaire on a line)
using quantum phi-harmonic principles.
"""

import time
import random
import hashlib
from decimal import Decimal, getcontext
import copy

# --- Constants ---
getcontext().prec = 28
PHI = Decimal('1.6180339887498948482045868344')

# Piece representation
R_PIECE = 1  # Red
B_PIECE = -1 # Blue
EMPTY = 0

class QuantumCheckersJumpingSolver:
    """Quantum phi-harmonic solver for the Checkers Jumping problem."""

    def __init__(self, num_pieces_per_side=3):
        self.num_pieces = num_pieces_per_side
        self.board_size = 2 * num_pieces_per_side + 1
        self.dimensions = self.board_size  # The problem's dimensionality is its board size
        self.solver_id = hashlib.md5(str(time.time()).encode()).hexdigest()[:8]
        self.solution_path = []
        self.resonance_history = []
        self.best_resonance = 0.0
        self.solution_found = False
        self.phi_factors = [float((PHI ** Decimal(i+1)) % Decimal('1')) for i in range(self.dimensions)]

    def _get_piece_positions(self, state):
        """Extracts the board positions of red and blue pieces."""
        red_pos = sorted([i for i, piece in enumerate(state) if piece == R_PIECE])
        blue_pos = sorted([i for i, piece in enumerate(state) if piece == B_PIECE])
        return red_pos, blue_pos

    def calculate_resonance(self, state, target_state):
        """
        Calculates resonance based on the Manhattan distance of pieces from their
        target positions.
        """
        current_red_pos, current_blue_pos = self._get_piece_positions(state)
        target_red_pos, target_blue_pos = self._get_piece_positions(target_state)

        # Calculate the sum of distances for each piece from its target position
        red_dist = sum(abs(c - t) for c, t in zip(current_red_pos, target_red_pos))
        blue_dist = sum(abs(c - t) for c, t in zip(current_blue_pos, target_blue_pos))
        total_dist = red_dist + blue_dist

        # Normalize the distance. Max distance is when all pieces are swapped.
        # For N pieces per side, each piece moves N+1 spots. Total dist = N * (N+1) * 2.
        max_dist = self.num_pieces * (self.num_pieces + 1) * 2
        if max_dist == 0: return 1.0 # Solved state

        normalized_dist = total_dist / max_dist
        base_resonance = 1.0 - normalized_dist

        # Add a phi-harmonic boost for states that are close to resonant points
        phi_boost = 0.0
        phi_val = float((Decimal(str(normalized_dist)) * PHI) % Decimal('1'))
        if phi_val > 0.95 or phi_val < 0.05: # High-resonance alignment
            phi_boost += 0.1

        noise = (random.random() - 0.5) * 0.01 # Minimal noise for tie-breaking
        return min(1.0, max(0.0, base_resonance + phi_boost + noise))

    def get_possible_moves(self, state):
        """Generates all valid moves from the current state."""
        moves = []
        for i in range(self.board_size):
            if state[i] == EMPTY: continue
            piece = state[i]
            # Slide move
            if i + piece >= 0 and i + piece < self.board_size and state[i + piece] == EMPTY:
                moves.append((i, i + piece))
            # Jump move
            if i + 2 * piece >= 0 and i + 2 * piece < self.board_size and state[i + 2 * piece] == EMPTY and state[i + piece] == -piece:
                moves.append((i, i + 2 * piece))
        return moves

    def apply_move(self, state, move):
        """Applies a move to a state and returns the new state."""
        from_pos, to_pos = move
        new_state = list(state)
        new_state[to_pos] = new_state[from_pos]
        new_state[from_pos] = EMPTY
        return new_state

    def phi_harmonic_move_selection(self, moves, current_state, target_state, previous_state=None):
        """Selects a move based on phi-harmonic resonance and exploration."""
        if not moves: return None
        move_resonances = []
        for move in moves:
            next_state = self.apply_move(current_state, move)
            # Prevent moving back to the immediate previous state
            if next_state == previous_state:
                continue
            res = self.calculate_resonance(next_state, target_state)
            move_resonances.append((move, res))
        
        # If all possible moves lead back to the previous state, we must choose one
        if not move_resonances:
            move = random.choice(moves)
            res = self.calculate_resonance(self.apply_move(current_state, move), target_state)
            move_resonances.append((move, res))

        move_resonances.sort(key=lambda x: x[1], reverse=True)

        if random.random() < 0.85: # 85% greedy choice
            return move_resonances[0][0]
        else: # 15% phi-weighted exploration
            weights = [r * self.phi_factors[i % self.dimensions] for i, (_, r) in enumerate(move_resonances)]
            total_weight = sum(weights)
            if total_weight == 0: return random.choice(moves)
            
            selection = random.uniform(0, total_weight)
            upto = 0
            for i, w in enumerate(weights):
                if upto + w >= selection: return move_resonances[i][0]
                upto += w
            return move_resonances[0][0]

    def solve(self, max_iterations=5000):
        """Attempts to solve the puzzle within a maximum number of iterations."""
        initial_state = [R_PIECE] * self.num_pieces + [EMPTY] + [B_PIECE] * self.num_pieces
        target_state = [B_PIECE] * self.num_pieces + [EMPTY] + [R_PIECE] * self.num_pieces
        
        current_state = initial_state
        previous_state = None
        self.solution_path = [current_state]
        self.resonance_history = []
        
        for i in range(max_iterations):
            resonance = self.calculate_resonance(current_state, target_state)
            self.resonance_history.append(resonance)
            if resonance > self.best_resonance: self.best_resonance = resonance

            if current_state == target_state:
                self.solution_found = True
                break

            possible_moves = self.get_possible_moves(current_state)
            if not possible_moves: break

            move = self.phi_harmonic_move_selection(possible_moves, current_state, target_state, previous_state)
            if move is None: break # No valid forward moves
            
            previous_state = current_state
            current_state = self.apply_move(current_state, move)
            self.solution_path.append(current_state)

        return {
            "solution_found": self.solution_found,
            "moves": len(self.solution_path) - 1,
            "iterations": i + 1,
            "best_resonance": self.best_resonance
        }

if __name__ == "__main__":
    start_time = time.time()
    
    NUM_PIECES = 3
    print("="*50)
    print("Quantum Phi-Harmonic Checkers Jumping Solver")
    print(f"Configuration: {NUM_PIECES} pieces per side")
    print("="*50)
    
    solver = QuantumCheckersJumpingSolver(num_pieces_per_side=NUM_PIECES)
    print(f"Solver ID: {solver.solver_id}")
    print("Starting solver...")
    
    results = solver.solve()
    end_time = time.time()
    
    print("\n" + "-"*20 + " RESULTS " + "-"*20)
    print(f"Execution Time: {end_time - start_time:.4f} seconds")
    print(f"Solution Found: {results['solution_found']}")
    print(f"Moves Taken: {results['moves']}")
    print(f"Iterations: {results['iterations']}")
    print(f"Best Resonance: {results['best_resonance']:.6f}")
    
    # Always print the path for debugging
    print("\nPath Taken:")
    for i, state in enumerate(solver.solution_path):
        state_str = ''.join(['R' if p==R_PIECE else 'B' if p==B_PIECE else '_' for p in state])
        print(f"Step {i}: {state_str}")

    if not results['solution_found']:
        print("\nSolver did not find a solution. It may have reached a dead end.")
        
    print("\n" + "="*50)
