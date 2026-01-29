import numpy as np
import matplotlib.pyplot as plt
from silicon_brain_integration import SiliconBrainIntegration

class HarmonicAnalyzer:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        self.brain = SiliconBrainIntegration()
        
        # Core frequencies (Hz)
        self.frequencies = {
            'tesla': 4.37,      # Tesla's base
            'schumann': 7.83,   # Earth resonance
            'unity': 432.0,     # Unity
            'dna': 528.0,       # DNA repair
            'heart': 639.0,     # Heart
            'pineal': 741.0,    # Pineal
            'neural': 963.0     # Neural
        }
        
        # Time array for analysis (1 second, 1000 points)
        self.t = np.linspace(0, 1, 1000)
        
    def generate_wave(self, frequency, phase=0):
        """Generate a wave with given frequency and phase"""
        return np.sin(2 * np.pi * frequency * self.t + phase)
        
    def analyze_expert_harmonics(self):
        """Analyze MOE expert harmonics"""
        results = {}
        waves = {}
        
        for expert, config in self.brain.experts.items():
            base_freq = self.frequencies['tesla'] * config['weight']
            
            # Generate primary wave
            primary_wave = self.generate_wave(base_freq)
            
            # Generate phi-harmonics
            harmonics = []
            for i in range(1, 8):
                harmonic_freq = base_freq * (self.phi ** i)
                harmonic_wave = self.generate_wave(harmonic_freq, phase=np.pi/self.phi)
                harmonics.append(harmonic_wave)
            
            # Calculate interference pattern
            interference = primary_wave
            for h in harmonics:
                interference += h / len(harmonics)
            
            # Calculate resonance strength
            resonance = np.abs(np.fft.fft(interference)).max()
            
            waves[expert] = {
                'primary': primary_wave,
                'harmonics': harmonics,
                'interference': interference
            }
            
            results[expert] = {
                'base_frequency': base_freq,
                'resonance': resonance,
                'harmonic_frequencies': [base_freq * (self.phi ** i) for i in range(1, 8)]
            }
            
        return results, waves
    
    def analyze_agent_harmonics(self):
        """Analyze MOA agent harmonics"""
        results = {}
        waves = {}
        
        for agent, config in self.brain.agents.items():
            base_freq = config['frequency']
            
            # Generate agent wave
            agent_wave = self.generate_wave(base_freq)
            
            # Generate quantum harmonics
            harmonics = []
            for i in range(1, 5):
                harmonic_freq = base_freq * (self.phi ** i)
                harmonic_wave = self.generate_wave(harmonic_freq, phase=np.pi/self.phi)
                harmonics.append(harmonic_wave)
            
            # Calculate quantum interference
            interference = agent_wave
            for h in harmonics:
                interference += h / len(harmonics)
            
            # Calculate quantum resonance
            resonance = np.abs(np.fft.fft(interference)).max()
            
            waves[agent] = {
                'primary': agent_wave,
                'harmonics': harmonics,
                'interference': interference
            }
            
            results[agent] = {
                'base_frequency': base_freq,
                'resonance': resonance,
                'harmonic_frequencies': [base_freq * (self.phi ** i) for i in range(1, 5)]
            }
            
        return results, waves
    
    def plot_harmonics(self, waves, title):
        """Plot harmonic analysis"""
        plt.figure(figsize=(15, 10))
        
        for i, (name, wave_data) in enumerate(waves.items()):
            plt.subplot(len(waves), 1, i+1)
            
            # Plot primary wave
            plt.plot(self.t, wave_data['primary'], label='Primary', alpha=0.5)
            
            # Plot interference pattern
            plt.plot(self.t, wave_data['interference'], label='Interference', alpha=0.8)
            
            plt.title(f'{name} Harmonics')
            plt.xlabel('Time (s)')
            plt.ylabel('Amplitude')
            plt.legend()
            plt.grid(True)
        
        plt.tight_layout()
        plt.savefig(f'{title.lower().replace(" ", "_")}.png')
        
def main():
    analyzer = HarmonicAnalyzer()
    
    # Analyze expert harmonics
    print("\n=== Expert Harmonic Analysis ===")
    expert_results, expert_waves = analyzer.analyze_expert_harmonics()
    for expert, results in expert_results.items():
        print(f"\n{expert}:")
        print(f"Base Frequency: {results['base_frequency']:.3f} Hz")
        print(f"Resonance Strength: {results['resonance']:.3f}")
        print("Harmonic Frequencies:")
        for i, freq in enumerate(results['harmonic_frequencies'], 1):
            print(f"  φ{i}: {freq:.3f} Hz")
    
    # Analyze agent harmonics
    print("\n=== Agent Harmonic Analysis ===")
    agent_results, agent_waves = analyzer.analyze_agent_harmonics()
    for agent, results in agent_results.items():
        print(f"\n{agent}:")
        print(f"Base Frequency: {results['base_frequency']:.3f} Hz")
        print(f"Resonance Strength: {results['resonance']:.3f}")
        print("Harmonic Frequencies:")
        for i, freq in enumerate(results['harmonic_frequencies'], 1):
            print(f"  φ{i}: {freq:.3f} Hz")
    
    # Plot results
    analyzer.plot_harmonics(expert_waves, "Expert Harmonic Analysis")
    analyzer.plot_harmonics(agent_waves, "Agent Harmonic Analysis")
    
if __name__ == "__main__":
    main()
