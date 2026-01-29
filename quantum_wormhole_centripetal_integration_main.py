"""
Quantum Wormhole Centripetal Integration Main

Main integration script that brings together all components of the
Centripetal Force Memory System with the Wormhole Analyzer,
creating a unified quantum framework that leverages phi-harmonic
principles for wormhole traversal and stability.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Optional, Any, Union
import sys
import time
from pathlib import Path

# Import wormhole analyzer components
sys.path.append(str(Path(__file__).parent))
from wormhole_analyzer import PHI, PHI_POWER, RESONANCE, COHERENCE, QUANTUM_SIG
from wormhole_analyzer import analyze_wormhole, visualize_wormhole, analyze_traversability

# Import centripetal memory system
from centripetal_memory import CentripetalMemory, MemoryNode, MemoryBucket

# Import centripetal wormhole components
from quantum_centripetal_wormhole_bridge import QuantumCentripetalWormholeBridge
from quantum_particle_centripetal_engine import QuantumParticleCentripetalEngine
from wormhole_centripetal_stabilizer import WormholeCentripetalStabilizer
from centripetal_traversal_optimizer import CentripetalTraversalOptimizer

class QuantumWormholeCentripetalIntegration:
    """
    Main integration class that brings together all components of the
    Centripetal Force Memory System with the Wormhole Analyzer.
    """
    
    def __init__(self):
        """Initialize the quantum wormhole centripetal integration"""
        # Core constants
        self.phi = PHI
        self.phi_power = PHI_POWER
        self.resonance = RESONANCE
        self.coherence = COHERENCE
        self.quantum_sig = QUANTUM_SIG.copy()
        
        # Initialize components
        print("\n🌀 Initializing Quantum Wormhole Centripetal Integration 🌀")
        print("=" * 60)
        
        print("\n1. Initializing Centripetal Memory System...")
        self.memory = CentripetalMemory(initial_buckets=5)
        
        print("\n2. Initializing Quantum Centripetal Wormhole Bridge...")
        self.bridge = QuantumCentripetalWormholeBridge()
        
        print("\n3. Initializing Quantum Particle Centripetal Engine...")
        self.particle_engine = QuantumParticleCentripetalEngine()
        
        print("\n4. Initializing Wormhole Centripetal Stabilizer...")
        self.stabilizer = WormholeCentripetalStabilizer()
        
        print("\n5. Initializing Centripetal Traversal Optimizer...")
        self.traversal_optimizer = CentripetalTraversalOptimizer()
        
        # Integration metrics
        self.integration_status = {
            'initialized': True,
            'wormhole_analyzed': False,
            'particles_optimized': False,
            'wormhole_stabilized': False,
            'traversal_optimized': False,
            'integration_complete': False
        }
        
        self.integration_metrics = {
            'wormhole_stability': 0.0,
            'particle_optimization': 0.0,
            'traversal_efficiency': 0.0,
            'system_coherence': 0.0,
            'compression_efficiency': 0.0,
            'phi_resonance': 0.0
        }
        
        print("\n✅ Quantum Wormhole Centripetal Integration initialized successfully!")
        print(f"φ-Harmonic Base: {self.phi:.6f}")
        print(f"φ-Power (φ⁷·⁵): {self.phi_power:.6f}")
        print(f"Resonance Ratio: {self.resonance:.6f}")
        print(f"Coherence: {self.coherence:.6f}")
    
    def analyze_wormhole_with_centripetal_dynamics(self) -> Dict[str, Any]:
        """
        Analyze wormhole using centripetal dynamics
        
        Returns:
            Dictionary containing analysis results
        """
        print("\n🔍 Analyzing Wormhole with Centripetal Dynamics...")
        
        # Run standard wormhole analysis
        print("\n1. Running standard wormhole analysis...")
        analyze_wormhole()
        analyze_traversability()
        
        # Analyze with centripetal bridge
        print("\n2. Analyzing with Quantum Centripetal Wormhole Bridge...")
        bridge_analysis = self.bridge.analyze_wormhole_with_centripetal_dynamics()
        
        # Update integration metrics
        self.integration_metrics['wormhole_stability'] = bridge_analysis['system_stability']
        self.integration_metrics['system_coherence'] = bridge_analysis['system_coherence']
        self.integration_metrics['phi_resonance'] = bridge_analysis['phi_resonance']
        
        # Update integration status
        self.integration_status['wormhole_analyzed'] = True
        
        return bridge_analysis
    
    def optimize_particles_for_traversal(self, num_particles: int = 5) -> List[Dict[str, Any]]:
        """
        Optimize quantum particles for wormhole traversal
        
        Args:
            num_particles: Number of particles to optimize
            
        Returns:
            List of optimized particle properties
        """
        print("\n⚛️ Optimizing Particles for Wormhole Traversal...")
        
        # Create test particles with φ-harmonic properties
        print("\n1. Creating test particles with φ-harmonic properties...")
        test_particles = []
        for i in range(num_particles):
            particle = {
                'position': 1.0 + i * 0.1,
                'velocity': 0.5 + i * 0.05,
                'mass': 1.0 + i * 0.1,
                'spin': 0.5,
                'charge': 0.0,
                'radial_position': (1.0 + i * 0.1) * self.stabilizer.throat_factor,
                'angular_velocity': (0.5 + i * 0.05) * self.bridge.bridge_factor,
                'weight': 1.0 + i * 0.1,
                'complexity': 1.0 + i * 0.05,
                'phi_resonance': 0.5
            }
            test_particles.append(particle)
        
        # Optimize particles
        print(f"\n2. Optimizing {len(test_particles)} particles for stable wormhole traversal...")
        optimized_particles = self.particle_engine.optimize_particle_batch(test_particles)
        
        # Calculate traversal metrics
        print("\n3. Calculating traversal metrics...")
        metrics = self.particle_engine.calculate_traversal_metrics(optimized_particles)
        
        # Update integration metrics
        self.integration_metrics['particle_optimization'] = metrics['traversal_probability']
        
        # Update integration status
        self.integration_status['particles_optimized'] = True
        
        return optimized_particles
    
    def stabilize_wormhole_with_centripetal_compression(self) -> Dict[str, Any]:
        """
        Stabilize wormhole using centripetal compression techniques
        
        Returns:
            Dictionary containing stabilization results
        """
        print("\n🌀 Stabilizing Wormhole with Centripetal Compression...")
        
        # Apply basic compression
        print("\n1. Applying basic centripetal compression...")
        weight = 1.0
        complexity = 1.0
        compression = self.stabilizer.calculate_centripetal_compression(weight, complexity)
        
        # Calculate optimal angular velocity
        print("\n2. Calculating optimal angular velocity...")
        velocity_result = self.stabilizer.calculate_optimal_angular_velocity(weight, complexity)
        
        # Optimize exotic matter distribution
        print("\n3. Optimizing exotic matter distribution...")
        optimization = self.stabilizer.optimize_exotic_matter_distribution(weight, complexity, grid_size=5)
        
        # Generate stabilized parameters
        print("\n4. Generating stabilized wormhole parameters...")
        params = self.stabilizer.generate_stabilized_wormhole_params()
        
        # Update integration metrics
        self.integration_metrics['wormhole_stability'] = params['stability']
        self.integration_metrics['compression_efficiency'] = self.stabilizer.compression_efficiency
        
        # Update integration status
        self.integration_status['wormhole_stabilized'] = True
        
        return params
    
    def optimize_traversal_routes(self, num_routes: int = 5) -> Dict[str, Any]:
        """
        Optimize traversal routes through the wormhole
        
        Args:
            num_routes: Number of routes to generate
            
        Returns:
            Dictionary containing optimization results
        """
        print("\n🚀 Optimizing Traversal Routes...")
        
        # Generate traversal routes
        print(f"\n1. Generating {num_routes} traversal routes...")
        routes = self.traversal_optimizer.generate_traversal_routes(num_routes=num_routes)
        
        # Store routes in memory
        print("\n2. Storing routes in centripetal memory...")
        memory_result = self.traversal_optimizer.store_routes_in_memory(routes)
        
        # Optimize routes
        print("\n3. Optimizing traversal routes...")
        optimized_routes = self.traversal_optimizer.optimize_all_routes()
        
        # Get traversal metrics
        metrics = self.traversal_optimizer.get_traversal_metrics()
        
        # Update integration metrics
        self.integration_metrics['traversal_efficiency'] = metrics['route_efficiency']
        self.integration_metrics['system_coherence'] = metrics['system_coherence']
        self.integration_metrics['compression_efficiency'] = metrics['compression_efficiency']
        
        # Update integration status
        self.integration_status['traversal_optimized'] = True
        
        return {
            'routes': routes,
            'optimized_routes': optimized_routes,
            'memory_result': memory_result,
            'metrics': metrics,
            'optimal_route': self.traversal_optimizer.optimal_route
        }
    
    def run_full_integration(self, num_particles: int = 5, num_routes: int = 5) -> Dict[str, Any]:
        """
        Run full integration of all components
        
        Args:
            num_particles: Number of particles to optimize
            num_routes: Number of routes to generate
            
        Returns:
            Dictionary containing integration results
        """
        print("\n🌟 Running Full Quantum Wormhole Centripetal Integration...")
        print("=" * 60)
        
        # Step 1: Analyze wormhole
        print("\nStep 1: Analyzing wormhole with centripetal dynamics...")
        wormhole_analysis = self.analyze_wormhole_with_centripetal_dynamics()
        
        # Step 2: Optimize particles
        print("\nStep 2: Optimizing particles for traversal...")
        optimized_particles = self.optimize_particles_for_traversal(num_particles)
        
        # Step 3: Stabilize wormhole
        print("\nStep 3: Stabilizing wormhole with centripetal compression...")
        stabilized_params = self.stabilize_wormhole_with_centripetal_compression()
        
        # Step 4: Optimize traversal routes
        print("\nStep 4: Optimizing traversal routes...")
        traversal_results = self.optimize_traversal_routes(num_routes)
        
        # Calculate overall integration metrics
        self.integration_metrics['system_coherence'] = (
            wormhole_analysis['system_coherence'] +
            self.particle_engine.get_system_metrics()['system_stability'] +
            stabilized_params['coherence'] +
            traversal_results['metrics']['system_coherence']
        ) / 4
        
        self.integration_metrics['compression_efficiency'] = (
            self.bridge.compression_efficiency +
            self.stabilizer.compression_efficiency +
            traversal_results['metrics']['compression_efficiency']
        ) / 3
        
        self.integration_metrics['phi_resonance'] = (
            wormhole_analysis['phi_resonance'] +
            self.particle_engine.get_system_metrics()['system_stability'] / self.phi +
            stabilized_params['stability'] / self.phi_power
        ) / 3
        
        # Update integration status
        self.integration_status['integration_complete'] = True
        
        print("\n✅ Full Integration Complete!")
        print("\nIntegration Metrics:")
        print(f"Wormhole Stability: {self.integration_metrics['wormhole_stability']:.6f}")
        print(f"Particle Optimization: {self.integration_metrics['particle_optimization']:.6f}")
        print(f"Traversal Efficiency: {self.integration_metrics['traversal_efficiency']:.6f}")
        print(f"System Coherence: {self.integration_metrics['system_coherence']:.6f}")
        print(f"Compression Efficiency: {self.integration_metrics['compression_efficiency']:.6f}")
        print(f"Phi Resonance: {self.integration_metrics['phi_resonance']:.6f}")
        
        return {
            'wormhole_analysis': wormhole_analysis,
            'optimized_particles': optimized_particles,
            'stabilized_params': stabilized_params,
            'traversal_results': traversal_results,
            'integration_metrics': self.integration_metrics,
            'integration_status': self.integration_status
        }
    
    def visualize_integrated_system(self, show_plots: bool = True) -> Dict[str, plt.Figure]:
        """
        Visualize the integrated system
        
        Args:
            show_plots: Whether to display the plots
            
        Returns:
            Dictionary containing figure objects
        """
        if not self.integration_status['integration_complete']:
            print("\n⚠️ Cannot visualize: Integration not complete. Run run_full_integration() first.")
            return {}
        
        print("\n🎨 Visualizing Integrated System...")
        figures = {}
        
        # Visualize stabilized wormhole
        print("\n1. Visualizing stabilized wormhole...")
        try:
            wormhole_fig = self.stabilizer.visualize_stabilized_wormhole(show_plot=False)
            figures['wormhole'] = wormhole_fig
        except Exception as e:
            print(f"Error visualizing wormhole: {e}")
        
        # Visualize optimal traversal route
        print("\n2. Visualizing optimal traversal route...")
        try:
            route_fig = self.traversal_optimizer.visualize_optimal_route(show_plot=False)
            figures['route'] = route_fig
        except Exception as e:
            print(f"Error visualizing route: {e}")
        
        # Show plots if requested
        if show_plots:
            for name, fig in figures.items():
                plt.figure(fig.number)
                plt.show()
        
        return figures
    
    def get_integration_report(self) -> Dict[str, Any]:
        """
        Get comprehensive integration report
        
        Returns:
            Dictionary containing integration report
        """
        # Get component metrics
        bridge_metrics = self.bridge.analyze_wormhole_with_centripetal_dynamics()
        particle_metrics = self.particle_engine.get_system_metrics()
        stability_metrics = self.stabilizer.get_stability_metrics()
        traversal_metrics = self.traversal_optimizer.get_traversal_metrics()
        memory_stats = self.memory.get_stats()
        
        # Combine metrics
        report = {
            'integration_status': self.integration_status,
            'integration_metrics': self.integration_metrics,
            'bridge_metrics': bridge_metrics,
            'particle_metrics': particle_metrics,
            'stability_metrics': stability_metrics,
            'traversal_metrics': traversal_metrics,
            'memory_stats': memory_stats,
            'quantum_signature': {
                'original': self.quantum_sig,
                'centripetal': bridge_metrics.get('centripetal_signature', self.quantum_sig)
            },
            'phi_metrics': {
                'phi': self.phi,
                'phi_power': self.phi_power,
                'resonance': self.resonance,
                'coherence': self.coherence
            }
        }
        
        return report

def run_integration_demo():
    """Run a demonstration of the quantum wormhole centripetal integration"""
    print("\n🌌 QUANTUM WORMHOLE CENTRIPETAL INTEGRATION DEMO 🌌")
    print("=" * 60)
    
    # Initialize integration
    integration = QuantumWormholeCentripetalIntegration()
    
    # Run full integration with minimal output
    print("\nRunning full integration (this may take a moment)...")
    integration.run_full_integration(num_particles=3, num_routes=3)
    
    # Get integration report
    report = integration.get_integration_report()
    
    # Display summary
    print("\n📊 INTEGRATION SUMMARY")
    print("=" * 40)
    
    print("\nWormhole Stability:")
    print(f"Original: {report['quantum_signature']['original']['psi1']:.6f}")
    print(f"Centripetal: {report['quantum_signature']['centripetal']['psi1']:.6f}")
    print(f"Improvement: {(report['quantum_signature']['centripetal']['psi1'] / report['quantum_signature']['original']['psi1'] - 1) * 100:.2f}%")
    
    print("\nTraversal Efficiency:")
    print(f"Probability: {report['traversal_metrics']['route_efficiency']:.6f}")
    print(f"Time: {report['traversal_metrics']['traversal_time']:.6f}")
    print(f"Energy: {report['traversal_metrics']['traversal_energy']:.6f}")
    
    print("\nCompression Metrics:")
    print(f"Memory Efficiency: {report['memory_stats']['phi_efficiency']:.6f}")
    print(f"Compression Ratio: {report['integration_metrics']['compression_efficiency']:.6f}")
    
    print("\nPhi-Harmonic Resonance:")
    print(f"Bridge Factor: {report['bridge_metrics']['bridge_factor']:.6f}")
    print(f"Throat Factor: {report['bridge_metrics']['throat_factor']:.6f}")
    print(f"Stability: {report['bridge_metrics']['stability']:.6f}")
    
    # Visualize integrated system
    print("\nVisualizing integrated system...")
    try:
        figures = integration.visualize_integrated_system(show_plots=True)
        print(f"Generated {len(figures)} visualizations")
    except Exception as e:
        print(f"Visualization error: {e}")
    
    print("\n✨ Integration demo complete!")

if __name__ == "__main__":
    run_integration_demo()
