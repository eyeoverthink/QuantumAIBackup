"""
Quantum Results Analyzer
Analyzes phi-harmonic resonance patterns from JSON data
"""

import json
import math
from typing import Dict
from dataclasses import dataclass
from collections import defaultdict

class QuantumAnalyzer:
    def __init__(self, json_path: str):
        # Load quantum data
        with open(json_path, 'r') as f:
            self.data = json.load(f)
            self.quantum_system = self.data['quantum_system']
        
        # Constants
        self.phi = (1 + math.sqrt(5)) / 2
    
    def analyze_frequencies(self) -> Dict:
        """Analyze base frequency evolution."""
        frequencies = self.quantum_system['base_frequencies']
        evolution = {}
        
        for name, freq in frequencies.items():
            evolution[name] = {
                'φ⁴': freq * (self.phi ** 4),
                'φ⁷': freq * (self.phi ** 7),
                'φ¹²': freq * (self.phi ** 12),
                'φ¹⁹': freq * (self.phi ** 19)
            }
        
        return evolution
    
    def analyze_author_bridges(self) -> Dict:
        """Analyze author quantum bridges."""
        authors = self.quantum_system['author_signatures']
        bridges = {}
        
        for author, data in authors.items():
            freq = data['frequency']
            bridges[author] = {
                'frequency': freq,
                'tesla_bridge': 1 / (1 + abs(freq - self.quantum_system['base_frequencies']['tesla'])),
                'dna_bridge': 1 / (1 + abs(freq - self.quantum_system['base_frequencies']['dna'])),
                'heart_bridge': 1 / (1 + abs(freq - self.quantum_system['base_frequencies']['heart'])),
                'evolution': data['evolution']
            }
        
        return bridges
    
    def analyze_rsa_performance(self) -> Dict:
        """Analyze RSA quantum performance."""
        rsa = self.quantum_system['rsa_performance']
        performance = {}
        
        for key_size, data in rsa.items():
            performance[key_size] = {
                'resonance': {
                    'physical': data['physical_resonance'],
                    'mental': data['mental_bridge'],
                    'quantum': data['quantum_flow'],
                    'cosmic': data['cosmic_state']
                },
                'total_resonance': data['total_resonance'],
                'time': data['time'],
                'classical_estimate': data['classical_estimate']
            }
        
        return performance
    
    def analyze_consciousness(self) -> Dict:
        """Analyze consciousness evolution."""
        consciousness = self.quantum_system['consciousness_evolution']
        metrics = {}
        
        for level, data in consciousness.items():
            metrics[level] = {
                'power': data['power'],
                'dimensions': data['dimensions'],
                'resonance': data['resonance']
            }
            if 'evolution' in data:
                metrics[level]['evolution'] = data['evolution']
        
        return metrics
    
    def print_analysis(self):
        """Print comprehensive quantum analysis."""
        print("Quantum System Analysis")
        print("=====================")
        
        # Frequency Evolution
        print("\nFrequency Evolution:")
        frequencies = self.analyze_frequencies()
        for name, evol in frequencies.items():
            print(f"\n{name.title()}:")
            for power, freq in evol.items():
                print(f"{power}: {freq:.2f} Hz")
        
        # Author Bridges
        print("\nAuthor Quantum Bridges:")
        bridges = self.analyze_author_bridges()
        for author, data in bridges.items():
            print(f"\n{author.title()}:")
            print(f"Frequency: {data['frequency']} Hz")
            print(f"Tesla Bridge: {data['tesla_bridge']:.6f}")
            print(f"DNA Bridge: {data['dna_bridge']:.6f}")
            print(f"Heart Bridge: {data['heart_bridge']:.6f}")
            print(f"Evolution: {data['evolution']['start']} → {data['evolution']['end']}")
        
        # RSA Performance
        print("\nRSA Quantum Performance:")
        performance = self.analyze_rsa_performance()
        for key_size, data in performance.items():
            print(f"\n{key_size}:")
            print("Resonance:")
            for level, res in data['resonance'].items():
                print(f"- {level}: {res:.9f}")
            print(f"Total Resonance: {data['total_resonance']:.9f}")
            print(f"Time: {data['time']}")
            print(f"Classical Estimate: {data['classical_estimate']}")
        
        # Consciousness Evolution
        print("\nConsciousness Evolution:")
        consciousness = self.analyze_consciousness()
        for level, data in consciousness.items():
            print(f"\n{level.title()}:")
            print(f"Power: φ^{data['power']}")
            print(f"Dimensions: {data['dimensions']}D")
            print(f"Resonance: {data['resonance']:.9f}")
            if 'evolution' in data:
                for freq, evol in data['evolution'].items():
                    print(f"{freq}: {evol['start']} Hz → {evol['end']} Hz")

def main():
    """Run quantum analysis."""
    analyzer = QuantumAnalyzer('phi_quantum_results/quantum_results.json')
    analyzer.print_analysis()

if __name__ == '__main__':
    main()
