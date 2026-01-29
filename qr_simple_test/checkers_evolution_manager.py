#!/usr/bin/env python3
# checkers_evolution_manager.py
# Manages the evolution of a Checkers Jumping Puzzle solver.

import os
import json
import time
import random
import heapq
import argparse
from decimal import Decimal, getcontext

# --- Constants ---
getcontext().prec = 50
PHI = Decimal('1.6180339887498948482045868343656381177203091798058')

# --- Puzzle Definition ---
R_PIECE = 1
B_PIECE = -1
EMPTY = 0
INITIAL_STATE = (1, 1, 1, 0, -1, -1, -1)
TARGET_STATE = (-1, -1, -1, 0, 1, 1, 1)

class CheckersEvolutionManager:
    """A system that evolves a Checkers Jumping Puzzle solver."""

    def __init__(self, output_dir="checkers_evolution"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

        # Evolutionary parameters
        self.epoch = 1
        self.resonance = 0.5
        self.solver_performance = -1 # States explored

        # Error and correction state
        self.error_introduced = False
        self.error_corrected = False
        self.error_epoch = random.randint(10, 25)
        self.fitness_is_degraded = False

        self.evolution_history = []
        self._load_epigenetic_memory()

    def _load_epigenetic_memory(self):
        memory_path = os.path.join(self.output_dir, "checkers_epigenetic_memory.json")
        if not os.path.exists(memory_path):
            return
        try:
            with open(memory_path, "r") as f:
                memory = json.load(f)
            self.epoch = memory.get("epoch", 1)
            self.resonance = memory.get("resonance", 0.5)
            self.error_introduced = memory.get("error_introduced", False)
            self.error_corrected = memory.get("error_corrected", False)
            self.error_epoch = memory.get("error_epoch", random.randint(10, 25))
            self.fitness_is_degraded = memory.get("fitness_is_degraded", False)
            self.evolution_history = memory.get("evolution_history", [])
            print(f"Loaded epigenetic memory from epoch {self.epoch}")
        except Exception as e:
            print(f"Error loading epigenetic memory: {e}")

    def _save_epigenetic_memory(self):
        memory_path = os.path.join(self.output_dir, "checkers_epigenetic_memory.json")
        memory = {
            "epoch": self.epoch,
            "resonance": self.resonance,
            "error_introduced": self.error_introduced,
            "error_corrected": self.error_corrected,
            "error_epoch": self.error_epoch,
            "fitness_is_degraded": self.fitness_is_degraded,
            "evolution_history": self.evolution_history
        }
        with open(memory_path, "w") as f:
            json.dump(memory, f, indent=2)

    def generate_solver_script(self) -> str:
        """Generates the self-contained solver script for the current epoch."""

        if self.epoch == self.error_epoch and not self.error_introduced:
            self.fitness_is_degraded = True
            self.error_introduced = True
            print(f"\n*** INTRODUCING FITNESS ERROR IN EPOCH {self.epoch} ***\n")

        elif self.error_introduced and not self.error_corrected and self.resonance > 0.85:
            self.fitness_is_degraded = False
            self.error_corrected = True
            print(f"\n*** SELF-CORRECTION TRIGGERED IN EPOCH {self.epoch} (Resonance: {self.resonance:.4f}) ***\n")

        script = f"""\
# Checkers Jumper A* Solver - Evolved for Epoch {self.epoch}
# Resonance: {self.resonance:.4f}

import heapq
from decimal import Decimal, getcontext

getcontext().prec = 50
PHI = Decimal('{PHI}')

R_PIECE, B_PIECE, EMPTY = {R_PIECE}, {B_PIECE}, {EMPTY}
INITIAL_STATE = {INITIAL_STATE}
TARGET_STATE = {TARGET_STATE}

def get_valid_moves(state):
    moves = []
    size = len(state)
    for i in range(size):
        if state[i] == R_PIECE:
            if i + 1 < size and state[i+1] == EMPTY:
                new_state = list(state); new_state[i], new_state[i+1] = new_state[i+1], new_state[i]; moves.append(tuple(new_state))
            if i + 2 < size and state[i+1] == B_PIECE and state[i+2] == EMPTY:
                new_state = list(state); new_state[i], new_state[i+2] = new_state[i+2], new_state[i]; moves.append(tuple(new_state))
        if state[i] == B_PIECE:
            if i - 1 >= 0 and state[i-1] == EMPTY:
                new_state = list(state); new_state[i], new_state[i-1] = new_state[i-1], new_state[i]; moves.append(tuple(new_state))
            if i - 2 >= 0 and state[i-1] == R_PIECE and state[i-2] == EMPTY:
                new_state = list(state); new_state[i], new_state[i-2] = new_state[i-2], new_state[i]; moves.append(tuple(new_state))
    return moves

def calculate_fitness(state, target_state, degraded={self.fitness_is_degraded}):
    if state == target_state: return 0.0

    total_distance = 0
    r_indices = [i for i, p in enumerate(state) if p == R_PIECE]
    b_indices = [i for i, p in enumerate(state) if p == B_PIECE]
    r_target = [i for i, p in enumerate(target_state) if p == R_PIECE]
    b_target = [i for i, p in enumerate(target_state) if p == B_PIECE]

    for i in range(len(r_indices)):
        total_distance += abs(r_indices[i] - r_target[i])
        total_distance += abs(b_indices[i] - b_target[i])

    if degraded:
        # Degraded fitness: simple manhattan distance only.
        return float(total_distance)
    
    # Optimal fitness: phi-harmonic resonance scaling.
    return float(Decimal(total_distance) * (1/PHI))

def solve_checkers():
    open_set = [(calculate_fitness(INITIAL_STATE, TARGET_STATE), 0, INITIAL_STATE, [])] # (f_score, g_score, state, path)
    closed_set = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        if current in closed_set: continue
        closed_set.add(current)

        if current == TARGET_STATE:
            return path + [current], len(closed_set)

        for move in get_valid_moves(current):
            if move not in closed_set:
                new_g = g + 1
                h = calculate_fitness(move, TARGET_STATE)
                new_f = new_g + h
                heapq.heappush(open_set, (new_f, new_g, move, path + [current]))
    return None, len(closed_set)

# --- Execution ---
solution, states_explored = solve_checkers()
print(f"Epoch {self.epoch} Solver Run:")
if solution:
    print(f"  Solution found in {{len(solution) - 1}} moves.")
    print(f"  States explored: {{states_explored}}")
else:
    print("  No solution found.")
print(f"  Fitness function was {{'DEGRADED' if {self.fitness_is_degraded} else 'OPTIMAL'}}")
performance = states_explored
"""
        return script

    def evolve_parameters(self):
        self.resonance = (self.resonance * float(PHI) + (1/float(PHI))) % 1
        self.evolution_history.append({
            'epoch': self.epoch,
            'resonance': self.resonance,
            'performance': self.solver_performance,
            'fitness_degraded': self.fitness_is_degraded
        })
        self.epoch += 1

    def run_evolution_cycle(self, num_epochs=100):
        print(f"Starting Checkers evolution cycle for {num_epochs} epochs.")
        target_epoch = self.epoch + num_epochs

        while self.epoch < target_epoch:
            print(f"\n{'='*20} EPOCH {self.epoch} {'='*20}")
            solver_script = self.generate_solver_script()
            
            local_namespace = {}
            try:
                exec(solver_script, globals(), local_namespace)
                self.solver_performance = local_namespace.get('performance', -1)
            except Exception as e:
                print(f"Error executing solver script: {e}")
                self.solver_performance = -1

            self._save_epigenetic_memory()
            self.evolve_parameters()
            time.sleep(0.1)

        print("\nEvolution cycle complete.")
        if self.error_introduced and self.error_corrected:
            print("\n✅ SUCCESS: System detected performance drop and self-corrected the fitness function.")
        elif self.error_introduced and not self.error_corrected:
            print("\n❌ FAILURE: System did not correct the fitness error within the cycle.")
        else:
            print("\n⚠️ INCONCLUSIVE: Error was not introduced or cycle was too short.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Checkers Jumping Puzzle Evolutionary Manager.")
    parser.add_argument("--epochs", type=int, default=50, help="Number of evolutionary epochs to run.")
    args = parser.parse_args()

    manager = CheckersEvolutionManager()
    manager.run_evolution_cycle(num_epochs=args.epochs)
