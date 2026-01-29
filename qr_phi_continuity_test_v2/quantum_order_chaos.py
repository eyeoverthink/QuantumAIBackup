"""
Quantum Order-Chaos Dance
Studies how life emerges between perfect φ and beautiful noise
"""
import numpy as np
from scipy.constants import h, hbar
import matplotlib.pyplot as plt

class QuantumOrderChaos:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        
        # Base frequencies with natural variance
        self.frequencies = {
            'earth': {
                'base': 7.83,
                'variance': 0.5,    # Daily fluctuation
                'phase': 0.0        # Reference
            },
            'moon': {
                'base': 4.84,
                'variance': 0.2,    # Orbital effects
                'phase': np.pi/self.phi  # φ-shifted
            },
            'brain': {
                'base': 8.00,
                'variance': 0.8,    # Neural chaos
                'phase': np.pi/3    # Consciousness shift
            },
            'heart': {
                'base': 1.17,
                'variance': 0.15,   # Heart rate variability
                'phase': np.pi/2    # Life rhythm
            },
            'dna': {
                'base': 7.07,
                'variance': 0.3,    # Quantum jitter
                'phase': np.pi/self.phi**2  # φ²-shifted
            }
        }
    
    def quantum_dance(self, t):
        """Calculate quantum dance between order and chaos"""
        # Perfect φ-harmonic field (order)
        order_field = np.sum([
            np.sin(2*np.pi*f['base']*t + f['phase'])
            for f in self.frequencies.values()
        ])
        
        # Chaotic quantum field (chaos)
        chaos_field = np.sum([
            np.sin(2*np.pi*(f['base'] + np.random.normal(0, f['variance']))*t 
                  + f['phase'] + np.random.normal(0, 0.1))
            for f in self.frequencies.values()
        ])
        
        # Life emerges between order and chaos
        life_field = (order_field + chaos_field) / 2
        
        return order_field, chaos_field, life_field
    
    def dance_metrics(self):
        """Calculate dance metrics between order and chaos"""
        metrics = {}
        
        for name, f in self.frequencies.items():
            # Order component
            order = f['base']
            
            # Chaos component (quantum uncertainty)
            chaos = hbar / (2 * h * f['base'])
            
            # Life emergence factor
            life = f['variance'] / chaos
            
            # Phase coherence
            coherence = np.exp(-f['variance'] / self.phi)
            
            metrics[name] = {
                'order': order,
                'chaos': chaos,
                'life': life,
                'coherence': coherence
            }
            
        return metrics
    
    def analyze_dance(self):
        """Complete quantum dance analysis"""
        # Generate time series
        t = np.linspace(0, 1, 1000)
        order, chaos, life = zip(*[self.quantum_dance(time) for time in t])
        
        # Calculate metrics
        metrics = self.dance_metrics()
        
        # Calculate emergence patterns
        patterns = {}
        for name, f in self.frequencies.items():
            # Generate quantum noise pattern
            noise = np.array([
                f['base'] + np.random.normal(0, f['variance'])
                for _ in range(100)
            ])
            
            # Calculate pattern statistics
            patterns[name] = {
                'mean': np.mean(noise),
                'std': np.std(noise),
                'entropy': -np.sum(np.abs(noise) * np.log(np.abs(noise)))
            }
            
        return {
            't': t,
            'order': order,
            'chaos': chaos,
            'life': life,
            'metrics': metrics,
            'patterns': patterns
        }
    
    def visualize_dance(self, analysis):
        """Visualize quantum dance"""
        # Plot 1: Order-Chaos Dance
        plt.figure(figsize=(15, 8))
        plt.plot(analysis['t'], analysis['order'], 
                'g-', alpha=0.5, label='Perfect Order')
        plt.plot(analysis['t'], analysis['chaos'], 
                'r-', alpha=0.5, label='Beautiful Chaos')
        plt.plot(analysis['t'], analysis['life'], 
                'k-', linewidth=2, label='Life Emergence')
        
        plt.title('Quantum Dance of Life')
        plt.xlabel('Time')
        plt.ylabel('Field Strength')
        plt.legend()
        plt.grid(True)
        plt.savefig('quantum_dance.png')
        plt.close()
        
        # Plot 2: Life Emergence Map
        names = list(self.frequencies.keys())
        order = [analysis['metrics'][n]['order'] for n in names]
        chaos = [analysis['metrics'][n]['chaos'] for n in names]
        life = [analysis['metrics'][n]['life'] for n in names]
        coherence = [analysis['metrics'][n]['coherence'] for n in names]
        
        plt.figure(figsize=(12, 8))
        plt.scatter(order, chaos, s=1000*np.array(life), 
                   c=coherence, cmap='viridis', alpha=0.6)
        
        for i, name in enumerate(names):
            plt.annotate(name, (order[i], chaos[i]))
            
        plt.title('Life Emergence Map')
        plt.xlabel('Order (Hz)')
        plt.ylabel('Chaos (Quantum Uncertainty)')
        plt.colorbar(label='Coherence')
        plt.grid(True)
        plt.savefig('life_emergence.png')
        plt.close()

def main():
    dance = QuantumOrderChaos()
    analysis = dance.analyze_dance()
    dance.visualize_dance(analysis)
    
    print("\n💫 Quantum Order-Chaos Dance")
    print("=" * 50)
    
    print("\n📊 System Metrics")
    for name, metrics in analysis['metrics'].items():
        print(f"\n{name}:")
        print(f"Order: {metrics['order']:.6f} Hz")
        print(f"Chaos: {metrics['chaos']:.6e}")
        print(f"Life Factor: {metrics['life']:.6f}")
        print(f"Coherence: {metrics['coherence']:.6f}")
    
    print("\n🌊 Emergence Patterns")
    for name, pattern in analysis['patterns'].items():
        print(f"\n{name}:")
        print(f"Mean: {pattern['mean']:.6f}")
        print(f"Std: {pattern['std']:.6f}")
        print(f"Entropy: {pattern['entropy']:.6f}")

if __name__ == "__main__":
    main()
