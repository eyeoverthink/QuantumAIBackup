"""
QUANTUM RANDOM COLLIDER V4
Enhanced version with improved element handling and φ-harmonic collision prediction
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
from quantum_random_collider_v2 import QuantumRandomCollider
from quantum_json_encoder import QuantumJSONEncoder
from quantum_collision_evolution import QuantumCollisionEvolution
from quantum_element_handler import QuantumElementHandler

class QuantumRandomColliderV4(QuantumRandomCollider):
    def __init__(self):
        super().__init__()
        
        # Initialize element handler
        self.element_handler = QuantumElementHandler()
        
        # Initialize discovered elements pool
        self.discovered_pool = {}
        self.discovered_pool_file = 'discovered_elements_pool.json'
        self._load_discovered_pool()
        
        # Register known elements
        self._register_known_elements()
        
    def _register_known_elements(self):
        """Register known elements from collision system"""
        for name, data in self.collision_system.elements.items():
            self.element_handler.register_known_element(name, data)
            
    def _load_discovered_pool(self):
        """Load previously discovered elements"""
        if os.path.exists(self.discovered_pool_file):
            try:
                with open(self.discovered_pool_file, 'r') as f:
                    self.discovered_pool = json.load(f)
                print(f"Loaded {len(self.discovered_pool)} discovered elements")
                
                # Register discovered elements
                for name, data in self.discovered_pool.items():
                    self.element_handler.register_discovered_element(name, data)
            except json.JSONDecodeError:
                print("Warning: Could not load discovered elements pool")
                self.discovered_pool = {}
                
    def _save_discovered_pool(self):
        """Save discovered elements pool to disk"""
        with open(self.discovered_pool_file, 'w') as f:
            json.dump(self.discovered_pool, f, cls=QuantumJSONEncoder, indent=2)
            
    def select_collision_particles(self, use_discovered=True):
        """Select particles for collision with φ-harmonic weighting"""
        available_elements = list(self.collision_system.elements.keys())
        
        if use_discovered and self.discovered_pool:
            available_elements.extend(list(self.discovered_pool.keys()))
            
        # Calculate resonances and weights
        weights = []
        for name in available_elements:
            element = self.element_handler.get_element_data(name)
            if element:
                # Use inverse resonance as weight (lower resonance = higher probability)
                weight = 1 / (element['resonance'] + 0.0001)
                weights.append(weight)
            else:
                weights.append(0.0001)  # Small weight for unknown elements
                
        # Select two particles
        selected = random.choices(available_elements, weights=weights, k=2)
        return selected[0], selected[1]
        
    def run_collision(self, num_collisions=100, use_discovered=True):
        """Run quantum collisions with enhanced element handling"""
        print(f"\nStarting {num_collisions} collisions (using discovered pool: {use_discovered})")
        
        for i in range(num_collisions):
            # Select particles
            particle1, particle2 = self.select_collision_particles(use_discovered)
            
            # Check compatibility
            compatibility = self.element_handler.calculate_compatibility(particle1, particle2)
            
            if compatibility < 0.3:  # Skip low compatibility collisions
                print(f"\nSkipping low compatibility collision: {particle1} + {particle2} (compatibility: {compatibility:.3f})")
                continue
                
            # Predict collision result
            prediction = self.element_handler.predict_collision_result(particle1, particle2)
            
            if not prediction:
                print(f"\nWarning: Could not predict collision between {particle1} and {particle2}")
                continue
                
            new_name, new_properties = prediction
            
            try:
                # Run collision simulation
                result = self.collision_system.simulate_collision([particle1, particle2])
                
                # Enhance result with predicted properties
                result['predicted_name'] = new_name
                result['predicted_properties'] = new_properties
                result['compatibility'] = compatibility
                
                # Process new element if discovered
                if result.get('new_element'):
                    element_data = result['new_element']
                    element_name = new_name  # Use predicted name
                    
                    # Add quantum properties
                    element_data.update(new_properties)
                    
                    # Add to discovered pool if new
                    if element_name not in self.discovered_pool:
                        self.discovered_pool[element_name] = element_data
                        self._save_discovered_pool()
                        
                        # Register with element handler
                        self.element_handler.register_discovered_element(element_name, element_data)
                        
                        # Log discovery
                        print(f"\nDiscovered new element: {element_name}")
                        print(f"Mass: {element_data.get('mass')}")
                        print(f"Compatibility: {compatibility:.3f}")
                        print(f"Properties: {element_data.get('properties', {})}")
                        
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
                
            # Update log
            with open(self.log_file, 'a') as f:
                f.write(f"\n## Collision {i+1}\n")
                f.write(f"- Particle 1: {particle1}\n")
                f.write(f"- Particle 2: {particle2}\n")
                f.write(f"- Compatibility: {compatibility:.3f}\n")
                if result.get('new_element'):
                    f.write(f"- **New Element Discovered**: {new_name}\n")
                f.write(f"- Resonance: {result.get('resonance', 'N/A')}\n")
                
        print(f"\nCompleted {num_collisions} collisions")
        print(f"Total discovered elements: {len(self.discovered_pool)}")

def main():
    collider = QuantumRandomColliderV4()
    
    # Run initial collisions without discovered pool
    collider.run_collision(num_collisions=50, use_discovered=False)
    
    # Run collisions with discovered pool
    collider.run_collision(num_collisions=50, use_discovered=True)
    
    return True

if __name__ == "__main__":
    main()
