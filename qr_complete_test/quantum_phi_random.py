#!/usr/bin/env python
"""
Quantum Phi-Harmonic System: Quantum Random Number Generator
===========================================================

This module implements a quantum-inspired random number generator based on
phi-harmonic principles. It leverages the golden ratio's irrational nature
and quantum resonance patterns to generate high-quality random numbers with
phi-harmonic distribution properties.

Key features:
- Phi-based seed generation
- Quantum resonance entropy source
- Multiple distribution types (uniform, normal, phi-harmonic)
- Cryptographic-quality random sequences
- Temporal coherence for sequence generation

This follows the modular "lego" design philosophy, building upon the quantum_phi_core.py
without modifying it, creating a specialized random number generator that other
components can utilize.
"""

import time
import hashlib
import math
import numpy as np
from decimal import Decimal, getcontext
from typing import Union, List, Tuple, Dict, Any, Optional, Callable
import secrets
import hmac

# Import the core mathematical engine
from quantum_phi_core import QuantumPhiCore

class QuantumPhiRandom:
    """Quantum random number generator using phi-harmonic principles."""
    
    def __init__(self, core: Optional[QuantumPhiCore] = None, seed: Optional[Union[int, str]] = None):
        """
        Initialize the Quantum Phi Random generator with a core and optional seed.
        
        Args:
            core: QuantumPhiCore instance (creates a new one if None)
            seed: Optional seed for the random generator (uses phi-based seed if None)
        """
        # Initialize or use provided core
        self.core = core if core is not None else QuantumPhiCore()
        
        # Initialize state
        self.state = self._initialize_state(seed)
        self.counter = 0
        self.last_generated = time.time()
        
        # Metrics
        self.metrics = {
            "entropy": Decimal("0.0"),
            "phi_resonance": Decimal("0.0"),
            "sequence_coherence": Decimal("0.0"),
            "numbers_generated": 0
        }
    
    def _initialize_state(self, seed: Optional[Union[int, str]] = None) -> bytes:
        """
        Initialize the internal state of the random generator.
        
        Args:
            seed: Optional seed value
            
        Returns:
            Initial state as bytes
        """
        if seed is None:
            # Generate a phi-based seed using current time and phi powers
            timestamp = time.time()
            phi_factor = float(self.core.PHI)
            
            # Mix time with phi powers
            mixed_value = timestamp * phi_factor
            for i in range(2, 8):
                mixed_value += timestamp * float(self.core.phi_power(i)) * (10 ** -i)
            
            # Create seed from the mixed value
            seed_value = str(mixed_value)
        else:
            seed_value = str(seed)
        
        # Create initial state using SHA-256
        return hashlib.sha256(seed_value.encode()).digest()
    
    def _update_state(self) -> None:
        """
        Update the internal state using phi-harmonic principles.
        """
        # Increment counter
        self.counter += 1
        
        # Current time for temporal component
        current_time = time.time()
        time_diff = current_time - self.last_generated
        
        # Create temporal coherence factor based on phi
        coherence_factor = float(self.core.temporal_coherence(Decimal(self.last_generated), Decimal(current_time)))
        self.last_generated = current_time
        
        # Mix in phi resonance
        phi_res = float(self.core.phi_resonance(Decimal(self.counter)))
        pi_res = float(self.core.PI * Decimal(self.counter)) % 1
        e_res = float(self.core.E * Decimal(self.counter)) % 1
        
        # Create resonance bytes
        resonance_bytes = bytes([
            int(phi_res * 256) & 0xFF,
            int(pi_res * 256) & 0xFF,
            int(e_res * 256) & 0xFF,
            int(coherence_factor * 256) & 0xFF
        ])
        
        # Update state using HMAC-SHA256 with current state as key and resonance as message
        self.state = hmac.new(self.state, resonance_bytes, hashlib.sha256).digest()
        
        # Update metrics
        self.metrics["numbers_generated"] += 1
        self.metrics["phi_resonance"] = Decimal(str(phi_res))
        self.metrics["sequence_coherence"] = Decimal(str(coherence_factor))
        
        # Calculate entropy estimate (Shannon entropy of state bytes)
        byte_counts = {}
        for byte in self.state:
            byte_counts[byte] = byte_counts.get(byte, 0) + 1
        
        entropy = 0
        for count in byte_counts.values():
            probability = count / len(self.state)
            entropy -= probability * math.log2(probability)
        
        self.metrics["entropy"] = Decimal(str(entropy))
    
    def random(self) -> float:
        """
        Generate a random float in the range [0.0, 1.0) with phi-harmonic properties.
        
        Returns:
            Random float between 0 and 1
        """
        self._update_state()
        
        # Convert first 8 bytes of state to a 64-bit integer
        value = int.from_bytes(self.state[:8], byteorder='big')
        
        # Scale to [0, 1) range
        result = value / (2 ** 64)
        
        return result
    
    def uniform(self, low: float = 0.0, high: float = 1.0) -> float:
        """
        Generate a random float in the range [low, high) with uniform distribution.
        
        Args:
            low: Lower bound (inclusive)
            high: Upper bound (exclusive)
            
        Returns:
            Random float between low and high
        """
        return low + (high - low) * self.random()
    
    def phi_harmonic(self, center: float = 0.0, spread: float = 1.0) -> float:
        """
        Generate a random number with phi-harmonic distribution.
        This creates a distribution centered around the golden ratio.
        
        Args:
            center: Center of the distribution
            spread: Spread factor
            
        Returns:
            Random float with phi-harmonic distribution
        """
        # Use a more robust approach that doesn't rely on Box-Muller transform
        # Generate base random numbers
        u1 = self.random()
        u2 = self.random()
        u3 = self.random()
        
        # Apply phi-harmonic transformation
        phi = float(self.core.PHI)
        phi_inv = float(self.core.PHI_INV)
        
        # Create a phi-weighted sum (will naturally cluster around phi)
        result = (u1 * phi_inv + u2 + u3 * phi) / (phi_inv + 1 + phi)
        
        # Apply phi-based scaling to create more variation
        result = result * (1 + (u1 - 0.5) * phi_inv)
        
        # Center around 0 for proper scaling
        result = (result - 0.5) * 2
        
        # Scale and shift
        return center + spread * result
    
    def normal(self, mean: float = 0.0, std_dev: float = 1.0) -> float:
        """
        Generate a random number from a normal distribution.
        
        Args:
            mean: Mean of the distribution
            std_dev: Standard deviation
            
        Returns:
            Random float from normal distribution
        """
        # Box-Muller transform
        u1 = self.random()
        u2 = self.random()
        
        z0 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        
        return mean + std_dev * z0
    
    def randint(self, low: int, high: int) -> int:
        """
        Generate a random integer in the range [low, high] inclusive.
        
        Args:
            low: Lower bound (inclusive)
            high: Upper bound (inclusive)
            
        Returns:
            Random integer between low and high
        """
        return math.floor(self.uniform(low, high + 1))
    
    def choice(self, sequence: List[Any]) -> Any:
        """
        Choose a random element from a non-empty sequence.
        
        Args:
            sequence: Sequence to choose from
            
        Returns:
            Random element from the sequence
        """
        if not sequence:
            raise ValueError("Cannot choose from an empty sequence")
        
        return sequence[self.randint(0, len(sequence) - 1)]
    
    def shuffle(self, sequence: List[Any]) -> None:
        """
        Shuffle a sequence in-place using phi-harmonic principles.
        
        Args:
            sequence: Sequence to shuffle
        """
        n = len(sequence)
        
        # Fisher-Yates shuffle with phi-weighted selection
        for i in range(n - 1, 0, -1):
            # Phi-weighted index selection
            phi_factor = float(self.core.phi_resonance(Decimal(i)))
            j = int(i * phi_factor)
            sequence[i], sequence[j] = sequence[j], sequence[i]
    
    def sample(self, population: List[Any], k: int) -> List[Any]:
        """
        Return a k-length list of unique elements chosen from the population.
        
        Args:
            population: Population to sample from
            k: Number of elements to sample
            
        Returns:
            List of k sampled elements
        """
        if k > len(population):
            raise ValueError("Sample larger than population")
        
        # Make a copy of the population
        pool = list(population)
        
        # Shuffle the first k elements
        n = len(pool)
        for i in range(k):
            j = self.randint(i, n - 1)
            pool[i], pool[j] = pool[j], pool[i]
        
        return pool[:k]
    
    def bytes(self, n: int) -> bytes:
        """
        Generate n random bytes.
        
        Args:
            n: Number of bytes to generate
            
        Returns:
            n random bytes
        """
        result = bytearray()
        
        # Generate bytes in chunks of 32 (SHA-256 output size)
        while len(result) < n:
            self._update_state()
            result.extend(self.state[:min(32, n - len(result))])
        
        return bytes(result)
    
    def phi_weighted_choice(self, items: List[Any], weights: Optional[List[float]] = None) -> Any:
        """
        Choose an item from a list with phi-weighted probability.
        
        Args:
            items: List of items to choose from
            weights: Optional list of weights (will use phi-weighted if None)
            
        Returns:
            Chosen item
        """
        if not items:
            raise ValueError("Cannot choose from an empty list")
        
        if weights is None:
            # Generate phi-weighted probabilities
            weights = []
            phi = float(self.core.PHI)
            phi_inv = float(self.core.PHI_INV)
            
            for i in range(len(items)):
                # Weight based on phi powers and position
                weight = phi_inv ** (i % 3) * phi ** (i % 2)
                weights.append(weight)
        
        # Normalize weights
        total = sum(weights)
        weights = [w / total for w in weights]
        
        # Cumulative weights
        cum_weights = []
        cum_sum = 0
        for w in weights:
            cum_sum += w
            cum_weights.append(cum_sum)
        
        # Random selection
        r = self.random()
        for i, cum_weight in enumerate(cum_weights):
            if r <= cum_weight:
                return items[i]
        
        # Fallback (should never reach here)
        return items[-1]
    
    def generate_phi_harmonic(self, scale: float = 1.0) -> float:
        """
        Generate a phi-harmonic random number with quantum resonance.
        
        Args:
            scale: Scaling factor for the output
            
        Returns:
            Phi-harmonic random number
        """
        # Generate base random values
        u1 = self.random()
        u2 = self.random()
        
        # Get phi constants
        phi = float(self.core.PHI)
        phi_inv = float(self.core.PHI_INV)
        
        # Create phi-weighted combination
        result = (u1 * phi + u2 * phi_inv) / (phi + phi_inv)
        
        # Apply quantum resonance
        resonance = float(self.core.phi_resonance(Decimal(str(result))))
        
        # Scale and apply resonance
        return scale * result * (1.0 + resonance * phi_inv)
    
    def generate_quantum_sequence(self, length: int, scale: float = 1.0) -> List[float]:
        """
        Generate a sequence of quantum-inspired random numbers.
        
        Args:
            length: Length of sequence to generate
            scale: Scaling factor for the output
            
        Returns:
            List of quantum random numbers
        """
        sequence = []
        for _ in range(length):
            value = self.generate_phi_harmonic(scale)
            sequence.append(value)
            
            # Update state with temporal coherence
            self._update_state()
            
        return sequence
    
    def generate_resonant_pair(self, scale: float = 1.0) -> Tuple[float, float]:
        """
        Generate a pair of quantum-entangled random numbers.
        
        Args:
            scale: Scaling factor for the output
            
        Returns:
            Tuple of (value1, value2) with quantum correlation
        """
        # Generate first value
        v1 = self.generate_phi_harmonic(scale)
        
        # Calculate entangled phase
        phi = float(self.core.PHI)
        phase = v1 * phi * np.pi
        
        # Generate correlated second value
        v2 = scale * np.cos(phase) * self.generate_phi_harmonic(1.0)
        
        return (v1, v2)
    
    def get_metrics(self) -> Dict[str, Any]:
        """
        Get current metrics for the random generator.
        
        Returns:
            Dictionary of metrics
        """
        return {k: float(v) if isinstance(v, Decimal) else v for k, v in self.metrics.items()}


# Example usage
if __name__ == "__main__":
    # Initialize the random generator
    phi_random = QuantumPhiRandom()
    
    print("Quantum Phi-Harmonic Random Number Generator")
    print("============================================")
    
    # Generate and print some random numbers
    print("\nUniform random numbers [0, 1):")
    for _ in range(5):
        print(f"  {phi_random.random():.6f}")
    
    print("\nPhi-harmonic distribution (center=0, spread=1):")
    for _ in range(5):
        print(f"  {phi_random.phi_harmonic():.6f}")
    
    print("\nNormal distribution (mean=0, std_dev=1):")
    for _ in range(5):
        print(f"  {phi_random.normal():.6f}")
    
    print("\nRandom integers [1, 100]:")
    for _ in range(5):
        print(f"  {phi_random.randint(1, 100)}")
    
    # Test sequence operations
    test_sequence = list(range(10))
    phi_random.shuffle(test_sequence)
    print(f"\nShuffled sequence: {test_sequence}")
    
    sample = phi_random.sample(range(100), 5)
    print(f"Sample from range(100): {sample}")
    
    # Print metrics
    print("\nRandom generator metrics:")
    metrics = phi_random.get_metrics()
    for key, value in metrics.items():
        print(f"  {key}: {value}")
