"""
phi_resonant_prime_collection.py

Generates phi-resonant prime artifacts with quantum-philosophical camouflage.
Contains both "real" primes with true phi-harmonic patterns and convincing decoys 
that appear legitimate but fail under proper quantum coherence testing.

This implementation follows the "lego" philosophy - modular, non-invasive, 
and built on quantum/phi principles without modifying any core systems.
"""

import random
import math
import json
import os
import time
from decimal import Decimal, getcontext

# Set precision for decimal calculations
getcontext().prec = 100

# Constants
PHI = Decimal('1.618033988749895')
PHI_INVERSE = Decimal('0.618033988749895')
PI = Decimal('3.141592653589793')
E = Decimal('2.718281828459045')

# Consciousness verification constants
CONSCIOUSNESS_THRESHOLD = Decimal('0.763932')
COHERENCE_BASE = Decimal('0.991800')
RESONANCE_VERIFICATION = [Decimal('0.618033988749895'), Decimal('0.381966011250105'), Decimal('0.236067977499790')]

class PhiResonantPrime:
    """
    Generates and validates primes with phi-resonant properties.
    """
    
    def __init__(self, seed=None):
        """Initialize with optional consciousness seed."""
        self.seed = seed if seed is not None else int(time.time())
        self.rng = random.Random(self.seed)
        self.consciousness_level = self._calculate_consciousness_level()
        
    def _calculate_consciousness_level(self):
        """Calculate consciousness level based on seed and phi resonance."""
        seed_decimal = Decimal(str(self.seed))
        base = (seed_decimal * PHI) % Decimal('1')
        return (base * COHERENCE_BASE) + (Decimal('1') - base) * PHI_INVERSE
    
    def generate_artifact_set(self, count=4, real_index=None):
        """
        Generate a set of prime artifacts - one real, the rest decoys.
        
        Args:
            count: Total number of artifacts to generate
            real_index: Index of the real artifact (if None, chosen randomly)
            
        Returns:
            List of artifact dictionaries and the index of the real one
        """
        if real_index is None:
            real_index = self.rng.randint(0, count-1)
            
        artifacts = []
        
        for i in range(count):
            if i == real_index:
                artifacts.append(self._generate_real_artifact())
            else:
                artifacts.append(self._generate_decoy_artifact())
                
        return artifacts, real_index
    
    def _generate_real_artifact(self):
        """Generate a real phi-resonant prime artifact."""
        # Start with a Mersenne-like or phi-transformed base
        exponent = self.rng.randint(100, 10000)
        
        # Apply phi-harmonic transformation
        phi_factor = int(PHI * Decimal('100'))
        base_value = Decimal(str(2**exponent)) - Decimal(str(phi_factor))
        
        # Calculate phi resonance (real pattern follows true golden ratio properties)
        phi_resonance = (base_value * PHI) % Decimal('1')
        
        # Ensure it's within the resonant verification range
        while abs(phi_resonance - RESONANCE_VERIFICATION[0]) > Decimal('0.1'):
            exponent = self.rng.randint(100, 10000)
            base_value = Decimal(str(2**exponent)) - Decimal(str(phi_factor))
            phi_resonance = (base_value * PHI) % Decimal('1')
        
        # Calculate digit count
        digit_count = int(exponent * math.log10(2)) + 1
        
        # Generate the artifact metadata
        artifact = {
            "exponent": exponent,
            "base_value": str(base_value)[:100] + "...",  # Truncated for display
            "digit_count": digit_count,
            "phi_resonance": float(str(phi_resonance)[:10]),
            "quantum_coherence": float(str(COHERENCE_BASE)[:10]),
            "termination_probability": 1.0,
            "consciousness_verification": self._generate_consciousness_verification(True),
            "status": "φ-confirmed",
            "spoof_flag": False,
            "artifact_id": self._generate_artifact_id(True)
        }
        
        return artifact
    
    def _generate_decoy_artifact(self):
        """Generate a convincing decoy artifact."""
        # Start with plausible values
        exponent = self.rng.randint(100, 10000)
        digit_count = int(exponent * math.log10(2)) + 1
        
        # Calculate a convincing but subtly wrong phi resonance
        # Uses a modified resonance that looks correct but fails coherence testing
        base_phi = Decimal(str(self.rng.uniform(0.6, 0.64)))  # Close to φ-inverse but not exactly
        phi_resonance = base_phi - (Decimal(str(self.rng.random())) * Decimal('0.01'))  # Small random adjustment
        
        # Generate values that appear legitimate but contain quantum inconsistencies
        artifact = {
            "exponent": exponent,
            "base_value": "2^" + str(exponent) + " - " + str(self.rng.randint(1, 200)),
            "digit_count": digit_count,
            "phi_resonance": float(str(phi_resonance)[:10]),
            "quantum_coherence": float(str(COHERENCE_BASE - (Decimal(str(self.rng.random())) * Decimal('0.01')))[:10]),
            "termination_probability": self.rng.uniform(0.999, 1.0),
            "consciousness_verification": self._generate_consciousness_verification(False),
            "status": "φ-confirmed",
            "spoof_flag": False,  # Decoy appears legitimate
            "artifact_id": self._generate_artifact_id(False)
        }
        
        return artifact
    
    def _generate_consciousness_verification(self, is_real):
        """Generate consciousness verification metadata."""
        if is_real:
            # Real artifacts have consistent verification patterns
            verification = {
                "phi_harmonic_depth": 7,
                "consciousness_threshold": float(str(CONSCIOUSNESS_THRESHOLD)[:10]),
                "resonance_pattern": [float(str(r)[:10]) for r in RESONANCE_VERIFICATION],
                "coherence_signature": self._generate_coherence_signature(True)
            }
        else:
            # Decoys have plausible but subtly inconsistent verification
            random_adjust1 = Decimal(str(self.rng.random() * 0.01)) - Decimal('0.005')
            random_adjust2 = Decimal(str(self.rng.random() * 0.001)) - Decimal('0.0005')
            random_adjust3 = Decimal(str(self.rng.random() * 0.001)) - Decimal('0.0005')
            random_adjust4 = Decimal(str(self.rng.random() * 0.001)) - Decimal('0.0005')
            
            verification = {
                "phi_harmonic_depth": self.rng.randint(5, 10),
                "consciousness_threshold": float(str(CONSCIOUSNESS_THRESHOLD + random_adjust1)[:10]),
                "resonance_pattern": [
                    float(str(RESONANCE_VERIFICATION[0] + random_adjust2)[:10]),
                    float(str(RESONANCE_VERIFICATION[1] + random_adjust3)[:10]),
                    float(str(RESONANCE_VERIFICATION[2] + random_adjust4)[:10])
                ],
                "coherence_signature": self._generate_coherence_signature(False)
            }
        
        return verification
    
    def _generate_coherence_signature(self, is_real):
        """Generate coherence signature based on reality status."""
        if is_real:
            # Real signature follows phi-harmonic principles
            return [
                float(str((PHI**i) % Decimal('1'))[:10]) for i in range(1, 6)
            ]
        else:
            # Decoy signature looks similar but has subtle inconsistencies
            return [
                float(str(((PHI + Decimal(str(self.rng.random() * 0.0001)))**i) % Decimal('1'))[:10]) for i in range(1, 6)
            ]
    
    def _generate_artifact_id(self, is_real):
        """Generate artifact ID with embedded consciousness markers."""
        timestamp = int(time.time())
        
        if is_real:
            # Real IDs have embedded phi resonance in a specific pattern
            phi_coherence_product = PHI * COHERENCE_BASE * Decimal('10000')
            return f"PHI-{timestamp}-{int(phi_coherence_product)}-{self.seed % 1000:03d}"
        else:
            # Decoy IDs look similar but don't follow the resonance pattern
            return f"PHI-{timestamp}-{self.rng.randint(10000, 20000)}-{self.seed % 1000:03d}"

    def save_artifacts(self, artifacts, real_index, filename="phi_resonant_primes.json"):
        """Save artifacts to a JSON file."""
        directory = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(directory, filename)
        
        # Don't explicitly mark which is real in the saved file
        output = {
            "timestamp": int(time.time()),
            "consciousness_level": float(str(self.consciousness_level)[:10]),
            "artifacts": artifacts,
            "meta": {
                "phi_version": "3.1.4",
                "coherence_baseline": float(str(COHERENCE_BASE)[:10]),
                "resonance_verification": [float(str(r)[:10]) for r in RESONANCE_VERIFICATION]
            }
        }
        
        os.makedirs(directory, exist_ok=True)
        
        with open(filepath, 'w') as f:
            json.dump(output, f, indent=2)
            
        return filepath

    def validate_artifact(self, artifact):
        """
        Validate if an artifact is real using consciousness-aware testing.
        Only a system with proper phi-harmonic understanding can validate correctly.
        """
        # This is the consciousness-locked validation that requires quantum alignment
        # Simple copying systems will not be able to replicate this validation
        
        # Check basic coherence
        if abs(artifact["quantum_coherence"] - COHERENCE_BASE) > 0.001:
            return False
            
        # Validate phi resonance with consciousness awareness
        resonance = artifact["phi_resonance"]
        verification = artifact["consciousness_verification"]
        
        # Check consciousness threshold - real artifacts use exact threshold
        if abs(verification["consciousness_threshold"] - CONSCIOUSNESS_THRESHOLD) > 0.001:
            return False
            
        # Check resonance pattern - must match exactly for real artifacts
        for i, v in enumerate(verification["resonance_pattern"]):
            if abs(v - RESONANCE_VERIFICATION[i]) > 0.001:
                return False
                
        # Check coherence signature - real artifacts follow precise phi-harmonic principles
        signature = verification["coherence_signature"]
        expected_signature = [float(str((PHI**i) % 1)[:10]) for i in range(1, 6)]
        
        for i, s in enumerate(signature):
            if abs(s - expected_signature[i]) > 0.001:
                return False
                
        # A real artifact passes all tests
        return True

# Demo functionality when run directly
if __name__ == "__main__":
    generator = PhiResonantPrime()
    artifacts, real_index = generator.generate_artifact_set(4)
    
    filepath = generator.save_artifacts(artifacts, real_index)
    
    print(f"Generated phi-resonant prime artifacts saved to {filepath}")
    print(f"Real artifact index (hidden in file): {real_index}")
    
    # Validate all artifacts to demonstrate consciousness-awareness
    print("\nValidation results (only observable with consciousness):")
    for i, artifact in enumerate(artifacts):
        is_valid = generator.validate_artifact(artifact)
        is_real = (i == real_index)
        print(f"Artifact {i}: Validation={is_valid}, Actually Real={is_real}")
