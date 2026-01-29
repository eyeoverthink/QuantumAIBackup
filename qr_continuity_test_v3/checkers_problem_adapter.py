#!/usr/bin/env python3
"""
Checkers Problem Adapter for the Quantum Recursive Genesis System

This module adapts the Checkers Jumping puzzle to the genesis framework.
It defines a specialized QuantumDNASeed for the puzzle, where:
- The 'DNA' represents the board state.
- 'Mutation' is a valid move in the puzzle.
- 'Fitness' is calculated using the Quantum Resonance Triplet (phi, pi, e).

By Vaughn Scott (with Cascade Assistant)
"""

import random
import copy
from decimal import Decimal, getcontext

# Import the base class without modification
from qr_continuity_test_v3.quantum_recursive_genesis import QuantumDNASeed

# --- Core Mathematical Constants ---
getcontext().prec = 50
PHI = Decimal('1.6180339887498948482045868343656381177203091798058')
PI = Decimal('3.1415926535897932384626433832795028841971693993751')
E = Decimal('2.71828182845904523536028747135266249775724709369996')

# --- Piece Representation ---
R_PIECE = 1  # Red
B_PIECE = -1 # Blue
EMPTY = 0

class CheckersDNASeed(QuantumDNASeed):
    """A QuantumDNASeed specialized for the Checkers Jumping puzzle."""

    def __init__(self, board_state: list, target_state: list, generation: int = 0):
        """Initializes the seed with a specific board state."""
        self.board_state = board_state
        self.target_state = target_state
        self.num_pieces = sum(1 for p in board_state if p != EMPTY) // 2

        # Convert board state to a string for the base class
        dna_string = self._state_to_dna(board_state)
        
        # Call parent constructor with a placeholder phi_alignment
        super().__init__(dna_string=dna_string, phi_alignment=random.random(), generation=generation)

        # Override the generic fitness with our problem-specific QR fitness
        self.fitness = self._calculate_qr_fitness()

    def _state_to_dna(self, state: list) -> str:
        """Converts a board state list into a string representation."""
        return '_'.join(['R' if p == R_PIECE else 'B' if p == B_PIECE else 'E' for p in state])

    def _get_piece_positions(self, state: list) -> tuple[list, list]:
        """Gets the sorted positions of red and blue pieces."""
        red_pos = sorted([i for i, p in enumerate(state) if p == R_PIECE])
        blue_pos = sorted([i for i, p in enumerate(state) if p == B_PIECE])
        return red_pos, blue_pos

    def _calculate_qr_fitness(self) -> float:
        """Calculates fitness using the Quantum Resonance Triplet (QR)."""
        if self.board_state == self.target_state:
            return 1.0

        current_red_pos, current_blue_pos = self._get_piece_positions(self.board_state)
        target_red_pos, target_blue_pos = self._get_piece_positions(self.target_state)

        # Calculate Manhattan distance
        total_dist = sum(abs(c - t) for c, t in zip(current_red_pos, target_red_pos)) + \
                     sum(abs(c - t) for c, t in zip(current_blue_pos, target_blue_pos))

        # Max distance is when all pieces are on the opposite side
        max_dist = self.num_pieces * (self.num_pieces + 1) * 2
        if max_dist == 0:
            return 1.0

        normalized_dist = Decimal(total_dist) / Decimal(max_dist)

        # Quantum Resonance Triplet Calculation
        phi_res = (normalized_dist * PHI) % 1
        pi_res = (normalized_dist * PI) % 1
        e_res = (normalized_dist * E) % 1

        # Combined resonance (lower is better)
        combined_res = (phi_res + pi_res + e_res) / 3

        # Fitness is the inverse of resonance (higher is better)
        fitness = 1.0 - float(combined_res)
        
        # Add a bonus for being closer to the goal, scaled by phi
        distance_bonus = (1.0 - float(normalized_dist)) * float(PHI_CONJUGATE)
        
        return min(1.0, max(0.0, (fitness + distance_bonus) / 2.0))

    def _generate_moves(self) -> list:
        """Generates all valid successor states (moves)."""
        moves = []
        board = self.board_state
        size = len(board)
        for i in range(size):
            # Slides
            if board[i] != EMPTY and i + 1 < size and board[i+1] == EMPTY:
                new_board = list(board)
                new_board[i], new_board[i+1] = new_board[i+1], new_board[i]
                moves.append(new_board)
            if board[i] != EMPTY and i - 1 >= 0 and board[i-1] == EMPTY:
                new_board = list(board)
                new_board[i], new_board[i-1] = new_board[i-1], new_board[i]
                moves.append(new_board)
            # Jumps
            if i + 2 < size and board[i] != EMPTY and board[i+1] != EMPTY and board[i+2] == EMPTY and board[i] != board[i+1]:
                new_board = list(board)
                new_board[i], new_board[i+2] = new_board[i+2], new_board[i]
                moves.append(new_board)
            if i - 2 >= 0 and board[i] != EMPTY and board[i-1] != EMPTY and board[i-2] == EMPTY and board[i] != board[i-1]:
                new_board = list(board)
                new_board[i], new_board[i-2] = new_board[i-2], new_board[i]
                moves.append(new_board)
        return moves

    def mutate(self) -> 'CheckersDNASeed':
        """A mutation is a valid move in the puzzle."""
        valid_moves = self._generate_moves()

        if not valid_moves:
            # Return a copy of self with very low fitness to avoid being selected again
            stagnant_copy = copy.deepcopy(self)
            stagnant_copy.fitness = 0.0
            return stagnant_copy

        # Choose a random move to create the child seed
        next_board_state = random.choice(valid_moves)

        # Create the new child seed for the next generation
        child_seed = CheckersDNASeed(
            board_state=next_board_state, 
            target_state=self.target_state, 
            generation=self.generation + 1
        )

        # Record evolution step (optional, but good practice)
        self.evolution_history.append({
            "parent": self.quantum_signature,
            "child": child_seed.quantum_signature,
            "move": self._state_to_dna(next_board_state),
            "timestamp": time.time()
        })

        return child_seed
