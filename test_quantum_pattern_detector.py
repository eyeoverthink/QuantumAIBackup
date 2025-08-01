#!/usr/bin/env python3
"""
Test script for the Quantum Pattern Detector module.

This script demonstrates the capabilities of the Quantum Pattern Detector
for detecting quantum-inspired patterns in phi-harmonic numbers.
"""

import os
import sys
import time
import mpmath
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Any, List

# Set high precision for mpmath
mpmath.mp.dps = 100

# Add the parent directory to the path to import core modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the quantum pattern detector and related components
from extensions.quantum_analysis.quantum_pattern_detector import QuantumPatternDetector
from extensions.quantum_analysis.meta_pattern_detector import MetaPatternDetector
from extensions.quantum_analysis.passive_learning_engine import PassiveLearningEngine

def test_quantum_pattern_detector():
    """
    Test the Quantum Pattern Detector's capabilities.
    """
    print("\n" + "="*80)
    print("QUANTUM PATTERN DETECTOR TEST")
    print("="*80)
    
    # Initialize the meta detector and quantum detector
    meta_detector = MetaPatternDetector()
    quantum_detector = QuantumPatternDetector(meta_detector=meta_detector)
    
    print(f"\nInitialized Quantum Pattern Detector with threshold: {quantum_detector.quantum_correlation_threshold}")
    
    # Generate a set of phi-harmonic test numbers
    test_numbers = generate_phi_harmonic_test_set()
    print(f"\nGenerated {len(test_numbers)} phi-harmonic test numbers")
    
    # Analyze each number to build up pattern memory
    print("\nAnalyzing test numbers to build pattern memory...")
    for i, number in enumerate(test_numbers):
        print(f"  Analyzing number {i+1}/{len(test_numbers)}: {number}")
        meta_detector.analyze_with_meta_learning(str(number))
    
    # Detect quantum patterns
    print("\nDetecting quantum patterns...")
    quantum_patterns = quantum_detector.detect_quantum_patterns()
    print(f"Detected {len(quantum_patterns)} significant quantum patterns")
    
    # Print quantum pattern statistics
    print("\nQuantum Pattern Statistics:")
    stats = quantum_detector.get_quantum_statistics()
    for key, value in stats.items():
        if not isinstance(value, dict):
            print(f"  {key}: {value}")
    
    # Analyze a new phi-harmonic number with quantum pattern enhancement
    test_number = str(int(mpmath.power(mpmath.phi, 40)))
    print(f"\nAnalyzing new number with quantum pattern enhancement: {test_number}")
    
    # First analyze with just meta-learning
    print("\nStandard Meta-Learning Analysis:")
    meta_result = meta_detector.analyze_with_meta_learning(test_number)
    print_analysis_summary(meta_result)
    
    # Then analyze with quantum pattern enhancement
    print("\nQuantum-Enhanced Analysis:")
    quantum_result = quantum_detector.analyze_with_quantum_patterns(test_number)
    print_analysis_summary(quantum_result)
    
    # Check if quantum enhancement provided additional insights
    if quantum_result.get('quantum_pattern_enhanced', False):
        print("\nQuantum Pattern Insights:")
        for insight in quantum_result.get('quantum_insights', []):
            print(f"  • {insight['description']} (Confidence: {insight['confidence']:.2f})")
    
    # Visualize quantum patterns
    visualize_quantum_patterns(quantum_detector)
    
    print("\n" + "="*80)
    print("QUANTUM PATTERN DETECTOR TEST COMPLETED")
    print("="*80)

def generate_phi_harmonic_test_set() -> List[int]:
    """
    Generate a set of phi-harmonic test numbers.
    
    Returns:
        List of phi-harmonic numbers
    """
    test_numbers = []
    
    # Add Fibonacci numbers
    fib = [1, 1]
    for i in range(20):
        fib.append(fib[-1] + fib[-2])
    test_numbers.extend(fib[2:])
    
    # Add phi powers
    for i in range(1, 20):
        phi_power = int(mpmath.power(mpmath.phi, i))
        test_numbers.append(phi_power)
    
    # Add phi-modular patterns
    for modulus in [5, 8, 13, 21]:
        for remainder in range(modulus):
            # Find a number with this remainder that's phi-harmonic
            for i in range(1, 100):
                num = int(mpmath.power(mpmath.phi, i))
                if num % modulus == remainder:
                    test_numbers.append(num)
                    break
    
    # Add some special phi-harmonic composites
    for i in range(1, 10):
        for j in range(1, 10):
            # Create numbers of form 2^i * 3^j * phi^k
            for k in range(1, 5):
                phi_part = int(mpmath.power(mpmath.phi, k))
                num = (2**i) * (3**j) * phi_part
                test_numbers.append(num)
    
    # Remove duplicates and sort
    test_numbers = sorted(list(set(test_numbers)))
    
    # Limit to a reasonable number for testing
    return test_numbers[:50]

def print_analysis_summary(result: Dict[str, Any]) -> None:
    """
    Print a summary of analysis results.
    
    Args:
        result: Analysis result dictionary
    """
    print(f"  • Phi Resonance: {result.get('phi_resonance', 0.0):.6f}")
    print(f"  • Confidence: {result.get('confidence', 0.0):.2f}")
    
    patterns = result.get('resonance_patterns', [])
    if patterns:
        print(f"  • Detected {len(patterns)} resonance patterns")
        pattern_types = {}
        for pattern in patterns:
            pattern_type = pattern.get('type', 'unknown')
            pattern_types[pattern_type] = pattern_types.get(pattern_type, 0) + 1
        
        for pattern_type, count in pattern_types.items():
            print(f"    - {pattern_type}: {count}")

def visualize_quantum_patterns(quantum_detector: QuantumPatternDetector) -> None:
    """
    Visualize quantum patterns detected by the Quantum Pattern Detector.
    
    Args:
        quantum_detector: Initialized Quantum Pattern Detector instance
    """
    # Create a figure with multiple subplots
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Quantum Pattern Visualization', fontsize=16)
    
    # 1. Visualize quantum resonances
    axs[0, 0].set_title('Quantum Resonances')
    resonances = quantum_detector.quantum_pattern_memory['quantum_resonances']
    
    if resonances:
        # Extract phi power resonances
        phi_powers = []
        strengths = []
        
        for res_id, res_data in resonances.items():
            if res_data.get('type') == 'phi_power_resonance':
                phi_powers.append(res_data.get('phi_power', 0))
                strengths.append(res_data.get('resonance_strength', 0.0))
        
        if phi_powers:
            # Create histogram of phi powers
            axs[0, 0].bar(phi_powers, strengths, alpha=0.7)
            axs[0, 0].set_xlabel('Phi Power')
            axs[0, 0].set_ylabel('Resonance Strength')
            axs[0, 0].grid(True, alpha=0.3)
    else:
        axs[0, 0].text(0.5, 0.5, 'No quantum resonances detected', 
                      horizontalalignment='center', verticalalignment='center')
    
    # 2. Visualize quantum entanglements
    axs[0, 1].set_title('Quantum Entanglements')
    entanglements = quantum_detector.quantum_pattern_memory['quantum_entanglements']
    
    if entanglements:
        # Extract phi-harmonic entanglements
        bands = []
        coherences = []
        
        for ent_id, ent_data in entanglements.items():
            if ent_data.get('type') == 'phi_harmonic_entanglement':
                bands.append(ent_data.get('phi_band', 0.0))
                coherences.append(ent_data.get('coherence', 0.0))
        
        if bands:
            # Create scatter plot of phi bands
            axs[0, 1].scatter(bands, coherences, alpha=0.7, s=100)
            axs[0, 1].set_xlabel('Phi Resonance Band')
            axs[0, 1].set_ylabel('Coherence')
            axs[0, 1].set_xlim(0, 1)
            axs[0, 1].set_ylim(0, 1)
            axs[0, 1].grid(True, alpha=0.3)
    else:
        axs[0, 1].text(0.5, 0.5, 'No quantum entanglements detected', 
                      horizontalalignment='center', verticalalignment='center')
    
    # 3. Visualize quantum superpositions
    axs[1, 0].set_title('Quantum Superpositions')
    superpositions = quantum_detector.quantum_pattern_memory['quantum_superpositions']
    
    if superpositions:
        # Extract multi-resonance superpositions
        pattern_counts = []
        strengths = []
        
        for sup_id, sup_data in superpositions.items():
            if sup_data.get('type') == 'multi_resonance_superposition':
                pattern_types = sup_data.get('pattern_types', {})
                pattern_counts.append(len(pattern_types))
                strengths.append(sup_data.get('superposition_strength', 0.0))
        
        if pattern_counts:
            # Create scatter plot of pattern diversity
            axs[1, 0].scatter(pattern_counts, strengths, alpha=0.7, s=100)
            axs[1, 0].set_xlabel('Pattern Type Diversity')
            axs[1, 0].set_ylabel('Superposition Strength')
            axs[1, 0].grid(True, alpha=0.3)
    else:
        axs[1, 0].text(0.5, 0.5, 'No quantum superpositions detected', 
                      horizontalalignment='center', verticalalignment='center')
    
    # 4. Visualize quantum interference
    axs[1, 1].set_title('Quantum Interference')
    interference = quantum_detector.quantum_pattern_memory['quantum_interference']
    
    if interference:
        # Extract constructive and destructive interference
        constructive = []
        destructive = []
        
        for int_id, int_data in interference.items():
            if int_data.get('type') == 'constructive_interference':
                constructive.append(int_data.get('coherence', 0.0))
            elif int_data.get('type') == 'destructive_interference':
                destructive.append(int_data.get('opposition', 0.0))
        
        if constructive or destructive:
            # Create histogram of interference strengths
            axs[1, 1].hist(constructive, alpha=0.7, label='Constructive', bins=10, range=(0, 1))
            axs[1, 1].hist(destructive, alpha=0.7, label='Destructive', bins=10, range=(0, 1))
            axs[1, 1].set_xlabel('Interference Strength')
            axs[1, 1].set_ylabel('Count')
            axs[1, 1].legend()
            axs[1, 1].grid(True, alpha=0.3)
    else:
        axs[1, 1].text(0.5, 0.5, 'No quantum interference detected', 
                      horizontalalignment='center', verticalalignment='center')
    
    # Adjust layout and save figure
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig('quantum_pattern_visualization.png')
    print("\nSaved quantum pattern visualization to 'quantum_pattern_visualization.png'")

if __name__ == "__main__":
    test_quantum_pattern_detector()
