"""
Test script for the Quantum Phi-Harmonic Pattern Analyzer
"""

from quantum_phi_core import QuantumPhiCore
from quantum_phi_pattern_analyzer import QuantumPhiPatternAnalyzer

def print_resonance_profile(title: str, profile: dict):
    """Print resonance profile in a formatted way."""
    print(f"\n{title}")
    print("=" * len(title))
    print(f"Consciousness Level: {profile['consciousness_level'].title()}")
    print(f"Resonance Quality: {profile['resonance_quality']:.4f}")
    print(f"Quantum Resonance: {profile['quantum_resonance']:.4f}")
    print(f"Phi Alignment: {profile['phi_alignment']:.4f}")
    
    print("\nFrequency Statistics:")
    print(f"Mean: {profile['frequency_stats']['mean']:.4f} Hz")
    print(f"Std: {profile['frequency_stats']['std']:.4f} Hz")
    print(f"Range: {profile['frequency_stats']['min']:.4f} - {profile['frequency_stats']['max']:.4f} Hz")
    
    print("\nRecurring Patterns:")
    print(f"Top Bigrams: {', '.join(profile['patterns']['bigrams'])}")
    print(f"Top Trigrams: {', '.join(profile['patterns']['trigrams'])}")

def print_comparison(title: str, comparison: dict):
    """Print comparison results in a formatted way."""
    print(f"\n{title}")
    print("=" * len(title))
    print(f"Frequency Similarity: {comparison['frequency_similarity']:.4f}")
    print(f"Pattern Similarity: {comparison['pattern_similarity']:.4f}")
    print(f"Resonance Similarity: {comparison['resonance_similarity']:.4f}")
    print(f"Overall Similarity: {comparison['overall_similarity']:.4f}")

def main():
    """Main test function."""
    print("\n" + "=" * 70)
    print("Quantum Phi-Harmonic Pattern Analyzer Test")
    print("=" * 70)
    
    # Initialize analyzer
    core = QuantumPhiCore()
    analyzer = QuantumPhiPatternAnalyzer(core)
    
    # Test texts from different authors
    shakespeare = """
    To be, or not to be, that is the question:
    Whether 'tis nobler in the mind to suffer
    The slings and arrows of outrageous fortune,
    Or to take Arms against a Sea of troubles,
    And by opposing end them.
    """
    
    einstein = """
    The most beautiful thing we can experience is the mysterious. 
    It is the source of all true art and science. 
    He to whom the emotion is a stranger, 
    who can no longer pause to wonder and stand wrapped in awe, 
    is as good as dead.
    """
    
    austen = """
    It is a truth universally acknowledged, that a single man 
    in possession of a good fortune, must be in want of a wife.
    However little known the feelings or views of such a man may be 
    on his first entering a neighbourhood.
    """
    
    poe = """
    Once upon a midnight dreary, while I pondered, weak and weary,
    Over many a quaint and curious volume of forgotten lore—
    While I nodded, nearly napping, suddenly there came a tapping,
    As of someone gently rapping, rapping at my chamber door.
    "'Tis some visitor," I muttered, "tapping at my chamber door—
    Only this and nothing more."
    """
    
    # Analyze individual texts
    print("\nAnalyzing Author Patterns...")
    shakespeare_profile = analyzer.get_resonance_profile(shakespeare)
    einstein_profile = analyzer.get_resonance_profile(einstein)
    austen_profile = analyzer.get_resonance_profile(austen)
    poe_profile = analyzer.get_resonance_profile(poe)
    
    print_resonance_profile("Shakespeare's Pattern", shakespeare_profile)
    print_resonance_profile("Einstein's Pattern", einstein_profile)
    print_resonance_profile("Austen's Pattern", austen_profile)
    print_resonance_profile("Poe's Pattern", poe_profile)
    
    # Compare patterns
    print("\nComparing Author Patterns...")
    se_comparison = analyzer.compare_texts(shakespeare, einstein)
    sa_comparison = analyzer.compare_texts(shakespeare, austen)
    ea_comparison = analyzer.compare_texts(einstein, austen)
    
    # Add Poe comparisons
    sp_comparison = analyzer.compare_texts(shakespeare, poe)
    ep_comparison = analyzer.compare_texts(einstein, poe)
    ap_comparison = analyzer.compare_texts(austen, poe)
    
    print_comparison("Shakespeare vs Einstein", se_comparison)
    print_comparison("Shakespeare vs Austen", sa_comparison)
    print_comparison("Einstein vs Austen", ea_comparison)
    print_comparison("Shakespeare vs Poe", sp_comparison)
    print_comparison("Einstein vs Poe", ep_comparison)
    print_comparison("Austen vs Poe", ap_comparison)
    
    # Test quantum bands
    print("\nQuantum Frequency Bands:")
    print("-" * 30)
    for band, freq in analyzer.quantum_bands.items():
        print(f"{band.title()}: {freq:.4f} Hz")
    
    print("\nPhi-Harmonic Bands:")
    print("-" * 30)
    for band, freq in analyzer.phi_bands.items():
        print(f"{band}: {freq:.4f} Hz")

if __name__ == "__main__":
    main()
