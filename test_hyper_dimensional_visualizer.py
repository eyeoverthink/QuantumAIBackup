#!/usr/bin/env python3
"""
Test script for the Hyper-Dimensional Visualizer

This script demonstrates the capabilities of the Hyper-Dimensional Visualizer
for visualizing quantum resonance patterns in phi-harmonic numbers.
"""

import os
import sys
import mpmath
import time
from typing import Dict, Any, List

# Set precision for high-precision calculations
mpmath.mp.dps = 1000

# Add the parent directory to the path to import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the necessary modules
from extensions.quantum_analysis.quantum_resonance_analyzer import QuantumResonanceAnalyzer
from extensions.quantum_analysis.hyper_dimensional_visualizer import HyperDimensionalVisualizer

def test_hyper_dimensional_visualizer():
    """
    Test the Hyper-Dimensional Visualizer with sample phi-harmonic numbers.
    """
    print("=" * 80)
    print("TESTING HYPER-DIMENSIONAL VISUALIZER")
    print("=" * 80)
    
    # Create output directory
    output_dir = "quantum_visualization_results"
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize the quantum analyzer and visualizer
    quantum_analyzer = QuantumResonanceAnalyzer()
    visualizer = HyperDimensionalVisualizer(quantum_analyzer, dimensions=5)
    
    # Test with different phi-harmonic numbers
    test_numbers = [
        # Small phi-harmonic number
        "1618033988749894848204586834365638117720309179805762862135448622705260462818902449707207204189391137484754088075386891752126633862223536931793180060766726354433389086595939582905638322661319928290267880675208766892501711696207032221043216269548626296313614438149758701220340805887954454749246185695364864449241044320771344947049565846788509874339442212544877066478091588460749988712400765217057517978834166256249407589069704000281210427621771117778053153171410117046665991466979873176135600670874807101317952368942752194843530614433039449576485930594983782603621381589221865256989930816299144873708661568335886846509371401804503736832042381597731939526294317529196029680893094771432357266700295431108023288661764441559561004493980736273087564379515434594187725847316047576504481327807244770689632348937287337330203626588535746646743381150531016336322462745749225524817991791950313992030770831259045256500780172201700991903731462127889056197059687104537522308253916896586134920139621240925839777944573555991502406094821151770186841546296972634725726064307597024635191235004101797346454913921835172436564292866695233794138358007390640514359332189054283113226387908016701088600430272559324670888490466730465704828999418041654581354979268647710615309862156579682124436053380271759405977522197896980152697843330785810488329165540437284575151838303881393815638523059005021203664922115788385444888797525019676404920306205566575247280905565233436736417501371189967937340179564082745590970208"
    ]
    
    for i, number in enumerate(test_numbers):
        print(f"\nTesting with phi-harmonic number {i+1}:")
        print(f"Number: {number[:50]}... ({len(number)} digits)")
        
        # Time the visualization process
        start_time = time.time()
        
        # Generate a comprehensive visualization report
        report_dir = os.path.join(output_dir, f"number_{i+1}")
        os.makedirs(report_dir, exist_ok=True)
        
        try:
            report = visualizer.generate_quantum_visualization_report(number, report_dir)
            
            # Print report details
            print(f"\nVisualization report generated in {time.time() - start_time:.2f} seconds")
            print(f"Report location: {report['report']}")
            
            # Print visualization paths
            for key, path in report.items():
                if key != 'report' and not key.endswith('_error'):
                    print(f"- {key}: {path}")
            
            # Print any errors
            errors = {k: v for k, v in report.items() if k.endswith('_error')}
            if errors:
                print("\nErrors encountered:")
                for k, v in errors.items():
                    print(f"- {k.replace('_error', '')}: {v}")
        
        except Exception as e:
            print(f"Error generating visualization report: {e}")

def test_individual_visualizations():
    """
    Test individual visualization methods.
    """
    print("\n" + "=" * 80)
    print("TESTING INDIVIDUAL VISUALIZATION METHODS")
    print("=" * 80)
    
    # Create output directory
    output_dir = "quantum_visualization_results/individual"
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize the quantum analyzer and visualizer
    quantum_analyzer = QuantumResonanceAnalyzer()
    visualizer = HyperDimensionalVisualizer(quantum_analyzer, dimensions=5)
    
    # Test number
    number = "1618033988749894848204586834365638117720309179805762862135448622705260462818902449707207204189391137484754088075386891752126633862223536931793180060766726354433389086595939582905638322661319928290267880675208766892501711696207032221043216269548626296313614438149758701220340805887954454749246185695364864449241044320771344947049565846788509874339442212544877066478091588460749988712400765217057517978834166256249407589069704000281210427621771117778053153171410117046665991466979873176135600670874807101317952368942752194843530614433039449576485930594983782603621381589221865256989930816299144873708661568335886846509371401804503736832042381597731939526294317529196029680893094771432357266700295431108023288661764441559561004493980736273087564379515434594187725847316047576504481327807244770689632348937287337330203626588535746646743381150531016336322462745749225524817991791950313992030770831259045256500780172201700991903731462127889056197059687104537522308253916896586134920139621240925839777944573555991502406094821151770186841546296972634725726064307597024635191235004101797346454913921835172436564292866695233794138358007390640514359332189054283113226387908016701088600430272559324670888490466730465704828999418041654581354979268647710615309862156579682124436053380271759405977522197896980152697843330785810488329165540437284575151838303881393815638523059005021203664922115788385444888797525019676404920306205566575247280905565233436736417501371189967937340179564082745590970208"
    
    # Test hyper-dimensional visualization
    print("\nTesting hyper-dimensional visualization:")
    try:
        output_file = os.path.join(output_dir, "hyper_dimensional_test.png")
        result = visualizer.visualize_in_higher_dimensions(number, output_file)
        print(f"Visualization saved to: {result}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test quantum circuit visualization
    print("\nTesting quantum circuit visualization:")
    try:
        output_file = os.path.join(output_dir, "quantum_circuit_test.png")
        result = visualizer.visualize_quantum_circuit(number, output_file)
        print(f"Visualization saved to: {result}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test entanglement visualization
    print("\nTesting entanglement visualization:")
    try:
        # Create a second number by multiplying by phi
        mpf_number = mpmath.mpf(number)
        number2 = str(mpf_number * mpmath.phi)
        
        output_file = os.path.join(output_dir, "entanglement_test.png")
        result = visualizer.visualize_entanglement(number, number2, output_file)
        print(f"Visualization saved to: {result}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    """
    Main function to run all tests.
    """
    # Test the Hyper-Dimensional Visualizer
    test_hyper_dimensional_visualizer()
    
    # Test individual visualization methods
    test_individual_visualizations()
    
    print("\nAll tests completed.")

if __name__ == "__main__":
    main()
