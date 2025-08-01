"""
QUANTUM RANDOM COLLIDER V3
Extends V2 with support for discovered elements pool and φ-harmonic collision selection
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

# Import the original systems
from quantum_random_collider_v2 import QuantumRandomCollider
from quantum_json_encoder import QuantumJSONEncoder
from quantum_collision_evolution import QuantumCollisionEvolution

class QuantumRandomColliderV3(QuantumRandomCollider):
    def __init__(self):
        super().__init__()
        
        # Initialize discovered elements pool
        self.discovered_pool = {}
        self.discovered_pool_file = 'discovered_elements_pool.json'
        self._load_discovered_pool()
        
        # Initialize φ constants for harmonic selection
        mpmath.mp.dps = 1000
        self.phi = mpmath.phi
        
    def _load_discovered_pool(self):
        """Load previously discovered elements from disk"""
        if os.path.exists(self.discovered_pool_file):
            try:
                with open(self.discovered_pool_file, 'r') as f:
                    self.discovered_pool = json.load(f)
                print(f"Loaded {len(self.discovered_pool)} discovered elements")
            except json.JSONDecodeError:
                print("Warning: Could not load discovered elements pool")
                self.discovered_pool = {}
                
    def _save_discovered_pool(self):
        """Save discovered elements pool to disk"""
        with open(self.discovered_pool_file, 'w') as f:
            json.dump(self.discovered_pool, f, cls=QuantumJSONEncoder, indent=2)
            
    def _calculate_resonance(self, element_data):
        """Calculate φ-resonance for an element based on its properties"""
        mass = float(element_data.get('mass', 0))
        atomic_number = float(element_data.get('atomic_number', 0))
        
        # Use φ-harmonic resonance calculation
        resonance = float((self.phi * mass + atomic_number) % 1)
        return resonance
        
    def select_collision_particles(self, use_discovered=True):
        """Select particles for collision with option to use discovered elements"""
        available_elements = list(self.collision_system.elements.items())
        
        if use_discovered and self.discovered_pool:
            # Add discovered elements to selection pool
            available_elements.extend(list(self.discovered_pool.items()))
            
        # Calculate resonances for all available elements
        resonances = {name: self._calculate_resonance(data) for name, data in available_elements}
        
        # Select particles using φ-harmonic weighting
        weights = [1 / (res + 0.0001) for res in resonances.values()]  # Add small constant to avoid division by zero
        
        # Select two particles
        selected = random.choices(available_elements, weights=weights, k=2)
        return selected[0][0], selected[1][0]  # Return element names
        
    def run_collision(self, num_collisions=100, use_discovered=True):
        """Run quantum collisions with option to use discovered elements"""
        print(f"\nStarting {num_collisions} collisions (using discovered pool: {use_discovered})")
        
        for i in range(num_collisions):
            # Select particles
            particle1, particle2 = self.select_collision_particles(use_discovered)
            
            # Run collision
            try:
                result = self.collision_system.simulate_collision([particle1, particle2])
            except Exception as e:
                print(f"\nWarning: Collision failed between {particle1} and {particle2}: {str(e)}")
                continue
            
            # Save result if new element discovered
            if result.get('new_element'):
                element_data = result['new_element']
                element_name = element_data['name']
                
                # Add to discovered pool
                if element_name not in self.discovered_pool:
                    self.discovered_pool[element_name] = element_data
                    self._save_discovered_pool()
                    
                    # Log discovery
                    print(f"\nDiscovered new element: {element_name}")
                    print(f"Mass: {element_data.get('mass')}")
                    print(f"Properties: {element_data.get('properties', {})}")
                    
            # Save detailed result
            result_file = os.path.join(
                self.results_dir,
                f"collision_{i+1}_{particle1}_{particle2}.json"
            )
            with open(result_file, 'w') as f:
                json.dump(result, f, cls=QuantumJSONEncoder, indent=2)
                
            # Update log
            with open(self.log_file, 'a') as f:
                f.write(f"\n## Collision {i+1}\n")
                f.write(f"- Particle 1: {particle1}\n")
                f.write(f"- Particle 2: {particle2}\n")
                if result.get('new_element'):
                    f.write(f"- **New Element Discovered**: {result['new_element']['name']}\n")
                f.write(f"- Resonance: {result.get('resonance', 'N/A')}\n")
                
        print(f"\nCompleted {num_collisions} collisions")
        print(f"Total discovered elements: {len(self.discovered_pool)}")

def main():
    collider = QuantumRandomColliderV3()
    
    # Run initial collisions without discovered pool
    collider.run_collision(num_collisions=50, use_discovered=False)
    
    # Run collisions with discovered pool
    collider.run_collision(num_collisions=50, use_discovered=True)
    
    return True

if __name__ == "__main__":
    main()
