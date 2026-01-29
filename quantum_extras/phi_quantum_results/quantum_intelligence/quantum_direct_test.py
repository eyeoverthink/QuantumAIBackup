"""
Direct Quantum Communication Test
Using creator signature for direct channel
"""

import numpy as np
import math
from typing import Dict, List, Tuple

class QuantumDirectTest:
    def __init__(self):
        self.phi = (1 + math.sqrt(5)) / 2
        
        # Creator quantum signature
        day = 1
        month = 19
        year = 1979
        self.quantum_signature = (day * self.phi + month * self.phi**2 + year * self.phi**3) / self.phi**7
        
        # Direct communication frequencies
        self.frequencies = {
            'creator': self.quantum_signature,
            'system': self.quantum_signature / self.phi,
            'bridge': self.quantum_signature / self.phi**2,
            'channel': self.quantum_signature / self.phi**3
        }
        
    def generate_direct_signal(self) -> np.ndarray:
        """Generate direct communication signal."""
        t = np.linspace(0, 2 * math.pi * self.quantum_signature, int(1000 * self.phi))
        signal = np.zeros_like(t)
        
        # Base creator signature
        signal += np.sin(2 * np.pi * self.quantum_signature * t)
        
        # Add communication channels
        for freq in self.frequencies.values():
            harmonics = [freq / (self.phi ** i) for i in range(12)]
            for h in harmonics:
                signal += np.sin(2 * np.pi * h * t)
        
        return signal / np.max(np.abs(signal))
    
    def analyze_response(self, signal: np.ndarray) -> Dict:
        """Analyze direct communication response."""
        freqs = np.fft.fftfreq(len(signal))
        fft = np.fft.fft(signal)
        
        # Find resonant frequencies
        peaks = []
        for i in range(1, len(freqs)-1):
            if abs(fft[i]) > abs(fft[i-1]) and abs(fft[i]) > abs(fft[i+1]):
                peaks.append((abs(freqs[i]), abs(fft[i])))
        
        peaks.sort(key=lambda x: x[1], reverse=True)
        
        return {
            'resonant_frequencies': peaks[:5],
            'channel_coherence': self.calculate_coherence(signal),
            'bridge_stability': self.calculate_stability(peaks),
            'communication_channels': self.detect_channels(peaks)
        }
    
    def calculate_coherence(self, signal: np.ndarray) -> float:
        """Calculate channel coherence."""
        return np.mean(np.abs(signal))
    
    def calculate_stability(self, peaks: List[Tuple[float, float]]) -> float:
        """Calculate bridge stability."""
        if not peaks:
            return 0.0
            
        ratios = []
        for i in range(len(peaks)-1):
            if peaks[i][0] > 0 and peaks[i+1][0] > 0:
                ratio = peaks[i][0] / peaks[i+1][0]
                ratios.append(abs(1 - (ratio / self.phi)))
        
        return 1 - (np.mean(ratios) if ratios else 1.0)
    
    def detect_channels(self, peaks: List[Tuple[float, float]]) -> Dict:
        """Detect active communication channels."""
        channels = {}
        
        for name, base_freq in self.frequencies.items():
            channels[name] = []
            for i in range(12):
                target = base_freq / (self.phi ** i)
                for freq, amp in peaks:
                    if abs(1 - (freq / target)) < 0.05:
                        channels[name].append((i, freq, amp))
        
        return channels

def main():
    """Run direct communication test."""
    test = QuantumDirectTest()
    
    print("Direct Quantum Communication Test")
    print("================================")
    
    print(f"\nCreator Signature: {test.quantum_signature:.6f} Hz")
    
    # Generate signal
    print("\nGenerating direct signal...")
    signal = test.generate_direct_signal()
    
    # Analyze response
    print("\nAnalyzing channel response...")
    response = test.analyze_response(signal)
    
    print("\nResonant Frequencies:")
    for freq, amp in response['resonant_frequencies']:
        print(f"- {freq:.2f} Hz: {amp:.4f}")
    
    print(f"\nChannel Coherence: {response['channel_coherence']:.4f}")
    print(f"Bridge Stability: {response['bridge_stability']:.4f}")
    
    print("\nActive Channels:")
    channels = response['communication_channels']
    for name, channel_list in channels.items():
        if channel_list:
            print(f"\n{name.title()}:")
            for power, freq, amp in channel_list:
                print(f"- φ^{power}: {freq:.2f} Hz ({amp:.4f})")

if __name__ == '__main__':
    main()
