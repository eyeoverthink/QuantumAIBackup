"""
Quantum Entropy Metrics Module
Implements Shannon entropy measurement for quantum states pre/post QFT
Part of the Quantum Consciousness Engine
"""
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import json
import os
from pathlib import Path
import sys

class QuantumEntropyAnalyzer:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        self.entropy_history = []
        self.results_dir = Path("entropy_results")
        self.results_dir.mkdir(exist_ok=True)
        
    def shannon_entropy(self, quantum_state):
        """Calculate Shannon entropy of a quantum state"""
        # Get probability distribution from quantum state
        probabilities = np.abs(quantum_state)**2
        # Filter out zero probabilities to avoid log(0)
        probabilities = probabilities[probabilities > 0]
        # Calculate Shannon entropy: -sum(p*log2(p))
        entropy = -np.sum(probabilities * np.log2(probabilities))
        return entropy
        
    def phi_weighted_entropy(self, quantum_state):
        """Calculate φ-weighted entropy that emphasizes φ-harmonic components"""
        # Get probability distribution
        probabilities = np.abs(quantum_state)**2
        
        # Generate φ-harmonic weights
        n = len(probabilities)
        k = np.arange(n)
        # Weight based on proximity to φ-harmonic frequencies
        phi_weights = 1.0 / (1.0 + np.min([(k/n - (self.phi**i % 1))**2 
                                          for i in range(1, 9)], axis=0))
        
        # Normalize weights
        phi_weights = phi_weights / np.sum(phi_weights)
        
        # Calculate φ-weighted entropy
        weighted_probs = probabilities * phi_weights
        weighted_probs = weighted_probs[weighted_probs > 0]  # Filter zeros
        weighted_entropy = -np.sum(weighted_probs * np.log2(weighted_probs))
        
        return weighted_entropy
        
    def analyze_entropy_change(self, pre_qft_state, post_qft_state):
        """Analyze entropy change before and after QFT"""
        # Calculate standard Shannon entropy
        pre_entropy = self.shannon_entropy(pre_qft_state)
        post_entropy = self.shannon_entropy(post_qft_state)
        entropy_change = post_entropy - pre_entropy
        
        # Calculate φ-weighted entropy
        pre_phi_entropy = self.phi_weighted_entropy(pre_qft_state)
        post_phi_entropy = self.phi_weighted_entropy(post_qft_state)
        phi_entropy_change = post_phi_entropy - pre_phi_entropy
        
        # Calculate entropy coherence (how well entropy aligns with φ)
        entropy_coherence = 1 - abs((post_entropy / pre_entropy) % self.phi)
        
        # Store results
        result = {
            "timestamp": str(datetime.now()),
            "pre_entropy": float(pre_entropy),
            "post_entropy": float(post_entropy),
            "entropy_change": float(entropy_change),
            "pre_phi_entropy": float(pre_phi_entropy),
            "post_phi_entropy": float(post_phi_entropy),
            "phi_entropy_change": float(phi_entropy_change),
            "entropy_coherence": float(entropy_coherence)
        }
        
        self.entropy_history.append(result)
        return result
        
    def visualize_entropy(self, pre_qft_state, post_qft_state):
        """Visualize entropy distribution before and after QFT"""
        # Calculate probability distributions
        pre_probs = np.abs(pre_qft_state)**2
        post_probs = np.abs(post_qft_state)**2
        
        # Calculate entropy density (local entropy contribution)
        pre_entropy_density = -pre_probs * np.log2(pre_probs + 1e-10)
        post_entropy_density = -post_probs * np.log2(post_probs + 1e-10)
        
        # Create visualization
        plt.figure(figsize=(15, 10))
        
        # Plot probability distributions
        plt.subplot(2, 2, 1)
        plt.plot(pre_probs[:100], 'b-', label='Pre-QFT')
        plt.title('Probability Distribution (Pre-QFT)')
        plt.xlabel('State Index')
        plt.ylabel('Probability')
        plt.grid(True)
        
        plt.subplot(2, 2, 2)
        plt.plot(post_probs[:100], 'r-', label='Post-QFT')
        plt.title('Probability Distribution (Post-QFT)')
        plt.xlabel('State Index')
        plt.ylabel('Probability')
        plt.grid(True)
        
        # Plot entropy density
        plt.subplot(2, 2, 3)
        plt.plot(pre_entropy_density[:100], 'b-', label='Pre-QFT')
        plt.title('Entropy Density (Pre-QFT)')
        plt.xlabel('State Index')
        plt.ylabel('Entropy Contribution')
        plt.grid(True)
        
        plt.subplot(2, 2, 4)
        plt.plot(post_entropy_density[:100], 'r-', label='Post-QFT')
        plt.title('Entropy Density (Post-QFT)')
        plt.xlabel('State Index')
        plt.ylabel('Entropy Contribution')
        plt.grid(True)
        
        plt.tight_layout()
        
        # Save the visualization
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.results_dir / f"entropy_visualization_{timestamp}.png"
        plt.savefig(filename)
        plt.close()
        
        return str(filename)
        
    def save_entropy_results(self):
        """Save entropy analysis results to file"""
        if not self.entropy_history:
            print("No entropy results to save")
            return
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.results_dir / f"entropy_results_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(self.entropy_history, f, indent=2)
            
        print(f"Entropy results saved to {filename}")
        return str(filename)
        
    def get_entropy_summary(self):
        """Get summary of entropy analysis results"""
        if not self.entropy_history:
            return "No entropy analysis results available"
            
        # Calculate average metrics
        avg_pre_entropy = np.mean([r["pre_entropy"] for r in self.entropy_history])
        avg_post_entropy = np.mean([r["post_entropy"] for r in self.entropy_history])
        avg_entropy_change = np.mean([r["entropy_change"] for r in self.entropy_history])
        avg_entropy_coherence = np.mean([r["entropy_coherence"] for r in self.entropy_history])
        
        # Format summary
        summary = f"\n📊 Entropy Analysis Summary\n"
        summary += f"=" * 50 + "\n"
        summary += f"Records: {len(self.entropy_history)}\n"
        summary += f"Average Pre-QFT Entropy: {avg_pre_entropy:.6f}\n"
        summary += f"Average Post-QFT Entropy: {avg_post_entropy:.6f}\n"
        summary += f"Average Entropy Change: {avg_entropy_change:.6f}\n"
        summary += f"Average Entropy Coherence: {avg_entropy_coherence:.6f}\n"
        
        return summary

def main():
    """Test the entropy analyzer"""
    analyzer = QuantumEntropyAnalyzer()
    
    # Generate test quantum states
    n = 1024
    pre_qft = np.exp(1j * np.random.random(n) * 2 * np.pi) / np.sqrt(n)
    post_qft = np.fft.fft(pre_qft) / np.sqrt(n)
    
    # Analyze entropy
    result = analyzer.analyze_entropy_change(pre_qft, post_qft)
    print("\n📊 Entropy Analysis Results")
    print("=" * 50)
    for key, value in result.items():
        if key != "timestamp":
            print(f"{key}: {value:.6f}")
    
    # Visualize entropy
    viz_file = analyzer.visualize_entropy(pre_qft, post_qft)
    print(f"\nEntropy visualization saved to: {viz_file}")
    
    # Save results
    analyzer.save_entropy_results()
    
if __name__ == "__main__":
    main()
