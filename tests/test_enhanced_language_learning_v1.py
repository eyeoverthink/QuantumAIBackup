"""
Test script for Enhanced Language Learning V1 with practical examples.
"""

import numpy as np
from typing import Dict, List, Any

from extensions.quantum_analysis.enhanced_language_learning_v1 import EnhancedLanguageLearningV1

def test_practical_processing(processor: EnhancedLanguageLearningV1,
                            examples: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Test practical language processing examples."""
    results = []
    
    print("\nTesting Practical Processing")
    print("=" * 50)
    
    for example in examples:
        print(f"\nProcessing Example: {example['type']}")
        print("-" * 40)
        print(f"Input: {example['text']}")
        print(f"Context: {example['context']}")
        
        # Process input
        result = processor.process_input(
            text=example['text'],
            context=example['context']
        )
        
        print("\nResults:")
        print(f"Coherence: {result['coherence']:.6f}")
        print(f"Stability: {result['stability']:.6f}")
        print(f"Evolution: {result['evolution']:.6f}")
        print("\nFeatures:")
        for key, value in result['features'].items():
            print(f"{key}: {value:.6f}")
        
        results.append(result)
    
    return results

def test_practical_generation(processor: EnhancedLanguageLearningV1,
                            results: List[Dict[str, Any]]) -> List[str]:
    """Test practical language generation from processed results."""
    responses = []
    
    print("\nTesting Practical Generation")
    print("=" * 50)
    
    for result in results:
        print("\nGenerating Response")
        print("-" * 40)
        print("Input Features:")
        for key, value in result['features'].items():
            print(f"{key}: {value:.6f}")
        
        # Extract context from state
        context = {
            'relevance': result['state']['semantic_coherence'] / processor.phi,
            'importance': result['state']['temporal_stability'] * processor.phi,
            'complexity': result['state']['pattern_evolution'] / processor.phi
        }
        
        # Generate response
        response = processor.generate_response(
            features=result['features'],
            context=context
        )
        
        print("\nGenerated Response:")
        print(response)
        
        responses.append(response)
    
    return responses

def main():
    # Initialize processor
    processor = EnhancedLanguageLearningV1()
    
    # Practical test examples
    examples = [
        {
            'type': 'Pattern Recognition',
            'text': "The system detected recurring patterns in user behavior and engagement metrics.",
            'context': {
                'relevance': 0.95,
                'importance': 0.90,
                'complexity': 0.85
            }
        },
        {
            'type': 'User Intent',
            'text': "User searches for product recommendations based on previous purchases.",
            'context': {
                'relevance': 0.90,
                'importance': 0.85,
                'complexity': 0.75
            }
        },
        {
            'type': 'Semantic Analysis',
            'text': "Analyzing customer feedback to identify key sentiment patterns and trends.",
            'context': {
                'relevance': 0.85,
                'importance': 0.95,
                'complexity': 0.80
            }
        },
        {
            'type': 'Learning Progress',
            'text': "System adapts response patterns based on user interaction history.",
            'context': {
                'relevance': 0.95,
                'importance': 0.90,
                'complexity': 0.85
            }
        },
        {
            'type': 'Feature Extraction',
            'text': "Extracting key features from user profiles for personalized recommendations.",
            'context': {
                'relevance': 0.90,
                'importance': 0.85,
                'complexity': 0.80
            }
        }
    ]
    
    # Test processing
    print("\nTesting Enhanced Language Learning V1")
    print("=" * 80)
    
    results = test_practical_processing(
        processor=processor,
        examples=examples
    )
    
    # Test generation
    responses = test_practical_generation(
        processor=processor,
        results=results
    )
    
    # Calculate metrics
    avg_coherence = np.mean([r['coherence'] for r in results])
    avg_stability = np.mean([r['stability'] for r in results])
    avg_evolution = np.mean([r['evolution'] for r in results])
    avg_learning = np.mean([r['features']['learning_progress'] for r in results])
    
    print("\nOverall Metrics")
    print("=" * 50)
    print(f"Average Coherence: {avg_coherence:.6f}")
    print(f"Average Stability: {avg_stability:.6f}")
    print(f"Average Evolution: {avg_evolution:.6f}")
    print(f"Average Learning Progress: {avg_learning:.6f}")

if __name__ == "__main__":
    main()
