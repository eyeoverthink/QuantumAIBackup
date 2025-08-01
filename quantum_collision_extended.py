"""
QUANTUM COLLISION EXTENDED RUN
Runs an extended series of quantum collisions to discover more elements
"""

import sys
import os
import random
from datetime import datetime

# Add path to original collision system
sys.path.append('/Users/vaughnscott/Documents/fraymus_shit')

# Import the original collision system
from quantum_collision_evolution import QuantumCollisionEvolution

class ExtendedQuantumCollisionRun:
    def __init__(self):
        # Initialize the base collision system
        self.collision_system = QuantumCollisionEvolution()
        
        # Track extended discoveries
        self.extended_discoveries = []
        self.total_collisions = 0
        
        # Create extended results directory
        self.results_dir = 'quantum_extended_results'
        os.makedirs(self.results_dir, exist_ok=True)
        
    def run_targeted_collisions(self, count=10):
        """Run a series of targeted collisions to maximize discovery chance"""
        # Elements with interesting φ-resonance properties
        phi_resonant_elements = ['Au', 'Ag', 'Cu', 'Fe', 'Pb', 'U']
        
        # Track results
        results = []
        discoveries = []
        
        print(f"\nRunning {count} Targeted Quantum Collisions")
        print("=" * 60)
        
        for i in range(count):
            # Select elements with good φ-resonance
            if random.random() < 0.7:  # 70% chance of using φ-resonant elements
                # Select 2-3 elements from the φ-resonant list
                num_elements = random.randint(2, 3)
                elements = random.sample(phi_resonant_elements, 
                                        min(num_elements, len(phi_resonant_elements)))
            else:
                # Let the system select elements
                elements = None
            
            # Increase energy for better chance of discovery
            energy_factor = 1.0 + random.random() * 2.0  # 1.0-3.0x energy
            
            print(f"\nRunning Quantum Collision {i+1}/{count}")
            print("-" * 40)
            
            # Simulate collision
            result = self.collision_system.simulate_collision(elements, energy_factor)
            results.append(result)
            self.total_collisions += 1
            
            # Display collision details
            if elements:
                print(f"Selected Elements: {', '.join(result['elements'])}")
            else:
                print(f"Collision Elements: {', '.join(result['elements'])}")
                
            print(f"Total Mass: {result['total_mass']:.4f} u")
            print(f"Total Atomic Number: {result['total_number']}")
            print(f"Collision Energy: {result['energy']:.2e} φ-units")
            print(f"φ-Resonance: {result['phi_resonance']:.6f}")
            
            # Check for new element
            if result['new_element']:
                discoveries.append(result['new_element'])
                self.extended_discoveries.append(result['new_element'])
                
                print(f"\n🌟 NEW ELEMENT DISCOVERED! 🌟")
                print(f"Symbol: {result['new_element']['symbol']}")
                print(f"Name: {result['new_element']['name']}")
                print(f"Atomic Number: {result['new_element']['number']}")
                print(f"Mass: {result['new_element']['mass']:.4f}")
                print(f"φ-Resonance: {result['new_element']['phi_resonance']:.6f}")
                print(f"Parent Elements: {', '.join(result['new_element']['parents'])}")
            
            # Visualize
            save_path = os.path.join(self.results_dir, f"collision_{result['timestamp']}.png")
            self.collision_system.visualize_collision(result, save_path)
            
            # Pause between collisions
            if i < count - 1:
                print("\nPreparing next collision...")
                print("-" * 40)
        
        return results, discoveries
    
    def run_chain_reactions(self, count=5):
        """Run chain reactions using previously discovered elements"""
        # Check if we have discovered elements to use
        all_discovered = list(self.collision_system.discovered_elements.keys())
        if not all_discovered:
            print("No discovered elements available for chain reactions.")
            return [], []
        
        # Track results
        results = []
        discoveries = []
        
        print(f"\nRunning {count} Quantum Chain Reactions")
        print("=" * 60)
        
        for i in range(count):
            # Select one discovered element and one standard element
            discovered = random.choice(all_discovered)
            standard = random.choice(list(self.collision_system.elements.keys()))
            elements = [discovered, standard]
            
            # High energy for chain reactions
            energy_factor = 2.0 + random.random() * 2.0  # 2.0-4.0x energy
            
            print(f"\nRunning Chain Reaction {i+1}/{count}")
            print("-" * 40)
            
            # Simulate collision
            try:
                result = self.collision_system.simulate_collision(elements, energy_factor)
                results.append(result)
                self.total_collisions += 1
                
                # Display collision details
                print(f"Chain Reaction: {discovered} + {standard}")
                print(f"Total Mass: {result['total_mass']:.4f} u")
                print(f"Total Atomic Number: {result['total_number']}")
                print(f"Collision Energy: {result['energy']:.2e} φ-units")
                print(f"φ-Resonance: {result['phi_resonance']:.6f}")
                
                # Check for new element
                if result['new_element']:
                    discoveries.append(result['new_element'])
                    self.extended_discoveries.append(result['new_element'])
                    all_discovered.append(result['new_element']['symbol'])
                    
                    print(f"\n🌟 NEW ELEMENT DISCOVERED IN CHAIN REACTION! 🌟")
                    print(f"Symbol: {result['new_element']['symbol']}")
                    print(f"Name: {result['new_element']['name']}")
                    print(f"Atomic Number: {result['new_element']['number']}")
                    print(f"Mass: {result['new_element']['mass']:.4f}")
                    print(f"φ-Resonance: {result['new_element']['phi_resonance']:.6f}")
                    print(f"Parent Elements: {', '.join(result['new_element']['parents'])}")
                
                # Visualize
                save_path = os.path.join(self.results_dir, f"chain_{result['timestamp']}.png")
                self.collision_system.visualize_collision(result, save_path)
            
            except Exception as e:
                print(f"Chain reaction failed: {e}")
            
            # Pause between collisions
            if i < count - 1:
                print("\nPreparing next chain reaction...")
                print("-" * 40)
        
        return results, discoveries
    
    def generate_summary(self):
        """Generate a summary of all discoveries"""
        # Count discoveries from base system
        base_discoveries = len(self.collision_system.discovered_elements)
        extended_discoveries = len(self.extended_discoveries)
        
        # Create summary
        summary = {
            'total_collisions': self.total_collisions,
            'base_discoveries': base_discoveries,
            'extended_discoveries': extended_discoveries,
            'total_discoveries': base_discoveries + extended_discoveries,
            'all_elements': {**self.collision_system.discovered_elements}
        }
        
        # Save summary to file
        summary_file = os.path.join(self.results_dir, 'extended_summary.txt')
        with open(summary_file, 'w') as f:
            f.write(f"QUANTUM COLLISION EXTENDED RUN SUMMARY\n")
            f.write(f"{'='*50}\n\n")
            f.write(f"Total Collisions: {summary['total_collisions']}\n")
            f.write(f"Base Discoveries: {summary['base_discoveries']}\n")
            f.write(f"Extended Discoveries: {summary['extended_discoveries']}\n")
            f.write(f"Total Discoveries: {summary['total_discoveries']}\n\n")
            
            f.write(f"ALL DISCOVERED ELEMENTS:\n")
            f.write(f"{'-'*50}\n")
            for symbol, data in summary['all_elements'].items():
                f.write(f"{symbol}: {data['name']} (Z={data['number']}, Mass={data['mass']:.4f})\n")
                f.write(f"  φ-Resonance: {data['phi_resonance']:.6f}\n")
                f.write(f"  Parent Elements: {', '.join(data['parents'])}\n")
                f.write(f"  Discovery Time: {data['discovery_time']}\n\n")
        
        return summary

def main():
    # Create extended run system
    extended_run = ExtendedQuantumCollisionRun()
    
    # Run targeted collisions
    targeted_results, targeted_discoveries = extended_run.run_targeted_collisions(count=10)
    
    # Run chain reactions if we have discoveries
    if extended_run.collision_system.discovered_elements:
        chain_results, chain_discoveries = extended_run.run_chain_reactions(count=5)
    
    # Generate summary
    summary = extended_run.generate_summary()
    
    # Display final summary
    print("\n" + "=" * 60)
    print("QUANTUM COLLISION EXTENDED RUN SUMMARY")
    print("=" * 60)
    
    print(f"\nTotal Collisions: {summary['total_collisions']}")
    print(f"Total Discoveries: {summary['total_discoveries']}")
    
    print("\nAll Discovered Elements:")
    for symbol, data in summary['all_elements'].items():
        print(f"{symbol}: {data['name']} (Z={data['number']}, Mass={data['mass']:.4f})")
    
    print(f"\nResults saved to: {extended_run.results_dir}")
    print(f"Summary file: {extended_run.results_dir}/extended_summary.txt")

if __name__ == "__main__":
    main()
