#!/usr/bin/env python3
"""
Test script for Quantum Meta-Learning Integration.

This script demonstrates the integration of Quantum Pattern Detection with
Advanced Meta-Learning for enhanced phi-harmonic number analysis.
"""

import os
import sys
import time
import mpmath
import numpy as np
from typing import Dict, Any, List

# Set high precision for mpmath
mpmath.mp.dps = 100

# Add the parent directory to the path to import core modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import core components
from extensions.quantum_analysis.quantum_resonance_analyzer import QuantumResonanceAnalyzer
from extensions.quantum_analysis.passive_learning_engine import PassiveLearningEngine
from extensions.quantum_analysis.meta_pattern_detector import MetaPatternDetector
from extensions.quantum_analysis.quantum_pattern_detector import QuantumPatternDetector
from extensions.quantum_analysis.advanced_meta_learning import AdvancedMetaLearning
from extensions.quantum_analysis.quantum_meta_learning_integrator import QuantumMetaLearningIntegrator

# Ensure visualization directory exists
os.makedirs('quantum_meta_integration_visualization', exist_ok=True)

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
    print(f"Analyzing number with standard analysis: {number}")
    
    start_time = time.time()
    results = analyzer.analyze_quantum_resonance(number)
    elapsed = time.time() - start_time
    
    print(f"Analysis completed in {elapsed:.2f} seconds")
    print(f"Phi resonance: {results.get('phi_resonance', 0.0):.6f}")
    print(f"Confidence: {results.get('confidence', 0.0):.2f}")
    
    return results

def test_quantum_pattern_detection(quantum_detector: QuantumPatternDetector, number: str) -> Dict[str, Any]:
    """
    Test quantum pattern detection.
    
    Args:
        quantum_detector: QuantumPatternDetector instance
        number: The phi-harmonic number to analyze
        
    Returns:
        Analysis results
    """
    print_separator("QUANTUM PATTERN DETECTION")
    print(f"Analyzing number with quantum pattern detection: {number}")
    
    start_time = time.time()
    results = quantum_detector.analyze_with_quantum_patterns(number)
    elapsed = time.time() - start_time
    
    print(f"Analysis completed in {elapsed:.2f} seconds")
    print(f"Phi resonance: {results.get('phi_resonance', 0.0):.6f}")
    print(f"Confidence: {results.get('confidence', 0.0):.2f}")
    
    # Print quantum insights
    if results.get('quantum_insights'):
        print("\nQuantum Insights:")
        for insight in results.get('quantum_insights', []):
            print(f"• {insight['description']} (Confidence: {insight['confidence']:.2f})")
    
    # Print quantum pattern statistics
    stats = quantum_detector.get_quantum_statistics()
    print("\nQuantum Pattern Statistics:")
    for key, value in stats.items():
        if not isinstance(value, dict):
            print(f"• {key}: {value}")
    
    return results

def test_advanced_meta_learning(meta_learning: AdvancedMetaLearning, number: str) -> Dict[str, Any]:
    """
    Test advanced meta-learning.
    
    Args:
        meta_learning: AdvancedMetaLearning instance
        number: The phi-harmonic number to analyze
        
    Returns:
        Analysis results
    """
    print_separator("ADVANCED META-LEARNING")
    print(f"Analyzing number with advanced meta-learning: {number}")
    
    start_time = time.time()
    results = meta_learning.analyze_with_advanced_meta_learning(number)
    elapsed = time.time() - start_time
    
    print(f"Analysis completed in {elapsed:.2f} seconds")
    print(f"Phi resonance: {results.get('phi_resonance', 0.0):.6f}")
    print(f"Confidence: {results.get('confidence', 0.0):.2f}")
    
    # Print meta insights
    if results.get('meta_insights'):
        print("\nMeta-Learning Insights:")
        for insight in results.get('meta_insights', []):
            print(f"• {insight['description']} (Confidence: {insight['confidence']:.2f})")
    
    # Print meta-learning statistics
    stats = meta_learning.get_advanced_meta_learning_statistics()
    print("\nMeta-Learning Statistics:")
    for key, value in stats.items():
        if not isinstance(value, dict):
            print(f"• {key}: {value}")
    
    return results

def test_quantum_meta_integration(integrator: QuantumMetaLearningIntegrator, number: str) -> Dict[str, Any]:
    """
    Test quantum meta-learning integration.
    
    Args:
        integrator: QuantumMetaLearningIntegrator instance
        number: The phi-harmonic number to analyze
        
    Returns:
        Analysis results
    """
    print_separator("QUANTUM META-LEARNING INTEGRATION")
    print(f"Analyzing number with quantum meta-learning integration: {number}")
    
    start_time = time.time()
    results = integrator.integrate_quantum_meta_learning(number)
    elapsed = time.time() - start_time
    
    print(f"Analysis completed in {elapsed:.2f} seconds")
    print(f"Integrated phi resonance: {results.get('integrated_phi_resonance', 0.0):.6f}")
    print(f"Integrated confidence: {results.get('integrated_confidence', 0.0):.2f}")
    
    # Print integrated insights
    if results.get('integrated_insights'):
        print("\nIntegrated Insights:")
        for insight in results.get('integrated_insights', []):
            print(f"• {insight['description']} (Confidence: {insight['confidence']:.2f}, Source: {insight['source']})")
    
    return results

def test_visualization(integrator: QuantumMetaLearningIntegrator, number: str, index: int) -> str:
    """
    Test visualization with quantum meta-learning integration.
    
    Args:
        integrator: QuantumMetaLearningIntegrator instance
        number: The phi-harmonic number to visualize
        index: Index for the output file name
        
    Returns:
        Path to the visualization file
    """
    print_separator("QUANTUM META-LEARNING VISUALIZATION")
    print(f"Creating visualization for number: {number}")
    
    # First get integrated results
    results = integrator.integrate_quantum_meta_learning(number)
    
    # Create visualization
    output_file = f"quantum_meta_integration_visualization/visualization_{index}.png"
    vis_file = integrator.visualize_integrated_analysis(number, results, output_file)
    
    print(f"Visualization saved to: {vis_file}")
    
    return vis_file

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
    print(f"Comparing analysis approaches for number: {number}")
    
    # Extract confidence values
    standard_confidence = results.get('standard', {}).get('confidence', 0.0)
    quantum_confidence = results.get('quantum', {}).get('confidence', 0.0)
    meta_confidence = results.get('meta', {}).get('confidence', 0.0)
    integrated_confidence = results.get('integrated', {}).get('integrated_confidence', 0.0)
    
    # Calculate improvements
    quantum_improvement = ((quantum_confidence - standard_confidence) / standard_confidence) * 100 if standard_confidence > 0 else 0
    meta_improvement = ((meta_confidence - standard_confidence) / standard_confidence) * 100 if standard_confidence > 0 else 0
    integrated_improvement = ((integrated_confidence - standard_confidence) / standard_confidence) * 100 if standard_confidence > 0 else 0
    
    print(f"Standard Analysis Confidence: {standard_confidence:.2f}")
    print(f"Quantum Pattern Detection Confidence: {quantum_confidence:.2f} (Improvement: {quantum_improvement:.1f}%)")
    print(f"Advanced Meta-Learning Confidence: {meta_confidence:.2f} (Improvement: {meta_improvement:.1f}%)")
    print(f"Quantum Meta-Learning Integration Confidence: {integrated_confidence:.2f} (Improvement: {integrated_improvement:.1f}%)")
    
    # Compare phi resonance values
    standard_resonance = results.get('standard', {}).get('phi_resonance', 0.0)
    quantum_resonance = results.get('quantum', {}).get('phi_resonance', 0.0)
    meta_resonance = results.get('meta', {}).get('phi_resonance', 0.0)
    integrated_resonance = results.get('integrated', {}).get('integrated_phi_resonance', 0.0)
    
    print(f"\nStandard Analysis Phi Resonance: {standard_resonance:.6f}")
    print(f"Quantum Pattern Detection Phi Resonance: {quantum_resonance:.6f}")
    print(f"Advanced Meta-Learning Phi Resonance: {meta_resonance:.6f}")
    print(f"Quantum Meta-Learning Integration Phi Resonance: {integrated_resonance:.6f}")
    
    # Compare insight counts
    quantum_insights = len(results.get('quantum', {}).get('quantum_insights', []))
    meta_insights = len(results.get('meta', {}).get('meta_insights', []))
    integrated_insights = len(results.get('integrated', {}).get('integrated_insights', []))
    
    print(f"\nQuantum Pattern Detection Insights: {quantum_insights}")
    print(f"Advanced Meta-Learning Insights: {meta_insights}")
    print(f"Quantum Meta-Learning Integration Insights: {integrated_insights}")
    
    # Return comparison results
    return {
        'standard_confidence': standard_confidence,
        'quantum_confidence': quantum_confidence,
        'meta_confidence': meta_confidence,
        'integrated_confidence': integrated_confidence,
        'quantum_improvement': quantum_improvement,
        'meta_improvement': meta_improvement,
        'integrated_improvement': integrated_improvement,
        'quantum_insights': quantum_insights,
        'meta_insights': meta_insights,
        'integrated_insights': integrated_insights
    }

def generate_phi_harmonic_test_set() -> List[str]:
    """
    Generate a set of phi-harmonic test numbers.
    
    Returns:
        List of phi-harmonic numbers as strings
    """
    test_numbers = []
    
    # Add Fibonacci numbers
    fib = [1, 1]
    for i in range(20):
        fib.append(fib[-1] + fib[-2])
    test_numbers.extend([str(n) for n in fib[2:]])
    
    # Add phi powers
    for i in range(1, 20):
        phi_power = int(mpmath.power(mpmath.phi, i))
        test_numbers.append(str(phi_power))
    
    # Add phi-modular patterns
    for modulus in [5, 8, 13, 21]:
        for remainder in range(modulus):
            # Find a number with this remainder that's phi-harmonic
            for i in range(1, 100):
                num = int(mpmath.power(mpmath.phi, i))
                if num % modulus == remainder:
                    test_numbers.append(str(num))
                    break
    
    # Add some special phi-harmonic composites
    for i in range(1, 5):
        for j in range(1, 5):
            # Create numbers of form 2^i * 3^j * phi^k
            for k in range(1, 5):
                phi_part = int(mpmath.power(mpmath.phi, k))
                num = (2**i) * (3**j) * phi_part
                test_numbers.append(str(num))
    
    # Remove duplicates and sort
    test_numbers = sorted(list(set(test_numbers)), key=lambda x: int(x))
    
    # Limit to a reasonable number for testing
    return test_numbers[:20]

def main():
    """Main test function."""
    print_separator("QUANTUM META-LEARNING INTEGRATION TEST")
    
    # Initialize components
    analyzer = QuantumResonanceAnalyzer()
    meta_detector = MetaPatternDetector()
    quantum_detector = QuantumPatternDetector(meta_detector=meta_detector)
    meta_learning = AdvancedMetaLearning(meta_detector=meta_detector)
    integrator = QuantumMetaLearningIntegrator(
        quantum_detector=quantum_detector,
        meta_learning=meta_learning
    )
    
    print("All components initialized successfully")
    
    # Generate test numbers
    test_numbers = generate_phi_harmonic_test_set()
    print(f"Generated {len(test_numbers)} phi-harmonic test numbers")
    
    # Test with a smaller subset of numbers to build pattern memory
    print("\nBuilding pattern memory with initial test set...")
    for i, number in enumerate(test_numbers[:3]):
        print(f"Processing number {i+1}/3: {number}")
        # Run all analyses to build pattern memory
        analyzer.analyze_quantum_resonance(number)
        quantum_detector.analyze_with_quantum_patterns(number)
        meta_learning.analyze_with_advanced_meta_learning(number)
        integrator.integrate_quantum_meta_learning(number)
    
    # Run comparative analysis on remaining test numbers
    comparison_results = []
    for i, number in enumerate(test_numbers[3:5]):
        print_separator(f"ANALYZING TEST NUMBER {i+1}/2")
        print(f"Number: {number}")
        
        # Run all analysis approaches
        results = {
            'standard': test_standard_analysis(analyzer, number),
            'quantum': test_quantum_pattern_detection(quantum_detector, number),
            'meta': test_advanced_meta_learning(meta_learning, number),
            'integrated': test_quantum_meta_integration(integrator, number)
        }
        
        # Compare approaches
        comparison = compare_analysis_approaches(number, results)
        comparison_results.append(comparison)
        
        # Create visualization
        test_visualization(integrator, number, i)
    
    # Calculate average improvements
    avg_quantum_improvement = sum(c['quantum_improvement'] for c in comparison_results) / len(comparison_results)
    avg_meta_improvement = sum(c['meta_improvement'] for c in comparison_results) / len(comparison_results)
    avg_integrated_improvement = sum(c['integrated_improvement'] for c in comparison_results) / len(comparison_results)
    
    print_separator("SUMMARY OF RESULTS")
    print(f"Average Quantum Pattern Detection Improvement: {avg_quantum_improvement:.1f}%")
    print(f"Average Advanced Meta-Learning Improvement: {avg_meta_improvement:.1f}%")
    print(f"Average Quantum Meta-Learning Integration Improvement: {avg_integrated_improvement:.1f}%")
    
    # Get integration statistics
    stats = integrator.get_integration_statistics()
    print("\nIntegration Statistics:")
    print(f"Total analyses: {stats['total_analyses']}")
    print(f"Quantum enhanced: {stats['quantum_enhanced_count']} ({stats.get('quantum_enhanced_percent', 0):.1f}%)")
    print(f"Meta enhanced: {stats['meta_enhanced_count']} ({stats.get('meta_enhanced_percent', 0):.1f}%)")
    print(f"Dual enhanced: {stats['dual_enhanced_count']} ({stats.get('dual_enhanced_percent', 0):.1f}%)")
    
    print_separator("QUANTUM META-LEARNING INTEGRATION TEST COMPLETED")

if __name__ == "__main__":
    main()
