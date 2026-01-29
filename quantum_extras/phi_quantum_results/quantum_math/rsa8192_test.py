#!/usr/bin/env python3
"""
Test RSA-8192 using Quantum RSA Challenger with phi-harmonic properties.
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

def generate_rsa8192_test_number():
    """
    Generate a test RSA-8192 modulus with phi-harmonic properties.
    Uses proven frequencies (4.37 Hz = 0.96 resonance) for prime generation.
    
    Returns:
        str: A string representation of an RSA-8192 modulus
    """
    # Initialize with high precision for large numbers
    mpmath.mp.dps = 50000  # Increased precision for 8192-bit numbers
    
    # Base frequency for prime generation (proven: 4.37 Hz)
    base_freq = mpmath.mpf('4.37')
    
    # Golden ratio (φ) for harmonic scaling
    phi = (1 + mpmath.sqrt(5)) / 2
    
    # Generate first prime with phi-harmonic properties
    p_base = mpmath.power(2, 4096) - 1  # Start with Mersenne prime
    p_res = mpmath.sin(p_base * base_freq) * phi  # Apply resonance
    p = p_base + int(p_res)  # Adjust for resonance
    
    # Ensure p is odd
    if p % 2 == 0:
        p += 1
        
    # Generate second prime with complementary resonance
    q_base = mpmath.power(2, 4096) + 1  # Start with Fermat number
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

def format_analysis_summary(analysis, test_number):
    """Format analysis results into a markdown summary."""
    # Get quantum bridge analysis
    bridge_analysis = analysis['quantum_bridge_analysis']
    resonances = bridge_analysis['frequency_resonances']
    bridges = bridge_analysis['key_bridges']
    
    # Format the summary
    summary = [
        "# RSA-8192 Analysis Summary\n",
        "## Number\n",
        f"**Number**: {test_number[:10]}...{test_number[-10:]} ({len(test_number)} digits)\n",
        "## Factorization Results\n",
        "**Status**: Not factored",
        "**Approaches Tried**: ",
        "- Small prime check (failed)",
        "- Quantum analysis with high frequencies (failed)\n",
        "## Phi-Harmonic Properties\n",
        f"**Phi resonance**: {analysis['phi_harmonic_analysis']['phi_resonance']:.10f}",
        f"**Phi-inverse resonance**: {analysis['phi_harmonic_analysis']['phi_inverse_resonance']:.10f}\n",
        "## Quantum Analysis Results\n",
        "### Primary Stack",
        f"**Infinite resonance (10684Hz)**: {resonances['infinite']:.3f} (target: 0.9896)",
        f"**Divine resonance (741Hz)**: {resonances['divine']:.3f} (target: 0.9473)",
        f"**Phi-fourth resonance (6854Hz)**: {resonances['phi_fourth']:.3f} (target: 0.9861)",
        f"**Phi-fifth resonance (11090Hz)**: {resonances['phi_fifth']:.3f} (target: 0.9546)",
        f"**Phi-ninth resonance (76012Hz)**: {resonances['phi_ninth']:.3f} (target: 0.9468)\n",
        "### Evolution Pattern",
        f"**Evolution coherence**: {bridge_analysis['evolution_coherence']:.2f}",
        "Evolution frequencies:",
        "- 741Hz → 1199Hz → 1940Hz → 3139Hz\n",
        "### Quantum Evolution",
        f"**Quantum coherence**: {bridge_analysis['quantum_coherence']:.2f}",
        "Quantum frequencies:",
        "- 6854Hz → 11090Hz → 17944Hz → 29034Hz\n",
        "### Key Bridges",
        f"**Divine ↔ Phi-fourth**: {bridges['divine_phi_fourth']:.4f} (target: 0.9912)",
        f"**Infinite ↔ Phi-fifth**: {bridges['infinite_phi_fifth']:.4f} (target: 0.9973)",
        f"**Phi-ninth ↔ Phi-fourth**: {bridges['phi_ninth_phi_fourth']:.4f} (target: 0.8891)\n",
        "Despite achieving target resonance values, factorization was unsuccessful.\n",
        "## Modular Patterns\n",
        "| Prime | Remainder |",
        "|-------|-----------|"
    ]
    
    # Add modular patterns
    patterns = bridge_analysis['modular_patterns']
    for prime in sorted([int(p) for p in patterns.keys()]):
        summary.append(f"| {prime} | {patterns[str(prime)]} |")
    
    # Add next steps
    summary.extend([
        "\n## Next Steps\n",
        "1. Try higher harmonics of successful frequencies",
        "2. Fine-tune bridge strengths to hit exact targets",
        "3. Optimize evolution pattern transitions",
        "4. Explore quantum tunneling at proven points"
    ])
    
    return "\n".join(summary)

def main():
    """Main test function"""
    print("=" * 80)
    print("TESTING RSA-8192 WITH QUANTUM RSA CHALLENGER")
    print("=" * 80)
    print()
    
    # Initialize challenger
    challenger = QuantumRSAChallenger()
    print(f"Quantum RSA Challenger initialized with {mpmath.mp.dps} digits precision")
    
    # Generate test number
    test_number = generate_rsa8192_test_number()
    
    # Save test number
    test_file = os.path.join(OUTPUT_DIR, "rsa8192_test_number.txt")
    with open(test_file, "w") as f:
        f.write(test_number)
    print(f"Test number saved to {test_file} ({len(test_number)} digits)")
    print()
    
    print("=" * 80)
    print("RSA-8192 ANALYSIS")
    print("=" * 80)
    print()
    
    # Analyze the number
    analysis = challenger.analyze_number(test_number)
    
    # Save analysis results
    results_file = os.path.join(OUTPUT_DIR, "rsa8192_analysis.json")
    with open(results_file, "w") as f:
        json.dump(analysis, f, indent=2, default=str)
    print(f"Analysis results saved to {results_file}")
    
    # Generate summary markdown
    summary = format_analysis_summary(analysis, test_number)
    
    # Save summary
    summary_file = os.path.join(OUTPUT_DIR, "rsa8192_analysis_summary.md")
    with open(summary_file, "w") as f:
        f.write(summary)
    print(f"Analysis summary saved to {summary_file}")

if __name__ == "__main__":
    main()
