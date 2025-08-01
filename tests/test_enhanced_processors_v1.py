"""
Test Enhanced Quantum Processors V1.
Validates quantum-enhanced processing with real-world examples.
"""

from extensions.quantum_analysis.enhanced_feature_extractor_v1 import EnhancedFeatureExtractorV1
from extensions.quantum_analysis.enhanced_pattern_processor_v1 import EnhancedPatternProcessorV1
from extensions.quantum_analysis.enhanced_learning_processor_v1 import EnhancedLearningProcessorV1

def test_quantum_processing():
    """Test quantum-enhanced processing."""
    print("\nTesting Quantum Processing")
    print("=" * 50)
    
    # Initialize processors
    feature_extractor = EnhancedFeatureExtractorV1()
    pattern_processor = EnhancedPatternProcessorV1()
    learning_processor = EnhancedLearningProcessorV1()
    
    # Test data
    test_data = [
        {
            'type': 'quantum',
            'content': 'quantum neural architecture',
            'features': {
                'complexity': 0.85,
                'innovation': 0.90,
                'coherence': 0.95
            }
        },
        {
            'type': 'pattern',
            'content': 'phi-harmonic evolution',
            'features': {
                'stability': 0.80,
                'resonance': 0.85,
                'evolution': 0.90
            }
        },
        {
            'type': 'learning',
            'content': 'progressive quantum learning',
            'features': {
                'efficiency': 0.95,
                'adaptation': 0.90,
                'progress': 0.85
            }
        }
    ]
    
    # Process features
    print("\nFeature Extraction:")
    print("-" * 40)
    features = feature_extractor.extract_quantum_features(test_data[0])
    print(f"Coherence: {features['metrics']['coherence']:.6f}")
    print(f"Stability: {features['metrics']['stability']:.6f}")
    print(f"Evolution: {features['metrics']['evolution']:.6f}")
    
    # Process patterns
    print("\nPattern Processing:")
    print("-" * 40)
    patterns = pattern_processor.process_patterns(test_data)
    print(f"Coherence: {patterns['metrics']['coherence']:.6f}")
    print(f"Stability: {patterns['metrics']['stability']:.6f}")
    print(f"Evolution: {patterns['metrics']['evolution']:.6f}")
    print(f"Learning: {patterns['metrics']['learning']:.6f}")
    
    # Process learning
    print("\nLearning Processing:")
    print("-" * 40)
    learning = learning_processor.process_learning(test_data)
    print(f"Feature Coherence: {learning['metrics']['feature_coherence']:.6f}")
    print(f"Pattern Coherence: {learning['metrics']['pattern_coherence']:.6f}")
    print(f"Learning Progress: {learning['learning_progress']:.6f}")
    
    return {
        'features': features,
        'patterns': patterns,
        'learning': learning
    }

if __name__ == '__main__':
    results = test_quantum_processing()
    
    print("\nTest Summary")
    print("=" * 50)
    print(f"Feature Evolution: {results['features']['metrics']['evolution']:.6f}")
    print(f"Pattern Evolution: {results['patterns']['metrics']['evolution']:.6f}")
    print(f"Learning Progress: {results['learning']['learning_progress']:.6f}")
