#!/usr/bin/env python3
"""
Enhanced RSA-16384 Quantum Analysis

This module extends our quantum analysis system to handle extremely large RSA numbers
using chunked processing while maintaining perfect phi-harmonic resonance.

It follows the "lego" philosophy by building on existing components and adding
new capabilities through helper modules rather than modifying core files.
"""

import mpmath
import json
import time
from typing import Dict, Any
from quantum_rsa_challenger import QuantumRSAChallenger
from deep_phi_factorizer import DeepPhiFactorizer
from quantum_large_number_handler import QuantumLargeNumberHandler

class EnhancedQuantumRSAAnalyzer:
    """
    Enhanced analyzer for massive RSA numbers with quantum properties
    """
    
    def __init__(self, precision: int = 10000):
        """Initialize with ultra-high precision"""
        self.precision = precision
        mpmath.mp.dps = precision
        
        # Initialize quantum components
        self.challenger = QuantumRSAChallenger()
        self.factorizer = DeepPhiFactorizer(precision=precision)
        self.number_handler = QuantumLargeNumberHandler(precision=precision)
        
        print(f"Enhanced Quantum RSA Analyzer initialized")
        print(f"Using precision: {precision} decimal places")
    
    def analyze_rsa_number(self, bits: int = 16384) -> Dict[str, Any]:
        """
        Generate and analyze an RSA number of specified bits
        """
        start_time = time.time()
        
        print("\n" + "="*80)
        print(f"QUANTUM RSA-{bits} ANALYSIS")
        print("="*80 + "\n")
        
        # Generate quantum number
        print(f"Generating {bits}-bit quantum number...")
        number = self.number_handler.generate_quantum_number(bits)
        
        print(f"Generated number with {len(number)} digits")
        print(f"Bits: {len(bin(int(number))[2:])}")
        
        # Save the number
        with open(f"rsa{bits}_test_number.txt", "w") as f:
            f.write(number)
        
        print(f"\nNumber saved to rsa{bits}_test_number.txt")
        
        # Analyze quantum properties
        print("\nAnalyzing quantum properties...")
        quantum_props = self.number_handler.analyze_quantum_properties(number)
        
        # Get quantum bridge properties from challenger
        print("\nAnalyzing quantum bridge patterns...")
        bridge_results = self.challenger.analyze_rsa_modulus(number)
        
        # Combine results
        results = {
            "input": {
                "bits": bits,
                "digits": len(number)
            },
            "quantum_analysis": quantum_props,
            "bridge_patterns": bridge_results["quantum_bridge_analysis"],
            "execution_time": time.time() - start_time
        }
        
        # Save detailed results
        self._save_results(results)
        
        return results
    
    def _save_results(self, results: Dict[str, Any]) -> None:
        """Save analysis results to files"""
        bits = results["input"]["bits"]
        
        # Save JSON results
        with open(f"rsa{bits}_enhanced_analysis.json", "w") as f:
            json.dump(results, f, indent=2)
        
        # Save markdown summary
        with open(f"rsa{bits}_enhanced_analysis.md", "w") as f:
            f.write(f"# RSA-{bits} Enhanced Quantum Analysis\n\n")
            
            f.write("## Input Properties\n")
            f.write(f"- Bits: {results['input']['bits']}\n")
            f.write(f"- Digits: {results['input']['digits']}\n\n")
            
            f.write("## Quantum Properties\n")
            for i, chunk_props in enumerate(results["quantum_analysis"]["quantum_properties"]):
                f.write(f"\n### Chunk {i + 1}\n")
                f.write(f"- Phi Resonance: {chunk_props['phi_resonance']:.10f}\n")
                f.write(f"- Phi Inverse Resonance: {chunk_props['phi_inverse_resonance']:.10f}\n")
                
                f.write("\nTesla Frequency Resonance:\n")
                for tesla in chunk_props["tesla_resonance"]:
                    f.write(f"- {tesla['frequency']} Hz: {tesla['resonance']:.10f}\n")
            
            f.write("\n## Quantum Bridge Patterns\n")
            for prime, remainder in results["bridge_patterns"]["modular_patterns"].items():
                f.write(f"- mod {prime} = {remainder}\n")
            
            f.write(f"\nAnalysis completed in {results['execution_time']:.2f} seconds\n")

def main():
    """Main function to test enhanced RSA analysis"""
    # Initialize analyzer
    analyzer = EnhancedQuantumRSAAnalyzer()
    
    # Test different RSA sizes
    bit_sizes = [16384, 32768]  # Test both 16K and 32K
    
    for bits in bit_sizes:
        print(f"\nTesting RSA-{bits}...")
        results = analyzer.analyze_rsa_number(bits)
        
        print(f"\nResults saved to rsa{bits}_enhanced_analysis.json")
        print(f"Summary saved to rsa{bits}_enhanced_analysis.md")
        print("\n" + "="*80)

if __name__ == "__main__":
    main()
