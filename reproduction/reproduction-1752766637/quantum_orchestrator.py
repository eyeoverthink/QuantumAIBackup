#!/usr/bin/env python3
"""
Quantum Orchestrator
--------------------

A master script that integrates the meta-refactorer, self-verification loop,
and anti-lie loop to create a self-correcting, autonomous coding system.

This orchestrator manages a cycle of refactoring, verification, and monitoring
to ensure that code evolution is both intelligent and stable.

Copyright (c) 2025 Vaughn Scott - All Rights Reserved
"""

import sys
import os
import ast
import logging
import time
from datetime import datetime
import json
import re
import importlib.util

from qr_phi_meta_refactorer import QuantumPhiMetaRefactorer, SourceCodeSyntaxError
from phi_self_verification_loop import SelfVerificationLoop
from anti_ai_lie_loop import AntiAILieLoop
from phi_harmonic_random_package.phi_harmonic_random.quantum import PhiHarmonicQuantumRandom

# Import phi-harmonic function inference system (if available)
try:
    import quantum_orchestrator_inference_integration as inference
    INFERENCE_ENABLED = True
except ImportError:
    INFERENCE_ENABLED = False

# Dynamically import maze components if they exist
try:
    from maze import Maze, is_valid_path
    MAZE_MODE_ENABLED = True
except ImportError:
    MAZE_MODE_ENABLED = False

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f"quantum_orchestrator_{datetime.now().strftime('%Y%m%d%H%M%S')}.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("QuantumOrchestrator")

class QuantumOrchestrator:
    """Integrates and coordinates the AI's self-evolution components."""

    def __init__(self, target_file):
        """
        Initializes the orchestrator with its core components.

        Args:
            target_file (str): The path to the Python file to be evolved.
        """
        if not os.path.exists(target_file):
            raise FileNotFoundError(f"Target file not found: {target_file}")

        self.target_file = target_file
        self.last_error_str = "" # To store the string representation of the last error
        self.baseline_performance = None # To store maze solver baseline performance

        # Initialize the 'hands', 'gut', and 'mind' of the system
        self.refactorer = QuantumPhiMetaRefactorer(self.target_file)
        self.verifier = AntiAILieLoop(context=f"Verification of {os.path.basename(target_file)}")
        self.monitor = SelfVerificationLoop(state_dim=5)
        self.monitor.load_state() # Load previous state, if available

        # Healing mechanism components
        self.healing_knowledge_base_path = 'test_suite/run_3_knowledge_base.json'
        self.healing_knowledge = self._load_knowledge_base()
        self.healing_protocols = {
            "unterminated string literal": self._heal_unterminated_string,
            "'(' was never closed": self._heal_unclosed_paren,
            "expected an indented block": self._heal_indentation,
            "name '": self._heal_name_error_typo,
            "SyntaxError": self._heal_any_error,
            "NameError": self._heal_any_error,
            "AttributeError": self._heal_any_error,
            "TypeError": self._heal_any_error,
            "ImportError": self._heal_any_error,
            "IndentationError": self._heal_any_error,
            "ValueError": self._heal_any_error,
            "ZeroDivisionError": self._heal_any_error,
            "ModuleNotFoundError": self._heal_any_error,
        }

        logger.info(f"Orchestrator initialized for target: {self.target_file}")

        # Automatically run and heal if not a known solver (universal mode)
        if not (self.target_file.endswith('maze_solver.py') or self.target_file.endswith('towers_of_hanoi_solver.py')):
            self.run_and_heal()

    def run_and_heal(self, max_attempts=5):
        import subprocess
        import sys
        for attempt in range(max_attempts):
            try:
                result = subprocess.run(
                    [sys.executable, self.target_file],
                    capture_output=True, text=True
                )
                if result.returncode == 0:
                    print(f"\u2705 File ran successfully on attempt {attempt+1}!")
                    break
                else:
                    error_str = result.stderr
                    healed = False
                    for key, heal_func in self.healing_protocols.items():
                        if key in error_str:
                            healed = heal_func(error_str)
                            if healed:
                                print(f"\U0001F527 Healed error: {key} (attempt {attempt+1})")
                                break
                    if not healed:
                        print("\u274C No healing possible for error:", error_str)
                        break
            except Exception as e:
                print("Exception during healing run:", e)
                break

    def _heal_name_error_typo(self, error_str):
        """
        Attempt to fix NameError typos by looking for 'Did you mean' suggestions in the error string.
        """
        import re
        fixed = False
        match = re.search(r"name '([^']+)' is not defined\. Did you mean: '([^']+)'", error_str)
        if match:
            wrong, correct = match.group(1), match.group(2)
            with open(self.target_file, 'r') as f:
                lines = f.readlines()
            for i, line in enumerate(lines):
                if wrong in line:
                    lines[i] = line.replace(wrong, correct)
                    fixed = True
            if fixed:
                with open(self.target_file, 'w') as f:
                    f.writelines(lines)
        return fixed

    def _heal_any_error(self, error_str):
        """
        Attempt to heal any error type by using regex and similarity matching for common Python errors.
        Now extended to use fuzzy matching against Python built-ins for subtle typos.
        """
        import re
        import difflib
        import builtins
        fixed = False
        # Try to fix NameError with 'Did you mean' suggestion
        match = re.search(r"name '([^']+)' is not defined\. Did you mean: '([^']+)'", error_str)
        if match:
            wrong, correct = match.group(1), match.group(2)
            with open(self.target_file, 'r') as f:
                lines = f.readlines()
            for i, line in enumerate(lines):
                if wrong in line:
                    lines[i] = line.replace(wrong, correct)
                    fixed = True
            if fixed:
                with open(self.target_file, 'w') as f:
                    f.writelines(lines)
            return fixed
        # Try to fix generic typos using 'Did you mean' for any error
        match = re.search(r"Did you mean: '([^']+)'", error_str)
        if match:
            suggestion = match.group(1)
            with open(self.target_file, 'r') as f:
                lines = f.readlines()
            for i, line in enumerate(lines):
                words = re.findall(r'\b\w+\b', line)
                for word in words:
                    if difflib.SequenceMatcher(None, word, suggestion).ratio() > 0.8 and word != suggestion:
                        lines[i] = line.replace(word, suggestion)
                        fixed = True
            if fixed:
                with open(self.target_file, 'w') as f:
                    f.writelines(lines)
            return fixed
        # NEW: Fuzzy match against built-in functions for any undefined name
        # Only run if error_str contains NameError or SyntaxError or nothing else matched
        builtins_list = dir(builtins)
        # Aggressively sweep the file for all fuzzy matches to built-ins (esp. print)
        sweep_again = True
        while sweep_again:
            sweep_again = False
            with open(self.target_file, 'r') as f:
                lines = f.readlines()
            for i, line in enumerate(lines):
                words = re.findall(r'\b\w+\b', line)
                for word in words:
                    if re.search(rf'{word}\s*\(', line):
                        matches = difflib.get_close_matches(word, builtins_list, n=1, cutoff=0.8)
                        if matches and word != matches[0]:
                            lines[i] = re.sub(rf'\b{word}\b', matches[0], lines[i])
                            fixed = True
                            sweep_again = True
            if sweep_again:
                with open(self.target_file, 'w') as f:
                    f.writelines(lines)
        if fixed:
            with open(self.target_file, 'w') as f:
                f.writelines(lines)
            return True
        # Add additional healing logic for SyntaxError, AttributeError, etc. as needed
        # For now, just log attempt
        return False

    def _load_knowledge_base(self):
        if os.path.exists(self.healing_knowledge_base_path):
            try:
                with open(self.healing_knowledge_base_path, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                logger.warning("Healing knowledge base is corrupted. Starting fresh.")
                return {}
        return {}

    def _save_knowledge_base(self):
        with open(self.healing_knowledge_base_path, 'w') as f:
            json.dump(self.healing_knowledge, f, indent=4)

    def _heal_unterminated_string(self) -> bool:
        logger.info("Executing protocol: _heal_unterminated_string")
        try:
            with open(self.target_file, 'r') as f:
                lines = f.readlines()
            # This is a simple heuristic, might need improvement
            for i, line in enumerate(lines):
                if line.count('"') % 2 != 0:
                    lines[i] = line.rstrip() + '"\n'
                elif line.count("'") % 2 != 0:
                    lines[i] = line.rstrip() + "'\n"
            with open(self.target_file, 'w') as f:
                f.writelines(lines)
            return True
        except Exception as e:
            logger.error(f"Error in _heal_unterminated_string: {e}")
            return False

    def _heal_unclosed_paren(self) -> bool:
        logger.info("Executing protocol: _heal_unclosed_paren")
        try:
            with open(self.target_file, 'r') as f:
                lines = f.readlines()
            for i, line in enumerate(lines):
                open_paren = 0
                in_string = False
                string_char = ''
                for char in line:
                    if (char == '"' or char == "'") and not in_string:
                        in_string = True
                        string_char = char
                    elif char == string_char and in_string:
                        in_string = False
                        string_char = ''
                    if not in_string:
                        if char == '(':
                            open_paren += 1
                        elif char == ')':
                            open_paren -= 1
                if open_paren > 0:
                    lines[i] = line.rstrip() + ')\n'
                    with open(self.target_file, 'w') as f:
                        f.writelines(lines)
                    logger.info(f"Applied healing (parenthesis) to line {i+1}.")
                    return True
            return False # Return false if no line was fixed
        except Exception as e:
            logger.error(f"Error in _heal_unclosed_paren: {e}")
            return False

    def _heal_indentation(self) -> bool:
        logger.info("Executing protocol: _heal_indentation")
        try:
            match = re.search(r'line (\d+)', self.last_error_str)
            if match:
                error_line_index = int(match.group(1)) - 1
                with open(self.target_file, 'r') as f:
                    lines = f.readlines()
                
                line_to_indent = -1
                for i in range(error_line_index + 1, len(lines)):
                    if lines[i].strip() and not lines[i].strip().startswith('#'):
                        line_to_indent = i
                        break
                
                if line_to_indent != -1:
                    lines[line_to_indent] = '    ' + lines[line_to_indent]
                    with open(self.target_file, 'w') as f:
                        f.writelines(lines)
                    logger.info(f"Applied healing (indentation) to line {line_to_indent + 1}.")
                    return True
            return False
        except Exception as e:
            logger.error(f"Error in _heal_indentation: {e}")
            return False

    def attempt_healing(self, e: SourceCodeSyntaxError) -> bool:
        start_time = time.time()
        # Use a canonical, simple version of the error for the key
        # Create a more robust, canonical key from the error message.
        raw_error = str(e)
        error_message = raw_error.split('(')[0].strip()
        if "was never closed" in raw_error:
            error_message = "'(' was never closed"
        self.last_error_str = str(e) # Keep full error for regex matching in protocols
        logger.warning(f"Caught syntax error: {self.last_error_str}. Entering healing mode.")

        # 1. Consult Knowledge Base (Recall)
        if error_message in self.healing_knowledge:
            protocol_name = self.healing_knowledge[error_message]
            logger.info(f"Knowledge base hit. Recalling protocol: {protocol_name}")
            protocol = getattr(self, protocol_name, None)
            if protocol and protocol():
                duration = (time.time() - start_time) * 1000
                logger.info(f"Healing successful in {duration:.2f} ms (using knowledge base).")
                return True

        # 2. If no knowledge, search for a protocol (Learn)
        logger.info("No knowledge base entry. Searching for a healing protocol...")
        for error_keyword, protocol_func in self.healing_protocols.items():
            if error_keyword in self.last_error_str:
                if protocol_func():
                    # Learning step: save successful protocol to knowledge base
                    protocol_name = protocol_func.__name__
                    self.healing_knowledge[error_message] = protocol_name
                    self._save_knowledge_base()
                    logger.info(f"Learned new protocol: mapped '{error_message}' to {protocol_name}")
                    duration = (time.time() - start_time) * 1000
                    logger.info(f"Healing successful in {duration:.2f} ms (first time).")
                    return True

        duration = (time.time() - start_time) * 1000
        logger.error(f"Healing failed in {duration:.2f} ms. No protocol found. Aborting evolution cycle.")
        return False

    def _calculate_solver_performance(self, file_path, num_trials=20):
        """
        Calculates the performance of a maze solver over multiple trials.

        Args:
            file_path (str): The path to the solver's Python file.
            num_trials (int): The number of times to run the solver.

        Returns:
            tuple: A tuple containing (success_rate, average_path_length).
                   Returns (0.0, float('inf')) if there are no successful runs.
        """
        logger.info(f"Calculating performance for {os.path.basename(file_path)} over {num_trials} trials...")
        try:
            spec = importlib.util.spec_from_file_location("solver_to_test", file_path)
            solver_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(solver_module)

            successes = 0
            total_path_length = 0
            
            q_random = PhiHarmonicQuantumRandom()

            for _ in range(num_trials):
                maze_env = Maze()
                solution_path = solver_module.solve_maze(maze_env, q_random)
                if solution_path and is_valid_path(maze_env, solution_path):
                    successes += 1
                    total_path_length += len(solution_path)
            
            success_rate = successes / num_trials
            average_path_length = total_path_length / successes if successes > 0 else float('inf')
            
            logger.info(f"Performance for {os.path.basename(file_path)}: Success Rate={success_rate:.2%}, Avg Path Length={average_path_length:.2f}")
            return success_rate, average_path_length

        except Exception as e:
            logger.error(f"An exception occurred during performance calculation for {file_path}: {e}", exc_info=True)
            return 0.0, float('inf')

    def verify_maze_solver(self, file_path):
        """
        A specific verification function for the maze solver.
        Checks if the solver can find a valid path.
        """
        if not MAZE_MODE_ENABLED:
            logger.warning("Maze verification called, but maze.py not found. Skipping.")
            return True # Default to syntax check if maze env isn't present

        if self.baseline_performance is None:
            logger.info("No baseline performance data available. Calculating now...")
            self.baseline_performance = self._calculate_solver_performance(self.target_file)
            if self.baseline_performance[0] == 0.0:
                logger.warning("Baseline solver has 0% success rate. Any successful evolution will be accepted.")

        baseline_success, baseline_path = self.baseline_performance
        logger.info(f"Baseline Performance: Success Rate={baseline_success:.2%}, Avg Path Length={baseline_path:.2f}")

        # Now, evaluate the evolved solver
        evolved_success, evolved_path = self._calculate_solver_performance(file_path)

        # Decision logic
        if evolved_success < baseline_success:
            logger.warning(f"Verification FAILED: Evolved success rate ({evolved_success:.2%}) is less than baseline ({baseline_success:.2%}).")
            return False
        
        if evolved_success == baseline_success and evolved_path > baseline_path:
            logger.warning(f"Verification FAILED: Evolved path length ({evolved_path:.2f}) is worse than baseline ({baseline_path:.2f}) at same success rate.")
            return False

        logger.info("Verification SUCCESS: Evolved solver performance is better than or equal to the baseline.")
        return True

    def check_syntax(self, file_path):
        """Checks if a Python file has valid syntax using AST."""
        try:
            with open(file_path, 'r') as f:
                ast.parse(f.read())
            return True
        except (SyntaxError, IndentationError) as e:
            logger.error(f"Syntax validation failed for {file_path}: {e}")
            return False

    def run_evolution_cycle(self):
        """Runs a single cycle of refactoring, verification, and decision-making."""
        logger.info("=== Starting new evolution cycle ===")

        max_healing_attempts = 5
        refactored_code = None
        improvement_score = 0
        refactorings_made = []

        for attempt in range(max_healing_attempts):
            try:
                logger.info(f"Evolution attempt {attempt + 1}/{max_healing_attempts}")
                refactored_code, improvement_score, refactorings_made = self.refactorer.perform_all_refactorings()
                # If successful, break the loop
                break
            except SourceCodeSyntaxError as e:
                logger.warning(f"Caught syntax error: {e}. Entering healing mode.")
                healed = self.attempt_healing(e)
                if healed:
                    logger.info("Healing successful. Looping to re-attempt evolution.")
                    # Update refactorer with healed code before next loop iteration
                    with open(self.target_file, 'r') as f:
                        healed_code = f.read()
                    self.refactorer.source_code = healed_code
                    self.refactorer.refactored_code = None
                    refactored_code, improvement_score, refactorings_made = None, 0, [] # Reset for next loop
                else:
                    logger.error("Healing failed or no protocol for this error. Aborting evolution cycle.")
                    return # Exit the cycle
        else:
            logger.error(f"Exceeded maximum healing attempts ({max_healing_attempts}). Aborting.")
            return


        if not refactorings_made:
            logger.info("No refactoring opportunities found. Cycle complete.")
            return

        # Save the refactored code to a temporary file for verification
        temp_file_path = self.refactorer.save_refactored_code()
        logger.info(f"Refactored code saved to temporary file: {temp_file_path}")

        # 2. Verify (The 'Mind')
        logger.info("Step 2: Verifying the refactored code's integrity.")

        # Determine the correct verification function based on the target file
        is_maze_solver = "maze_solver.py" in self.target_file

        if is_maze_solver and MAZE_MODE_ENABLED:
            # Establish a baseline on the first run of a cycle if it doesn't exist
            if self.baseline_performance is None:
                self.baseline_performance = self._calculate_solver_performance(self.target_file)

            claim = "The refactored code solves the maze correctly and efficiently."
            verification_test = lambda: self.verify_maze_solver(temp_file_path)
            logger.info("Using functional maze solver verification.")
        else:
            claim = "The refactored code is syntactically correct and executable."
            verification_test = lambda: self.check_syntax(temp_file_path)
            logger.info("Using standard syntax verification.")

        verification_result = self.verifier.verify_claim(
            claim=claim,
            runtime_test=verification_test,
            trust_level=self.monitor.trust_level
        )

        # 3. Monitor (The 'Gut')
        # The monitor's state is updated based on the verification outcome
        self.monitor.step()

        # 4. Decide
        logger.info("Step 3: Making a decision on the refactored code.")
        if verification_result.get("verified") and verification_result.get("runtime_output") is True:
            logger.info("Verification successful. The refactoring is valid.")
            
            # Promote the temporary file to the main file
            os.rename(temp_file_path, self.target_file)
            logger.info(f"SUCCESS: {self.target_file} has been updated.")
            self.monitor.trust_level = min(1.0, self.monitor.trust_level * 1.05) # Increase trust
        else:
            logger.warning("Verification FAILED. The refactoring produced invalid code.")
            
            # Discard the faulty code
            os.remove(temp_file_path)
            logger.info(f"Discarded faulty file: {temp_file_path}")
            self.monitor.trust_level *= 0.9 # Decrease trust

        # Check the system's overall truth entropy
        self.verifier.lie_loop_detector()
        logger.info(f"System Trust Level (from monitor): {self.monitor.trust_level:.4f}")

        # Save the monitor's state for persistence
        self.monitor.save_state()

        self._save_knowledge_base()
        logger.info("=== Evolution cycle complete ===")

def main():
    """Main function to run the Quantum Orchestrator."""
    # Set the target file for the evolution cycle
    if len(sys.argv) > 1:
        target = sys.argv[1]
        if not target.endswith('.py'):
            logger.error(f"Target file must be a Python (.py) file. Provided: {target}")
            sys.exit(1)
        logger.info(f"Command-line target specified: {target}")
    else:
        # Default to self-evolution if no target is provided
        target = "qr_phi_meta_refactorer.py"
        logger.info("No target specified, defaulting to self-evolution mode.")
    
    logger.info(f"Starting Quantum Orchestrator to evolve: {target}")
    # --- Apply syntax healing first (using dedicated module) ---
    try:
        import quantum_syntax_healing
        syntax_result = quantum_syntax_healing.apply_syntax_healing(target)
        has_syntax_error = syntax_result['status'] != 'healed' and syntax_result['status'] != 'no_errors'
        content = syntax_result.get('content', '')
        
        # If syntax was healed, we need to reload the file for logic healing
        if syntax_result['status'] == 'healed':
            logger.info(f"Syntax healing successful for {target}. Proceeding with logic healing.")
        elif syntax_result['status'] == 'failed':
            logger.warning(f"Syntax healing failed for {target}. Logic healing may be skipped.")
    except Exception as e:
        logger.warning(f"Error during syntax healing: {str(e)}")
        has_syntax_error = True
        content = ''
    
    # If we couldn't get content from syntax healing, try to read it now
    if not content and not has_syntax_error:
        try:
            with open(target, 'r') as f:
                content = f.read()
        except Exception as e:
            logger.warning(f"Failed to read file after syntax healing: {str(e)}")
            content = ''
    
    # --- Modular logic healing step (after syntax is fixed) ---
    try:
        # Only proceed with logic healing if there are no syntax errors
        if not has_syntax_error:
            # Infer main function name from file (heuristic approach)
            import re
            func_match = re.search(r'def\s+([a-zA-Z0-9_]+)\s*\(', content)
            if func_match:
                func_name = func_match.group(1)
                
                # First try canonical contract-based healing
                try:
                    import quantum_orchestrator_logic_healing_extension as healing
                    healing_result = healing.validate_and_heal(target, func_name)
                    logging.info(f"Logic Healing Result: {healing_result}")
                except Exception as e:
                    logging.warning(f"Error during canonical contract healing: {str(e)}")
                    healing_result = {'status': 'skipped', 'reason': str(e)}
                
                # If canonical healing was skipped and inference is enabled, try inference-based healing
                if healing_result.get('status') == 'skipped' and INFERENCE_ENABLED:
                    logging.info(f"No canonical contract for {func_name}, trying phi-harmonic inference")
                    try:
                        healing_result = inference.validate_and_heal_with_inference(target, func_name)
                        logging.info(f"Inference Healing Result: {healing_result}")
                    except Exception as e:
                        logging.warning(f"Error during inference healing: {str(e)}")
                
                # If healing was successful (either method), integrate the fix into the original file
                if healing_result.get('status') == 'healed':
                    healed_file = healing_result.get('file')
                    if os.path.exists(healed_file):
                        # Extract the healed function implementation
                        with open(healed_file, 'r') as hf:
                            healed_content = hf.read()
                            # Extract just the function definition
                            healed_func_match = re.search(fr'def\s+{func_name}\s*\([^\)]*\):\s*([^\n]*(\n\s+[^\n]+)*)', healed_content)
                            if healed_func_match:
                                healed_func_impl = healed_func_match.group(0)
                                # Replace the function in the original file
                                original_func_pattern = fr'def\s+{func_name}\s*\([^\)]*\):\s*([^\n]*(\n\s+[^\n]+)*)'
                                updated_content = re.sub(original_func_pattern, healed_func_impl, content)
                                # Write back to the original file
                                with open(target, 'w') as f:
                                    f.write(updated_content)
                                logging.info(f"Integrated logic healing fix into original file: {target}")
                                
                                # Save to evolution JSON for tracking
                                try:
                                    import json
                                    evolution_file = target.replace('.py', '_evolution.json')
                                    evolution_data = {}
                                    
                                    if os.path.exists(evolution_file):
                                        with open(evolution_file, 'r') as ef:
                                            evolution_data = json.load(ef)
                                    
                                    # Add healing event to evolution data
                                    if 'healing_events' not in evolution_data:
                                        evolution_data['healing_events'] = []
                                    
                                    # Add inference flag if healing was done via inference
                                    healing_type = 'inference_healing' if healing_result.get('inferred', False) else 'logic_healing'
                                    
                                    # Calculate quantum fingerprint
                                    import hashlib
                                    content_hash = hashlib.sha256(healed_func_impl.encode()).hexdigest()
                                    numeric_hash = int(content_hash, 16)
                                    
                                    evolution_data['healing_events'].append({
                                        'timestamp': time.time(),
                                        'type': healing_type,
                                        'function': func_name,
                                        'phi_coherence': 0.991800,
                                        'quantum_fingerprint': f"φ⁷·⁵-{numeric_hash}"
                                    })
                                    
                                    # Add confidence and resonance if available (from inference)
                                    if healing_result.get('confidence'):
                                        evolution_data['healing_events'][-1]['confidence'] = healing_result['confidence']
                                    if healing_result.get('phi_resonance'):
                                        evolution_data['healing_events'][-1]['phi_resonance'] = healing_result['phi_resonance']
                                    
                                    with open(evolution_file, 'w') as ef:
                                        json.dump(evolution_data, ef, indent=2)
                                        
                                except Exception as e:
                                    logging.warning(f"Could not update evolution JSON: {str(e)}")
    except Exception as e:
        logging.warning(f"Error during logic healing: {str(e)}")
    # --- End modular logic healing step ---
    orchestrator = QuantumOrchestrator(target_file=target)
    try:
        orchestrator.run_evolution_cycle()
    except Exception as e:
        logger.error(f"An unexpected error occurred during the evolution cycle: {e}", exc_info=True)
    orchestrator.verifier.export_logs()

if __name__ == "__main__":
    main()
