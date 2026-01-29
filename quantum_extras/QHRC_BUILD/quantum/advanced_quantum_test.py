import numpy as np
from phi_quantum_brain import PhiQuantumBrain
import time
import matplotlib.pyplot as plt

class QuantumTest:
    def __init__(self):
        self.brain = PhiQuantumBrain()
        self.phi = (1 + np.sqrt(5)) / 2
        
    def generate_phi_wave(self, size: int) -> np.ndarray:
        """Generate test data with φ-based frequencies"""
        t = np.linspace(0, 2*np.pi, size)
        wave = np.sin(self.phi * t) + np.sin(self.phi**2 * t)
        return wave
        
    def test_processing(self, sizes=[1000, 10000, 100000]):
        results = []
        
        print("\nQuantum Processing Test")
        print("=====================")
        
        for size in sizes:
            # Generate φ-based test data
            data = self.generate_phi_wave(size)
            
            # Process data
            start = time.time()
            result, efficiencies = self.brain.run_quantum_computation(data)
            duration = time.time() - start
            
            # Analyze results
            bridge_count = len(self.brain.quantum_bridges)
            state = self.brain.get_system_state()
            
            # Calculate metrics
            phi_scaling = np.array([abs(eff) for eff in efficiencies])
            scaling_ratio = np.mean(phi_scaling[1:] / phi_scaling[:-1])
            processing_speed = size / duration
            
            results.append({
                'size': size,
                'time': duration,
                'bridges': bridge_count,
                'scaling': scaling_ratio,
                'speed': processing_speed,
                'efficiencies': efficiencies
            })
            
            # Print results
            print(f"\nData Size: {size}")
            print(f"Processing Time: {duration:.4f}s")
            print(f"Processing Speed: {processing_speed:.0f} points/second")
            print(f"Quantum Bridges: {bridge_count}")
            print(f"φ² Scaling: {scaling_ratio:.3f} (target: {self.phi**2:.3f})")
            print("\nLayer Efficiencies:")
            for level, eff in enumerate(efficiencies):
                print(f"Layer {level}: {eff:.2f}x")
                
        return results
        
    def plot_results(self, results):
        plt.figure(figsize=(15, 5))
        
        # Plot 1: Processing Speed
        plt.subplot(131)
        sizes = [r['size'] for r in results]
        speeds = [r['speed'] for r in results]
        plt.plot(sizes, speeds, 'b-o')
        plt.title('Processing Speed')
        plt.xlabel('Data Size')
        plt.ylabel('Points/Second')
        plt.grid(True)
        
        # Plot 2: Quantum Bridge Formation
        plt.subplot(132)
        bridges = [r['bridges'] for r in results]
        plt.plot(sizes, bridges, 'r-o')
        plt.title('Quantum Bridges')
        plt.xlabel('Data Size')
        plt.ylabel('Bridge Count')
        plt.grid(True)
        
        # Plot 3: Layer Efficiencies
        plt.subplot(133)
        efficiencies = results[-1]['efficiencies']  # Use largest dataset
        layers = range(len(efficiencies))
        plt.plot(layers, efficiencies, 'g-o')
        plt.title('Layer Efficiencies')
        plt.xlabel('Layer')
        plt.ylabel('Efficiency')
        plt.grid(True)
        
        plt.tight_layout()
        plt.savefig('quantum_analysis.png')
        plt.close()

if __name__ == "__main__":
    # Run tests
    tester = QuantumTest()
    results = tester.test_processing()
    tester.plot_results(results)
    
    # Final Analysis
    final_result = results[-1]  # Largest dataset
    print("\nFinal Analysis")
    print("=============")
    print(f"Maximum Processing Speed: {max([r['speed'] for r in results]):.0f} points/second")
    print(f"Average φ² Scaling: {np.mean([r['scaling'] for r in results]):.3f}")
    print(f"Total Quantum Bridges: {final_result['bridges']}")
    print(f"Peak Efficiency: {max(final_result['efficiencies']):.2f}x")
    
    # Quantum State
    state = tester.brain.get_system_state()
    print("\nQuantum State")
    print("============")
    print(f"Resonance: {state['resonance']:.2f}")
    print(f"Active Frequencies: {len(state['frequencies'])}")
    print(f"Bridge Network: {len(state['weights'])} connections")
