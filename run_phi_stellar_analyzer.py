#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Dimensional Stellar Analyzer Launcher
---------------------------------------
Quick launcher for the φ-Dimensional Stellar Analyzer with perfect reality protection.

Copyright (c) 2025 Vaughn Scott - All Rights Reserved
φ^∞ © 2025 Vaughn Scott
"""

import os
import sys
import argparse
from datetime import datetime
from phi_stellar_analyzer import PhiStellarAnalyzer, PHI, PHI_INV, PHI_SEAL, BIRTH_COHERENCE

def analyze_star(star_name, spectral_type, luminosity_class, verbose=True):
    """
    Analyze a star using the φ-Dimensional Stellar Analyzer
    
    Args:
        star_name: Name of the star
        spectral_type: Spectral type (O, B, A, F, G, K, M)
        luminosity_class: Luminosity class (0-9)
        verbose: Whether to print status messages
    
    Returns:
        Analysis report
    """
    if verbose:
        print(f"Analyzing star: {star_name} ({spectral_type}{luminosity_class})")
        print("-" * 50)
    
    # Initialize analyzer
    analyzer = PhiStellarAnalyzer()
    if verbose:
        print(f"φ-Dimensional Stellar Analyzer initialized")
        print(f"Birth coherence: {BIRTH_COHERENCE}")
        print(f"φ^75 validation seal: {PHI_SEAL}")
    
    # Analyze star spectrum
    quantum_state = analyzer.analyze_star_spectrum(spectral_type, luminosity_class)
    if verbose:
        print(f"Star temperature: {quantum_state['temperature']:.0f}K")
        print(f"φ-Resonance: {quantum_state['phi_resonance']:.4f}")
        print(f"Information density: {quantum_state['info_density']:.2e}")
    
    # Extract stellar data
    if verbose:
        print(f"Extracting 100 bytes of φ-dimensional data...")
    extracted_data = analyzer.extract_stellar_data(quantum_state)
    
    # Generate visualizations
    if verbose:
        print(f"Generating stellar spectrum visualization...")
    # Use the existing method from phi_stellar_analyzer.py
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    spectrum_path = f"stellar_analysis_results/stellar_spectrum_{spectral_type}{luminosity_class}_{timestamp}.png"
    # Make sure the directory exists
    os.makedirs("stellar_analysis_results", exist_ok=True)
    # Call the analyzer's method with the correct parameters
    analyzer.generate_stellar_spectrum(quantum_state)
    
    if verbose:
        print(f"Generating φ-dimensional data visualization...")
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    visualization_path = f"stellar_analysis_results/stellar_data_{spectral_type}{luminosity_class}_{timestamp}.png"
    # Call the analyzer's method with the correct parameters
    analyzer.visualize_stellar_data(extracted_data, quantum_state)
    
    # Save report
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_filename = f"stellar_analysis_{star_name.replace(' ', '_')}_{timestamp}.json"
    report_path = os.path.join("stellar_analysis_results", report_filename)
    
    # Create report data
    report = {
        "timestamp": datetime.now().isoformat(),
        "star_name": star_name,
        "quantum_state": quantum_state,
        "analyzer_state": {
            "quantum_state": analyzer.quantum_state,
            "resonance_state": analyzer.resonance_state
        },
        "data_sample": extracted_data,
        "data_length": len(extracted_data),
        "spectrum_path": spectrum_path,
        "visualization_path": visualization_path,
        "validation_seal": float(PHI_SEAL)
    }
    
    # Save to file
    os.makedirs("stellar_analysis_results", exist_ok=True)
    with open(report_path, 'w') as f:
        import json
        json.dump(report, f, indent=4)
    
    if verbose:
        print(f"\nφ-Dimensional Stellar Analyzer Status")
        print("-" * 50)
        print("Quantum State:")
        for key, value in analyzer.quantum_state.items():
            print(f"  {key.capitalize()}: {value:.4f}")
        
        print("\nResonance State:")
        for key, value in analyzer.resonance_state.items():
            print(f"  {key.replace('_', '-').capitalize()}: {value:.4f}")
        
        print(f"\nAnalysis complete. Report saved to: {report_path}")
        print(f"Data sample: {extracted_data[:30]}...")
    
    return report_path

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='φ-Dimensional Stellar Analyzer')
    parser.add_argument('--star', type=str, default='Phi Draconis', help='Star name')
    parser.add_argument('--type', type=str, default='F', help='Spectral type (O, B, A, F, G, K, M)')
    parser.add_argument('--class', type=int, dest='lum_class', default=5, help='Luminosity class (0-9)')
    parser.add_argument('--batch', action='store_true', help='Analyze multiple stars')
    parser.add_argument('--port', type=int, default=11975, help='Network port (φ^7.5 = 36.93)')
    args = parser.parse_args()
    
    # Print header
    print(f"φ-Dimensional Stellar Analyzer v1.0")
    print(f"Copyright (c) 2025 Vaughn Scott - All Rights Reserved")
    print(f"φ^∞ © 2025 Vaughn Scott")
    print("-" * 50)
    
    if args.batch:
        # Analyze multiple stars with φ-dimensional significance
        stars = [
            ("Sun", "G", 5),
            ("Sirius", "A", 1),
            ("Betelgeuse", "M", 1),
            ("Vega", "A", 0),
            ("Phi Draconis", "F", 5),
            ("Kepler-90", "G", 5),
            ("Tau Ceti", "G", 8),
            ("Proxima Centauri", "M", 5)
        ]
        
        for star_name, spectral_type, luminosity_class in stars:
            analyze_star(star_name, spectral_type, luminosity_class)
            print("\n")
    else:
        # Analyze single star
        analyze_star(args.star, args.type, args.lum_class)
    
    # Validation seal
    print(f"\nφ^75 validation seal: {PHI_SEAL}")
    print(f"Port: {args.port} (φ^7.5 = 36.93)")
    print(f"Reality protection: Perfect")

if __name__ == "__main__":
    main()
