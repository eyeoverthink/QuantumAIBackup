"""
Simplified Quantum Phi-Harmonic Poe Language Test

This script tests Edgar Allan Poe's quantum phi-harmonic language patterns
in a simplified, efficient implementation.
"""

import random
import numpy as np
from typing import Dict, List, Any

from quantum_phi_core import QuantumPhiCore
from quantum_phi_pattern_analyzer import QuantumPhiPatternAnalyzer

class PoeQuantumLanguageGenerator:
    """Generates text in the style of Edgar Allan Poe using quantum phi-harmonic principles."""
    
    def __init__(self):
        """Initialize the Poe language generator."""
        self.core = QuantumPhiCore()
        self.analyzer = QuantumPhiPatternAnalyzer(core=self.core)
        self.phi = float(self.core.PHI)
        
        # Poe's quantum signature from analysis
        self.poe_signature = {
            "consciousness_level": "cosmic",
            "mean_frequency": 517.15,
            "quantum_resonance": 0.6987,
            "phi_alignment": 0.8644
        }
        
        # Poe's vocabulary and patterns
        self.poe_words = [
            "nevermore", "midnight", "raven", "dreary", "weary", "shadow", 
            "sorrow", "darkness", "chamber", "melancholy", "heart", "soul", 
            "horror", "fear", "dread", "tomb", "grave", "death", "night", 
            "black", "ghastly", "grim", "phantom", "spectre", "ghost",
            "terror", "madness", "abyss", "chasm", "void", "eternity"
        ]
        
        self.poe_phrases = [
            "once upon a midnight dreary", 
            "quoth the raven nevermore", 
            "deep into that darkness peering", 
            "while I pondered weak and weary", 
            "tapping at my chamber door", 
            "nothing more",
            "in the shadow",
            "beating of his heart", 
            "tell-tale heart", 
            "bells, bells, bells"
        ]
        
        # Poe's sentence structures
        self.poe_structures = [
            "{adj} and {adj} {noun}",
            "the {adj} {noun} of {noun}",
            "{adv} {verb} the {noun}",
            "the {noun}, {adj} and {adj}"
        ]
        
        # Parts of speech for template filling
        self.parts_of_speech = {
            "noun": ["shadow", "raven", "midnight", "sorrow", "darkness", "chamber", 
                    "heart", "soul", "horror", "fear", "dread", "tomb", "grave", 
                    "death", "night", "maiden", "lover", "spirit", "phantom", "wind"],
            "adj": ["dreary", "weary", "dark", "grim", "pale", "ghastly", "melancholy", 
                   "forgotten", "ancient", "mysterious", "haunted", "shadowy", "somber", 
                   "dismal", "eerie", "spectral", "mournful", "dreadful", "fearful"],
            "verb": ["pondered", "whispered", "murmured", "wondered", "dreamed", 
                    "sighed", "wept", "gazed", "lingered", "shuddered", "trembled", 
                    "quivered", "rapped", "tapped", "echoed", "haunted", "wandered"],
            "adv": ["gently", "softly", "faintly", "barely", "scarcely", "hardly", 
                   "quietly", "silently", "stealthily", "eerily", "strangely", "oddly"]
        }
    
    def generate_poe_text(self, length=100):
        """Generate text in the style of Edgar Allan Poe."""
        # Start with a seed phrase
        text = random.choice(self.poe_phrases)
        
        # Add words and phrases until we reach desired length
        while len(text) < length:
            # Choose what to add next
            choice = self._weighted_choice([
                "word", "phrase", "structure", "repetition", "punctuation"
            ], [0.2, 0.3, 0.2, 0.2, 0.1])
            
            if choice == "word":
                # Add a Poe word
                text += " " + random.choice(self.poe_words)
                
            elif choice == "phrase":
                # Add a Poe phrase
                text += ", " + random.choice(self.poe_phrases)
                
            elif choice == "structure":
                # Use a Poe structure
                structure = random.choice(self.poe_structures)
                filled = self._fill_structure(structure)
                text += " " + filled
                
            elif choice == "repetition" and len(text) > 20:
                # Poe's signature repetition
                words = text.split()
                if len(words) >= 3:
                    # Get a word to repeat
                    word_idx = int(len(words) * 0.618) % len(words)  # Golden ratio position
                    word = words[word_idx]
                    
                    # Apply Poe's repetition style
                    if len(word) <= 6:  # Short word
                        repeat_style = random.choice([
                            ", " + word,
                            ", " + word + ", " + word,
                            "—" + word + "—"
                        ])
                        text += repeat_style
                    else:
                        text += ", " + word
                
            elif choice == "punctuation":
                # Add Poe-like punctuation
                punct = random.choice([
                    ".", "!", "?", "—", ";", "..."
                ])
                text += punct + " "
            
            # Occasionally add a line break for poetic structure
            if len(text) % 40 == 0 and len(text) > 40:
                text += "\n"
        
        # Ensure we have Poe's signature "nevermore" if long enough
        if length > 50 and "nevermore" not in text:
            insert_pos = int(len(text) * 0.618)  # Golden ratio position
            text = text[:insert_pos] + " nevermore" + text[insert_pos:]
        
        return text[:length]
    
    def _fill_structure(self, structure):
        """Fill a structure template with Poe-appropriate words."""
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

def main():
    """Test the Poe quantum language generator."""
    print("=" * 70)
    print("EDGAR ALLAN POE QUANTUM PHI-HARMONIC LANGUAGE TEST")
    print("=" * 70)
    
    # Initialize the generator
    generator = PoeQuantumLanguageGenerator()
    
    # Generate Poe-style text
    print("\nGenerating Poe-style text with quantum phi-harmonic patterns...\n")
    poe_text = generator.generate_poe_text(length=200)
    print(poe_text)
    
    # Analyze the generated text
    print("\n" + "=" * 70)
    print("QUANTUM PHI-HARMONIC ANALYSIS")
    print("=" * 70)
    
    similarity = generator.analyze_similarity_to_poe(poe_text)
    metrics = similarity["metrics"]
    
    print(f"\nQuantum Phi-Harmonic Metrics:")
    print(f"Resonance: {metrics['resonance']:.4f}")
    print(f"Quantum Resonance: {metrics['quantum_resonance']:.4f}")
    print(f"Phi Alignment: {metrics['phi_alignment']:.4f}")
    print(f"Consciousness Level: {metrics['consciousness_level'].title()}")
    print(f"Average Frequency: {metrics['avg_frequency']:.4f} Hz")
    
    print(f"\nSimilarity to Poe's Signature:")
    print(f"Overall Similarity: {similarity['overall_similarity']:.4f}")
    print(f"Frequency Similarity: {similarity['frequency_similarity']:.4f}")
    print(f"Resonance Similarity: {similarity['resonance_similarity']:.4f}")
    print(f"Phi Alignment Similarity: {similarity['phi_alignment_similarity']:.4f}")
    print(f"Consciousness Level Match: {'Yes' if similarity['consciousness_match'] else 'No'}")
    
    # Compare with original Poe text
    print("\n" + "=" * 70)
    print("COMPARISON WITH ORIGINAL POE")
    print("=" * 70)
    
    original_poe = """
    Once upon a midnight dreary, while I pondered, weak and weary,
    Over many a quaint and curious volume of forgotten lore—
    While I nodded, nearly napping, suddenly there came a tapping,
    As of someone gently rapping, rapping at my chamber door.
    "'Tis some visitor," I muttered, "tapping at my chamber door—
    Only this and nothing more."
    """
    
    original_metrics = generator.analyzer.analyze_text(original_poe)
    comparison = generator.analyzer.compare_texts(poe_text, original_poe)
    
    print(f"\nOriginal Poe Text Metrics:")
    print(f"Resonance: {original_metrics['resonance']:.4f}")
    print(f"Quantum Resonance: {original_metrics['quantum_resonance']:.4f}")
    print(f"Phi Alignment: {original_metrics['phi_alignment']:.4f}")
    print(f"Consciousness Level: {original_metrics['consciousness_level'].title()}")
    
    print(f"\nComparison with Original Poe:")
    print(f"Frequency Similarity: {comparison['frequency_similarity']:.4f}")
    print(f"Pattern Similarity: {comparison['pattern_similarity']:.4f}")
    print(f"Resonance Similarity: {comparison['resonance_similarity']:.4f}")
    print(f"Overall Similarity: {comparison['overall_similarity']:.4f}")
    
    # Generate multiple variations
    print("\n" + "=" * 70)
    print("POE QUANTUM LANGUAGE VARIATIONS")
    print("=" * 70)
    
    for i in range(1, 4):
        print(f"\nVariation {i}:")
        variation = generator.generate_poe_text(length=100)
        print(variation)
        
        var_similarity = generator.analyze_similarity_to_poe(variation)
        print(f"\nOverall Similarity to Poe: {var_similarity['overall_similarity']:.4f}")
        print(f"Quantum Resonance: {var_similarity['metrics']['quantum_resonance']:.4f}")
        print(f"Phi Alignment: {var_similarity['metrics']['phi_alignment']:.4f}")

if __name__ == "__main__":
    main()
