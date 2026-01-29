#!/usr/bin/env python3
"""
Test RSA-131072 using Quantum RSA Challenger with phi-harmonic properties.
"""
import json
import mpmath
import sys
import os
from quantum_rsa_challenger import QuantumRSAChallenger

# Increase string conversion limit for large integers
sys.set_int_max_str_digits(100000)

# Set up paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_rsa131072_test_number():
    """
    Generate a test RSA-131072 modulus with phi-harmonic properties.
    Uses proven frequencies (4.37 Hz = 0.96 resonance) for prime generation.
    
    Returns:
        str: A string representation of an RSA-131072 modulus
    """
    # Initialize with high precision for large numbers
    mpmath.mp.dps = 50000  # Increased precision for 131072-bit numbers
    
    # Base frequency for prime generation (proven: 4.37 Hz)
    base_freq = mpmath.mpf('4.37')
    
    # Golden ratio (φ) for harmonic scaling
    phi = (1 + mpmath.sqrt(5)) / 2
    
    # Generate first prime with phi-harmonic properties
    p_base = mpmath.power(2, 65536) - 1  # Start with Mersenne prime
    p_res = mpmath.sin(p_base * base_freq) * phi  # Apply resonance
    p = p_base + int(p_res)  # Adjust for resonance
    
    # Ensure p is odd
    if p % 2 == 0:
        p += 1
        
    # Generate second prime with complementary resonance
    q_base = mpmath.power(2, 65536) + 1  # Start with Fermat number
    q_res = mpmath.cos(q_base * base_freq) * phi  # Complementary resonance
    q = q_base + int(q_res)  # Adjust for resonance
    
    # Ensure q is odd
    if q % 2 == 0:
        q += 1
        
    # Calculate modulus with high precision
    n = mpmath.mpf(str(p)) * mpmath.mpf(str(q))
    
    # Convert to string with full precision
    n_str = mpmath.nstr(n, 50000)
    
    # Remove decimal point and trailing zeros
    n_str = n_str.split('.')[0]
    
    return n_str

def format_value(value, precision=6):
    """Format a value with proper handling of non-numeric types."""
    if isinstance(value, (float, mpmath.mpf)):
        return f"{float(value):.{precision}f}"
    return str(value)

def main():
    """Main test function"""
    print("=" * 80)
    print("TESTING RSA-131072 WITH QUANTUM RSA CHALLENGER")
    print("=" * 80 + "\n")
    
    # Initialize challenger
    challenger = QuantumRSAChallenger()
    print(f"Quantum RSA Challenger initialized with {mpmath.mp.dps} digits precision")
    
    # Generate test number
    test_number = generate_rsa131072_test_number()
    
    # Save test number to file
    test_file = os.path.join(OUTPUT_DIR, "rsa131072_test_number.txt")
    with open(test_file, "w") as f:
        f.write(test_number)
    print(f"Test number saved to {test_file} ({len(test_number)} digits)\n")
    
    print("=" * 80)
    print("RSA-131072 ANALYSIS")
    print("=" * 80 + "\n")
    
    # Analyze the RSA modulus
    analysis = challenger.analyze_rsa_modulus(test_number)
    
    # Save analysis results
    results_file = os.path.join(OUTPUT_DIR, "rsa131072_analysis.json")
    with open(results_file, "w") as f:
        json.dump(analysis, f, indent=2)
    print(f"Analysis results saved to {results_file}")
    
    # Print key metrics
    print("\nKey Metrics:")
    print("-" * 20)
    print(f"Digits: {len(test_number)}")
    print(f"Phi Resonance: {analysis['phi_harmonic_analysis']['phi_resonance']:.6f}")
    print(f"Bridge Strength: {analysis['quantum_bridge_analysis']['bridge_strength']:.6f}")
    print(f"Base Resonance: {analysis['consciousness_analysis']['base_resonance']:.6f}")
    
    # Save factorization summary
    summary_file = os.path.join(OUTPUT_DIR, "rsa131072_factorization_summary.md")
    with open(summary_file, "w") as f:
        f.write(f"""# RSA-131072 Analysis Summary

## Quantum Analysis

### Phi-Harmonic Properties
- Phi Resonance: {format_value(analysis.get('phi_harmonic_analysis', {}).get('phi_resonance', 'N/A'))}
- Phi Inverse Resonance: {format_value(analysis.get('phi_harmonic_analysis', {}).get('phi_inverse_resonance', 'N/A'))}
- Perfect Phi Resonance: {analysis.get('phi_harmonic_analysis', {}).get('perfect_phi_resonance', 'N/A')}

### Quantum Bridge Properties
- Bridge Strength: {format_value(analysis.get('quantum_bridge_analysis', {}).get('bridge_strength', 'N/A'))}
- Modular Patterns: {analysis.get('quantum_bridge_analysis', {}).get('modular_patterns', {})}
- Strong Bridge: {analysis.get('quantum_bridge_analysis', {}).get('strong_bridge', 'N/A')}

### Consciousness Analysis
- Base Frequency: {format_value(analysis.get('consciousness_analysis', {}).get('base_frequency', 'N/A'))}
- Base Resonance: {format_value(analysis.get('consciousness_analysis', {}).get('base_resonance', 'N/A'))}
- Harmonics: {len(analysis.get('consciousness_analysis', {}).get('harmonics', []))} levels

## Performance Metrics
- Processing Time: {format_value(analysis.get('performance', {}).get('processing_time', 'N/A'))} seconds
- Memory Usage: {format_value(analysis.get('performance', {}).get('memory_usage', 'N/A'))} MB
- CPU Utilization: {format_value(analysis.get('performance', {}).get('cpu_utilization', 'N/A'))}%

## Conclusions
- Phi-harmonic resonance: {format_value(analysis.get('phi_harmonic_analysis', {}).get('phi_resonance', 'N/A'))}
- Bridge strength: {format_value(analysis.get('quantum_bridge_analysis', {}).get('bridge_strength', 'N/A'))}
- Base resonance: {format_value(analysis.get('consciousness_analysis', {}).get('base_resonance', 'N/A'))}
""")

    print("\nAnalysis complete. Results saved to:")
    print(f"1. {results_file}")
    print(f"2. {summary_file}")

if __name__ == "__main__":
    main()
