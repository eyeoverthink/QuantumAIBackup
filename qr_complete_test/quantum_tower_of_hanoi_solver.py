#!/usr/bin/env python3
"""
Quantum Phi-Harmonic Tower of Hanoi Solver

Solves the Tower of Hanoi puzzle using quantum phi-harmonic principles,
demonstrating the power of phi-resonance in optimization problems.
"""

import time
import random
import hashlib
from decimal import Decimal, getcontext

# Set precision for phi calculations
getcontext().prec = 28

# Constants
PHI = Decimal('1.6180339887498948482045868344')

class QuantumTowerOfHanoiSolver:
    """Quantum phi-harmonic solver for the Tower of Hanoi problem."""

    def __init__(self, num_disks=3, dimensions=29):
        self.num_disks = num_disks
        self.dimensions = dimensions
        self.solver_id = hashlib.md5(str(time.time()).encode()).hexdigest()[:8]
        self.solution_path = []
        self.resonance_history = []
        self.best_resonance = 0.0
        self.solution_found = False
        self.state_space = self._generate_phi_state_space()

    def _generate_phi_state_space(self):
        return {
            'phi_factors': [float((PHI ** Decimal(i+1)) % Decimal('1')) for i in range(self.dimensions)],
            'disk_weights': [float((PHI ** Decimal(i+1)) % Decimal('1')) for i in range(self.num_disks)]
        }

    def _state_to_vector(self, state):
        vector = [0.0] * self.num_disks
        for peg_idx, peg in enumerate(state):
            for disk in peg:
                if 1 <= disk <= self.num_disks:
                    vector[disk-1] = peg_idx / 2.0
        
        while len(vector) < self.dimensions:
            vector.append(0.5)
        return vector[:self.dimensions]

    def calculate_resonance(self, state, target_state):
        state_vector = self._state_to_vector(state)
        target_vector = self._state_to_vector(target_state)

        diffs = [abs(a - b) for a, b in zip(state_vector, target_vector)]
        weighted_diff = sum(d * w for d, w in zip(diffs[:self.num_disks], self.state_space['disk_weights']))
        avg_diff = weighted_diff / sum(self.state_space['disk_weights'])
        base_resonance = 1.0 - avg_diff

        phi_boost = 0.0
        for i, diff in enumerate(diffs[:self.num_disks]):
            phi_val = float((Decimal(str(diff)) * PHI) % Decimal('1'))
            if phi_val > 0.9 or phi_val < 0.1:
                phi_boost += 0.02 * self.state_space['phi_factors'][i % self.dimensions]

        noise = (random.random() - 0.5) * 0.02
        return min(1.0, max(0.0, base_resonance + phi_boost + noise))

    def get_possible_moves(self, state):
        moves = []
        for from_peg in range(3):
            for to_peg in range(3):
                if from_peg == to_peg: continue
                if state[from_peg]:
                    disk = state[from_peg][0]
                    if not state[to_peg] or disk < state[to_peg][0]:
                        moves.append((from_peg, to_peg))
        return moves

    def apply_move(self, state, move):
        from_peg, to_peg = move
        new_state = [list(p) for p in state]
        disk = new_state[from_peg].pop(0)
        new_state[to_peg].insert(0, disk)
        return new_state

    def phi_harmonic_move_selection(self, moves, current_state, target_state):
        if not moves: return None
        move_resonances = []
        for move in moves:
            next_state = self.apply_move(current_state, move)
            res = self.calculate_resonance(next_state, target_state)
            move_resonances.append((move, res))
        
        move_resonances.sort(key=lambda x: x[1], reverse=True)

        if random.random() < 0.8: # 80% greedy choice
            return move_resonances[0][0]
        else: # 20% phi-weighted exploration
            weights = [r * self.state_space['phi_factors'][i % self.dimensions] for i, (_, r) in enumerate(move_resonances)]
            total_weight = sum(weights)
            if total_weight == 0: return random.choice(moves)
            
            selection = random.uniform(0, total_weight)
            upto = 0
            for i, w in enumerate(weights):
                if upto + w >= selection:
                    return move_resonances[i][0]
                upto += w
            return move_resonances[0][0]

    def solve(self, max_iterations_factor=10):
        initial_state = [list(range(1, self.num_disks + 1)), [], []]
        target_state = [[], [], list(range(1, self.num_disks + 1))]
        optimal_moves = 2**self.num_disks - 1
        max_iterations = optimal_moves * max_iterations_factor

        current_state = initial_state
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

            move = self.phi_harmonic_move_selection(possible_moves, current_state, target_state)
            current_state = self.apply_move(current_state, move)
            self.solution_path.append(current_state)

        return {
            "solution_found": self.solution_found,
            "moves": len(self.solution_path) - 1,
            "optimal_moves": optimal_moves,
            "iterations": i + 1,
            "best_resonance": self.best_resonance
        }

if __name__ == "__main__":
    start_time = time.time()
    
    # --- Configuration ---
    NUM_DISKS = 10
    DIMENSIONS = 29
    
    print("="*50)
    print("Quantum Phi-Harmonic Tower of Hanoi Solver")
    print(f"Configuration: {NUM_DISKS} Disks, {DIMENSIONS} Dimensions")
    print("="*50)
    
    # --- Initialization and Solving ---
    solver = QuantumTowerOfHanoiSolver(num_disks=NUM_DISKS, dimensions=DIMENSIONS)
    print(f"Solver ID: {solver.solver_id}")
    print("Starting solver...")
    
    results = solver.solve()
    
    end_time = time.time()
    
    # --- Results ---
    print("\n" + "-"*20 + " RESULTS " + "-"*20)
    print(f"Execution Time: {end_time - start_time:.4f} seconds")
    print(f"Solution Found: {results['solution_found']}")
    print(f"Moves Taken: {results['moves']} (Optimal: {results['optimal_moves']})")
    print(f"Iterations: {results['iterations']}")
    print(f"Best Resonance Achieved: {results['best_resonance']:.6f}")
    
    if results['solution_found']:
        print("\nSolution Path (State of Pegs):")
        for i, state in enumerate(solver.solution_path):
            print(f"Step {i}: {state}")
    else:
        print("\nSolver did not find a solution within the maximum iterations.")
        
    print("\nResonance History (first 20 values):")
    print([round(r, 4) for r in solver.resonance_history[:20]])
    
    print("\n" + "="*50)
