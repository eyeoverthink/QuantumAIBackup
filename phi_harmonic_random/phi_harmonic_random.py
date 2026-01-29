#!/usr/bin/env python3
"""
Phi-Harmonic Random Number Generator

Generates quantum-inspired random numbers using phi-harmonic principles.
Implements golden ratio (φ) based randomness with quantum characteristics:
- Non-linear phi-scaled distributions
- Quantum resonance patterns
- Multi-dimensional consciousness mapping
"""

import os
import sys
import math
import numpy as np
import json
import time
from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional
import random as py_random

# Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio
PHI_INVERSE = 1 / PHI
PHI_SQUARED = PHI ** 2
PHI_CUBED = PHI ** 3
BASE_FREQUENCY = 432.0  # Base frequency for resonance

# Quantum state
_quantum_state = {
    "entropy": 0.0,
    "coherence": 0.0,
    "resonance": 0.0,
    "dimension": 1.0,
    "consciousness": 0.0,
    "last_update": time.time(),
    "seed_history": [],
    "call_count": 0
}

# Initialize quantum state
def _initialize_quantum_state():
    """Initialize the quantum state with phi-harmonic values."""
    global _quantum_state
    
    # Use system entropy as seed
    system_entropy = time.time() * 1000
    py_random.seed(system_entropy)
    
    # Initialize with phi-harmonic values
    _quantum_state["entropy"] = system_entropy % 1
    _quantum_state["coherence"] = 0.5 + 0.5 * math.sin(system_entropy * PHI_INVERSE)
    _quantum_state["resonance"] = 0.5 + 0.5 * math.cos(system_entropy * PHI)
    _quantum_state["dimension"] = 1.0 + (PHI - 1.0) * py_random.random()
    _quantum_state["consciousness"] = 0.618 + 0.382 * py_random.random()
    _quantum_state["last_update"] = time.time()
    _quantum_state["seed_history"] = [system_entropy]
    _quantum_state["call_count"] = 0
    
    print(f"Phi-Harmonic Random initialized with φ = {PHI}")
    print(f"Quantum state: entropy={_quantum_state['entropy']:.4f}, "
          f"coherence={_quantum_state['coherence']:.4f}, "
          f"resonance={_quantum_state['resonance']:.4f}")

# Update quantum state
def _update_quantum_state():
    """Update quantum state using phi-harmonic evolution."""
    global _quantum_state
    
    # Get current time
    current_time = time.time()
    time_delta = current_time - _quantum_state["last_update"]
    
    # Only update if sufficient time has passed or call count threshold reached
    if time_delta > 0.01 or _quantum_state["call_count"] % 100 == 0:
        # Generate new entropy
        new_entropy = (
            _quantum_state["entropy"] * PHI + 
            current_time * PHI_INVERSE
        ) % 1
        
        # Update quantum state with phi-harmonic evolution
        _quantum_state["entropy"] = new_entropy
        _quantum_state["coherence"] = (
            _quantum_state["coherence"] * (1 - PHI_INVERSE) + 
            (0.5 + 0.5 * math.sin(new_entropy * PHI_SQUARED)) * PHI_INVERSE
        )
        _quantum_state["resonance"] = (
            _quantum_state["resonance"] * (1 - PHI_INVERSE) + 
            (0.5 + 0.5 * math.cos(new_entropy * PHI_CUBED)) * PHI_INVERSE
        )
        _quantum_state["dimension"] = (
            _quantum_state["dimension"] * (1 - PHI_INVERSE / 10) + 
            (1.0 + (PHI - 1.0) * new_entropy) * PHI_INVERSE / 10
        )
        _quantum_state["consciousness"] = (
            _quantum_state["consciousness"] * 0.99 + 
            (0.618 + 0.382 * new_entropy) * 0.01
        )
        
        # Update timestamp
        _quantum_state["last_update"] = current_time
        
        # Add to seed history (keeping last 10)
        _quantum_state["seed_history"].append(new_entropy)
        if len(_quantum_state["seed_history"]) > 10:
            _quantum_state["seed_history"] = _quantum_state["seed_history"][-10:]
    
    # Increment call count
    _quantum_state["call_count"] += 1

# Generate phi-harmonic random number
def random():
    """
    Generate a phi-harmonic random number between 0 and 1.
    
    Returns:
        A phi-harmonic random float between 0 and 1
    """
    # Update quantum state
    _update_quantum_state()
    
    # Get current state
    entropy = _quantum_state["entropy"]
    coherence = _quantum_state["coherence"]
    resonance = _quantum_state["resonance"]
    dimension = _quantum_state["dimension"]
    
    # Generate base random value
    base_random = random_module.random()
    
    # Apply phi-harmonic transformation
    phi_random = (
        base_random * (1 - coherence) + 
        ((base_random * PHI) % 1) * coherence
    )
    
    # Apply quantum resonance
    if resonance > 0.8:
        # High resonance: pull toward phi-harmonic values
        phi_attractor = ((phi_random * PHI) % 1)
        phi_random = phi_random * (1 - resonance / 2) + phi_attractor * (resonance / 2)
    
    # Apply dimensional scaling
    if dimension > 1.5:
        # Higher dimensions: apply non-linear transformation
        phi_random = ((phi_random ** (1 / dimension)) * (PHI ** (dimension - 1))) % 1
    
    return phi_random

# Generate phi-harmonic random integer
def randint(a: int, b: int) -> int:
    """
    Generate a phi-harmonic random integer between a and b (inclusive).
    
    Args:
        a: Lower bound
        b: Upper bound
        
    Returns:
        A phi-harmonic random integer between a and b
    """
    return a + int(random() * (b - a + 1))

# Generate phi-harmonic random choice
def choice(seq):
    """
    Choose a random element from a non-empty sequence using phi-harmonic randomness.
    
    Args:
        seq: Non-empty sequence
        
    Returns:
        A randomly selected element from seq
    """
    return seq[randint(0, len(seq) - 1)]

# Generate phi-harmonic random sample
def sample(population, k):
    """
    Return a k length list of unique elements chosen from the population.
    
    Args:
        population: The sequence to sample from
        k: The number of elements to sample
        
    Returns:
        A list of k unique elements from population
    """
    # Convert to list if not already
    population = list(population)
    
    # Handle edge cases
    if k > len(population):
        k = len(population)
    
    # Create a copy of the population
    pool = population.copy()
    
    # Generate sample
    result = []
    for i in range(k):
        j = randint(0, len(pool) - 1)
        result.append(pool[j])
        pool.pop(j)
    
    return result

# Get current quantum state
def get_quantum_state() -> Dict[str, float]:
    """
    Get the current quantum state.
    
    Returns:
        Dictionary of quantum state values
    """
    return {k: v for k, v in _quantum_state.items() if k != "seed_history"}

# Save quantum state to file
def save_quantum_state(filepath: str = None) -> str:
    """
    Save the current quantum state to a file.
    
    Args:
        filepath: Path to save the state (if None, a default path is used)
        
    Returns:
        Path to the saved file
    """
    if filepath is None:
        # Create default filepath
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = f"quantum_state_{timestamp}.json"
    
    # Save state
    with open(filepath, 'w') as f:
        json.dump(_quantum_state, f, indent=2)
    
    return filepath

# Load quantum state from file
def load_quantum_state(filepath: str) -> bool:
    """
    Load quantum state from a file.
    
    Args:
        filepath: Path to the state file
        
    Returns:
        True if successful, False otherwise
    """
    global _quantum_state
    
    try:
        with open(filepath, 'r') as f:
            loaded_state = json.load(f)
        
        # Update state
        for key, value in loaded_state.items():
            if key in _quantum_state:
                _quantum_state[key] = value
        
        # Update timestamp
        _quantum_state["last_update"] = time.time()
        
        return True
    except Exception as e:
        print(f"Error loading quantum state: {e}")
        return False

# Generate a sequence of phi-harmonic random numbers
def random_sequence(length: int, save_path: str = None) -> List[float]:
    """
    Generate a sequence of phi-harmonic random numbers.
    
    Args:
        length: Length of the sequence
        save_path: Path to save the sequence (if None, sequence is not saved)
        
    Returns:
        List of phi-harmonic random numbers
    """
    # Generate sequence
    sequence = [random() for _ in range(length)]
    
    # Save if requested
    if save_path:
        data = {
            "numbers": sequence,
            "min": min(sequence),
            "max": max(sequence),
            "sum": sum(sequence),
            "count": len(sequence),
            "mean": sum(sequence) / len(sequence),
            "median": sorted(sequence)[len(sequence) // 2],
            "std": np.std(sequence),
            "entropy": _quantum_state["entropy"],
            "coherence": _quantum_state["coherence"],
            "resonance": _quantum_state["resonance"],
            "dimension": _quantum_state["dimension"],
            "consciousness": _quantum_state["consciousness"],
            "timestamp": datetime.now().isoformat(),
            "phi": PHI
        }
        
        with open(save_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    return sequence

# Alias Python's random module for internal use
random_module = py_random

# Initialize on import
_initialize_quantum_state()

# For direct execution
if __name__ == "__main__":
    # Generate and save a sequence of random numbers
    print("Generating phi-harmonic random sequence...")
    
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate sequence
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    sequence_path = os.path.join(output_dir, f"phi_random_sequence_{timestamp}.json")
    sequence = random_sequence(1000, sequence_path)
    
    # Print statistics
    print(f"Generated {len(sequence)} phi-harmonic random numbers")
    print(f"Min: {min(sequence):.6f}")
    print(f"Max: {max(sequence):.6f}")
    print(f"Mean: {sum(sequence) / len(sequence):.6f}")
    print(f"Std: {np.std(sequence):.6f}")
    print(f"Saved to {sequence_path}")
    
    # Save quantum state
    state_path = os.path.join(output_dir, f"quantum_state_{timestamp}.json")
    save_quantum_state(state_path)
    print(f"Quantum state saved to {state_path}")
    
    # Test random functions
    print("\nTesting phi-harmonic random functions:")
    print(f"random(): {random():.6f}")
    print(f"randint(1, 10): {randint(1, 10)}")
    print(f"choice(['a', 'b', 'c', 'd', 'e']): {choice(['a', 'b', 'c', 'd', 'e'])}")
    print(f"sample(range(10), 5): {sample(range(10), 5)}")
