"""
Quantum Superradiance Test
Tests quantum amplification through Fibonacci-scaled resonance
"""
import numpy as np
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt
from quantum_superposition import QuantumSuperposition
from quantum_core.constants import PHI

class SuperradianceTester:
    def __init__(self):
        self.base_freq = 0.96  # Proven resonance frequency
        self.phi = PHI
        self.fib_sequence = [1, 1]  # Start of Fibonacci
        self.resonance_levels = []
        
    def next_fibonacci(self) -> float:
        """Generate next Fibonacci number and return its ratio."""
        next_num = self.fib_sequence[-1] + self.fib_sequence[-2]
        self.fib_sequence.append(next_num)
        return next_num / self.fib_sequence[-2]  # Returns ratio
        
    def test_superradiance(self, levels: int = 8) -> Dict[str, List[float]]:
        """Test superradiance using Fibonacci-scaled frequencies."""
        print("\n🌟 Quantum Superradiance Analysis")
        print("=" * 50)
        
        qsys = QuantumSuperposition()
        results = {
            'coherence': [],
            'amplification': [],
            'resonance': [],
            'phi_alignment': []
        }
        
        # Test each resonance level
        for level in range(levels):
            # Generate Fibonacci-scaled frequencies
            ratio = self.next_fibonacci()
            freq = self.base_freq * ratio
            
            print(f"\nLevel {level + 1} (Frequency: {freq:.3f} Hz)")
            print("-" * 30)
            
            # Create quantum state
            state_name = f"level_{level}"
            qsys.create_superposition(state_name, [freq])
            
            # Measure initial state
            metrics = qsys.measure_wave_interaction(state_name, state_name)
            initial_coherence = metrics['interference']
            
            # Apply resonance boost
            boost_freq = freq * self.phi
            qsys.create_superposition(f"boost_{level}", [boost_freq])
            qsys.entangle_states(state_name, f"boost_{level}")
            
            # Measure amplified state
            post_metrics = qsys.measure_wave_interaction(state_name, f"boost_{level}")
            
            # Calculate metrics
            amplification = post_metrics['interference'] / initial_coherence
            resonance = np.abs(freq - self.base_freq * self.phi**level)
            phi_alignment = np.abs(ratio - self.phi)
            
            # Store results
            results['coherence'].append(initial_coherence)
            results['amplification'].append(amplification)
            results['resonance'].append(resonance)
            results['phi_alignment'].append(phi_alignment)
            
            print(f"• Initial Coherence: {initial_coherence:.6f}")
            print(f"• Amplification: {amplification:.6f}x")
            print(f"• Resonance: {resonance:.6f}")
            print(f"• Phi Alignment: {phi_alignment:.6f}")
            
            # Test for superradiance threshold
            if amplification > self.phi:
                print("⚡ SUPERRADIANCE DETECTED!")
                
        return results

    def visualize_results(self, results: Dict[str, List[float]]) -> None:
        """Visualize superradiance test results."""
        plt.figure(figsize=(15, 10))
        
        # Plot 1: Coherence and Amplification
        plt.subplot(221)
        plt.plot(results['coherence'], 'b.-', label='Coherence')
        plt.plot(results['amplification'], 'r.-', label='Amplification')
        plt.axhline(y=self.phi, color='g', linestyle='--', label='Phi Threshold')
        plt.title('Quantum State Evolution')
        plt.xlabel('Level')
        plt.ylabel('Magnitude')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Plot 2: Resonance Profile
        plt.subplot(222)
        plt.plot(results['resonance'], 'm.-')
        plt.title('Resonance Profile')
        plt.xlabel('Level')
        plt.ylabel('Resonance Deviation')
        plt.grid(True, alpha=0.3)
        
        # Plot 3: Phi Alignment
        plt.subplot(223)
        plt.plot(results['phi_alignment'], 'k.-')
        plt.title('Golden Ratio Alignment')
        plt.xlabel('Level')
        plt.ylabel('Deviation from Phi')
        plt.grid(True, alpha=0.3)
        
        # Plot 4: Phase Space
        plt.subplot(224)
        plt.scatter(results['coherence'], results['amplification'], 
                   c=results['resonance'], cmap='viridis')
        plt.colorbar(label='Resonance')
        plt.title('Quantum Phase Space')
        plt.xlabel('Coherence')
        plt.ylabel('Amplification')
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()

def run_superradiance_test():
    """Run superradiance analysis."""
    tester = SuperradianceTester()
    results = tester.test_superradiance()
    tester.visualize_results(results)

if __name__ == "__main__":
    run_superradiance_test()
