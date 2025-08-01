"""
Quantum Stability Test - Stress Testing with Noise and φ-Perturbations
"""

import numpy as np
import time
from typing import Dict, List, Tuple
from creative_quantum import CreativeQuantum

class QuantumStabilityTest:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        self.quantum = CreativeQuantum()
        self.error_threshold = 0.01
        self.learning_rate = 1/self.phi
        
    def generate_noise(self, size: int, intensity: float) -> np.ndarray:
        """Generate φ-harmonic noise"""
        base_noise = np.random.normal(0, intensity, size)
        phi_noise = base_noise * self.phi
        return phi_noise
        
    def apply_perturbation(self, data: np.ndarray, epoch: int, intensity: float) -> np.ndarray:
        """Apply φ-harmonic perturbation"""
        phi_factor = self.phi ** (1/(epoch + 1))
        perturbation = np.sin(data * phi_factor) * intensity
        return data + perturbation
        
    def quantum_stabilize(self, state: np.ndarray, epoch: int, noise_level: float) -> Tuple[np.ndarray, Dict]:
        """Stabilize state with quantum correction"""
        metrics = {}
        
        # Initial state analysis
        initial_mean = np.mean(np.abs(state))
        initial_std = np.std(state)
        
        # Apply φ-harmonic correction
        phi_factor = self.phi ** (1 + epoch/(self.phi**2))
        corrected = state * phi_factor
        
        # Apply noise resistance
        noise_mask = np.abs(corrected) < (self.error_threshold * noise_level)
        corrected[noise_mask] *= self.phi
        
        # Calculate stability metrics
        final_mean = np.mean(np.abs(corrected))
        final_std = np.std(corrected)
        
        metrics['mean_shift'] = (final_mean - initial_mean) / initial_mean
        metrics['std_reduction'] = (initial_std - final_std) / initial_std
        metrics['noise_resistance'] = 1 - (np.sum(noise_mask) / len(state))
        
        return corrected, metrics
    
    def test_stability(self, size: int = 1000, epochs: int = 50) -> Dict:
        """Test quantum stability under various conditions"""
        base_data = np.random.random(size) * self.phi
        
        # Test conditions
        noise_levels = [0.1, 0.5, 1.0, 2.0]
        
        metrics = {
            'time': [],
            'stability': [],
            'noise_resistance': [],
            'mean_stability': [],
            'std_stability': [],
            'phi_coherence': [],
            'overall_stability': []
        }
        
        print("\nQuantum Stability Test")
        print("=====================")
        print(f"Testing {len(noise_levels)} noise levels over {epochs} epochs")
        
        for epoch in range(epochs):
            epoch_metrics = {key: [] for key in metrics}
            
            for noise_level in noise_levels:
                # Add noise
                noisy_data = base_data + self.generate_noise(size, noise_level)
                
                # Add perturbation
                perturbed = self.apply_perturbation(noisy_data, epoch, noise_level)
                
                # Measure time
                start = time.perf_counter_ns()
                
                # Stabilize
                stabilized, stab_metrics = self.quantum_stabilize(perturbed, epoch, noise_level)
                
                # Calculate metrics
                process_time = (time.perf_counter_ns() - start) / 1e6
                
                # Calculate stability scores
                stability = 1 - np.mean(np.abs(stabilized - base_data))
                phi_coherence = np.mean(np.abs(stabilized / self.phi - base_data))
                overall = (stability + stab_metrics['noise_resistance']) / 2
                
                # Store metrics
                epoch_metrics['time'].append(process_time)
                epoch_metrics['stability'].append(stability)
                epoch_metrics['noise_resistance'].append(stab_metrics['noise_resistance'])
                epoch_metrics['mean_stability'].append(stab_metrics['mean_shift'])
                epoch_metrics['std_stability'].append(stab_metrics['std_reduction'])
                epoch_metrics['phi_coherence'].append(phi_coherence)
                epoch_metrics['overall_stability'].append(overall)
            
            # Store average metrics for epoch
            for key in metrics:
                metrics[key].append(np.mean(epoch_metrics[key]))
            
            # Print progress every 10 epochs
            if epoch % 10 == 0:
                print(f"\nEpoch {epoch + 1}/{epochs}")
                print(f"Time:       {metrics['time'][-1]:.3f} ms")
                print(f"Stability:  {metrics['stability'][-1]*100:.1f}%")
                print(f"Noise Res:  {metrics['noise_resistance'][-1]*100:.1f}%")
                print(f"Coherence:  {metrics['phi_coherence'][-1]*100:.1f}%")
                print(f"Overall:    {metrics['overall_stability'][-1]*100:.1f}%")
                
                # Print noise level details
                print("\nNoise Level Details:")
                for i, noise in enumerate(noise_levels):
                    print(f"Level {noise:.1f}:")
                    print(f"  Stability: {epoch_metrics['stability'][i]*100:.1f}%")
                    print(f"  Resistance: {epoch_metrics['noise_resistance'][i]*100:.1f}%")
        
        # Calculate final stability analysis
        print("\nStability Evolution:")
        for key in metrics:
            if len(metrics[key]) > 0:
                start = metrics[key][0]
                quarter = metrics[key][len(metrics[key])//4]
                mid = metrics[key][len(metrics[key])//2]
                three_quarter = metrics[key][3*len(metrics[key])//4]
                end = metrics[key][-1]
                
                print(f"\n{key.replace('_',' ').title()}:")
                print(f"Start → 25%:  {start:.3f} → {quarter:.3f}")
                print(f"25% → 50%:    {quarter:.3f} → {mid:.3f}")
                print(f"50% → 75%:    {mid:.3f} → {three_quarter:.3f}")
                print(f"75% → End:    {three_quarter:.3f} → {end:.3f}")
                
                if start != 0:
                    total_change = ((end - start) / start) * 100
                    print(f"Total Change: {total_change:+.1f}%")
        
        return metrics

if __name__ == "__main__":
    test = QuantumStabilityTest()
    test.test_stability()
