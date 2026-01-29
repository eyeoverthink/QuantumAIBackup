"""
Quantum Particle Centripetal Engine

Applies centripetal force dynamics to quantum particles in wormhole space,
calculating optimal trajectories and maintaining phi-harmonic resonance.
This engine optimizes particle mass and velocity for stable wormhole traversal.
"""

import numpy as np
from typing import Dict, List, Tuple, Optional, Any, Union
import sys
from pathlib import Path

# Import wormhole analyzer components
sys.path.append(str(Path(__file__).parent))
from wormhole_analyzer import PHI, PHI_POWER, RESONANCE, COHERENCE, QUANTUM_SIG

class QuantumParticleCentripetalEngine:
    """
    Engine that applies centripetal force dynamics to quantum particles
    in wormhole space, optimizing trajectories and maintaining phi-harmonic resonance.
    """
    
    def __init__(self):
        """Initialize the quantum particle centripetal engine"""
        # Core constants from wormhole analyzer
        self.phi = PHI
        self.phi_power = PHI_POWER
        self.resonance = RESONANCE
        self.coherence = COHERENCE
        self.quantum_sig = QUANTUM_SIG.copy()
        
        # Engine-specific parameters
        self.bridge_factor = (self.phi ** self.quantum_sig['tau']) / self.phi_power
        self.throat_factor = (self.phi ** self.quantum_sig['psi0']) * self.resonance
        self.stability = (self.phi ** self.quantum_sig['psi1']) * self.coherence
        
        # Particle dynamics parameters
        self.gravity_constant = 1.0 / self.phi
        self.force_threshold = 1.0 / self.phi
        self.stability_factor = self.phi
        self.time_step = 0.1 / self.phi
        
        # System metrics
        self.total_particles = 0
        self.total_energy = 0.0
        self.system_angular_momentum = 0.0
        self.system_stability = self.stability
        
        print(f"Quantum Particle Centripetal Engine initialized")
        print(f"φ-Harmonic Bridge Factor: {self.bridge_factor:.6f}")
        print(f"φ-Harmonic Throat Factor: {self.throat_factor:.6f}")
        print(f"φ-Harmonic Stability: {self.stability:.6f}")
    
    def calculate_centripetal_force(self, particle: Dict[str, Any]) -> float:
        """
        Calculate centripetal force for a quantum particle in wormhole space
        
        Args:
            particle: Quantum particle properties
            
        Returns:
            Centripetal force value
        """
        # Basic centripetal force: F = m * v² / r
        basic_force = particle['mass'] * (particle['velocity'] ** 2) / (particle['position'] + 1e-10)
        
        # Add gravitational component with φ-harmonic scaling
        gravity = self.gravity_constant * particle['mass'] / (particle['position'] ** 2 + 1e-10)
        
        # Add weight-based resonance force
        resonance = abs(1 - abs(particle['velocity'] / (self.phi * particle['weight'])))
        resonance_force = particle['mass'] * resonance * particle['weight'] * self.phi
        
        # Add angular momentum with weight consideration
        angular_momentum = particle['mass'] * particle['velocity'] * particle['position'] * particle['weight']
        momentum_force = angular_momentum * particle['weight'] * self.phi
        
        # Add quantum tunneling effect
        tunneling = np.exp(-particle['weight'] * particle['position']) * self.phi
        tunneling_force = particle['mass'] * tunneling * self.phi
        
        # Add complexity-based force
        complexity_force = particle['mass'] * particle['complexity'] * particle['weight'] * self.phi
        
        # Total force with φ-harmonic scaling
        total_force = (basic_force + gravity + resonance_force + momentum_force + 
                       tunneling_force + complexity_force) * self.bridge_factor
        
        return total_force
    
    def update_particle_position(self, particle: Dict[str, Any], dt: float) -> Dict[str, Any]:
        """
        Update particle position using centripetal force dynamics
        
        Args:
            particle: Quantum particle properties
            dt: Time step
            
        Returns:
            Updated particle properties
        """
        # Calculate force
        force = self.calculate_centripetal_force(particle)
        
        # Update position using force with weight scaling
        acceleration = force / particle['mass']
        particle['velocity'] += acceleration * dt * particle['weight']
        particle['position'] += particle['velocity'] * dt * particle['weight']
        
        # Apply weight-based damping with resonance
        resonance = abs(1 - abs(particle['velocity'] / (self.phi * particle['weight'])))
        damping = 1 - (1 / self.phi) * resonance * particle['weight']
        particle['velocity'] *= damping
        
        # Update angular velocity and radial position
        particle['angular_velocity'] = particle['velocity'] * self.bridge_factor
        particle['radial_position'] = particle['position'] * self.throat_factor
        
        # Update phi-resonance
        particle['phi_resonance'] = abs(1 - abs(particle['velocity'] / (self.phi * particle['weight'])))
        
        # Update spin and charge
        particle['spin'] = np.sin(particle['velocity'] * self.phi) * 0.5
        particle['charge'] = np.cos(particle['position'] * self.phi) * particle['weight']
        
        return particle
    
    def simulate_particle_trajectory(self, particle: Dict[str, Any], steps: int = 100) -> List[Dict[str, Any]]:
        """
        Simulate particle trajectory through wormhole space
        
        Args:
            particle: Initial quantum particle properties
            steps: Number of simulation steps
            
        Returns:
            List of particle states throughout trajectory
        """
        trajectory = [particle.copy()]
        current_particle = particle.copy()
        
        for _ in range(steps):
            current_particle = self.update_particle_position(current_particle, self.time_step)
            trajectory.append(current_particle.copy())
        
        return trajectory
    
    def calculate_trajectory_stability(self, trajectory: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Calculate stability metrics for a particle trajectory
        
        Args:
            trajectory: List of particle states
            
        Returns:
            Dictionary containing stability metrics
        """
        if not trajectory:
            return {
                'stability': 0.0,
                'coherence': 0.0,
                'resonance': 0.0,
                'traversability': 0.0
            }
        
        # Calculate average phi-resonance
        resonances = [p['phi_resonance'] for p in trajectory]
        avg_resonance = sum(resonances) / len(resonances)
        
        # Calculate position stability (lower variance = higher stability)
        positions = [p['position'] for p in trajectory]
        pos_variance = np.var(positions) if len(positions) > 1 else 0
        pos_stability = self.phi / (1 + pos_variance)
        
        # Calculate velocity stability (lower variance = higher stability)
        velocities = [p['velocity'] for p in trajectory]
        vel_variance = np.var(velocities) if len(velocities) > 1 else 0
        vel_stability = self.phi / (1 + vel_variance)
        
        # Calculate overall stability with φ-harmonic scaling
        stability = self.stability * pos_stability * vel_stability * avg_resonance
        
        # Calculate coherence with φ-harmonic scaling
        coherence = self.coherence * avg_resonance * pos_stability
        
        # Calculate traversability with φ-harmonic scaling
        traversability = stability * coherence * self.bridge_factor
        
        return {
            'stability': stability,
            'coherence': coherence,
            'resonance': avg_resonance,
            'traversability': traversability,
            'position_stability': pos_stability,
            'velocity_stability': vel_stability
        }
    
    def optimize_particle_properties(self, particle: Dict[str, Any]) -> Dict[str, Any]:
        """
        Optimize particle properties for stable wormhole traversal
        
        Args:
            particle: Initial quantum particle properties
            
        Returns:
            Optimized particle properties
        """
        # Create test variations with φ-harmonic scaling
        variations = []
        
        # Base particle
        variations.append(particle.copy())
        
        # Vary mass
        mass_up = particle.copy()
        mass_up['mass'] *= self.phi
        variations.append(mass_up)
        
        mass_down = particle.copy()
        mass_down['mass'] /= self.phi
        variations.append(mass_down)
        
        # Vary velocity
        vel_up = particle.copy()
        vel_up['velocity'] *= self.phi
        variations.append(vel_up)
        
        vel_down = particle.copy()
        vel_down['velocity'] /= self.phi
        variations.append(vel_down)
        
        # Vary weight
        weight_up = particle.copy()
        weight_up['weight'] *= self.phi
        variations.append(weight_up)
        
        weight_down = particle.copy()
        weight_down['weight'] /= self.phi
        variations.append(weight_down)
        
        # Simulate trajectories and find most stable
        best_stability = 0.0
        best_particle = particle.copy()
        
        for var in variations:
            trajectory = self.simulate_particle_trajectory(var, steps=50)
            metrics = self.calculate_trajectory_stability(trajectory)
            
            if metrics['stability'] > best_stability:
                best_stability = metrics['stability']
                best_particle = var.copy()
        
        # Fine-tune best particle with φ-harmonic resonance
        best_particle['phi_resonance'] = abs(1 - abs(best_particle['velocity'] / (self.phi * best_particle['weight'])))
        best_particle['angular_velocity'] = best_particle['velocity'] * self.bridge_factor
        best_particle['radial_position'] = best_particle['position'] * self.throat_factor
        
        return best_particle
    
    def optimize_particle_batch(self, particles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Optimize a batch of particles for stable wormhole traversal
        
        Args:
            particles: List of initial quantum particle properties
            
        Returns:
            List of optimized particle properties
        """
        optimized_particles = []
        
        for i, particle in enumerate(particles):
            print(f"Optimizing particle {i+1}/{len(particles)}...")
            optimized = self.optimize_particle_properties(particle)
            optimized_particles.append(optimized)
        
        # Update system metrics
        self.total_particles = len(optimized_particles)
        self.total_energy = sum(p['mass'] * (p['velocity'] ** 2) / 2 for p in optimized_particles)
        self.system_angular_momentum = sum(p['mass'] * p['velocity'] * p['position'] for p in optimized_particles)
        
        # Calculate system stability
        trajectories = [self.simulate_particle_trajectory(p, steps=20) for p in optimized_particles]
        stability_metrics = [self.calculate_trajectory_stability(t) for t in trajectories]
        self.system_stability = sum(m['stability'] for m in stability_metrics) / len(stability_metrics)
        
        return optimized_particles
    
    def calculate_traversal_metrics(self, optimized_particles: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Calculate traversal metrics for optimized particles
        
        Args:
            optimized_particles: List of optimized particle properties
            
        Returns:
            Dictionary containing traversal metrics
        """
        if not optimized_particles:
            return {
                'traversal_probability': 0.0,
                'traversal_time': 0.0,
                'traversal_energy': 0.0,
                'traversal_stability': 0.0
            }
        
        # Calculate trajectories
        trajectories = [self.simulate_particle_trajectory(p, steps=100) for p in optimized_particles]
        
        # Calculate stability metrics
        stability_metrics = [self.calculate_trajectory_stability(t) for t in trajectories]
        
        # Calculate traversal probability
        traversal_probs = [m['traversability'] for m in stability_metrics]
        avg_probability = sum(traversal_probs) / len(traversal_probs)
        
        # Calculate traversal time with φ-harmonic scaling
        traversal_times = [len(t) * self.time_step * self.phi for t in trajectories]
        avg_time = sum(traversal_times) / len(traversal_times)
        
        # Calculate traversal energy
        traversal_energies = [sum(p['mass'] * (p['velocity'] ** 2) / 2 for p in t) / len(t) for t in trajectories]
        avg_energy = sum(traversal_energies) / len(traversal_energies)
        
        # Calculate traversal stability
        traversal_stabilities = [m['stability'] for m in stability_metrics]
        avg_stability = sum(traversal_stabilities) / len(traversal_stabilities)
        
        return {
            'traversal_probability': avg_probability,
            'traversal_time': avg_time,
            'traversal_energy': avg_energy,
            'traversal_stability': avg_stability,
            'individual_probabilities': traversal_probs,
            'individual_times': traversal_times,
            'individual_energies': traversal_energies,
            'individual_stabilities': traversal_stabilities
        }
    
    def get_system_metrics(self) -> Dict[str, Any]:
        """
        Get current system metrics
        
        Returns:
            Dictionary containing system metrics
        """
        return {
            'total_particles': self.total_particles,
            'total_energy': self.total_energy,
            'system_angular_momentum': self.system_angular_momentum,
            'system_stability': self.system_stability,
            'bridge_factor': self.bridge_factor,
            'throat_factor': self.throat_factor,
            'stability': self.stability,
            'phi': self.phi,
            'phi_power': self.phi_power,
            'resonance': self.resonance,
            'coherence': self.coherence
        }

def test_particle_centripetal_engine():
    """Test the Quantum Particle Centripetal Engine"""
    print("\n⚛️ Quantum Particle Centripetal Engine Test ⚛️")
    print("=" * 50)
    
    # Initialize engine
    engine = QuantumParticleCentripetalEngine()
    
    # Create test particles with φ-harmonic properties
    test_particles = []
    for i in range(5):
        particle = {
            'position': 1.0 + i * 0.1,
            'velocity': 0.5 + i * 0.05,
            'mass': 1.0 + i * 0.1,
            'spin': 0.5,
            'charge': 0.0,
            'radial_position': (1.0 + i * 0.1) * engine.throat_factor,
            'angular_velocity': (0.5 + i * 0.05) * engine.bridge_factor,
            'weight': 1.0 + i * 0.1,
            'complexity': 1.0 + i * 0.05,
            'phi_resonance': 0.5
        }
        test_particles.append(particle)
    
    print(f"\nCreated {len(test_particles)} test particles with φ-harmonic properties")
    
    # Optimize particles
    print("\nOptimizing particles for stable wormhole traversal...")
    optimized_particles = engine.optimize_particle_batch(test_particles)
    
    print("\nOptimization complete!")
    print("\nOriginal vs. Optimized Properties (First Particle):")
    print(f"Position: {test_particles[0]['position']:.4f} → {optimized_particles[0]['position']:.4f}")
    print(f"Velocity: {test_particles[0]['velocity']:.4f} → {optimized_particles[0]['velocity']:.4f}")
    print(f"Mass: {test_particles[0]['mass']:.4f} → {optimized_particles[0]['mass']:.4f}")
    print(f"Weight: {test_particles[0]['weight']:.4f} → {optimized_particles[0]['weight']:.4f}")
    print(f"φ-Resonance: {test_particles[0]['phi_resonance']:.4f} → {optimized_particles[0]['phi_resonance']:.4f}")
    
    # Calculate traversal metrics
    print("\nCalculating traversal metrics...")
    metrics = engine.calculate_traversal_metrics(optimized_particles)
    
    print("\nTraversal Metrics:")
    print(f"Traversal Probability: {metrics['traversal_probability']:.6f}")
    print(f"Traversal Time: {metrics['traversal_time']:.6f} time units")
    print(f"Traversal Energy: {metrics['traversal_energy']:.6f} energy units")
    print(f"Traversal Stability: {metrics['traversal_stability']:.6f}")
    
    # Get system metrics
    system_metrics = engine.get_system_metrics()
    
    print("\nSystem Metrics:")
    print(f"Total Particles: {system_metrics['total_particles']}")
    print(f"Total Energy: {system_metrics['total_energy']:.6f}")
    print(f"System Angular Momentum: {system_metrics['system_angular_momentum']:.6f}")
    print(f"System Stability: {system_metrics['system_stability']:.6f}")
    
    # Simulate trajectory for first optimized particle
    print("\nSimulating trajectory for first optimized particle...")
    trajectory = engine.simulate_particle_trajectory(optimized_particles[0], steps=10)
    
    print("\nTrajectory Snapshot (First 5 steps):")
    for i, state in enumerate(trajectory[:5]):
        print(f"Step {i}: Position={state['position']:.4f}, Velocity={state['velocity']:.4f}, φ-Resonance={state['phi_resonance']:.4f}")
    
    # Calculate trajectory stability
    stability_metrics = engine.calculate_trajectory_stability(trajectory)
    
    print("\nTrajectory Stability Metrics:")
    print(f"Stability: {stability_metrics['stability']:.6f}")
    print(f"Coherence: {stability_metrics['coherence']:.6f}")
    print(f"Resonance: {stability_metrics['resonance']:.6f}")
    print(f"Traversability: {stability_metrics['traversability']:.6f}")
    print(f"Position Stability: {stability_metrics['position_stability']:.6f}")
    print(f"Velocity Stability: {stability_metrics['velocity_stability']:.6f}")

if __name__ == "__main__":
    test_particle_centripetal_engine()
