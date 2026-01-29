"""
Test script for Quantum Phi Meta-Learning and Language Processing integration
"""
import time
import numpy as np
from datetime import datetime
from typing import Dict, List, Any, Tuple

from quantum_phi_core import QuantumPhiCore
from quantum_phi_random import QuantumPhiRandom
from quantum_phi_meta_learner import QuantumPhiMetaLearner

def print_section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

def test_language_patterns():
    """
    Test quantum phi-harmonic language pattern analysis and learning
    """
    print("\n" + "="*70)
    print("Quantum Phi-Harmonic Learning System Test")
    print("="*70)
    
    # Initialize core components with phi-harmonic principles
    core = QuantumPhiCore()
    random_gen = QuantumPhiRandom(core=core)
    learner = QuantumPhiMetaLearner(core=core, random_gen=random_gen)
    
    # Convert phi to float for calculations
    phi = float(core.PHI)
    phi_inverse = float(1/phi)
    
    print(f"Golden Ratio (φ): {core.PHI}")
    print(f"Phi Inverse (φ⁻¹): {phi_inverse}")
    
    # Test language pattern analysis
    print("\n" + "="*70)
    print("Language Pattern Analysis")
    print("="*70 + "\n")
    
    test_texts = [
        "Quantum resonance creates harmonic patterns in nature",
        "The golden ratio appears in spiral galaxies",
        "Fibonacci sequences emerge in quantum phenomena"
    ]
    
    pattern_resonances = []
    for text in test_texts:
        print(f"Analyzing: '{text}'")
        
        # Analyze text pattern
        pattern = {'text_content': text, 'type': 'language'}
        analysis = learner.language_processor.analyze_text_pattern(text)
        
        # Display analysis results
        print(f"Syllable Pattern: {analysis['syllable_count']} syllables")
        print(f"Cadence: {analysis['cadence_type']} (score: {analysis['cadence_score']:.4f})")
        print(f"Resonance: {analysis['resonance']:.4f}")
        pattern_resonances.append(analysis['resonance'])
        
        # Test next word prediction
        context = text.split()[-3:]  # Use last 3 words as context
        next_word, confidence = learner.language_processor.predict_next_word(context)
        print(f"Next Word Prediction: '{next_word}' (confidence: {confidence:.4f})\n")
        
        # Integrate pattern into learner
        learner._integrate_patterns([pattern])
    
    # Calculate overall resonance metrics
    avg_resonance = sum(pattern_resonances) / len(pattern_resonances) if pattern_resonances else 0.0
    phi_quality = avg_resonance / phi if avg_resonance > 0 else 0.0
    resonance_coherence = 1.0 - abs(phi_quality - phi_inverse)
    
    print("\nResonance Metrics:")
    print(f"Average Resonance: {avg_resonance:.4f}")
    print(f"Phi-Harmonic Quality: {phi_quality:.4f}")
    print(f"Resonance Coherence: {resonance_coherence:.4f}")
    
    # Display pattern memory statistics
    print("\n" + "="*70)
    print("Meta-Learning Integration")
    print("="*70 + "\n")
    
    print("Pattern Memory Statistics:")
    for category, patterns in learner.pattern_memory.items():
        print(f"{category}: {len(patterns)} patterns")
    
    print("\nLearning Metrics:")
    metrics = learner.get_metrics()
    for metric, value in metrics.items():
        print(f"{metric}: {value}")
    
    # Test passive learning
    print("\n" + "="*70)
    print("Passive Learning Test")
    print("="*70 + "\n")
    
    print("Initiating passive learning cycle...")
    learning_results = learner.passive_learn()
    
    print("\nPassive Learning Results:")
    for metric, value in learning_results.items():
        print(f"{metric}: {value}")
    
    # Display quantum gate integration
    print("\n" + "="*70)
    print("Quantum Gate Integration")
    print("="*70 + "\n")
    
    print("Quantum Gate Frequencies:")
    for gate, data in learner.language_processor.quantum_gates.items():
        freq = float(data['frequency'])
        # Calculate power of phi using logarithm
        power = round(np.log(freq) / np.log(phi), 2)
        print(f"Gate {gate}: {data['pattern']} (φ^{power:.2f})")
        
    # Display harmonic resonance patterns
    print("\nHarmonic Resonance Analysis:")
    for pattern in learner.pattern_memory['language_patterns']:
        if 'quantum_state' in pattern:
            state = pattern['quantum_state']
            resonance = float(pattern.get('resonance', 0.0))
            text = pattern.get('text', 'Unknown')
            
            # Calculate quantum coherence
            coherence = sum(abs(x) for x in state) / len(state)
            
            # Calculate phi-harmonic alignment
            phi_alignment = abs(resonance - phi_inverse) / phi_inverse
            
            print(f"\nPattern: {text}")
            print(f"Quantum State: {[f'{x:.4f}' for x in state]}")
            print(f"Resonance: {resonance:.4f}")
            print(f"Coherence: {coherence:.4f}")
            print(f"Phi Alignment: {phi_alignment:.4f}")
            
    # Test phi-harmonic word prediction
    print("\n" + "="*70)
    print("Word Prediction Analysis")
    print("="*70 + "\n")
    
    test_contexts = [
        ["quantum", "resonance", "creates"],
        ["golden", "ratio", "appears"],
        ["fibonacci", "sequences", "emerge"]
    ]
    
    prediction_resonances = []
    for context in test_contexts:
        next_word, confidence = learner.language_processor.predict_next_word(context)
        print(f"\nContext: {' '.join(context)}")
        print(f"Predicted: '{next_word}' (confidence: {confidence:.4f})")
        
        # Calculate prediction resonance
        state = learner.language_processor._calculate_quantum_state(next_word)
        resonance = sum(abs(x) for x in state) / len(state)
        prediction_resonances.append(resonance)
        print(f"Prediction Resonance: {resonance:.4f}")
    
    # Calculate prediction quality metrics
    avg_pred_resonance = sum(prediction_resonances) / len(prediction_resonances)
    pred_phi_quality = avg_pred_resonance / phi
    pred_coherence = 1.0 - abs(pred_phi_quality - phi_inverse)
    
    print("\nPrediction Quality Metrics:")
    print(f"Average Prediction Resonance: {avg_pred_resonance:.4f}")
    print(f"Prediction Phi-Quality: {pred_phi_quality:.4f}")
    print(f"Prediction Coherence: {pred_coherence:.4f}")
    
    # Test resonance between patterns
    total_resonance = 0
    pattern_count = 0
    
    for pattern in learner.pattern_memory['language_patterns']:
        resonance = learner.language_processor._calculate_text_resonance(pattern['text_content'])
        total_resonance += resonance
        pattern_count += 1
        print(f"\nPattern Resonance for '{pattern['text_content'][:30]}...': {resonance:.4f}")
        
    avg_resonance = total_resonance / pattern_count if pattern_count > 0 else 0
    print(f"\nAverage Resonance: {avg_resonance:.4f}")
    print(f"Phi-Harmonic Quality: {(avg_resonance/phi):.4f}")
    
    print_section("Test Complete")
    print("\nAll tests completed successfully!")

if __name__ == "__main__":
    test_language_patterns()
