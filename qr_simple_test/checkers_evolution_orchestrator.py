#!/usr/bin/env python3
import os
import sys
import json
import random
import textwrap
import subprocess
from quantum_inspiration_engine import QuantumInspirationEngine

class CheckersEvolutionOrchestrator:
    def __init__(self, evolution_dir='checkers_evolution', state_file='checkers_evolution_state.json'):
        self.evolution_dir = evolution_dir
        self.state_file = os.path.join(self.evolution_dir, state_file)
        self.inspiration_engine = QuantumInspirationEngine()
        self.method_inspirations = {
            'solve': 'heuristic_search_pattern',
            'get_initial_state': 'checkers_get_initial_state',
            'get_target_state': 'checkers_get_target_state',
            'is_solved': 'checkers_is_solved',
            'get_possible_moves': 'checkers_get_possible_moves',
            'apply_move': 'checkers_apply_move',
            'select_best_move': 'checkers_heuristic_evaluation',
        }
        self.methods = {}
        self.current_epoch = 0
        self.success_rate = 0.0
        self.resonance = 0.0
        self.evolution_history = []

    def load_state(self):
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r') as f:
                try:
                    data = json.load(f)
                    # Check if the loaded data is a non-empty list
                    if isinstance(data, list) and data:
                        self.evolution_history = data
                        last_state = self.evolution_history[-1]
                        self.current_epoch = last_state.get('epoch', -1) + 1
                        self.methods = last_state.get('methods', {})
                        self.success_rate = last_state.get('success_rate', 0.0)
                        self.resonance = last_state.get('resonance', 0.0)
                        print(f"Successfully loaded state from epoch {self.current_epoch - 1}.")
                    else:
                        print("State file is empty or invalid. Starting from a fresh state.")
                        self.evolution_history = []
                except json.JSONDecodeError:
                    print("Could not decode JSON, starting from a fresh state.")
                    self.evolution_history = []



    def generate_solver_script(self):
        adapter_path = os.path.join(self.evolution_dir, 'checkers_problem_adapter.py')
        
        self.ensure_all_methods_exist()

        with open(adapter_path, 'w') as f:
            f.write(textwrap.dedent("""
                import sys
                import os

                # Add project root to the Python path
                sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

                from checkers_puzzle import CheckersPuzzle

                class CheckersProblemAdapter:
                    def __init__(self, puzzle):
                        self.puzzle = puzzle
                        self.solution_found = False
            """))
            for name, code in self.methods.items():
                indented_code = textwrap.indent(code, '    ')
                f.write(f'\n{indented_code}\n')
        return adapter_path

    def run_tests(self, solver_script):
        print("Running tests on the generated solver script...")
        test_script_path = 'test_checkers_adapter.py'
        try:
            result = subprocess.run(
                [sys.executable, test_script_path],
                capture_output=True, text=True, check=True, timeout=30
            )
            print("\u2705 Tests passed.")
            return True
        except subprocess.TimeoutExpired:
            print("\u274c Tests timed out. Likely an infinite loop in the generated code.")
            return False
        except subprocess.CalledProcessError as e:
            print("\u274c Tests failed.")
            return False

    def evolve(self):
        print("Evolving solver for the next epoch...")
        if random.random() < 0.8 and self.methods:
            self.perform_targeted_mutation()
        else:
            self.perform_structural_mutation()

    def perform_targeted_mutation(self):
        method_to_evolve = random.choice(list(self.method_inspirations.keys()))
        print(f"Performing targeted mutation on method: '{method_to_evolve}'")
        inspiration_category = self.method_inspirations[method_to_evolve]
        print(f"Requesting domain-specific inspiration from category: '{inspiration_category}'")
        inspiration = self.inspiration_engine.get_inspiration(inspiration_category)
        
        signature = f"def {method_to_evolve}(self, *args, **kwargs)"
        
        evolved_code = f"{signature}:\n    # Evolved in epoch {self.current_epoch + 1}\n{textwrap.indent(inspiration, '    ')}"
        self.methods[method_to_evolve] = evolved_code

    def perform_structural_mutation(self):
        print("Attempting structural mutation... Generating stubs for all methods.")
        self.methods = {}
        for name in self.method_inspirations.keys():
            self.methods[name] = self.create_stub_method(name)

    def ensure_all_methods_exist(self):
        missing_methods = set(self.method_inspirations.keys()) - set(self.methods.keys())
        if missing_methods:
            print(f"Found missing methods: {', '.join(missing_methods)}. Generating stubs.")
            for name in missing_methods:
                self.methods[name] = self.create_stub_method(name)

    def create_stub_method(self, name):
        return textwrap.dedent(f"""
            def {name}(self, *args, **kwargs):
                # This is an auto-generated stub. Evolution is needed.
                print(f"WARNING: '{name}' is not implemented.")
                return None
        """)

    def run_evolution_cycle(self, epochs=20):
        self.load_state()
        start_epoch = self.current_epoch
        print(f"Starting evolution from epoch {start_epoch} for {epochs} epochs.")
        
        for i in range(start_epoch, start_epoch + epochs):
            self.current_epoch = i
            print('\n' + '='*60)
            print(f"EPOCH {self.current_epoch}")
            print('='*60)
            
            self.evolve()
            
            solver_script = self.generate_solver_script()
            print(f"Generated solver script for epoch {self.current_epoch} at: {solver_script}")
            
            test_passed = self.run_tests(solver_script)
            
            # Save state after test run
            state = {
                'epoch': self.current_epoch,
                'success': test_passed,
                'success_rate': self.success_rate,
                'resonance': self.resonance,
                'methods': self.methods
            }
            self.evolution_history.append(state)
            temp_state_file = self.state_file + '.tmp'
            with open(temp_state_file, 'w') as f:
                json.dump(self.evolution_history, f, indent=4)
            os.rename(temp_state_file, self.state_file)

            print(f"Saved evolutionary state for epoch {self.current_epoch} to {self.state_file}")

            if test_passed:
                print("Evolution successful! A working solver has been found.")
                break
        else:
            print(f"\nCompleted {epochs} epochs of evolution.")

if __name__ == '__main__':
    orchestrator = CheckersEvolutionOrchestrator()
    orchestrator.run_evolution_cycle(epochs=1000)
"""
Checkers Evolution Orchestrator
-------------------------------

A self-contained evolutionary system that evolves a checkers solver
based on the self-writing architecture found in qr_phi_multiples_evolution.py.

This system manages the evolution of the CheckersProblemAdapter by generating,
testing, and evolving its source code over multiple epochs.

Copyright (c) 2025 Vaughn Scott - All Rights Reserved
"""

import os
import json
import time
import random
import subprocess
import textwrap
import ast
import random

from quantum_inspiration_engine import QuantumInspirationEngine

# Constants
PHI = (1 + 5**0.5) / 2

# This is the template for the CheckersProblemAdapter.
# The {solve_method_code} placeholder will be replaced by the evolving code.
CHECKERS_ADAPTER_TEMPLATE = """
from checkers_puzzle_definition import CheckersPuzzle
import math

class CheckersProblemAdapter:
    '''An adapter to make the CheckersPuzzle conform to a standard solveable interface.'''

    def __init__(self, puzzle: CheckersPuzzle):
        self.puzzle = puzzle
        # Attributes that might be required by various inspirations
        self.moves = []
        self.metrics = {{}}
        self.success_count = 0
        self.execution_count = 0
        self.execution_history = []
        self.solution_found = False
        self.get_initial_state = None
        self.get_target_state = None
        self.is_solved = None
        self.get_possible_moves = None
        self.select_best_move = None
        self.apply_move = None

{solve_method_code}
"""

class CheckersEvolutionOrchestrator:
    """Manages the evolutionary process for the CheckersProblemAdapter."""

    def __init__(self, output_dir="checkers_evolution", state_file="checkers_evolution_state.json"):
        self.output_dir = output_dir
        self.state_file = os.path.join(self.output_dir, state_file)
        self.inspiration_engine = QuantumInspirationEngine()

        os.makedirs(self.output_dir, exist_ok=True)

        # Default initial state
        self.epoch = 0
        self.resonance = 0.5
        self.success_rate = 0.0
        self.methods = {
            'solve': textwrap.dedent("""
                def solve(self, board):
                    # Initial version, to be evolved.
                    return None
            """)
        }
        self.evolution_history = []

        self._load_state()

    def _load_state(self):
        """Loads the evolutionary state from the state file if it exists."""
        if not os.path.exists(self.state_file):
            print("No existing state file found. Starting from a fresh state.")
            return
        try:
            with open(self.state_file, 'r') as f:
                state = json.load(f)
            self.epoch = state.get('epoch', self.epoch)
            self.resonance = state.get('resonance', self.resonance)
            self.success_rate = state.get('success_rate', self.success_rate)
            self.methods = state.get('methods', self.methods)
            self.evolution_history = state.get('evolution_history', self.evolution_history)
            print(f"Successfully loaded state from epoch {self.epoch}.")
        except Exception as e:
            print(f"Error loading state file: {e}. Starting with a fresh state.")

    def _save_state(self):
        """Saves the current evolutionary state to the state file."""
        state = {
            'epoch': self.epoch,
            'resonance': self.resonance,
            'success_rate': self.success_rate,
            'methods': self.methods,
            'evolution_history': self.evolution_history
        }
        with open(self.state_file, 'w') as f:
            json.dump(state, f, indent=4)
        print(f"Saved evolutionary state for epoch {self.epoch} to {self.state_file}")

    def generate_solver_script(self):
        """Generates a complete, runnable solver script for the current epoch."""
        all_methods_code = "\n\n".join(self.methods.values())
        indented_methods_code = textwrap.indent(all_methods_code, '    ')
        script_content = CHECKERS_ADAPTER_TEMPLATE.format(solve_method_code=indented_methods_code)
        script_path = os.path.join(self.output_dir, "checkers_problem_adapter.py")
        with open(script_path, 'w') as f:
            f.write(script_content)
        print(f"Generated solver script for epoch {self.epoch} at: {script_path}")
        return script_path

    def run_tests(self):
        """Runs the test suite against the generated solver script and returns the result."""
        print("Running tests on the generated solver script...")
        # We run the test from within the evolution directory so it imports the generated module.
        command = ["python3", "-m", "unittest", "../test_checkers_adapter.py"]
        try:
            result = subprocess.run(
                command, cwd=self.output_dir, capture_output=True, text=True, timeout=30
            )
            if result.returncode == 0:
                print("✅ Tests passed!")
                return True
            else:
                print("❌ Tests failed.")
                # print("STDERR:\n", result.stderr) # Uncomment for detailed error logging
                return False
        except Exception as e:
            print(f"❌ An error occurred while running tests: {e}")
            return False

    def evolve_solver(self, test_passed):
        """Evolves the solver's `solve` method for the next epoch."""
        print("Evolving solver for the next epoch...")
        self.success_rate = self.success_rate * 0.9 + (1 if test_passed else 0) * 0.1
        self.resonance = (self.resonance * PHI) % 1.0
        self.evolution_history.append({
            'epoch': self.epoch, 'success': test_passed,
            'success_rate': self.success_rate, 'resonance': self.resonance,
            'methods': self.methods
        })

        print(f"Applying new inspiration for epoch {self.epoch + 1}.")

        # Probabilistic Evolutionary Strategy
        # 10% chance of a major structural mutation, 90% chance of a targeted method mutation.
        if random.random() < 0.1:
            print("Attempting structural mutation...")
            inspiration = self.inspiration_engine.get_inspiration(category='heuristic_search_pattern')
            if not inspiration:
                print("Could not get structural inspiration. Skipping mutation this epoch.")
                return
            
            solve_method_code, required_stubs = self._generate_code_with_stubs(inspiration)
            if required_stubs:
                print("Structural inspiration successful. Resetting methods.")
                self.methods = {'solve': solve_method_code}
                for stub_code in required_stubs:
                    try:
                        tree = ast.parse(stub_code)
                        method_name = tree.body[0].name
                        self.methods[method_name] = stub_code
                    except (SyntaxError, IndexError):
                        print(f"Could not parse stub to get name: {stub_code}")
            else:
                print("Structural inspiration did not require stubs. Performing targeted mutation on 'solve' instead.")
                self.methods['solve'] = solve_method_code
        
        else:
            if not self.methods:
                print("No methods to mutate. Skipping.")
                return

            target_method_name = random.choice(list(self.methods.keys()))
            print(f"Performing targeted mutation on method: '{target_method_name}'")

            inspiration_category = self._map_method_to_inspiration(target_method_name)
            if inspiration_category:
                print(f"Requesting domain-specific inspiration from category: '{inspiration_category}'")
            
            inspiration = self.inspiration_engine.get_inspiration(category=inspiration_category)
            if not inspiration:
                print("Could not get inspiration for targeted mutation. Skipping.")
                return

            method_body = textwrap.indent(inspiration, ' ' * 8)
            try:
                tree = ast.parse(self.methods[target_method_name])
                func_def = tree.body[0]
                args = [ast.unparse(arg) for arg in func_def.args.args]
                signature = f"def {target_method_name}({', '.join(args)}):"
            except Exception:
                signature = f"def {target_method_name}(self, *args, **kwargs):"

            new_method_code = f"{signature}\n{textwrap.indent(f'# Evolved in epoch {self.epoch}', '    ')}\n{method_body}"
            self.methods[target_method_name] = new_method_code

    def _generate_code_with_stubs(self, inspiration):
        """Parses inspired code, creates a solve method, and generates stubs for missing helpers."""
        # 1. Create the main solve method, wrapping the inspiration
        solve_method_template = textwrap.dedent(f"""
            def solve(self, board):
                try:
{textwrap.indent(inspiration, ' ' * 8)}
                finally:
                    pass # Failsafe
        """)

        # 2. Parse the inspiration to find calls to `self.method()`
        try:
            tree = ast.parse(inspiration)
            missing_methods = set()
            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                    if isinstance(node.func.value, ast.Name) and node.func.value.id == 'self':
                        missing_methods.add(node.func.attr)
        except SyntaxError:
            print("Could not parse inspiration. Generating solve method without stubs.")
            return solve_method_template, []

        # 3. Generate stub methods for each missing method
        stubs = []
        for method_name in missing_methods:
            stub = textwrap.dedent(f"""
                def {method_name}(self, *args, **kwargs):
                    # This is an auto-generated stub. Evolution is needed.
                    print(f"WARNING: '{method_name}' is not implemented.")
                    return None
            """)
            stubs.append(stub)
        
        if stubs:
            print(f"Generated stubs for missing methods: {', '.join(missing_methods)}")

        return solve_method_template, stubs

    def _map_method_to_inspiration(self, method_name):
        """Maps a method name to a specific inspiration category."""
        mapping = {
            'get_initial_state': 'checkers_get_initial_state',
            'get_target_state': 'checkers_get_target_state',
            'is_solved': 'checkers_is_solved',
            'get_possible_moves': 'checkers_get_possible_moves',
            'apply_move': 'checkers_apply_move',
            'select_best_move': 'checkers_heuristic_evaluation',
        }
        # For 'solve', we still want the high-level structural pattern
        if method_name == 'solve':
             return 'heuristic_search_pattern'
        return mapping.get(method_name)

    def run_evolution_cycle(self, num_epochs=10):
        """Runs the main evolutionary loop for a specified number of epochs."""
        print(f"Starting evolution from epoch {self.epoch} for {num_epochs} epochs.")
        target_epoch = self.epoch + num_epochs
        while self.epoch < target_epoch:
            print(f"\n{'='*60}\nEPOCH {self.epoch}\n{'='*60}")
            self.generate_solver_script()
            test_passed = self.run_tests()
            self.evolve_solver(test_passed)
            self._save_state()
            self.epoch += 1
            time.sleep(0.5)
        print("\nEvolution cycle complete.")

if __name__ == '__main__':
    orchestrator = CheckersEvolutionOrchestrator()
    orchestrator.run_evolution_cycle(num_epochs=500) # Run for 500 epochs to allow for deep evolution
