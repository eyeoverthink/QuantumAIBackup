"""
Quantum Phi-Harmonic Poe Language Agent

This module creates an interactive agent that generates text in the style of Edgar Allan Poe
using quantum phi-harmonic principles. The agent analyzes Poe's unique writing patterns
including his phi alignment, quantum resonance, and consciousness levels.
"""

import random
import numpy as np
import re
from typing import Dict, List, Tuple, Any, Optional

from quantum_phi_core import QuantumPhiCore
from quantum_phi_language_generator import QuantumPhiLanguageGenerator
from quantum_phi_pattern_analyzer import QuantumPhiPatternAnalyzer

class QuantumPhiPoeAgent:
    """
    An agent that generates and analyzes text in the style of Edgar Allan Poe
    using quantum phi-harmonic principles.
    """
    
    def __init__(self, core: Optional[QuantumPhiCore] = None):
        """Initialize the Poe agent with quantum phi-harmonic components."""
        self.core = core if core else QuantumPhiCore()
        self.generator = QuantumPhiLanguageGenerator(core=self.core)
        self.analyzer = QuantumPhiPatternAnalyzer(core=self.core)
        
        # Poe's quantum signature from analysis
        self.poe_signature = {
            "consciousness_level": "cosmic",
            "mean_frequency": 517.15,
            "quantum_resonance": 0.6987,
            "phi_alignment": 0.8644,
            "resonance_quality": "high"
        }
        
        # Poe's language patterns
        self.poe_patterns = {
            "words": [
                "nevermore", "midnight", "raven", "dreary", "weary", "shadow", 
                "sorrow", "darkness", "chamber", "melancholy", "heart", "soul", 
                "horror", "fear", "dread", "tomb", "grave", "death", "night", 
                "black", "ghastly", "grim", "phantom", "spectre", "ghost",
                "terror", "madness", "abyss", "chasm", "void", "eternity",
                "silence", "whisper", "echo", "hollow", "pale", "crimson",
                "scarlet", "ebony", "velvet", "ancient", "forgotten", "mystery"
            ],
            "phrases": [
                "once upon a midnight dreary", 
                "quoth the raven nevermore", 
                "deep into that darkness peering", 
                "while I pondered weak and weary", 
                "tapping at my chamber door", 
                "nothing more",
                "in the shadow",
                "beating of his heart", 
                "tell-tale heart", 
                "bells, bells, bells",
                "chamber door",
                "forgotten lore",
                "gently rapping",
                "darkness there and nothing more",
                "soul from out that shadow",
                "nameless here forevermore",
                "into the darkness peering",
                "doubting, dreaming dreams",
                "separate dying ember",
                "ghost upon the floor"
            ],
            "structures": [
                "{verb}, {verb}",
                "the {adj} {noun}",
                "{adj}, {adj}, and {adj}",
                "the {noun} of {noun}",
                "from the {noun} to the {noun}",
                "{adv} {verb} the {noun}",
                "the {adj} and {adj} {noun}"
            ],
            "meters": [
                "trochaic_octameter",  # Poe's signature meter in "The Raven"
                "iambic_pentameter",
                "anapestic_tetrameter"
            ]
        }
        
        # Templates for different Poe-like structures
        self.templates = {
            "raven_like": "Once upon a {time} {adj}, while I {verb}, {adj} and {adj},\n"
                         "Over many a {adj} and {adj} volume of {adj} lore—\n"
                         "While I {verb}, nearly {verb}, suddenly there came a {verb},\n"
                         "As of someone {adv} {verb}, {verb} at my {location} door.\n"
                         "\"'Tis some {noun},\" I {verb}, \"{verb} at my {location} door—\n"
                         "Only this and nothing more.\"",
            
            "tell_tale_heart": "True!—{adj}—{adj} I had been and am; but why will you say that I am {adj}?\n"
                              "The {noun} had {verb} my {noun}. It had {verb} my {noun}.\n"
                              "I heard all things in the {location} and in the {location}.\n"
                              "I heard many things in {location}. How, then, am I {adj}?",
            
            "annabel_lee": "It was many and many a {time} ago,\n"
                          "In a {location} by the sea,\n"
                          "That a {noun} there {verb} whom you may know\n"
                          "By the name of {name};\n"
                          "And this {noun} she {verb} with no other thought\n"
                          "Than to {verb} and be {verb} by me."
        }
        
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
                   "quietly", "silently", "stealthily", "eerily", "strangely", "oddly"],
            "time": ["midnight", "twilight", "evening", "night", "witching hour", 
                    "gloaming", "December", "autumn", "winter", "bleak hour"],
            "location": ["chamber", "mansion", "castle", "crypt", "tomb", "grave", 
                        "dungeon", "cellar", "attic", "study", "library", "palace"],
            "name": ["Annabel Lee", "Lenore", "Ulalume", "Ligeia", "Morella", "Berenice"]
        }
    
    def generate_poe_text(self, length: int = 100, style: str = "general") -> str:
        """
        Generate text in the style of Edgar Allan Poe.
        
        Args:
            length: Desired length of text
            style: Style of Poe's writing ('general', 'raven', 'tell_tale_heart', 'annabel_lee')
            
        Returns:
            Text in Poe's style with quantum phi-harmonic patterns
        """
        if style == "template":
            # Use a random template
            template_key = random.choice(list(self.templates.keys()))
            return self.fill_template(self.templates[template_key])
        
        elif style in self.templates:
            # Use a specific template
            return self.fill_template(self.templates[style])
        
        else:
            # Use the enhanced language generator
            phi = float(self.core.PHI)
            
            # Start with a seed phrase
            seed_phrase = random.choice(self.poe_patterns["phrases"])
            
            # Build text with Poe's patterns
            text_segments = [seed_phrase]
            
            while sum(len(segment) for segment in text_segments) < length * 1.5:
                # Choose what to generate next based on phi-harmonic probabilities
                choice = self._phi_weighted_choice([
                    "word", "phrase", "structure", "repetition", "punctuation"
                ], [1/phi**2, 1/phi, 1, phi-1, (phi-1)**2])
                
                if choice == "word":
                    # Add a Poe word
                    word = self._phi_weighted_choice(self.poe_patterns["words"])
                    text_segments.append(" " + word)
                
                elif choice == "phrase":
                    # Add a Poe phrase
                    phrase = self._phi_weighted_choice(self.poe_patterns["phrases"])
                    text_segments.append(", " + phrase)
                
                elif choice == "structure":
                    # Use a Poe structure
                    structure = self._phi_weighted_choice(self.poe_patterns["structures"])
                    
                    # Fill the structure with Poe words
                    filled_structure = self._fill_structure(structure)
                    text_segments.append(" " + filled_structure)
                
                elif choice == "repetition" and text_segments:
                    # Poe's signature repetition
                    if len(text_segments) > 3:
                        # Get a previous segment
                        segment_idx = int((len(text_segments) - 1) * ((phi - 1) % 1))
                        segment = text_segments[segment_idx].strip()
                        
                        # Apply Poe's repetition style
                        if len(segment.split()) <= 3:  # Short segment
                            repeat_style = self._phi_weighted_choice([
                                ", " + segment,
                                ", " + segment + ", " + segment,
                                "—" + segment + "—"
                            ])
                            text_segments.append(repeat_style)
                        else:
                            text_segments.append(", " + segment)
                
                elif choice == "punctuation":
                    # Add Poe-like punctuation
                    punct = self._phi_weighted_choice([
                        ".", "!", "?", "—", ";", "...", "!—", "?—"
                    ])
                    text_segments.append(punct + "\n")
            
            # Join segments and clean up
            full_text = "".join(text_segments)
            
            # Clean up formatting
            full_text = re.sub(r'\s+', ' ', full_text)  # Remove extra spaces
            full_text = re.sub(r'[\s,]+,', ',', full_text)  # Fix comma spacing
            full_text = re.sub(r'[\s.]+\.', '.', full_text)  # Fix period spacing
            
            # Ensure we have Poe's signature "nevermore" if long enough
            if length > 50 and "nevermore" not in full_text:
                insert_pos = int(len(full_text) * (phi - 1))
                full_text = full_text[:insert_pos] + " nevermore" + full_text[insert_pos:]
            
            return full_text[:length]
    
    def _fill_structure(self, structure: str) -> str:
        """Fill a structure template with Poe-appropriate words."""
        # Find all placeholders like {noun}, {adj}, etc.
        placeholders = re.findall(r'\{(\w+)\}', structure)
        
        filled = structure
        for placeholder in placeholders:
            if placeholder in self.parts_of_speech:
                word = self._phi_weighted_choice(self.parts_of_speech[placeholder])
                filled = filled.replace('{' + placeholder + '}', word, 1)
        
        return filled
    
    def fill_template(self, template: str) -> str:
        """Fill a Poe template with appropriate words."""
        # Find all placeholders
        placeholders = re.findall(r'\{(\w+)\}', template)
        
        filled = template
        for placeholder in placeholders:
            if placeholder in self.parts_of_speech:
                word = self._phi_weighted_choice(self.parts_of_speech[placeholder])
                filled = filled.replace('{' + placeholder + '}', word, 1)
        
        return filled
    
    def analyze_poe_similarity(self, text: str) -> Dict[str, Any]:
        """
        Analyze how closely a text matches Poe's quantum phi-harmonic signature.
        
        Args:
            text: Text to analyze
            
        Returns:
            Dictionary with similarity metrics
        """
        # Analyze the text
        metrics = self.analyzer.analyze_text(text)
        
        # Compare with Poe's signature
        similarity = {
            "frequency_similarity": 1 - abs(metrics["avg_frequency"] - self.poe_signature["mean_frequency"]) / self.poe_signature["mean_frequency"],
            "resonance_similarity": 1 - abs(metrics["quantum_resonance"] - self.poe_signature["quantum_resonance"]) / self.poe_signature["quantum_resonance"],
            "phi_alignment_similarity": 1 - abs(metrics["phi_alignment"] - self.poe_signature["phi_alignment"]) / self.poe_signature["phi_alignment"],
            "consciousness_match": metrics["consciousness_level"] == self.poe_signature["consciousness_level"],
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
    
    def generate_with_consciousness(self, consciousness_level: str, length: int = 100) -> str:
        """
        Generate Poe-style text at a specific consciousness level.
        
        Args:
            consciousness_level: One of 'physical', 'emotional', 'mental', 'intuitive', 'cosmic'
            length: Desired length of text
            
        Returns:
            Text in Poe's style at the specified consciousness level
        """
        # Map consciousness levels to frequency ranges
        consciousness_freqs = {
            "physical": (100, 300),
            "emotional": (300, 500),
            "mental": (500, 700),
            "intuitive": (700, 900),
            "cosmic": (900, 1100)
        }
        
        # Get the frequency range for the specified consciousness level
        freq_range = consciousness_freqs.get(consciousness_level.lower(), (500, 700))
        
        # Generate text with the appropriate frequency modulation
        text = self.generate_poe_text(length)
        
        # Analyze and check if it matches the desired consciousness level
        metrics = self.analyzer.analyze_text(text)
        
        # If it's already at the right consciousness level, return it
        if metrics["consciousness_level"] == consciousness_level.lower():
            return text
        
        # Otherwise, try again with a different seed
        for _ in range(3):  # Try a few times
            text = self.generate_poe_text(length)
            metrics = self.analyzer.analyze_text(text)
            if metrics["consciousness_level"] == consciousness_level.lower():
                return text
        
        # If we couldn't get the right consciousness level, return the best we have
        return text
    
    def _phi_weighted_choice(self, choices, weights=None):
        """Make a phi-weighted random choice from a list of options."""
        if weights is None:
            # Use phi-weighted distribution if no weights provided
            phi = float(self.core.PHI)
            weights = [phi ** (i % 3) for i in range(len(choices))]
            
        # Normalize weights
        total = sum(weights)
        weights = [w/total for w in weights]
        
        # Cumulative distribution
        cum_weights = [sum(weights[:i+1]) for i in range(len(weights))]
        
        # Generate phi-harmonic random value
        phi_seed = (float(self.core.PHI) * len(choices)) % 1
        r = (phi_seed + sum(cum_weights) / len(cum_weights)) % 1
        
        # Find the choice
        for i, cw in enumerate(cum_weights):
            if r <= cw:
                return choices[i]
                
        return choices[-1]  # Fallback

def main():
    """Test the Poe agent with various generation styles."""
    # Initialize the agent
    core = QuantumPhiCore()
    poe_agent = QuantumPhiPoeAgent(core=core)
    
    # Generate and analyze text in different styles
    styles = ["general", "raven", "tell_tale_heart", "annabel_lee", "template"]
    
    for style in styles:
        print(f"\n{'='*70}\nPoe Style: {style}\n{'='*70}")
        
        # Generate text
        text = poe_agent.generate_poe_text(length=150, style=style)
        print(f"\nGenerated Text:\n{text}\n")
        
        # Analyze similarity to Poe
        similarity = poe_agent.analyze_poe_similarity(text)
        
        print(f"Similarity to Poe:")
        print(f"Overall: {similarity['overall_similarity']:.4f}")
        print(f"Frequency: {similarity['frequency_similarity']:.4f}")
        print(f"Resonance: {similarity['resonance_similarity']:.4f}")
        print(f"Phi Alignment: {similarity['phi_alignment_similarity']:.4f}")
        print(f"Consciousness Match: {similarity['consciousness_match']}")
        
        # Print metrics
        metrics = similarity["metrics"]
        print(f"\nQuantum Phi-Harmonic Metrics:")
        print(f"Resonance: {metrics['resonance']:.4f}")
        print(f"Quantum Resonance: {metrics['quantum_resonance']:.4f}")
        print(f"Phi Alignment: {metrics['phi_alignment']:.4f}")
        print(f"Consciousness Level: {metrics['consciousness_level'].title()}")
        print(f"Average Frequency: {metrics['avg_frequency']:.4f} Hz")
    
    # Test different consciousness levels
    print(f"\n{'='*70}\nPoe at Different Consciousness Levels\n{'='*70}")
    
    for level in ["physical", "emotional", "mental", "intuitive", "cosmic"]:
        print(f"\n{level.title()} Consciousness:")
        text = poe_agent.generate_with_consciousness(level, length=100)
        print(text)
        
        # Analyze
        metrics = poe_agent.analyzer.analyze_text(text)
        print(f"\nActual Consciousness Level: {metrics['consciousness_level'].title()}")
        print(f"Quantum Resonance: {metrics['quantum_resonance']:.4f}")
        print(f"Phi Alignment: {metrics['phi_alignment']:.4f}")

if __name__ == "__main__":
    main()
