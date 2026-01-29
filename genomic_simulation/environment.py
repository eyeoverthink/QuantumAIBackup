from decimal import Decimal, getcontext

getcontext().prec = 50
PHI = (Decimal(1) + Decimal(5).sqrt()) / Decimal(2)

class Environment:
    """
    Defines the environmental conditions that influence genome expression.
    """
    def __init__(self, resource_level: float, resonance_field: float):
        """
        Initializes the simulation environment.

        Args:
            resource_level (float): A value from 0.0 to 1.0 indicating the
                                    availability of resources.
            resonance_field (float): A value from 0.0 to 1.0 representing the
                                     ambient phi-harmonic resonance.
        """
        if not (0.0 <= resource_level <= 1.0):
            raise ValueError("Resource level must be between 0.0 and 1.0")
        if not (0.0 <= resonance_field <= 1.0):
            raise ValueError("Resonance field must be between 0.0 and 1.0")

        self.resource_level = Decimal(str(resource_level))
        self.resonance_field = Decimal(str(resonance_field))

    def get_expression_modifier(self, codon_resonance_target: float) -> Decimal:
        """
        Calculates a modifier for gene expression based on resonance alignment.

        The modifier is higher when the codon's target resonance is closer to the
        environment's resonance field.

        Args:
            codon_resonance_target (float): The target resonance of a specific codon.

        Returns:
            Decimal: A modifier value, typically around 1.0.
        """
        target = Decimal(str(codon_resonance_target))
        # Calculate the difference, wrapping around the circle (mod 1)
        diff = abs(self.resonance_field - target)
        resonance_alignment = Decimal(1) - min(diff, Decimal(1) - diff)
        
        # Combine with resource level. High resources and high alignment = max expression.
        modifier = (self.resource_level + resonance_alignment) / Decimal(2)
        return modifier

    def __repr__(self) -> str:
        return (
            f"Environment(resources={self.resource_level:.2f}, "
            f"resonance_field={self.resonance_field:.6f})"
        )
