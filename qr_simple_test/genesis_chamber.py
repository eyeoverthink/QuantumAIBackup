import logging
import os
import subprocess
import time
import hashlib
from quantum_test_runner import QuantumTestRunner
from quantum_gene import QuantumGene
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f"genesis_chamber_{datetime.now().strftime('%Y%m%d%H%M%S')}.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("GenesisChamber")

class GenesisChamber:
    """
    An experimental framework to evolve code to solve a specific, testable problem.
    """

    def __init__(self, problem_file: str, test_module: str, max_evolutions: int = 10):
        if not os.path.exists(problem_file):
            raise FileNotFoundError(f"Problem file not found: {problem_file}")
        
        self.problem_file = problem_file
        self.test_module = test_module
        self.max_evolutions = max_evolutions
        self.test_runner = QuantumTestRunner(test_module_name=self.test_module)
        self.evolution_count = 0

    def run_experiment(self):
        """
        Starts the evolution process to solve the defined problem.
        """
        logger.info("=== Starting Genesis Chamber Experiment ===")
        logger.info(f"Problem File: {self.problem_file}")
        logger.info(f"Test Module: {self.test_module}")
        logger.info("-----------------------------------------")

        while self.evolution_count < self.max_evolutions:
            self.evolution_count += 1
            logger.info(f"--- Evolution Cycle {self.evolution_count}/{self.max_evolutions} ---")

            # Step 1: Test the current state of the code
            logger.info("Running tests on current code...")
            test_passed = self.test_runner.run_tests()

            if test_passed:
                logger.info("🎉 SUCCESS: The code has evolved to pass all tests!")
                self.generate_solver_gene()
                return True

            # Step 2: If tests fail, evolve the code
            logger.info("Tests failed. Initiating evolution with Quantum Orchestrator...")
            self.evolve_code()

            # Give a moment for file system to catch up
            time.sleep(1)

        logger.warning(f"Experiment finished after {self.max_evolutions} cycles. The solution was not found.")
        return False

    def evolve_code(self):
        """
        Invokes the Quantum Orchestrator as a subprocess to evolve the problem file.
        """
        try:
            command = ["python3", "quantum_orchestrator.py", self.problem_file]
            process = subprocess.run(command, capture_output=True, text=True, check=True)
            logger.info("Quantum Orchestrator executed successfully.")
            logger.debug(f"Orchestrator STDOUT:\n{process.stdout}")
            if process.stderr:
                logger.warning(f"Orchestrator STDERR:\n{process.stderr}")
        except subprocess.CalledProcessError as e:
            logger.error(f"Quantum Orchestrator failed to execute.", exc_info=True)
            logger.error(f"STDOUT: {e.stdout}")
            logger.error(f"STDERR: {e.stderr}")
        except FileNotFoundError:
            logger.error("Could not find 'python3'. Please ensure it is in your PATH.")

    def generate_solver_gene(self):
        """
        Generates a 'Solver Gene' QR code containing the solution's DNA.
        """
        logger.info("Generating Solver Gene for the solution...")
        try:
            with open(self.problem_file, 'r') as f:
                solution_code = f.read()
            
            code_hash = hashlib.sha256(solution_code.encode()).hexdigest()

            gene_data = {
                'solver_gene': True,
                'problem_file': self.problem_file,
                'test_module': self.test_module,
                'code_hash': code_hash,
                'evolution_cycles': self.evolution_count,
                'solution_timestamp': datetime.now().isoformat()
            }

            quantum_gene = QuantumGene(state_data=gene_data)
            gene_path = quantum_gene.encode_to_qr(output_dir="solver_genes")
            logger.info(f"🧬 Solver Gene saved to: {gene_path}")

        except Exception as e:
            logger.error(f"Failed to generate Solver Gene: {e}", exc_info=True)

def main():
    """Defines and runs the checkers puzzle experiment."""
    problem = "checkers_problem_adapter.py"
    test = "test_checkers_adapter"

    if os.path.exists(problem):
        # We will limit the evolutions for this first run to see the process.
        chamber = GenesisChamber(problem_file=problem, test_module=test, max_evolutions=5)
        chamber.run_experiment()
    else:
        logger.error(f"Cannot start experiment: Problem file '{problem}' does not exist.")

if __name__ == "__main__":
    main()
