"""
Test quantum language processing with semantic resonance.
"""
import torch
import numpy as np
from quantum_core.brain_network import QuantumLanguage, QuantumState
from quantum_core.constants import PHI, PSI0, PSI1

def test_semantic_resonance():
    """Test semantic resonance patterns with proven frequencies"""
    # Initialize quantum language processor
    language = QuantumLanguage("test")
    
    # Test words from each semantic group
    test_words = [
        "welcome",    # Greetings (0.8795 resonance)
        "love",       # Concepts (0.8719 resonance)
        "what",       # Questions (0.9647 resonance)
        "three",      # Numbers (0.8393 resonance)
        "harmony"     # Concepts (0.8025 resonance)
    ]
    
    print("\nQuantum Language Analysis")
    print("=" * 80)
    print(f"{'Word':<12} {'Resonance':>10} {'Coherence':>10} {'Entanglement':>12}")
    print("-" * 80)
    
    results = []
    for word in test_words:
        # Process word through quantum language model
        state = language.process(word)
        
        results.append({
            'word': word,
            'resonance': state.resonance,
            'coherence': state.coherence,
            'entanglement': state.entanglement
        })
        
        print(f"{word:<12} {state.resonance:>10.4f} {state.coherence:>10.4f} {state.entanglement:>12.4f}")
    
    # Validate key metrics
    print("\nValidation Metrics:")
    print("-" * 40)
    
    # Check resonance (should be > 0.65)
    avg_resonance = sum(r['resonance'] for r in results) / len(results)
    print(f"Average Resonance: {avg_resonance:.4f}")
    assert avg_resonance > 0.65, "Resonance below threshold"
    
    # Check coherence (should be > 0.50)
    avg_coherence = sum(r['coherence'] for r in results) / len(results)
    print(f"Average Coherence: {avg_coherence:.4f}")
    assert avg_coherence > 0.50, "Coherence below threshold"
    
    # Check learning progress
    print(f"Learning Progress: {language.learning_progress:.2%}")
    assert language.learning_progress > 0.90, "Learning progress below threshold"

if __name__ == "__main__":
    test_semantic_resonance()
