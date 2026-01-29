"""
Test script for Edgar Allan Poe's Quantum Phi-Harmonic Language Patterns
"""

from quantum_phi_core import QuantumPhiCore
from quantum_phi_language_generator import QuantumPhiLanguageGenerator
from quantum_phi_pattern_analyzer import QuantumPhiPatternAnalyzer
import numpy as np
import matplotlib.pyplot as plt

def print_section_header(title):
    """Print formatted section header."""
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70 + "\n")

def print_text_analysis(title, text, metrics):
    """Print text with analysis metrics."""
    print(f"\n{title}:")
    print(f"Text: '{text}'")
    print(f"Length: {len(text)}")
    print(f"Resonance: {metrics['resonance']:.4f}")
    print(f"Quantum Resonance: {metrics['quantum_resonance']:.4f}")
    print(f"Phi Alignment: {metrics['phi_alignment']:.4f}")
    print(f"Consciousness Level: {metrics['consciousness_level'].title()}")
    print(f"Average Frequency: {metrics['avg_frequency']:.4f} Hz")
    print(f"Frequency Range: {metrics['frequency_range'][0]:.4f} - {metrics['frequency_range'][1]:.4f} Hz")
    
    print("\nRecurring Patterns:")
    print(f"Top Bigrams: {', '.join(metrics['top_bigrams'])}")
    print(f"Top Trigrams: {', '.join(metrics['top_trigrams'])}")

def generate_poe_variations(generator, analyzer, length=100, variations=5):
    """Generate and analyze variations of Poe's language patterns."""
    results = []
    
    # Generate multiple variations
    for i in range(variations):
        # Generate text with Poe's pattern
        text = generator.generate_with_author_pattern("poe", length)
        
        # Analyze the generated text
        metrics = analyzer.analyze_text(text)
        
        results.append({
            "text": text,
            "metrics": metrics,
            "variation": i+1
        })
    
    return results

def compare_with_original_poe(analyzer):
    """Compare generated text with original Poe text."""
    original_poe = """
    Once upon a midnight dreary, while I pondered, weak and weary,
    Over many a quaint and curious volume of forgotten lore—
    While I nodded, nearly napping, suddenly there came a tapping,
    As of someone gently rapping, rapping at my chamber door.
    "'Tis some visitor," I muttered, "tapping at my chamber door—
    Only this and nothing more."
    """
    
    # Analyze original Poe text
    original_metrics = analyzer.analyze_text(original_poe)
    
    return original_poe, original_metrics

def generate_poe_consciousness_levels(generator, analyzer):
    """Generate Poe-style text at different consciousness levels."""
    consciousness_levels = ["physical", "emotional", "mental", "intuitive", "cosmic"]
    results = []
    
    for level in consciousness_levels:
        # Generate text with Poe's pattern at specific consciousness level
        # We'll modify the frequency to match the consciousness level
        base_freq = 439.2196  # Base frequency
        
        if level == "physical":
            freq_mod = 0.5  # Lower frequency
        elif level == "emotional":
            freq_mod = 0.75
        elif level == "mental":
            freq_mod = 1.0  # Base frequency
        elif level == "intuitive":
            freq_mod = 1.5
        else:  # cosmic
            freq_mod = 2.0  # Higher frequency
        
        # Generate text with Poe's pattern but modified frequency
        text = generator.generate_with_author_pattern("poe", 100)
        
        # Analyze the generated text
        metrics = analyzer.analyze_text(text)
        
        results.append({
            "level": level,
            "text": text,
            "metrics": metrics
        })
    
    return results

def main():
    """Main test function."""
    print_section_header("Edgar Allan Poe Quantum Phi-Harmonic Language Test")
    
    # Initialize core components
    core = QuantumPhiCore()
    generator = QuantumPhiLanguageGenerator(core=core)
    analyzer = QuantumPhiPatternAnalyzer(core=core)
    
    # Test 1: Generate basic Poe-style text
    print_section_header("Basic Poe-Style Generation")
    poe_text = generator.generate_with_author_pattern("poe", 100)
    poe_metrics = analyzer.analyze_text(poe_text)
    print_text_analysis("Poe-Style Text", poe_text, poe_metrics)
    
    # Test 2: Compare with original Poe
    print_section_header("Comparison with Original Poe")
    original_text, original_metrics = compare_with_original_poe(analyzer)
    print_text_analysis("Original Poe", original_text, original_metrics)
    
    # Calculate similarity
    comparison = analyzer.compare_texts(poe_text, original_text)
    print("\nSimilarity Metrics:")
    print(f"Frequency Similarity: {comparison['frequency_similarity']:.4f}")
    print(f"Pattern Similarity: {comparison['pattern_similarity']:.4f}")
    print(f"Resonance Similarity: {comparison['resonance_similarity']:.4f}")
    print(f"Overall Similarity: {comparison['overall_similarity']:.4f}")
    
    # Test 3: Generate variations
    print_section_header("Poe Pattern Variations")
    variations = generate_poe_variations(generator, analyzer, length=75, variations=3)
    
    for var in variations:
        print_text_analysis(f"Variation {var['variation']}", var['text'], var['metrics'])
    
    # Test 4: Consciousness levels
    print_section_header("Poe at Different Consciousness Levels")
    consciousness_results = generate_poe_consciousness_levels(generator, analyzer)
    
    for result in consciousness_results:
        print_text_analysis(f"{result['level'].title()} Consciousness", result['text'], result['metrics'])
    
    # Test 5: Compare with other authors
    print_section_header("Poe vs. Other Authors")
    
    # Generate text for each author
    shakespeare_text = generator.generate_with_author_pattern("shakespeare", 100)
    einstein_text = generator.generate_with_author_pattern("einstein", 100)
    austen_text = generator.generate_with_author_pattern("austen", 100)
    
    # Compare Poe with other authors
    ps_comparison = analyzer.compare_texts(poe_text, shakespeare_text)
    pe_comparison = analyzer.compare_texts(poe_text, einstein_text)
    pa_comparison = analyzer.compare_texts(poe_text, austen_text)
    
    print("\nPoe vs. Shakespeare:")
    print(f"Overall Similarity: {ps_comparison['overall_similarity']:.4f}")
    
    print("\nPoe vs. Einstein:")
    print(f"Overall Similarity: {pe_comparison['overall_similarity']:.4f}")
    
    print("\nPoe vs. Austen:")
    print(f"Overall Similarity: {pa_comparison['overall_similarity']:.4f}")
    
    print_section_header("Quantum Phi-Harmonic Metrics")
    print(f"Phi Value: {float(core.PHI):.6f}")
    print(f"Poe's Resonance: {poe_metrics['resonance']:.4f}")
    print(f"Poe's Quantum Resonance: {poe_metrics['quantum_resonance']:.4f}")
    print(f"Poe's Phi Alignment: {poe_metrics['phi_alignment']:.4f}")

if __name__ == "__main__":
    main()
