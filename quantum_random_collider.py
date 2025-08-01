"""
QUANTUM RANDOM COLLIDER
Runs random quantum collisions and saves each result to a unique file
"""

import os
import sys
import random
import json
from datetime import datetime

# Add path to original collision system
sys.path.append('/Users/vaughnscott/Documents/fraymus_shit')

# Import the original collision system
from quantum_collision_evolution import QuantumCollisionEvolution

class QuantumRandomCollider:
    def __init__(self):
        # Initialize the collision system
        self.collision_system = QuantumCollisionEvolution()
        
        # Create results directory with timestamp to avoid overwriting
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.results_dir = f'quantum_random_collisions_{timestamp}'
        os.makedirs(self.results_dir, exist_ok=True)
        
        # Create log file
        self.log_file = os.path.join(self.results_dir, 'collision_log.md')
        with open(self.log_file, 'w') as f:
            f.write(f"# Quantum Random Collision Log\n\n")
            f.write(f"**Run Time:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"## Collision Results\n\n")
    
    def run_random_collision(self):
        """Run a single random collision with 3 elements"""
        # Get all available elements
        all_elements = list(self.collision_system.elements.keys())
        
        # Include discovered elements if available
        discovered_elements = list(self.collision_system.discovered_elements.keys())
        all_available = all_elements + discovered_elements
        
        # Select 3 random elements (or fewer if not enough available)
        num_elements = min(3, len(all_available))
        selected_elements = random.sample(all_available, num_elements)
        
        # Random energy factor (1.0-3.0x)
        energy_factor = 1.0 + random.random() * 2.0
        
        # Simulate collision
        print(f"\nRunning Random Quantum Collision")
        print(f"Selected Elements: {', '.join(selected_elements)}")
        print(f"Energy Factor: {energy_factor:.2f}x")
        
        try:
            # Simulate collision
            result = self.collision_system.simulate_collision(selected_elements, energy_factor)
            
            # Save result
            self._save_collision_result(result)
            
            return result
        except Exception as e:
            print(f"Collision failed: {e}")
            return None
    
    def _save_collision_result(self, result):
        """Save collision result to unique files"""
        if not result:
            return
        
        # Extract key information
        timestamp = result['timestamp']
        elements = result['elements']
        phi_resonance = result['phi_resonance']
        new_element = result['new_element']
        
        # Create unique filename for this collision
        elements_str = '_'.join(elements)
        base_filename = f"collision_{timestamp}_{elements_str}"
        
        # Save visualization
        viz_path = os.path.join(self.results_dir, f"{base_filename}.png")
        self.collision_system.visualize_collision(result, viz_path)
        
        # Save data as JSON
        data_path = os.path.join(self.results_dir, f"{base_filename}.json")
        with open(data_path, 'w') as f:
            # Create a copy of the result dict that's JSON serializable
            json_result = {}
            for k, v in result.items():
                if k == 'quantum_state':
                    continue  # Skip quantum state arrays
                elif isinstance(v, (int, float, str, bool, list, dict)) or v is None:
                    json_result[k] = v
                elif hasattr(v, 'tolist'):  # Handle numpy arrays
                    json_result[k] = v.tolist()
                else:
                    json_result[k] = str(v)  # Convert other types to string
            
            # Handle new element data
            if 'new_element' in json_result and json_result['new_element']:
                clean_element = {}
                for k, v in json_result['new_element'].items():
                    if k == 'quantum_state':
                        continue
                    elif isinstance(v, (int, float, str, bool, list, dict)) or v is None:
                        clean_element[k] = v
                    elif hasattr(v, 'tolist'):  # Handle numpy arrays
                        clean_element[k] = v.tolist()
                    else:
                        clean_element[k] = str(v)
                json_result['new_element'] = clean_element
            
            json.dump(json_result, f, indent=2)
        
        # Update log file
        with open(self.log_file, 'a') as f:
            f.write(f"### Collision {timestamp}\n\n")
            f.write(f"- **Elements:** {', '.join(elements)}\n")
            f.write(f"- **Total Mass:** {result['total_mass']:.4f} u\n")
            f.write(f"- **Total Atomic Number:** {result['total_number']}\n")
            f.write(f"- **Collision Energy:** {result['energy']:.2e} φ-units\n")
            f.write(f"- **φ-Resonance:** {phi_resonance:.6f}\n")
            
            if new_element:
                f.write(f"\n🌟 **NEW ELEMENT DISCOVERED!** 🌟\n\n")
                f.write(f"- **Symbol:** {new_element['symbol']}\n")
                f.write(f"- **Name:** {new_element['name']}\n")
                f.write(f"- **Atomic Number:** {new_element['number']}\n")
                f.write(f"- **Mass:** {new_element['mass']:.4f}\n")
                f.write(f"- **φ-Resonance:** {new_element['phi_resonance']:.6f}\n")
                f.write(f"- **Parent Elements:** {', '.join(new_element['parents'])}\n")
            
            f.write(f"\n**Files:**\n")
            f.write(f"- [Visualization]({os.path.basename(viz_path)})\n")
            f.write(f"- [Data]({os.path.basename(data_path)})\n\n")
            f.write(f"---\n\n")
        
        # Print result
        print(f"\nCollision Results:")
        print(f"Elements: {', '.join(elements)}")
        print(f"Total Mass: {result['total_mass']:.4f} u")
        print(f"Total Atomic Number: {result['total_number']}")
        print(f"Collision Energy: {result['energy']:.2e} φ-units")
        print(f"φ-Resonance: {phi_resonance:.6f}")
        
        if new_element:
            print(f"\n🌟 NEW ELEMENT DISCOVERED! 🌟")
            print(f"Symbol: {new_element['symbol']}")
            print(f"Name: {new_element['name']}")
            print(f"Atomic Number: {new_element['number']}")
            print(f"Mass: {new_element['mass']:.4f}")
            print(f"φ-Resonance: {new_element['phi_resonance']:.6f}")
            print(f"Parent Elements: {', '.join(new_element['parents'])}")
        
        print(f"\nResults saved to:")
        print(f"- Visualization: {viz_path}")
        print(f"- Data: {data_path}")
        print(f"- Log: {self.log_file}")

def main():
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description='Run random quantum collisions')
    parser.add_argument('--count', type=int, default=1, 
                        help='Number of random collisions to run (default: 1)')
    args = parser.parse_args()
    
    # Create random collider
    collider = QuantumRandomCollider()
    
    # Run specified number of collisions
    print(f"Running {args.count} random quantum collisions...")
    
    for i in range(args.count):
        print(f"\nCollision {i+1}/{args.count}")
        print("-" * 40)
        result = collider.run_random_collision()
    
    # Print summary
    print(f"\nAll collisions complete!")
    print(f"Results saved to: {collider.results_dir}")
    print(f"Log file: {collider.log_file}")

if __name__ == "__main__":
    main()
