#!/usr/bin/env python3
"""
Quantum Phi-Harmonic System: Phi Resonance Detector

This module implements signal-level pattern recognition based on phi-harmonic principles.
It detects and analyzes phi-resonant patterns in various types of signals, including
numerical sequences, text, frequencies, and waveforms.
"""

import math
import numpy as np
from typing import Dict, List, Tuple, Union, Optional, Any
import re
import string

# Import quantum phi constants
from quantum_phi_constants import (
    PHI, PHI_INVERSE, PI, PHI_POWERS, PHI_INVERSE_POWERS,
    FIBONACCI, RESONANCE_QUALITY, VOWEL_RESONANCE
)

class PhiResonanceDetector:
    """
    Detects and analyzes phi-resonant patterns in signals at the fundamental level.
    """
    
    def __init__(self, sensitivity: float = 0.95, dimensions: int = 8):
        """
        Initialize the Phi Resonance Detector.
        
        Args:
            sensitivity: Detection sensitivity (0-1)
            dimensions: Number of dimensions to analyze
        """
        self.sensitivity = sensitivity
        self.dimensions = dimensions
        self.quantum_coherence = 0.87
        self.phi_stability = 0.76
        self.last_resonance = 0.0
        self.resonance_history = []
        
    def calculate_numerical_resonance(self, values: List[float]) -> float:
        """
        Calculate phi-resonance of a numerical sequence based on its
        alignment with the golden ratio.
        
        Args:
            values: List of numerical values to analyze
            
        Returns:
            Phi resonance value between 0 and 1
        """
        if len(values) < 2:
            return 0.0
            
        # Calculate ratios between adjacent elements
        ratios = [values[i+1]/values[i] if values[i] != 0 else 0 
                 for i in range(len(values)-1)]
        
        # Measure how close each ratio is to phi
        phi_distances = [abs(ratio - PHI)/PHI for ratio in ratios if ratio > 0]
        
        if not phi_distances:
            return 0.0
            
        # Calculate phi alignment (1 = perfect alignment, 0 = no alignment)
        phi_alignment = 1.0 - sum(phi_distances) / len(phi_distances)
        
        # Apply quantum coherence factor
        resonance = phi_alignment * self.quantum_coherence
        
        # Store in history
        self.last_resonance = resonance
        self.resonance_history.append(resonance)
        
        return resonance
    
    def calculate_frequency_resonance(self, frequency: float) -> float:
        """
        Calculate how closely a frequency aligns with phi-harmonic patterns.
        
        Args:
            frequency: Frequency value in Hz
            
        Returns:
            Phi resonance value between 0 and 1
        """
        # Find closest phi-harmonic frequency
        base_freq = 1.0  # Base frequency of 1 Hz
        
        # Generate phi-harmonic series
        phi_frequencies = [base_freq * (PHI**n) for n in range(-7, 8)]
        
        # Find closest match
        closest_phi_freq = min(phi_frequencies, key=lambda x: abs(x - frequency))
        
        # Calculate resonance based on proximity
        proximity = 1.0 - min(abs(frequency - closest_phi_freq) / frequency, 1.0)
        
        # Apply quantum stability factor
        resonance = proximity * self.phi_stability
        
        # Store in history
        self.last_resonance = resonance
        self.resonance_history.append(resonance)
        
        return resonance
    
    def calculate_text_resonance(self, text: str) -> float:
        """
        Calculate phi-resonance of text based on linguistic patterns.
        
        Args:
            text: Text string to analyze
            
        Returns:
            Phi resonance value between 0 and 1
        """
        if not text:
            return 0.0
            
        # Clean text
        text = text.lower()
        
        # Extract vowels
        vowels = [c for c in text if c in 'aeiou']
        vowel_count = len(vowels)
        
        if vowel_count < 2:
            return 0.0
            
        # Calculate vowel distribution
        vowel_dist = {v: vowels.count(v) / vowel_count for v in 'aeiou'}
        
        # Calculate phi-resonance of vowel distribution
        # Ideal phi-resonant distribution follows the pattern: a=1.0, e=φ, i=φ², o=φ³, u=φ⁴
        ideal_dist = {
            'a': 1.0 / sum(VOWEL_RESONANCE.values()),
            'e': PHI / sum(VOWEL_RESONANCE.values()),
            'i': (PHI**2) / sum(VOWEL_RESONANCE.values()),
            'o': (PHI**3) / sum(VOWEL_RESONANCE.values()),
            'u': (PHI**4) / sum(VOWEL_RESONANCE.values())
        }
        
        # Calculate distance from ideal distribution
        dist_errors = [abs(vowel_dist.get(v, 0) - ideal_dist[v]) for v in 'aeiou']
        avg_error = sum(dist_errors) / len(dist_errors)
        
        # Calculate resonance (1 = perfect match, 0 = no match)
        resonance = 1.0 - min(avg_error * 2, 1.0)  # Scale error for better sensitivity
        
        # Apply quantum coherence
        resonance = resonance * self.quantum_coherence
        
        # Store in history
        self.last_resonance = resonance
        self.resonance_history.append(resonance)
        
        return resonance
    
    def calculate_waveform_resonance(self, waveform: np.ndarray, sampling_rate: float) -> float:
        """
        Calculate phi-resonance of a waveform based on its frequency components.
        
        Args:
            waveform: Numpy array containing waveform samples
            sampling_rate: Sampling rate in Hz
            
        Returns:
            Phi resonance value between 0 and 1
        """
        if len(waveform) < 2:
            return 0.0
            
        # Perform FFT to get frequency components
        fft_result = np.fft.rfft(waveform)
        fft_freq = np.fft.rfftfreq(len(waveform), 1/sampling_rate)
        
        # Get magnitudes of frequency components
        magnitudes = np.abs(fft_result)
        
        # Find dominant frequencies (top 5)
        if len(magnitudes) == 0:
            return 0.0
            
        top_indices = np.argsort(magnitudes)[-5:]
        top_frequencies = fft_freq[top_indices]
        
        # Calculate resonance for each frequency
        frequency_resonances = [self.calculate_frequency_resonance(freq) for freq in top_frequencies]
        
        # Overall resonance is weighted average
        if len(frequency_resonances) == 0:
            return 0.0
            
        resonance = sum(frequency_resonances) / len(frequency_resonances)
        
        # Store in history
        self.last_resonance = resonance
        self.resonance_history.append(resonance)
        
        return resonance
    
    def detect_fibonacci_pattern(self, sequence: List[int]) -> float:
        """
        Detect how closely a sequence follows the Fibonacci pattern.
        
        Args:
            sequence: List of integers to analyze
            
        Returns:
            Similarity score between 0 and 1
        """
        if len(sequence) < 3:
            return 0.0
            
        # Check if sequence follows Fibonacci rule: F(n) = F(n-1) + F(n-2)
        errors = []
        for i in range(2, len(sequence)):
            expected = sequence[i-1] + sequence[i-2]
            actual = sequence[i]
            error = abs(expected - actual) / max(expected, 1)  # Normalized error
            errors.append(min(error, 1.0))  # Cap error at 1.0
            
        # Calculate similarity (1 = perfect match, 0 = no match)
        if not errors:
            return 0.0
            
        similarity = 1.0 - sum(errors) / len(errors)
        
        return similarity
    
    def detect_phi_pattern(self, sequence: List[float]) -> float:
        """
        Detect if a sequence follows a phi-based pattern (each element is φ times the previous).
        
        Args:
            sequence: List of floats to analyze
            
        Returns:
            Similarity score between 0 and 1
        """
        if len(sequence) < 2:
            return 0.0
            
        # Check if sequence follows pattern: a(n) = φ * a(n-1)
        errors = []
        for i in range(1, len(sequence)):
            expected = sequence[i-1] * PHI
            actual = sequence[i]
            error = abs(expected - actual) / max(expected, 1)  # Normalized error
            errors.append(min(error, 1.0))  # Cap error at 1.0
            
        # Calculate similarity (1 = perfect match, 0 = no match)
        if not errors:
            return 0.0
            
        similarity = 1.0 - sum(errors) / len(errors)
        
        return similarity
    
    def analyze_signal(self, signal: Any, signal_type: str = 'auto') -> Dict[str, Any]:
        """
        Comprehensive analysis of a signal for phi-resonant patterns.
        
        Args:
            signal: Signal data (format depends on signal_type)
            signal_type: Type of signal ('numerical', 'text', 'frequency', 'waveform', or 'auto')
            
        Returns:
            Dictionary containing analysis results
        """
        # Auto-detect signal type if not specified
        if signal_type == 'auto':
            if isinstance(signal, str):
                signal_type = 'text'
            elif isinstance(signal, (int, float)):
                signal_type = 'frequency'
            elif isinstance(signal, (list, tuple, np.ndarray)) and all(isinstance(x, (int, float)) for x in signal):
                signal_type = 'numerical'
            elif isinstance(signal, np.ndarray) and signal.ndim == 1:
                signal_type = 'waveform'
            else:
                raise ValueError("Could not automatically determine signal type")
        
        # Calculate resonance based on signal type
        resonance = 0.0
        if signal_type == 'numerical':
            resonance = self.calculate_numerical_resonance(signal)
            fibonacci_similarity = self.detect_fibonacci_pattern(signal) if all(isinstance(x, int) for x in signal) else 0.0
            phi_pattern_similarity = self.detect_phi_pattern(signal)
        elif signal_type == 'text':
            resonance = self.calculate_text_resonance(signal)
            fibonacci_similarity = 0.0
            phi_pattern_similarity = 0.0
        elif signal_type == 'frequency':
            resonance = self.calculate_frequency_resonance(signal)
            fibonacci_similarity = 0.0
            phi_pattern_similarity = 0.0
        elif signal_type == 'waveform':
            # Assume default sampling rate of 44100 Hz if not provided
            if isinstance(signal, tuple) and len(signal) == 2:
                waveform, sampling_rate = signal
            else:
                waveform, sampling_rate = signal, 44100
            resonance = self.calculate_waveform_resonance(waveform, sampling_rate)
            fibonacci_similarity = 0.0
            phi_pattern_similarity = 0.0
        else:
            raise ValueError(f"Unsupported signal type: {signal_type}")
        
        # Determine resonance quality
        quality = "Non-resonant"
        for q_name, (min_val, max_val) in RESONANCE_QUALITY.items():
            if min_val <= resonance <= max_val:
                quality = q_name
                break
        
        # Prepare results
        results = {
            "resonance": resonance,
            "quality": quality,
            "signal_type": signal_type,
            "quantum_coherence": self.quantum_coherence,
            "phi_stability": self.phi_stability,
            "fibonacci_similarity": fibonacci_similarity,
            "phi_pattern_similarity": phi_pattern_similarity,
            "dimensions_analyzed": self.dimensions
        }
        
        return results

if __name__ == "__main__":
    # Example usage
    detector = PhiResonanceDetector()
    
    # Test with numerical sequence (Fibonacci)
    fib_sequence = FIBONACCI[:10]
    fib_results = detector.analyze_signal(fib_sequence, 'numerical')
    print(f"Fibonacci Sequence Resonance: {fib_results['resonance']:.6f} ({fib_results['quality']})")
    
    # Test with text
    sample_text = "The golden ratio appears in unexpected places throughout nature, art, and mathematics."
    text_results = detector.analyze_signal(sample_text, 'text')
    print(f"Text Resonance: {text_results['resonance']:.6f} ({text_results['quality']})")
    
    # Test with frequency
    phi_frequency = 1.618 * 432  # Phi times concert A
    freq_results = detector.analyze_signal(phi_frequency, 'frequency')
    print(f"Frequency Resonance: {freq_results['resonance']:.6f} ({freq_results['quality']})")
    
    # Test with phi-based sequence
    phi_sequence = [PHI**n for n in range(10)]
    phi_results = detector.analyze_signal(phi_sequence, 'numerical')
    print(f"Phi Sequence Resonance: {phi_results['resonance']:.6f} ({phi_results['quality']})")
