"""
Test script for validating Quantum Language Processor V1 with real-world data.
"""

import numpy as np
from typing import Dict, List, Any, Tuple

from extensions.quantum_analysis.quantum_language_processor_v1 import QuantumLanguageProcessorV1

def test_text_processing(processor: QuantumLanguageProcessorV1,
                        text: str,
                        context: Dict[str, Any]) -> Dict[str, Any]:
    """Test text processing with quantum enhancement."""
    print("\nProcessing Text:")
    print("-" * 40)
    print(f"Input: {text}")
    print(f"Context: {context}")
    
    # Process text
    result = processor.process_text(
        text=text,
        context=context
    )
    
    print("\nResults:")
    print(f"Coherence: {result['coherence']:.6f}")
    print(f"Stability: {result['stability']:.6f}")
    print(f"Evolution: {result['evolution']:.6f}")
    print("\nFeatures:")
    for key, value in result['features'].items():
        print(f"{key}: {value:.6f}")
    
    return result

def test_text_generation(processor: QuantumLanguageProcessorV1,
                        features: Dict[str, Any],
                        context: Dict[str, Any]) -> str:
    """Test text generation with quantum enhancement."""
    print("\nGenerating Text:")
    print("-" * 40)
    print("Input Features:")
    for key, value in features.items():
        print(f"{key}: {value:.6f}")
    print(f"Context: {context}")
    
    # Generate text
    text = processor.generate_text(
        features=features,
        context=context
    )
    
    print("\nGenerated Text:")
    print(text)
    
    return text

def main():
    print("\n" + "=" * 80)
    print("QUANTUM LANGUAGE PROCESSOR V1 TEST")
    print("=" * 80 + "\n")
    
    # Initialize processor
    processor = QuantumLanguageProcessorV1()
    
    # Test data
    test_texts = [
        "The quantum system processes information using phi-harmonic principles.",
        "Neural networks enhance pattern recognition through deep learning.",
        "Language models understand context and generate coherent responses.",
        "Temporal bridges connect quantum states across multiple dimensions.",
        "Self-validation ensures robust and adaptive processing capabilities."
    ]
    
    test_contexts = [
        {
            'relevance': 0.95,
            'importance': 0.85,
            'complexity': 0.75
        },
        {
            'relevance': 0.85,
            'importance': 0.95,
            'complexity': 0.65
        },
        {
            'relevance': 0.75,
            'importance': 0.85,
            'complexity': 0.95
        }
    ]
    
    print("Testing Text Processing...")
    print("-" * 40 + "\n")
    
    processing_results = []
    for text in test_texts:
        for context in test_contexts:
            result = test_text_processing(
                processor=processor,
                text=text,
                context=context
            )
            processing_results.append(result)
    
    print("\nProcessing Metrics:")
    print("-" * 40)
    
    avg_coherence = np.mean([r['coherence'] for r in processing_results])
    avg_stability = np.mean([r['stability'] for r in processing_results])
    avg_evolution = np.mean([r['evolution'] for r in processing_results])
    
    print(f"Average Coherence: {avg_coherence:.6f}")
    print(f"Average Stability: {avg_stability:.6f}")
    print(f"Average Evolution: {avg_evolution:.6f}")
    
    print("\nTesting Text Generation...")
    print("-" * 40 + "\n")
    
    # Generate text from processed features
    for result in processing_results[:3]:  # Test first 3 results
        generated_text = test_text_generation(
            processor=processor,
            features=result['features'],
            context=result['pattern']['context']
        )
    
    print("\n" + "=" * 80)
    print("TEST COMPLETED")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    main()
