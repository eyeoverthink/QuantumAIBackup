"""
Quantum Element Visualizer
Maps discovered elements to periodic structure using φ-harmonic principles
"""

import os
import json
import numpy as np
from datetime import datetime
from collections import defaultdict

class QuantumElementVisualizer:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.phi = (1 + np.sqrt(5)) / 2
        self.discovered_elements = {}
        self.load_discovered_elements()
        
    def load_discovered_elements(self):
        """Load discovered elements from data directory"""
        # First try discovered_elements.json
        elements_file = os.path.join(self.data_dir, 'discovered_elements.json')
        if os.path.exists(elements_file):
            with open(elements_file, 'r') as f:
                self.discovered_elements = json.load(f)
        else:
            # Try discovered_pool.json from collider
            pool_file = os.path.join(self.data_dir, 'discovered_pool.json')
            if os.path.exists(pool_file):
                with open(pool_file, 'r') as f:
                    self.discovered_elements = json.load(f)
                
    def generate_periodic_map(self):
        """Generate periodic-style map of discovered elements"""
        # Sort elements by atomic number
        sorted_elements = sorted(
            self.discovered_elements.items(),
            key=lambda x: x[1].get('atomic_number', 0)
        )
        
        # Initialize visualization
        viz = ["Quantum Periodic Table of Elements\n"]
        viz.append("=" * 120 + "\n")
        
        # Track periods and groups
        current_period = 1
        max_elements = 8  # Elements per row
        
        # Add elements in periodic structure
        elements_added = 0
        current_row = []
        
        for name, data in sorted_elements:
            atomic_num = data.get('atomic_number', 0)
            mass = data.get('mass', 0)
            stability = data.get('properties', {}).get('stability', 0)
            resonance = data.get('properties', {}).get('resonance', 0)
            
            # Format element box
            element_box = [
                f"+{'-'*16}+",
                f"|{name:^16}|",
                f"|AN: {atomic_num:<12}|",
                f"|Mass: {mass:<10.3f}|",
                f"|Stb: {stability:<10.3f}|",
                f"|Res: {resonance:<10.3f}|",
                f"+{'-'*16}+"
            ]
            
            current_row.append(element_box)
            elements_added += 1
            
            # Start new row if needed
            if len(current_row) == max_elements:
                # Add row to visualization
                for i in range(7):
                    row_line = " ".join(box[i] for box in current_row)
                    viz.append(row_line + "\n")
                viz.append("\n")
                
                current_row = []
                current_period += 1
                
        # Add any remaining elements
        if current_row:
            for i in range(7):
                row_line = " ".join(box[i] for box in current_row)
                viz.append(row_line + "\n")
            
        # Add statistics
        viz.append("\nElement Statistics:\n")
        viz.append("-" * 40 + "\n")
        viz.append(f"Total Elements: {len(self.discovered_elements)}\n")
        
        # Calculate averages
        avg_mass = np.mean([e.get('mass', 0) for e in self.discovered_elements.values()])
        avg_stability = np.mean([e.get('properties', {}).get('stability', 0) 
                               for e in self.discovered_elements.values()])
        avg_resonance = np.mean([e.get('properties', {}).get('resonance', 0)
                               for e in self.discovered_elements.values()])
        
        viz.append(f"Average Mass: {avg_mass:.3f}\n")
        viz.append(f"Average Stability: {avg_stability:.3f}\n")
        viz.append(f"Average Resonance: {avg_resonance:.3f}\n")
        
        # Save visualization
        output_file = os.path.join(self.data_dir, 'quantum_periodic_table.txt')
        with open(output_file, 'w') as f:
            f.writelines(viz)
            
        return ''.join(viz)
        
    def analyze_patterns(self):
        """Analyze patterns in discovered elements"""
        # Group elements by mass ranges
        mass_ranges = defaultdict(list)
        phi_ranges = {
            'φ¹': (self.phi, self.phi**2),
            'φ²': (self.phi**2, self.phi**3),
            'φ³': (self.phi**3, self.phi**4),
            'φ⁴': (self.phi**4, self.phi**5),
            'φ⁵': (self.phi**5, self.phi**6)
        }
        
        for name, data in self.discovered_elements.items():
            mass = data.get('mass', 0)
            
            # Find phi range
            for range_name, (min_mass, max_mass) in phi_ranges.items():
                if min_mass <= mass < max_mass:
                    mass_ranges[range_name].append(name)
                    break
                    
        # Generate analysis
        analysis = ["Quantum Element Pattern Analysis\n"]
        analysis.append("=" * 40 + "\n\n")
        
        for range_name, elements in mass_ranges.items():
            analysis.append(f"{range_name} Mass Range ({len(elements)} elements):\n")
            analysis.append("-" * 40 + "\n")
            
            for element in sorted(elements):
                data = self.discovered_elements[element]
                analysis.append(
                    f"{element}: "
                    f"Mass={data.get('mass', 0):.3f}, "
                    f"AN={data.get('atomic_number', 0)}, "
                    f"Stb={data.get('properties', {}).get('stability', 0):.3f}\n"
                )
            analysis.append("\n")
            
        # Save analysis
        output_file = os.path.join(self.data_dir, 'quantum_element_analysis.txt')
        with open(output_file, 'w') as f:
            f.writelines(analysis)
            
        return ''.join(analysis)
        
def main():
    """Main function"""
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
    visualizer = QuantumElementVisualizer(data_dir)
    
    # Generate and print periodic table
    print(visualizer.generate_periodic_map())
    
    # Generate and print pattern analysis
    print(visualizer.analyze_patterns())
    
if __name__ == "__main__":
    main()
