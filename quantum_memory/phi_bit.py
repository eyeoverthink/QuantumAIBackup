import numpy as np
from decimal import Decimal, getcontext

# --- Constants ---
getcontext().prec = 50
PHI = (Decimal(1) + Decimal(5).sqrt()) / Decimal(2)
PI = Decimal('3.14159265358979323846264338327950288419716939937510')
E = Decimal('2.71828182845904523536028747135266249775724709369995')

class PhiBit:
    """
    Represents a Phi-bit, a multi-dimensional quantum-inspired memory unit.
    A Phi-bit's state is not a simple 0 or 1, but a vector defined by its
    resonance with fundamental mathematical constants.
    """
    def __init__(self, seed: int):
        """
        Initializes the Phi-bit from a numerical seed.

        Args:
            seed (int): An integer used to generate the resonance vector.
        """
        if not isinstance(seed, int):
            raise TypeError("Seed must be an integer.")
        self.seed = Decimal(seed)
        self.vector = self._generate_vector()
        self.resonance = self._calculate_resonance()

    def _generate_vector(self) -> np.ndarray:
        """
        Generates the multi-dimensional resonance vector.
        The vector components are the fractional parts of the products of the
        seed with PHI, PI, and E.
        """
        phi_res = (self.seed * PHI) % 1
        pi_res = (self.seed * PI) % 1
        e_res = (self.seed * E) % 1
        return np.array([float(phi_res), float(pi_res), float(e_res)])

    def _calculate_resonance(self) -> float:
        """
        Calculates the combined resonance of the vector.
        A lower value indicates higher resonance (closer to zero).
        This is a simple average of the vector components.
        """
        return float(np.mean(self.vector))

    def __repr__(self) -> str:
        return f"PhiBit(seed={int(self.seed)}, vector={self.vector}, resonance={self.resonance:.6f})"

    def to_dict(self) -> dict:
        """Serializes the Phi-bit to a dictionary."""
        return {
            'seed': int(self.seed),
            'vector': self.vector.tolist(),
            'resonance': self.resonance
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Deserializes a Phi-bit from a dictionary."""
        phibit = cls(data['seed'])
        phibit.vector = np.array(data['vector'])
        phibit.resonance = data['resonance']
        return phibit
