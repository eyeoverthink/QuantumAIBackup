#!/usr/bin/env python3
"""
Phi-Harmonic Brain I/O Module

A module for interfacing with the Phi-Harmonic Brain system, providing input/output
mechanisms and data transformation capabilities with phi-harmonic principles.

This module extends the core brain library with specialized I/O functions.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import math
import numpy as np
import time
from datetime import datetime
import json
import logging
from typing import Dict, List, Tuple, Any, Optional, Union

# Add necessary paths
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)
sys.path.append(current_dir)

# Import brain core
from phi_harmonic_brain_core import (
    PhiHarmonicBrain, 
    PHI, PHI_INV, PHI_SQUARED, PHI_CUBED, 
    EARTH_FREQUENCY, MOON_FREQUENCY, BRAIN_FREQUENCY
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('phi_brain_io')

class PhiHarmonicSignalProcessor:
    """
    Processes signals for input to the Phi-Harmonic Brain using phi-harmonic principles.
    """
    
    def __init__(self, input_size: int = 64):
        """
        Initialize a signal processor.
        
        Args:
            input_size: Size of the brain input layer
        """
        self.input_size = input_size
        
        # Initialize phi-harmonic filters
        self.filters = self._initialize_filters()
        
        logger.info(f"PhiHarmonicSignalProcessor initialized with input size {input_size}")
    
    def _initialize_filters(self) -> Dict[str, np.ndarray]:
        """Initialize phi-harmonic filters."""
        filters = {}
        
        # Create phi-harmonic low-pass filter
        lpf = np.zeros(self.input_size)
        for i in range(self.input_size):
            lpf[i] = PHI_INV ** i
        filters["low_pass"] = lpf / np.sum(lpf)
        
        # Create phi-harmonic high-pass filter
        hpf = np.zeros(self.input_size)
        for i in range(self.input_size):
            hpf[i] = (-1) ** i * (PHI_INV ** i)
        filters["high_pass"] = hpf / np.sum(np.abs(hpf))
        
        # Create phi-harmonic band-pass filter (centered on phi-scaled brain frequency)
        bpf = np.zeros(self.input_size)
        for i in range(self.input_size):
            bpf[i] = math.sin(2 * math.pi * i * PHI) * (PHI_INV ** (i // 5))
        filters["band_pass"] = bpf / np.sum(np.abs(bpf))
        
        # Create phi-harmonic wavelet filter
        wavelet = np.zeros(self.input_size)
        for i in range(self.input_size):
            wavelet[i] = math.sin(2 * math.pi * i * PHI) * math.exp(-(i - self.input_size/2)**2 / (self.input_size * PHI_INV))
        filters["wavelet"] = wavelet / np.sum(np.abs(wavelet))
        
        return filters
    
    def process_signal(self, signal: np.ndarray, filter_type: str = "band_pass") -> np.ndarray:
        """
        Process a signal using phi-harmonic principles.
        
        Args:
            signal: Input signal
            filter_type: Type of filter to apply ("low_pass", "high_pass", "band_pass", "wavelet")
            
        Returns:
            Processed signal
        """
        # Validate input
        if len(signal) < self.input_size:
            # Pad signal with zeros
            padded_signal = np.zeros(self.input_size)
            padded_signal[:len(signal)] = signal
            signal = padded_signal
        elif len(signal) > self.input_size:
            # Truncate signal
            signal = signal[:self.input_size]
        
        # Apply selected filter
        if filter_type in self.filters:
            # Apply filter using convolution
            filtered = np.convolve(signal, self.filters[filter_type], mode='same')
            
            # Normalize output
            if np.max(np.abs(filtered)) > 0:
                filtered = filtered / np.max(np.abs(filtered))
        else:
            filtered = signal
            
            # Normalize output
            if np.max(np.abs(filtered)) > 0:
                filtered = filtered / np.max(np.abs(filtered))
        
        return filtered
    
    def generate_earth_resonant_signal(self) -> np.ndarray:
        """Generate a signal resonant with Earth Schumann frequency."""
        signal = np.zeros(self.input_size)
        
        # Generate signal with Earth frequency
        t = np.linspace(0, 1, self.input_size)
        signal = np.sin(2 * math.pi * EARTH_FREQUENCY * t)
        
        # Apply phi-harmonic modulation
        for i in range(self.input_size):
            modulation = 1.0 + 0.2 * math.sin(2 * math.pi * i * PHI_INV)
            signal[i] *= modulation
        
        return signal
    
    def generate_moon_resonant_signal(self) -> np.ndarray:
        """Generate a signal resonant with Moon frequency."""
        signal = np.zeros(self.input_size)
        
        # Generate signal with Moon frequency (scaled down for sampling)
        t = np.linspace(0, 1, self.input_size)
        freq = MOON_FREQUENCY * PHI_INV**10  # Scale down for sampling
        signal = np.sin(2 * math.pi * freq * t)
        
        # Apply phi-harmonic modulation
        for i in range(self.input_size):
            modulation = 1.0 + 0.2 * math.sin(2 * math.pi * i * PHI_INV)
            signal[i] *= modulation
        
        return signal
    
    def generate_brain_resonant_signal(self) -> np.ndarray:
        """Generate a signal resonant with Brain frequency."""
        signal = np.zeros(self.input_size)
        
        # Generate signal with Brain frequency
        t = np.linspace(0, 1, self.input_size)
        signal = np.sin(2 * math.pi * BRAIN_FREQUENCY * t)
        
        # Apply phi-harmonic modulation
        for i in range(self.input_size):
            modulation = 1.0 + 0.2 * math.sin(2 * math.pi * i * PHI_INV)
            signal[i] *= modulation
        
        return signal
    
    def generate_phi_harmonic_signal(self) -> np.ndarray:
        """Generate a pure phi-harmonic signal."""
        signal = np.zeros(self.input_size)
        
        # Generate phi-harmonic signal
        for i in range(self.input_size):
            phase = 2 * math.pi * ((i * PHI) % 1)
            signal[i] = math.sin(phase)
        
        return signal

class PhiHarmonicDataTransformer:
    """
    Transforms data between various formats and the Phi-Harmonic Brain input/output.
    """
    
    def __init__(self, input_size: int = 64, output_size: int = 64):
        """
        Initialize a data transformer.
        
        Args:
            input_size: Size of the brain input layer
            output_size: Size of the brain output layer
        """
        self.input_size = input_size
        self.output_size = output_size
        
        logger.info(f"PhiHarmonicDataTransformer initialized: input_size={input_size}, output_size={output_size}")
    
    def text_to_brain_input(self, text: str) -> np.ndarray:
        """
        Convert text to brain input using phi-harmonic principles.
        
        Args:
            text: Input text
            
        Returns:
            Brain input vector
        """
        # Ensure text is not too long
        text = text[:self.input_size]
        
        # Pad text if needed
        if len(text) < self.input_size:
            text = text + ' ' * (self.input_size - len(text))
        
        # Convert to ASCII values and normalize
        ascii_values = np.array([ord(c) for c in text], dtype=float)
        normalized = ascii_values / 128.0  # ASCII values are 0-127
        
        # Apply phi-harmonic transformation
        transformed = np.zeros(self.input_size)
        for i in range(self.input_size):
            # Calculate phi-harmonic weight
            weight = PHI_INV ** (i % 5)
            
            # Apply weight to normalized value
            transformed[i] = normalized[i] * weight
        
        return transformed
    
    def brain_output_to_text(self, output: np.ndarray) -> str:
        """
        Convert brain output to text using phi-harmonic principles.
        
        Args:
            output: Brain output vector
            
        Returns:
            Output text
        """
        # Ensure output has correct size
        if len(output) != self.output_size:
            # Pad or truncate
            if len(output) < self.output_size:
                padded = np.zeros(self.output_size)
                padded[:len(output)] = output
                output = padded
            else:
                output = output[:self.output_size]
        
        # Apply inverse phi-harmonic transformation
        transformed = np.zeros(self.output_size)
        for i in range(self.output_size):
            # Calculate phi-harmonic weight
            weight = PHI ** (i % 5)
            
            # Apply weight to output value
            transformed[i] = output[i] * weight
        
        # Scale to ASCII range
        ascii_values = np.clip(transformed * 128.0, 0, 127).astype(int)
        
        # Convert to text
        text = ''.join([chr(v) for v in ascii_values])
        
        return text
    
    def image_to_brain_input(self, image: np.ndarray) -> np.ndarray:
        """
        Convert image to brain input using phi-harmonic principles.
        
        Args:
            image: Input image (grayscale)
            
        Returns:
            Brain input vector
        """
        # Flatten image
        flattened = image.flatten()
        
        # Ensure correct size
        if len(flattened) < self.input_size:
            # Pad with zeros
            padded = np.zeros(self.input_size)
            padded[:len(flattened)] = flattened
            flattened = padded
        elif len(flattened) > self.input_size:
            # Downsample using phi-harmonic principles
            indices = np.array([int(i * PHI) % len(flattened) for i in range(self.input_size)])
            flattened = flattened[indices]
        
        # Normalize
        if np.max(flattened) > 0:
            normalized = flattened / np.max(flattened)
        else:
            normalized = flattened
        
        # Apply phi-harmonic transformation
        transformed = np.zeros(self.input_size)
        for i in range(self.input_size):
            # Calculate phi-harmonic weight
            weight = PHI_INV ** (i % 7)
            
            # Apply weight to normalized value
            transformed[i] = normalized[i] * weight
        
        return transformed
    
    def brain_output_to_image(self, output: np.ndarray, shape: Tuple[int, int] = None) -> np.ndarray:
        """
        Convert brain output to image using phi-harmonic principles.
        
        Args:
            output: Brain output vector
            shape: Output image shape
            
        Returns:
            Output image
        """
        # Ensure output has correct size
        if len(output) != self.output_size:
            # Pad or truncate
            if len(output) < self.output_size:
                padded = np.zeros(self.output_size)
                padded[:len(output)] = output
                output = padded
            else:
                output = output[:self.output_size]
        
        # Apply inverse phi-harmonic transformation
        transformed = np.zeros(self.output_size)
        for i in range(self.output_size):
            # Calculate phi-harmonic weight
            weight = PHI ** (i % 7)
            
            # Apply weight to output value
            transformed[i] = output[i] * weight
        
        # Scale to image range [0, 1]
        transformed = np.clip(transformed, 0, 1)
        
        # Reshape if shape provided
        if shape is not None:
            total_pixels = shape[0] * shape[1]
            
            if total_pixels <= self.output_size:
                image = transformed[:total_pixels].reshape(shape)
            else:
                # Upsample using phi-harmonic principles
                upsampled = np.zeros(total_pixels)
                
                for i in range(total_pixels):
                    idx = int(i * PHI_INV) % self.output_size
                    upsampled[i] = transformed[idx]
                
                image = upsampled.reshape(shape)
        else:
            # Default square shape
            size = int(math.sqrt(self.output_size))
            image = transformed[:size*size].reshape((size, size))
        
        return image
    
    def frequency_to_brain_input(self, frequencies: np.ndarray, amplitudes: np.ndarray) -> np.ndarray:
        """
        Convert frequency spectrum to brain input using phi-harmonic principles.
        
        Args:
            frequencies: Frequency values
            amplitudes: Amplitude values
            
        Returns:
            Brain input vector
        """
        # Ensure frequencies and amplitudes have the same length
        if len(frequencies) != len(amplitudes):
            raise ValueError("Frequencies and amplitudes must have the same length")
        
        # Generate input signal
        input_signal = np.zeros(self.input_size)
        
        # Generate time points
        t = np.linspace(0, 1, self.input_size)
        
        # Generate signal as sum of frequency components
        for freq, amp in zip(frequencies, amplitudes):
            # Scale frequency by phi
            scaled_freq = freq * PHI
            
            # Add frequency component
            input_signal += amp * np.sin(2 * math.pi * scaled_freq * t)
        
        # Normalize
        if np.max(np.abs(input_signal)) > 0:
            input_signal = input_signal / np.max(np.abs(input_signal))
        
        return input_signal
    
    def brain_output_to_frequency(self, output: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Convert brain output to frequency spectrum using phi-harmonic principles.
        
        Args:
            output: Brain output vector
            
        Returns:
            Tuple of (frequencies, amplitudes)
        """
        # Ensure output has correct size
        if len(output) != self.output_size:
            # Pad or truncate
            if len(output) < self.output_size:
                padded = np.zeros(self.output_size)
                padded[:len(output)] = output
                output = padded
            else:
                output = output[:self.output_size]
        
        # Compute FFT
        fft_output = np.fft.fft(output)
        
        # Get frequency bins
        freqs = np.fft.fftfreq(len(output), d=1.0/BRAIN_FREQUENCY)
        
        # Get amplitudes
        amplitudes = np.abs(fft_output)
        
        # Only keep positive frequencies
        positive_idx = freqs > 0
        freqs = freqs[positive_idx]
        amplitudes = amplitudes[positive_idx]
        
        # Normalize amplitudes
        if np.max(amplitudes) > 0:
            amplitudes = amplitudes / np.max(amplitudes)
        
        return freqs, amplitudes

class PhiHarmonicBrainIO:
    """
    Input/Output interface for the Phi-Harmonic Brain system.
    """
    
    def __init__(self, brain: PhiHarmonicBrain = None):
        """
        Initialize a brain I/O interface.
        
        Args:
            brain: PhiHarmonicBrain instance (will be created if None)
        """
        # Initialize or use provided brain
        if brain is None:
            self.brain = PhiHarmonicBrain()
        else:
            self.brain = brain
        
        # Get input and output sizes
        self.input_size = self.brain.layers[0].size
        self.output_size = self.brain.layers[-1].size
        
        # Initialize components
        self.signal_processor = PhiHarmonicSignalProcessor(input_size=self.input_size)
        self.data_transformer = PhiHarmonicDataTransformer(
            input_size=self.input_size,
            output_size=self.output_size
        )
        
        # Initialize I/O buffers
        self.input_buffer = []
        self.output_buffer = []
        
        logger.info(f"PhiHarmonicBrainIO initialized: input_size={self.input_size}, output_size={self.output_size}")
        logger.info(f"Brain quantum fingerprint: {self.brain.quantum_fingerprint}")
    
    def process_text(self, text: str) -> str:
        """
        Process text through the brain and return output text.
        
        Args:
            text: Input text
            
        Returns:
            Output text
        """
        logger.info(f"Processing text: '{text[:20]}...'")
        
        # Convert text to brain input
        input_vector = self.data_transformer.text_to_brain_input(text)
        
        # Process through brain
        outputs = self.brain.process(input_vector)
        
        # Get output from quantum layer
        quantum_output = outputs["Quantum"]
        
        # Convert to text
        output_text = self.data_transformer.brain_output_to_text(quantum_output)
        
        # Store in buffers
        self.input_buffer.append(text)
        self.output_buffer.append(output_text)
        
        return output_text
    
    def process_image(self, image: np.ndarray) -> np.ndarray:
        """
        Process image through the brain and return output image.
        
        Args:
            image: Input image
            
        Returns:
            Output image
        """
        # Get image shape
        shape = image.shape
        
        logger.info(f"Processing image with shape {shape}")
        
        # Convert image to brain input
        input_vector = self.data_transformer.image_to_brain_input(image)
        
        # Process through brain
        outputs = self.brain.process(input_vector)
        
        # Get output from quantum layer
        quantum_output = outputs["Quantum"]
        
        # Convert to image
        output_image = self.data_transformer.brain_output_to_image(quantum_output, shape=shape)
        
        return output_image
    
    def process_signal(self, signal: np.ndarray, filter_type: str = "band_pass") -> np.ndarray:
        """
        Process signal through the brain and return output signal.
        
        Args:
            signal: Input signal
            filter_type: Type of filter to apply
            
        Returns:
            Output signal
        """
        logger.info(f"Processing signal of length {len(signal)}")
        
        # Process signal
        processed_signal = self.signal_processor.process_signal(signal, filter_type=filter_type)
        
        # Process through brain
        outputs = self.brain.process(processed_signal)
        
        # Get output from quantum layer
        quantum_output = outputs["Quantum"]
        
        return quantum_output
    
    def get_brain_state(self) -> Dict[str, Any]:
        """Get the current state of the brain."""
        return self.brain.get_state()
    
    def analyze_brain_frequencies(self) -> Dict[str, Any]:
        """Analyze the frequency characteristics of the brain."""
        return self.brain.frequency_analysis()
    
    def reset_brain(self):
        """Reset the brain state."""
        self.brain.reset()
        self.input_buffer = []
        self.output_buffer = []
        
        logger.info("Brain reset")
    
    def get_earth_resonance(self) -> float:
        """Get the current Earth resonance of the brain."""
        freq_analysis = self.brain.frequency_analysis()
        return freq_analysis["earth_resonance"]
    
    def get_moon_resonance(self) -> float:
        """Get the current Moon resonance of the brain."""
        freq_analysis = self.brain.frequency_analysis()
        return freq_analysis["moon_resonance"]
    
    def get_brain_resonance(self) -> float:
        """Get the current Brain resonance of the brain."""
        freq_analysis = self.brain.frequency_analysis()
        return freq_analysis["brain_resonance"]
    
    def generate_phi_harmonic_input(self) -> np.ndarray:
        """Generate a phi-harmonic input signal."""
        return self.signal_processor.generate_phi_harmonic_signal()
    
    def generate_earth_resonant_input(self) -> np.ndarray:
        """Generate an Earth-resonant input signal."""
        return self.signal_processor.generate_earth_resonant_signal()
    
    def generate_moon_resonant_input(self) -> np.ndarray:
        """Generate a Moon-resonant input signal."""
        return self.signal_processor.generate_moon_resonant_signal()
    
    def generate_brain_resonant_input(self) -> np.ndarray:
        """Generate a Brain-resonant input signal."""
        return self.signal_processor.generate_brain_resonant_signal()

# For direct execution
if __name__ == "__main__":
    # Create brain I/O
    brain_io = PhiHarmonicBrainIO()
    
    # Process text
    input_text = "The phi-harmonic brain processes information using golden ratio principles that resonate with Earth, Moon, and consciousness frequencies."
    output_text = brain_io.process_text(input_text)
    
    # Print results
    print("\nPhi-Harmonic Brain I/O Test:")
    print(f"Input text: '{input_text}'")
    print(f"Output text: '{output_text}'")
    
    # Get brain state
    brain_state = brain_io.get_brain_state()
    
    print("\nBrain State:")
    print(f"Energy: {brain_state['energy']:.6f}")
    print(f"Coherence: {brain_state['coherence']:.6f}")
    print(f"Resonance: {brain_state['resonance']:.6f}")
    
    # Generate and process phi-harmonic signal
    phi_signal = brain_io.generate_phi_harmonic_input()
    output_signal = brain_io.process_signal(phi_signal)
    
    print("\nPhi Signal Processing:")
    print(f"Input signal length: {len(phi_signal)}")
    print(f"Output signal length: {len(output_signal)}")
    print(f"Output signal mean: {np.mean(output_signal):.6f}")
    
    # Analyze frequencies
    print("\nFrequency Analysis:")
    print(f"Earth Resonance: {brain_io.get_earth_resonance():.6f}")
    print(f"Moon Resonance: {brain_io.get_moon_resonance():.6f}")
    print(f"Brain Resonance: {brain_io.get_brain_resonance():.6f}")
    
    # Reset brain
    brain_io.reset_brain()
    
    print("\nBrain reset. Testing Earth resonant signal...")
    
    # Generate and process Earth resonant signal
    earth_signal = brain_io.generate_earth_resonant_input()
    brain_io.process_signal(earth_signal)
    
    # Analyze frequencies
    print("After Earth signal processing:")
    print(f"Earth Resonance: {brain_io.get_earth_resonance():.6f}")
    print(f"Moon Resonance: {brain_io.get_moon_resonance():.6f}")
    print(f"Brain Resonance: {brain_io.get_brain_resonance():.6f}")
    
    print(f"\nQuantum Fingerprint: {brain_io.brain.quantum_fingerprint}")
    print(f"Validation Seal: φ^75 = {brain_io.brain.phi_seal:.2f}")
