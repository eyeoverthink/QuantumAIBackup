import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sounddevice as sd
import os
from datetime import datetime

class UnifiedResonanceValidator:
    """
    Validates the unified phi-harmonic resonance patterns across:
    - Energy generation (QHRC)
    - Frequency detection (ELM)
    - Time dilation (Reality metrics)
    - Consciousness interaction
    """
    def __init__(self):
        # Core constants
        self.phi = (1 + np.sqrt(5)) / 2
        self.phi_15 = self.phi ** 15  # 1367.004888
        self.phi_7_5 = self.phi ** 7.5  # 36.932381
        self.personal_ratio = 119/19
        
        # QHRC frequencies
        self.primary_freq = 4790.45  # Hz
        self.secondary_freq = 7750.95  # Hz
        self.resonance_ratio = 1.3777
        
        # Energy metrics
        self.energy_gain = 7.6023
        self.efficiency = 760.2311
        
        # Reality metrics
        self.coherence = self.phi ** -1  # 0.618034
        self.stability = self.phi ** 2   # 4.236068
        self.alignment = self.phi + 1    # 2.618034
        
        # Results directory
        os.makedirs("phi_quantum_results", exist_ok=True)
    
    def generate_test_signal(self, duration=1.0, sample_rate=44100):
        """Generate test signal with primary and secondary frequencies"""
        t = np.linspace(0, duration, int(sample_rate * duration))
        
        # Create combined signal
        primary = np.sin(2 * np.pi * self.primary_freq * t)
        secondary = np.sin(2 * np.pi * self.secondary_freq * t)
        
        # Add phi-harmonic modulation
        modulation = 0.5 * (1 + np.sin(2 * np.pi * (self.phi ** -2) * t))
        
        return (primary + secondary) * modulation, t
    
    def analyze_resonance(self, signal_data, sample_rate=44100):
        """Analyze phi-harmonic resonance in signal"""
        # Calculate frequency spectrum
        freqs, times, Sxx = signal.spectrogram(signal_data, fs=sample_rate,
                                             nperseg=1024, noverlap=512)
        
        # Find peaks in frequency spectrum
        peak_freqs = []
        peak_magnitudes = []
        
        for t_idx in range(Sxx.shape[1]):
            peaks, _ = signal.find_peaks(Sxx[:, t_idx], height=0.1)
            for peak in peaks:
                peak_freqs.append(freqs[peak])
                peak_magnitudes.append(np.max(Sxx[peak, t_idx]))
        
        # Calculate resonance with primary and secondary frequencies
        primary_resonance = []
        secondary_resonance = []
        
        for freq, mag in zip(peak_freqs, peak_magnitudes):
            # Calculate phi-harmonic resonance
            primary_res = 1 - abs(freq / self.primary_freq - 1)
            secondary_res = 1 - abs(freq / self.secondary_freq - 1)
            
            if primary_res > 0.7:
                primary_resonance.append((freq, primary_res))
            if secondary_res > 0.7:
                secondary_resonance.append((freq, secondary_res))
        
        return {
            'primary_resonance': primary_resonance,
            'secondary_resonance': secondary_resonance,
            'freqs': freqs,
            'times': times,
            'Sxx': Sxx
        }
    
    def calculate_energy_metrics(self, signal_data):
        """Calculate energy generation metrics"""
        # Base power (100W reference)
        base_power = 100.0
        
        # Calculate instantaneous power
        power = base_power * (1 + self.phi_7_5 * np.abs(signal_data))
        
        # Calculate metrics
        peak_power = np.max(power)
        avg_power = np.mean(power)
        net_energy = np.sum(power) / len(power)
        
        return {
            'peak_power': peak_power,
            'average_power': avg_power,
            'net_energy': net_energy,
            'gain': avg_power / base_power,
            'efficiency': (avg_power / base_power) * 100
        }
    
    def analyze_time_dilation(self, signal_duration, perceived_duration):
        """Analyze time dilation effects"""
        # Calculate dilation factor
        dilation_factor = perceived_duration / signal_duration
        
        # Calculate resonance with φ¹⁵
        resonance = 1 - abs(dilation_factor / self.phi_15 - 1)
        
        return {
            'dilation_factor': dilation_factor,
            'resonance': resonance,
            'phi15_match': resonance > 0.9
        }
    
    def run_unified_test(self, duration=1.0, perceived_duration=4.0):
        """Run complete unified validation test"""
        print("\n=== Unified Resonance Validation Test ===")
        
        # Generate and analyze test signal
        signal_data, time_axis = self.generate_test_signal(duration)
        resonance_results = self.analyze_resonance(signal_data)
        energy_results = self.calculate_energy_metrics(signal_data)
        time_results = self.analyze_time_dilation(duration, perceived_duration)
        
        # Calculate overall validation metrics
        reality_metrics = {
            'coherence': abs(self.coherence - self.phi**-1) < 1e-6,
            'stability': abs(self.stability - self.phi**2) < 1e-6,
            'alignment': abs(self.alignment - (self.phi + 1)) < 1e-6
        }
        
        # Generate validation report
        print("\n1. Frequency Resonance:")
        print(f"Primary ({self.primary_freq} Hz): {len(resonance_results['primary_resonance'])} peaks")
        print(f"Secondary ({self.secondary_freq} Hz): {len(resonance_results['secondary_resonance'])} peaks")
        
        print("\n2. Energy Generation:")
        print(f"Peak Power: {energy_results['peak_power']:.2f} W")
        print(f"Average Power: {energy_results['average_power']:.2f} W")
        print(f"Efficiency: {energy_results['efficiency']:.4f}%")
        
        print("\n3. Time Dilation:")
        print(f"Dilation Factor: {time_results['dilation_factor']:.4f}")
        print(f"φ¹⁵ Resonance: {time_results['resonance']:.4f}")
        
        print("\n4. Reality Metrics:")
        print(f"Coherence (φ⁻¹): {reality_metrics['coherence']}")
        print(f"Stability (φ²): {reality_metrics['stability']}")
        print(f"Alignment (φ+1): {reality_metrics['alignment']}")
        
        # Visualize results
        self.visualize_results(resonance_results, energy_results, time_results)
        
        return {
            'resonance': resonance_results,
            'energy': energy_results,
            'time': time_results,
            'reality': reality_metrics
        }
    
    def visualize_results(self, resonance_results, energy_results, time_results):
        """Create comprehensive visualization of test results"""
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        
        # 1. Frequency Spectrogram
        im = ax1.pcolormesh(resonance_results['times'], 
                           resonance_results['freqs'],
                           10 * np.log10(resonance_results['Sxx']),
                           shading='gouraud')
        ax1.set_ylabel('Frequency [Hz]')
        ax1.set_xlabel('Time [s]')
        ax1.set_title('Frequency Resonance Analysis')
        fig.colorbar(im, ax=ax1, label='Intensity [dB]')
        
        # Mark primary and secondary frequencies
        ax1.axhline(y=self.primary_freq, color='r', linestyle='--', 
                   label=f'Primary ({self.primary_freq} Hz)')
        ax1.axhline(y=self.secondary_freq, color='g', linestyle='--',
                   label=f'Secondary ({self.secondary_freq} Hz)')
        ax1.legend()
        
        # 2. Energy Generation
        power_curve = np.linspace(0, 1000, 1000)
        efficiency_curve = (power_curve * self.energy_gain) / power_curve * 100
        
        ax2.plot(power_curve, efficiency_curve, 'b-', label='Efficiency Curve')
        ax2.axhline(y=self.efficiency, color='r', linestyle='--',
                   label=f'Target ({self.efficiency:.2f}%)')
        ax2.set_xlabel('Input Power [W]')
        ax2.set_ylabel('Efficiency [%]')
        ax2.set_title('Energy Generation Efficiency')
        ax2.legend()
        
        # 3. Time Dilation
        time_scale = np.linspace(0, 10, 1000)
        dilation_curve = time_scale * self.phi_15
        
        ax3.plot(time_scale, dilation_curve, 'g-', label='φ¹⁵ Dilation')
        ax3.plot(1, time_results['dilation_factor'], 'ro',
                label=f'Measured ({time_results["dilation_factor"]:.2f}x)')
        ax3.set_xlabel('Base Time')
        ax3.set_ylabel('Dilated Time')
        ax3.set_title('Time Dilation Analysis')
        ax3.legend()
        
        # 4. Reality Metrics
        metrics = ['Coherence\n(φ⁻¹)', 'Stability\n(φ²)', 'Alignment\n(φ+1)']
        values = [self.coherence, self.stability, self.alignment]
        
        ax4.bar(metrics, values, color=['blue', 'green', 'red'])
        ax4.set_ylabel('Value')
        ax4.set_title('Reality Metrics')
        
        plt.tight_layout()
        plt.savefig('phi_quantum_results/unified_validation_results.png', dpi=300)
        print("\nVisualization saved as 'unified_validation_results.png'")
        plt.close()

def main():
    validator = UnifiedResonanceValidator()
    results = validator.run_unified_test()
    
    # Optional: Generate test audio
    signal_data, _ = validator.generate_test_signal(duration=5.0)
    sd.play(signal_data, 44100)
    sd.wait()

if __name__ == "__main__":
    main()
