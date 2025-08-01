"""
Observer-Dependent Entropy in Phi-Harmonic Systems
Tests whether entropy emerges only through observation in phi-harmonic frameworks
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os

# Constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio
PHI_INV = 1 / PHI  # Golden ratio inverse

class ObserverEntropySystem:
    """Simulates a phi-harmonic system with observer-dependent entropy"""
    
    def __init__(self, size=1000, dimensions=3):
        self.size = size
        self.dimensions = dimensions
        self.phi_field = None
        self.observed_states = []
        self.entropy_values = []
        self.observation_points = []
    
    def _generate_phi_harmonic_field(self):
        """Generate a phi-harmonic field with inherent order"""
        # Create a multidimensional field
        shape = tuple([self.size] * self.dimensions)
        field = np.zeros(shape)
        
        # Generate coordinates for each dimension
        coords = []
        for d in range(self.dimensions):
            coords.append(np.linspace(0, 10*np.pi, self.size))
        
        # Fill the field with phi-harmonic patterns
        # This represents the "pre-observed" state with inherent order
        if self.dimensions == 1:
            x = coords[0]
            field = np.sin(PHI * x) + np.sin(PHI_INV * x)
        elif self.dimensions == 2:
            x, y = np.meshgrid(coords[0], coords[1])
            field = np.sin(PHI * x) * np.cos(PHI_INV * y) + np.sin(PHI_INV * x) * np.cos(PHI * y)
        elif self.dimensions == 3:
            x, y, z = np.meshgrid(coords[0], coords[1], coords[2], indexing='ij')
            field = (np.sin(PHI * x) * np.cos(PHI_INV * y) * np.sin(PHI**2 * z) + 
                     np.sin(PHI_INV * x) * np.cos(PHI * y) * np.sin(PHI_INV**2 * z))
        
        self.phi_field = field
        return field
    
    def _calculate_entropy(self, data):
        """Calculate Shannon entropy of the data"""
        # Bin the data to create a probability distribution
        hist, bin_edges = np.histogram(data, bins=50, density=True)
        
        # Remove zeros to avoid log(0)
        hist = hist[hist > 0]
        
        # Calculate Shannon entropy
        entropy = -np.sum(hist * np.log2(hist))
        return entropy
    
    def _observe_field(self, num_observations=10, observer_precision=1.0):
        """Simulate observations of the field with varying precision"""
        if self.phi_field is None:
            self._generate_phi_harmonic_field()
        
        observed_states = []
        entropy_values = []
        observation_points = []
        
        for i in range(num_observations):
            # Simulate observation with limited precision
            # Lower precision means more "noise" added to the observation
            noise_level = 1.0 / observer_precision
            
            # Add observation noise
            if self.dimensions == 1:
                # For 1D, observe the entire array with noise
                observed = self.phi_field + noise_level * np.random.normal(0, 1, self.phi_field.shape)
                observed_states.append(observed)
                
                # Calculate entropy
                entropy = self._calculate_entropy(observed.flatten())
                
                # For 1D, we're observing the whole array
                observation_point = 0
                
            else:
                # For higher dimensions, observe a random slice or projection
                dim = np.random.randint(0, self.dimensions)
                slice_indices = [slice(None)] * self.dimensions
                slice_idx = np.random.randint(0, self.size)
                slice_indices[dim] = slice_idx
                
                # Get the slice and add noise
                observed = self.phi_field[tuple(slice_indices)] + noise_level * np.random.normal(0, 1, self.phi_field[tuple(slice_indices)].shape)
                observed_states.append(observed)
                
                # Calculate entropy of the observed slice
                entropy = self._calculate_entropy(observed.flatten())
            
            entropy_values.append(entropy)
            if self.dimensions > 1:
                observation_points.append((dim, slice_idx))
            else:
                observation_points.append(observation_point)
        
        self.observed_states = observed_states
        self.entropy_values = entropy_values
        self.observation_points = observation_points
        
        return observed_states, entropy_values
    
    def run_observer_experiment(self, precision_levels=None):
        """Run experiment with different observer precision levels"""
        if precision_levels is None:
            precision_levels = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]
        
        # Generate the phi-harmonic field once
        if self.phi_field is None:
            self._generate_phi_harmonic_field()
        
        # Calculate the "true" entropy of the full field
        true_entropy = self._calculate_entropy(self.phi_field.flatten())
        print(f"True entropy of the full phi-harmonic field: {true_entropy:.4f}")
        
        # Observe with different precision levels
        results = []
        for precision in precision_levels:
            print(f"Observing with precision level: {precision}")
            _, entropies = self._observe_field(num_observations=20, observer_precision=precision)
            avg_entropy = np.mean(entropies)
            results.append({
                'precision': precision,
                'average_entropy': avg_entropy,
                'entropy_increase': avg_entropy - true_entropy
            })
            print(f"  Average observed entropy: {avg_entropy:.4f}")
            print(f"  Entropy increase due to observation: {avg_entropy - true_entropy:.4f}")
        
        return results
    
    def visualize_results(self, results, save_path='observer_entropy.png'):
        """Visualize the relationship between observer precision and entropy"""
        plt.figure(figsize=(15, 10))
        
        # Plot 1: Original phi-harmonic field
        if self.dimensions == 1:
            plt.subplot(2, 2, 1)
            plt.plot(self.phi_field)
            plt.title('Original Phi-Harmonic Field (1D)')
            plt.xlabel('Position')
            plt.ylabel('Value')
        elif self.dimensions == 2:
            plt.subplot(2, 2, 1)
            plt.imshow(self.phi_field, cmap='viridis')
            plt.colorbar()
            plt.title('Original Phi-Harmonic Field (2D)')
        else:
            plt.subplot(2, 2, 1)
            # For 3D, show a central slice
            central_slice = self.phi_field[self.size//2, :, :]
            plt.imshow(central_slice, cmap='viridis')
            plt.colorbar()
            plt.title('Original Phi-Harmonic Field (3D Central Slice)')
        
        # Plot 2: Example observed state
        if len(self.observed_states) > 0:
            plt.subplot(2, 2, 2)
            if self.dimensions == 1:
                plt.plot([self.observed_states[0]])
                plt.title('Example Observed State (1D)')
                plt.xlabel('Position')
                plt.ylabel('Value')
            else:
                # Check if observed state is 1D array (which happens when observing a slice of higher dim)
                if len(self.observed_states[0].shape) == 1:
                    plt.plot(self.observed_states[0])
                    plt.title(f'Example Observed State ({self.dimensions}D Slice)')
                    plt.xlabel('Position')
                    plt.ylabel('Value')
                else:
                    plt.imshow(self.observed_states[0], cmap='viridis')
                    plt.colorbar()
                    plt.title(f'Example Observed State ({self.dimensions}D Slice)')
        
        # Plot 3: Precision vs Entropy
        plt.subplot(2, 2, 3)
        precisions = [r['precision'] for r in results]
        entropies = [r['average_entropy'] for r in results]
        
        plt.plot(precisions, entropies, 'o-')
        plt.xscale('log')
        plt.title('Observer Precision vs. Measured Entropy')
        plt.xlabel('Observer Precision (log scale)')
        plt.ylabel('Average Entropy')
        plt.grid(True)
        
        # Add trendline
        if len(precisions) > 1 and all(e > 0 for e in entropies):
            # Fit a power law: entropy = a * precision^b
            log_precisions = np.log(precisions)
            log_entropies = np.log(entropies)
            slope, intercept, r_value, p_value, std_err = stats.linregress(log_precisions, log_entropies)
            
            # Plot trendline
            x_fit = np.linspace(min(precisions), max(precisions), 100)
            y_fit = np.exp(intercept) * x_fit**slope
            plt.plot(x_fit, y_fit, 'r--', label=f'Power Law: E ∝ P^{slope:.2f}')
            plt.legend()
            
            # Add R-squared value
            plt.text(0.05, 0.95, f'R² = {r_value**2:.4f}', transform=plt.gca().transAxes, 
                     bbox=dict(facecolor='white', alpha=0.8))
        
        # Plot 4: Entropy increase vs Precision
        plt.subplot(2, 2, 4)
        entropy_increases = [r['entropy_increase'] for r in results]
        
        plt.plot(precisions, entropy_increases, 'o-', color='green')
        plt.xscale('log')
        plt.title('Observer Precision vs. Entropy Increase')
        plt.xlabel('Observer Precision (log scale)')
        plt.ylabel('Entropy Increase')
        plt.grid(True)
        
        # Add horizontal line at zero
        plt.axhline(y=0, color='r', linestyle='-', alpha=0.3)
        
        # Add phi and phi^-1 lines
        plt.axhline(y=PHI, color='purple', linestyle='--', alpha=0.5, label=f'φ = {PHI:.4f}')
        plt.axhline(y=PHI_INV, color='orange', linestyle='--', alpha=0.5, label=f'φ⁻¹ = {PHI_INV:.4f}')
        plt.legend()
        
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        
        print(f"Visualization saved to {save_path}")

def run_entropy_experiment():
    """Run the observer-dependent entropy experiment"""
    print("=== Observer-Dependent Entropy Experiment ===")
    print(f"Testing whether entropy emerges through observation in phi-harmonic systems")
    print(f"Golden ratio (φ): {PHI}")
    
    # Create output directory
    output_dir = "entropy_experiment_results"
    os.makedirs(output_dir, exist_ok=True)
    
    # Run experiments for different dimensions
    dimensions = [1, 2, 3]
    
    for dim in dimensions:
        print(f"\nRunning experiment for {dim}D phi-harmonic field:")
        system = ObserverEntropySystem(size=100, dimensions=dim)
        results = system.run_observer_experiment()
        
        # Visualize results
        system.visualize_results(results, save_path=os.path.join(output_dir, f"entropy_{dim}d.png"))
    
    # Analyze results
    print("\nAnalysis of Observer-Dependent Entropy:")
    print("-" * 60)
    
    # Check if entropy increases as precision decreases
    # This would confirm that observation introduces entropy
    entropy_correlation = False
    try:
        entropy_correlation = all(results[i]['average_entropy'] > results[i+1]['average_entropy'] 
                                for i in range(len(results)-1))
    except IndexError:
        # Handle case where results might be empty
        pass
    
    if entropy_correlation:
        print("✓ CONFIRMED: Entropy increases as observer precision decreases")
        print("  This supports the theory that entropy emerges through observation")
        print("  rather than being an inherent property of the phi-harmonic system.")
    else:
        print("✗ NOT CONFIRMED: No clear relationship between observer precision and entropy")
        print("  The results do not support the observer-dependent entropy theory.")
    
    # Check for phi-harmonic patterns in entropy values
    entropy_increases = [r['entropy_increase'] for r in results]
    phi_patterns = [abs(e - PHI) < 0.1 or abs(e - PHI_INV) < 0.1 for e in entropy_increases]
    
    if any(phi_patterns):
        print("\n✓ PHI-HARMONIC PATTERN DETECTED: Some entropy increases are approximately")
        print(f"  equal to φ ({PHI:.4f}) or 1/φ ({PHI_INV:.4f}), suggesting that the")
        print("  observation process itself follows phi-harmonic principles.")
    
    print(f"\nResults saved to {output_dir}/")

if __name__ == "__main__":
    run_entropy_experiment()
