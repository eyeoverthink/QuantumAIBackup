"""
QUANTUM RANDOM COLLIDER V6
Enhanced with dynamic φ-harmonic tunneling thresholds
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
from quantum_random_collider_v5 import QuantumRandomColliderV5
from quantum_collision_handler_v2 import QuantumCollisionHandlerV2
from quantum_json_encoder import QuantumJSONEncoder
from quantum_molecular_chains import QuantumMolecularChains
from quantum_element_registry import QuantumElementRegistry
from phi_element_visualizer import PhiElementVisualizer

class QuantumRandomColliderV6(QuantumRandomColliderV5):
    def __init__(self):
        super().__init__()
        
        # Initialize handlers
        self.collision_handler = QuantumCollisionHandlerV2()
        self.visualizer = PhiElementVisualizer()
        
    def run_collision(self, num_collisions=100, use_discovered=True):
        """Run quantum collisions with enhanced visualization"""
        print(f"\nStarting {num_collisions} collisions (using discovered pool: {use_discovered})")
        
        # Track collision statistics
        stats = {
            'total': 0,
            'successful': 0,
            'failed': 0,
            'avg_energy': 0,
            'avg_resonance': 0,
            'avg_tunneling': 0,
            'avg_success_prob': 0
        }
        
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
                stats['total'] += 1
                
                # Update statistics
                collision_data = result['collision_data']
                stats['avg_energy'] += collision_data['energy']
                stats['avg_resonance'] += collision_data['resonance']
                stats['avg_tunneling'] += collision_data['tunneling']
                stats['avg_success_prob'] += collision_data['success_probability']
                
                # Process new element if discovered
                if result['success']:
                    stats['successful'] += 1
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
                        viz_data = f"""
Collision Data:
- Energy: {collision_data['energy']:.3f}
- Resonance: {collision_data['resonance']:.3f}
- Tunneling Probability: {collision_data['tunneling']:.3f}
- Success Probability: {collision_data['success_probability']:.3f}
- Required Threshold: {collision_data['threshold']:.3f}

Element Properties:
- Mass: {element_data['mass']:.3f}
- Atomic Number: {element_data['atomic_number']}
- Binding Energy: {element_data['binding_energy']:.3f}
- Resonance Boost: {element_data['resonance_boost']:.3f}
"""
                        reaction_viz += viz_data
                        
                        with open(viz_file, 'w') as f:
                            f.write(reaction_viz)
                            
                        # Log discovery with quantum properties
                        # Generate ASCII visualization
                        self.visualizer.visualize_element(
                            element_name,
                            element_data['atomic_number'],
                            element_data['mass'],
                            element_data['binding_energy'],
                            element_data['properties']['resonance']
                        )
                        print(f"Stability: {element_data['properties']['stability']:.3f}")
                        print(f"Success Probability: {collision_data['success_probability']:.3f}")
                else:
                    stats['failed'] += 1
                    print(f"\nCollision failed: {result['reason']}")
                    
            except Exception as e:
                print(f"\nWarning: Collision failed between {particle1} and {particle2}: {str(e)}")
                
        # Print final statistics
        if stats['total'] > 0:
            print(f"\nCollision Statistics:")
            print(f"Total Collisions: {stats['total']}")
            print(f"Successful: {stats['successful']} ({stats['successful']/stats['total']*100:.1f}%)")
            print(f"Failed: {stats['failed']} ({stats['failed']/stats['total']*100:.1f}%)")
            print(f"Average Energy: {stats['avg_energy']/stats['total']:.3f}")
            print(f"Average Resonance: {stats['avg_resonance']/stats['total']:.3f}")
            print(f"Average Tunneling: {stats['avg_tunneling']/stats['total']:.3f}")
            print(f"Average Success Probability: {stats['avg_success_prob']/stats['total']:.3f}")
            
        print(f"\nTotal discovered elements: {len(self.discovered_pool)}")
        
def main():
    """Main function"""
    collider = QuantumRandomColliderV6()
    
    # Run collisions with base elements
    collider.run_collision(num_collisions=50, use_discovered=False)
    
    # Run collisions with discovered elements
    collider.run_collision(num_collisions=50, use_discovered=True)
    
if __name__ == "__main__":
    main()
