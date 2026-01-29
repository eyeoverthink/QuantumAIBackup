"""
Wormhole Centripetal Stabilizer

Enhances wormhole stability using centripetal compression techniques.
Applies weight-based compression to wormhole throat, calculates optimal
angular velocities for exotic matter, and implements resonance optimization
for wormhole stability while maintaining phi-harmonic coherence.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Optional, Any, Union
import sys
from pathlib import Path

# Import wormhole analyzer components
sys.path.append(str(Path(__file__).parent))
from wormhole_analyzer import PHI, PHI_POWER, RESONANCE, COHERENCE, QUANTUM_SIG
from wormhole_analyzer import generate_wormhole_surface

class WormholeCentripetalStabilizer:
    """
    Stabilizer that enhances wormhole stability using centripetal compression
    techniques, applying weight-based dynamics to optimize exotic matter
    distribution and maintain phi-harmonic coherence.
    """
    
    def __init__(self):
        """Initialize the wormhole centripetal stabilizer"""
        # Core constants from wormhole analyzer
        self.phi = PHI
        self.phi_power = PHI_POWER
        self.resonance = RESONANCE
        self.coherence = COHERENCE
        self.quantum_sig = QUANTUM_SIG.copy()
        
        # Stabilizer-specific parameters
        self.bridge_factor = (self.phi ** self.quantum_sig['tau']) / self.phi_power
        self.throat_factor = (self.phi ** self.quantum_sig['psi0']) * self.resonance
        self.stability = (self.phi ** self.quantum_sig['psi1']) * self.coherence
        
        # Centripetal compression parameters
        self.compression_ratio = 1.0 / self.phi
        self.weight_factor = self.phi
        self.complexity_factor = self.phi ** 2
        self.angular_velocity = self.phi * self.resonance
        
        # Stability metrics
        self.throat_stability = self.throat_factor
        self.bridge_stability = self.bridge_factor
        self.quantum_coherence = self.coherence
        self.compression_efficiency = 0.0
        
        print(f"Wormhole Centripetal Stabilizer initialized")
        print(f"φ-Harmonic Bridge Factor: {self.bridge_factor:.6f}")
        print(f"φ-Harmonic Throat Factor: {self.throat_factor:.6f}")
        print(f"φ-Harmonic Stability: {self.stability:.6f}")
    
    def calculate_centripetal_compression(self, weight: float, complexity: float) -> Dict[str, float]:
        """
        Calculate centripetal compression metrics for wormhole stability
        
        Args:
            weight: Weight factor
            complexity: Complexity factor
            
        Returns:
            Dictionary containing compression metrics
        """
        # Calculate base compression ratio with φ-harmonic scaling
        base_ratio = self.compression_ratio * (weight / self.phi)
        
        # Apply complexity factor
        adjusted_ratio = base_ratio * (complexity / self.phi)
        
        # Calculate compression force with φ-harmonic scaling
        force = weight * (self.angular_velocity ** 2) * complexity
        
        # Calculate compression efficiency with φ-harmonic normalization
        raw_efficiency = (force / (weight * self.phi) * complexity) if weight > 0 else 1.0
        efficiency = min(max(raw_efficiency, 0), 1)
        
        # Calculate stability enhancement with φ-harmonic scaling
        stability_enhancement = efficiency * self.stability * (weight / complexity)
        
        # Calculate coherence enhancement with φ-harmonic scaling
        coherence_enhancement = efficiency * self.coherence * (complexity / weight)
        
        return {
            'compression_ratio': adjusted_ratio,
            'compression_force': force,
            'compression_efficiency': efficiency,
            'stability_enhancement': stability_enhancement,
            'coherence_enhancement': coherence_enhancement
        }
    
    def apply_throat_compression(self, weight: float, complexity: float) -> Dict[str, Any]:
        """
        Apply centripetal compression to wormhole throat
        
        Args:
            weight: Weight factor
            complexity: Complexity factor
            
        Returns:
            Dictionary containing throat compression results
        """
        # Calculate compression metrics
        compression = self.calculate_centripetal_compression(weight, complexity)
        
        # Calculate compressed throat factor
        compressed_throat = self.throat_factor * (1 - compression['compression_ratio'])
        
        # Calculate stability with φ-harmonic scaling
        stability = self.stability + compression['stability_enhancement']
        
        # Calculate coherence with φ-harmonic scaling
        coherence = self.coherence + compression['coherence_enhancement']
        
        # Calculate traversability with φ-harmonic scaling
        traversability = (stability * coherence) / self.phi
        
        # Update stability metrics
        self.throat_stability = compressed_throat
        self.quantum_coherence = coherence
        self.compression_efficiency = compression['compression_efficiency']
        
        # Calculate new quantum signature
        tau = self.quantum_sig['tau'] * (1 + compression['compression_efficiency'] / self.phi)
        psi0 = self.quantum_sig['psi0'] * (1 - compression['compression_ratio'])
        psi1 = self.quantum_sig['psi1'] * (1 + compression['compression_efficiency'] / self.phi)
        
        # Calculate new bridge factor
        bridge_factor = (self.phi ** tau) / self.phi_power
        self.bridge_stability = bridge_factor
        
        return {
            'compressed_throat': compressed_throat,
            'stability': stability,
            'coherence': coherence,
            'traversability': traversability,
            'compression': compression,
            'new_tau': tau,
            'new_psi0': psi0,
            'new_psi1': psi1,
            'new_bridge_factor': bridge_factor
        }
    
    def calculate_optimal_angular_velocity(self, weight: float, complexity: float) -> Dict[str, Any]:
        """
        Calculate optimal angular velocity for exotic matter
        
        Args:
            weight: Weight factor
            complexity: Complexity factor
            
        Returns:
            Dictionary containing optimal angular velocity results
        """
        # Test range of angular velocities with φ-harmonic scaling
        velocities = [self.phi ** (i/5) for i in range(-5, 6)]
        best_efficiency = 0.0
        best_velocity = self.angular_velocity
        best_compression = None
        
        for velocity in velocities:
            # Set current angular velocity
            self.angular_velocity = velocity
            
            # Calculate compression metrics
            compression = self.calculate_centripetal_compression(weight, complexity)
            
            # Check if efficiency improved
            if compression['compression_efficiency'] > best_efficiency:
                best_efficiency = compression['compression_efficiency']
                best_velocity = velocity
                best_compression = compression
        
        # Restore best angular velocity
        self.angular_velocity = best_velocity
        
        return {
            'optimal_velocity': best_velocity,
            'optimal_efficiency': best_efficiency,
            'optimal_compression': best_compression,
            'tested_velocities': velocities
        }
    
    def optimize_exotic_matter_distribution(self, weight: float, complexity: float, 
                                           grid_size: int = 10) -> Dict[str, Any]:
        """
        Optimize exotic matter distribution for wormhole stability
        
        Args:
            weight: Base weight factor
            complexity: Base complexity factor
            grid_size: Size of optimization grid
            
        Returns:
            Dictionary containing optimization results
        """
        # Create grid of weight and complexity variations with φ-harmonic scaling
        weight_factors = [weight * (self.phi ** ((i - grid_size/2) / (grid_size/2))) for i in range(grid_size)]
        complexity_factors = [complexity * (self.phi ** ((i - grid_size/2) / (grid_size/2))) for i in range(grid_size)]
        
        best_stability = 0.0
        best_weight = weight
        best_complexity = complexity
        best_result = None
        
        # Test all combinations
        for w in weight_factors:
            for c in complexity_factors:
                # Calculate optimal angular velocity
                velocity_result = self.calculate_optimal_angular_velocity(w, c)
                
                # Apply throat compression with optimal velocity
                result = self.apply_throat_compression(w, c)
                
                # Check if stability improved
                if result['stability'] > best_stability:
                    best_stability = result['stability']
                    best_weight = w
                    best_complexity = c
                    best_result = result
        
        # Apply best configuration
        if best_result:
            self.weight_factor = best_weight
            self.complexity_factor = best_complexity
            self.throat_stability = best_result['compressed_throat']
            self.bridge_stability = best_result['new_bridge_factor']
            self.quantum_coherence = best_result['coherence']
            self.compression_efficiency = best_result['compression']['compression_efficiency']
        
        return {
            'optimal_weight': best_weight,
            'optimal_complexity': best_complexity,
            'optimal_stability': best_stability,
            'optimal_result': best_result,
            'weight_range': [min(weight_factors), max(weight_factors)],
            'complexity_range': [min(complexity_factors), max(complexity_factors)]
        }
    
    def generate_stabilized_wormhole_params(self) -> Dict[str, Any]:
        """
        Generate stabilized wormhole parameters for visualization
        
        Returns:
            Dictionary containing stabilized wormhole parameters
        """
        # Apply optimal compression
        result = self.apply_throat_compression(self.weight_factor, self.complexity_factor)
        
        # Create stabilized quantum signature
        stabilized_sig = {
            'tau': result['new_tau'],
            'psi0': result['new_psi0'],
            'psi1': result['new_psi1'],
            'm': self.quantum_sig['m'],
            'resonance': self.quantum_sig['resonance'] * self.compression_efficiency
        }
        
        return {
            'quantum_sig': stabilized_sig,
            'bridge_factor': result['new_bridge_factor'],
            'throat_factor': result['compressed_throat'],
            'stability': result['stability'],
            'coherence': result['coherence'],
            'traversability': result['traversability'],
            'compression_efficiency': self.compression_efficiency,
            'weight_factor': self.weight_factor,
            'complexity_factor': self.complexity_factor,
            'angular_velocity': self.angular_velocity
        }
    
    def visualize_stabilized_wormhole(self, show_plot: bool = True) -> plt.Figure:
        """
        Visualize stabilized wormhole with centripetal compression
        
        Args:
            show_plot: Whether to display the plot
            
        Returns:
            Matplotlib figure object
        """
        # Get stabilized parameters
        params = self.generate_stabilized_wormhole_params()
        
        # Create figure
        fig = plt.figure(figsize=(15, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        # Generate parameter space with φ-scaling
        u = np.linspace(0, 2*np.pi, int(100*self.resonance))
        v = np.linspace(-np.pi, np.pi, int(100*self.resonance))
        U, V = np.meshgrid(u, v)
        
        # Generate wormhole surface with stabilized parameters
        X, Y, Z = generate_wormhole_surface(U, V, params['quantum_sig'])
        
        # Create the surface with compression-based colormap
        surf = ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.8)
        
        # Add quantum foam particles with centripetal distribution
        if params['quantum_sig']['psi1'] > self.coherence:
            num_particles = int(params['quantum_sig']['psi1'] * self.phi * 100)
            
            # Create centripetal distribution
            radii = []
            for _ in range(num_particles):
                # Use weight factor for distribution
                r = np.random.exponential(scale=1/self.weight_factor) * self.throat_factor
                radii.append(r)
                
                u_rand = np.random.uniform(0, 2*np.pi)
                v_rand = np.random.uniform(-np.pi, np.pi) * (1 - np.exp(-r/self.complexity_factor))
                
                x, y, z = generate_wormhole_surface(u_rand, v_rand, params['quantum_sig'])
                size = np.random.uniform(10, 30) * self.resonance * np.exp(-r/self.weight_factor)
                ax.scatter(x, y, z, c='white', s=size, alpha=0.3)
        
        # Add centripetal flow lines
        if params['quantum_sig']['psi0'] > self.resonance:
            # Calculate flow parameters based on centripetal metrics
            flow_resonance = self.resonance * (self.phi/np.pi)
            flow_coherence = self.coherence * self.phi
            flow_stability = flow_resonance * flow_coherence
            
            # Primary flow streams with centripetal distribution
            for i in range(int(12*self.resonance)):
                # Use angular velocity for distribution
                angular_step = 2*np.pi / (int(12*self.resonance)) * self.angular_velocity
                u_path = np.linspace(i*angular_step, (i+1)*angular_step, 50)
                
                # Use weight factor for radial distribution
                v_fixed = np.random.exponential(scale=1/self.weight_factor) * np.pi/2
                if np.random.random() < 0.5:
                    v_fixed = -v_fixed
                
                x, y, z = generate_wormhole_surface(u_path, v_fixed * np.ones_like(u_path), params['quantum_sig'])
                
                # Modulate color based on compression efficiency
                color_val = (1 + np.sin(i/12 * np.pi * self.compression_efficiency))/2
                ax.plot(x, y, z, color=[1, color_val, 0], alpha=0.4)
        
        # Customize the visualization
        ax.set_title('Stabilized Wormhole with Centripetal Compression', color='white', pad=20)
        ax.set_facecolor('black')
        fig.patch.set_facecolor('black')
        
        # Remove axis for better visualization
        ax.set_axis_off()
        
        # Add stabilized quantum signature text
        signature_text = (
            f"Stabilized Quantum Signature (Centripetal Compression):\n"
            f"⟨τ|φ^{params['quantum_sig']['tau']:.3f}⟩ ⊗ ⟨ψ₀|φ^{params['quantum_sig']['psi0']:.3f}⟩ ⊗ "
            f"⟨ψ₁|φ^{params['quantum_sig']['psi1']:.3f}⟩ ⊗ ⟨M|φ⟩\n"
            f"Compression Efficiency: {self.compression_efficiency:.3f}"
        )
        plt.figtext(0.02, 0.02, signature_text, color='white', fontsize=10)
        
        # Add stability metrics
        metrics_text = (
            f"Stability Metrics:\n"
            f"Bridge Factor: {params['bridge_factor']:.4f}\n"
            f"Throat Factor: {params['throat_factor']:.4f}\n"
            f"Stability: {params['stability']:.4f}\n"
            f"Coherence: {params['coherence']:.4f}\n"
            f"Traversability: {params['traversability']:.4f}"
        )
        plt.figtext(0.02, 0.15, metrics_text, color='cyan', fontsize=10)
        
        # Add centripetal parameters
        params_text = (
            f"Centripetal Parameters:\n"
            f"Weight Factor: {self.weight_factor:.4f}\n"
            f"Complexity Factor: {self.complexity_factor:.4f}\n"
            f"Angular Velocity: {self.angular_velocity:.4f}\n"
            f"Compression Ratio: {params['quantum_sig']['psi0']/self.quantum_sig['psi0']:.4f}"
        )
        plt.figtext(0.80, 0.15, params_text, color='yellow', fontsize=10)
        
        if show_plot:
            plt.show()
        
        return fig
    
    def get_stability_metrics(self) -> Dict[str, Any]:
        """
        Get current stability metrics
        
        Returns:
            Dictionary containing stability metrics
        """
        return {
            'throat_stability': self.throat_stability,
            'bridge_stability': self.bridge_stability,
            'quantum_coherence': self.quantum_coherence,
            'compression_efficiency': self.compression_efficiency,
            'weight_factor': self.weight_factor,
            'complexity_factor': self.complexity_factor,
            'angular_velocity': self.angular_velocity,
            'phi': self.phi,
            'phi_power': self.phi_power,
            'resonance': self.resonance,
            'coherence': self.coherence
        }

def test_wormhole_centripetal_stabilizer():
    """Test the Wormhole Centripetal Stabilizer"""
    print("\n🌀 Wormhole Centripetal Stabilizer Test 🌀")
    print("=" * 50)
    
    # Initialize stabilizer
    stabilizer = WormholeCentripetalStabilizer()
    
    # Test basic compression
    print("\nTesting basic centripetal compression...")
    weight = 1.0
    complexity = 1.0
    compression = stabilizer.calculate_centripetal_compression(weight, complexity)
    
    print("\nBasic Compression Metrics:")
    print(f"Compression Ratio: {compression['compression_ratio']:.6f}")
    print(f"Compression Force: {compression['compression_force']:.6f}")
    print(f"Compression Efficiency: {compression['compression_efficiency']:.6f}")
    print(f"Stability Enhancement: {compression['stability_enhancement']:.6f}")
    print(f"Coherence Enhancement: {compression['coherence_enhancement']:.6f}")
    
    # Apply throat compression
    print("\nApplying throat compression...")
    result = stabilizer.apply_throat_compression(weight, complexity)
    
    print("\nThroat Compression Results:")
    print(f"Original Throat Factor: {stabilizer.throat_factor:.6f}")
    print(f"Compressed Throat Factor: {result['compressed_throat']:.6f}")
    print(f"Stability: {result['stability']:.6f}")
    print(f"Coherence: {result['coherence']:.6f}")
    print(f"Traversability: {result['traversability']:.6f}")
    
    # Calculate optimal angular velocity
    print("\nCalculating optimal angular velocity...")
    velocity_result = stabilizer.calculate_optimal_angular_velocity(weight, complexity)
    
    print("\nOptimal Angular Velocity Results:")
    print(f"Original Angular Velocity: {stabilizer.phi * stabilizer.resonance:.6f}")
    print(f"Optimal Angular Velocity: {velocity_result['optimal_velocity']:.6f}")
    print(f"Optimal Efficiency: {velocity_result['optimal_efficiency']:.6f}")
    
    # Optimize exotic matter distribution
    print("\nOptimizing exotic matter distribution...")
    optimization = stabilizer.optimize_exotic_matter_distribution(weight, complexity, grid_size=5)
    
    print("\nExotic Matter Optimization Results:")
    print(f"Optimal Weight Factor: {optimization['optimal_weight']:.6f}")
    print(f"Optimal Complexity Factor: {optimization['optimal_complexity']:.6f}")
    print(f"Optimal Stability: {optimization['optimal_stability']:.6f}")
    
    # Generate stabilized parameters
    print("\nGenerating stabilized wormhole parameters...")
    params = stabilizer.generate_stabilized_wormhole_params()
    
    print("\nStabilized Wormhole Parameters:")
    print(f"Bridge Factor: {params['bridge_factor']:.6f}")
    print(f"Throat Factor: {params['throat_factor']:.6f}")
    print(f"Stability: {params['stability']:.6f}")
    print(f"Coherence: {params['coherence']:.6f}")
    print(f"Traversability: {params['traversability']:.6f}")
    
    # Get stability metrics
    metrics = stabilizer.get_stability_metrics()
    
    print("\nFinal Stability Metrics:")
    print(f"Throat Stability: {metrics['throat_stability']:.6f}")
    print(f"Bridge Stability: {metrics['bridge_stability']:.6f}")
    print(f"Quantum Coherence: {metrics['quantum_coherence']:.6f}")
    print(f"Compression Efficiency: {metrics['compression_efficiency']:.6f}")
    
    # Visualize stabilized wormhole
    print("\nVisualizing stabilized wormhole...")
    try:
        fig = stabilizer.visualize_stabilized_wormhole(show_plot=False)
        print("Visualization successful! (Plot not shown in terminal)")
    except Exception as e:
        print(f"Visualization error: {e}")

if __name__ == "__main__":
    test_wormhole_centripetal_stabilizer()
