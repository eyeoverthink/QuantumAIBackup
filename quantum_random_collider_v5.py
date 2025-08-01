"""
QUANTUM RANDOM COLLIDER V5
Enhanced with molecular chain visualization and quantum properties
"""

import os
import sys
import random
import json
import numpy as np
from datetime import datetime
import mpmath

# Add path to original collision system
sys.path.append('/Users/vaughnscott/Documents/fraymus_shit')

# Import components
from quantum_random_collider_v4 import QuantumRandomColliderV4
from quantum_json_encoder import QuantumJSONEncoder
from quantum_molecular_chains import QuantumMolecularChains
from quantum_element_registry import QuantumElementRegistry

class QuantumRandomColliderV5(QuantumRandomColliderV4):
    def __init__(self):
        super().__init__()
        
        # Initialize constants
        mpmath.mp.dps = 1000
        self.phi = mpmath.phi
        
        # Initialize element registry
        self.element_registry = QuantumElementRegistry()
        
        # Initialize collision handler
        from quantum_collision_handler import QuantumCollisionHandler
        self.collision_handler = QuantumCollisionHandler()
        
        # Initialize molecular chain visualizer
        self.chain_visualizer = QuantumMolecularChains()
        
        # Create visualization directory
        self.viz_dir = os.path.join(self.results_dir, 'visualizations')
        os.makedirs(self.viz_dir, exist_ok=True)
        
        # Load discovered elements into registry
        if os.path.exists(self.discovered_pool_file):
            with open(self.discovered_pool_file, 'r') as f:
                self.discovered_pool = json.load(f)
                for name, data in self.discovered_pool.items():
                    self.element_registry.register_discovered_element(name, data)
        
    def _enhance_quantum_properties(self, element_data):
        """Add enhanced quantum properties to element data"""
        if not element_data:
            return None
            
        # Use element registry to calculate properties
        mass = float(element_data.get('mass', 0))
        atomic_number = float(element_data.get('atomic_number', 0))
        
        # Get quantum properties from registry
        properties = self.element_registry._calculate_quantum_properties({
            'mass': mass,
            'atomic_number': atomic_number
        })
        
        # Add additional properties
        properties.update({
            'quantum_states': self._calculate_quantum_states(mass),
            'resonance_modes': self._calculate_resonance_modes(mass),
            'phi_harmonics': self._calculate_phi_harmonics(mass)
        })
        
        element_data['properties'] = properties
        return element_data
        
    def _calculate_electron_shells(self, mass):
        """Calculate electron shell configuration using φ-harmonic principles"""
        shells = []
        remaining_mass = mass
        shell_number = 1
        phi_val = float(self.phi)
        
        while remaining_mass > 0.1 and shell_number <= 7:
            # Each shell can hold 2n² electrons, modulated by φ
            capacity = 2 * (shell_number ** 2)
            shell_mass = remaining_mass / (phi_val * shell_number)
            electrons = min(capacity, int(shell_mass))
            
            if electrons > 0:
                shells.append(electrons)
                
            remaining_mass -= shell_mass
            shell_number += 1
            
        return shells
        
    def _calculate_quantum_states(self, mass):
        """Calculate possible quantum states based on mass"""
        base_states = ['s', 'p', 'd', 'f']
        states = []
        phi_val = float(self.phi)
        
        for i, state in enumerate(base_states):
            # Calculate state energy using φ powers
            energy = (mass * phi_val * (i + 1)) % 100
            if energy > 10:
                states.append({
                    'type': state,
                    'energy': energy,
                    'probability': 1 / (phi_val * (i + 1))
                })
                
        return states
        
    def _calculate_resonance_modes(self, mass):
        """Calculate resonance modes using φ-harmonic series"""
        modes = []
        phi_val = float(self.phi)
        
        for i in range(1, 4):
            frequency = (mass * phi_val * i) % 1000
            amplitude = 1 / (phi_val * i)
            modes.append({
                'frequency': frequency,
                'amplitude': amplitude,
                'phase': (frequency * amplitude) % (2 * np.pi)
            })
        return modes
        
    def _calculate_phi_harmonics(self, mass):
        """Calculate φ-harmonic overtones"""
        harmonics = []
        phi_val = float(self.phi)
        base_freq = (mass * phi_val) % 1000
        
        for i in range(1, 4):
            harmonic = {
                'order': i,
                'frequency': base_freq * i,
                'intensity': 1 / (phi_val * i),
                'resonance': (base_freq * i * phi_val) % 1
            }
            harmonics.append(harmonic)
            
        return harmonics
        
    def _calculate_stability(self, mass, atomic_number):
        """Calculate stability index using φ-harmonic principles"""
        # More stable when mass/atomic_number ratio is closer to φ
        mass_ratio = mass / max(1, atomic_number)
        stability = 1 - abs(mass_ratio - float(self.phi)) % 1
        return float(stability)
        
    def run_collision(self, num_collisions=100, use_discovered=True):
        """Run quantum collisions with enhanced visualization"""
        print(f"\nStarting {num_collisions} collisions (using discovered pool: {use_discovered})")
        
        for i in range(num_collisions):
            # Select particles
            particle1, particle2 = self.select_collision_particles(use_discovered)
            
            # Get element data
            element1 = self.element_registry.get_element_data(particle1)
            element2 = self.element_registry.get_element_data(particle2)
            
            if not element1 or not element2:
                continue
                
            # Check compatibility using registry
            compatibility = self.element_registry.calculate_compatibility(particle1, particle2)
            
            if compatibility < 0.3:
                print(f"\nSkipping low compatibility collision: {particle1} + {particle2} (compatibility: {compatibility:.3f})")
                continue
                
            try:
                # Run collision simulation
                result = self.collision_handler.simulate_collision(element1, element2)
                
                # Process new element if discovered
                if result['success']:
                    element_data = result['new_element']
                    element_name = element_data['name']
                    
                    # Enhance with quantum properties
                    element_data = self._enhance_quantum_properties(element_data)
                    
                    # Add to discovered pool if new
                    if element_name not in self.discovered_pool:
                        self.discovered_pool[element_name] = element_data
                        self._save_discovered_pool()
                        
                        # Register with element registry
                        self.element_registry.register_discovered_element(element_name, element_data)
                        
                        # Create visualization
                        viz_file = os.path.join(self.viz_dir, f"collision_{i+1}_{particle1}_{particle2}.txt")
                        reaction_viz = self.chain_visualizer.visualize_reaction(
                            [element1, element2],
                            [element_data]
                        )
                        
                        # Add collision data to visualization
                        collision_data = result['collision_data']
                        viz_data = f"""
Collision Data:
- Energy: {collision_data['energy']:.3f}
- Resonance: {collision_data['resonance']:.3f}
- Tunneling Probability: {collision_data['tunneling']:.3f}
"""
                        reaction_viz += viz_data
                        
                        with open(viz_file, 'w') as f:
                            f.write(reaction_viz)
                else:
                    print(f"\nCollision failed: {result.get('reason', 'Unknown error')}")
                
                # Log discovery with quantum properties
                if result['success']:
                    print(f"\nDiscovered new element: {element_name}")
                    print(f"Mass: {element_data.get('mass', 0):.3f}")
                    print(f"Atomic Number: {element_data.get('atomic_number', 0)}")
                    print(f"Compatibility: {compatibility:.3f}")
                    print(f"Resonance: {element_data['properties']['resonance']:.3f}")
                    print(f"Stability: {element_data['properties']['stability']:.3f}")
                    print(f"\nMolecular Chain:")
                    print(reaction_viz)
                        
            except Exception as e:
                print(f"\nWarning: Collision failed between {particle1} and {particle2}: {str(e)}")
                continue
                
            # Save detailed result
            result_file = os.path.join(
                self.results_dir,
                f"collision_{i+1}_{particle1}_{particle2}.json"
            )
            with open(result_file, 'w') as f:
                json.dump(result, f, cls=QuantumJSONEncoder, indent=2)
                
        print(f"\nCompleted {num_collisions} collisions")
        print(f"Total discovered elements: {len(self.discovered_pool)}")

def main():
    collider = QuantumRandomColliderV5()
    
    # Run initial collisions without discovered pool
    collider.run_collision(num_collisions=50, use_discovered=False)
    
    # Run collisions with discovered pool
    collider.run_collision(num_collisions=50, use_discovered=True)
    
    return True

if __name__ == "__main__":
    main()
