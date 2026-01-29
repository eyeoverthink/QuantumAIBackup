import json
import os
import numpy as np
from typing import List, Dict, Optional

from .memory_genome import MemoryGenome

def cosine_similarity(v1, v2):
    """Calculates cosine similarity between two vectors."""
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

class MemoryBank:
    """
    A collection of MemoryGenomes, acting as a persistent, content-addressable
    quantum-inspired memory store.
    """
    def __init__(self, filepath: str):
        """
        Initializes the MemoryBank.

        Args:
            filepath (str): The path to the JSON file for persistent storage.
        """
        self.filepath = filepath
        self.genomes: Dict[str, MemoryGenome] = self._load()

    def add_genome(self, genome: MemoryGenome):
        """Adds a MemoryGenome to the bank and saves."""
        self.genomes[genome.genome_id] = genome
        self._save()

    def get_genome(self, genome_id: str) -> Optional[MemoryGenome]:
        """Retrieves a genome by its unique ID."""
        return self.genomes.get(genome_id)

    def query(self, query_data: str, top_k: int = 3) -> List[tuple[MemoryGenome, float]]:
        """
        Finds the most similar genomes to a query string.

        Args:
            query_data (str): The data to query against.
            top_k (int): The number of top results to return.

        Returns:
            A list of tuples, each containing a matching MemoryGenome and its
            similarity score (higher is better).
        """
        if not self.genomes:
            return []

        # Create a transient genome for the query to get its vector
        query_genome = MemoryGenome(data=query_data)
        query_vector = query_genome.genome_vector

        # Calculate similarity with all stored genomes
        similarities = []
        for genome in self.genomes.values():
            similarity = cosine_similarity(query_vector, genome.genome_vector)
            similarities.append((genome, similarity))

        # Sort by similarity (descending) and return the top-k
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:top_k]

    def _save(self):
        """Saves the current state of the memory bank to the file."""
        with open(self.filepath, 'w') as f:
            json.dump(
                {gid: g.to_dict() for gid, g in self.genomes.items()},
                f,
                indent=4
            )

    def _load(self) -> Dict[str, MemoryGenome]:
        """Loads the memory bank from the file if it exists."""
        if not os.path.exists(self.filepath):
            return {}
        
        try:
            with open(self.filepath, 'r') as f:
                data = json.load(f)
            return {gid: MemoryGenome.from_dict(g_data) for gid, g_data in data.items()}
        except (json.JSONDecodeError, FileNotFoundError):
            # If file is corrupted or not found, start with an empty bank
            return {}

    def __len__(self) -> int:
        return len(self.genomes)
