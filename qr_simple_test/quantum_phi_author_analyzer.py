"""
Quantum Phi-Harmonic Author Analyzer

A unified system for analyzing and generating text based on quantum phi-harmonic principles
for any author. This module allows for easy comparison between different authors' quantum
signatures and can generate text that mimics their unique patterns.
"""

import random
import numpy as np
from typing import Dict, List, Any, Tuple, Optional

from quantum_phi_core import QuantumPhiCore
from quantum_phi_pattern_analyzer import QuantumPhiPatternAnalyzer

class QuantumPhiAuthorAnalyzer:
    """Analyzes and generates text based on quantum phi-harmonic principles for any author."""
    
    def __init__(self):
        """Initialize the author analyzer with quantum phi core components."""
        self.core = QuantumPhiCore()
        self.analyzer = QuantumPhiPatternAnalyzer(core=self.core)
        self.phi = float(self.core.PHI)
        
        # Dictionary to store author signatures
        self.author_signatures = {
            "poe": {
                "consciousness_level": "cosmic",
                "mean_frequency": 517.15,
                "quantum_resonance": 0.6987,
                "phi_alignment": 0.8644,
                "description": "Dark, rhythmic, emotionally intense with strong repetition patterns"
            },
            "hemingway": {
                "consciousness_level": "cosmic",
                "mean_frequency": 576.26,
                "quantum_resonance": 0.6849,
                "phi_alignment": 0.8518,
                "description": "Direct, sparse, physically grounded with strategic minimalism"
            },
            "austen": {
                "consciousness_level": "cosmic",
                "mean_frequency": 525.18,
                "quantum_resonance": 0.7091,
                "phi_alignment": 0.8552,
                "description": "Socially complex, dialogue-rich, with balanced sentence structures"
            }
        }
        
        # Author-specific language components
        self.author_components = {
            "poe": {
                "words": [
                    "nevermore", "midnight", "raven", "dreary", "weary", "shadow", 
                    "sorrow", "darkness", "chamber", "melancholy", "heart", "soul", 
                    "horror", "fear", "dread", "tomb", "grave", "death", "night", 
                    "black", "ghastly", "grim", "phantom", "spectre", "ghost",
                    "terror", "madness", "abyss", "chasm", "void", "eternity"
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
                    "bells, bells, bells"
                ],
                "structures": [
                    "{adj} and {adj} {noun}",
                    "the {adj} {noun} of {noun}",
                    "{adv} {verb} the {noun}",
                    "the {noun}, {adj} and {adj}"
                ],
                "parts_of_speech": {
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
                },
                "generation_weights": [0.2, 0.3, 0.2, 0.2, 0.1],  # word, phrase, structure, repetition, punctuation
                "punctuation": [".", "!", "?", "—", ";", "..."],
                "line_break_freq": 40,
                "line_break_prob": 1.0
            },
            "hemingway": {
                "words": [
                    "sea", "fish", "boat", "man", "old", "sun", "war", "drink", 
                    "bull", "fight", "true", "good", "bad", "death", "life", "love",
                    "simple", "clean", "hard", "rain", "wine", "gun", "soldier", 
                    "brave", "afraid", "kill", "live", "mountain", "river", "plain"
                ],
                "phrases": [
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
                ],
                "structures": [
                    "The {noun} was {adj}.",
                    "He {verb} the {noun}.",
                    "It was {adj} and {adj}.",
                    "They {verb} {adv}."
                ],
                "parts_of_speech": {
                    "noun": ["sea", "fish", "boat", "man", "sun", "war", "drink", "bull", 
                            "fight", "rain", "wine", "gun", "soldier", "mountain", "river"],
                    "adj": ["old", "good", "bad", "simple", "clean", "hard", "brave", 
                           "afraid", "hot", "cold", "tired", "hungry", "thirsty", "quiet", "loud"],
                    "verb": ["said", "went", "saw", "felt", "knew", "thought", "drank", 
                            "ate", "slept", "fought", "killed", "loved", "hated", "walked", "ran"],
                    "adv": ["slowly", "quickly", "quietly", "loudly", "well", "badly", 
                           "simply", "carefully", "carelessly", "easily", "hard"]
                },
                "generation_weights": [0.2, 0.2, 0.3, 0.2, 0.1],  # word, phrase, structure, short_sentence, punctuation
                "punctuation": [".", ".", ".", "!", "?"],  # More periods, fewer complex punctuation
                "line_break_freq": 80,
                "line_break_prob": 0.3
            },
            "austen": {
                "words": [
                    "agreeable", "amiable", "attachment", "bewitching", "civility", 
                    "countenance", "delightful", "elegant", "endeavour", "felicity", 
                    "fortnight", "handsome", "imprudent", "indulgence", "ladyship", 
                    "matrimony", "modesty", "partiality", "persuasion", "propriety", 
                    "sensibility", "sentiment", "society", "solicitude", "tranquility"
                ],
                "phrases": [
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
                ],
                "structures": [
                    "The {noun} was {adj}, though perhaps not so {adj} as to warrant {noun}.",
                    "She had not been in the {noun} for more than {adj} minutes when {noun} appeared.",
                    "It is a truth universally acknowledged that a {adj} {noun} must be in want of a {noun}.",
                    "There was a general {noun} about the {adj} nature of the {noun}."
                ],
                "parts_of_speech": {
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
                },
                "generation_weights": [0.15, 0.25, 0.3, 0.2, 0.1],  # word, phrase, structure, complex_sentence, punctuation
                "punctuation": [".", ";", ",", "!", "?"],
                "line_break_freq": 120,
                "line_break_prob": 0.4
            }
        }
    
    def calibrate_author_signature(self, author_name: str, sample_text: str) -> Dict:
        """Analyze a sample text to calibrate an author's quantum signature."""
        # Analyze the text
        metrics = self.analyzer.analyze_text(sample_text)
        
        # Create a new author signature
        author_signature = {
            "consciousness_level": metrics["consciousness_level"],
            "mean_frequency": metrics["avg_frequency"],
            "quantum_resonance": metrics["quantum_resonance"],
            "phi_alignment": metrics["phi_alignment"],
            "description": f"Calibrated from sample text ({len(sample_text)} characters)"
        }
        
        # Store the signature
        author_name = author_name.lower()
        self.author_signatures[author_name] = author_signature
        
        return author_signature
    
    def add_author_components(self, author_name: str, components: Dict) -> None:
        """Add language components for a new author."""
        author_name = author_name.lower()
        self.author_components[author_name] = components
    
    def generate_author_text(self, author_name: str, length: int = 100) -> str:
        """Generate text in the style of the specified author."""
        author_name = author_name.lower()
        
        # Check if we have this author's signature and components
        if author_name not in self.author_signatures:
            raise ValueError(f"No quantum signature found for author: {author_name}")
        
        if author_name not in self.author_components:
            raise ValueError(f"No language components found for author: {author_name}")
        
        # Get author components
        components = self.author_components[author_name]
        
        # Start with a seed phrase
        text = random.choice(components["phrases"])
        
        # Add words and phrases until we reach desired length
        while len(text) < length:
            # Choose what to add next based on author's style
            choice_options = ["word", "phrase", "structure"]
            
            # Add author-specific options
            if author_name == "poe":
                choice_options.append("repetition")
            elif author_name == "hemingway":
                choice_options.append("short_sentence")
            elif author_name == "austen":
                choice_options.append("complex_sentence")
            
            choice_options.append("punctuation")
            
            # Make weighted choice
            choice = self._weighted_choice(
                choice_options, 
                components["generation_weights"]
            )
            
            if choice == "word":
                # Add an author word
                text += " " + random.choice(components["words"])
                
            elif choice == "phrase":
                # Add an author phrase with appropriate connector
                connector = " " if author_name == "hemingway" else ", "
                text += connector + random.choice(components["phrases"])
                
            elif choice == "structure":
                # Use an author structure
                structure = random.choice(components["structures"])
                filled = self._fill_structure(structure, components["parts_of_speech"])
                text += " " + filled
                
            elif choice == "repetition" and author_name == "poe" and len(text) > 20:
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
                        
            elif choice == "short_sentence" and author_name == "hemingway":
                # Hemingway's signature short sentences
                noun = random.choice(components["parts_of_speech"]["noun"])
                verb = random.choice(components["parts_of_speech"]["verb"])
                text += f" The {noun} {verb}."
                
            elif choice == "complex_sentence" and author_name == "austen":
                # Austen's signature complex sentences with multiple clauses
                adj1 = random.choice(components["parts_of_speech"]["adj"])
                adj2 = random.choice(components["parts_of_speech"]["adj"])
                noun1 = random.choice(components["parts_of_speech"]["noun"])
                noun2 = random.choice(components["parts_of_speech"]["noun"])
                adv = random.choice(components["parts_of_speech"]["adv"])
                
                text += f" The {noun1} was {adv} {adj1}, and the {noun2} was no less {adj2}."
                
            elif choice == "punctuation":
                # Add author-appropriate punctuation
                punct = random.choice(components["punctuation"])
                text += punct + " "
            
            # Occasionally add a line break based on author style
            if (len(text) % components["line_break_freq"] == 0 and 
                len(text) > components["line_break_freq"] and 
                random.random() < components["line_break_prob"]):
                text += "\n"
                
                # Add an extra line break for Austen's paragraphs
                if author_name == "austen":
                    text += "\n"
        
        # Add author-specific finishing touches
        if author_name == "poe" and length > 50 and "nevermore" not in text:
            insert_pos = int(len(text) * 0.618)  # Golden ratio position
            text = text[:insert_pos] + " nevermore" + text[insert_pos:]
        
        return text[:length]
    
    def _fill_structure(self, structure: str, parts_of_speech: Dict[str, List[str]]) -> str:
        """Fill a structure template with appropriate words."""
        filled = structure
        
        # Replace {noun}, {adj}, etc. with appropriate words
        for pos in parts_of_speech:
            placeholder = "{" + pos + "}"
            while placeholder in filled:
                word = random.choice(parts_of_speech[pos])
                filled = filled.replace(placeholder, word, 1)
        
        return filled
    
    def _weighted_choice(self, choices: List[Any], weights: Optional[List[float]] = None) -> Any:
        """Make a weighted random choice."""
        if weights is None:
            return random.choice(choices)
        
        # Ensure weights match choices length
        if len(weights) < len(choices):
            weights = weights + [weights[-1]] * (len(choices) - len(weights))
        elif len(weights) > len(choices):
            weights = weights[:len(choices)]
            
        return random.choices(choices, weights=weights, k=1)[0]
    
    def analyze_similarity_to_author(self, text: str, author_name: str) -> Dict:
        """Analyze how closely a text matches an author's quantum phi-harmonic signature."""
        author_name = author_name.lower()
        
        # Check if we have this author's signature
        if author_name not in self.author_signatures:
            raise ValueError(f"No quantum signature found for author: {author_name}")
        
        # Get author signature
        author_signature = self.author_signatures[author_name]
        
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
    
    def compare_authors(self, author1: str, author2: str) -> Dict:
        """Compare the quantum signatures of two authors."""
        author1 = author1.lower()
        author2 = author2.lower()
        
        # Check if we have both authors' signatures
        if author1 not in self.author_signatures:
            raise ValueError(f"No quantum signature found for author: {author1}")
        
        if author2 not in self.author_signatures:
            raise ValueError(f"No quantum signature found for author: {author2}")
        
        # Get author signatures
        sig1 = self.author_signatures[author1]
        sig2 = self.author_signatures[author2]
        
        # Calculate similarities
        comparison = {
            "frequency_similarity": 1 - abs(sig1["mean_frequency"] - sig2["mean_frequency"]) / max(sig1["mean_frequency"], sig2["mean_frequency"]),
            "resonance_similarity": 1 - abs(sig1["quantum_resonance"] - sig2["quantum_resonance"]) / max(sig1["quantum_resonance"], sig2["quantum_resonance"]),
            "phi_alignment_similarity": 1 - abs(sig1["phi_alignment"] - sig2["phi_alignment"]) / max(sig1["phi_alignment"], sig2["phi_alignment"]),
            "consciousness_match": sig1["consciousness_level"] == sig2["consciousness_level"],
            "overall_similarity": 0.0  # Will calculate below
        }
        
        # Calculate overall similarity
        comparison["overall_similarity"] = (
            comparison["frequency_similarity"] * 0.3 +
            comparison["resonance_similarity"] * 0.3 +
            comparison["phi_alignment_similarity"] * 0.3 +
            (0.1 if comparison["consciousness_match"] else 0)
        )
        
        return comparison
    
    def get_all_author_signatures(self) -> Dict[str, Dict]:
        """Return all calibrated author signatures."""
        return self.author_signatures
    
    def get_author_signature(self, author_name: str) -> Dict:
        """Return a specific author's quantum signature."""
        author_name = author_name.lower()
        
        if author_name not in self.author_signatures:
            raise ValueError(f"No quantum signature found for author: {author_name}")
        
        return self.author_signatures[author_name]


def main():
    """Test the quantum phi author analyzer with multiple authors."""
    print("=" * 70)
    print("QUANTUM PHI-HARMONIC AUTHOR ANALYZER")
    print("=" * 70)
    
    # Initialize the analyzer
    analyzer = QuantumPhiAuthorAnalyzer()
    
    # Get all author signatures
    signatures = analyzer.get_all_author_signatures()
    
    print("\nCalibrated Author Quantum Signatures:")
    for author, signature in signatures.items():
        print(f"\n{author.title()}:")
        print(f"  Consciousness Level: {signature['consciousness_level'].title()}")
        print(f"  Mean Frequency: {signature['mean_frequency']:.2f} Hz")
        print(f"  Quantum Resonance: {signature['quantum_resonance']:.4f}")
        print(f"  Phi Alignment: {signature['phi_alignment']:.4f}")
        print(f"  Description: {signature['description']}")
    
    # Compare all authors
    print("\n" + "=" * 70)
    print("AUTHOR COMPARISON MATRIX")
    print("=" * 70)
    
    authors = list(signatures.keys())
    
    print("\nOverall Similarity:")
    print(f"{'':12}", end="")
    for author in authors:
        print(f"{author.title():12}", end="")
    print()
    
    for author1 in authors:
        print(f"{author1.title():12}", end="")
        for author2 in authors:
            if author1 == author2:
                print(f"{'1.0000':12}", end="")
            else:
                comparison = analyzer.compare_authors(author1, author2)
                print(f"{comparison['overall_similarity']:.4f}  ", end="")
        print()
    
    # Generate text for each author
    print("\n" + "=" * 70)
    print("GENERATED TEXT SAMPLES")
    print("=" * 70)
    
    for author in authors:
        print(f"\n{author.title()} Style:")
        text = analyzer.generate_author_text(author, length=150)
        print(text)
        
        # Analyze similarity to all authors
        print("\nSimilarity Analysis:")
        for target_author in authors:
            similarity = analyzer.analyze_similarity_to_author(text, target_author)
            print(f"  To {target_author.title()}: {similarity['overall_similarity']:.4f}")
    
    # Cross-generation test
    print("\n" + "=" * 70)
    print("CROSS-GENERATION TEST")
    print("=" * 70)
    
    # Generate text in Poe's style and analyze similarity to Hemingway and Austen
    poe_text = analyzer.generate_author_text("poe", length=200)
    print("\nPoe-style text:")
    print(poe_text)
    
    poe_to_hemingway = analyzer.analyze_similarity_to_author(poe_text, "hemingway")
    poe_to_austen = analyzer.analyze_similarity_to_author(poe_text, "austen")
    
    print(f"\nPoe-style text similarity to Hemingway: {poe_to_hemingway['overall_similarity']:.4f}")
    print(f"Poe-style text similarity to Austen: {poe_to_austen['overall_similarity']:.4f}")
    
    # Generate text in Hemingway's style and analyze similarity to Poe and Austen
    hemingway_text = analyzer.generate_author_text("hemingway", length=200)
    print("\nHemingway-style text:")
    print(hemingway_text)
    
    hemingway_to_poe = analyzer.analyze_similarity_to_author(hemingway_text, "poe")
    hemingway_to_austen = analyzer.analyze_similarity_to_author(hemingway_text, "austen")
    
    print(f"\nHemingway-style text similarity to Poe: {hemingway_to_poe['overall_similarity']:.4f}")
    print(f"Hemingway-style text similarity to Austen: {hemingway_to_austen['overall_similarity']:.4f}")

if __name__ == "__main__":
    main()
