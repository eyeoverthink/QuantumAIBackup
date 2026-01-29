"""
Quantum Pattern Comparison Test
Comparing Tesla's system with Quantum Signature patterns
"""

import numpy as np
import math
from typing import Dict, List, Tuple

class PatternComparisonTest:
    def __init__(self):
        self.phi = (1 + math.sqrt(5)) / 2
        
        # Tesla's frequencies
        self.tesla_frequencies = {
            'unity': 432.0,
            'dna': 528.0,
            'heart': 639.0,
            'cosmic': 741.0
        }
        
        # Quantum signature (01-19-1979)
        day = 1
        month = 19
        year = 1979
        self.quantum_signature = (day * self.phi + month * self.phi**2 + year * self.phi**3) / self.phi**7
        
        # Quantum frequencies
        self.quantum_frequencies = {
            'creator': self.quantum_signature,
            'bridge': self.quantum_signature / self.phi,
            'channel': self.quantum_signature / self.phi**2,
            'gate': self.quantum_signature / self.phi**3
        }
        
    def generate_tesla_signal(self) -> np.ndarray:
        """Generate Tesla-based signal."""
        t = np.linspace(0, 2 * math.pi, 1000)
        signal = np.zeros_like(t)
        
        for freq in self.tesla_frequencies.values():
            harmonics = [freq * (self.phi ** i) for i in range(7)]
            for h in harmonics:
                signal += np.sin(2 * np.pi * h * t)
        
        return signal / np.max(np.abs(signal))
    
    def generate_quantum_signal(self) -> np.ndarray:
        """Generate Quantum signature signal."""
        t = np.linspace(0, 2 * math.pi * self.quantum_signature, int(1000 * self.phi))
        signal = np.zeros_like(t)
        
        signal += np.sin(2 * np.pi * self.quantum_signature * t)
        
        for freq in self.quantum_frequencies.values():
            harmonics = [freq / (self.phi ** i) for i in range(12)]
            for h in harmonics:
                signal += np.sin(2 * np.pi * h * t)
        
        return signal / np.max(np.abs(signal))
    
    def analyze_signal(self, signal: np.ndarray) -> Dict:
        """Analyze signal patterns."""
        freqs = np.fft.fftfreq(len(signal))
        fft = np.fft.fft(signal)
        
        peaks = []
        for i in range(1, len(freqs)-1):
            if abs(fft[i]) > abs(fft[i-1]) and abs(fft[i]) > abs(fft[i+1]):
                peaks.append((abs(freqs[i]), abs(fft[i])))
        
        peaks.sort(key=lambda x: x[1], reverse=True)
        
        return {
            'dominant_frequencies': peaks[:5],
            'coherence': self.calculate_coherence(signal),
            'stability': self.calculate_stability(peaks),
            'dimensionality': self.calculate_dimensionality(peaks)
        }
    
    def calculate_coherence(self, signal: np.ndarray) -> float:
        """Calculate signal coherence."""
        return np.mean(np.abs(signal))
    
    def calculate_stability(self, peaks: List[Tuple[float, float]]) -> float:
        """Calculate frequency stability."""
        if not peaks:
            return 0.0
            
        ratios = []
        for i in range(len(peaks)-1):
            if peaks[i][0] > 0 and peaks[i+1][0] > 0:
                ratio = peaks[i][0] / peaks[i+1][0]
                ratios.append(abs(1 - (ratio / self.phi)))
        
        return 1 - (np.mean(ratios) if ratios else 1.0)
    
    def calculate_dimensionality(self, peaks: List[Tuple[float, float]]) -> int:
        """Estimate signal dimensionality."""
        unique_ratios = set()
        for i in range(len(peaks)-1):
            for j in range(i+1, len(peaks)):
                if peaks[i][0] > 0 and peaks[j][0] > 0:
                    ratio = peaks[i][0] / peaks[j][0]
                    unique_ratios.add(round(ratio, 4))
        return len(unique_ratios)

def main():
    """Run pattern comparison test."""
    test = PatternComparisonTest()
    
    print("Pattern Comparison Test")
    print("======================")
    
    # Tesla patterns
    print("\nTesla System Patterns:")
    print("---------------------")
    tesla_signal = test.generate_tesla_signal()
    tesla_analysis = test.analyze_signal(tesla_signal)
    
    print("\nDominant Frequencies:")
    for freq, amp in tesla_analysis['dominant_frequencies']:
        print(f"- {freq:.2f} Hz: {amp:.4f}")
    
    print(f"\nCoherence: {tesla_analysis['coherence']:.4f}")
    print(f"Stability: {tesla_analysis['stability']:.4f}")
    print(f"Dimensionality: {tesla_analysis['dimensionality']}")
    
    # Quantum patterns
    print("\nQuantum System Patterns:")
    print("----------------------")
    quantum_signal = test.generate_quantum_signal()
    quantum_analysis = test.analyze_signal(quantum_signal)
    
    print("\nDominant Frequencies:")
    for freq, amp in quantum_analysis['dominant_frequencies']:
        print(f"- {freq:.2f} Hz: {amp:.4f}")
    
    print(f"\nCoherence: {quantum_analysis['coherence']:.4f}")
    print(f"Stability: {quantum_analysis['stability']:.4f}")
    print(f"Dimensionality: {quantum_analysis['dimensionality']}")

if __name__ == '__main__':
    main()
