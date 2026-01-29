import json
import uuid
import datetime
import numpy as np
from typing import List, Dict, Any

from .phi_bit import PhiBit

class MemoryGenome:
    """
    Represents a sequence of Phi-bits, forming a complete memory unit or "genome."
    This class handles the encoding of raw data into a quantum-inspired format.
    """
    def __init__(self, data: str, genome_id: str = None, timestamp: str = None):
        """
        Initializes and encodes a memory genome from input data.

        Args:
            data (str): The string data to be encoded.
            genome_id (str, optional): Existing UUID. If None, a new one is created.
            timestamp (str, optional): Existing timestamp. If None, a new one is created.
        """
        self.data = data
        self.genome_id = genome_id or str(uuid.uuid4())
        self.timestamp = timestamp or datetime.datetime.utcnow().isoformat()
        
        self.phibit_sequence: List[PhiBit] = self._encode(data)
        self.average_resonance = self._calculate_average_resonance()
        self.genome_vector = self._calculate_genome_vector()

    def _encode(self, data: str) -> List[PhiBit]:
        """
        Encodes a string into a sequence of Phi-bits.
        Each character's ordinal value is used as the seed for a Phi-bit.
        """
        if not isinstance(data, str):
            raise TypeError("Input data must be a string.")
        return [PhiBit(seed=ord(char)) for char in data]

    def _calculate_average_resonance(self) -> float:
        """Calculates the average resonance across all Phi-bits in the sequence."""
        if not self.phibit_sequence:
            return 0.0
        return sum(p.resonance for p in self.phibit_sequence) / len(self.phibit_sequence)

    def _calculate_genome_vector(self) -> np.ndarray:
        """
        Calculates a 6D vector representing the genome.
        This vector consists of the mean and standard deviation of the Phi-bit vectors,
        providing a richer representation of the memory's structure.
        """
        if not self.phibit_sequence:
            return np.zeros(6)
        
        vectors = [p.vector for p in self.phibit_sequence]
        mean_vector = np.mean(vectors, axis=0)
        std_vector = np.std(vectors, axis=0)
        
        return np.concatenate([mean_vector, std_vector])

    def __repr__(self) -> str:
        return (
            f"MemoryGenome(id={self.genome_id}, chars={len(self.data)}, "
            f"avg_resonance={self.average_resonance:.6f})"
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serializes the MemoryGenome to a dictionary."""
        return {
            'genome_id': self.genome_id,
            'timestamp': self.timestamp,
            'data': self.data,
            'phibit_sequence': [p.to_dict() for p in self.phibit_sequence],
            'average_resonance': self.average_resonance,
            'genome_vector': self.genome_vector.tolist()
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """Deserializes a MemoryGenome from a dictionary."""
        genome = cls(data['data'], genome_id=data['genome_id'], timestamp=data['timestamp'])
        # Re-construct Phi-bits to ensure consistency
        genome.phibit_sequence = [PhiBit.from_dict(pd) for pd in data['phibit_sequence']]
        genome.average_resonance = data['average_resonance']
        genome.genome_vector = np.array(data['genome_vector'])
        return genome
