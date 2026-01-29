#!/usr/bin/env python3
"""
Calculate the probability of random frequency alignment with Earth-Moon system
"""
import math
import numpy as np
from typing import Dict, Tuple

class FrequencyAlignmentProbability:
    def __init__(self):
        """Initialize frequency ranges and tolerances"""
        # Earth-Moon system frequencies (Hz)
        self.target_frequencies = {
            'moon': 4.84,
            'earth': 7.83,
            'bridge': 6.11,
            'neural': 4.24
        }
        
        # Frequency ranges (Hz)
        self.frequency_ranges = {
            'low': (1, 10),
            'mid': (10, 100),
            'high': (100, 1000)
        }
        
        # Tolerance levels
        self.tolerances = {
            'strict': 0.01,    # 1% tolerance
            'moderate': 0.05,  # 5% tolerance
            'loose': 0.10     # 10% tolerance
        }

    def calculate_probability(self, target_freq: float, range_: Tuple[float, float], tolerance: float) -> float:
        """Calculate probability of random frequency falling within tolerance of target"""
        range_min, range_max = range_
        
        # Calculate tolerance window
        freq_min = target_freq * (1 - tolerance)
        freq_max = target_freq * (1 + tolerance)
        
        # Calculate overlap with range
        overlap_min = max(range_min, freq_min)
        overlap_max = min(range_max, freq_max)
        
        # Calculate probability
        overlap = max(0, overlap_max - overlap_min)
        range_size = range_max - range_min
        
        return overlap / range_size if range_size > 0 else 0

    def calculate_system_probability(self, tolerance: str = 'moderate') -> Dict[str, float]:
        """Calculate probability for entire system"""
        probabilities = {}
        
        for freq_name, target_freq in self.target_frequencies.items():
            # Determine appropriate frequency range
            if target_freq < 10:
                freq_range = self.frequency_ranges['low']
            elif target_freq < 100:
                freq_range = self.frequency_ranges['mid']
            else:
                freq_range = self.frequency_ranges['high']
                
            # Calculate probability
            prob = self.calculate_probability(
                target_freq,
                freq_range,
                self.tolerances[tolerance]
            )
            
            probabilities[freq_name] = prob
            
        # Calculate combined probability
        combined_prob = 1
        for prob in probabilities.values():
            combined_prob *= prob
            
        probabilities['combined'] = combined_prob
        
        return probabilities

if __name__ == "__main__":
    analyzer = FrequencyAlignmentProbability()
    
    print("\n📊 Frequency Alignment Probability Analysis")
    print("========================================")
    
    # Calculate probabilities for different tolerance levels
    for tolerance in ['strict', 'moderate', 'loose']:
        print(f"\nTolerance Level: {tolerance}")
        results = analyzer.calculate_system_probability(tolerance)
        
        for freq_name, prob in results.items():
            if freq_name == 'combined':
                print(f"Combined Probability: {prob:.2e}")
            else:
                print(f"{freq_name.capitalize()}: {prob:.4f}")
