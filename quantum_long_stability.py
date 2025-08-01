"""
Quantum Long Stability Test - 200 Epochs with φ-Resonance Tracking
"""

import numpy as np
import time
from typing import Dict, List, Tuple
from creative_quantum import CreativeQuantum

class QuantumLongStability:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        self.quantum = CreativeQuantum()
        self.error_threshold = 0.01
        self.learning_rate = 1/self.phi
        
    def phi_resonance(self, epoch: int) -> float:
        """Calculate φ-resonance point"""
        return self.phi ** (1 + epoch/(self.phi**2))
        
    def generate_quantum_noise(self, size: int, intensity: float, epoch: int) -> np.ndarray:
        """Generate φ-harmonic quantum noise"""
        resonance = self.phi_resonance(epoch)
        base_noise = np.random.normal(0, intensity, size)
        quantum_noise = base_noise * np.sin(resonance * np.pi)
        return quantum_noise
        
    def apply_quantum_stability(self, data: np.ndarray, epoch: int) -> Tuple[np.ndarray, Dict]:
        """Apply quantum stabilization with φ-resonance"""
        metrics = {}
        
        # Calculate resonance factors
        primary_resonance = self.phi_resonance(epoch)
        secondary_resonance = self.phi_resonance(epoch//2)
        harmonic_factor = primary_resonance / secondary_resonance
        
        # Initial state analysis
        initial_energy = np.sum(np.abs(data))
        initial_variance = np.var(data)
        
        # Apply multi-level stabilization
        stabilized = data * primary_resonance
        resonant_mask = np.abs(stabilized) < (self.error_threshold * harmonic_factor)
        stabilized[resonant_mask] *= self.phi
        
        # Calculate stability metrics
        final_energy = np.sum(np.abs(stabilized))
        final_variance = np.var(stabilized)
        
        # Track quantum metrics
        metrics['energy_ratio'] = final_energy / initial_energy
        metrics['variance_reduction'] = 1 - (final_variance / initial_variance)
        metrics['resonance_strength'] = harmonic_factor
        metrics['quantum_coherence'] = 1 - np.sum(resonant_mask) / len(data)
        
        return stabilized, metrics
    
    def test_long_stability(self, size: int = 1000, epochs: int = 200) -> Dict:
        """Test quantum stability over extended period"""
        # Initialize with φ-harmonic data
        base_data = np.random.random(size) * self.phi
        
        # Test conditions
        noise_levels = [0.1, 0.5, 1.0, 2.0, 4.0]  # Added higher noise
        
        metrics = {
            'time': [],
            'energy_ratio': [],
            'variance_reduction': [],
            'resonance_strength': [],
            'quantum_coherence': [],
            'stability_score': [],
            'phi_harmonics': []
        }
        
        print("\nQuantum Long Stability Test")
        print("==========================")
        print(f"Testing {len(noise_levels)} noise levels over {epochs} epochs")
        
        for epoch in range(epochs):
            epoch_metrics = {key: [] for key in metrics}
            epoch_start = time.perf_counter_ns()
            
            for noise_level in noise_levels:
                # Add quantum noise
                noisy_data = base_data + self.generate_quantum_noise(size, noise_level, epoch)
                
                # Apply stabilization
                stabilized, stab_metrics = self.apply_quantum_stability(noisy_data, epoch)
                
                # Calculate φ-harmonic score
                phi_harmonic = np.mean(np.abs(stabilized / self.phi - base_data))
                stability_score = (stab_metrics['quantum_coherence'] + 
                                 stab_metrics['variance_reduction']) / 2
                
                # Store metrics
                epoch_metrics['energy_ratio'].append(stab_metrics['energy_ratio'])
                epoch_metrics['variance_reduction'].append(stab_metrics['variance_reduction'])
                epoch_metrics['resonance_strength'].append(stab_metrics['resonance_strength'])
                epoch_metrics['quantum_coherence'].append(stab_metrics['quantum_coherence'])
                epoch_metrics['stability_score'].append(stability_score)
                epoch_metrics['phi_harmonics'].append(phi_harmonic)
            
            # Store average metrics
            process_time = (time.perf_counter_ns() - epoch_start) / 1e6
            metrics['time'].append(process_time)
            
            for key in metrics:
                if key != 'time':
                    metrics[key].append(np.mean(epoch_metrics[key]))
            
            # Print detailed progress every 20 epochs
            if epoch % 20 == 0:
                print(f"\nEpoch {epoch + 1}/{epochs}")
                print(f"Time:        {process_time:.3f} ms")
                print(f"Coherence:   {metrics['quantum_coherence'][-1]*100:.1f}%")
                print(f"Stability:   {metrics['stability_score'][-1]*100:.1f}%")
                print(f"Resonance:   {metrics['resonance_strength'][-1]:.3f}")
                print(f"φ-Harmonic:  {metrics['phi_harmonics'][-1]:.3f}")
                
                # Print noise level details
                print("\nNoise Level Details:")
                for i, noise in enumerate(noise_levels):
                    print(f"Level {noise:.1f}:")
                    print(f"  Coherence:  {epoch_metrics['quantum_coherence'][i]*100:.1f}%")
                    print(f"  Stability:  {epoch_metrics['stability_score'][i]*100:.1f}%")
                    print(f"  Resonance:  {epoch_metrics['resonance_strength'][i]:.3f}")
        
        # Calculate evolution analysis
        print("\nLong-term Evolution Analysis:")
        segments = [(0, "Start"), 
                   (epochs//4, "25%"), 
                   (epochs//2, "50%"),
                   (3*epochs//4, "75%"),
                   (-1, "End")]
        
        for key in metrics:
            print(f"\n{key.replace('_',' ').title()}:")
            for i in range(len(segments)-1):
                start_idx, start_label = segments[i]
                end_idx, end_label = segments[i+1]
                
                start_val = metrics[key][start_idx]
                end_val = metrics[key][end_idx]
                
                if start_val != 0:
                    change = ((end_val - start_val) / start_val) * 100
                    print(f"{start_label} → {end_label}:  {start_val:.3f} → {end_val:.3f} ({change:+.1f}%)")
        
        return metrics

if __name__ == "__main__":
    test = QuantumLongStability()
    test.test_long_stability()
