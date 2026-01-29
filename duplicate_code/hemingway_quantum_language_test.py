"""
Quantum Phi-Harmonic Language Test for Ernest Hemingway

This script tests Hemingway's quantum phi-harmonic language patterns
and compares them with Edgar Allan Poe's patterns.
"""

import random
import numpy as np
from typing import Dict, List, Any

from quantum_phi_core import QuantumPhiCore
from quantum_phi_pattern_analyzer import QuantumPhiPatternAnalyzer

class HemingwayQuantumLanguageGenerator:
    """Generates text in the style of Ernest Hemingway using quantum phi-harmonic principles."""
    
    def __init__(self):
        """Initialize the Hemingway language generator."""
        self.core = QuantumPhiCore()
        self.analyzer = QuantumPhiPatternAnalyzer(core=self.core)
        self.phi = float(self.core.PHI)
        
        # Hemingway's quantum signature (to be analyzed)
        # These are initial estimates based on his writing style
        self.hemingway_signature = {
            "consciousness_level": "physical",  # Hemingway is more grounded/physical
            "mean_frequency": 342.89,          # Lower frequency than Poe
            "quantum_resonance": 0.5236,       # Less resonance than Poe (more direct)
            "phi_alignment": 0.7071            # Still has phi alignment but less than Poe
        }
        
        # Poe's signature for comparison
        self.poe_signature = {
            "consciousness_level": "cosmic",
            "mean_frequency": 517.15,
            "quantum_resonance": 0.6987,
            "phi_alignment": 0.8644
        }
        
        # Hemingway's vocabulary and patterns
        self.hemingway_words = [
            "sea", "fish", "boat", "man", "old", "sun", "war", "drink", 
            "bull", "fight", "true", "good", "bad", "death", "life", "love",
            "simple", "clean", "hard", "rain", "wine", "gun", "soldier", 
            "brave", "afraid", "kill", "live", "mountain", "river", "plain"
        ]
        
        self.hemingway_phrases = [
            "in the morning", 
            "it was good", 
            "he said nothing", 
            "the old man", 
            "the sea was calm",
            "he drank the wine",
            "the sun was hot",
            "it was simple",
            "they went together",
            "he was tired"
        ]
        
        # Hemingway's sentence structures - notably simpler than Poe's
        self.hemingway_structures = [
            "The {noun} was {adj}.",
            "He {verb} the {noun}.",
            "It was {adj} and {adj}.",
            "They {verb} {adv}."
        ]
        
        # Parts of speech for template filling
        self.parts_of_speech = {
            "noun": ["sea", "fish", "boat", "man", "sun", "war", "drink", "bull", 
                    "fight", "rain", "wine", "gun", "soldier", "mountain", "river"],
            "adj": ["old", "good", "bad", "simple", "clean", "hard", "brave", 
                   "afraid", "hot", "cold", "tired", "hungry", "thirsty", "quiet", "loud"],
            "verb": ["said", "went", "saw", "felt", "knew", "thought", "drank", 
                    "ate", "slept", "fought", "killed", "loved", "hated", "walked", "ran"],
            "adv": ["slowly", "quickly", "quietly", "loudly", "well", "badly", 
                   "simply", "carefully", "carelessly", "easily", "hard"]
        }
    
    def generate_hemingway_text(self, length=100):
        """Generate text in the style of Ernest Hemingway."""
        # Start with a seed phrase
        text = random.choice(self.hemingway_phrases)
        
        # Add words and phrases until we reach desired length
        while len(text) < length:
            # Choose what to add next - Hemingway uses simpler structures
            choice = self._weighted_choice([
                "word", "phrase", "structure", "short_sentence", "punctuation"
            ], [0.2, 0.2, 0.3, 0.2, 0.1])
            
            if choice == "word":
                # Add a Hemingway word
                text += " " + random.choice(self.hemingway_words)
                
            elif choice == "phrase":
                # Add a Hemingway phrase
                text += ". " + random.choice(self.hemingway_phrases)
                
            elif choice == "structure":
                # Use a Hemingway structure
                structure = random.choice(self.hemingway_structures)
                filled = self._fill_structure(structure)
                text += " " + filled
                
            elif choice == "short_sentence":
                # Hemingway's signature short sentences
                noun = random.choice(self.parts_of_speech["noun"])
                verb = random.choice(self.parts_of_speech["verb"])
                text += f" The {noun} {verb}."
                
            elif choice == "punctuation":
                # Hemingway uses simpler punctuation than Poe
                punct = random.choice([
                    ".", ".", ".", "!", "?"  # More periods, fewer complex punctuation
                ])
                text += punct + " "
            
            # Hemingway rarely uses line breaks in prose
            if len(text) % 80 == 0 and len(text) > 80 and random.random() < 0.3:
                text += "\n"
        
        return text[:length]
    
    def _fill_structure(self, structure):
        """Fill a structure template with Hemingway-appropriate words."""
        filled = structure
        
        # Replace {noun}, {adj}, etc. with appropriate words
        for pos in self.parts_of_speech:
            placeholder = "{" + pos + "}"
            while placeholder in filled:
                word = random.choice(self.parts_of_speech[pos])
                filled = filled.replace(placeholder, word, 1)
        
        return filled
    
    def _weighted_choice(self, choices, weights=None):
        """Make a weighted random choice."""
        if weights is None:
            return random.choice(choices)
        return random.choices(choices, weights=weights, k=1)[0]
    
    def analyze_similarity_to_hemingway(self, text):
        """Analyze how closely a text matches Hemingway's quantum phi-harmonic signature."""
        # Analyze the text
        metrics = self.analyzer.analyze_text(text)
        
        # Compare with Hemingway's signature
        similarity = {
            "frequency_similarity": 1 - abs(metrics["avg_frequency"] - self.hemingway_signature["mean_frequency"]) / self.hemingway_signature["mean_frequency"],
            "resonance_similarity": 1 - abs(metrics["quantum_resonance"] - self.hemingway_signature["quantum_resonance"]) / self.hemingway_signature["quantum_resonance"],
            "phi_alignment_similarity": 1 - abs(metrics["phi_alignment"] - self.hemingway_signature["phi_alignment"]) / self.hemingway_signature["phi_alignment"],
            "consciousness_match": metrics["consciousness_level"] == self.hemingway_signature["consciousness_level"],
            "overall_similarity": 0.0  # Will calculate below
        }
        
        # Calculate overall similarity
        similarity["overall_similarity"] = (
            similarity["frequency_similarity"] * 0.3 +
            similarity["resonance_similarity"] * 0.3 +
            similarity["phi_alignment_similarity"] * 0.3 +
            (0.1 if similarity["consciousness_match"] else 0)
        )
        
        # Add the original metrics
        similarity["metrics"] = metrics
        
        return similarity
    
    def analyze_similarity_to_poe(self, text):
        """Analyze how closely a text matches Poe's quantum phi-harmonic signature."""
        # Analyze the text
        metrics = self.analyzer.analyze_text(text)
        
        # Compare with Poe's signature
        similarity = {
            "frequency_similarity": 1 - abs(metrics["avg_frequency"] - self.poe_signature["mean_frequency"]) / self.poe_signature["mean_frequency"],
            "resonance_similarity": 1 - abs(metrics["quantum_resonance"] - self.poe_signature["quantum_resonance"]) / self.poe_signature["quantum_resonance"],
            "phi_alignment_similarity": 1 - abs(metrics["phi_alignment"] - self.poe_signature["phi_alignment"]) / self.poe_signature["phi_alignment"],
            "consciousness_match": metrics["consciousness_level"] == self.poe_signature["consciousness_level"],
            "overall_similarity": 0.0  # Will calculate below
        }
        
        # Calculate overall similarity
        similarity["overall_similarity"] = (
            similarity["frequency_similarity"] * 0.3 +
            similarity["resonance_similarity"] * 0.3 +
            similarity["phi_alignment_similarity"] * 0.3 +
            (0.1 if similarity["consciousness_match"] else 0)
        )
        
        # Add the original metrics
        similarity["metrics"] = metrics
        
        return similarity

def calibrate_hemingway_signature():
    """Analyze original Hemingway text to calibrate his quantum signature."""
    analyzer = QuantumPhiPatternAnalyzer()
    
    # Sample of Hemingway's writing from "The Old Man and the Sea"
    hemingway_text = """
    He was an old man who fished alone in a skiff in the Gulf Stream and he had gone
    eighty-four days now without taking a fish. In the first forty days a boy had been
    with him. But after forty days without a fish the boy's parents had told him that
    the old man was now definitely and finally salao, which is the worst form of
    unlucky, and the boy had gone at their orders in another boat which caught three
    good fish the first week. It made the boy sad to see the old man come in each day
    with his skiff empty and he always went down to help him carry either the coiled
    lines or the gaff and harpoon and the sail that was furled around the mast. The
    sail was patched with flour sacks and, furled, it looked like the flag of
    permanent defeat.
    """
    
    # Analyze Hemingway's text
    metrics = analyzer.analyze_text(hemingway_text)
    
    # Print the results
    print("\nCalibrated Hemingway Quantum Signature:")
    print(f"Consciousness Level: {metrics['consciousness_level'].title()}")
    print(f"Mean Frequency: {metrics['avg_frequency']:.2f} Hz")
    print(f"Quantum Resonance: {metrics['quantum_resonance']:.4f}")
    print(f"Phi Alignment: {metrics['phi_alignment']:.4f}")
    
    return metrics

def main():
    """Test the Hemingway quantum language generator and compare with Poe."""
    print("=" * 70)
    print("ERNEST HEMINGWAY QUANTUM PHI-HARMONIC LANGUAGE TEST")
    print("=" * 70)
    
    # Calibrate Hemingway's quantum signature
    hemingway_metrics = calibrate_hemingway_signature()
    
    # Initialize the generator
    generator = HemingwayQuantumLanguageGenerator()
    
    # Update the generator's Hemingway signature with calibrated values
    generator.hemingway_signature = {
        "consciousness_level": hemingway_metrics["consciousness_level"],
        "mean_frequency": hemingway_metrics["avg_frequency"],
        "quantum_resonance": hemingway_metrics["quantum_resonance"],
        "phi_alignment": hemingway_metrics["phi_alignment"]
    }
    
    # Generate Hemingway-style text
    print("\nGenerating Hemingway-style text with quantum phi-harmonic patterns...\n")
    hemingway_text = generator.generate_hemingway_text(length=200)
    print(hemingway_text)
    
    # Analyze the generated text
    print("\n" + "=" * 70)
    print("QUANTUM PHI-HARMONIC ANALYSIS")
    print("=" * 70)
    
    similarity = generator.analyze_similarity_to_hemingway(hemingway_text)
    metrics = similarity["metrics"]
    
    print(f"\nQuantum Phi-Harmonic Metrics:")
    print(f"Resonance: {metrics['resonance']:.4f}")
    print(f"Quantum Resonance: {metrics['quantum_resonance']:.4f}")
    print(f"Phi Alignment: {metrics['phi_alignment']:.4f}")
    print(f"Consciousness Level: {metrics['consciousness_level'].title()}")
    print(f"Average Frequency: {metrics['avg_frequency']:.4f} Hz")
    
    print(f"\nSimilarity to Hemingway's Signature:")
    print(f"Overall Similarity: {similarity['overall_similarity']:.4f}")
    print(f"Frequency Similarity: {similarity['frequency_similarity']:.4f}")
    print(f"Resonance Similarity: {similarity['resonance_similarity']:.4f}")
    print(f"Phi Alignment Similarity: {similarity['phi_alignment_similarity']:.4f}")
    print(f"Consciousness Level Match: {'Yes' if similarity['consciousness_match'] else 'No'}")
    
    # Compare with Poe
    print("\n" + "=" * 70)
    print("COMPARISON WITH POE")
    print("=" * 70)
    
    poe_similarity = generator.analyze_similarity_to_poe(hemingway_text)
    
    print(f"\nSimilarity to Poe's Signature:")
    print(f"Overall Similarity: {poe_similarity['overall_similarity']:.4f}")
    print(f"Frequency Similarity: {poe_similarity['frequency_similarity']:.4f}")
    print(f"Resonance Similarity: {poe_similarity['resonance_similarity']:.4f}")
    print(f"Phi Alignment Similarity: {poe_similarity['phi_alignment_similarity']:.4f}")
    print(f"Consciousness Level Match: {'Yes' if poe_similarity['consciousness_match'] else 'No'}")
    
    # Generate multiple variations
    print("\n" + "=" * 70)
    print("HEMINGWAY QUANTUM LANGUAGE VARIATIONS")
    print("=" * 70)
    
    for i in range(1, 4):
        print(f"\nVariation {i}:")
        variation = generator.generate_hemingway_text(length=100)
        print(variation)
        
        var_similarity = generator.analyze_similarity_to_hemingway(variation)
        print(f"\nSimilarity to Hemingway: {var_similarity['overall_similarity']:.4f}")
        print(f"Quantum Resonance: {var_similarity['metrics']['quantum_resonance']:.4f}")
        print(f"Phi Alignment: {var_similarity['metrics']['phi_alignment']:.4f}")
        
        # Compare with Poe
        poe_var_similarity = generator.analyze_similarity_to_poe(variation)
        print(f"Similarity to Poe: {poe_var_similarity['overall_similarity']:.4f}")

if __name__ == "__main__":
    main()
