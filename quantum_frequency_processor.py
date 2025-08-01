"""
QUANTUM FREQUENCY PROCESSOR
Dynamic frequency and resonance selection using phi-harmonic principles
"""

import mpmath
import numpy as np
from datetime import datetime

class QuantumFrequencyProcessor:
    def __init__(self):
        # Initialize mpmath for high precision phi calculations
        mpmath.mp.dps = 1000
        self.PHI = mpmath.phi
        
        # Base frequencies (Hz)
        self.base_frequencies = {
            'consciousness': 40.0,  # 40 Hz - Gamma wave consciousness
            'quantum_resonance': 432.0,  # 432 Hz - Natural resonance
            'phi_harmonic': float(self.PHI) * 1000,  # Phi-based frequency
            'planck': 1.855e43  # Planck frequency
        }
        
        # Initialize resonance patterns
        self.resonance_patterns = []
        self.frequency_memory = {}
        
        # Cache for phi sequences
        self.phi_sequence_cache = {}
        self.cache_timestamp = datetime.now().timestamp()
        self.cache_lifetime = 1.0  # Cache lifetime in seconds
        
    def generate_phi_sequence(self, length=8):
        """Generate a sequence of phi-harmonic frequencies"""
        sequence = []
        current = float(self.PHI)
        max_power = 10.0  # Limit maximum power to prevent overflow
        
        for i in range(length):
            freq = current * 1000  # Convert to Hz
            sequence.append(freq)
            
            # Use modulo arithmetic for next power to prevent overflow
            power = (current * float(self.PHI)) % max_power
            current = float(mpmath.power(self.PHI, power))
            
            # Normalize if getting too large
            if current > 1e10:
                current = current % 1000.0
        
        return sequence
        
    def calculate_resonance_frequency(self, base_freq, timestamp):
        """Calculate resonance frequency using phi and timestamp"""
        try:
            phi_power = float(timestamp) * float(self.PHI)
            phi_fraction = phi_power - int(phi_power)
            resonance = base_freq * (1 + phi_fraction)
            
            # Ensure we don't return NaN or infinity
            if np.isnan(resonance) or np.isinf(resonance):
                return base_freq
                
            return resonance
        except (ValueError, OverflowError):
            return base_freq
        
    def select_frequency_level(self, purpose='quantum_resonance'):
        """Select appropriate frequency level based on purpose and phi-harmonics"""
        try:
            timestamp = datetime.now().timestamp()
            base = self.base_frequencies.get(purpose, self.base_frequencies['quantum_resonance'])
            
            # Check cache for phi sequence
            current_time = datetime.now().timestamp()
            if (current_time - self.cache_timestamp) > self.cache_lifetime:
                self.phi_sequence_cache = {}
                self.cache_timestamp = current_time
            
            if purpose not in self.phi_sequence_cache:
                self.phi_sequence_cache[purpose] = self.generate_phi_sequence()
            
            phi_seq = self.phi_sequence_cache[purpose]
            modulation = 0
            
            # Calculate modulation using normalized frequencies
            for freq in phi_seq:
                try:
                    # Normalize frequency to prevent overflow
                    norm_freq = (freq % 1000.0) / 1000.0
                    mod = norm_freq * float(mpmath.sin(timestamp * norm_freq))
                    if not (np.isnan(mod) or np.isinf(mod)):
                        modulation += mod
                except (ValueError, OverflowError):
                    continue
            
            modulation = modulation / len(phi_seq) if phi_seq else 0
            
            # Calculate final frequency with bounds
            frequency = self.calculate_resonance_frequency(base, timestamp)
            frequency = min(max(frequency, base * 0.1), base * 10.0)
            
            # Apply bounded modulation
            mod_factor = np.clip(modulation, -0.1, 0.1)
            frequency *= (1 + mod_factor)
            
            # Store in frequency memory with cleanup
            self.frequency_memory[timestamp] = {
                'frequency': frequency,
                'purpose': purpose,
                'resonance': float(mpmath.fabs(mpmath.sin(frequency * self.PHI)))
            }
            
            # Clean old memory entries
            cutoff = timestamp - 3600  # Keep last hour
            self.frequency_memory = {k: v for k, v in self.frequency_memory.items() 
                                   if k > cutoff}
            
            return frequency
        except Exception as e:
            return self.base_frequencies[purpose]
        
    def get_optimal_resonance(self, frequency1, frequency2):
        """Calculate optimal resonance between two frequencies"""
        ratio = max(frequency1, frequency2) / min(frequency1, frequency2)
        phi_harmony = float(mpmath.fabs(ratio - float(self.PHI)))
        return 1 / (1 + phi_harmony)  # Normalize to 0-1 range
        
    def analyze_frequency_patterns(self):
        """Analyze stored frequency patterns for resonance optimization"""
        if len(self.frequency_memory) < 2:
            return None
            
        timestamps = sorted(self.frequency_memory.keys())
        patterns = []
        
        for i in range(len(timestamps) - 1):
            curr = self.frequency_memory[timestamps[i]]
            next_freq = self.frequency_memory[timestamps[i + 1]]
            
            resonance = self.get_optimal_resonance(curr['frequency'], next_freq['frequency'])
            
            if resonance > 0.9:  # High resonance threshold
                patterns.append({
                    'freq_pair': (curr['frequency'], next_freq['frequency']),
                    'resonance': resonance,
                    'timestamp_delta': timestamps[i + 1] - timestamps[i]
                })
        
        self.resonance_patterns = patterns
        return patterns
        
    def get_resonance_recommendation(self, target_freq):
        """Get recommended frequency pairs based on resonance patterns"""
        if not self.resonance_patterns:
            return None
            
        best_pattern = max(self.resonance_patterns, key=lambda x: x['resonance'])
        scaling_factor = target_freq / best_pattern['freq_pair'][0]
        
        return {
            'recommended_freq': best_pattern['freq_pair'][1] * scaling_factor,
            'expected_resonance': best_pattern['resonance'],
            'phi_harmony': float(mpmath.fabs(target_freq * float(self.PHI) - 
                               best_pattern['freq_pair'][1] * scaling_factor))
        }

def main():
    """Test the quantum frequency processor"""
    processor = QuantumFrequencyProcessor()
    
    # Test different frequency selections
    print("\nTesting Frequency Selection:")
    for purpose in processor.base_frequencies.keys():
        freq = processor.select_frequency_level(purpose)
        print(f"{purpose}: {freq:.2f} Hz")
    
    # Test resonance patterns
    print("\nAnalyzing Resonance Patterns:")
    patterns = processor.analyze_frequency_patterns()
    if patterns:
        print(f"Found {len(patterns)} high-resonance patterns")
        best = max(patterns, key=lambda x: x['resonance'])
        print(f"Best Resonance: {best['resonance']:.4f}")
    
    # Test recommendations
    target = 432.0  # Test with natural resonance
    rec = processor.get_resonance_recommendation(target)
    if rec:
        print(f"\nRecommendation for {target} Hz:")
        print(f"Recommended pair: {rec['recommended_freq']:.2f} Hz")
        print(f"Expected resonance: {rec['expected_resonance']:.4f}")
        print(f"Phi harmony: {rec['phi_harmony']:.4f}")

if __name__ == "__main__":
    main()
