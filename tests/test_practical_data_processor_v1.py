"""
Test practical data processing with real-world user scenarios.
"""

import numpy as np
from typing import Dict, List, Any

from extensions.quantum_analysis.practical_data_processor_v1 import PracticalDataProcessorV1

def test_user_behavior_analysis(processor: PracticalDataProcessorV1):
    """Test user behavior analysis with real data."""
    print("\nTesting User Behavior Analysis")
    print("=" * 50)
    
    # Sample user behaviors
    behaviors = [
        {
            'type': 'search',
            'content': 'quantum computing applications in machine learning',
            'timestamp': 1678987654,
            'session_duration': 450,
            'click_count': 8,
            'scroll_depth': 0.85,
            'tags': ['quantum', 'ml', 'computing']
        },
        {
            'type': 'interaction',
            'content': 'deep learning model optimization techniques',
            'timestamp': 1678987754,
            'session_duration': 380,
            'click_count': 6,
            'scroll_depth': 0.75,
            'tags': ['deep-learning', 'optimization']
        },
        {
            'type': 'engagement',
            'content': 'neural network architecture patterns',
            'timestamp': 1678987854,
            'session_duration': 520,
            'click_count': 12,
            'scroll_depth': 0.95,
            'tags': ['neural-networks', 'patterns']
        }
    ]
    
    # Analysis context
    context = {
        'relevance': 0.95,
        'importance': 0.90,
        'complexity': 0.85
    }
    
    print("\nAnalyzing User Behaviors:")
    for behavior in behaviors:
        print(f"\nType: {behavior['type']}")
        print(f"Content: {behavior['content']}")
        print(f"Duration: {behavior['session_duration']}s")
        print(f"Engagement: {behavior['click_count']} clicks, {behavior['scroll_depth']*100}% scroll")
    
    # Analyze behaviors
    results = processor.analyze_user_behavior(
        behaviors=behaviors,
        context=context
    )
    
    print("\nAnalysis Results:")
    print("-" * 40)
    print("Metrics:")
    for key, value in results['metrics'].items():
        print(f"{key}: {value:.6f}")
    
    print("\nEvolution Factor:")
    print(f"{results['evolution']:.6f}")
    
    return results

def test_recommendation_generation(processor: PracticalDataProcessorV1,
                                 user_data: Dict[str, Any]):
    """Test recommendation generation with user data."""
    print("\nTesting Recommendation Generation")
    print("=" * 50)
    
    # Generation context
    context = {
        'relevance': 0.90,
        'importance': 0.85,
        'complexity': 0.80
    }
    
    print("\nUser Data:")
    print("-" * 40)
    print(f"Type: {user_data['type']}")
    print(f"Content: {user_data['content']}")
    print(f"Session: {user_data['session_duration']}s")
    print(f"Engagement: {user_data['click_count']} clicks, {user_data['scroll_depth']*100}% scroll")
    
    # Generate recommendations
    recommendations = processor.generate_recommendations(
        user_data=user_data,
        context=context
    )
    
    print("\nRecommendations:")
    print("-" * 40)
    for i, rec in enumerate(recommendations, 1):
        print(f"\nRecommendation {i}:")
        print(f"Pattern Type: {rec.get('type', 'N/A')}")
        print(f"Coherence: {rec.get('coherence', 0.0):.6f}")
        print(f"Evolution: {rec.get('evolution', 0.0):.6f}")
    
    return recommendations

def main():
    print("\nPRACTICAL DATA PROCESSOR V1 TEST")
    print("=" * 80)
    
    # Initialize processor
    processor = PracticalDataProcessorV1()
    
    # Test behavior analysis
    analysis_results = test_user_behavior_analysis(processor)
    
    # Test recommendation generation
    user_data = {
        'type': 'profile',
        'content': 'interested in quantum computing and machine learning',
        'timestamp': 1678988054,
        'session_duration': 750,
        'click_count': 15,
        'scroll_depth': 0.90,
        'tags': ['quantum', 'ml', 'computing', 'interests'],
        'history': [
            'quantum research',
            'machine learning applications',
            'neural networks'
        ]
    }
    
    recommendations = test_recommendation_generation(
        processor=processor,
        user_data=user_data
    )
    
    print("\nTest Summary")
    print("=" * 50)
    print(f"Behaviors Analyzed: {len(analysis_results['patterns'])}")
    print(f"Recommendations Generated: {len(recommendations)}")
    print(f"Evolution Factor: {analysis_results['evolution']:.6f}")
    
    # Calculate phi-harmonic metrics
    phi = (1 + 5 ** 0.5) / 2
    metrics = analysis_results['metrics']
    
    print("\nPhi-Harmonic Metrics:")
    print("-" * 40)
    print(f"Coherence Ratio: {metrics['coherence']/phi:.6f}")
    print(f"Stability Factor: {metrics['stability']*phi:.6f}")
    print(f"Evolution Growth: {metrics['evolution']/(phi**2):.6f}")
    print(f"Learning Progress: {metrics['learning']*phi:.6f}")

if __name__ == "__main__":
    main()
