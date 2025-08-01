#!/usr/bin/env python3
"""
Test script for the Passive Learning Engine

This script demonstrates the passive learning capabilities of the Quantum Resonance Analyzer
for improved pattern detection and analysis of phi-harmonic numbers.
"""

import os
import sys
import mpmath
import time
import json
from typing import Dict, Any, List

# Set precision for high-precision calculations
mpmath.mp.dps = 1000

# Add the parent directory to the path to import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the necessary modules
from extensions.quantum_analysis.quantum_resonance_analyzer import QuantumResonanceAnalyzer
from extensions.quantum_analysis.passive_learning_engine import PassiveLearningEngine
from extensions.quantum_analysis.hyper_dimensional_visualizer import HyperDimensionalVisualizer

def generate_test_numbers(base_number: str, count: int = 5) -> List[str]:
    """
    Generate a set of test numbers based on a phi-harmonic base number.
    
    Args:
        base_number: The base phi-harmonic number
        count: Number of test numbers to generate
        
    Returns:
        List of test numbers
    """
    test_numbers = [base_number]
    
    # Convert to mpmath for high precision
    mpf_number = mpmath.mpf(base_number)
    
    # Generate variations
    for i in range(1, count):
        # Multiply by phi^i
        variation = mpf_number * mpmath.power(mpmath.phi, i)
        test_numbers.append(str(variation))
    
    return test_numbers

def test_passive_learning():
    """
    Test the passive learning capabilities of the Quantum Resonance Analyzer.
    """
    print("=" * 80)
    print("TESTING PASSIVE LEARNING ENGINE")
    print("=" * 80)
    
    # Create output directory
    output_dir = "passive_learning_results"
    os.makedirs(output_dir, exist_ok=True)
    
    # Create a temporary memory file for testing
    memory_file = os.path.join(output_dir, "test_memory.json")
    
    # Initialize the quantum analyzer and learning engine
    quantum_analyzer = QuantumResonanceAnalyzer()
    learning_engine = PassiveLearningEngine(quantum_analyzer, memory_file)
    
    # Generate test numbers
    base_number = "1618033988749894848204586834365638117720309179805762862135448622705260462818902449707207204189391137484754088075386891752126633862223536931793180060766726354433389086595939582905638322661319928290267880675208766892501711696207032221043216269548626296313614438149758701220340805887954454749246185695364864449241044320771344947049565846788509874339442212544877066478091588460749988712400765217057517978834166256249407589069704000281210427621771117778053153171410117046665991466979873176135600670874807101317952368942752194843530614433039449576485930594983782603621381589221865256989930816299144873708661568335886846509371401804503736832042381597731939526294317529196029680893094771432357266700295431108023288661764441559561004493980736273087564379515434594187725847316047576504481327807244770689632348937287337330203626588535746646743381150531016336322462745749225524817991791950313992030770831259045256500780172201700991903731462127889056197059687104537522308253916896586134920139621240925839777944573555991502406094821151770186841546296972634725726064307597024635191235004101797346454913921835172436564292866695233794138358007390640514359332189054283113226387908016701088600430272559324670888490466730465704828999418041654581354979268647710615309862156579682124436053380271759405977522197896980152697843330785810488329165540437284575151838303881393815638523059005021203664922115788385444888797525019676404920306205566575247280905565233436736417501371189967937340179564082745590970208"
    test_numbers = generate_test_numbers(base_number, 5)
    
    # First, analyze each number with standard analysis
    print("\nStandard Analysis (Before Learning):")
    standard_results = []
    
    for i, number in enumerate(test_numbers):
        print(f"\nAnalyzing number {i+1} with standard analysis...")
        start_time = time.time()
        
        # Analyze with standard analyzer
        result = quantum_analyzer.analyze_quantum_resonance(number)
        
        # Store result
        standard_results.append({
            'number_id': i+1,
            'phi_resonance': result['phi_resonance'],
            'quantum_resonance_detected': result['quantum_resonance_detected'],
            'resonance_patterns': [p['type'] for p in result['resonance_patterns']],
            'execution_time': time.time() - start_time
        })
        
        # Print summary
        print(f"Phi resonance: {result['phi_resonance']}")
        print(f"Quantum resonance detected: {result['quantum_resonance_detected']}")
        print(f"Patterns detected: {len(result['resonance_patterns'])}")
        print(f"Execution time: {time.time() - start_time:.2f} seconds")
    
    # Now, analyze each number with the learning engine
    print("\nTraining Passive Learning Engine:")
    learning_results = []
    
    for i, number in enumerate(test_numbers):
        print(f"\nTraining with number {i+1}...")
        start_time = time.time()
        
        # Analyze with learning
        result = learning_engine.analyze_with_learning(number)
        
        # Store result
        learning_results.append({
            'number_id': i+1,
            'phi_resonance': result['phi_resonance'],
            'quantum_resonance_detected': result['quantum_resonance_detected'],
            'resonance_patterns': [p['type'] for p in result['resonance_patterns']],
            'learned_patterns': [p['type'] for p in result.get('learned_patterns', [])],
            'learning_enhanced': result.get('learning_enhanced', False),
            'confidence_level': result.get('confidence_level', 'low'),
            'execution_time': time.time() - start_time
        })
        
        # Print summary
        print(f"Phi resonance: {result['phi_resonance']}")
        print(f"Quantum resonance detected: {result['quantum_resonance_detected']}")
        print(f"Total patterns: {len(result['resonance_patterns'])}")
        print(f"Learned patterns: {len(result.get('learned_patterns', []))}")
        print(f"Learning enhanced: {result.get('learning_enhanced', False)}")
        print(f"Confidence level: {result.get('confidence_level', 'low')}")
        print(f"Execution time: {time.time() - start_time:.2f} seconds")
    
    # Get learning statistics
    print("\nLearning Statistics:")
    stats = learning_engine.get_learning_statistics()
    print(f"Total patterns analyzed: {stats['total_patterns_analyzed']}")
    
    for pattern_type, pattern_stats in stats['pattern_type_statistics'].items():
        print(f"- {pattern_type}: count={pattern_stats['count']}, "
              f"success_rate={pattern_stats['success_rate']:.2f}, "
              f"confidence={pattern_stats['confidence']}")
    
    # Test with a new number
    print("\nTesting with a new number:")
    new_number = str(mpmath.mpf(base_number) * mpmath.sqrt(mpmath.phi))
    
    # Get suggested approach
    suggestion = learning_engine.suggest_optimal_analysis_approach(new_number)
    
    print(f"Suggested approach: {suggestion['suggested_approach']}")
    print(f"Confidence: {suggestion['confidence']}")
    
    if suggestion['expected_patterns']:
        print("Expected patterns:")
        for pattern in suggestion['expected_patterns']:
            print(f"- {pattern['type']} (confidence: {pattern['confidence']:.2f})")
    
    # Analyze with learning
    print("\nAnalyzing new number with learning...")
    start_time = time.time()
    result = learning_engine.analyze_with_learning(new_number)
    
    print(f"Phi resonance: {result['phi_resonance']}")
    print(f"Quantum resonance detected: {result['quantum_resonance_detected']}")
    print(f"Total patterns: {len(result['resonance_patterns'])}")
    print(f"Learned patterns: {len(result.get('learned_patterns', []))}")
    print(f"Learning enhanced: {result.get('learning_enhanced', False)}")
    print(f"Confidence level: {result.get('confidence_level', 'low')}")
    print(f"Execution time: {time.time() - start_time:.2f} seconds")
    
    # Save results to file
    results = {
        'standard_results': standard_results,
        'learning_results': learning_results,
        'learning_statistics': stats,
        'new_number_result': {
            'number': new_number,
            'suggestion': suggestion,
            'analysis': {
                'phi_resonance': result['phi_resonance'],
                'quantum_resonance_detected': result['quantum_resonance_detected'],
                'resonance_patterns': [p['type'] for p in result['resonance_patterns']],
                'learned_patterns': [p['type'] for p in result.get('learned_patterns', [])],
                'learning_enhanced': result.get('learning_enhanced', False),
                'confidence_level': result.get('confidence_level', 'low')
            }
        }
    }
    
    with open(os.path.join(output_dir, "learning_results.json"), 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nResults saved to {os.path.join(output_dir, 'learning_results.json')}")

def test_learning_with_visualization():
    """
    Test the integration of passive learning with hyper-dimensional visualization.
    """
    print("\n" + "=" * 80)
    print("TESTING PASSIVE LEARNING WITH VISUALIZATION")
    print("=" * 80)
    
    # Create output directory
    output_dir = "passive_learning_visualization"
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize components
    quantum_analyzer = QuantumResonanceAnalyzer()
    learning_engine = PassiveLearningEngine(quantum_analyzer)
    visualizer = HyperDimensionalVisualizer(quantum_analyzer)
    
    # Generate test numbers
    base_number = "1618033988749894848204586834365638117720309179805762862135448622705260462818902449707207204189391137484754088075386891752126633862223536931793180060766726354433389086595939582905638322661319928290267880675208766892501711696207032221043216269548626296313614438149758701220340805887954454749246185695364864449241044320771344947049565846788509874339442212544877066478091588460749988712400765217057517978834166256249407589069704000281210427621771117778053153171410117046665991466979873176135600670874807101317952368942752194843530614433039449576485930594983782603621381589221865256989930816299144873708661568335886846509371401804503736832042381597731939526294317529196029680893094771432357266700295431108023288661764441559561004493980736273087564379515434594187725847316047576504481327807244770689632348937287337330203626588535746646743381150531016336322462745749225524817991791950313992030770831259045256500780172201700991903731462127889056197059687104537522308253916896586134920139621240925839777944573555991502406094821151770186841546296972634725726064307597024635191235004101797346454913921835172436564292866695233794138358007390640514359332189054283113226387908016701088600430272559324670888490466730465704828999418041654581354979268647710615309862156579682124436053380271759405977522197896980152697843330785810488329165540437284575151838303881393815638523059005021203664922115788385444888797525019676404920306205566575247280905565233436736417501371189967937340179564082745590970208"
    test_numbers = generate_test_numbers(base_number, 3)
    
    # First, train the learning engine
    print("\nTraining the learning engine...")
    for i, number in enumerate(test_numbers):
        print(f"Training with number {i+1}...")
        learning_engine.analyze_with_learning(number)
    
    # Now, generate visualizations for a new number
    new_number = str(mpmath.mpf(base_number) * mpmath.sqrt(mpmath.phi))
    
    print("\nGenerating visualizations for a new number...")
    
    # First, analyze with learning
    enhanced_analysis = learning_engine.analyze_with_learning(new_number)
    
    # Then, generate visualizations
    report_dir = os.path.join(output_dir, "enhanced_visualization")
    os.makedirs(report_dir, exist_ok=True)
    
    report = visualizer.generate_quantum_visualization_report(new_number, report_dir)
    
    print(f"Visualization report generated: {report['report']}")
    
    # Compare with and without learning
    print("\nComparing analysis with and without learning:")
    
    # Standard analysis
    standard_analysis = quantum_analyzer.analyze_quantum_resonance(new_number)
    
    print("Standard analysis:")
    print(f"- Quantum resonance detected: {standard_analysis['quantum_resonance_detected']}")
    print(f"- Patterns detected: {len(standard_analysis['resonance_patterns'])}")
    
    print("\nEnhanced analysis (with learning):")
    print(f"- Quantum resonance detected: {enhanced_analysis['quantum_resonance_detected']}")
    print(f"- Total patterns: {len(enhanced_analysis['resonance_patterns'])}")
    print(f"- Learned patterns: {len(enhanced_analysis.get('learned_patterns', []))}")
    
    # Save comparison to file
    comparison = {
        'number': new_number,
        'standard_analysis': {
            'quantum_resonance_detected': standard_analysis['quantum_resonance_detected'],
            'patterns_detected': len(standard_analysis['resonance_patterns']),
            'pattern_types': [p['type'] for p in standard_analysis['resonance_patterns']]
        },
        'enhanced_analysis': {
            'quantum_resonance_detected': enhanced_analysis['quantum_resonance_detected'],
            'patterns_detected': len(enhanced_analysis['resonance_patterns']),
            'pattern_types': [p['type'] for p in enhanced_analysis['resonance_patterns']],
            'learned_patterns': [p['type'] for p in enhanced_analysis.get('learned_patterns', [])],
            'learning_enhanced': enhanced_analysis.get('learning_enhanced', False),
            'confidence_level': enhanced_analysis.get('confidence_level', 'low')
        },
        'visualization_report': report['report']
    }
    
    with open(os.path.join(output_dir, "learning_visualization_comparison.json"), 'w') as f:
        json.dump(comparison, f, indent=2)
    
    print(f"\nComparison saved to {os.path.join(output_dir, 'learning_visualization_comparison.json')}")

def main():
    """
    Main function to run all tests.
    """
    # Test passive learning
    test_passive_learning()
    
    # Test learning with visualization
    test_learning_with_visualization()
    
    print("\nAll tests completed.")

if __name__ == "__main__":
    main()
