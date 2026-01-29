#!/usr/bin/env python3
"""
Quantum Phi-Harmonic Pattern Analyzer

Analyzes text and other content for quantum phi-harmonic patterns,
consciousness frequencies, and golden ratio structures.
"""

import os
import json
import math
import random
import re
from typing import Dict, List, Any, Tuple, Optional
from pathlib import Path

# Import core if available, otherwise define constants here
try:
    from quantum_phi_core import QuantumPhiCore
except ImportError:
    class QuantumPhiCore:
        """Simplified QuantumPhiCore for standalone operation."""
        def __init__(self):
            self.PHI = (1 + 5 ** 0.5) / 2  # Golden Ratio ≈ 1.618034
            self.PI = 3.141592653589793
            self.E = 2.718281828459045


class QuantumPhiAnalyzer:
    """
    Quantum Phi-Harmonic Pattern Analyzer.
    
    Analyzes content for quantum phi-harmonic patterns, consciousness frequencies,
    and golden ratio structures. Can compare content to author signatures and
    determine similarity scores.
    """
    
    def __init__(self):
        """Initialize the analyzer."""
        self.core = QuantumPhiCore()
        self.phi = float(self.core.PHI)
        self.pi = float(self.core.PI)
        self.e = float(self.core.E)
        
        # Load configuration if available
        self.config = self._load_config()
        
        # Initialize author signatures
        self.author_signatures = self.config.get("author_signatures", {})
        
        # Initialize composer signatures
        self.composer_signatures = self.config.get("composer_signatures", {})
        
        # Initialize consciousness levels
        self.consciousness_levels = self.config.get("consciousness_levels", {})
        
        # Initialize quantum resonance scale
        self.quantum_resonance = self.config.get("quantum_resonance", {})
    
    def _load_config(self) -> Dict:
        """Load configuration from config file."""
        config_path = os.path.join(os.path.dirname(__file__), "quantum_phi_config.json")
        
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Warning: Could not load config file: {e}")
        
        # Default configuration
        return {
            "consciousness_levels": {
                "physical": {"min_freq": 0, "max_freq": 200},
                "emotional": {"min_freq": 200, "max_freq": 300},
                "mental": {"min_freq": 300, "max_freq": 400},
                "intuitive": {"min_freq": 400, "max_freq": 500},
                "cosmic": {"min_freq": 500, "max_freq": 1000}
            },
            "author_signatures": {
                "poe": {
                    "frequency": 517.15,
                    "resonance": 0.6987,
                    "phi_alignment": 0.8644
                },
                "hemingway": {
                    "frequency": 576.26,
                    "resonance": 0.6849,
                    "phi_alignment": 0.8518
                },
                "austen": {
                    "frequency": 525.18,
                    "resonance": 0.7091,
                    "phi_alignment": 0.8552
                },
                "shakespeare": {
                    "frequency": 555.40,
                    "resonance": 0.6730,
                    "phi_alignment": 0.8537
                }
            }
        }
    
    def analyze_text(self, text: str) -> Dict:
        """
        Analyze text for quantum phi-harmonic patterns.
        
        Args:
            text: The text to analyze
            
        Returns:
            Dictionary with analysis results
        """
        # Calculate basic metrics
        word_count = len(text.split())
        sentence_count = len(re.split(r'[.!?]+', text))
        paragraph_count = len([p for p in text.split('\n\n') if p.strip()])
        
        # Calculate quantum phi-harmonic metrics
        frequency = self._calculate_consciousness_frequency(text)
        consciousness_level = self._determine_consciousness_level(frequency)
        phi_resonance = self._calculate_phi_resonance(text)
        phi_alignment = self._calculate_phi_alignment(text)
        
        # Determine author similarity
        author_similarities = self._calculate_author_similarities(frequency, phi_resonance, phi_alignment)
        
        # Determine most likely author
        if author_similarities:
            most_likely_author = max(author_similarities.items(), key=lambda x: x[1])
        else:
            most_likely_author = ("unknown", 0.0)
        
        # Calculate quantum fingerprint
        quantum_fingerprint = self._calculate_quantum_fingerprint(text)
        
        return {
            "word_count": word_count,
            "sentence_count": sentence_count,
            "paragraph_count": paragraph_count,
            "consciousness_frequency": frequency,
            "consciousness_level": consciousness_level,
            "phi_resonance": phi_resonance,
            "phi_alignment": phi_alignment,
            "most_likely_author": most_likely_author[0],
            "author_confidence": most_likely_author[1],
            "author_similarities": author_similarities,
            "quantum_fingerprint": quantum_fingerprint
        }
    
    def analyze_file(self, file_path: str) -> Dict:
        """
        Analyze a text file for quantum phi-harmonic patterns.
        
        Args:
            file_path: Path to the file to analyze
            
        Returns:
            Dictionary with analysis results
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
            
            result = self.analyze_text(text)
            result["file_path"] = file_path
            
            return result
        except Exception as e:
            return {
                "error": str(e),
                "file_path": file_path
            }
    
    def compare_texts(self, text1: str, text2: str) -> Dict:
        """
        Compare two texts for quantum phi-harmonic similarity.
        
        Args:
            text1: First text to compare
            text2: Second text to compare
            
        Returns:
            Dictionary with comparison results
        """
        # Analyze both texts
        analysis1 = self.analyze_text(text1)
        analysis2 = self.analyze_text(text2)
        
        # Calculate similarity metrics
        frequency_similarity = 1.0 - abs(analysis1["consciousness_frequency"] - analysis2["consciousness_frequency"]) / 1000.0
        resonance_similarity = 1.0 - abs(analysis1["phi_resonance"] - analysis2["phi_resonance"])
        alignment_similarity = 1.0 - abs(analysis1["phi_alignment"] - analysis2["phi_alignment"])
        
        # Calculate overall quantum similarity
        quantum_similarity = (frequency_similarity * 0.3) + (resonance_similarity * 0.3) + (alignment_similarity * 0.4)
        
        return {
            "text1_analysis": analysis1,
            "text2_analysis": analysis2,
            "frequency_similarity": frequency_similarity,
            "resonance_similarity": resonance_similarity,
            "alignment_similarity": alignment_similarity,
            "quantum_similarity": quantum_similarity
        }
    
    def _calculate_consciousness_frequency(self, text: str) -> float:
        """
        Calculate the consciousness frequency of a text.
        
        This measures the vibrational quality of the text on the consciousness
        frequency spectrum from physical (0-200 Hz) to cosmic (500-1000 Hz).
        """
        # Split into paragraphs, sentences, and words
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        sentences = [s.strip() for p in paragraphs for s in re.split(r'[.!?]+', p) if s.strip()]
        words = [w for s in sentences for w in s.split()]
        
        # Calculate complexity metrics
        avg_word_length = sum(len(w) for w in words) / len(words) if words else 0
        avg_sentence_length = len(words) / len(sentences) if sentences else 0
        avg_paragraph_length = len(sentences) / len(paragraphs) if paragraphs else 0
        
        # Calculate vocabulary richness
        unique_words = len(set(w.lower() for w in words))
        vocabulary_richness = unique_words / len(words) if words else 0
        
        # Calculate phi-harmonic patterns
        phi_patterns = self._detect_phi_patterns(sentences)
        
        # Calculate base frequency based on complexity
        base_frequency = 100 + (avg_word_length * 10) + (avg_sentence_length * 2) + (avg_paragraph_length * 5)
        
        # Adjust for vocabulary richness
        base_frequency += vocabulary_richness * 200
        
        # Adjust for phi-harmonic patterns
        base_frequency += phi_patterns * 300
        
        # Apply phi modulation
        frequency = base_frequency * (1 + (self.phi - 1) * phi_patterns)
        
        # Ensure within reasonable bounds
        return max(0.0, min(1000.0, frequency))
    
    def _detect_phi_patterns(self, sentences: List[str]) -> float:
        """
        Detect phi-harmonic patterns in a list of sentences.
        Returns a score between 0.0 and 1.0.
        """
        if not sentences:
            return 0.0
        
        # Calculate sentence lengths
        lengths = [len(s.split()) for s in sentences]
        
        # Calculate ratios between consecutive sentences
        ratios = []
        for i in range(1, len(lengths)):
            if lengths[i-1] > 0:
                ratios.append(lengths[i] / lengths[i-1])
        
        # Calculate proximity to phi for each ratio
        phi_proximities = [abs(r - self.phi) for r in ratios]
        
        # Calculate average proximity to phi
        avg_proximity = sum(phi_proximities) / len(phi_proximities) if phi_proximities else 1.0
        
        # Convert to a score between 0.0 and 1.0
        return 1.0 / (1.0 + avg_proximity)
    
    def _determine_consciousness_level(self, frequency: float) -> str:
        """Determine the consciousness level based on frequency."""
        for level, range_data in self.consciousness_levels.items():
            min_freq = range_data.get("min_freq", 0)
            max_freq = range_data.get("max_freq", 0)
            
            if min_freq <= frequency <= max_freq:
                return level
        
        # Default to cosmic if above all ranges
        if frequency > 500:
            return "cosmic"
        
        # Default to physical if below all ranges
        return "physical"
    
    def _calculate_phi_resonance(self, text: str) -> float:
        """
        Calculate phi-harmonic resonance for a text.
        
        This measures how well the text resonates with golden ratio patterns
        at multiple scales (words, sentences, paragraphs).
        """
        # Split into paragraphs, sentences, and words
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        sentences = [s.strip() for p in paragraphs for s in re.split(r'[.!?]+', p) if s.strip()]
        words = [w for s in sentences for w in s.split()]
        
        # Calculate length metrics
        paragraph_lengths = [len(p.split()) for p in paragraphs]
        sentence_lengths = [len(s.split()) for s in sentences]
        
        # Calculate average lengths
        avg_paragraph_len = sum(paragraph_lengths) / len(paragraph_lengths) if paragraph_lengths else 0
        avg_sentence_len = sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0
        
        # Calculate phi-resonance based on proximity to golden ratio
        paragraph_phi_diff = abs(avg_paragraph_len / avg_sentence_len - self.phi) if avg_sentence_len else 1
        sentence_word_distribution = self._analyze_distribution(sentence_lengths)
        
        # Calculate word pattern resonance
        word_pattern_resonance = self._analyze_word_patterns(words)
        
        # Combine metrics into overall phi resonance (0.0 to 1.0)
        phi_resonance = 0.3 + (1 / (1 + paragraph_phi_diff)) * 0.3 + sentence_word_distribution * 0.2 + word_pattern_resonance * 0.2
        
        # Ensure within bounds
        return max(0.0, min(1.0, phi_resonance))
    
    def _analyze_distribution(self, values: List[int]) -> float:
        """
        Analyze a distribution of values for phi-harmonic patterns.
        Returns a score between 0.0 and 1.0, where 1.0 is perfect phi-harmonic alignment.
        """
        if not values:
            return 0.0
        
        # Calculate differences between consecutive values
        diffs = [abs(values[i] - values[i-1]) for i in range(1, len(values))]
        
        # Calculate ratios between consecutive values
        ratios = [values[i] / values[i-1] if values[i-1] else 0 for i in range(1, len(values))]
        
        # Calculate proximity to phi for each ratio
        phi_proximities = [abs(r - self.phi) for r in ratios if r > 0]
        
        # Calculate average proximity to phi
        avg_proximity = sum(phi_proximities) / len(phi_proximities) if phi_proximities else 1.0
        
        # Convert to a score between 0.0 and 1.0
        return 1.0 / (1.0 + avg_proximity)
    
    def _analyze_word_patterns(self, words: List[str]) -> float:
        """
        Analyze word patterns for phi-harmonic resonance.
        Returns a score between 0.0 and 1.0.
        """
        if not words:
            return 0.0
        
        # Calculate word lengths
        lengths = [len(w) for w in words]
        
        # Calculate average word length
        avg_length = sum(lengths) / len(lengths)
        
        # Calculate proximity to phi and phi^2
        phi_proximity = abs(avg_length - self.phi)
        phi_squared_proximity = abs(avg_length - self.phi**2)
        
        # Use the closer proximity
        best_proximity = min(phi_proximity, phi_squared_proximity)
        
        # Convert to a score between 0.0 and 1.0
        return 1.0 / (1.0 + best_proximity)
    
    def _calculate_phi_alignment(self, text: str) -> float:
        """
        Calculate phi alignment for a text.
        
        This measures how well the text structure aligns with golden ratio proportions
        at multiple scales (words, sentences, paragraphs).
        """
        # Split into paragraphs, sentences, and words
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        sentences = [s.strip() for p in paragraphs for s in re.split(r'[.!?]+', p) if s.strip()]
        words = [w for s in sentences for w in s.split()]
        
        # Calculate structural metrics
        total_paragraphs = len(paragraphs)
        total_sentences = len(sentences)
        total_words = len(words)
        
        # Calculate phi-based ideal proportions
        ideal_sentence_per_paragraph = self.phi
        ideal_words_per_sentence = self.phi ** 2
        
        # Calculate actual proportions
        actual_sentence_per_paragraph = total_sentences / total_paragraphs if total_paragraphs else 0
        actual_words_per_sentence = total_words / total_sentences if total_sentences else 0
        
        # Calculate alignment scores (0.0 to 1.0)
        paragraph_alignment = 1.0 / (1.0 + abs(actual_sentence_per_paragraph - ideal_sentence_per_paragraph))
        sentence_alignment = 1.0 / (1.0 + abs(actual_words_per_sentence - ideal_words_per_sentence))
        
        # Calculate word pattern alignment
        word_pattern_alignment = self._calculate_word_pattern_alignment(words)
        
        # Combine into overall phi alignment
        phi_alignment = (paragraph_alignment * 0.3) + (sentence_alignment * 0.3) + (word_pattern_alignment * 0.4)
        
        # Ensure within bounds
        return max(0.0, min(1.0, phi_alignment))
    
    def _calculate_word_pattern_alignment(self, words: List[str]) -> float:
        """
        Calculate word pattern alignment with phi-harmonic principles.
        Returns a score between 0.0 and 1.0.
        """
        if not words:
            return 0.0
        
        # Calculate word lengths
        lengths = [len(w) for w in words]
        
        # Find Fibonacci-like patterns in word lengths
        fibonacci_patterns = 0
        for i in range(2, len(lengths)):
            if abs(lengths[i] - (lengths[i-1] + lengths[i-2])) <= 1:
                fibonacci_patterns += 1
        
        # Calculate pattern density
        pattern_density = fibonacci_patterns / (len(lengths) - 2) if len(lengths) > 2 else 0
        
        # Calculate repetition patterns
        repetition_score = self._calculate_repetition_patterns(words)
        
        # Combine scores
        return 0.5 * pattern_density + 0.5 * repetition_score
    
    def _calculate_repetition_patterns(self, words: List[str]) -> float:
        """
        Calculate repetition patterns in word usage.
        Returns a score between 0.0 and 1.0.
        """
        if not words:
            return 0.0
        
        # Count word frequencies
        word_counts = {}
        for word in words:
            word_lower = word.lower()
            word_counts[word_lower] = word_counts.get(word_lower, 0) + 1
        
        # Calculate frequency distribution
        frequencies = list(word_counts.values())
        
        # Calculate ratio of unique words to total words
        unique_ratio = len(word_counts) / len(words)
        
        # Calculate ideal ratio based on phi
        ideal_ratio = 1 / self.phi
        
        # Calculate proximity to ideal ratio
        ratio_proximity = abs(unique_ratio - ideal_ratio)
        
        # Convert to a score between 0.0 and 1.0
        return 1.0 / (1.0 + ratio_proximity)
    
    def _calculate_author_similarities(self, frequency: float, phi_resonance: float, phi_alignment: float) -> Dict[str, float]:
        """
        Calculate similarity scores to known author signatures.
        
        Args:
            frequency: Consciousness frequency
            phi_resonance: Phi resonance score
            phi_alignment: Phi alignment score
            
        Returns:
            Dictionary mapping author names to similarity scores
        """
        similarities = {}
        
        for author, signature in self.author_signatures.items():
            # Get author metrics
            author_frequency = signature.get("frequency", 0)
            author_resonance = signature.get("resonance", 0)
            author_alignment = signature.get("phi_alignment", 0)
            
            # Calculate similarity components
            frequency_similarity = 1.0 - abs(frequency - author_frequency) / 1000.0
            resonance_similarity = 1.0 - abs(phi_resonance - author_resonance)
            alignment_similarity = 1.0 - abs(phi_alignment - author_alignment)
            
            # Calculate overall similarity
            similarity = (frequency_similarity * 0.3) + (resonance_similarity * 0.3) + (alignment_similarity * 0.4)
            
            # Add to results
            similarities[author] = similarity
        
        return similarities
    
    def _calculate_quantum_fingerprint(self, text: str) -> str:
        """
        Calculate a quantum fingerprint for the text.
        
        This is a unique identifier based on the quantum phi-harmonic properties
        of the text, represented as a hexadecimal string.
        """
        # Calculate basic metrics
        word_count = len(text.split())
        sentence_count = len(re.split(r'[.!?]+', text))
        paragraph_count = len([p for p in text.split('\n\n') if p.strip()])
        
        # Calculate quantum metrics
        frequency = self._calculate_consciousness_frequency(text)
        phi_resonance = self._calculate_phi_resonance(text)
        phi_alignment = self._calculate_phi_alignment(text)
        
        # Create a unique fingerprint
        fingerprint_value = (
            word_count * self.phi +
            sentence_count * (self.phi ** 2) +
            paragraph_count * (self.phi ** 3) +
            frequency * (self.phi ** 4) +
            phi_resonance * (self.phi ** 5) +
            phi_alignment * (self.phi ** 6)
        )
        
        # Convert to hexadecimal
        fingerprint = hex(int(fingerprint_value * 1000000))[2:]
        
        # Ensure consistent length
        return fingerprint.zfill(16)
    
    def generate_report(self, analysis: Dict) -> str:
        """
        Generate a human-readable report from analysis results.
        
        Args:
            analysis: Analysis results dictionary
            
        Returns:
            Formatted report as a string
        """
        # Extract metrics
        word_count = analysis.get("word_count", 0)
        sentence_count = analysis.get("sentence_count", 0)
        paragraph_count = analysis.get("paragraph_count", 0)
        frequency = analysis.get("consciousness_frequency", 0)
        consciousness_level = analysis.get("consciousness_level", "unknown")
        phi_resonance = analysis.get("phi_resonance", 0)
        phi_alignment = analysis.get("phi_alignment", 0)
        most_likely_author = analysis.get("most_likely_author", "unknown")
        author_confidence = analysis.get("author_confidence", 0)
        author_similarities = analysis.get("author_similarities", {})
        quantum_fingerprint = analysis.get("quantum_fingerprint", "")
        
        # Format the report
        report = [
            "# Quantum Phi-Harmonic Analysis Report",
            "",
            "## Basic Metrics",
            f"- Word Count: {word_count}",
            f"- Sentence Count: {sentence_count}",
            f"- Paragraph Count: {paragraph_count}",
            "",
            "## Quantum Phi-Harmonic Metrics",
            f"- Consciousness Frequency: {frequency:.2f} Hz",
            f"- Consciousness Level: {consciousness_level.title()}",
            f"- Phi Resonance: {phi_resonance:.4f}",
            f"- Phi Alignment: {phi_alignment:.4f}",
            "",
            "## Author Analysis",
            f"- Most Similar Author: {most_likely_author.title()}",
            f"- Confidence: {author_confidence:.4f}",
            "",
            "### Author Similarities"
        ]
        
        # Add author similarities
        for author, similarity in sorted(author_similarities.items(), key=lambda x: x[1], reverse=True):
            report.append(f"- {author.title()}: {similarity:.4f}")
        
        # Add quantum fingerprint
        report.extend([
            "",
            "## Quantum Fingerprint",
            f"- Fingerprint: {quantum_fingerprint}"
        ])
        
        # Add interpretation
        report.extend([
            "",
            "## Interpretation",
            f"This text operates at the {consciousness_level.title()} consciousness level ({frequency:.2f} Hz), "
            f"indicating a focus on {self._get_consciousness_focus(consciousness_level)}. "
            f"It exhibits a phi resonance of {phi_resonance:.4f}, which is "
            f"{self._interpret_phi_resonance(phi_resonance)}. "
            f"The phi alignment of {phi_alignment:.4f} shows "
            f"{self._interpret_phi_alignment(phi_alignment)}."
        ])
        
        # Add author interpretation if confidence is high enough
        if author_confidence > 0.7:
            report.append(
                f"The writing style shows strong similarities to {most_likely_author.title()} "
                f"(confidence: {author_confidence:.4f}), suggesting similar quantum phi-harmonic patterns "
                f"in the writing structure and style."
            )
        
        return "\n".join(report)
    
    def _get_consciousness_focus(self, level: str) -> str:
        """Get the focus description for a consciousness level."""
        focuses = {
            "physical": "material reality and sensory perception",
            "emotional": "feelings, relationships, and emotional resonance",
            "mental": "ideas, patterns, and analytical thinking",
            "intuitive": "insights, synthesis, and holistic understanding",
            "cosmic": "universal principles and transcendent awareness"
        }
        return focuses.get(level, "unknown aspects")
    
    def _interpret_phi_resonance(self, resonance: float) -> str:
        """Interpret phi resonance value."""
        if resonance > 0.9:
            return "exceptionally strong, indicating natural alignment with golden ratio patterns"
        elif resonance > 0.8:
            return "very strong, showing clear phi-harmonic structures"
        elif resonance > 0.7:
            return "strong, with significant phi-harmonic elements"
        elif resonance > 0.6:
            return "moderate, with some phi-harmonic patterns present"
        elif resonance > 0.5:
            return "modest, with occasional phi-harmonic elements"
        else:
            return "relatively weak in terms of phi-harmonic resonance"
    
    def _interpret_phi_alignment(self, alignment: float) -> str:
        """Interpret phi alignment value."""
        if alignment > 0.9:
            return "exceptional structural alignment with golden ratio proportions"
        elif alignment > 0.8:
            return "very strong structural alignment with phi-harmonic principles"
        elif alignment > 0.7:
            return "strong structural alignment with golden ratio patterns"
        elif alignment > 0.6:
            return "moderate structural alignment with phi-harmonic principles"
        elif alignment > 0.5:
            return "some structural alignment with golden ratio patterns"
        else:
            return "limited structural alignment with phi-harmonic principles"


def main():
    """Main function to demonstrate analyzer functionality."""
    # Create analyzer
    analyzer = QuantumPhiAnalyzer()
    
    # Sample texts
    samples = {
        "poe": """Once upon a midnight dreary, while I pondered, weak and weary,
Over many a quaint and curious volume of forgotten lore—
While I nodded, nearly napping, suddenly there came a tapping,
As of someone gently rapping, rapping at my chamber door.
"'Tis some visitor," I muttered, "tapping at my chamber door—
Only this and nothing more."
""",
        "hemingway": """He was an old man who fished alone in a skiff in the Gulf Stream and he had gone eighty-four days now without taking a fish. In the first forty days a boy had been with him. But after forty days without a fish the boy's parents had told him that the old man was now definitely and finally salao, which is the worst form of unlucky.""",
        "austen": """It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered the rightful property of some one or other of their daughters."""
    }
    
    # Analyze each sample
    for author, sample in samples.items():
        print(f"\nAnalyzing {author.title()} sample:")
        print("-" * 40)
        
        # Analyze the text
        analysis = analyzer.analyze_text(sample)
        
        # Print the report
        report = analyzer.generate_report(analysis)
        print(report)
        
        # Save report to file
        output_dir = "analysis_output"
        os.makedirs(output_dir, exist_ok=True)
        
        with open(f"{output_dir}/{author}_analysis.md", 'w') as f:
            f.write(report)
        
        print(f"\nReport saved to {output_dir}/{author}_analysis.md")
    
    # Compare two samples
    print("\nComparing Poe and Hemingway:")
    print("-" * 40)
    
    comparison = analyzer.compare_texts(samples["poe"], samples["hemingway"])
    
    print(f"Quantum Similarity: {comparison['quantum_similarity']:.4f}")
    print(f"Frequency Similarity: {comparison['frequency_similarity']:.4f}")
    print(f"Resonance Similarity: {comparison['resonance_similarity']:.4f}")
    print(f"Alignment Similarity: {comparison['alignment_similarity']:.4f}")


if __name__ == "__main__":
    main()
