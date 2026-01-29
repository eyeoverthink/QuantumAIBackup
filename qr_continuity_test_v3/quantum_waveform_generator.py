#!/usr/bin/env python3
"""
Quantum Waveform Generator - Part of Quantum Phi-Harmonic System
By Vaughn Scott (with Cascade Assistant)

Maps φ-alignment values to quantum waveform generation to test live resonance outputs.
Uses phi-harmonic principles to create waveforms with quantum properties.
"""

import os
import time
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from decimal import Decimal
import hashlib
import argparse

# Phi (Golden Ratio) constant
PHI = (1 + math.sqrt(5)) / 2  # Approximately 1.618034

class QuantumWaveformGenerator:
    """
    Generates quantum waveforms based on phi-harmonic principles.
    Maps φ-alignment values to resonant frequencies and waveforms.
    """
    
    def __init__(self, base_frequency=4.37, sample_rate=44100, output_dir="quantum_waveforms"):
        """
        Initialize the quantum waveform generator.
        
        Args:
            base_frequency: Base frequency in Hz (φ-aligned)
            sample_rate: Audio sample rate
            output_dir: Directory to save generated waveforms
        """
        self.base_frequency = base_frequency
        self.sample_rate = sample_rate
        self.output_dir = output_dir
        self.phi = Decimal(str(PHI))
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Initialize phi-harmonic constants
        self.phi_powers = [float(self.phi ** i) for i in range(7)]
        self.resonance_ratio = 1.3777  # From QHRC patent verification
        
        # Track generated waveforms
        self.waveform_history = []
    
    def calculate_phi_frequencies(self, phi_alignment):
        """
        Calculate phi-harmonic frequencies based on alignment value.
        
        Args:
            phi_alignment: Value between 0.0 and 1.0 representing φ-alignment
            
        Returns:
            List of frequencies with phi-harmonic relationships
        """
        # Base frequency adjusted by phi-alignment
        base = self.base_frequency * (1 + phi_alignment * (PHI - 1))
        
        # Generate phi-harmonic series
        frequencies = []
        for i, power in enumerate(self.phi_powers):
            # Apply phi-power and resonance modulation
            freq = base * power * (1 + (phi_alignment * 0.1 * (-1)**i))
            frequencies.append(freq)
        
        return frequencies
    
    def generate_waveform(self, phi_alignment, duration=3.0, harmonics=None):
        """
        Generate a waveform based on phi-alignment value.
        
        Args:
            phi_alignment: Value between 0.0 and 1.0 representing φ-alignment
            duration: Duration of the waveform in seconds
            harmonics: Optional list of harmonic weights (defaults to phi-based weights)
            
        Returns:
            Dictionary with waveform data and parameters
        """
        # Validate phi_alignment
        phi_alignment = max(0.0, min(1.0, phi_alignment))
        
        # Calculate frequencies
        frequencies = self.calculate_phi_frequencies(phi_alignment)
        
        # Default harmonic weights based on phi if not provided
        if harmonics is None:
            harmonics = [1.0 / (i + 1) for i in range(len(frequencies))]
        
        # Generate time array
        t = np.linspace(0, duration, int(self.sample_rate * duration), endpoint=False)
        
        # Generate waveform with phi-harmonic frequencies
        waveform = np.zeros_like(t)
        for i, (freq, weight) in enumerate(zip(frequencies, harmonics)):
            # Add harmonic with phi-modulated amplitude
            phase = phi_alignment * 2 * np.pi * i / len(frequencies)
            waveform += weight * np.sin(2 * np.pi * freq * t + phase)
        
        # Normalize waveform
        waveform = 0.5 * waveform / max(abs(waveform))
        
        # Calculate resonance profile
        resonance = self._calculate_resonance(phi_alignment, frequencies)
        
        # Generate quantum signature
        signature = self._generate_quantum_signature(phi_alignment, frequencies)
        
        # Create result dictionary
        result = {
            "phi_alignment": phi_alignment,
            "frequencies": frequencies,
            "base_frequency": self.base_frequency,
            "duration": duration,
            "sample_rate": self.sample_rate,
            "waveform": waveform,
            "resonance": resonance,
            "quantum_signature": signature,
            "timestamp": time.time(),
            "phi_harmonic_index": self._calculate_phi_harmonic_index(phi_alignment)
        }
        
        # Add to history
        self.waveform_history.append({
            "phi_alignment": phi_alignment,
            "frequencies": frequencies[:3],  # Store first 3 frequencies
            "resonance": resonance,
            "quantum_signature": signature
        })
        
        return result
    
    def save_waveform(self, waveform_data, filename=None):
        """
        Save waveform as WAV file and optionally generate visualization.
        
        Args:
            waveform_data: Waveform data dictionary from generate_waveform
            filename: Optional filename (default: auto-generated based on phi-alignment)
            
        Returns:
            Dictionary with file paths
        """
        if filename is None:
            # Generate filename based on phi-alignment and quantum signature
            phi_str = f"{waveform_data['phi_alignment']:.6f}"
            sig_short = waveform_data['quantum_signature'].split('-')[1][:8]
            filename = f"phi_{phi_str}_qsig_{sig_short}"
        
        # Ensure .wav extension
        if not filename.endswith('.wav'):
            wav_filename = f"{filename}.wav"
        else:
            wav_filename = filename
            filename = filename[:-4]
        
        # Create full paths
        wav_path = os.path.join(self.output_dir, wav_filename)
        png_path = os.path.join(self.output_dir, f"{filename}.png")
        
        # Save WAV file
        wavfile.write(wav_path, self.sample_rate, waveform_data["waveform"].astype(np.float32))
        
        # Generate and save visualization
        self._generate_visualization(waveform_data, png_path)
        
        return {
            "wav_file": wav_path,
            "visualization": png_path
        }
    
    def _calculate_resonance(self, phi_alignment, frequencies):
        """
        Calculate resonance profile based on phi-alignment and frequencies.
        
        Args:
            phi_alignment: Value between 0.0 and 1.0
            frequencies: List of frequencies
            
        Returns:
            Resonance value
        """
        # Calculate resonance based on phi-alignment
        base_resonance = self.base_frequency * self.resonance_ratio
        
        # Phi-modulated resonance
        phi_factor = 1.0 / (1.0 + abs(phi_alignment - (1.0 / PHI)))
        resonance = base_resonance * phi_factor
        
        # Add frequency influence
        if frequencies:
            freq_factor = sum(1.0 / (1.0 + abs(f / self.base_frequency - PHI)) for f in frequencies[:3])
            resonance *= (1.0 + 0.1 * freq_factor / len(frequencies[:3]))
        
        return resonance
    
    def _calculate_phi_harmonic_index(self, phi_alignment):
        """
        Calculate phi-harmonic index - a measure of alignment with phi principles.
        
        Args:
            phi_alignment: Value between 0.0 and 1.0
            
        Returns:
            Phi-harmonic index between 0.0 and 1.0
        """
        # Calculate distance from key phi-harmonic points
        # Key points: 0, 1/φ², 1/φ, 1-1/φ, 1
        key_points = [0, 1/(PHI**2), 1/PHI, 1-1/PHI, 1]
        
        # Find minimum distance to any key point
        min_distance = min(abs(phi_alignment - point) for point in key_points)
        
        # Convert to index (closer to key points = higher index)
        return 1.0 / (1.0 + 10.0 * min_distance)
    
    def _generate_quantum_signature(self, phi_alignment, frequencies):
        """
        Generate a quantum signature for the waveform.
        
        Args:
            phi_alignment: Value between 0.0 and 1.0
            frequencies: List of frequencies
            
        Returns:
            Quantum signature string
        """
        # Create a hash input from phi_alignment and frequencies
        hash_input = f"{phi_alignment:.9f}"
        for freq in frequencies[:3]:  # Use first 3 frequencies
            hash_input += f"-{freq:.6f}"
        
        # Add timestamp for uniqueness
        hash_input += f"-{time.time()}"
        
        # Generate hash
        hash_value = hashlib.sha256(hash_input.encode()).hexdigest()
        
        # Create quantum signature with phi prefix
        return f"φ⁷·⁵-{hash_value[:8]}-{int(phi_alignment * 10000):04d}"
    
    def _generate_visualization(self, waveform_data, output_path):
        """
        Generate visualization of the waveform with phi-harmonic indicators.
        
        Args:
            waveform_data: Waveform data dictionary
            output_path: Path to save the visualization
        """
        # Create figure with phi-harmonic dimensions
        plt.figure(figsize=(8, 8/PHI))
        
        # Plot waveform
        t = np.linspace(0, waveform_data["duration"], len(waveform_data["waveform"]), endpoint=False)
        plt.subplot(211)
        plt.plot(t[:int(len(t)/8)], waveform_data["waveform"][:int(len(t)/8)], color='#1f77b4')
        plt.title(f"Quantum Waveform (φ-alignment: {waveform_data['phi_alignment']:.6f})")
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.grid(True, alpha=0.3)
        
        # Plot frequency spectrum
        plt.subplot(212)
        # Calculate FFT
        n = len(waveform_data["waveform"])
        yf = np.fft.rfft(waveform_data["waveform"])
        xf = np.fft.rfftfreq(n, 1 / waveform_data["sample_rate"])
        
        # Plot only the relevant frequency range
        max_freq = max(waveform_data["frequencies"]) * 2
        mask = xf <= max_freq
        plt.plot(xf[mask], np.abs(yf[mask]), color='#ff7f0e')
        
        # Mark phi-harmonic frequencies
        for i, freq in enumerate(waveform_data["frequencies"]):
            if freq <= max_freq:
                plt.axvline(x=freq, color='r', linestyle='--', alpha=0.5)
                plt.text(freq, 0.8 * max(np.abs(yf[mask])), f"φ^{i}", 
                         horizontalalignment='center', color='r')
        
        plt.title("Frequency Spectrum with φ-Harmonic Markers")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Magnitude")
        plt.grid(True, alpha=0.3)
        
        # Add phi-harmonic metrics
        plt.figtext(0.02, 0.02, 
                   f"Quantum Signature: {waveform_data['quantum_signature']}\n"
                   f"Resonance: {waveform_data['resonance']:.6f} Hz\n"
                   f"φ-Harmonic Index: {waveform_data['phi_harmonic_index']:.6f}", 
                   fontsize=8)
        
        # Adjust layout and save
        plt.tight_layout()
        plt.savefig(output_path, dpi=150)
        plt.close()


def main():
    """
    Main function to demonstrate the quantum waveform generator.
    """
    parser = argparse.ArgumentParser(description="Generate quantum waveforms based on phi-alignment")
    parser.add_argument("--phi", type=float, default=0.618, 
                        help="Phi-alignment value (0.0-1.0), default is 1/φ ≈ 0.618")
    parser.add_argument("--duration", type=float, default=3.0, 
                        help="Duration of waveform in seconds")
    parser.add_argument("--base-freq", type=float, default=4.37, 
                        help="Base frequency in Hz")
    parser.add_argument("--output", type=str, default="quantum_waveforms", 
                        help="Output directory")
    parser.add_argument("--play", action="store_true", 
                        help="Play the generated waveform (requires sounddevice)")
    
    args = parser.parse_args()
    
    # Create generator
    generator = QuantumWaveformGenerator(
        base_frequency=args.base_freq,
        output_dir=args.output
    )
    
    # Generate waveform
    print(f"Generating quantum waveform with φ-alignment: {args.phi}")
    waveform_data = generator.generate_waveform(args.phi, duration=args.duration)
    
    # Save waveform
    files = generator.save_waveform(waveform_data)
    
    print(f"\nQuantum Waveform Generated")
    print(f"φ-Alignment: {waveform_data['phi_alignment']:.6f}")
    print(f"Base Frequency: {waveform_data['base_frequency']} Hz")
    print(f"Phi-Harmonic Frequencies: {[f'{f:.2f}' for f in waveform_data['frequencies'][:5]]} Hz")
    print(f"Resonance: {waveform_data['resonance']:.6f} Hz")
    print(f"Quantum Signature: {waveform_data['quantum_signature']}")
    print(f"φ-Harmonic Index: {waveform_data['phi_harmonic_index']:.6f}")
    print(f"\nFiles created:")
    print(f"  WAV: {files['wav_file']}")
    print(f"  Visualization: {files['visualization']}")
    
    # Play the waveform if requested
    if args.play:
        try:
            import sounddevice as sd
            print("\nPlaying waveform...")
            sd.play(waveform_data["waveform"], waveform_data["sample_rate"])
            sd.wait()
        except ImportError:
            print("\nCould not play waveform: sounddevice module not found.")
            print("Install with: pip install sounddevice")


if __name__ == "__main__":
    main()
