#!/usr/bin/env python
"""
Test script for the Quantum Phi-Harmonic Language Generator.
Demonstrates pattern-based generation, consciousness levels,
and meta-learning capabilities.
"""

from quantum_phi_core import QuantumPhiCore
from quantum_phi_language_generator import QuantumPhiLanguageGenerator
from quantum_phi_frequency_processor import QuantumPhiFrequencyProcessor

def print_section(title: str) -> None:
    """Print a section header."""
    print("\n" + "="*70)
    print(title)
    print("="*70 + "\n")

def analyze_text(processor: QuantumPhiFrequencyProcessor, text: str) -> None:
    """Analyze and print text metrics."""
    metrics = processor.analyze_frequency_pattern(text)
    print(f"Text: '{text}'")
    print(f"Length: {len(text)}")
    print(f"Resonance: {metrics['resonance']:.4f}")
    print(f"Quantum Resonance: {metrics['quantum_resonance']:.4f}")
    print(f"Neural Resonance: {metrics['neural_resonance']:.4f}")
    print(f"Phi Alignment: {metrics['phi_alignment']:.4f}")
    print(f"Average Frequency: {metrics['average_frequency']:.4f} Hz")
    print()

def main():
    """Run language generator tests."""
    # Initialize components
    core = QuantumPhiCore()
    generator = QuantumPhiLanguageGenerator(core=core)
    processor = QuantumPhiFrequencyProcessor(core=core)
    
    print_section("Quantum Phi-Harmonic Language Generator Test")
    
    # Test consciousness levels
    print_section("Consciousness-Level Generation")
    
    base_text = "Quantum consciousness emerges through golden spirals of phi"
    
    for level in ['physical', 'emotional', 'mental', 'intuitive', 'cosmic']:
        print(f"\n{level.title()} Consciousness:")
        generated = generator.generate_with_consciousness(
            base_text, level, length=50, add_punctuation=True
        )
        analyze_text(processor, generated)
        
        # Print consciousness band metrics
        band = generator.consciousness_levels[level]['band']
        print(f"Consciousness Band:")
        print(f"Base: {band['base']:.6f}")
        print(f"Resonance: {band['resonance']:.6f}")
        print(f"Harmony: {band['harmony']:.6f}\n")
    
    # Test irrational punctuation
    print_section("Irrational Punctuation Patterns")
    
    # Test with phi decimals (space)
    freqs = [float(processor.letter_frequencies['a']) + 0.618034]
    text = generator.generate_from_frequencies(freqs)
    print("Phi (0.618034) -> Space:")
    print(f"Generated: '{text}'\n")
    
    # Test with pi decimals (comma)
    freqs = [float(processor.letter_frequencies['b']) + 0.141593]
    text = generator.generate_from_frequencies(freqs)
    print("Pi (0.141593) -> Comma:")
    print(f"Generated: '{text}'\n")
    
    # Test with e decimals (period)
    freqs = [float(processor.letter_frequencies['c']) + 0.718282]
    text = generator.generate_from_frequencies(freqs)
    print("e (0.718282) -> Period:")
    print(f"Generated: '{text}'\n")
    
    # Test quantum states
    print_section("Quantum State Frequencies")
    
    for state, freq in generator.quantum_states.items():
        print(f"{state.title()}: {freq:.6f} Hz")
    
    # Test meta-learning with consciousness
    print_section("Meta-Learning with Consciousness")
    
    sources = [
        "Quantum fields resonate with cosmic frequencies",
        "Neural patterns emerge in golden spirals",
        "Consciousness flows through harmonic waves"
    ]
    
    # Generate with phi-weighted sources
    weights = [float(core.phi_power(i)) for i in range(len(sources))]
    weights = [float(w) / sum(weights) for w in weights]
    
    print("Phi-Weighted Meta-Learning:")
    for level in ['physical', 'emotional', 'mental', 'intuitive', 'cosmic']:
        print(f"\n{level.title()} Consciousness:")
        text = ""
        for source, weight in zip(sources, weights):
            # Generate text with consciousness
            generated = generator.generate_with_consciousness(
                source, level, length=30, add_punctuation=True
            )
            # Apply phi-weighted combination
            text += generator.generate_from_frequencies(
                [float(processor.letter_frequencies[c]) * weight 
                 for c in generated if c in processor.letter_frequencies]
            )
        analyze_text(processor, text)
    
    print("\n======================================================================")
    print("Author Pattern Tests")
    print("======================================================================\n")

    # Test author patterns
    results = generator.test_author_patterns()

    for author, data in results.items():
        print(f"\n{author.title()} Pattern:")
        print(f"Text: '{data['text']}'")
        print(f"Length: {data['length']}")
        print(f"Resonance: {data['resonance']:.4f}")
        print(f"Average Frequency: {data['avg_frequency']:.4f} Hz")
        print(f"Frequency Modulation: {data['frequency_mod']:.4f}")
        print("\nPhi-Harmonic Analysis:")
        
        # Calculate phi-harmonic metrics
        base_freq = 439.2196  # From frequency analysis doc
        phi = float(generator.core.PHI)
        
        print(f"Base Frequency: {base_freq:.4f} Hz")
        print(f"Phi¹ Band: {base_freq * phi:.4f} Hz")
        print(f"Phi² Band: {base_freq * phi**2:.4f} Hz")
        print(f"Phi³ Band: {base_freq * phi**3:.4f} Hz")
        print(f"Phi⁻¹ Band: {base_freq / phi:.4f} Hz")
        print(f"Phi⁻² Band: {base_freq / phi**2:.4f} Hz")
        print(f"Phi⁻³ Band: {base_freq / phi**3:.4f} Hz")
        
        # Get resonance patterns from generator
        resonance = generator.resonance_patterns[author] if author in generator.resonance_patterns else generator.resonance_patterns['mental']
        
        print("\nResonance Patterns:")
        print(f"Subharmonic: {resonance['subharmonic']:.4f}")
        print(f"Quantum Resonance: {resonance['quantum']:.4f}")
        print(f"Coherence: {resonance['coherence']:.4f}")
        print(f"Harmony: {resonance['harmony']:.4f}")
        print(f"Phi Alignment: {resonance['phi_alignment']:.4f}")
    
    print("\n======================================================================")
    print("Meta-Learning with Author Patterns")
    print("======================================================================\n")

    # Test meta-learning with all authors
    sources = [pattern['pattern'] for pattern in generator.author_patterns.values()]
    meta_text = generator.generate_with_meta_learning(sources, length=90)

    print("Combined Author Patterns:")
    print(f"Text: '{meta_text}'")
    print(f"Length: {len(meta_text)}")

    # Calculate combined metrics
    freqs = []
    for c in meta_text:
        if c in generator.frequency_processor.letter_frequencies:
            freq = float(generator.frequency_processor.letter_frequencies[c])
            freqs.append(freq)

    if freqs:
        avg_freq = sum(freqs) / len(freqs)
        print(f"Average Frequency: {avg_freq:.4f} Hz")
        print(f"Frequency Range: ({min(freqs):.4f}, {max(freqs):.4f})")
        print(f"Phi-Harmonic Balance: {abs(avg_freq - base_freq * phi) / base_freq:.4f}")
    
    # Print generator metrics
    print_section("Generator Metrics")
    metrics = generator.get_metrics()
    print("Pattern Windows:", metrics['pattern_windows'])
    print("Consciousness Levels:", metrics['consciousness_levels'])
    print("Frequency Range:", metrics['frequency_range'])

if __name__ == "__main__":
    main()
