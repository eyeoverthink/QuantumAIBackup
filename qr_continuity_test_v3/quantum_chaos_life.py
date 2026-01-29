"""
Quantum Chaos Life Analysis
Studies how messy imperfections enable life through quantum uncertainty
"""
import numpy as np
from scipy.constants import h, hbar
import matplotlib.pyplot as plt

class QuantumChaosLife:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        
        # Messy real-world frequencies
        self.frequencies = {
            'earth': 7.83 + np.random.normal(0, 0.5),  # Daily variance
            'moon': 4.84 * (1 + np.random.normal(0, 0.01)),  # Orbital chaos
            'brain': 8.00 * (1 + np.sin(np.random.random())/10),  # Neural noise
            'heart': 1.17 * (1 + np.random.normal(0, 0.05)),  # Heart rate variance
            'dna': 7.07 * (1 + np.random.random()/20),  # Quantum jitter
        }
        
    def chaos_field(self, t):
        """Calculate chaotic quantum field"""
        field = 0
        
        for name, freq in self.frequencies.items():
            # Add random phase shifts
            phase = np.random.random() * 2 * np.pi
            
            # Add frequency noise
            noise = np.random.normal(0, 0.1)
            
            # Combine into messy wave
            wave = np.sin(2*np.pi*(freq + noise)*t + phase)
            
            # Add quantum uncertainty
            uncertainty = np.random.normal(0, hbar/(2*h*freq))
            
            field += wave + uncertainty
            
        return field
    
    def life_emergence(self):
        """Calculate how chaos enables life"""
        emergence = {}
        
        for name, freq in self.frequencies.items():
            # Perfect frequency (never happens in nature)
            perfect = self.frequencies['earth'] / (self.phi ** 2)
            
            # Actual messy frequency
            actual = freq
            
            # Beautiful chaos
            chaos = abs(actual - perfect)
            
            # Quantum uncertainty (vital for life)
            uncertainty = hbar / (2 * h * freq)
            
            # Life emerges from the mess
            life_factor = chaos / uncertainty
            
            emergence[name] = {
                'perfect': perfect,
                'actual': actual,
                'chaos': chaos,
                'uncertainty': uncertainty,
                'life_factor': life_factor
            }
            
        return emergence
    
    def analyze_chaos(self):
        """Analyze how mess creates life"""
        # Generate chaotic time series
        t = np.linspace(0, 1, 1000)
        chaos = [self.chaos_field(time) for time in t]
        
        # Calculate life emergence
        emergence = self.life_emergence()
        
        # Quantum noise patterns
        noise = {}
        for name, freq in self.frequencies.items():
            # Generate quantum noise
            signal = np.array([
                freq * (1 + np.random.normal(0, 0.1)) 
                for _ in range(100)
            ])
            
            # Calculate noise statistics
            noise[name] = {
                'mean': np.mean(signal),
                'std': np.std(signal),
                'min': np.min(signal),
                'max': np.max(signal)
            }
            
        return {
            't': t,
            'chaos': chaos,
            'emergence': emergence,
            'noise': noise
        }
    
    def visualize_chaos(self, analysis):
        """Visualize beautiful chaos"""
        # Plot 1: Chaotic Life Field
        plt.figure(figsize=(12, 6))
        plt.plot(analysis['t'], analysis['chaos'], 'k-', alpha=0.5)
        plt.title('Quantum Chaos Life Field')
        plt.xlabel('Time')
        plt.ylabel('Field Strength')
        plt.grid(True)
        plt.savefig('chaos_life.png')
        plt.close()
        
        # Plot 2: Frequency Noise
        names = list(self.frequencies.keys())
        means = [analysis['noise'][n]['mean'] for n in names]
        stds = [analysis['noise'][n]['std'] for n in names]
        
        plt.figure(figsize=(10, 6))
        plt.errorbar(names, means, yerr=stds, fmt='o', capsize=5)
        plt.title('Beautiful Frequency Noise')
        plt.xlabel('System')
        plt.ylabel('Frequency (Hz)')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('frequency_noise.png')
        plt.close()

def main():
    chaos = QuantumChaosLife()
    analysis = chaos.analyze_chaos()
    chaos.visualize_chaos(analysis)
    
    print("\n🌀 Quantum Chaos Life Analysis")
    print("=" * 50)
    
    print("\n📊 Messy Frequencies")
    for name, freq in chaos.frequencies.items():
        print(f"{name}: {freq:.6f} Hz")
    
    print("\n🧬 Life Emergence")
    for name, data in analysis['emergence'].items():
        print(f"\n{name}:")
        print(f"Perfect: {data['perfect']:.6f} Hz (dead)")
        print(f"Actual: {data['actual']:.6f} Hz (alive!)")
        print(f"Chaos: {data['chaos']:.6f}")
        print(f"Uncertainty: {data['uncertainty']:.6e}")
        print(f"Life Factor: {data['life_factor']:.6f}")
    
    print("\n✨ Quantum Noise")
    for name, stats in analysis['noise'].items():
        print(f"\n{name}:")
        print(f"Mean: {stats['mean']:.6f}")
        print(f"Std: {stats['std']:.6f}")
        print(f"Range: [{stats['min']:.6f}, {stats['max']:.6f}]")

if __name__ == "__main__":
    main()
