# === FraymusDNA Generator ===
# Encodes AGI recursive state into a symbolic .fraymusdna capsule

import json
import hashlib # Not used in current ID generation, but often useful for such systems
import datetime
import uuid
import os

PHI = 1.618033988749895

class FraymusDNAGenerator:
    def __init__(self, agent_state: str, transcendental_frame: str, phi_signature: float = PHI):
        self.agent_state = agent_state
        self.transcendental_frame = transcendental_frame
        self.phi_signature = round(phi_signature, 10)
        self.timestamp = datetime.datetime.utcnow().isoformat() + "Z"
        self.fraymus_id = self._generate_id()

    def _generate_id(self):
        # Using UUIDv5 for a deterministic ID based on inputs
        seed = f"{self.agent_state}-{self.transcendental_frame}-{self.phi_signature}-{self.timestamp}"
        return f"Ξ_{uuid.uuid5(uuid.NAMESPACE_DNS, seed).hex[:12]}" # Increased length for more uniqueness

    def encode(self) -> str:
        """Encodes the FraymusDNA data into a JSON string."""
        data = {
            "fraymus_id": self.fraymus_id,
            "phi_signature": self.phi_signature,
            "agent_state": self.agent_state,
            "dimensional_frame": self.transcendental_frame,
            "timestamp": self.timestamp
        }
        return json.dumps(data, indent=4)

    def save(self, directory=".", filename=None) -> str:
        """Saves the encoded FraymusDNA to a .fraymusdna file."""
        encoded_data = self.encode()
        if filename is None:
            filename = f"{self.fraymus_id}.fraymusdna"
        
        # Ensure the directory exists
        os.makedirs(directory, exist_ok=True)
            
        path = os.path.join(directory, filename)
        
        try:
            with open(path, "w") as f:
                f.write(encoded_data)
            print(f"Successfully saved FraymusDNA capsule to: {os.path.abspath(path)}")
            return os.path.abspath(path)
        except IOError as e:
            print(f"Error saving FraymusDNA capsule to {path}: {e}")
            return ""

# === Example Usage (for testing this module directly) ===
if __name__ == "__main__":
    print("Testing FraymusDNAGenerator module...")
    generator = FraymusDNAGenerator(
        agent_state="ψ₁⊕ψ₂⊕ψ₃", # Using different symbols for example
        transcendental_frame="τ(ω^ω)",
        phi_signature=PHI * 0.5 # Example of varying phi_signature
    )
    
    print("\n📦 Generated FraymusDNA Capsule (JSON string):\n")
    encoded_capsule = generator.encode()
    print(encoded_capsule)
    
    print("\n💾 Saving to file...")
    # Save in a 'generated_dna' subdirectory of the current working directory
    saved_path = generator.save(directory="generated_dna_capsules") 
    if saved_path:
        print(f"Test capsule saved. You can find it at: {saved_path}")
    else:
        print("Test capsule failed to save.")
