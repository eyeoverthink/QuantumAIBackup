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
import ast
import os
import time
import hashlib
import logging
from datetime import datetime

from qr_phi_meta_refactorer import QuantumPhiMetaRefactorer
from anti_ai_lie_loop import AntiAILieLoop
from phi_self_verification_loop import SelfVerificationLoop
from quantum_gene import QuantumGene
from quantum_mutator import CodeMutator

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
        
        # Initialize the 'hands', 'gut', and 'mind' of the system
        self.refactorer = QuantumPhiMetaRefactorer(self.target_file)
        self.verifier = AntiAILieLoop(context=f"Verification of {os.path.basename(target_file)}")
        self.monitor = SelfVerificationLoop(state_dim=5)
        self.monitor.load_state() # Load previous state, if available
        logger.info(f"Orchestrator initialized for target: {self.target_file}")

    def check_syntax(self, file_path):
        """Checks if a Python file has valid syntax using AST.

        Returns:
            bool: True if syntax is valid, False otherwise.
        """
        try:
            with open(file_path, 'r') as f:
                ast.parse(f.read())
            return True
        except (SyntaxError, IndentationError) as e:
            logger.error(f"Syntax validation failed for {file_path}: {e}")
            return False

    def run_evolution_cycle(self):
        """Runs a single cycle of mutation, refactoring, verification, and decision-making."""
        logger.info("=== Starting new evolution cycle ===")

        # Step 1: Mutate (The 'Imagination')
        logger.info("Step 1: Attempting to mutate the code.")
        try:
            with open(self.target_file, 'r') as f:
                original_code = f.read()
            
            mutator = CodeMutator(function_name='solve')
            mutated_code, mutation_applied = mutator.mutate(original_code)
            
            candidate_code = mutated_code # The mutate function returns the new or original code
            
            if mutation_applied:
                logger.info("A mutation was successfully applied.")
            else:
                logger.info("No mutation was applied.")
        except Exception as e:
            logger.error(f"Error during mutation phase: {e}", exc_info=True)
            return # Exit cycle on mutation error

        # Step 2: Refactor (The 'Hands')
        logger.info("Step 2: Attempting to refactor the candidate code.")
        
        candidate_path = f"{self.target_file}.candidate"
        with open(candidate_path, 'w') as f:
            f.write(candidate_code)
        
        candidate_refactorer = QuantumPhiMetaRefactorer(candidate_path)
        refactored_code, improvement_score, refactorings_made = candidate_refactorer.perform_all_refactorings()

        if not mutation_applied and not refactorings_made:
            logger.info("No mutations or refactorings were applied. Cycle complete.")
            os.remove(candidate_path)
            return

        if refactorings_made:
            temp_file_path = candidate_refactorer.save_refactored_code()
            logger.info(f"Refactored candidate saved to temporary file: {temp_file_path}")
            os.remove(candidate_path)
        else:
            temp_file_path = candidate_path
            logger.info(f"Mutated candidate will be used for verification: {temp_file_path}")

        if not temp_file_path or not os.path.exists(temp_file_path):
            logger.error(f"FATAL: No valid candidate file found for verification. Path: '{temp_file_path}'")
            if os.path.exists(candidate_path) and temp_file_path != candidate_path:
                os.remove(candidate_path)
            return

        # Step 3: Verify (The 'Mind')
        logger.info("Step 3: Verifying the candidate code's integrity.")
        claim = "The candidate code is syntactically correct and executable."
        verification_result = self.verifier.verify_claim(
            claim=claim,
            runtime_test=lambda: self.check_syntax(temp_file_path),
            trust_level=self.monitor.trust_level
        )

        # Step 4: Monitor (The 'Gut')
        # The monitor's state is updated based on the verification outcome
        self.monitor.step()

        # Step 5: Decide
        logger.info("Step 5: Making a decision on the candidate code.")
        if verification_result.get("verified") and verification_result.get("runtime_output") is True:
            logger.info("Verification successful. The refactoring is valid.")
            
            # Promote the temporary file to the main file
            os.rename(temp_file_path, self.target_file)
            logger.info(f"SUCCESS: {self.target_file} has been updated.")
            self.monitor.trust_level = min(1.0, self.monitor.trust_level * 1.05) # Increase trust

            # Generate the Quantum Gene for this evolution
            logger.info("Generating Quantum Gene for this successful evolution...")
            with open(self.target_file, 'r') as f:
                current_code = f.read()
            
            code_hash = hashlib.sha256(current_code.encode()).hexdigest()

            gene_data = {
                'trust_level': self.monitor.trust_level,
                'code_hash': code_hash,
                'refactoring_history': self.refactorer.refactoring_history,
                'target_file': self.target_file,
                'evolution_timestamp': datetime.now().isoformat()
            }

            quantum_gene = QuantumGene(state_data=gene_data)
            gene_path = quantum_gene.encode_to_qr()
            logger.info(f"🧬 Quantum Gene saved to: {gene_path}")
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
    orchestrator = QuantumOrchestrator(target_file=target)
    
    # If a target is specified via command-line, run once. Otherwise, loop for autonomous evolution.
    if len(sys.argv) > 1:
        # Run one cycle for targeted evolution (e.g., from Genesis Chamber) and exit.
        orchestrator.run_evolution_cycle()
    else:
        # Run evolution cycles continuously for autonomous self-evolution.
        while True:
            try:
                orchestrator.run_evolution_cycle()
                # Wait for a configured interval before the next cycle
                # Set to 1 hour (3600s) for autonomous operation, shorter for testing.
                sleep_interval = 10 
                logger.info(f"Cycle complete. Waiting for {sleep_interval} seconds before next cycle...")
                time.sleep(sleep_interval)
            except KeyboardInterrupt:
                logger.info("Autonomous evolution loop terminated by user.")
                break
            except Exception as e:
                logger.error(f"An unexpected error occurred during the evolution cycle: {e}", exc_info=True)
                logger.info("Attempting to recover. Waiting 60 seconds before next cycle...")
                time.sleep(60)
    
    # Export the verification logs
    orchestrator.verifier.export_logs()

if __name__ == "__main__":
    main()
