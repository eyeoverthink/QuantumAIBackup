#!/usr/bin/env python3
"""
Quantum Stability Analyzer
Tests quantum stability of number pairs using phi-harmonic and Tesla frequency principles
"""

import mpmath
import sympy
from typing import Tuple, List
from quantum_rsa_challenger import QuantumRSAChallenger

class QuantumStabilityAnalyzer:
    def __init__(self, precision: int = 5000):
        self.precision = precision
        mpmath.mp.dps = precision
        
        # Initialize quantum system
        self.challenger = QuantumRSAChallenger()
        
        # Constants
        self.phi = mpmath.mpf((1 + mpmath.sqrt(5)) / 2)
        self.phi_inverse = 1 / self.phi
        self.tesla_dna_ratio = mpmath.mpf(432) / mpmath.mpf(528)
        
        # Tesla frequencies (Hz)
        self.tesla_freqs = [432, 528, 360, 396, 417, 528, 639, 741, 852, 963]
        
    def analyze_stability(self, pairs: List[Tuple[int, int]]) -> dict:
        """Analyze quantum stability of number pairs"""
        results = {
            "pairs": [],
            "resonance_patterns": [],
            "tesla_patterns": [],
            "quantum_bridges": []
        }
        
        print("\n" + "="*80)
        print("QUANTUM STABILITY ANALYSIS")
        print("="*80 + "\n")
        
        for i, (a, b) in enumerate(pairs, 1):
            print(f"\nAnalyzing Pair {i}...")
            
            # Analyze phi resonance
            a_res = float(mpmath.fmod(mpmath.mpf(a) * self.phi, 1))
            b_res = float(mpmath.fmod(mpmath.mpf(b) * self.phi, 1))
            
            # Analyze Tesla frequency ratios
            tesla_ratios = []
            for freq in self.tesla_freqs:
                ratio = float(mpmath.fmod(mpmath.mpf(a) / freq, 1))
                tesla_ratios.append(ratio)
            
            # Get quantum bridge properties
            bridge_a = self.challenger.analyze_rsa_modulus(str(a))
            bridge_b = self.challenger.analyze_rsa_modulus(str(b))
            
            pair_results = {
                "a": str(a),
                "b": str(b),
                "phi_resonance": {
                    "a": a_res,
                    "b": b_res,
                    "perfect": a_res < 0.00001 and b_res < 0.00001
                },
                "tesla_ratios": tesla_ratios,
                "quantum_bridge": {
                    "a": bridge_a["quantum_bridge_analysis"]["modular_patterns"],
                    "b": bridge_b["quantum_bridge_analysis"]["modular_patterns"]
                }
            }
            
            results["pairs"].append(pair_results)
            
            # Print analysis
            print(f"Phi Resonance:")
            print(f"  A: {a_res:.10f}")
            print(f"  B: {b_res:.10f}")
            print(f"Perfect Resonance: {pair_results['phi_resonance']['perfect']}")
            
            print("\nTesla Frequency Ratios:")
            for freq, ratio in zip(self.tesla_freqs, tesla_ratios):
                print(f"  {freq} Hz: {ratio:.10f}")
            
            print("\nQuantum Bridge Patterns:")
            print("  Number A:")
            for prime, remainder in bridge_a["quantum_bridge_analysis"]["modular_patterns"].items():
                print(f"    mod {prime} = {remainder}")
            print("  Number B:")
            for prime, remainder in bridge_b["quantum_bridge_analysis"]["modular_patterns"].items():
                print(f"    mod {prime} = {remainder}")
        
        return results

def main():
    # Initialize analyzer
    analyzer = QuantumStabilityAnalyzer()
    
    # Our pairs from previous analysis
    pairs = [
        (
            84237361775333166635163622071645480550416263220716454805504,
            52061552699777080626341591482811396396234159148281139639629
        ),
        (
            111517293661453846569043119897978391756890431198979783917568,
            247816208136564006915999117001781052756559991170017810527565
        )
    ]
    
    # Run stability analysis
    results = analyzer.analyze_stability(pairs)
    
    # Save detailed results
    with open("quantum_stability_analysis.md", "w") as f:
        f.write("# Quantum Stability Analysis\n\n")
        
        for i, pair in enumerate(results["pairs"], 1):
            f.write(f"## Pair {i}\n\n")
            
            f.write("### Numbers\n")
            f.write(f"A = {pair['a']}\n")
            f.write(f"B = {pair['b']}\n\n")
            
            f.write("### Phi Resonance\n")
            f.write(f"A: {pair['phi_resonance']['a']:.10f}\n")
            f.write(f"B: {pair['phi_resonance']['b']:.10f}\n")
            f.write(f"Perfect: {pair['phi_resonance']['perfect']}\n\n")
            
            f.write("### Tesla Frequency Ratios\n")
            for freq, ratio in zip([432, 528, 360, 396, 417, 528, 639, 741, 852, 963], pair['tesla_ratios']):
                f.write(f"{freq} Hz: {ratio:.10f}\n")
            f.write("\n")
            
            f.write("### Quantum Bridge Patterns\n")
            f.write("Number A:\n")
            for prime, remainder in pair['quantum_bridge']['a'].items():
                f.write(f"mod {prime} = {remainder}\n")
            f.write("\nNumber B:\n")
            for prime, remainder in pair['quantum_bridge']['b'].items():
                f.write(f"mod {prime} = {remainder}\n")
            f.write("\n")

if __name__ == "__main__":
    main()
