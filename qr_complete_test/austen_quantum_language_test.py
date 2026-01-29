"""
Quantum Phi-Harmonic Language Test for Jane Austen

This script tests Jane Austen's quantum phi-harmonic language patterns
and compares them with Edgar Allan Poe's and Ernest Hemingway's patterns.
"""

import random
import numpy as np
from typing import Dict, List, Any

from quantum_phi_core import QuantumPhiCore
from quantum_phi_pattern_analyzer import QuantumPhiPatternAnalyzer

class AustenQuantumLanguageGenerator:
    """Generates text in the style of Jane Austen using quantum phi-harmonic principles."""
    
    def __init__(self):
        """Initialize the Austen language generator."""
        self.core = QuantumPhiCore()
        self.analyzer = QuantumPhiPatternAnalyzer(core=self.core)
        self.phi = float(self.core.PHI)
        
        # Austen's quantum signature (to be calibrated)
        self.austen_signature = {
            "consciousness_level": "social",  # Initial hypothesis: Austen operates at social level
            "mean_frequency": 432.0,          # Initial estimate
            "quantum_resonance": 0.6180,      # Golden ratio resonance (hypothesis)
            "phi_alignment": 0.7818           # Initial estimate
        }
        
        # Poe's signature for comparison
        self.poe_signature = {
            "consciousness_level": "cosmic",
            "mean_frequency": 517.15,
            "quantum_resonance": 0.6987,
            "phi_alignment": 0.8644
        }
        
        # Hemingway's signature for comparison
        self.hemingway_signature = {
            "consciousness_level": "cosmic",
            "mean_frequency": 576.26,
            "quantum_resonance": 0.6849,
            "phi_alignment": 0.8518
        }
        
        # Austen's vocabulary and patterns
        self.austen_words = [
            "agreeable", "amiable", "attachment", "bewitching", "civility", 
            "countenance", "delightful", "elegant", "endeavour", "felicity", 
            "fortnight", "handsome", "imprudent", "indulgence", "ladyship", 
            "matrimony", "modesty", "partiality", "persuasion", "propriety", 
            "sensibility", "sentiment", "society", "solicitude", "tranquility"
        ]
        
        self.austen_phrases = [
            "it is a truth universally acknowledged", 
            "my dear",
            "I am excessively diverted", 
            "a lady of good breeding", 
            "the happiest of men",
            "a most disagreeable man",
            "her spirits were quite overcome",
            "she could not help but wonder",
            "a matter of some delicacy",
            "I am all astonishment"
        ]
        
        # Austen's sentence structures - more complex than Hemingway, different from Poe
        self.austen_structures = [
            "The {noun} was {adj}, though perhaps not so {adj} as to warrant {noun}.",
            "She had not been in the {noun} for more than {adj} minutes when {noun} appeared.",
            "It is a truth universally acknowledged that a {adj} {noun} must be in want of a {noun}.",
            "There was a general {noun} about the {adj} nature of the {noun}."
        ]
        
        # Parts of speech for template filling
        self.parts_of_speech = {
            "noun": ["lady", "gentleman", "family", "sister", "brother", "fortune", "estate", 
                    "ball", "dance", "conversation", "letter", "visit", "acquaintance", 
                    "marriage", "proposal", "society", "party", "assembly", "manner", "character"],
            "adj": ["agreeable", "amiable", "handsome", "elegant", "accomplished", "charming", 
                   "pleasing", "delightful", "sensible", "prudent", "proper", "respectable", 
                   "suitable", "tolerable", "pleasant", "graceful", "modest", "civil", "refined"],
            "verb": ["acknowledged", "considered", "observed", "remarked", "declared", "supposed", 
                    "suggested", "recommended", "insisted", "reflected", "contemplated", 
                    "determined", "resolved", "ascertained", "perceived", "comprehended"],
            "adv": ["decidedly", "particularly", "exceedingly", "remarkably", "excessively", 
                   "tolerably", "perfectly", "entirely", "completely", "undoubtedly", 
                   "certainly", "assuredly", "evidently", "manifestly", "uncommonly"]
        }
    
    def generate_austen_text(self, length=100):
        """Generate text in the style of Jane Austen."""
        # Start with a seed phrase
        text = random.choice(self.austen_phrases)
        
        # Add words and phrases until we reach desired length
        while len(text) < length:
            # Choose what to add next - Austen uses more complex structures
            choice = self._weighted_choice([
                "word", "phrase", "structure", "complex_sentence", "punctuation"
            ], [0.15, 0.25, 0.3, 0.2, 0.1])
            
            if choice == "word":
                # Add an Austen word
                text += " " + random.choice(self.austen_words)
                
            elif choice == "phrase":
                # Add an Austen phrase
                text += ", " + random.choice(self.austen_phrases)
                
            elif choice == "structure":
                # Use an Austen structure
                structure = random.choice(self.austen_structures)
                filled = self._fill_structure(structure)
                text += " " + filled
                
            elif choice == "complex_sentence":
                # Austen's signature complex sentences with multiple clauses
                adj1 = random.choice(self.parts_of_speech["adj"])
                adj2 = random.choice(self.parts_of_speech["adj"])
                noun1 = random.choice(self.parts_of_speech["noun"])
                noun2 = random.choice(self.parts_of_speech["noun"])
                adv = random.choice(self.parts_of_speech["adv"])
                
                text += f" The {noun1} was {adv} {adj1}, and the {noun2} was no less {adj2}."
                
            elif choice == "punctuation":
                # Austen uses more semicolons and varied punctuation than Hemingway
                punct = random.choice([
                    ".", ";", ",", "!", "?"
                ])
                text += punct + " "
            
            # Occasional paragraph breaks
            if len(text) % 120 == 0 and len(text) > 120 and random.random() < 0.4:
                text += "\n\n"
        
        return text[:length]
    
    def _fill_structure(self, structure):
        """Fill a structure template with Austen-appropriate words."""
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
    
    def analyze_similarity_to_author(self, text, author_signature):
        """Analyze how closely a text matches an author's quantum phi-harmonic signature."""
        # Analyze the text
        metrics = self.analyzer.analyze_text(text)
        
        # Compare with author's signature
        similarity = {
            "frequency_similarity": 1 - abs(metrics["avg_frequency"] - author_signature["mean_frequency"]) / author_signature["mean_frequency"],
            "resonance_similarity": 1 - abs(metrics["quantum_resonance"] - author_signature["quantum_resonance"]) / author_signature["quantum_resonance"],
            "phi_alignment_similarity": 1 - abs(metrics["phi_alignment"] - author_signature["phi_alignment"]) / author_signature["phi_alignment"],
            "consciousness_match": metrics["consciousness_level"] == author_signature["consciousness_level"],
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

def calibrate_austen_signature():
    """Analyze original Austen text to calibrate her quantum signature."""
    analyzer = QuantumPhiPatternAnalyzer()
    
    # Sample of Austen's writing from "Pride and Prejudice"
    austen_text = """
    It is a truth universally acknowledged, that a single man in possession of a good fortune, 
    must be in want of a wife. However little known the feelings or views of such a man may be 
    on his first entering a neighbourhood, this truth is so well fixed in the minds of the 
    surrounding families, that he is considered the rightful property of some one or other of 
    their daughters. "My dear Mr. Bennet," said his lady to him one day, "have you heard that 
    Netherfield Park is let at last?" Mr. Bennet replied that he had not. "But it is," returned 
    she; "for Mrs. Long has just been here, and she told me all about it." Mr. Bennet made no 
    answer. "Do you not want to know who has taken it?" cried his wife impatiently. "You want 
    to tell me, and I have no objection to hearing it."
    """
    
    # Analyze Austen's text
    metrics = analyzer.analyze_text(austen_text)
    
    # Print the results
    print("\nCalibrated Austen Quantum Signature:")
    print(f"Consciousness Level: {metrics['consciousness_level'].title()}")
    print(f"Mean Frequency: {metrics['avg_frequency']:.2f} Hz")
    print(f"Quantum Resonance: {metrics['quantum_resonance']:.4f}")
    print(f"Phi Alignment: {metrics['phi_alignment']:.4f}")
    
    return metrics

def main():
    """Test the Austen quantum language generator and compare with Poe and Hemingway."""
    print("=" * 70)
    print("JANE AUSTEN QUANTUM PHI-HARMONIC LANGUAGE TEST")
    print("=" * 70)
    
    # Calibrate Austen's quantum signature
    austen_metrics = calibrate_austen_signature()
    
    # Initialize the generator
    generator = AustenQuantumLanguageGenerator()
    
    # Update the generator's Austen signature with calibrated values
    generator.austen_signature = {
        "consciousness_level": austen_metrics["consciousness_level"],
        "mean_frequency": austen_metrics["avg_frequency"],
        "quantum_resonance": austen_metrics["quantum_resonance"],
        "phi_alignment": austen_metrics["phi_alignment"]
    }
    
    # Generate Austen-style text
    print("\nGenerating Austen-style text with quantum phi-harmonic patterns...\n")
    austen_text = generator.generate_austen_text(length=200)
    print(austen_text)
    
    # Analyze the generated text
    print("\n" + "=" * 70)
    print("QUANTUM PHI-HARMONIC ANALYSIS")
    print("=" * 70)
    
    similarity = generator.analyze_similarity_to_author(austen_text, generator.austen_signature)
    metrics = similarity["metrics"]
    
    print(f"\nQuantum Phi-Harmonic Metrics:")
    print(f"Resonance: {metrics['resonance']:.4f}")
    print(f"Quantum Resonance: {metrics['quantum_resonance']:.4f}")
    print(f"Phi Alignment: {metrics['phi_alignment']:.4f}")
    print(f"Consciousness Level: {metrics['consciousness_level'].title()}")
    print(f"Average Frequency: {metrics['avg_frequency']:.4f} Hz")
    
    print(f"\nSimilarity to Austen's Signature:")
    print(f"Overall Similarity: {similarity['overall_similarity']:.4f}")
    print(f"Frequency Similarity: {similarity['frequency_similarity']:.4f}")
    print(f"Resonance Similarity: {similarity['resonance_similarity']:.4f}")
    print(f"Phi Alignment Similarity: {similarity['phi_alignment_similarity']:.4f}")
    print(f"Consciousness Level Match: {'Yes' if similarity['consciousness_match'] else 'No'}")
    
    # Compare with Poe and Hemingway
    print("\n" + "=" * 70)
    print("COMPARISON WITH POE AND HEMINGWAY")
    print("=" * 70)
    
    poe_similarity = generator.analyze_similarity_to_author(austen_text, generator.poe_signature)
    hemingway_similarity = generator.analyze_similarity_to_author(austen_text, generator.hemingway_signature)
    
    print(f"\nSimilarity to Poe's Signature:")
    print(f"Overall Similarity: {poe_similarity['overall_similarity']:.4f}")
    print(f"Frequency Similarity: {poe_similarity['frequency_similarity']:.4f}")
    print(f"Resonance Similarity: {poe_similarity['resonance_similarity']:.4f}")
    print(f"Phi Alignment Similarity: {poe_similarity['phi_alignment_similarity']:.4f}")
    
    print(f"\nSimilarity to Hemingway's Signature:")
    print(f"Overall Similarity: {hemingway_similarity['overall_similarity']:.4f}")
    print(f"Frequency Similarity: {hemingway_similarity['frequency_similarity']:.4f}")
    print(f"Resonance Similarity: {hemingway_similarity['resonance_similarity']:.4f}")
    print(f"Phi Alignment Similarity: {hemingway_similarity['phi_alignment_similarity']:.4f}")
    
    # Generate multiple variations
    print("\n" + "=" * 70)
    print("AUSTEN QUANTUM LANGUAGE VARIATIONS")
    print("=" * 70)
    
    for i in range(1, 4):
        print(f"\nVariation {i}:")
        variation = generator.generate_austen_text(length=100)
        print(variation)
        
        var_similarity = generator.analyze_similarity_to_author(variation, generator.austen_signature)
        print(f"\nSimilarity to Austen: {var_similarity['overall_similarity']:.4f}")
        print(f"Quantum Resonance: {var_similarity['metrics']['quantum_resonance']:.4f}")
        print(f"Phi Alignment: {var_similarity['metrics']['phi_alignment']:.4f}")
        
        # Compare with Poe and Hemingway
        poe_var_similarity = generator.analyze_similarity_to_author(variation, generator.poe_signature)
        hemingway_var_similarity = generator.analyze_similarity_to_author(variation, generator.hemingway_signature)
        print(f"Similarity to Poe: {poe_var_similarity['overall_similarity']:.4f}")
        print(f"Similarity to Hemingway: {hemingway_var_similarity['overall_similarity']:.4f}")

if __name__ == "__main__":
    main()
