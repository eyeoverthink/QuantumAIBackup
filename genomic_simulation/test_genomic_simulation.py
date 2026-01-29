import os
from genomic_simulation.digital_dna import DigitalDNA
from genomic_simulation.environment import Environment
from genomic_simulation.simulator import Simulator

def run_simulation_test():
    """Demonstrates the Genomic Simulation system."""
    print("--- Genomic Simulation Test ---")

    # 1. Load the Digital DNA
    # We use an existing genome file as the basis for our organism.
    genome_path = "qr_phi_hanoi_genome.json"
    if not os.path.exists(genome_path):
        print(f"Error: Genome file not found at '{genome_path}'.")
        print("Please run the qr_genome_phi_hanoi.py script first to generate it.")
        return

    dna = DigitalDNA(genome_filepath=genome_path)

    # 2. Define two different environments
    env_rich = Environment(resource_level=0.9, resonance_field=0.62)
    env_poor = Environment(resource_level=0.2, resonance_field=0.15)

    # --- Simulation 1: Rich Environment ---
    print("\n--- Running Simulation in a RICH Environment ---")
    simulator_rich = Simulator(dna, env_rich)
    simulator_rich.print_simulation_setup()
    phenotype_rich = simulator_rich.run()
    print(phenotype_rich.get_summary())

    # --- Simulation 2: Poor Environment ---
    print("\n\n--- Running Simulation in a POOR Environment ---")
    simulator_poor = Simulator(dna, env_poor)
    simulator_poor.print_simulation_setup()
    phenotype_poor = simulator_poor.run()
    print(phenotype_poor.get_summary())
    
    print("\n\n--- Test Comparison ---")
    print("Notice how the same DNA produces a different phenotype based on the environment.")
    print(f"Rich Env Metabolism: {phenotype_rich.expressed_traits['metabolic_rate']:.4f}")
    print(f"Poor Env Metabolism: {phenotype_poor.expressed_traits['metabolic_rate']:.4f}")
    print("Test complete.")

if __name__ == "__main__":
    run_simulation_test()
