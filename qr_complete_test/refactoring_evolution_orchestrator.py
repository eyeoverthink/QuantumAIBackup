import os
import sys
import hashlib

# --- Import the Lego bricks ---

# 1. The Refactoring Tools
from qr_phi_meta_refactorer_v2_standalone import QuantumPhiMetaRefactorer as RefactorerV2
from qr_phi_meta_refactorer_robust import QuantumPhiMetaRefactorer as RefactorerRobust

# 2. The Predictive Simulator
from genomic_simulation.digital_dna import DigitalDNA
from genomic_simulation.environment import Environment
from genomic_simulation.simulator import Simulator

# 3. The Wisdom Keeper
from quantum_memory.memory_bank import MemoryBank
from quantum_memory.memory_genome import MemoryGenome

# 4. The Secure Logger
from time_based_hashing.hash_chain import HashChain

class RefactoringEvolutionOrchestrator:
    """
    An intelligent orchestrator that uses simulation and memory to guide
    phi-harmonic code refactoring and securely logs the process.
    """
    def __init__(self, memory_path: str, log_chain: HashChain):
        self.memory_bank = MemoryBank(filepath=memory_path)
        self.log_chain = log_chain
        print("Refactoring Evolution Orchestrator Initialized.")
        print(f"  - Using Memory Bank at: {memory_path}")
        print(f"  - Attached to Hash Chain with {len(log_chain.chain)} blocks.")

    def evolve_script(self, file_path: str):
        """
        Analyzes, simulates, refactors, and logs the evolution of a single script.
        """
        print(f"\n--- Starting Evolution for: {file_path} ---")
        if not os.path.exists(file_path):
            print(f"Error: File not found at {file_path}")
            return

        with open(file_path, 'r') as f:
            original_code = f.read()
        
        original_hash = hashlib.sha256(original_code.encode()).hexdigest()
        print(f"Original Code Hash: {original_hash[:16]}...")

        # 1. Query memory for past wisdom (future implementation)
        wisdom = self.memory_bank.query(original_hash, top_k=1)
        if wisdom:
            print(f"Found past wisdom for similar code: {wisdom[0]}")

        # 2. Run both refactorers to get potential futures
        print("\n[Step 1/3] Generating potential refactorings...")
        refactorer_v2 = RefactorerV2(debug=False)
        refactored_code_v2, score_v2 = refactorer_v2.load_and_refactor_file(file_path)

        refactorer_robust = RefactorerRobust(file_path, debug=False)
        refactored_code_robust, score_robust = refactorer_robust.perform_all_refactorings()
        
        print(f"  - V2 proposal score: {score_v2:.4f}")
        print(f"  - Robust proposal score: {score_robust:.4f}")

        # 3. Simulate the fitness of each potential refactoring
        print("\n[Step 2/3] Simulating fitness of each proposal...")
        fitness_v2 = self._simulate_fitness(refactored_code_v2, score_v2)
        fitness_robust = self._simulate_fitness(refactored_code_robust, score_robust)

        print(f"  - V2 simulated fitness (metabolic rate): {fitness_v2:.4f}")
        print(f"  - Robust simulated fitness (metabolic rate): {fitness_robust:.4f}")

        # 4. Choose the best one based on simulated fitness
        if fitness_v2 > fitness_robust and score_v2 > 0:
            print("\n[Step 3/3] Decision: V2 refactoring is superior. Applying changes.")
            winner = refactorer_v2
            final_code = refactored_code_v2
            choice = "v2"
        elif fitness_robust > fitness_v2 and score_robust > 0:
            print("\n[Step 3/3] Decision: Robust refactoring is superior. Applying changes.")
            winner = refactorer_robust
            final_code = refactored_code_robust
            choice = "robust"
        else:
            print("\n[Step 3/3] Decision: No significant improvement found. No changes will be applied.")
            return

        # 5. Save the new code
        output_path = winner.save_refactored_code()
        new_hash = hashlib.sha256(final_code.encode()).hexdigest()

        # 6. Log the entire operation
        log_data = {
            "event": "CodeEvolution",
            "file_path": file_path,
            "original_hash": original_hash,
            "new_hash": new_hash,
            "chosen_refactorer": choice,
            "v2_score": f"{score_v2:.4f}",
            "robust_score": f"{score_robust:.4f}",
            "v2_fitness": f"{fitness_v2:.4f}",
            "robust_fitness": f"{fitness_robust:.4f}",
            "output_path": output_path
        }
        self.log_chain.add_block(str(log_data))
        print(f"Evolutionary step securely logged in HashChain.")

        # 7. Update memory with the result
        wisdom_genome = MemoryGenome(data=f"Refactored {original_hash[:8]}: chose {choice} with fitness {max(fitness_v2, fitness_robust):.4f}")
        self.memory_bank.add_genome(wisdom_genome)
        print("Outcome stored in MemoryBank for future wisdom.")

    def _simulate_fitness(self, code: str, improvement_score: float) -> float:
        """Uses GenomicSimulation to predict the fitness of refactored code."""
        if not code.strip() or improvement_score == 0:
            return 0.0

        # Create a temporary genome file from the code's structure
        genome_data = self._code_to_genome_json(code)
        temp_genome_path = "/tmp/temp_refactor_genome.json"
        with open(temp_genome_path, 'w') as f:
            f.write(genome_data)

        dna = DigitalDNA(temp_genome_path)
        
        # The improvement score from the refactorer creates the environment
        # A better refactoring job creates a richer environment
        environment = Environment(resource_level=improvement_score, resonance_field=improvement_score * 0.5)
        
        simulator = Simulator(dna, environment)
        phenotype = simulator.run()

        os.remove(temp_genome_path)
        
        # The 'metabolic_rate' of the phenotype represents the code's fitness
        return float(phenotype.expressed_traits.get('metabolic_rate', 0.0))

    def _code_to_genome_json(self, code: str) -> str:
        """Converts a Python code string to a JSON string for DigitalDNA."""
        import ast
        import json

        try:
            tree = ast.parse(code)
        except SyntaxError:
            return json.dumps({
                "genome_id": "invalid_syntax_genome",
                "phi_metadata": {
                    "version": "1.0",
                    "source": "RefactoringEvolutionOrchestrator",
                    "error": "SyntaxError in input code"
                },
                "codons": []
            })

        codons = []
        for i, node in enumerate(ast.walk(tree)):
            codon = {
                "id": f"node_{i}_{type(node).__name__}",
                "type": type(node).__name__,
                "complexity": 1,
                "dependencies": [],
                "traits": {"structural_complexity": 1, "metabolic_rate": 0.5}
            }
            if isinstance(node, ast.FunctionDef):
                codon['traits']['metabolic_rate'] = 2.0 # Functions are active
                codon['complexity'] = len(node.body)
            elif isinstance(node, ast.ClassDef):
                codon['traits']['structural_complexity'] = 5.0 # Classes add structure
                codon['complexity'] = len(node.body)
            codons.append(codon)

        genome = {
            "genome_id": "refactored_code_genome",
            "phi_metadata": {
                "version": "1.0",
                "source": "RefactoringEvolutionOrchestrator"
            },
            "codons": codons
        }
        return json.dumps(genome, indent=2)

def main():
    """
    Main function to run the orchestrator.
    """
    if len(sys.argv) < 2:
        print("Usage: python refactoring_evolution_orchestrator.py <path_to_script_to_evolve>")
        sys.exit(1)

    target_script_path = sys.argv[1]

    # Initialize the shared systems
    shared_log_chain = HashChain()
    shared_memory_bank_path = "/tmp/refactoring_wisdom.json"

    # Create the orchestrator
    orchestrator = RefactoringEvolutionOrchestrator(
        memory_path=shared_memory_bank_path,
        log_chain=shared_log_chain
    )

    # Evolve the target script
    orchestrator.evolve_script(target_script_path)

    # Verify the integrity of the log
    print("\n--- Final Log Chain State ---")
    print(shared_log_chain.to_json())
    print(f"Is chain valid? {shared_log_chain.is_chain_valid()}")

if __name__ == "__main__":
    main()
