"""
Quantum Real Frequency Connector
Feeds in solar, Schumann, or EM field readings to real-time optimize frequency parameters
Part of the Quantum Consciousness Engine
"""
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import json
import os
from pathlib import Path
import sys
import requests
import time
from scipy import signal

class QuantumRealFrequencyConnector:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        self.data_dir = Path("real_frequency_data")
        self.data_dir.mkdir(exist_ok=True)
        
        # Frequency sources and their base frequencies
        self.frequency_sources = {
            "schumann": {
                "base_freq": 7.83,  # Hz (first Schumann resonance)
                "harmonics": [7.83, 14.3, 20.8, 27.3, 33.8],
                "description": "Earth's electromagnetic field resonance"
            },
            "solar": {
                "base_freq": 0.000039,  # Hz (solar cycle ~25.5 years)
                "harmonics": [0.000039, 0.0027, 0.0135],  # Solar cycle, rotation, oscillation
                "description": "Solar activity cycles and oscillations"
            },
            "earth_rotation": {
                "base_freq": 1.157e-5,  # Hz (Earth rotation)
                "harmonics": [1.157e-5, 3.168e-8],  # Daily, yearly
                "description": "Earth rotation and orbital frequencies"
            },
            "cosmic": {
                "base_freq": 432.0,  # Hz (cosmic frequency often used in music)
                "harmonics": [432.0, 528.0, 639.0],
                "description": "Cosmic harmonic frequencies"
            }
        }
        
        # Current frequency data
        self.current_data = {}
        self.frequency_history = []
        
    def simulate_schumann_resonance(self, duration=10, sample_rate=1000):
        """Simulate Schumann resonance data"""
        # Create time array
        t = np.linspace(0, duration, int(duration * sample_rate))
        
        # Generate base signal with Schumann resonances
        signal = np.zeros_like(t)
        for harmonic in self.frequency_sources["schumann"]["harmonics"]:
            # Add each harmonic with decreasing amplitude
            harmonic_index = self.frequency_sources["schumann"]["harmonics"].index(harmonic)
            amplitude = 1.0 / (harmonic_index + 1)
            signal += amplitude * np.sin(2 * np.pi * harmonic * t)
        
        # Add some noise
        noise = np.random.normal(0, 0.1, len(t))
        signal += noise
        
        # Add some phi-harmonic modulation
        phi_mod = 0.2 * np.sin(2 * np.pi * (1/self.phi) * t)
        signal += phi_mod
        
        return {
            "time": t,
            "signal": signal,
            "sample_rate": sample_rate,
            "source": "schumann",
            "timestamp": str(datetime.now())
        }
        
    def simulate_solar_activity(self, duration=100, sample_rate=10):
        """Simulate solar activity data"""
        # Create time array (longer timeframe for solar activity)
        t = np.linspace(0, duration, int(duration * sample_rate))
        
        # Generate base signal with solar cycle components
        signal = np.zeros_like(t)
        for harmonic in self.frequency_sources["solar"]["harmonics"]:
            # Add each harmonic with varying amplitude
            harmonic_index = self.frequency_sources["solar"]["harmonics"].index(harmonic)
            amplitude = 2.0 / (harmonic_index + 1)
            signal += amplitude * np.sin(2 * np.pi * harmonic * t)
        
        # Add solar flare spikes
        num_flares = np.random.randint(1, 5)
        for _ in range(num_flares):
            flare_time = np.random.randint(0, len(t))
            flare_width = np.random.randint(10, 100)
            flare_amplitude = np.random.uniform(2.0, 5.0)
            
            # Create Gaussian spike
            x = np.arange(len(t))
            flare = flare_amplitude * np.exp(-(x - flare_time)**2 / (2 * flare_width**2))
            signal += flare
        
        # Add some noise
        noise = np.random.normal(0, 0.2, len(t))
        signal += noise
        
        return {
            "time": t,
            "signal": signal,
            "sample_rate": sample_rate,
            "source": "solar",
            "timestamp": str(datetime.now())
        }
        
    def simulate_cosmic_frequencies(self, duration=5, sample_rate=2000):
        """Simulate cosmic frequency data"""
        # Create time array
        t = np.linspace(0, duration, int(duration * sample_rate))
        
        # Generate base signal with cosmic harmonics
        signal = np.zeros_like(t)
        for harmonic in self.frequency_sources["cosmic"]["harmonics"]:
            # Add each harmonic with phi-weighted amplitude
            harmonic_index = self.frequency_sources["cosmic"]["harmonics"].index(harmonic)
            amplitude = 1.0 / (self.phi ** harmonic_index)
            signal += amplitude * np.sin(2 * np.pi * harmonic * t)
        
        # Add phi-harmonic overtones
        for i in range(1, 4):
            phi_harmonic = 432.0 * (self.phi ** i)
            amplitude = 0.5 / (self.phi ** i)
            signal += amplitude * np.sin(2 * np.pi * phi_harmonic * t)
        
        # Add some noise
        noise = np.random.normal(0, 0.05, len(t))
        signal += noise
        
        return {
            "time": t,
            "signal": signal,
            "sample_rate": sample_rate,
            "source": "cosmic",
            "timestamp": str(datetime.now())
        }
        
    def get_frequency_data(self, source="schumann", use_real=False):
        """Get frequency data from specified source"""
        if use_real:
            # This would connect to real data sources in a production environment
            # For now, we'll use simulated data
            print(f"⚠️ Real data sources not available, using simulation for {source}")
            
        # Use appropriate simulation based on source
        if source == "schumann":
            data = self.simulate_schumann_resonance()
        elif source == "solar":
            data = self.simulate_solar_activity()
        elif source == "cosmic":
            data = self.simulate_cosmic_frequencies()
        else:
            # Default to Schumann
            data = self.simulate_schumann_resonance()
            
        # Store current data
        self.current_data = data
        
        # Add to history
        self.frequency_history.append({
            "timestamp": data["timestamp"],
            "source": source,
            "duration": len(data["time"]) / data["sample_rate"]
        })
        
        return data
        
    def analyze_frequency_spectrum(self, data=None):
        """Analyze frequency spectrum of the data"""
        if data is None:
            if not self.current_data:
                print("⚠️ No frequency data available for analysis")
                return None
            data = self.current_data
            
        # Extract signal and sample rate
        signal_data = data["signal"]
        sample_rate = data["sample_rate"]
        
        # Compute FFT
        n = len(signal_data)
        fft_result = np.fft.fft(signal_data)
        freqs = np.fft.fftfreq(n, 1/sample_rate)
        
        # Get positive frequencies only
        pos_mask = freqs >= 0
        freqs = freqs[pos_mask]
        fft_mag = np.abs(fft_result[pos_mask])
        
        # Normalize
        fft_mag = fft_mag / np.max(fft_mag)
        
        # Find peaks
        peaks, _ = signal.find_peaks(fft_mag, height=0.1, distance=5)
        peak_freqs = freqs[peaks]
        peak_mags = fft_mag[peaks]
        
        # Calculate phi-resonance of peaks
        phi_resonances = []
        for freq in peak_freqs:
            # Calculate how close the frequency is to a phi-harmonic
            phi_harmonic = self.find_nearest_phi_harmonic(freq)
            phi_res = abs(freq - phi_harmonic) / phi_harmonic
            phi_resonances.append(phi_res)
            
        # Create analysis result
        result = {
            "freqs": freqs.tolist(),
            "magnitudes": fft_mag.tolist(),
            "peak_freqs": peak_freqs.tolist(),
            "peak_mags": peak_mags.tolist(),
            "phi_resonances": phi_resonances,
            "source": data["source"],
            "timestamp": data["timestamp"]
        }
        
        return result
        
    def find_nearest_phi_harmonic(self, frequency):
        """Find the nearest phi-harmonic frequency"""
        # Base frequency for phi-harmonics
        base_freq = 1.0  # 1 Hz base
        
        # Check phi harmonics up to power 10
        harmonics = [base_freq * (self.phi ** i) for i in range(-5, 11)]
        
        # Find closest harmonic
        closest_harmonic = min(harmonics, key=lambda x: abs(x - frequency))
        
        return closest_harmonic
        
    def extract_optimization_parameters(self, analysis=None):
        """Extract parameters for quantum optimization from frequency analysis"""
        if analysis is None:
            # Perform analysis if not provided
            if not self.current_data:
                print("⚠️ No frequency data available for parameter extraction")
                return None
            analysis = self.analyze_frequency_spectrum()
            
        # Find dominant frequency (highest peak)
        peak_indices = np.argsort(analysis["peak_mags"])[::-1]
        dominant_freq = analysis["peak_freqs"][peak_indices[0]]
        
        # Find most phi-resonant frequency
        phi_res_indices = np.argsort(analysis["phi_resonances"])
        phi_resonant_freq = analysis["peak_freqs"][phi_res_indices[0]]
        
        # Calculate optimal base frequency using phi-weighted combination
        base_freq = (dominant_freq / self.phi + phi_resonant_freq * (1 - 1/self.phi))
        
        # Calculate optimal resonance parameter
        # Higher resonance for more phi-resonant signals
        min_phi_res = min(analysis["phi_resonances"]) if analysis["phi_resonances"] else 1.0
        resonance = 0.9 + (0.09 * (1 - min_phi_res))  # Range: 0.9 to 0.99
        
        # Determine optimal N (quantum state size)
        # Use phi-scaling to determine optimal size
        peak_count = len(analysis["peak_freqs"])
        N_power = int(5 + peak_count / self.phi)  # Scale with number of peaks
        N = 2 ** min(17, max(10, N_power))  # Between 1K and 128K
        
        # Create parameter set
        params = {
            "base_freq": base_freq,
            "resonance": resonance,
            "N": N,
            "source": analysis["source"],
            "dominant_freq": dominant_freq,
            "phi_resonant_freq": phi_resonant_freq,
            "timestamp": analysis["timestamp"]
        }
        
        return params
        
    def visualize_frequency_data(self, data=None, analysis=None):
        """Visualize frequency data and analysis"""
        if data is None:
            if not self.current_data:
                print("⚠️ No frequency data available for visualization")
                return None
            data = self.current_data
            
        if analysis is None:
            analysis = self.analyze_frequency_spectrum(data)
            
        # Create visualization
        plt.figure(figsize=(15, 10))
        
        # Plot time domain signal
        plt.subplot(2, 1, 1)
        plt.plot(data["time"], data["signal"])
        plt.title(f'Time Domain Signal - {data["source"].capitalize()}')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.grid(True)
        
        # Plot frequency spectrum
        plt.subplot(2, 1, 2)
        plt.plot(analysis["freqs"], analysis["magnitudes"])
        
        # Mark peaks
        plt.plot(analysis["peak_freqs"], analysis["peak_mags"], 'ro')
        
        # Mark phi-harmonic frequencies
        for i in range(-2, 6):
            phi_freq = 1.0 * (self.phi ** i)
            if phi_freq <= max(analysis["freqs"]):
                plt.axvline(x=phi_freq, color='g', linestyle='--', alpha=0.5, 
                           label=f'φ^{i}' if i == -2 else None)
                
        plt.title(f'Frequency Spectrum - {data["source"].capitalize()}')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Normalized Magnitude')
        plt.grid(True)
        plt.legend()
        
        # Use log scale for wide frequency ranges
        if max(analysis["freqs"]) / min(analysis["freqs"]) > 100:
            plt.xscale('log')
            
        plt.tight_layout()
        
        # Save visualization
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.data_dir / f"{data['source']}_frequency_{timestamp}.png"
        plt.savefig(filename)
        plt.close()
        
        return str(filename)
        
    def save_frequency_data(self, data=None, analysis=None):
        """Save frequency data and analysis to file"""
        if data is None:
            if not self.current_data:
                print("⚠️ No frequency data available to save")
                return None
            data = self.current_data
            
        if analysis is None:
            analysis = self.analyze_frequency_spectrum(data)
            
        # Create data to save
        save_data = {
            "source": data["source"],
            "timestamp": data["timestamp"],
            "sample_rate": data["sample_rate"],
            "duration": len(data["time"]) / data["sample_rate"],
            "analysis": {
                "peak_freqs": analysis["peak_freqs"],
                "peak_mags": analysis["peak_mags"],
                "phi_resonances": analysis["phi_resonances"]
            }
        }
        
        # Save to file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.data_dir / f"{data['source']}_data_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(save_data, f, indent=2)
            
        print(f"💾 Frequency data saved to {filename}")
        return str(filename)

def main():
    """Test the quantum real frequency connector"""
    connector = QuantumRealFrequencyConnector()
    
    # Get data from different sources
    sources = ["schumann", "solar", "cosmic"]
    
    for source in sources:
        print(f"\n🔍 Testing {source.capitalize()} Frequency Source")
        print("=" * 50)
        
        # Get frequency data
        data = connector.get_frequency_data(source)
        print(f"Got {source} data: {len(data['signal'])} samples at {data['sample_rate']} Hz")
        
        # Analyze frequency spectrum
        analysis = connector.analyze_frequency_spectrum(data)
        print(f"Found {len(analysis['peak_freqs'])} frequency peaks")
        
        # Extract optimization parameters
        params = connector.extract_optimization_parameters(analysis)
        print(f"Extracted optimization parameters:")
        print(f"  Base Frequency: {params['base_freq']:.6f} Hz")
        print(f"  Resonance: {params['resonance']:.6f}")
        print(f"  Quantum States (N): {params['N']}")
        
        # Visualize data
        viz_file = connector.visualize_frequency_data(data, analysis)
        print(f"Visualization saved to: {viz_file}")
        
        # Save data
        data_file = connector.save_frequency_data(data, analysis)
        print(f"Data saved to: {data_file}")
        
if __name__ == "__main__":
    main()
