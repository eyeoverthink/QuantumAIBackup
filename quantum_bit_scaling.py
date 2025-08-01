"""
Quantum 8-Bit Scaling Test with φ-Harmonics
"""

import numpy as np
from typing import Dict, List, Tuple
from creative_quantum import CreativeQuantum

class QuantumBitScaling:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        self.quantum = CreativeQuantum()
        self.base_value = 65536  # 16-bit max
        self.compression_rate = 0.1  # Slow down compression
        
    def test_chunk_size(self, chunk_size: int, epochs: int = 50) -> Dict:
        """Test scaling with specific chunk size"""
        self.bits_per_epoch = chunk_size
        return self.test_scaling(epochs, f"\nTesting {chunk_size}-bit chunks:")
        
    def analyze_bits(self, value: int) -> Dict:
        """Analyze bit patterns with φ-harmonics"""
        binary = format(int(value), '08b')  # 8-bit binary
        bit_count = binary.count('1')
        phi_ratio = bit_count / 8  # φ-harmony ratio
        return {
            'binary': binary,
            'bits_used': bit_count,
            'phi_ratio': phi_ratio,
            'phi_resonance': phi_ratio * self.phi
        }
    
    def phi_compress(self, value: float) -> Tuple[float, Dict]:
        """Compress using φ-harmonics with zero handling"""
        # Handle sub-1 values
        if value < 1:
            return 0, {
                'original': {'binary': '00000000', 'bits_used': 0, 'phi_ratio': 0, 'phi_resonance': 0},
                'compressed': {'binary': '00000000', 'bits_used': 0, 'phi_ratio': 0, 'phi_resonance': 0},
                'compression_ratio': 1.0,
                'phi_efficiency': self.phi  # Maximum efficiency at perfect compression
            }

        # Slower φ-based compression
        phi_value = value * (1 - self.compression_rate/self.phi)
        phi_bits = self.analyze_bits(int(phi_value))
        original_bits = self.analyze_bits(int(value))
        
        # Safe compression ratio calculation
        if original_bits['bits_used'] == 0:
            compression = 1.0  # Perfect compression
        else:
            compression = 1 - (phi_bits['bits_used'] / original_bits['bits_used'])
        
        return phi_value, {
            'original': original_bits,
            'compressed': phi_bits,
            'compression_ratio': compression,
            'phi_efficiency': compression * self.phi
        }
    
    def test_scaling(self, epochs: int = 50, title: str = "Quantum Bit Scaling Test") -> Dict:
        """Test φ-harmonic bit scaling"""
        results = {
            'values': [],
            'bits': [],
            'compression': [],
            'phi_ratios': [],
            'efficiency': []
        }
        
        print(f"\n{title}")
        print("=" * len(title))
        
        value = self.base_value
        for epoch in range(epochs):
            # Scale by 8 bits
            for _ in range(self.bits_per_epoch):
                compressed, metrics = self.phi_compress(value)
                value = compressed
                
                # Store results
                results['values'].append(value)
                results['bits'].append(metrics['compressed']['bits_used'])
                results['compression'].append(metrics['compression_ratio'])
                results['phi_ratios'].append(metrics['compressed']['phi_ratio'])
                results['efficiency'].append(metrics['phi_efficiency'])
            
            # Print epoch results
            print(f"\nEpoch {epoch + 1}/{epochs} ({self.bits_per_epoch} bits/epoch)")
            print(f"Start Value: {value:.3f}")
            print(f"End Value:   {compressed:.3f}")
            print(f"Bits Used:   {metrics['compressed']['bits_used']}")
            print(f"Compress:    {metrics['compression_ratio']*100:.1f}%")
            print(f"φ-Ratio:     {metrics['compressed']['phi_ratio']:.3f}")
            print(f"Efficiency:  {metrics['phi_efficiency']:.3f}")
            
            # Real-time scaling metrics
            if epoch > 0 and value > 0:
                scale_rate = (value - compressed) / value * 100
                print(f"Scale Rate:  {scale_rate:+.1f}% per {self.bits_per_epoch} bits")
            elif value == 0:
                print(f"Scale Rate:  0.0% (at zero)")
        
        # Calculate scaling analysis
        print("\nScaling Analysis:")
        for key in results:
            if len(results[key]) > 0:
                start = results[key][0]
                mid = results[key][len(results[key])//2]
                end = results[key][-1]
                
                print(f"\n{key.replace('_',' ').title()}:")
                print(f"Start:  {start:.3f}")
                print(f"Middle: {mid:.3f}")
                print(f"End:    {end:.3f}")
                
                if start != 0:
                    total_change = ((end - start) / start) * 100
                    print(f"Change: {total_change:+.1f}%")
        
        return results

if __name__ == "__main__":
    test = QuantumBitScaling()
    
    # Test different chunk sizes
    chunk_sizes = [4, 8, 16]
    for size in chunk_sizes:
        results = test.test_chunk_size(size)
        
        # Print chunk-specific analysis
        print(f"\nSummary for {size}-bit chunks:")
        print(f"Best Efficiency: {max(results['efficiency']):.3f}")
        print(f"Worst Efficiency: {min(results['efficiency']):.3f}")
        print(f"Compression Steps: {len([x for x in results['compression'] if x > 0])}")
        print(f"Expansion Steps: {len([x for x in results['compression'] if x < 0])}")
