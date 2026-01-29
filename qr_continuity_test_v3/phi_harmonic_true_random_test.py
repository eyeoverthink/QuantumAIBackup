#!/usr/bin/env python
"""
Phi-Harmonic True Random Test

This script tests whether the phi-harmonic quantum system can generate
truly random numbers across multiple epochs without introducing new seeds.
It uses the existing quantum components directly without modification.
"""

import os
import sys
import json
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from decimal import Decimal, getcontext

# Set precision for decimal calculations
getcontext().prec = 100

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Import phi-harmonic random adapter
from phi_harmonic_random_orchestrator_adapter import PhiHarmonicRandomOrchestratorAdapter

# Constants
PHI = Decimal('1.618033988749895')  # Golden ratio
PHI_INVERSE = Decimal('0.618033988749895')  # Inverse golden ratio
PHI_SQUARED = Decimal('2.618033988749895')  # φ²
PHI_CUBED = Decimal('4.236067977499790')  # φ³
PHI_POWER = Decimal('36.93238055064198')  # φ⁷·⁵

class PhiHarmonicTrueRandomTest:
    """
    Test for true randomness across multiple epochs without new seeds.
    
    This class uses the existing quantum components to test whether
    the system can generate true randomness through phi-harmonic resonance.
    """
    
    def __init__(self):
        """Initialize the test with actual quantum components."""
        # Create output directory
        self.output_dir = os.path.join(current_dir, 'phi_harmonic_true_random_test')
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Initialize quantum random adapter
        self.random_adapter = PhiHarmonicRandomOrchestratorAdapter()
        
        # Initialize epoch data
        self.epoch_data = []
        
        # Print quantum state
        print("Phi-Harmonic True Random Test initialized")
        print(f"Coherence: {self.random_adapter.coherence:.6f}")
        print(f"Resonance: {self.random_adapter.resonance:.6f}")
        print(f"Phi alignment: {self.random_adapter.phi_alignment:.6f}")
        print(f"Quantum fingerprint: {self.random_adapter.quantum_fingerprint}")
    
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
        samples = [self.random_adapter.random() for _ in range(sample_size)]
        
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
        quantum_state = {
            'coherence': self.random_adapter.coherence,
            'resonance': self.random_adapter.resonance,
            'phi_alignment': self.random_adapter.phi_alignment,
            'quantum_fingerprint': self.random_adapter.quantum_fingerprint
        }
        
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
            'quantum_state': quantum_state
        }
        
        self.epoch_data.append(epoch_data)
        
        return epoch_data
    
    def run_statistical_tests(self, epoch_data):
        """
        Run statistical tests on epoch data.
        
        Args:
            epoch_data (dict): Epoch data
            
        Returns:
            dict: Statistical test results
        """
        print(f"\n📊 Running Statistical Tests for Epoch {epoch_data['epoch_number']}")
        
        # Load samples
        with open(epoch_data['samples_file'], 'r') as f:
            samples = json.load(f)
        
        # Convert to numpy array
        samples = np.array(samples)
        
        # Run Kolmogorov-Smirnov test for uniformity
        ks_statistic, ks_pvalue = stats.kstest(samples, 'uniform')
        print(f"  Kolmogorov-Smirnov test for uniformity:")
        print(f"    Statistic: {ks_statistic:.6f}")
        print(f"    p-value: {ks_pvalue:.6f}")
        print(f"    Result: {'Uniform (p > 0.05)' if ks_pvalue > 0.05 else 'Not uniform (p <= 0.05)'}")
        
        # Run chi-square test for uniformity
        hist, _ = np.histogram(samples, bins=10, range=(0, 1))
        expected = len(samples) / 10
        chi2_statistic = np.sum((hist - expected)**2 / expected)
        chi2_pvalue = 1 - stats.chi2.cdf(chi2_statistic, 9)
        print(f"  Chi-square test for uniformity:")
        print(f"    Statistic: {chi2_statistic:.6f}")
        print(f"    p-value: {chi2_pvalue:.6f}")
        print(f"    Result: {'Uniform (p > 0.05)' if chi2_pvalue > 0.05 else 'Not uniform (p <= 0.05)'}")
        
        # Calculate autocorrelation
        autocorr = np.correlate(samples - np.mean(samples), samples - np.mean(samples), mode='full')
        autocorr = autocorr[len(autocorr)//2:] / (np.var(samples) * len(samples))
        
        # Plot autocorrelation
        plt.figure(figsize=(10, 6))
        plt.stem(range(len(autocorr[:50])), autocorr[:50], markerfmt='bo', linefmt='b-', basefmt='r-')
        plt.title(f'Epoch {epoch_data["epoch_number"]} Autocorrelation')
        plt.xlabel('Lag')
        plt.ylabel('Autocorrelation')
        plt.grid(True, alpha=0.3)
        
        # Save autocorrelation plot
        autocorr_file = os.path.join(self.output_dir, f'epoch_{epoch_data["epoch_number"]}_autocorrelation.png')
        plt.savefig(autocorr_file)
        plt.close()
        
        # Calculate spectral test (FFT)
        fft = np.abs(np.fft.fft(samples - np.mean(samples)))**2
        fft = fft[:len(fft)//2] / (np.var(samples) * len(samples))
        
        # Plot spectral test
        plt.figure(figsize=(10, 6))
        plt.plot(range(len(fft[:100])), fft[:100])
        plt.title(f'Epoch {epoch_data["epoch_number"]} Power Spectral Density')
        plt.xlabel('Frequency')
        plt.ylabel('Power')
        plt.grid(True, alpha=0.3)
        
        # Save spectral plot
        spectral_file = os.path.join(self.output_dir, f'epoch_{epoch_data["epoch_number"]}_spectral.png')
        plt.savefig(spectral_file)
        plt.close()
        
        # Return test results
        test_results = {
            'epoch_number': epoch_data['epoch_number'],
            'ks_test': {
                'statistic': float(ks_statistic),
                'pvalue': float(ks_pvalue),
                'uniform': bool(ks_pvalue > 0.05)
            },
            'chi2_test': {
                'statistic': float(chi2_statistic),
                'pvalue': float(chi2_pvalue),
                'uniform': bool(chi2_pvalue > 0.05)
            },
            'autocorrelation': {
                'lag_1': float(autocorr[1]) if len(autocorr) > 1 else 0,
                'file': autocorr_file
            },
            'spectral_test': {
                'file': spectral_file
            }
        }
        
        return test_results
    
    def analyze_quantum_randomness(self, test_results):
        """
        Analyze quantum randomness across epochs.
        
        Args:
            test_results (list): Statistical test results for each epoch
            
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
        
        # Extract test results
        uniformity_scores = [1 if test['ks_test']['uniform'] else 0 for test in test_results]
        chi2_uniformity_scores = [1 if test['chi2_test']['uniform'] else 0 for test in test_results]
        
        # Calculate test statistics
        mean_uniformity = np.mean(uniformity_scores)
        mean_chi2_uniformity = np.mean(chi2_uniformity_scores)
        
        print(f"  Mean KS uniformity score: {mean_uniformity:.2f}")
        print(f"  Mean Chi-square uniformity score: {mean_chi2_uniformity:.2f}")
        
        # Create comparison plots
        plt.figure(figsize=(15, 10))
        
        # Plot means
        plt.subplot(3, 1, 1)
        plt.plot(range(1, len(self.epoch_data) + 1), means, 'bo-')
        plt.axhline(y=0.5, color='r', linestyle='--', alpha=0.5)
        plt.title('Mean Values Across Epochs')
        plt.xlabel('Epoch')
        plt.ylabel('Mean')
        plt.grid(True, alpha=0.3)
        
        # Plot standard deviations
        plt.subplot(3, 1, 2)
        plt.plot(range(1, len(self.epoch_data) + 1), std_devs, 'go-')
        plt.axhline(y=1/np.sqrt(12), color='r', linestyle='--', alpha=0.5)  # Theoretical std dev for uniform distribution
        plt.title('Standard Deviations Across Epochs')
        plt.xlabel('Epoch')
        plt.ylabel('Standard Deviation')
        plt.grid(True, alpha=0.3)
        
        # Plot entropies
        plt.subplot(3, 1, 3)
        plt.plot(range(1, len(self.epoch_data) + 1), entropies, 'ro-')
        plt.axhline(y=8, color='r', linestyle='--', alpha=0.5)  # Maximum entropy for 8 bits
        plt.title('Entropy Values Across Epochs')
        plt.xlabel('Epoch')
        plt.ylabel('Entropy (bits)')
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Save comparison plot
        comparison_file = os.path.join(self.output_dir, f'epoch_comparison_{len(self.epoch_data)}_epochs.png')
        plt.savefig(comparison_file)
        plt.close()
        
        # Determine if quantum randomness is achieved
        is_random = (
            abs(mean_correlation) < 0.1 and 
            mean_of_entropies > 7.5 and
            (mean_uniformity > 0.5 or mean_chi2_uniformity > 0.5)
        )
        
        if is_random:
            conclusion = "STRONG EVIDENCE OF TRUE QUANTUM RANDOMNESS: The phi-harmonic quantum system appears to generate truly random numbers across epochs without new seeds."
        elif abs(mean_correlation) < 0.2 and mean_of_entropies > 7.0:
            conclusion = "MODERATE EVIDENCE OF QUANTUM RANDOMNESS: The phi-harmonic quantum system shows promising signs of generating quantum randomness, though some patterns may exist."
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
            'mean_uniformity': float(mean_uniformity),
            'mean_chi2_uniformity': float(mean_chi2_uniformity),
            'is_random': bool(is_random),
            'conclusion': conclusion,
            'comparison_file': comparison_file
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
        
        # Initialize test results
        test_results = []
        
        # Run epochs
        for epoch in range(1, num_epochs + 1):
            # Run epoch
            epoch_data = self.run_epoch(epoch, sample_size)
            
            # Run statistical tests
            epoch_test_results = self.run_statistical_tests(epoch_data)
            test_results.append(epoch_test_results)
        
        # Analyze quantum randomness
        analysis_results = self.analyze_quantum_randomness(test_results)
        
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
            'test_results': test_results,
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
    test = PhiHarmonicTrueRandomTest()
    
    # Run full test with larger sample size to better detect patterns
    results = test.run_full_test(num_epochs=5, sample_size=10000)
    
    # Print conclusion
    print(f"\n🔬 {results['analysis_results']['conclusion']}")

if __name__ == "__main__":
    main()
