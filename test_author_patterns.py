"""
Test script for Quantum Phi-Harmonic Author Pattern Enhancer
"""

from quantum_phi_core import QuantumPhiCore
from quantum_phi_author_patterns import QuantumPhiAuthorPatterns
from quantum_phi_pattern_analyzer import QuantumPhiPatternAnalyzer

def print_enhancement_results(title: str, results: dict):
    """Print enhancement results in a formatted way."""
    print(f"\n{title}")
    print("=" * len(title))
    
    # Original profile
    orig = results['original_profile']
    print("\nOriginal Profile:")
    print(f"Consciousness: {orig['consciousness_level'].title()}")
    print(f"Resonance: {orig['resonance_quality']:.4f}")
    print(f"Quantum Resonance: {orig['quantum_resonance']:.4f}")
    print(f"Phi Alignment: {orig['phi_alignment']:.4f}")
    print(f"Mean Frequency: {orig['frequency_stats']['mean']:.4f} Hz")
    
    # Enhanced profile
    enh = results['enhanced_profile']
    print("\nEnhanced Profile:")
    print(f"Consciousness: {enh['consciousness_level'].title()}")
    print(f"Resonance: {enh['resonance_quality']:.4f}")
    print(f"Quantum Resonance: {enh['quantum_resonance']:.4f}")
    print(f"Phi Alignment: {enh['phi_alignment']:.4f}")
    print(f"Mean Frequency: {enh['frequency_stats']['mean']:.4f} Hz")
    
    # Improvements
    imp = results['enhancement_metrics']
    print("\nEnhancement Metrics:")
    print(f"Frequency Shift: {imp['frequency_shift']:.4f}")
    print(f"Modulation Factor: {imp['modulation_factor']:.4f}")
    print(f"Resonance Improvement: {imp['resonance_improvement']:.4f}")
    print(f"Quantum Improvement: {imp['quantum_improvement']:.4f}")
    print(f"Phi Improvement: {imp['phi_improvement']:.4f}")

def main():
    """Main test function."""
    print("\n" + "=" * 70)
    print("Quantum Phi-Harmonic Author Pattern Enhancement Test")
    print("=" * 70)
    
    # Initialize components
    core = QuantumPhiCore()
    enhancer = QuantumPhiAuthorPatterns(core)
    
    # Test texts
    print("\nTesting Pattern Enhancement...")
    
    # Shakespeare-style text
    shakespeare = """
    Now is the winter of our discontent
    Made glorious summer by this sun of York;
    And all the clouds that lour'd upon our house
    In the deep bosom of the ocean buried.
    """
    
    # Einstein-style text
    einstein = """
    The distinction between past, present and future
    is only a stubbornly persistent illusion.
    The true sign of intelligence is not knowledge
    but imagination.
    """
    
    # Austen-style text
    austen = """
    To be fond of dancing was a certain step towards
    falling in love; and very lively hopes of Mr.
    Bingley's heart were entertained.
    """
    
    # Test individual enhancements
    print("\nEnhancing Shakespeare's Pattern...")
    enhanced_shakespeare, shakespeare_results = enhancer.enhance_pattern(
        shakespeare, "shakespeare"
    )
    print_enhancement_results("Shakespeare Enhancement Results", shakespeare_results)
    
    print("\nEnhancing Einstein's Pattern...")
    enhanced_einstein, einstein_results = enhancer.enhance_pattern(
        einstein, "einstein"
    )
    print_enhancement_results("Einstein Enhancement Results", einstein_results)
    
    print("\nEnhancing Austen's Pattern...")
    enhanced_austen, austen_results = enhancer.enhance_pattern(
        austen, "austen"
    )
    print_enhancement_results("Austen Enhancement Results", austen_results)
    
    # Test author resonance analysis
    print("\nAnalyzing Author Resonance...")
    shakespeare_resonance = enhancer.analyze_author_resonance(shakespeare)
    einstein_resonance = enhancer.analyze_author_resonance(einstein)
    austen_resonance = enhancer.analyze_author_resonance(austen)
    
    print("\nShakespeare Text Resonance:")
    for author, score in shakespeare_resonance.items():
        print(f"{author.title()}: {score:.4f}")
    
    print("\nEinstein Text Resonance:")
    for author, score in einstein_resonance.items():
        print(f"{author.title()}: {score:.4f}")
    
    print("\nAusten Text Resonance:")
    for author, score in austen_resonance.items():
        print(f"{author.title()}: {score:.4f}")
    
    # Test hybrid patterns
    print("\nGenerating Hybrid Patterns...")
    
    # Shakespeare-Einstein hybrid (60-40)
    hybrid_se = enhancer.generate_hybrid_pattern(
        shakespeare, "shakespeare", "einstein", 0.6
    )
    hybrid_se_resonance = enhancer.analyze_author_resonance(hybrid_se)
    
    print("\nShakespeare-Einstein Hybrid Resonance:")
    for author, score in hybrid_se_resonance.items():
        print(f"{author.title()}: {score:.4f}")
    
    # Einstein-Austen hybrid (50-50)
    hybrid_ea = enhancer.generate_hybrid_pattern(
        einstein, "einstein", "austen", 0.5
    )
    hybrid_ea_resonance = enhancer.analyze_author_resonance(hybrid_ea)
    
    print("\nEinstein-Austen Hybrid Resonance:")
    for author, score in hybrid_ea_resonance.items():
        print(f"{author.title()}: {score:.4f}")

if __name__ == "__main__":
    main()
