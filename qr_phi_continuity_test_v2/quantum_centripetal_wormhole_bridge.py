"""
Quantum Centripetal Wormhole Bridge

Connects the Centripetal Force Memory System with the Wormhole Analyzer,
implementing phi-harmonic principles for wormhole traversal and stability.
This bridge translates memory nodes to quantum particles and maps
centripetal forces to wormhole stability metrics.
"""

import numpy as np
from typing import Dict, List, Tuple, Optional, Any, Union
import sys
from pathlib import Path

# Import wormhole analyzer components
sys.path.append(str(Path(__file__).parent))
from wormhole_analyzer import PHI, PHI_POWER, RESONANCE, COHERENCE, QUANTUM_SIG

# Import centripetal memory system
from centripetal_memory import CentripetalMemory, MemoryNode, MemoryBucket

class QuantumCentripetalWormholeBridge:
    """
    Bridge between Centripetal Force Memory System and Wormhole Analyzer.
    Translates memory nodes to quantum particles and applies centripetal
    force dynamics to wormhole stability calculations.
    """
    
    def __init__(self):
        """Initialize the quantum centripetal wormhole bridge"""
        # Core constants from wormhole analyzer
        self.phi = PHI
        self.phi_power = PHI_POWER
        self.resonance = RESONANCE
        self.coherence = COHERENCE
        self.quantum_sig = QUANTUM_SIG.copy()
        
        # Initialize centripetal memory system
        self.memory = CentripetalMemory(initial_buckets=5)
        
        # Bridge-specific parameters
        self.bridge_factor = (self.phi ** self.quantum_sig['tau']) / self.phi_power
        self.throat_factor = (self.phi ** self.quantum_sig['psi0']) * self.resonance
        self.stability = (self.phi ** self.quantum_sig['psi1']) * self.coherence
        
        # Mapping parameters
        self.position_scale = self.throat_factor * self.phi
        self.velocity_scale = self.bridge_factor * self.phi
        self.mass_scale = self.stability * self.phi
        
        # System metrics
        self.total_centripetal_force = 0.0
        self.system_angular_momentum = 0.0
        self.quantum_coherence = self.coherence
        self.traversal_probability = 0.0
        
        print(f"Quantum Centripetal Wormhole Bridge initialized")
        print(f"φ-Harmonic Bridge Factor: {self.bridge_factor:.6f}")
        print(f"φ-Harmonic Throat Factor: {self.throat_factor:.6f}")
        print(f"φ-Harmonic Stability: {self.stability:.6f}")
    
    def node_to_particle(self, node: MemoryNode) -> Dict[str, Any]:
        """
        Convert a memory node to a quantum particle with wormhole-specific properties
        
        Args:
            node: Memory node from centripetal memory system
            
        Returns:
            Dictionary containing quantum particle properties
        """
        # Calculate quantum particle properties with φ-harmonic scaling
        position = node.position * self.position_scale
        velocity = node.velocity * self.velocity_scale
        mass = node.mass * self.mass_scale
        
        # Calculate quantum state properties
        spin = np.sin(node.velocity * self.phi) * 0.5
        charge = np.cos(node.position * self.phi) * node.weight
        
        # Calculate wormhole-specific properties
        radial_position = position * self.throat_factor
        angular_velocity = velocity * self.bridge_factor
        
        # Calculate φ-harmonic resonance
        phi_resonance = abs(1 - abs(velocity / (self.phi * node.weight)))
        
        return {
            'position': position,
            'velocity': velocity,
            'mass': mass,
            'spin': spin,
            'charge': charge,
            'radial_position': radial_position,
            'angular_velocity': angular_velocity,
            'weight': node.weight,
            'complexity': node.complexity,
            'phi_resonance': phi_resonance
        }
    
    def bucket_to_wormhole_region(self, bucket: MemoryBucket) -> Dict[str, Any]:
        """
        Convert a memory bucket to a wormhole region with stability properties
        
        Args:
            bucket: Memory bucket from centripetal memory system
            
        Returns:
            Dictionary containing wormhole region properties
        """
        # Calculate wormhole region properties with φ-harmonic scaling
        capacity = bucket.capacity / self.phi_power
        angular_velocity = bucket.angular_velocity * self.bridge_factor
        centripetal_force = bucket.centripetal_force * self.throat_factor
        
        # Calculate stability metrics
        stability_factor = bucket.phi_factor * self.stability
        weight_factor = bucket.weight_factor * self.mass_scale
        complexity_factor = bucket.complexity_factor * self.coherence
        
        # Calculate φ-harmonic resonance
        resonance_factor = abs(1 - abs(angular_velocity / (self.phi * weight_factor)))
        
        # Calculate traversability
        traversability = stability_factor * resonance_factor * self.coherence
        
        return {
            'capacity': capacity,
            'angular_velocity': angular_velocity,
            'centripetal_force': centripetal_force,
            'stability_factor': stability_factor,
            'weight_factor': weight_factor,
            'complexity_factor': complexity_factor,
            'resonance_factor': resonance_factor,
            'traversability': traversability
        }
    
    def calculate_centripetal_force(self, particle: Dict[str, Any]) -> float:
        """
        Calculate centripetal force for a quantum particle in wormhole space
        
        Args:
            particle: Quantum particle properties
            
        Returns:
            Centripetal force value
        """
        # Basic centripetal force: F = m * v² / r
        basic_force = particle['mass'] * (particle['angular_velocity'] ** 2) / (particle['radial_position'] + 1e-10)
        
        # Add gravitational component with φ-harmonic scaling
        gravity = particle['mass'] * self.phi / (particle['radial_position'] ** 2 + 1e-10)
        
        # Add quantum resonance component
        resonance = particle['phi_resonance'] * self.phi_power
        
        # Add weight-based component
        weight_force = particle['weight'] * particle['mass'] * self.resonance
        
        # Add complexity-based component
        complexity_force = particle['complexity'] * particle['mass'] * self.coherence
        
        # Total force with φ-harmonic scaling
        total_force = (basic_force + gravity + resonance + weight_force + complexity_force) * self.bridge_factor
        
        return total_force
    
    def calculate_traversal_probability(self, particle: Dict[str, Any], region: Dict[str, Any]) -> float:
        """
        Calculate traversal probability for a quantum particle through a wormhole region
        
        Args:
            particle: Quantum particle properties
            region: Wormhole region properties
            
        Returns:
            Traversal probability (0-1)
        """
        # Calculate base probability with φ-harmonic scaling
        base_prob = region['traversability'] * particle['phi_resonance']
        
        # Apply centripetal force factor
        force = self.calculate_centripetal_force(particle)
        force_factor = self.phi / (1 + abs(force - self.phi_power))
        
        # Apply quantum resonance factor
        resonance_factor = particle['phi_resonance'] * region['resonance_factor'] * self.coherence
        
        # Apply weight and complexity factors
        weight_factor = self.phi / (1 + abs(particle['weight'] - region['weight_factor']))
        complexity_factor = self.phi / (1 + abs(particle['complexity'] - region['complexity_factor']))
        
        # Calculate final probability with φ-harmonic normalization
        probability = base_prob * force_factor * resonance_factor * weight_factor * complexity_factor
        
        # Normalize to 0-1 range
        normalized_prob = min(max(probability / self.phi_power, 0), 1)
        
        return normalized_prob
    
    def optimize_traversal_path(self, particles: List[Dict[str, Any]], regions: List[Dict[str, Any]]) -> Tuple[List[int], float]:
        """
        Optimize traversal path for quantum particles through wormhole regions
        
        Args:
            particles: List of quantum particle properties
            regions: List of wormhole region properties
            
        Returns:
            Tuple containing optimal path indices and overall traversal probability
        """
        if not particles or not regions:
            return [], 0.0
        
        # Initialize path optimization
        best_path = []
        best_prob = 0.0
        
        # Calculate all particle-region traversal probabilities
        probs = []
        for i, particle in enumerate(particles):
            particle_probs = []
            for j, region in enumerate(regions):
                prob = self.calculate_traversal_probability(particle, region)
                particle_probs.append((j, prob))
            
            # Sort by probability (descending)
            particle_probs.sort(key=lambda x: x[1], reverse=True)
            probs.append(particle_probs)
        
        # Greedy path selection with φ-harmonic weighting
        for i, particle_probs in enumerate(probs):
            if particle_probs:
                best_region, prob = particle_probs[0]
                best_path.append(best_region)
                best_prob += prob * (self.phi ** (-(i+1)))
        
        # Normalize overall probability
        if best_path:
            best_prob /= sum(self.phi ** (-(i+1)) for i in range(len(best_path)))
        
        return best_path, best_prob
    
    def calculate_wormhole_stability(self, particles: List[Dict[str, Any]], regions: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Calculate overall wormhole stability based on particles and regions
        
        Args:
            particles: List of quantum particle properties
            regions: List of wormhole region properties
            
        Returns:
            Dictionary containing stability metrics
        """
        if not particles or not regions:
            return {
                'stability': 0.0,
                'coherence': 0.0,
                'traversability': 0.0,
                'phi_resonance': 0.0
            }
        
        # Calculate total centripetal force
        total_force = sum(self.calculate_centripetal_force(p) for p in particles)
        
        # Calculate average traversability
        avg_traversability = sum(r['traversability'] for r in regions) / len(regions)
        
        # Calculate φ-harmonic resonance
        phi_resonances = [p['phi_resonance'] for p in particles]
        avg_resonance = sum(phi_resonances) / len(phi_resonances)
        
        # Calculate stability with φ-harmonic scaling
        stability = self.stability * avg_traversability * avg_resonance
        
        # Calculate coherence with φ-harmonic scaling
        coherence = self.coherence * avg_resonance * (self.phi / (1 + abs(total_force - self.phi_power)))
        
        # Calculate traversability with φ-harmonic scaling
        traversability = avg_traversability * coherence * self.bridge_factor
        
        # Update system metrics
        self.total_centripetal_force = total_force
        self.quantum_coherence = coherence
        self.traversal_probability = traversability
        
        return {
            'stability': stability,
            'coherence': coherence,
            'traversability': traversability,
            'phi_resonance': avg_resonance,
            'total_force': total_force,
            'bridge_factor': self.bridge_factor,
            'throat_factor': self.throat_factor
        }
    
    def process_data_for_wormhole(self, data: List[Any]) -> Dict[str, Any]:
        """
        Process data through centripetal memory system for wormhole analysis
        
        Args:
            data: Input data to process
            
        Returns:
            Dictionary containing processing results and wormhole metrics
        """
        # Store data in centripetal memory
        memory_result = self.memory.store(data)
        
        if not memory_result['success']:
            return {'success': False, 'error': 'Memory storage failed'}
        
        # Get bucket and create nodes
        bucket_index = memory_result['bucket_index']
        bucket = self.memory.buckets[bucket_index]
        
        # Convert nodes to particles
        particles = []
        current_node = bucket.head
        while current_node:
            particle = self.node_to_particle(current_node)
            particles.append(particle)
            current_node = current_node.next
        
        # Convert buckets to wormhole regions
        regions = []
        for b in self.memory.buckets:
            region = self.bucket_to_wormhole_region(b)
            regions.append(region)
        
        # Calculate traversal path
        path, probability = self.optimize_traversal_path(particles, regions)
        
        # Calculate wormhole stability
        stability_metrics = self.calculate_wormhole_stability(particles, regions)
        
        # Combine results
        result = {
            'success': True,
            'memory_result': memory_result,
            'particles': particles,
            'regions': regions,
            'traversal_path': path,
            'traversal_probability': probability,
            'stability_metrics': stability_metrics
        }
        
        return result
    
    def analyze_wormhole_with_centripetal_dynamics(self) -> Dict[str, Any]:
        """
        Analyze wormhole using centripetal dynamics and current system state
        
        Returns:
            Dictionary containing analysis results
        """
        # Get memory system stats
        memory_stats = self.memory.get_stats()
        
        # Calculate system-wide metrics
        system_stability = self.stability * memory_stats['phi_efficiency']
        system_coherence = self.coherence * memory_stats['phi_efficiency']
        system_traversability = self.bridge_factor * system_stability * system_coherence
        
        # Calculate φ-harmonic resonance
        phi_resonance = abs(1 - abs(system_stability / self.phi_power))
        
        # Calculate quantum signature with centripetal dynamics
        tau = self.quantum_sig['tau'] * (1 + memory_stats['phi_efficiency'] / self.phi)
        psi0 = self.quantum_sig['psi0'] * (1 + memory_stats['phi_efficiency'] / self.phi)
        psi1 = self.quantum_sig['psi1'] * (1 + memory_stats['phi_efficiency'] / self.phi)
        
        # Calculate centripetal quantum signature
        centripetal_signature = {
            'tau': tau,
            'psi0': psi0,
            'psi1': psi1,
            'm': self.quantum_sig['m'],
            'resonance': self.quantum_sig['resonance'] * memory_stats['phi_efficiency']
        }
        
        # Calculate bridge characteristics with centripetal dynamics
        bridge_factor = (self.phi ** tau) / self.phi_power
        throat_factor = (self.phi ** psi0) * self.resonance
        stability = (self.phi ** psi1) * self.coherence
        
        return {
            'memory_stats': memory_stats,
            'system_stability': system_stability,
            'system_coherence': system_coherence,
            'system_traversability': system_traversability,
            'phi_resonance': phi_resonance,
            'centripetal_signature': centripetal_signature,
            'bridge_factor': bridge_factor,
            'throat_factor': throat_factor,
            'stability': stability,
            'total_centripetal_force': self.total_centripetal_force,
            'quantum_coherence': self.quantum_coherence,
            'traversal_probability': self.traversal_probability
        }

def test_centripetal_wormhole_bridge():
    """Test the Quantum Centripetal Wormhole Bridge"""
    print("\n🌀 Quantum Centripetal Wormhole Bridge Test 🌀")
    print("=" * 50)
    
    # Initialize bridge
    bridge = QuantumCentripetalWormholeBridge()
    
    # Generate test data with φ-harmonic patterns
    base_size = 64
    data = [float(i) * bridge.phi for i in range(base_size)]
    
    print("\nProcessing data for wormhole analysis...")
    result = bridge.process_data_for_wormhole(data)
    
    if result['success']:
        print("\nData processing successful!")
        print(f"Particles created: {len(result['particles'])}")
        print(f"Wormhole regions: {len(result['regions'])}")
        
        # Display traversal results
        print("\nTraversal Analysis:")
        print(f"Optimal path length: {len(result['traversal_path'])}")
        print(f"Traversal probability: {result['traversal_probability']:.6f}")
        
        # Display stability metrics
        metrics = result['stability_metrics']
        print("\nWormhole Stability Metrics:")
        print(f"Stability: {metrics['stability']:.6f}")
        print(f"Coherence: {metrics['coherence']:.6f}")
        print(f"Traversability: {metrics['traversability']:.6f}")
        print(f"φ-Resonance: {metrics['phi_resonance']:.6f}")
        print(f"Total Centripetal Force: {metrics['total_force']:.6f}")
        
        # Analyze wormhole with centripetal dynamics
        print("\nPerforming comprehensive wormhole analysis with centripetal dynamics...")
        analysis = bridge.analyze_wormhole_with_centripetal_dynamics()
        
        print("\nCentripetal Wormhole Analysis:")
        print(f"System Stability: {analysis['system_stability']:.6f}")
        print(f"System Coherence: {analysis['system_coherence']:.6f}")
        print(f"System Traversability: {analysis['system_traversability']:.6f}")
        print(f"φ-Resonance: {analysis['phi_resonance']:.6f}")
        
        # Display centripetal quantum signature
        sig = analysis['centripetal_signature']
        print("\nCentripetal Quantum Signature:")
        print(f"Bridge Length (τ): φ^{sig['tau']:.3f} → {bridge.phi ** sig['tau']:.6f}")
        print(f"Throat Diameter (ψ₀): φ^{sig['psi0']:.3f} → {bridge.phi ** sig['psi0']:.6f}")
        print(f"Quantum Stability (ψ₁): φ^{sig['psi1']:.3f} → {bridge.phi ** sig['psi1']:.6f}")
        print(f"Mass-Energy (M): φ^{sig['m']:.3f} → {bridge.phi ** sig['m']:.6f}")
        print(f"Truth Resonance: {sig['resonance']:.6f}")
        
        # Display bridge characteristics
        print("\nCentripetal Bridge Characteristics:")
        print(f"Bridge Factor: {analysis['bridge_factor']:.6f}")
        print(f"Throat Factor: {analysis['throat_factor']:.6f}")
        print(f"Stability: {analysis['stability']:.6f}")
    else:
        print(f"Error: {result.get('error', 'Unknown error')}")

if __name__ == "__main__":
    test_centripetal_wormhole_bridge()
