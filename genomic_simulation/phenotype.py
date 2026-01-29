from typing import List, Dict
from decimal import Decimal

class Phenotype:
    """
    Represents the observable traits of an organism, resulting from the
    expression of its DigitalDNA within a specific Environment.
    """
    def __init__(self, dna_id: str):
        """
        Initializes the Phenotype.

        Args:
            dna_id (str): The ID of the genome that this phenotype expresses.
        """
        self.dna_id = dna_id
        self.expressed_traits: Dict[str, Decimal] = {
            'metabolic_rate': Decimal('0'),
            'structural_complexity': Decimal('0'),
            'total_expression_level': Decimal('0')
        }
        self.codon_contributions: List[Dict] = []

    def add_trait_contribution(self, codon_id: str, expression_level: Decimal, traits: Dict[str, Decimal]):
        """
        Adds the contribution of a single expressed codon to the phenotype.

        Args:
            codon_id (str): The ID of the codon being expressed.
            expression_level (Decimal): The calculated expression level for this codon.
            traits (Dict[str, Decimal]): The traits derived from this codon.
        """
        self.codon_contributions.append({
            'codon_id': codon_id,
            'expression_level': expression_level,
            'traits': traits
        })
        
        # Aggregate the traits
        self.expressed_traits['metabolic_rate'] += traits.get('metabolic_rate', Decimal('0')) * expression_level
        self.expressed_traits['structural_complexity'] += traits.get('structural_complexity', Decimal('0')) * expression_level
        self.expressed_traits['total_expression_level'] += expression_level

    def finalize(self):
        """
        Normalizes the final traits after all codons have been processed.
        """
        num_codons = Decimal(len(self.codon_contributions))
        if num_codons > 0:
            # Average the total expression level
            self.expressed_traits['total_expression_level'] /= num_codons

    def __repr__(self) -> str:
        return (
            f"Phenotype(dna_id={self.dna_id}, "
            f"metabolism={self.expressed_traits['metabolic_rate']:.4f}, "
            f"complexity={self.expressed_traits['structural_complexity']:.4f})"
        )

    def get_summary(self) -> str:
        """
        Returns a detailed string summary of the phenotype.
        """
        summary = [f"--- Phenotype Summary for DNA: {self.dna_id} ---"]
        summary.append(f"  Metabolic Rate: {self.expressed_traits['metabolic_rate']:.4f}")
        summary.append(f"  Structural Complexity: {self.expressed_traits['structural_complexity']:.4f}")
        summary.append(f"  Avg. Expression Level: {self.expressed_traits['total_expression_level']:.4f}")
        summary.append("  Codon Contributions:")
        for contrib in self.codon_contributions:
            summary.append(
                f"    - {contrib['codon_id']}: Expression={contrib['expression_level']:.3f}, "
                f"Metabolism={contrib['traits']['metabolic_rate']:.2f}, "
                f"Complexity={contrib['traits']['structural_complexity']:.2f}"
            )
        return "\n".join(summary)
