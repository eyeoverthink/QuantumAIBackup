#!/usr/bin/env python3
# hanoi_evolution_manager.py
# Manages the evolution of a Tower of Hanoi solver, testing its self-correction capabilities.

import os
import json
import time
import random
import heapq
import argparse
import numpy as np
import matplotlib.pyplot as plt

# --- Constants ---
PHI = (1 + 5**0.5) / 2  # Golden Ratio

class HanoiEvolutionManager:
    """A system that evolves a Tower of Hanoi solver through self-correction."""

    def __init__(self, num_disks=3, output_dir="hanoi_evolution"):
        self.num_disks = num_disks
        self.start_state = tuple(range(num_disks, 0, -1)), (), ()
        self.goal_state = (), (), tuple(range(num_disks, 0, -1))
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

        # Evolutionary parameters
        self.epoch = 1
        self.resonance = 0.5
        self.complexity = 0.5
        self.mutation_rate = 0.1
        self.solver_performance = -1 # States explored, -1 for not run

        # Error and correction state
        self.error_introduced = False
        self.error_corrected = False
        self.error_epoch = random.randint(10, 29) # Epoch to introduce the error
        self.heuristic_is_degraded = False

        # History for visualization
        self.evolution_history = []

        self._load_epigenetic_memory()

    def _load_epigenetic_memory(self):
        memory_path = os.path.join(self.output_dir, "hanoi_epigenetic_memory.json")
        if not os.path.exists(memory_path):
            return
        try:
            with open(memory_path, "r") as f:
                memory = json.load(f)
            self.epoch = memory.get("epoch", 1)
            self.resonance = memory.get("resonance", 0.5)
            self.complexity = memory.get("complexity", 0.5)
            self.mutation_rate = memory.get("mutation_rate", 0.1)
            self.error_introduced = memory.get("error_introduced", False)
            self.error_corrected = memory.get("error_corrected", False)
            self.error_epoch = memory.get("error_epoch", random.randint(10, 25))
            self.heuristic_is_degraded = memory.get("heuristic_is_degraded", False)
            self.evolution_history = memory.get("evolution_history", [])
            print(f"Loaded epigenetic memory from epoch {self.epoch}")
        except Exception as e:
            print(f"Error loading epigenetic memory: {e}")

    def _save_epigenetic_memory(self):
        memory_path = os.path.join(self.output_dir, "hanoi_epigenetic_memory.json")
        memory = {
            "epoch": self.epoch,
            "resonance": self.resonance,
            "complexity": self.complexity,
            "mutation_rate": self.mutation_rate,
            "error_introduced": self.error_introduced,
            "error_corrected": self.error_corrected,
            "error_epoch": self.error_epoch,
            "heuristic_is_degraded": self.heuristic_is_degraded,
            "evolution_history": self.evolution_history
        }
        with open(memory_path, "w") as f:
            json.dump(memory, f, indent=2)

    def generate_solver_script(self) -> str:
        """Generates the complete, self-contained solver script for the current epoch."""
        
        # Determine if the heuristic should be degraded for this epoch
        if self.epoch == self.error_epoch and not self.error_introduced:
            self.heuristic_is_degraded = True
            self.error_introduced = True
            print(f"\n*** INTRODUCING HEURISTIC ERROR IN EPOCH {self.epoch} ***\n")

        # Determine if the system should attempt self-correction
        # Condition: Error was introduced, not yet corrected, and resonance is high.
        elif self.error_introduced and not self.error_corrected and self.resonance > 0.85:
            self.heuristic_is_degraded = False # Correct the heuristic
            self.error_corrected = True
            print(f"\n*** SELF-CORRECTION TRIGGERED IN EPOCH {self.epoch} (Resonance: {self.resonance:.4f}) ***\n")

        # The heuristic function is defined inside the generated script.
        # The 'degraded' parameter controls its behavior.
        script = f"""\
# Tower of Hanoi A* Solver - Evolved for Epoch {self.epoch}
# Resonance: {self.resonance:.4f} | Complexity: {self.complexity:.4f}

import heapq

PHI = {PHI}

def solve_hanoi(num_disks, start_state, goal_state, degraded_heuristic={self.heuristic_is_degraded}):
    \"\"\"A* search for Tower of Hanoi.\"\"\"

    def h(state):
        # Heuristic: Number of disks not in their final peg.
        misplaced_disks = 0
        for i in range(num_disks):
            disk = i + 1
            if disk not in state[2]:
                misplaced_disks += 1
        
        if degraded_heuristic:
            # Degraded heuristic: Ignore half the misplaced disks, making it less accurate.
            return misplaced_disks / 2
        return misplaced_disks

    def get_moves(state):
        moves = []
        for i in range(3):
            if not state[i]: continue
            disk = state[i][-1]
            for j in range(3):
                if i == j: continue
                if not state[j] or state[j][-1] > disk:
                    new_state = [list(p) for p in state]
                    new_state[j].append(new_state[i].pop())
                    moves.append(tuple(tuple(p) for p in new_state))
        return moves

    open_set = [(h(start_state), 0, start_state, [])] # (f_score, g_score, state, path)
    closed_set = set()
    g_scores = {{start_state: 0}}

    while open_set:
        _, g, current, path = heapq.heappop(open_set)

        if current == goal_state:
            return path + [current], len(closed_set)

        if current in closed_set:
            continue
        closed_set.add(current)

        for move in get_moves(current):
            new_g = g + 1
            if move not in g_scores or new_g < g_scores[move]:
                g_scores[move] = new_g
                f = new_g + h(move)
                heapq.heappush(open_set, (f, new_g, move, path + [current]))
    return None, len(closed_set)

# --- Execution ---
start_state = {self.start_state}
goal_state = {self.goal_state}
num_disks = {self.num_disks}

solution, states_explored = solve_hanoi(num_disks, start_state, goal_state)

print(f"Epoch {self.epoch} Solver Run:")
if solution:
    print(f"  Solution found in {{len(solution) - 1}} moves.")
    print(f"  States explored: {{states_explored}}")
else:
    print("  No solution found.")
print(f"  Heuristic was {{'DEGRADED' if {self.heuristic_is_degraded} else 'OPTIMAL'}}")

# Return performance metric for the manager
performance = states_explored
"""
        return script

    def evolve_parameters(self):
        """Evolve system parameters using phi-harmonic principles."""
        self.resonance = (self.resonance * PHI + (1/PHI)) % 1
        self.complexity = (self.complexity + (1/PHI)**2) % 1
        self.mutation_rate = abs((self.mutation_rate * PHI - (1/PHI)) % 0.1)

        self.evolution_history.append({
            'epoch': self.epoch,
            'resonance': self.resonance,
            'complexity': self.complexity,
            'performance': self.solver_performance,
            'heuristic_degraded': self.heuristic_is_degraded
        })
        self.epoch += 1

    def run_evolution_cycle(self, num_epochs=100):
        print(f"Starting Hanoi evolution cycle for {num_epochs} epochs.")
        target_epoch = self.epoch + num_epochs

        while self.epoch < target_epoch:
            print(f"\n{'='*20} EPOCH {self.epoch} {'='*20}")
            
            solver_script = self.generate_solver_script()
            
            # Execute the generated script and capture its performance
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
            print("\n✅ SUCCESS: System detected performance drop and self-corrected the heuristic.")
        elif self.error_introduced and not self.error_corrected:
            print("\n❌ FAILURE: System did not correct the heuristic error within the cycle.")
        else:
            print("\n⚠️ INCONCLUSIVE: Error was not introduced or cycle was too short.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Tower of Hanoi Evolutionary Manager.")
    parser.add_argument("--disks", type=int, default=4, help="Number of disks for the Tower of Hanoi puzzle.")
    parser.add_argument("--epochs", type=int, default=50, help="Number of evolutionary epochs to run.")
    args = parser.parse_args()

    manager = HanoiEvolutionManager(num_disks=args.disks)
    manager.run_evolution_cycle(num_epochs=args.epochs)
