#!/usr/bin/env python3
"""
Test script for Advanced Meta-Learning capabilities in Quantum Resonance Analysis.

This script demonstrates the advanced meta-learning capabilities for phi-harmonic numbers,
showing how the system can detect higher-order patterns across multiple analyses.
"""

import os
import sys
import json
import time
import mpmath
import numpy as np
from typing import Dict, Any, List

# Add the parent directory to the path to import core modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import core components
from extensions.quantum_analysis.quantum_resonance_analyzer import QuantumResonanceAnalyzer
from extensions.quantum_analysis.passive_learning_engine import PassiveLearningEngine
from extensions.quantum_analysis.hyper_dimensional_visualizer import HyperDimensionalVisualizer
from extensions.quantum_analysis.enhanced_hyper_dimensional_visualizer import EnhancedHyperDimensionalVisualizer
from extensions.quantum_analysis.meta_pattern_detector import MetaPatternDetector
from extensions.quantum_analysis.advanced_meta_learning import AdvancedMetaLearning

# Ensure visualization directory exists
os.makedirs('advanced_meta_learning_visualization', exist_ok=True)

def print_separator(title: str = "") -> None:
    """Print a separator line with optional title."""
    print("\n" + "=" * 80)
    if title:
        print(title)
        print("=" * 80)

def test_standard_analysis(analyzer: QuantumResonanceAnalyzer, number: str) -> Dict[str, Any]:
    """
    Test standard quantum resonance analysis.
    
    Args:
        analyzer: QuantumResonanceAnalyzer instance
        number: The phi-harmonic number to analyze
        
    Returns:
        Analysis results
    """
    print_separator("STANDARD QUANTUM RESONANCE ANALYSIS")
    print(f"Analyzing number with standard analysis...")
    
    # Perform standard analysis
    start_time = time.time()
    results = analyzer.analyze_quantum_resonance(number)
    end_time = time.time()
    
    # Print results
    print(f"Quantum resonance detected: {results['quantum_resonance_detected']}")
    print(f"Phi resonance: {results['phi_resonance']:.10f}")
    print(f"Analysis completed in {end_time - start_time:.2f} seconds.")
    
    return results

def test_passive_learning(learning_engine: PassiveLearningEngine, number: str) -> Dict[str, Any]:
    """
    Test passive learning enhanced analysis.
    
    Args:
        learning_engine: PassiveLearningEngine instance
        number: The phi-harmonic number to analyze
        
    Returns:
        Analysis results
    """
    print_separator("PASSIVE LEARNING ENHANCED ANALYSIS")
    print(f"Analyzing number with passive learning...")
    
    # Perform learning-enhanced analysis
    start_time = time.time()
    results = learning_engine.analyze_with_learning(number)
    end_time = time.time()
    
    # Print results
    print(f"Quantum resonance detected: {results['quantum_resonance_detected']}")
    print(f"Phi resonance: {results['phi_resonance']:.10f}")
    print(f"Learning enhanced: {results.get('learning_enhanced', False)}")
    print(f"Analysis completed in {end_time - start_time:.2f} seconds.")
    
    return results

def test_meta_pattern_detection(meta_detector: MetaPatternDetector, number: str) -> Dict[str, Any]:
    """
    Test meta-pattern detection.
    
    Args:
        meta_detector: MetaPatternDetector instance
        number: The phi-harmonic number to analyze
        
    Returns:
        Analysis results
    """
    print_separator("META-PATTERN DETECTION")
    print(f"Analyzing number with meta-pattern detection...")
    
    # Perform meta-pattern enhanced analysis
    start_time = time.time()
    results = meta_detector.analyze_with_meta_learning(number)
    end_time = time.time()
    
    # Print results
    print(f"Quantum resonance detected: {results['quantum_resonance_detected']}")
    print(f"Phi resonance: {results['phi_resonance']:.10f}")
    print(f"Learning enhanced: {results.get('learning_enhanced', False)}")
    print(f"Meta-pattern enhanced: {results.get('meta_pattern_enhanced', False)}")
    print(f"Analysis completed in {end_time - start_time:.2f} seconds.")
    
    # Print meta-insights if available
    if results.get('meta_insights'):
        print("\nMeta-insights:")
        for insight in results['meta_insights']:
            print(f"- {insight['description']} (confidence: {insight.get('confidence', 0.0):.2f})")
    
    return results

def test_advanced_meta_learning(advanced_meta_learning: AdvancedMetaLearning, number: str) -> Dict[str, Any]:
    """
    Test advanced meta-learning.
    
    Args:
        advanced_meta_learning: AdvancedMetaLearning instance
        number: The phi-harmonic number to analyze
        
    Returns:
        Analysis results
    """
    print_separator("ADVANCED META-LEARNING")
    print(f"Analyzing number with advanced meta-learning...")
    
    # Perform advanced meta-learning analysis
    start_time = time.time()
    results = advanced_meta_learning.analyze_with_advanced_meta_learning(number)
    end_time = time.time()
    
    # Print results
    print(f"Quantum resonance detected: {results['quantum_resonance_detected']}")
    print(f"Phi resonance: {results['phi_resonance']:.10f}")
    print(f"Learning enhanced: {results.get('learning_enhanced', False)}")
    print(f"Meta-pattern enhanced: {results.get('meta_pattern_enhanced', False)}")
    print(f"Advanced meta-learning enhanced: {results.get('advanced_meta_learning_enhanced', False)}")
    print(f"Analysis completed in {end_time - start_time:.2f} seconds.")
    
    # Print meta-insights if available
    if results.get('meta_insights'):
        print("\nMeta-insights:")
        for insight in results['meta_insights']:
            print(f"- {insight['description']} (confidence: {insight.get('confidence', 0.0):.2f})")
    
    # Print higher-order insights if available
    if results.get('higher_order_insights'):
        print("\nHigher-order insights:")
        for insight in results['higher_order_insights']:
            print(f"- {insight['description']} (confidence: {insight.get('confidence', 0.0):.2f})")
    
    # Print suggested approach if available
    suggested_approach = results.get('suggested_approach', {})
    if suggested_approach:
        print(f"\nSuggested approach: {suggested_approach.get('approach', 'unknown')}")
        print(f"Confidence: {suggested_approach.get('confidence', 0.0):.2f}")
        print(f"Description: {suggested_approach.get('description', '')}")
    
    return results

def test_visualization(advanced_meta_learning: AdvancedMetaLearning, number: str, index: int) -> str:
    """
    Test visualization with advanced meta-learning.
    
    Args:
        advanced_meta_learning: AdvancedMetaLearning instance
        number: The phi-harmonic number to visualize
        index: Index for the output file name
        
    Returns:
        Path to the visualization file
    """
    print_separator("ADVANCED META-LEARNING VISUALIZATION")
    print(f"Visualizing number with advanced meta-learning...")
    
    # Create output file name
    output_file = f"advanced_meta_learning_visualization/visualization_{index}.png"
    
    # Perform visualization
    start_time = time.time()
    visualization_file = advanced_meta_learning.visualize_with_advanced_meta_learning(number, output_file)
    end_time = time.time()
    
    print(f"Visualization completed in {end_time - start_time:.2f} seconds.")
    print(f"Visualization saved to: {visualization_file}")
    
    return visualization_file

def compare_analysis_approaches(number: str, results: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    """
    Compare different analysis approaches.
    
    Args:
        number: The phi-harmonic number analyzed
        results: Dictionary of results from different approaches
        
    Returns:
        Comparison results
    """
    print_separator("COMPARISON OF ANALYSIS APPROACHES")
    
    # Create comparison data
    comparison = {
        'number': number,
        'timestamp': time.time(),
        'approaches': {}
    }
    
    # Add results for each approach
    for approach, approach_results in results.items():
        comparison['approaches'][approach] = {
            'quantum_resonance_detected': approach_results.get('quantum_resonance_detected', False),
            'phi_resonance': approach_results.get('phi_resonance', 0.0),
            'patterns_detected': len(approach_results.get('resonance_patterns', [])),
            'learning_enhanced': approach_results.get('learning_enhanced', False),
            'meta_pattern_enhanced': approach_results.get('meta_pattern_enhanced', False),
            'advanced_meta_learning_enhanced': approach_results.get('advanced_meta_learning_enhanced', False),
            'meta_insights_count': len(approach_results.get('meta_insights', [])),
            'higher_order_insights_count': len(approach_results.get('higher_order_insights', []))
        }
    
    # Print comparison
    print(f"Comparing analysis approaches for phi-harmonic number:")
    
    # Print table header
    print(f"{'Approach':<25} {'Resonance':<10} {'Patterns':<10} {'Meta':<10} {'Higher':<10}")
    print(f"{'-'*25} {'-'*10} {'-'*10} {'-'*10} {'-'*10}")
    
    # Print table rows
    for approach, data in comparison['approaches'].items():
        print(f"{approach:<25} {data['phi_resonance']:<10.6f} {data['patterns_detected']:<10} {data['meta_insights_count']:<10} {data['higher_order_insights_count']:<10}")
    
    # Save comparison to file
    comparison_file = f"advanced_meta_learning_visualization/comparison.json"
    try:
        with open(comparison_file, 'w') as f:
            json.dump(comparison, f, indent=2)
        print(f"\nComparison saved to: {comparison_file}")
    except Exception as e:
        print(f"Error saving comparison: {e}")
    
    return comparison

def main() -> None:
    """Main test function."""
    print_separator("TESTING ADVANCED META-LEARNING")
    
    # Initialize components
    analyzer = QuantumResonanceAnalyzer()
    learning_engine = PassiveLearningEngine()
    meta_detector = MetaPatternDetector(learning_engine=learning_engine)
    advanced_meta_learning = AdvancedMetaLearning(
        learning_engine=learning_engine,
        meta_detector=meta_detector
    )
    
    # Define test phi-harmonic numbers
    # These numbers are designed to exhibit different patterns
    test_numbers = [
        # Phi-based number (golden ratio)
        "1618033988749894848204586834365638117720309179805762862135448622705260462818902449707207204189391137",
        
        # Phi^2-based number
        "2618033988749894848204586834365638117720309179805762862135448622705260462818902449707207204189391137",
        
        # Phi^3-based number
        "4236067977499789696409173668731276235440618359611525724270897245410520925637804899414414408378782274",
        
        # Phi^5-based number
        "11090169943749474241023934171828190588601545899028814310677243113526302314094512248536035102094695685",
        
        # Phi^8-based number
        "47288921376978896434112000260636151514393808549496428667772490381526302314094512248536035102094695685",
        
        # Arithmetic progression (phi + 1)
        "2618033988749894848204586834365638117720309179805762862135448622705260462818902449707207204189391137",
        
        # Arithmetic progression (phi + 2)
        "3618033988749894848204586834365638117720309179805762862135448622705260462818902449707207204189391137",
        
        # Geometric progression (phi * 2)
        "3236067977499789696409173668731276235440618359611525724270897245410520925637804899414414408378782274",
        
        # Geometric progression (phi * 3)
        "4854101966249684544613760503096914353160927539417288586406345868115781388456707348121621612568173411",
        
        # Complex pattern (phi^2 * 2 + 1)
        "6236067977499789696409173668731276235440618359611525724270897245410520925637804899414414408378782274"
    ]
    
    # Test each number with different approaches
    all_comparisons = []
    
    for i, number in enumerate(test_numbers):
        print_separator(f"TESTING NUMBER {i+1}/{len(test_numbers)}")
        print(f"Phi-harmonic number: {number[:50]}...")
        
        # Test with different approaches
        results = {
            'standard': test_standard_analysis(analyzer, number),
            'passive_learning': test_passive_learning(learning_engine, number),
            'meta_pattern': test_meta_pattern_detection(meta_detector, number),
            'advanced_meta_learning': test_advanced_meta_learning(advanced_meta_learning, number)
        }
        
        # Test visualization
        visualization_file = test_visualization(advanced_meta_learning, number, i+1)
        
        # Compare approaches
        comparison = compare_analysis_approaches(number, results)
        all_comparisons.append(comparison)
    
    # Print final statistics
    print_separator("ADVANCED META-LEARNING STATISTICS")
    
    # Get statistics
    stats = advanced_meta_learning.get_advanced_meta_learning_statistics()
    
    print(f"Total analyses: {stats['total_analyses']}")
    print(f"Meta-enhanced analyses: {stats['meta_enhanced_analyses']}")
    print(f"Higher-order analyses: {stats['higher_order_analyses']}")
    print(f"Average confidence: {stats.get('average_confidence', 0.0):.2f}")
    
    print(f"\nAdaptive thresholds:")
    adaptive_thresholds = stats.get('adaptive_thresholds', {})
    print(f"Confidence threshold: {adaptive_thresholds.get('confidence_threshold', 0.0):.2f}")
    print(f"Temporal weight: {adaptive_thresholds.get('temporal_weight', 0.0):.2f}")
    print(f"Hierarchical weight: {adaptive_thresholds.get('hierarchical_weight', 0.0):.2f}")
    print(f"Correlation weight: {adaptive_thresholds.get('correlation_weight', 0.0):.2f}")
    
    print(f"\nMeta-pattern statistics:")
    print(f"Total meta-patterns: {stats.get('total_meta_patterns', 0)}")
    print(f"Significant meta-patterns: {stats.get('significant_meta_patterns', 0)}")
    print(f"Cross-correlations: {stats.get('cross_correlations', 0)}")
    print(f"Temporal sequences: {stats.get('temporal_sequences', 0)}")
    print(f"Hierarchies: {stats.get('hierarchies', 0)}")
    
    # Save all comparisons to a single file
    all_comparisons_file = f"advanced_meta_learning_visualization/all_comparisons.json"
    try:
        with open(all_comparisons_file, 'w') as f:
            json.dump(all_comparisons, f, indent=2)
        print(f"\nAll comparisons saved to: {all_comparisons_file}")
    except Exception as e:
        print(f"Error saving all comparisons: {e}")
    
    print_separator("ALL TESTS COMPLETED")

if __name__ == "__main__":
    main()
