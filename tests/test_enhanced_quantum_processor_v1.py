"""
Test Enhanced Quantum Processor V1.
Tests quantum-enhanced processing with real-world examples.
"""

from extensions.quantum_analysis.enhanced_quantum_processor_v1 import EnhancedQuantumProcessorV1

def test_quantum_processing():
    """Test quantum-enhanced processing."""
    print("\nTesting Enhanced Quantum Processing")
    print("=" * 50)
    
    # Initialize processor
    processor = EnhancedQuantumProcessorV1()
    
    # Test data
    test_data = {
        'type': 'quantum_input',
        'content': 'quantum neural architecture with self-evolution',
        'features': {
            'complexity': 0.85,
            'innovation': 0.90,
            'coherence': 0.95,
            'stability': 0.80,
            'evolution': 0.90,
            'learning': 0.85
        },
        'patterns': [
            {'type': 'neural', 'weight': 0.95},
            {'type': 'quantum', 'weight': 0.90},
            {'type': 'evolution', 'weight': 0.85}
        ]
    }
    
    # Process quantum data
    print("\nProcessing Quantum Data:")
    print("-" * 40)
    results = processor.process_quantum_data(test_data)
    
    # Print feature results
    print("\nFeature Results:")
    print("-" * 40)
    for feature_type, values in results['features'].items():
        print(f"{feature_type}:")
        print(f"  Values: {[f'{v:.6f}' for v in values]}")
    
    # Print pattern results
    print("\nPattern Results:")
    print("-" * 40)
    for pattern_type, values in results['patterns'].items():
        print(f"{pattern_type}:")
        print(f"  Values: {[f'{v:.6f}' for v in values]}")
    
    # Print metrics
    print("\nMetrics:")
    print("-" * 40)
    for metric, value in results['metrics'].items():
        print(f"{metric}: {value:.6f}")
    
    # Print learning progress
    print("\nLearning Progress:")
    print("-" * 40)
    print(f"Progress: {results['learning_progress']:.6f}")
    
    return results

if __name__ == '__main__':
    results = test_quantum_processing()
    
    print("\nTest Summary")
    print("=" * 50)
    print(f"Coherence: {results['metrics']['coherence']:.6f}")
    print(f"Stability: {results['metrics']['stability']:.6f}")
    print(f"Evolution: {results['metrics']['evolution']:.6f}")
    print(f"Learning Progress: {results['learning_progress']:.6f}")
