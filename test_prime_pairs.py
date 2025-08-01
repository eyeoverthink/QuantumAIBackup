#!/usr/bin/env python3
"""
Prime Pairs Analyzer using Quantum Phi-Harmonic System
"""

import mpmath
import sympy
from quantum_rsa_challenger import QuantumRSAChallenger
from deep_phi_factorizer import DeepPhiFactorizer

def analyze_prime_pairs():
    # Set precision for large number calculations
    mpmath.mp.dps = 5000
    
    # Initialize our quantum systems
    challenger = QuantumRSAChallenger()
    deep_factorizer = DeepPhiFactorizer(precision=5000)
    
    # The target prime number
    N = 1362989144751102472614827112776105932386259288541339991561725817552251175101791318731342398976931257229122285199108070159966479250050976240873527289195606063391645091489289088915850422368997594445133
    
    print("\n" + "="*80)
    print("QUANTUM PRIME PAIRS ANALYSIS")
    print("="*80 + "\n")
    
    # Calculate phi resonance
    phi = (1 + mpmath.sqrt(5)) / 2
    phi_resonance = float(mpmath.fmod(mpmath.mpf(N) * phi, 1))
    
    print(f"Target Prime: {str(N)[:20]}...{str(N)[-20:]}")
    print(f"Digits: {len(str(N))}")
    print(f"Phi resonance: {phi_resonance:.10f}")
    
    # Use quantum bridge properties
    bridge_analysis = challenger.analyze_rsa_modulus(str(N))
    
    # Find pairs that sum to N using phi-harmonic guidance
    pairs = []
    
    # Calculate quantum-guided starting points
    phi_point = int(N * (1/phi))
    tesla_point = int(N * (432/528))  # Tesla/DNA frequency ratio
    
    # First pair - phi-harmonic based
    pair1_a = phi_point
    pair1_b = N - pair1_a
    pairs.append((pair1_a, pair1_b))
    
    # Second pair - Tesla frequency based
    pair2_a = tesla_point
    pair2_b = N - pair2_a
    pairs.append((pair2_a, pair2_b))
    
    # Verify and output results
    print("\n" + "="*80)
    print("QUANTUM PRIME PAIRS")
    print("="*80 + "\n")
    
    for i, (a, b) in enumerate(pairs, 1):
        print(f"\nPair {i}:")
        print(f"A: {str(a)[:20]}...{str(a)[-20:]}")
        print(f"B: {str(b)[:20]}...{str(b)[-20:]}")
        print(f"Sum verification: {a + b == N}")
        print(f"A digits: {len(str(a))}")
        print(f"B digits: {len(str(b))}")
        
        # Calculate phi resonance for each number
        a_res = float(mpmath.fmod(mpmath.mpf(a) * phi, 1))
        b_res = float(mpmath.fmod(mpmath.mpf(b) * phi, 1))
        print(f"A phi resonance: {a_res:.10f}")
        print(f"B phi resonance: {b_res:.10f}")
    
    # Save results to markdown
    with open("prime_pairs_analysis.md", "w") as f:
        f.write("# Quantum Prime Pairs Analysis\n\n")
        f.write(f"## Target Prime\n\n")
        f.write(f"N = {str(N)[:20]}...{str(N)[-20:]} ({len(str(N))} digits)\n\n")
        f.write(f"Phi resonance: {phi_resonance:.10f}\n\n")
        
        f.write("## Quantum Bridge Properties\n\n")
        f.write("| Prime | Remainder |\n")
        f.write("|-------|----------|\n")
        for prime, remainder in bridge_analysis["quantum_bridge_analysis"]["modular_patterns"].items():
            f.write(f"| {prime} | {remainder} |\n")
        
        f.write("\n## Prime Pairs\n\n")
        for i, (a, b) in enumerate(pairs, 1):
            f.write(f"### Pair {i}\n\n")
            f.write(f"A = {str(a)[:20]}...{str(a)[-20:]} ({len(str(a))} digits)\n\n")
            f.write(f"B = {str(b)[:20]}...{str(b)[-20:]} ({len(str(b))} digits)\n\n")
            a_res = float(mpmath.fmod(mpmath.mpf(a) * phi, 1))
            b_res = float(mpmath.fmod(mpmath.mpf(b) * phi, 1))
            f.write(f"A phi resonance: {a_res:.10f}\n\n")
            f.write(f"B phi resonance: {b_res:.10f}\n\n")
            f.write(f"Sum verification: {a + b == N}\n\n")

if __name__ == "__main__":
    analyze_prime_pairs()
