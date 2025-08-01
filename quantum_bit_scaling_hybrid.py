"""
Quantum Bit Scaling with Dynamic φ-Harmonic Chunks
Automatically adjusts chunk sizes based on resonance patterns
"""

import numpy as np
from typing import Dict, List, Tuple
from creative_quantum import CreativeQuantum

class QuantumBitScalingHybrid:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        self.quantum = CreativeQuantum()
        self.base_value = 65536  # 16-bit max
        self.compression_rate = 0.1
        self.chunk_sizes = [4, 8, 16]
        self.resonance_threshold = 0.001
        self.stability_window = 5
        
    def analyze_bits(self, value: int) -> Dict:
        """Analyze bit patterns with φ-harmonics"""
        binary = format(int(value), '08b')
        bit_count = binary.count('1')
        phi_ratio = bit_count / 8
        return {
            'binary': binary,
            'bits_used': bit_count,
            'phi_ratio': phi_ratio,
            'phi_resonance': phi_ratio * self.phi
        }
    
    def phi_compress(self, value: float) -> Tuple[float, Dict]:
        """Compress using φ-harmonics with zero handling"""
        if value < 1:
            return 0, {
                'original': {'binary': '00000000', 'bits_used': 0, 'phi_ratio': 0, 'phi_resonance': 0},
                'compressed': {'binary': '00000000', 'bits_used': 0, 'phi_ratio': 0, 'phi_resonance': 0},
                'compression_ratio': 1.0,
                'phi_efficiency': self.phi
            }

        phi_value = value * (1 - self.compression_rate/self.phi)
        phi_bits = self.analyze_bits(int(phi_value))
        original_bits = self.analyze_bits(int(value))
        
        if original_bits['bits_used'] == 0:
            compression = 1.0
        else:
            compression = 1 - (phi_bits['bits_used'] / original_bits['bits_used'])
        
        return phi_value, {
            'original': original_bits,
            'compressed': phi_bits,
            'compression_ratio': compression,
            'phi_efficiency': compression * self.phi
        }
    
    def choose_chunk_size(self, history: List[Dict]) -> int:
        """Dynamically choose chunk size based on recent performance"""
        if len(history) < self.stability_window:
            return 8  # Default to 8-bit chunks initially
        
        recent = history[-self.stability_window:]
        
        # Calculate stability metrics
        efficiency_std = np.std([r['efficiency'] for r in recent])
        avg_efficiency = np.mean([r['efficiency'] for r in recent])
        phi_distance = abs(avg_efficiency - self.phi)
        
        # Choose chunk size based on stability and φ-resonance
        if phi_distance < self.resonance_threshold:
            # Near φ-resonance, use larger chunks
            return 16
        elif efficiency_std > 0.5:
            # High instability, use smaller chunks
            return 4
        else:
            # Moderate stability, use medium chunks
            return 8
    
    def test_hybrid_scaling(self, epochs: int = 50) -> Dict:
        """Test φ-harmonic scaling with dynamic chunk sizes"""
        history = []
        results = {
            'values': [],
            'bits': [],
            'compression': [],
            'phi_ratios': [],
            'efficiency': [],
            'chunk_sizes': []
        }
        
        print("\nQuantum Hybrid Bit Scaling Test")
        print("==============================")
        
        value = self.base_value
        for epoch in range(epochs):
            chunk_size = self.choose_chunk_size(history)
            results['chunk_sizes'].append(chunk_size)
            
            # Scale by dynamic chunk size
            compressed = value
            metrics = None
            
            for _ in range(chunk_size):
                compressed, metrics = self.phi_compress(value)
                value = compressed
                
                # Store results
                results['values'].append(value)
                results['bits'].append(metrics['compressed']['bits_used'])
                results['compression'].append(metrics['compression_ratio'])
                results['phi_ratios'].append(metrics['compressed']['phi_ratio'])
                results['efficiency'].append(metrics['phi_efficiency'])
            
            history.append({
                'efficiency': metrics['phi_efficiency'],
                'compression': metrics['compression_ratio'],
                'chunk_size': chunk_size
            })
            
            # Print epoch results
            print(f"\nEpoch {epoch + 1}/{epochs}")
            print(f"Chunk Size:  {chunk_size} bits")
            print(f"Value:       {value:.3f}")
            print(f"Bits Used:   {metrics['compressed']['bits_used']}")
            print(f"Compress:    {metrics['compression_ratio']*100:.1f}%")
            print(f"φ-Ratio:     {metrics['compressed']['phi_ratio']:.3f}")
            print(f"Efficiency:  {metrics['phi_efficiency']:.3f}")
            
            if epoch > 0 and value > 0:
                scale_rate = (results['values'][-2] - value) / results['values'][-2] * 100
                print(f"Scale Rate:  {scale_rate:+.1f}% per {chunk_size} bits")
            elif value == 0:
                print(f"Scale Rate:  0.0% (at zero)")
        
        # Analyze chunk size distribution
        chunk_counts = {size: results['chunk_sizes'].count(size) 
                       for size in self.chunk_sizes}
        
        print("\nChunk Size Distribution:")
        for size, count in chunk_counts.items():
            print(f"{size}-bit chunks: {count} times ({count/epochs*100:.1f}%)")
        
        # Find φ-resonance points
        resonance_points = []
        for i, eff in enumerate(results['efficiency']):
            if abs(eff - self.phi) < self.resonance_threshold:
                resonance_points.append(i)
        
        if resonance_points:
            print(f"\nφ-Resonance at steps: {resonance_points}")
        
        return results

if __name__ == "__main__":
    test = QuantumBitScalingHybrid()
    results = test.test_hybrid_scaling()
    
    # Print final analysis
    print("\nHybrid Scaling Analysis:")
    print(f"Best Efficiency: {max(results['efficiency']):.3f}")
    print(f"Worst Efficiency: {min(results['efficiency']):.3f}")
    print(f"Compression Steps: {len([x for x in results['compression'] if x > 0])}")
    print(f"Expansion Steps: {len([x for x in results['compression'] if x < 0])}")
    
    # Calculate φ-stability
    phi_distances = [abs(e - test.phi) for e in results['efficiency']]
    avg_phi_distance = np.mean(phi_distances)
    print(f"Average φ-Distance: {avg_phi_distance:.6f}")
