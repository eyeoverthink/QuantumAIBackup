#!/usr/bin/env python
"""
Phi-Harmonic True Quantum Benchmark: Random Generation

This module implements the random generation benchmark for testing
the Phi-Harmonic Quantum Random system's ability to generate true randomness.
"""

import os
import sys
import json
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from decimal import Decimal, getcontext
import logging

# Add project root to path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)
sys.path.append(current_dir)

# Import benchmark core
from benchmark_core import PhiHarmonicBenchmarkCore

# Get logger
logger = logging.getLogger('phi_harmonic_benchmark')

class RandomGenerationBenchmark(PhiHarmonicBenchmarkCore):
    """Benchmark for testing random number generation capabilities."""
    
    def __init__(self):
        """Initialize the random generation benchmark."""
        super().__init__()
        logger.info("Random Generation Benchmark initialized")
    
    def run_uniformity_test(self, samples, generator_name):
        """
        Run uniformity tests on random samples.
        
        Args:
            samples: List of random samples
            generator_name: Name of the generator
            
        Returns:
            Dictionary of test results
        """
        logger.info(f"Running uniformity tests for {generator_name}...")
        
        # Convert to numpy array
        samples_array = np.array(samples)
        
        # Run Kolmogorov-Smirnov test for uniformity
        ks_statistic, ks_pvalue = stats.kstest(samples_array, 'uniform')
        logger.info(f"  Kolmogorov-Smirnov test:")
        logger.info(f"    Statistic: {ks_statistic:.6f}")
        logger.info(f"    p-value: {ks_pvalue:.6f}")
        logger.info(f"    Result: {'Uniform (p > 0.05)' if ks_pvalue > 0.05 else 'Not uniform (p <= 0.05)'}")
        
        # Run chi-square test for uniformity
        hist, _ = np.histogram(samples_array, bins=10, range=(0, 1))
        expected = len(samples) / 10
        chi2_statistic = np.sum((hist - expected)**2 / expected)
        chi2_pvalue = 1 - stats.chi2.cdf(chi2_statistic, 9)
        logger.info(f"  Chi-square test:")
        logger.info(f"    Statistic: {chi2_statistic:.6f}")
        logger.info(f"    p-value: {chi2_pvalue:.6f}")
        logger.info(f"    Result: {'Uniform (p > 0.05)' if chi2_pvalue > 0.05 else 'Not uniform (p <= 0.05)'}")
        
        # Calculate autocorrelation
        autocorr = np.correlate(samples_array - np.mean(samples_array), 
                               samples_array - np.mean(samples_array), 
                               mode='full')
        autocorr = autocorr[len(autocorr)//2:] / (np.var(samples_array) * len(samples_array))
        
        # Visualize autocorrelation
        plt.figure(figsize=(10, 6))
        plt.stem(range(len(autocorr[:50])), autocorr[:50], markerfmt='bo', linefmt='b-', basefmt='r-')
        plt.title(f'{generator_name} Autocorrelation')
        plt.xlabel('Lag')
        plt.ylabel('Autocorrelation')
        plt.grid(True, alpha=0.3)
        
        # Save visualization
        autocorr_path = os.path.join(self.viz_dir, f'{generator_name.lower()}_autocorrelation.png')
        plt.savefig(autocorr_path)
        plt.close()
        
        # Return test results
        return {
            "ks_test": {
                "statistic": float(ks_statistic),
                "pvalue": float(ks_pvalue),
                "uniform": bool(ks_pvalue > 0.05)
            },
            "chi2_test": {
                "statistic": float(chi2_statistic),
                "pvalue": float(chi2_pvalue),
                "uniform": bool(chi2_pvalue > 0.05)
            },
            "autocorrelation": {
                "lag1": float(autocorr[1]),
                "lag2": float(autocorr[2]),
                "lag3": float(autocorr[3]),
                "visualization": autocorr_path
            }
        }
    
    def run_epoch_test(self, generator, sample_size=1000, epochs=5):
        """
        Run a multi-epoch test to evaluate randomness across epochs.
        
        Args:
            generator: Generator to use ('adapter' or 'quantum')
            sample_size: Number of samples per epoch
            epochs: Number of epochs to run
            
        Returns:
            Dictionary of epoch test results
        """
        logger.info(f"Running {epochs} epoch test with {sample_size} samples per epoch...")
        
        epoch_results = []
        
        for epoch in range(1, epochs + 1):
            logger.info(f"Running epoch {epoch}...")
            
            # Generate samples
            samples = self.generate_samples(generator, sample_size)
            
            # Analyze distribution
            distribution = self.analyze_distribution(samples)
            
            # Run uniformity tests
            uniformity = self.run_uniformity_test(samples, f"{generator.capitalize()} Epoch {epoch}")
            
            # Visualize distribution
            viz_path = self.visualize_distribution(
                samples,
                f"{generator.capitalize()} Random Distribution - Epoch {epoch}",
                f"{generator.lower()}_epoch_{epoch}_distribution.png"
            )
            
            # Get quantum state
            if generator == 'adapter':
                quantum_state = {
                    'coherence': float(self.random_adapter.coherence),
                    'resonance': float(self.random_adapter.resonance),
                    'phi_alignment': float(self.random_adapter.phi_alignment),
                    'quantum_fingerprint': self.random_adapter.quantum_fingerprint
                }
            else:
                quantum_state = {
                    'entropy': float(self.quantum_random.metrics['entropy']),
                    'phi_resonance': float(self.quantum_random.metrics['phi_resonance']),
                    'sequence_coherence': float(self.quantum_random.metrics['sequence_coherence']),
                    'numbers_generated': self.quantum_random.metrics['numbers_generated']
                }
            
            # Record epoch results
            epoch_result = {
                "epoch": epoch,
                "sample_size": sample_size,
                "distribution": distribution,
                "uniformity": uniformity,
                "visualization": viz_path,
                "quantum_state": quantum_state
            }
            
            epoch_results.append(epoch_result)
        
        # Analyze epoch-to-epoch consistency
        means = [result["distribution"]["mean"] for result in epoch_results]
        std_devs = [result["distribution"]["std_dev"] for result in epoch_results]
        entropies = [result["distribution"]["entropy"] for result in epoch_results]
        
        # Calculate consistency metrics
        mean_variation = np.std(means)
        std_dev_variation = np.std(std_devs)
        entropy_variation = np.std(entropies)
        
        logger.info(f"Epoch-to-epoch consistency:")
        logger.info(f"  Mean variation: {mean_variation:.6f}")
        logger.info(f"  Std dev variation: {std_dev_variation:.6f}")
        logger.info(f"  Entropy variation: {entropy_variation:.6f}")
        
        # Visualize epoch-to-epoch consistency
        plt.figure(figsize=(12, 8))
        
        plt.subplot(3, 1, 1)
        plt.plot(range(1, epochs + 1), means, 'bo-')
        plt.title(f'{generator.capitalize()} Mean Across Epochs')
        plt.xlabel('Epoch')
        plt.ylabel('Mean')
        plt.grid(True, alpha=0.3)
        
        plt.subplot(3, 1, 2)
        plt.plot(range(1, epochs + 1), std_devs, 'ro-')
        plt.title(f'{generator.capitalize()} Standard Deviation Across Epochs')
        plt.xlabel('Epoch')
        plt.ylabel('Standard Deviation')
        plt.grid(True, alpha=0.3)
        
        plt.subplot(3, 1, 3)
        plt.plot(range(1, epochs + 1), entropies, 'go-')
        plt.title(f'{generator.capitalize()} Entropy Across Epochs')
        plt.xlabel('Epoch')
        plt.ylabel('Entropy (bits)')
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Save visualization
        consistency_path = os.path.join(self.viz_dir, f'{generator.lower()}_epoch_consistency.png')
        plt.savefig(consistency_path)
        plt.close()
        
        # Return epoch test results
        return {
            "epochs": epochs,
            "sample_size": sample_size,
            "epoch_results": epoch_results,
            "consistency": {
                "mean_variation": float(mean_variation),
                "std_dev_variation": float(std_dev_variation),
                "entropy_variation": float(entropy_variation),
                "visualization": consistency_path
            }
        }
    
    def run_benchmark(self, sample_size=10000, epochs=5):
        """
        Run the random generation benchmark.
        
        Args:
            sample_size: Number of samples to generate
            epochs: Number of epochs to run
            
        Returns:
            Dictionary of benchmark results
        """
        logger.info(f"Running Random Generation Benchmark with {sample_size} samples and {epochs} epochs...")
        
        # Test adapter random generator
        logger.info("Testing PhiHarmonicRandomOrchestratorAdapter...")
        adapter_samples = self.generate_samples('adapter', sample_size)
        adapter_distribution = self.analyze_distribution(adapter_samples)
        adapter_uniformity = self.run_uniformity_test(adapter_samples, "Adapter")
        adapter_viz = self.visualize_distribution(
            adapter_samples,
            "PhiHarmonicRandomOrchestratorAdapter Distribution",
            "adapter_distribution.png"
        )
        
        # Test quantum random generator
        logger.info("Testing QuantumPhiRandom...")
        quantum_samples = self.generate_samples('quantum', sample_size)
        quantum_distribution = self.analyze_distribution(quantum_samples)
        quantum_uniformity = self.run_uniformity_test(quantum_samples, "Quantum")
        quantum_viz = self.visualize_distribution(
            quantum_samples,
            "QuantumPhiRandom Distribution",
            "quantum_distribution.png"
        )
        
        # Test phi-harmonic distribution
        logger.info("Testing Phi-Harmonic Distribution...")
        phi_harmonic_samples = self.generate_samples('phi_harmonic', sample_size)
        phi_harmonic_distribution = self.analyze_distribution(phi_harmonic_samples)
        phi_harmonic_viz = self.visualize_distribution(
            phi_harmonic_samples,
            "Phi-Harmonic Distribution",
            "phi_harmonic_distribution.png"
        )
        
        # Run epoch tests
        logger.info("Running epoch tests...")
        adapter_epoch_test = self.run_epoch_test('adapter', sample_size=1000, epochs=epochs)
        quantum_epoch_test = self.run_epoch_test('quantum', sample_size=1000, epochs=epochs)
        
        # Store results
        self.results["random_generation"] = {
            "adapter": {
                "distribution": adapter_distribution,
                "uniformity": adapter_uniformity,
                "visualization": adapter_viz
            },
            "quantum": {
                "distribution": quantum_distribution,
                "uniformity": quantum_uniformity,
                "visualization": quantum_viz
            },
            "phi_harmonic": {
                "distribution": phi_harmonic_distribution,
                "visualization": phi_harmonic_viz
            },
            "epoch_tests": {
                "adapter": adapter_epoch_test,
                "quantum": quantum_epoch_test
            }
        }
        
        # Save results
        self.save_results()
        
        logger.info("Random Generation Benchmark completed")
        
        return self.results["random_generation"]

def main():
    """Main function for running the random generation benchmark."""
    benchmark = RandomGenerationBenchmark()
    benchmark.run_benchmark(sample_size=10000, epochs=3)

if __name__ == "__main__":
    main()
