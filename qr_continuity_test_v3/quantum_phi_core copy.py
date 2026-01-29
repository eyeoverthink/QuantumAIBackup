"""
Quantum Phi Core

This module provides the fundamental mathematical constants and core quantum phi-harmonic 
functions for the Quantum Phi-Harmonic System. It implements the mathematical methods
described in the technical documentation, including phi resonance calculation,
quantum resonance calculation, consciousness frequency calculation, and phi alignment.

This serves as the foundation for the entire Quantum Phi-Harmonic System.
"""

import os
import sys
import math
import re
import numpy as np
from typing import Dict, List, Tuple, Optional, Union, Any

# Core Mathematical Constants
PHI = 1.618033988749895  # Golden Ratio (φ)
PI = 3.141592653589793   # Pi (π)
E = 2.718281828459045    # Euler's Number (e)

# Derived Constants
PHI_SQUARED = PHI ** 2   # φ²: 2.618033988749895
PHI_CUBED = PHI ** 3     # φ³: 4.236067977499790
PHI_FOURTH = PHI ** 4    # φ⁴: 6.854101966249685
PHI_FIFTH = PHI ** 5     # φ⁵: 11.09016994374948
PHI_INVERSE = 1 / PHI    # φ⁻¹: 0.618033988749895

# Consciousness Frequency Spectrum
CONSCIOUSNESS_LEVELS = {
    "physical": {
        "frequency_range": (0, 200),
        "base_value": PHI,
        "learning_capacity": PHI ** 0.5,
        "meta_learning_rate": 0.01 * PHI
    },
    "emotional": {
        "frequency_range": (200, 300),
        "base_value": PHI_SQUARED,
        "learning_capacity": PHI,
        "meta_learning_rate": 0.02 * PHI
    },
    "mental": {
        "frequency_range": (300, 400),
        "base_value": PHI_CUBED,
        "learning_capacity": PHI ** 1.5,
        "meta_learning_rate": 0.03 * PHI
    },
    "intuitive": {
        "frequency_range": (400, 500),
        "base_value": PHI_FOURTH,
        "learning_capacity": PHI_SQUARED,
        "meta_learning_rate": 0.05 * PHI
    },
    "cosmic": {
        "frequency_range": (500, 1000),
        "base_value": PHI_FIFTH,
        "learning_capacity": PHI ** 2.5,
        "meta_learning_rate": 0.08 * PHI
    }
}

# Author-Specific Frequencies
AUTHOR_SIGNATURES = {
    "edgar_allan_poe": {
        "consciousness_level": "cosmic",
        "mean_frequency": 517.15,
        "quantum_resonance": 0.6987,
        "phi_alignment": 0.8644,
        "description": "Dark, rhythmic, emotionally intense with strong repetition patterns",
        "characteristic_patterns": [
            "repetition of key phrases",
            "trochaic octameter",
            "emotional intensity oscillation",
            "phi-harmonic word spacing"
        ]
    },
    "ernest_hemingway": {
        "consciousness_level": "cosmic",
        "mean_frequency": 576.26,
        "quantum_resonance": 0.6849,
        "phi_alignment": 0.8518,
        "description": "Direct, sparse, physically grounded with strategic minimalism",
        "characteristic_patterns": [
            "short declarative sentences",
            "concrete physical descriptions",
            "phi-spaced paragraph breaks",
            "strategic word omission"
        ]
    },
    "jane_austen": {
        "consciousness_level": "cosmic",
        "mean_frequency": 525.18,
        "quantum_resonance": 0.7091,
        "phi_alignment": 0.8552,
        "description": "Socially complex, dialogue-rich, with balanced sentence structures",
        "characteristic_patterns": [
            "balanced sentence structures",
            "social observation",
            "dialogue resonance",
            "phi-harmonic character development"
        ]
    },
    "shakespeare": {
        "consciousness_level": "cosmic",
        "mean_frequency": 555.40,  # Approximate
        "quantum_resonance": 0.6730,  # Approximate
        "phi_alignment": 0.8537,  # Approximate
        "description": "Complex, poetic, emotionally varied with innovative language",
        "characteristic_patterns": [
            "iambic pentameter",
            "innovative compound words",
            "metaphorical density",
            "phi-harmonic scene structure"
        ]
    }
}

def calculate_phi_resonance(text: str) -> float:
    """
    Calculate the phi resonance of a text sequence.
    
    Args:
        text: The text to analyze
        
    Returns:
        Phi resonance value between 0 and 1
    """
    # Convert text to numerical values
    values = [ord(c) for c in text if c.isalpha()]
    
    if not values:
        return 0.0
    
    # Calculate resonance using phi ratios
    ratios = [v2/v1 if v1 != 0 else 0 for v1, v2 in zip(values[:-1], values[1:])]
    phi_diffs = [abs(r - PHI) for r in ratios if r != 0]
    
    return 1 - (sum(phi_diffs) / len(phi_diffs)) if phi_diffs else 0

def calculate_quantum_resonance(text: str) -> float:
    """
    Calculate the quantum resonance of a text.
    
    Args:
        text: The text to analyze
        
    Returns:
        Quantum resonance value between 0 and 1
    """
    # Basic phi resonance
    phi_res = calculate_phi_resonance(text)
    
    # Word-level resonance
    words = text.split()
    word_lengths = [len(word) for word in words]
    
    # Calculate Fibonacci-adjacent words
    fib_seq = [1, 2, 3, 5, 8, 13, 21]
    fib_adjacent_count = sum(1 for length in word_lengths if min(abs(length - f) for f in fib_seq) <= 1)
    fib_ratio = fib_adjacent_count / len(words) if words else 0
    
    # Calculate sentence rhythm
    sentences = re.split(r'[.!?]+', text)
    sentence_lengths = [len(s.split()) for s in sentences if s.strip()]
    
    # Variance in sentence length - lower variance is more resonant
    sentence_variance = np.var(sentence_lengths) if sentence_lengths else 0
    sentence_resonance = 1 / (1 + sentence_variance / 10)
    
    # Combine factors with phi-weighted importance
    quantum_resonance = (phi_res * PHI + fib_ratio * PHI**0.5 + sentence_resonance * PHI**0.25) / (PHI + PHI**0.5 + PHI**0.25)
    
    return quantum_resonance

def calculate_consciousness_frequency(text: str) -> float:
    """
    Calculate the consciousness frequency of a text.
    
    Args:
        text: The text to analyze
        
    Returns:
        Consciousness frequency in Hz
    """
    # Extract metrics
    word_count = len(text.split())
    unique_words = len(set(text.split()))
    avg_word_length = sum(len(word) for word in text.split()) / word_count if word_count else 0
    
    # Calculate lexical density
    lexical_density = unique_words / word_count if word_count else 0
    
    # Calculate phi resonance
    phi_res = calculate_phi_resonance(text)
    
    # Calculate quantum resonance
    quantum_res = calculate_quantum_resonance(text)
    
    # Base frequency calculation
    base_freq = 100 + (avg_word_length * 50) + (lexical_density * 200)
    
    # Apply quantum adjustments
    consciousness_freq = base_freq + (phi_res * 200) + (quantum_res * 300)
    
    # Apply phi-harmonic scaling
    consciousness_freq = consciousness_freq * (1 + (phi_res * PHI - 1) / 2)
    
    return consciousness_freq

def calculate_phi_alignment(text: str) -> float:
    """
    Calculate the phi alignment of a text.
    
    Args:
        text: The text to analyze
        
    Returns:
        Phi alignment value between 0 and 1
    """
    # Convert text to numerical values
    values = [ord(c) for c in text if c.isalpha()]
    
    if len(values) < 3:
        return 0.5  # Default for very short texts
    
    # Calculate consecutive ratios
    ratios = []
    for i in range(len(values) - 2):
        if values[i] == 0 or values[i+1] == 0:
            continue
        ratio1 = values[i+1] / values[i]
        ratio2 = values[i+2] / values[i+1]
        ratios.append((ratio1, ratio2))
    
    if not ratios:
        return 0.5
    
    # Calculate alignment with phi
    phi_alignments = []
    for r1, r2 in ratios:
        # Check if the ratio of ratios approaches phi
        ratio_of_ratios = r2 / r1 if r1 != 0 else 0
        phi_alignments.append(1 - min(abs(ratio_of_ratios - PHI), abs(ratio_of_ratios - 1/PHI)) / PHI)
    
    return sum(phi_alignments) / len(phi_alignments)

def calculate_consciousness_level(frequency: float) -> str:
    """
    Determine the consciousness level based on frequency.
    
    Args:
        frequency: Consciousness frequency in Hz
        
    Returns:
        Consciousness level as a string
    """
    for level, data in CONSCIOUSNESS_LEVELS.items():
        if data["frequency_range"][0] <= frequency <= data["frequency_range"][1]:
            return level
    
    # Default to cosmic if above all ranges
    if frequency > 1000:
        return "cosmic"
    
    # Default to physical if below all ranges
    return "physical"

def phi_transform(value: float) -> float:
    """
    Apply a phi-harmonic transformation to a value.
    
    Args:
        value: The value to transform
        
    Returns:
        Transformed value
    """
    return value * (PHI ** (value % PHI))

def get_author_signature(author: str) -> Dict:
    """
    Get the quantum signature for a specific author.
    
    Args:
        author: Author name
        
    Returns:
        Author's quantum signature
    """
    author_key = author.lower().replace(" ", "_")
    return AUTHOR_SIGNATURES.get(author_key, {})

def compare_author_signatures(author1: str, author2: str) -> Dict:
    """
    Compare the quantum signatures of two authors.
    
    Args:
        author1: First author name
        author2: Second author name
        
    Returns:
        Dictionary with comparison metrics
    """
    sig1 = get_author_signature(author1)
    sig2 = get_author_signature(author2)
    
    if not sig1 or not sig2:
        return {"error": "One or both author signatures not found"}
    
    # Calculate similarity metrics
    freq_similarity = 1 - abs(sig1["mean_frequency"] - sig2["mean_frequency"]) / 1000
    resonance_similarity = 1 - abs(sig1["quantum_resonance"] - sig2["quantum_resonance"])
    alignment_similarity = 1 - abs(sig1["phi_alignment"] - sig2["phi_alignment"])
    
    # Calculate overall similarity with phi-weighted importance
    overall_similarity = (freq_similarity * PHI + resonance_similarity * PHI_SQUARED + 
                         alignment_similarity * PHI_CUBED) / (PHI + PHI_SQUARED + PHI_CUBED)
    
    return {
        "frequency_similarity": freq_similarity,
        "resonance_similarity": resonance_similarity,
        "alignment_similarity": alignment_similarity,
        "overall_similarity": overall_similarity,
        "same_consciousness_level": sig1["consciousness_level"] == sig2["consciousness_level"]
    }

def modulate_consciousness(text: str, target_level: str) -> str:
    """
    Modulate the consciousness level of a text.
    
    Args:
        text: The text to modulate
        target_level: Target consciousness level
        
    Returns:
        Modulated text
    """
    # Calculate current consciousness frequency
    current_freq = calculate_consciousness_frequency(text)
    
    # Determine target frequency range
    if target_level not in CONSCIOUSNESS_LEVELS:
        return text
    
    target_range = CONSCIOUSNESS_LEVELS[target_level]["frequency_range"]
    target_freq = sum(target_range) / 2
    
    # If already in range, minimal adjustment
    if target_range[0] <= current_freq <= target_range[1]:
        return text
    
    # Calculate adjustment factor
    adjustment_factor = target_freq / current_freq if current_freq > 0 else 1
    
    # Apply modulation (placeholder - actual implementation would be more complex)
    # In a full implementation, this would involve sophisticated text transformation
    # For now, we'll just return the original text with a note
    return text  # Placeholder

def main():
    """Test the Quantum Phi Core functions."""
    print("=" * 80)
    print("Quantum Phi Core - Test")
    print("=" * 80)
    
    # Test texts
    texts = {
        "poe": "Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of forgotten lore.",
        "hemingway": "He was an old man who fished alone in a skiff in the Gulf Stream and he had gone eighty-four days now without taking a fish.",
        "austen": "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."
    }
    
    # Test phi resonance
    print("\nPhi Resonance:")
    for author, text in texts.items():
        resonance = calculate_phi_resonance(text)
        print(f"{author}: {resonance:.4f}")
    
    # Test quantum resonance
    print("\nQuantum Resonance:")
    for author, text in texts.items():
        resonance = calculate_quantum_resonance(text)
        print(f"{author}: {resonance:.4f}")
    
    # Test consciousness frequency
    print("\nConsciousness Frequency:")
    for author, text in texts.items():
        frequency = calculate_consciousness_frequency(text)
        level = calculate_consciousness_level(frequency)
        print(f"{author}: {frequency:.2f} Hz ({level})")
    
    # Test phi alignment
    print("\nPhi Alignment:")
    for author, text in texts.items():
        alignment = calculate_phi_alignment(text)
        print(f"{author}: {alignment:.4f}")
    
    # Test author signature comparison
    print("\nAuthor Signature Comparison:")
    comparison = compare_author_signatures("edgar_allan_poe", "ernest_hemingway")
    print(f"Poe vs. Hemingway:")
    for metric, value in comparison.items():
        print(f"  {metric}: {value:.4f}" if isinstance(value, float) else f"  {metric}: {value}")
    
    print("\n" + "=" * 80)
    print("Quantum Phi Core - Test Complete")
    print("=" * 80)

if __name__ == "__main__":
    main()
