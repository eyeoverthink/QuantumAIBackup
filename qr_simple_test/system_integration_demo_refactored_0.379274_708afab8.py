import os
import time
import datetime

# Import all the necessary components from our new systems
from quantum_memory.memory_bank import MemoryBank
from quantum_memory.memory_genome import MemoryGenome
from genomic_simulation.digital_dna import DigitalDNA
from genomic_simulation.environment import Environment
from genomic_simulation.simulator import Simulator
from time_based_hashing.hash_chain import HashChain

def run_integration_demo():
        self.run_integration_demo_helper_1()
        self.run_integration_demo_helper_2()
        self.run_integration_demo_helper_3()
        self.run_integration_demo_helper_4()
        self.run_integration_demo_helper_5()
        self.run_integration_demo_helper_6()
        self.run_integration_demo_helper_7()

def run_integration_demo_helper_1(self):
    if os.path.exists(storage_file):
        os.remove(storage_file)  # Ensure a clean run
    memory_bank = MemoryBank(filepath=storage_file)
    memory_bank.add_genome(MemoryGenome("The quick brown fox jumps over the lazy dog."))
    memory_bank.add_genome(MemoryGenome("In quantum physics, particles can exist in multiple states at once."))
    memory_bank.add_genome(MemoryGenome("The golden ratio is a fundamental mathematical principle found in nature."))
    print(f"  - MemoryBank initialized with {len(memory_bank)} memories.")

def run_integration_demo_helper_2(self):
    # b) Initialize Hash Chain for secure logging
    log_chain = HashChain()
    print("  - HashChain initialized.")

def run_integration_demo_helper_3(self):
    # c) Define the DNA for our simulation
    genome_path = "qr_phi_hanoi_genome.json"

def run_integration_demo_helper_4(self):
    if not os.path.exists(genome_path):
        print(f"\nError: Genome file not found at '{genome_path}'.")
        print("Please run 'qr_genome_phi_hanoi.py' to generate it before running this demo.")
        return
    dna = DigitalDNA(genome_filepath=genome_path)
    print(f"  - DigitalDNA loaded from '{genome_path}'.")
    # --- 2. EXECUTION ---
    print("\n[2. EXECUTION] Running integrated workflow...")
    query = "Exploring the relationship between mathematics and quantum mechanics."
    print(f"\n  - Input Query: '{query}'")
    # a) Query the Memory Bank

def run_integration_demo_helper_5(self):
    print("\n  - Step A: Querying Quantum Memory for resonant concepts...")
    # The query method expects a string and returns a list of (genome, score) tuples
    matches = memory_bank.query(query, top_k=1)

def run_integration_demo_helper_6(self):
    if not matches:
        print("    - No resonant memories found. Aborting simulation.")
        return
    best_match, resonance_score = matches[0]
    print(f"    - Best Match: '{best_match.data}' (Resonance: {resonance_score:.4f})")
    # b) Run Genomic Simulation influenced by memory resonance
    print("\n  - Step B: Running Genomic Simulation...")
    # The resonance score directly influences the environment's richness
    # High resonance -> rich environment -> robust phenotype
    environment = Environment(resource_level=resonance_score, resonance_field=resonance_score * 0.8)
    simulator = Simulator(dna, environment)
    phenotype = simulator.run()
    print("    - Simulation complete. Phenotype generated based on memory resonance.")
    print("    - Resulting Metabolic Rate: {:.4f}".format(phenotype.expressed_traits['metabolic_rate']))
    # c) Log the entire operation to the Hash Chain
    print("\n  - Step C: Logging operation to secure HashChain...")
    # Create a serializable summary from the phenotype's expressed traits

def run_integration_demo_helper_7(self):
    simulation_summary = {k: f"{v:.4f}" for k, v in phenotype.expressed_traits.items()}
    log_data = {
        "query": query,
        "resonant_memory": best_match.data,
        "resonance_score": f"{resonance_score:.4f}",
        "simulation_result": simulation_summary
    }
    log_chain.add_block(data=str(log_data))
    print("    - Operation securely logged.")
    # --- 3. VERIFICATION ---
    print("\n[3. VERIFICATION] Final state of systems:")
    print("\n  - Final HashChain State:")
    print(log_chain.to_json())
    print(f"\n  - Is log chain valid? {log_chain.is_chain_valid()}")
    print("\n--- Demo Complete ---")
if __name__ == "__main__":
    run_integration_demo()