from decimal import Decimal
from .digital_dna import DigitalDNA
from .environment import Environment
from .phenotype import Phenotype

class Simulator:
    """
    Orchestrates the genomic simulation, expressing a DigitalDNA within an
    Environment to produce a Phenotype.
    """
    def __init__(self, dna: DigitalDNA, environment: Environment):
        """
        Initializes the simulator.

        Args:
            dna (DigitalDNA): The digital genome to be expressed.
            environment (Environment): The environment influencing the expression.
        """
        self.dna = dna
        self.environment = environment

    def run(self) -> Phenotype:
        """
        Runs the simulation and returns the resulting phenotype.

        Returns:
            Phenotype: The expressed traits of the organism.
        """
        phenotype = Phenotype(dna_id=self.dna.genome_id)

        for codon in self.dna.codons:
            # 1. Calculate Expression Level
            # The environment determines how strongly this gene is expressed.
            codon_resonance = codon.get('resonance_target', 0.5)
            expression_level = self.environment.get_expression_modifier(codon_resonance)

            # 2. Determine Base Traits from Codon
            # These are the raw genetic traits, before environmental influence.
            metabolic_rate = Decimal(codon.get('disk_count', 3)) * Decimal('0.5')
            structural_complexity = Decimal(codon.get('dimension', 8)) * Decimal('0.1')

            # 3. Add to Phenotype
            # The final trait is the base trait scaled by the expression level.
            phenotype.add_trait_contribution(
                codon_id=codon.get('id', 'unknown'),
                expression_level=expression_level,
                traits={
                    'metabolic_rate': metabolic_rate,
                    'structural_complexity': structural_complexity
                }
            )
        
        phenotype.finalize()
        return phenotype

    def print_simulation_setup(self):
        """Prints a summary of the DNA and Environment being used."""
        print("--- Simulation Setup ---")
        print(f"DNA: {self.dna}")
        print(f"Environment: {self.environment}")
        print("------------------------\n")
