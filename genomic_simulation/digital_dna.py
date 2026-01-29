import json
from typing import Dict, Any, List

class DigitalDNA:
    """
    Loads and represents a digital genome from a JSON file.
    This class provides a structured interface to the genetic information,
    making it accessible for the simulation.
    """
    def __init__(self, genome_filepath: str):
        """
        Initializes the DigitalDNA by loading from a file.

        Args:
            genome_filepath (str): The path to the genome JSON file.

        Raises:
            FileNotFoundError: If the genome file does not exist.
            ValueError: If the genome file is not valid JSON or is missing key fields.
        """
        self.filepath = genome_filepath
        self.genome_data: Dict[str, Any] = self._load_genome()
        self._validate_genome()

    def _load_genome(self) -> Dict[str, Any]:
        """Loads the JSON data from the specified file."""
        try:
            with open(self.filepath, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Genome file not found at: {self.filepath}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in genome file: {self.filepath}")

    def _validate_genome(self):
        """Ensures the loaded genome has the required structure."""
        required_keys = ['genome_id', 'phi_metadata', 'codons']
        for key in required_keys:
            if key not in self.genome_data:
                raise ValueError(f"Genome is missing required key: '{key}'")

    @property
    def genome_id(self) -> str:
        """Returns the unique ID of the genome."""
        return self.genome_data.get('genome_id', 'N/A')

    @property
    def phi_metadata(self) -> Dict[str, Any]:
        """Returns the phi-harmonic metadata of the genome."""
        return self.genome_data.get('phi_metadata', {})

    @property
    def codons(self) -> List[Dict[str, Any]]:
        """Returns the list of codons (genes) in the genome."""
        return self.genome_data.get('codons', [])

    def __repr__(self) -> str:
        return (
            f"DigitalDNA(id={self.genome_id}, "
            f"complexity={self.phi_metadata.get('complexity_level', 'N/A')}, "
            f"codons={len(self.codons)})"
        )
