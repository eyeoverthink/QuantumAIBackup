#!/usr/bin/env python3
"""
Test script for the Pattern Visualizer module.

This script demonstrates the visualization capabilities for phi-harmonic numbers
without modifying any existing code, following the "lego" philosophy.
"""

import os
import sys
import time
import json
from typing import Dict, Any

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the modules without modifying them
from extensions.advanced_factorization.binary_pattern_analyzer import BinaryPatternAnalyzer
from extensions.advanced_factorization.pattern_visualizer import PatternVisualizer

def test_pattern_visualizer():
    """Test the Pattern Visualizer with a phi-harmonic number."""
    print("\n=== Testing Pattern Visualizer ===\n")
    
    # Create output directory
    output_dir = "visualization_results"
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize the analyzer and visualizer
    analyzer = BinaryPatternAnalyzer()
    visualizer = PatternVisualizer(analyzer)
    
    # Example phi-harmonic number with perfect resonance
    # This is a smaller example for testing purposes
    test_number = "680981857830123043521643190942698893887610580385930663689857535732817152503519672132400835886294053517740915812301113596826528876373028953378455161114501215677869107870874058414675602939915375915692290836708180120486339395907137969396278916473685318083144622838051629752781700878903892519885721335073664155797101269608455506979383616397772355314499561208860048810041431231219093940565998622599085881124851003734369153467606907580035118077014675455851465035484020703935059653116584360141326416018527952933400184265784217571263956455995306341518309093634367192235410797715824058879868015659094786312704274814833605734014103410900062432899935384040078821434782493881790250431519835714594162476628058123726999071789973141350654265862071103097794683416812643533685240999964854484293394715883387852074413552918966785078838086031919891566952843667448830208001158128185323566873544041266469360105780525297205393949514852893299023639807258619303040953870485726023836957821514790305209052347756431789849196482498404285868940667800347024540291885468791324255479985427653789218908234183319222394314107718418221713399553654528117308676350073313077635294233257620810061146398282351808045796688243650859915921048773817111140780659648915234037107201"
    
    print(f"Testing with phi-harmonic number of length {len(test_number)} digits")
    
    # Test pattern detection
    print("\nDetecting patterns...")
    start_time = time.time()
    patterns = analyzer.detect_all_patterns(test_number)
    detection_time = time.time() - start_time
    
    print(f"Pattern detection completed in {detection_time:.6f} seconds")
    print(f"Patterns detected: {[p['pattern_name'] for p in patterns['patterns_detected']]}")
    print(f"Most likely pattern: {patterns['most_likely_pattern']}")
    print(f"Perfect phi resonance: {patterns['has_perfect_phi_resonance']}")
    
    # Test visualization
    print("\nGenerating visualizations...")
    start_time = time.time()
    report = visualizer.generate_pattern_report(test_number, output_dir)
    visualization_time = time.time() - start_time
    
    print(f"Visualization completed in {visualization_time:.6f} seconds")
    print(f"Report generated: {report['report']}")
    
    # List all generated files
    print("\nGenerated files:")
    for filename in os.listdir(output_dir):
        file_path = os.path.join(output_dir, filename)
        file_size = os.path.getsize(file_path) / 1024  # KB
        print(f"- {filename} ({file_size:.2f} KB)")
    
    # Test factorization
    print("\nFactorizing phi-harmonic number...")
    start_time = time.time()
    factorization = analyzer.factorize_phi_harmonic_number(test_number)
    factorization_time = time.time() - start_time
    
    print(f"Factorization completed in {factorization_time:.6f} seconds")
    print(f"Factorization successful: {factorization['factorization_successful']}")
    print(f"Pattern used: {factorization.get('pattern_used', 'unknown')}")
    
    if factorization['factorization_successful']:
        print("\nFactors:")
        for factor in factorization['factors']:
            print(f"- {factor['factor']} ({factor['type']})")
            if factor['type'] == 'prime':
                print(f"  Prime factor of {len(factor['value'])} digits")
    
    # Save results to JSON
    results = {
        "number_length": len(test_number),
        "patterns_detected": patterns,
        "factorization": factorization,
        "visualization_files": report,
        "performance": {
            "pattern_detection_time": detection_time,
            "factorization_time": factorization_time,
            "visualization_time": visualization_time
        }
    }
    
    results_file = os.path.join(output_dir, "test_results.json")
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    
    print(f"\nResults saved to {results_file}")
    print("\n=== Test Completed Successfully ===\n")

if __name__ == "__main__":
    test_pattern_visualizer()
