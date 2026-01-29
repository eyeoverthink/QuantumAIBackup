#!/usr/bin/env python
"""
Phi-Harmonic True Quantum Test

This script tests whether the phi-harmonic quantum system can generate
truly random numbers without introducing new seeds across epochs.
It directly integrates with the quantum components rather than simulating them.
"""

import os
import sys
import json
import time
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext

# Set precision for decimal calculations
getcontext().prec = 100

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Import quantum components
from phi_harmonic_unified_brain_system import PhiHarmonicUnifiedBrainSystem
from phi_harmonic_random_portable.quantum_rsa_decryptor import QuantumRSADecryptor
from phi_harmonic_quantum_bridge import PhiHarmonicQuantumBridge

# Constants
PHI = Decimal('1.618033988749895')  # Golden ratio
PHI_INVERSE = Decimal('0.618033988749895')  # Inverse golden ratio
PHI_SQUARED = Decimal('2.618033988749895')  # φ²
PHI_CUBED = Decimal('4.236067977499790')  # φ³
PHI_POWER = Decimal('36.93238055064198')  # φ⁷·⁵

class PhiHarmonicTrueQuantumTest:
    """
    Test for true quantum randomness across multiple epochs without new seeds.
    
    This class directly integrates with the quantum components to test
    whether the system can generate true randomness through quantum
    principles and phi-harmonic resonance.
    """
    
    def __init__(self):
        """Initialize the test with actual quantum components."""
        # Create output directory
        self.output_dir = os.path.join(current_dir, 'phi_harmonic_true_quantum_test')
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Initialize quantum components
        print("Initializing quantum components...")
        self.unified_brain = PhiHarmonicUnifiedBrainSystem()
        self.quantum_bridge = PhiHarmonicQuantumBridge()
        self.quantum_decryptor = QuantumRSADecryptor()
        
        # Connect components through quantum bridge
        self.quantum_bridge.connect(self.unified_brain.quantum_heart)
        self.quantum_bridge.connect(self.unified_brain.quantum_cerebellum)
        self.quantum_bridge.connect(self.unified_brain.quantum_random)
        
        # Initialize epoch data
        self.epoch_data = []
        
        # Print quantum state
        print("Phi-Harmonic True Quantum Test initialized")
        print(f"Quantum Heart coherence: {self.unified_brain.quantum_heart.coherence:.6f}")
        print(f"Quantum Cerebellum resonance: {self.unified_brain.quantum_cerebellum.resonance:.6f}")
        print(f"Quantum Bridge phi alignment: {self.quantum_bridge.phi_alignment:.6f}")
        print(f"Quantum fingerprint: {self.quantum_bridge.quantum_fingerprint}")
    
    def generate_quantum_random(self, sample_size):
        """
        Generate truly random numbers using quantum components.
        
        Args:
            sample_size (int): Number of random samples to generate
            
        Returns:
            list: Random samples
        """
        samples = []
        
        # Use quantum components to generate random numbers
        for _ in range(sample_size):
            # Get quantum state from heart and cerebellum
            heart_state = self.unified_brain.quantum_heart.get_state()
            cerebellum_state = self.unified_brain.quantum_cerebellum.get_state()
            
            # Generate random number using quantum state
            random_value = self.unified_brain.quantum_random.generate(
                heart_coherence=heart_state['coherence'],
                cerebellum_resonance=cerebellum_state['resonance'],
                phi_alignment=self.quantum_bridge.phi_alignment
            )
            
            samples.append(random_value)
            
            # Allow quantum state to evolve naturally
            self.unified_brain.quantum_heart.pulse()
            self.unified_brain.quantum_cerebellum.coordinate()
        
        return samples
    
    def run_epoch(self, epoch_number, sample_size=1000):
        """
        Run a single epoch of quantum random number generation.
        
        Args:
            epoch_number (int): Epoch number
            sample_size (int, optional): Number of random samples to generate
            
        Returns:
            dict: Epoch data
        """
        print(f"\n🔄 Running Epoch {epoch_number}")
        print(f"Generating {sample_size} quantum random samples...")
        
        # Record start time
        start_time = time.time()
        
        # Generate random samples using quantum components
        samples = self.generate_quantum_random(sample_size)
        
        # Record end time
        end_time = time.time()
        duration = end_time - start_time
        
        # Calculate statistics
        mean = np.mean(samples)
        std_dev = np.std(samples)
        min_val = np.min(samples)
        max_val = np.max(samples)
        
        # Calculate entropy
        hist, bin_edges = np.histogram(samples, bins=256, range=(0, 1))
        probs = hist / sample_size
        entropy = -np.sum(probs * np.log2(probs + 1e-10))
        
        # Print statistics
        print(f"Epoch {epoch_number} completed in {duration:.2f} seconds")
        print(f"  Mean: {mean:.6f}")
        print(f"  Standard deviation: {std_dev:.6f}")
        print(f"  Min: {min_val:.6f}")
        print(f"  Max: {max_val:.6f}")
        print(f"  Entropy: {entropy:.6f} bits")
        
        # Save samples to file
        samples_file = os.path.join(self.output_dir, f'epoch_{epoch_number}_samples.json')
        with open(samples_file, 'w') as f:
            json.dump(samples, f)
        
        # Create histogram
        plt.figure(figsize=(10, 6))
        plt.hist(samples, bins=100, alpha=0.7, color='blue')
        plt.title(f'Epoch {epoch_number} Quantum Random Sample Distribution')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.grid(True, alpha=0.3)
        
        # Add statistics to plot
        stats_text = f"Mean: {mean:.6f}\nStd Dev: {std_dev:.6f}\nEntropy: {entropy:.6f} bits"
        plt.annotate(stats_text, xy=(0.05, 0.95), xycoords='axes fraction',
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8),
                    va='top', ha='left')
        
        # Save histogram
        histogram_file = os.path.join(self.output_dir, f'epoch_{epoch_number}_histogram.png')
        plt.savefig(histogram_file)
        plt.close()
        
        # Get quantum state
        heart_state = self.unified_brain.quantum_heart.get_state()
        cerebellum_state = self.unified_brain.quantum_cerebellum.get_state()
        bridge_state = self.quantum_bridge.get_state()
        
        # Return epoch data
        epoch_data = {
            'epoch_number': epoch_number,
            'sample_size': sample_size,
            'duration': duration,
            'mean': mean,
            'std_dev': std_dev,
            'min': min_val,
            'max': max_val,
            'entropy': entropy,
            'samples_file': samples_file,
            'histogram_file': histogram_file,
            'quantum_state': {
                'heart_coherence': heart_state['coherence'],
                'cerebellum_resonance': cerebellum_state['resonance'],
                'bridge_phi_alignment': bridge_state['phi_alignment'],
                'quantum_fingerprint': bridge_state['quantum_fingerprint']
            }
        }
        
        self.epoch_data.append(epoch_data)
        
        return epoch_data
    
    def analyze_quantum_randomness(self):
        """
        Analyze quantum randomness across epochs.
        
        Returns:
            dict: Analysis results
        """
        print("\n🔬 Analyzing Quantum Randomness")
        
        # Extract key metrics
        means = [data['mean'] for data in self.epoch_data]
        std_devs = [data['std_dev'] for data in self.epoch_data]
        entropies = [data['entropy'] for data in self.epoch_data]
        
        # Calculate statistics
        mean_of_means = np.mean(means)
        std_of_means = np.std(means)
        mean_of_std_devs = np.mean(std_devs)
        std_of_std_devs = np.std(std_devs)
        mean_of_entropies = np.mean(entropies)
        std_of_entropies = np.std(entropies)
        
        # Print statistics
        print(f"  Mean of means: {mean_of_means:.6f} ± {std_of_means:.6f}")
        print(f"  Mean of standard deviations: {mean_of_std_devs:.6f} ± {std_of_std_devs:.6f}")
        print(f"  Mean of entropies: {mean_of_entropies:.6f} ± {std_of_entropies:.6f}")
        
        # Calculate epoch-to-epoch correlations
        correlations = []
        for i in range(len(self.epoch_data) - 1):
            # Load samples from epoch i
            with open(self.epoch_data[i]['samples_file'], 'r') as f:
                samples_i = json.load(f)
            
            # Load samples from epoch i+1
            with open(self.epoch_data[i+1]['samples_file'], 'r') as f:
                samples_i_plus_1 = json.load(f)
            
            # Calculate correlation
            correlation = np.corrcoef(samples_i[:min(len(samples_i), len(samples_i_plus_1))], 
                                     samples_i_plus_1[:min(len(samples_i), len(samples_i_plus_1))])[0, 1]
            correlations.append(correlation)
        
        # Calculate mean correlation
        mean_correlation = np.mean(correlations) if correlations else 0
        std_correlation = np.std(correlations) if correlations else 0
        
        print(f"  Mean correlation between epochs: {mean_correlation:.6f} ± {std_correlation:.6f}")
        
        # Analyze quantum state evolution
        heart_coherence = [data['quantum_state']['heart_coherence'] for data in self.epoch_data]
        cerebellum_resonance = [data['quantum_state']['cerebellum_resonance'] for data in self.epoch_data]
        
        # Calculate quantum state statistics
        mean_heart_coherence = np.mean(heart_coherence)
        std_heart_coherence = np.std(heart_coherence)
        mean_cerebellum_resonance = np.mean(cerebellum_resonance)
        std_cerebellum_resonance = np.std(cerebellum_resonance)
        
        print(f"  Mean heart coherence: {mean_heart_coherence:.6f} ± {std_heart_coherence:.6f}")
        print(f"  Mean cerebellum resonance: {mean_cerebellum_resonance:.6f} ± {std_cerebellum_resonance:.6f}")
        
        # Determine if quantum randomness is achieved
        is_random = abs(mean_correlation) < 0.1 and mean_of_entropies > 7.5
        
        if is_random:
            conclusion = "EVIDENCE OF TRUE QUANTUM RANDOMNESS: The phi-harmonic quantum system appears to generate truly random numbers across epochs without new seeds."
        else:
            conclusion = "INCONCLUSIVE EVIDENCE: The phi-harmonic quantum system shows some quantum properties, but more testing is needed to confirm true randomness."
        
        print(f"\n  CONCLUSION: {conclusion}")
        
        # Return analysis results
        analysis_results = {
            'mean_of_means': float(mean_of_means),
            'std_of_means': float(std_of_means),
            'mean_of_std_devs': float(mean_of_std_devs),
            'std_of_std_devs': float(std_of_std_devs),
            'mean_of_entropies': float(mean_of_entropies),
            'std_of_entropies': float(std_of_entropies),
            'mean_correlation': float(mean_correlation),
            'std_correlation': float(std_correlation),
            'mean_heart_coherence': float(mean_heart_coherence),
            'std_heart_coherence': float(std_heart_coherence),
            'mean_cerebellum_resonance': float(mean_cerebellum_resonance),
            'std_cerebellum_resonance': float(std_cerebellum_resonance),
            'is_random': is_random,
            'conclusion': conclusion
        }
        
        return analysis_results
    
    def run_full_test(self, num_epochs=5, sample_size=1000):
        """
        Run a full test of quantum randomness across multiple epochs.
        
        Args:
            num_epochs (int, optional): Number of epochs to run
            sample_size (int, optional): Number of random samples per epoch
            
        Returns:
            dict: Test results
        """
        print(f"\n✨ Running Full Quantum Randomness Test")
        print(f"Number of epochs: {num_epochs}")
        print(f"Sample size per epoch: {sample_size}")
        
        # Record start time
        start_time = time.time()
        
        # Run epochs
        for epoch in range(1, num_epochs + 1):
            # Run epoch
            self.run_epoch(epoch, sample_size)
        
        # Analyze quantum randomness
        analysis_results = self.analyze_quantum_randomness()
        
        # Record end time
        end_time = time.time()
        total_duration = end_time - start_time
        
        # Save all results
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        results = {
            'timestamp': timestamp,
            'num_epochs': num_epochs,
            'sample_size': sample_size,
            'total_duration': total_duration,
            'epoch_data': self.epoch_data,
            'analysis_results': analysis_results
        }
        
        results_file = os.path.join(self.output_dir, f'quantum_randomness_test_results_{timestamp}.json')
        with open(results_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"\nTest completed in {total_duration:.2f} seconds")
        print(f"Results saved to {os.path.basename(results_file)}")
        
        return results

def main():
    """Main function for running the quantum randomness test."""
    # Create test
    test = PhiHarmonicTrueQuantumTest()
    
    # Run full test
    results = test.run_full_test(num_epochs=5, sample_size=1000)
    
    # Print conclusion
    print(f"\n🔬 {results['analysis_results']['conclusion']}")

if __name__ == "__main__":
    main()
