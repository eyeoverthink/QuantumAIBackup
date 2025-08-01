"""
QUANTUM MOLECULAR VISUALIZER
Creates 3D molecular visualizations of quantum elements and their compounds
"""

import os
import sys
import json
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LinearSegmentedColormap, Normalize
import matplotlib.animation as animation
from datetime import datetime
import glob
import random

# Define φ (phi) constant
PHI = (1 + np.sqrt(5)) / 2

class QuantumMolecularVisualizer:
    def __init__(self):
        # Load standard elements
        self.standard_elements = self._load_standard_elements()
        
        # Load discovered elements
        self.discovered_elements = self._load_discovered_elements()
        
        # Combined elements
        self.all_elements = {**self.standard_elements, **self.discovered_elements}
        
        # Create output directory
        self.output_dir = 'quantum_molecular_structures'
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Define color maps for φ-resonance
        self.phi_cmap = self._create_phi_colormap()
        
        # Atomic radii (approximate, based on periodic trends)
        self.atomic_radii = {}
        for symbol, element in self.all_elements.items():
            if 'number' in element:
                # Base radius on atomic number with φ-scaling
                base_radius = 0.5 + 0.1 * np.log(1 + element['number'])
                # Apply φ-resonance factor if available
                if 'phi_resonance' in element:
                    # Adjust radius based on resonance (φ-resonant elements are more compact)
                    res_factor = 1.0 - 0.3 * (1.0 - abs(2 * element['phi_resonance'] - 1.0))
                    radius = base_radius * res_factor
                else:
                    radius = base_radius
                self.atomic_radii[symbol] = radius
    
    def _load_standard_elements(self):
        """Load standard elements from ASCII chart"""
        elements = {}
        
        # Try multiple possible file paths
        file_paths = [
            os.path.join(os.path.dirname(__file__), 'Ascii_Element_Chart.txt'),
            '/Users/vaughnscott/Library/Mobile Documents/com~apple~CloudDocs/fraymus_shit/Ascii_Element_Chart.txt',
            '/Users/vaughnscott/Documents/fraymus_shit/Ascii_Element_Chart.txt'
        ]
        
        found_file = False
        for file_path in file_paths:
            try:
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    found_file = True
                    print(f"Successfully loaded element chart from: {file_path}")
                    break
            except FileNotFoundError:
                continue
        
        if not found_file:
            print(f"Error loading standard elements: No element chart file found")
            # Create basic elements as fallback
            return self._create_default_elements()
                
        current_element = None
        for line in lines:
            line = line.strip()
            if line.startswith('Symbol:'):
                symbol = line.split('Symbol:')[1].strip()
                current_element = {'symbol': symbol}
            elif line.startswith('Name:') and current_element:
                current_element['name'] = line.split('Name:')[1].strip()
            elif line.startswith('Atomic Number:') and current_element:
                current_element['number'] = int(line.split('Atomic Number:')[1].strip())
            elif line.startswith('Mass:') and current_element:
                mass_str = line.split('Mass:')[1].strip()
                try:
                    current_element['mass'] = float(mass_str)
                except ValueError:
                    current_element['mass'] = 0.0
            elif line.startswith('Group:') and current_element:
                group_str = line.split('Group:')[1].strip()
                try:
                    current_element['group'] = int(group_str)
                except ValueError:
                    current_element['group'] = 0
            elif line.startswith('Period:') and current_element:
                period_str = line.split('Period:')[1].strip()
                try:
                    current_element['period'] = int(period_str)
                except ValueError:
                    current_element['period'] = 0
            
            # If we have a complete element, add it
            if current_element and 'symbol' in current_element and 'name' in current_element and 'number' in current_element:
                # Calculate φ-resonance for standard elements
                if 'mass' in current_element and current_element['mass'] > 0:
                    phi_res = (PHI * current_element['mass']) % 1
                    current_element['phi_resonance'] = phi_res
                else:
                    current_element['phi_resonance'] = 0.5  # Neutral if no mass
                
                # Add element to dict
                elements[current_element['symbol']] = current_element
                current_element = None
        
        try:
            pass  # Placeholder for try block structure
        except Exception as e:
            print(f"Error loading standard elements: {e}")
            # This exception handler is now properly aligned
        
        return elements
        
    def _create_default_elements(self):
        """Create default elements as fallback when element chart is not found"""
        elements = {}
        
        # Add basic elements with phi-resonance properties
        default_elements = [
            {'symbol': 'H', 'name': 'Hydrogen', 'number': 1, 'mass': 1.008, 'group': 1, 'period': 1},
            {'symbol': 'He', 'name': 'Helium', 'number': 2, 'mass': 4.003, 'group': 18, 'period': 1},
            {'symbol': 'C', 'name': 'Carbon', 'number': 6, 'mass': 12.011, 'group': 14, 'period': 2},
            {'symbol': 'N', 'name': 'Nitrogen', 'number': 7, 'mass': 14.007, 'group': 15, 'period': 2},
            {'symbol': 'O', 'name': 'Oxygen', 'number': 8, 'mass': 15.999, 'group': 16, 'period': 2},
            {'symbol': 'P', 'name': 'Phosphorus', 'number': 15, 'mass': 30.974, 'group': 15, 'period': 3},
            {'symbol': 'S', 'name': 'Sulfur', 'number': 16, 'mass': 32.06, 'group': 16, 'period': 3},
            {'symbol': 'Fe', 'name': 'Iron', 'number': 26, 'mass': 55.845, 'group': 8, 'period': 4},
            {'symbol': 'Au', 'name': 'Gold', 'number': 79, 'mass': 196.967, 'group': 11, 'period': 6},
            {'symbol': 'Φ', 'name': 'Phi-Element', 'number': 137, 'mass': PHI * 100, 'group': 0, 'period': 8}
        ]
        
        # Calculate phi-resonance for each element
        for element in default_elements:
            # Calculate φ-resonance
            if 'mass' in element and element['mass'] > 0:
                phi_res = (PHI * element['mass']) % 1
                element['phi_resonance'] = phi_res
            else:
                element['phi_resonance'] = 0.5  # Neutral if no mass
            
            # Add to elements dictionary
            elements[element['symbol']] = element
            
        print(f"Created {len(elements)} default elements as fallback")
        return elements
    
    def _load_discovered_elements(self):
        """Load discovered elements from quantum discoveries"""
        elements = {}
        
        # Try to load from all discovery directories
        try:
            # Find all quantum discovery directories
            discovery_dirs = glob.glob('/Users/vaughnscott/Documents/fraymus_shit/quantum_random_collisions_*')
            
            for dir_path in discovery_dirs:
                # Find all JSON files in this directory
                json_files = glob.glob(os.path.join(dir_path, '*.json'))
                
                for json_file in json_files:
                    try:
                        with open(json_file, 'r') as f:
                            data = json.load(f)
                            
                        # Check if this collision resulted in a new element
                        if 'new_element' in data and data['new_element']:
                            new_element = data['new_element']
                            
                            # Create element entry
                            if 'symbol' in new_element and 'name' in new_element:
                                symbol = new_element['symbol']
                                
                                # Check for duplicate symbols
                                if symbol in elements:
                                    # Append a number to make it unique
                                    base_symbol = symbol
                                    for i in range(2, 10):
                                        symbol = f"{base_symbol}{i}"
                                        if symbol not in elements:
                                            break
                                
                                # Add to elements dict
                                elements[symbol] = new_element
                                elements[symbol]['is_discovered'] = True
                    except Exception as e:
                        print(f"Error loading discovery from {json_file}: {e}")
            
            # Also check Quantum_Discoveries.txt
            if os.path.exists('/Users/vaughnscott/Documents/fraymus_shit/Quantum_Discoveries.txt'):
                with open('/Users/vaughnscott/Documents/fraymus_shit/Quantum_Discoveries.txt', 'r') as f:
                    content = f.read()
                
                # Split by discovery sections
                sections = content.split('NEW ELEMENT DISCOVERED:')
                
                for section in sections[1:]:  # Skip first empty section
                    lines = section.strip().split('\n')
                    
                    # First line has symbol and name
                    header = lines[0].strip()
                    symbol, name = header.split(' - ')
                    symbol = symbol.strip()
                    name = name.strip()
                    
                    # Skip if already loaded
                    if symbol in elements:
                        continue
                    
                    current_element = {
                        'symbol': symbol,
                        'name': name,
                        'is_discovered': True
                    }
                    
                    # Parse properties
                    for line in lines:
                        line = line.strip()
                        if line.startswith('Atomic Number:'):
                            current_element['number'] = int(line.split(':')[1].strip())
                        elif line.startswith('Mass:'):
                            current_element['mass'] = float(line.split(':')[1].strip())
                        elif line.startswith('Group:'):
                            group_period = line.split(':')[1].strip()
                            if ',' in group_period:
                                group = group_period.split(',')[0].strip()
                                current_element['group'] = int(group)
                        elif line.startswith('Period:'):
                            current_element['period'] = int(line.split(':')[1].strip())
                        elif line.startswith('φ-Resonance:'):
                            current_element['phi_resonance'] = float(line.split(':')[1].strip())
                        elif line.startswith('Parent Elements:'):
                            current_element['parents'] = line.split(':')[1].strip().split(', ')
                        elif line.startswith('Discovery Time:'):
                            current_element['discovery_time'] = line.split(':')[1].strip()
                    
                    # Add to elements dict if complete
                    if 'symbol' in current_element and 'number' in current_element and 'mass' in current_element:
                        elements[current_element['symbol']] = current_element
        
        except Exception as e:
            print(f"Error loading discovered elements: {e}")
        
        return elements
    
    def _create_phi_colormap(self):
        """Create a colormap for φ-resonance visualization"""
        # Define colors for different φ-resonance ranges
        colors = [
            (0.0, 'blue'),      # φ-Resonant (0.0)
            (0.2, 'cyan'),      # Near φ-Resonant
            (0.4, 'green'),     # Approaching φ-Neutral
            (0.5, 'yellow'),    # φ-Neutral (0.5)
            (0.6, 'orange'),    # Approaching Anti-φ-Resonant
            (0.8, 'red'),       # Near Anti-φ-Resonant
            (1.0, 'purple')     # Anti-φ-Resonant (1.0)
        ]
        
        # Create colormap
        cmap_name = 'phi_resonance'
        cm_points = [(x[0], x[1]) for x in colors]
        cmap = LinearSegmentedColormap.from_list(cmap_name, cm_points, N=256)
        
        return cmap
    
    def _calculate_bond_length(self, element1, element2):
        """Calculate bond length between two elements based on φ-harmonic principles"""
        # Get atomic radii
        radius1 = self.atomic_radii.get(element1, 1.0)
        radius2 = self.atomic_radii.get(element2, 1.0)
        
        # Get φ-resonance values
        res1 = self.all_elements.get(element1, {}).get('phi_resonance', 0.5)
        res2 = self.all_elements.get(element2, {}).get('phi_resonance', 0.5)
        
        # Calculate resonance compatibility
        res_diff = abs(res1 - res2)
        compatibility = 1.0 - res_diff
        
        # Base bond length on radii sum
        base_length = radius1 + radius2
        
        # Adjust based on resonance compatibility
        # More compatible elements (similar resonance) have shorter bonds
        bond_length = base_length * (1.0 - 0.3 * compatibility)
        
        # Apply φ-scaling
        bond_length = bond_length * (1.0 + 0.1 * (PHI - 1.0))
        
        return bond_length
    
    def _calculate_bond_strength(self, element1, element2):
        """Calculate bond strength between two elements based on φ-harmonic principles"""
        # Get φ-resonance values
        res1 = self.all_elements.get(element1, {}).get('phi_resonance', 0.5)
        res2 = self.all_elements.get(element2, {}).get('phi_resonance', 0.5)
        
        # Calculate resonance compatibility
        res_diff = abs(res1 - res2)
        compatibility = 1.0 - res_diff
        
        # Bond strength based on compatibility
        # More compatible elements (similar resonance) have stronger bonds
        bond_strength = 0.2 + 0.8 * compatibility
        
        # Apply φ-scaling
        bond_strength = bond_strength * PHI / 2.0
        
        return bond_strength
    
    def _generate_molecular_structure(self, elements):
        """Generate a molecular structure for a compound of the given elements"""
        # Number of atoms for each element (random for now)
        atom_counts = {}
        for element in elements:
            # More atoms for lighter elements
            mass = self.all_elements.get(element, {}).get('mass', 100.0)
            max_count = max(1, int(5 * (1.0 - min(mass / 300.0, 0.9))))
            atom_counts[element] = random.randint(1, max_count)
        
        # Total number of atoms
        total_atoms = sum(atom_counts.values())
        
        # Generate atom positions
        positions = {}
        radii = {}
        colors = {}
        
        # Start with central atom (heaviest element)
        heaviest = max(elements, key=lambda e: self.all_elements.get(e, {}).get('mass', 0.0))
        positions[heaviest] = [(0, 0, 0)]
        radii[heaviest] = [self.atomic_radii.get(heaviest, 1.0)]
        
        # Get φ-resonance color
        res = self.all_elements.get(heaviest, {}).get('phi_resonance', 0.5)
        colors[heaviest] = [self.phi_cmap(res)]
        
        # Remove one from count
        atom_counts[heaviest] -= 1
        
        # Add remaining atoms
        for element in elements:
            if atom_counts[element] <= 0:
                continue
                
            # Get element properties
            radius = self.atomic_radii.get(element, 1.0)
            res = self.all_elements.get(element, {}).get('phi_resonance', 0.5)
            color = self.phi_cmap(res)
            
            # Initialize if needed
            if element not in positions:
                positions[element] = []
                radii[element] = []
                colors[element] = []
            
            # Add atoms
            for i in range(atom_counts[element]):
                # Calculate position based on φ-harmonic principles
                # Use golden angle in 3D space for distribution
                golden_angle = 2.0 * np.pi * (1.0 - 1.0/PHI)
                
                # Distance from center based on bond length with heaviest element
                bond_length = self._calculate_bond_length(heaviest, element)
                
                # Adjust for atom index
                angle1 = golden_angle * i
                angle2 = np.arccos(1.0 - 2.0 * ((i % 5) / 5.0))
                
                # Calculate position
                x = bond_length * np.sin(angle2) * np.cos(angle1)
                y = bond_length * np.sin(angle2) * np.sin(angle1)
                z = bond_length * np.cos(angle2)
                
                # Add some randomness for more natural structure
                jitter = 0.1 * bond_length
                x += np.random.uniform(-jitter, jitter)
                y += np.random.uniform(-jitter, jitter)
                z += np.random.uniform(-jitter, jitter)
                
                positions[element].append((x, y, z))
                radii[element].append(radius)
                colors[element].append(color)
        
        # Calculate bonds
        bonds = []
        bond_colors = []
        
        # For each pair of elements
        for i, elem1 in enumerate(elements):
            for j, elem2 in enumerate(elements):
                if i >= j:  # Avoid duplicate pairs
                    continue
                
                # Calculate max bond length
                max_bond_length = 1.5 * self._calculate_bond_length(elem1, elem2)
                
                # Check each atom pair
                for pos1_idx, pos1 in enumerate(positions.get(elem1, [])):
                    for pos2_idx, pos2 in enumerate(positions.get(elem2, [])):
                        # Calculate distance
                        dx = pos2[0] - pos1[0]
                        dy = pos2[1] - pos1[1]
                        dz = pos2[2] - pos1[2]
                        distance = np.sqrt(dx*dx + dy*dy + dz*dz)
                        
                        # If close enough, create a bond
                        if distance <= max_bond_length:
                            bonds.append((pos1, pos2))
                            
                            # Bond color based on bond strength
                            strength = self._calculate_bond_strength(elem1, elem2)
                            bond_colors.append((strength, strength, strength, 0.7))
        
        return {
            'positions': positions,
            'radii': radii,
            'colors': colors,
            'bonds': bonds,
            'bond_colors': bond_colors,
            'atom_counts': atom_counts
        }
    
    def visualize_molecule(self, elements, save_path=None, show_plot=False):
        """Visualize a molecule made of the given elements"""
        # Generate molecular structure
        structure = self._generate_molecular_structure(elements)
        
        # Create figure
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Set background color
        ax.set_facecolor('#f0f0f0')
        
        # Plot atoms
        for element in elements:
            if element not in structure['positions']:
                continue
                
            # Get positions, radii, and colors
            pos = structure['positions'][element]
            rad = structure['radii'][element]
            col = structure['colors'][element]
            
            # Plot each atom
            for i in range(len(pos)):
                # Create sphere
                u = np.linspace(0, 2 * np.pi, 20)
                v = np.linspace(0, np.pi, 20)
                
                x = pos[i][0] + rad[i] * np.outer(np.cos(u), np.sin(v))
                y = pos[i][1] + rad[i] * np.outer(np.sin(u), np.sin(v))
                z = pos[i][2] + rad[i] * np.outer(np.ones(np.size(u)), np.cos(v))
                
                # Plot surface
                ax.plot_surface(x, y, z, color=col[i], alpha=0.8)
                
                # Add element label
                ax.text(pos[i][0], pos[i][1], pos[i][2], element, 
                       color='black', fontsize=10, ha='center', va='center')
        
        # Plot bonds
        for i, bond in enumerate(structure['bonds']):
            # Get start and end points
            start = bond[0]
            end = bond[1]
            
            # Plot line
            ax.plot([start[0], end[0]], [start[1], end[1]], [start[2], end[2]], 
                   color=structure['bond_colors'][i], linewidth=2)
        
        # Set axis labels
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        
        # Set axis limits
        max_range = 0
        for element in elements:
            if element not in structure['positions']:
                continue
                
            for pos in structure['positions'][element]:
                max_range = max(max_range, abs(pos[0]), abs(pos[1]), abs(pos[2]))
        
        ax.set_xlim(-max_range*1.2, max_range*1.2)
        ax.set_ylim(-max_range*1.2, max_range*1.2)
        ax.set_zlim(-max_range*1.2, max_range*1.2)
        
        # Create formula string
        formula = ""
        for element in elements:
            count = structure['atom_counts'].get(element, 0) + (1 if element == max(elements, key=lambda e: self.all_elements.get(e, {}).get('mass', 0.0)) else 0)
            if count > 0:
                formula += element
                if count > 1:
                    formula += str(count)
        
        # Add title
        ax.set_title(f'Molecular Structure: {formula}', fontsize=16)
        
        # Add legend for φ-resonance
        ax.text2D(0.05, 0.95, "φ-Resonance:", transform=ax.transAxes, fontsize=10)
        for i, (res, color) in enumerate([
            ("φ-Resonant (< 0.1)", 'blue'),
            ("φ-Neutral (≈ 0.5)", 'yellow'),
            ("Anti-φ-Resonant (> 0.9)", 'purple')
        ]):
            ax.text2D(0.05, 0.92 - i*0.03, res, transform=ax.transAxes, 
                     color=color, fontsize=8)
        
        # Save if path provided
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Molecular structure saved to {save_path}")
        
        # Show if requested
        if show_plot:
            plt.show()
        else:
            plt.close(fig)
        
        return formula
    
    def create_animated_molecule(self, elements, save_path=None):
        """Create an animated rotating view of the molecule"""
        # Generate molecular structure
        structure = self._generate_molecular_structure(elements)
        
        # Create figure
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Set background color
        ax.set_facecolor('#f0f0f0')
        
        # Plot atoms
        atom_plots = []
        for element in elements:
            if element not in structure['positions']:
                continue
                
            # Get positions, radii, and colors
            pos = structure['positions'][element]
            rad = structure['radii'][element]
            col = structure['colors'][element]
            
            # Plot each atom
            for i in range(len(pos)):
                # Create sphere
                u = np.linspace(0, 2 * np.pi, 15)
                v = np.linspace(0, np.pi, 15)
                
                x = pos[i][0] + rad[i] * np.outer(np.cos(u), np.sin(v))
                y = pos[i][1] + rad[i] * np.outer(np.sin(u), np.sin(v))
                z = pos[i][2] + rad[i] * np.outer(np.ones(np.size(u)), np.cos(v))
                
                # Plot surface
                atom = ax.plot_surface(x, y, z, color=col[i], alpha=0.8)
                atom_plots.append((atom, pos[i], element))
        
        # Plot bonds
        bond_lines = []
        for i, bond in enumerate(structure['bonds']):
            # Get start and end points
            start = bond[0]
            end = bond[1]
            
            # Plot line
            line, = ax.plot([start[0], end[0]], [start[1], end[1]], [start[2], end[2]], 
                          color=structure['bond_colors'][i], linewidth=2)
            bond_lines.append((line, start, end))
        
        # Set axis labels
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        
        # Set axis limits
        max_range = 0
        for element in elements:
            if element not in structure['positions']:
                continue
                
            for pos in structure['positions'][element]:
                max_range = max(max_range, abs(pos[0]), abs(pos[1]), abs(pos[2]))
        
        ax.set_xlim(-max_range*1.2, max_range*1.2)
        ax.set_ylim(-max_range*1.2, max_range*1.2)
        ax.set_zlim(-max_range*1.2, max_range*1.2)
        
        # Create formula string
        formula = ""
        for element in elements:
            count = structure['atom_counts'].get(element, 0) + (1 if element == max(elements, key=lambda e: self.all_elements.get(e, {}).get('mass', 0.0)) else 0)
            if count > 0:
                formula += element
                if count > 1:
                    formula += str(count)
        
        # Add title
        ax.set_title(f'Molecular Structure: {formula}', fontsize=16)
        
        # Add legend for φ-resonance
        ax.text2D(0.05, 0.95, "φ-Resonance:", transform=ax.transAxes, fontsize=10)
        for i, (res, color) in enumerate([
            ("φ-Resonant (< 0.1)", 'blue'),
            ("φ-Neutral (≈ 0.5)", 'yellow'),
            ("Anti-φ-Resonant (> 0.9)", 'purple')
        ]):
            ax.text2D(0.05, 0.92 - i*0.03, res, transform=ax.transAxes, 
                     color=color, fontsize=8)
        
        # Animation function
        def animate(i):
            # Rotate view
            ax.view_init(elev=30, azim=i)
            return []
        
        # Create animation
        anim = animation.FuncAnimation(fig, animate, frames=360, interval=50, blit=True)
        
        # Save if path provided
        if save_path:
            anim.save(save_path, writer='pillow', fps=30, dpi=100)
            print(f"Animated molecular structure saved to {save_path}")
            plt.close(fig)
        else:
            plt.show()
        
        return formula
    
    def visualize_discovered_molecules(self):
        """Visualize molecules for all discovered elements"""
        # Get all discovered elements
        discovered = list(self.discovered_elements.keys())
        
        # Create directory for molecule visualizations
        molecules_dir = os.path.join(self.output_dir, 'molecules')
        os.makedirs(molecules_dir, exist_ok=True)
        
        # Create molecules
        results = []
        
        # For each discovered element
        for element in discovered:
            # Get parent elements
            parents = self.discovered_elements[element].get('parents', [])
            
            # If we have parent elements, create molecule
            if parents:
                # Add the element itself to the mix
                elements = parents + [element]
                
                # Create static visualization
                static_path = os.path.join(molecules_dir, f"{element}_molecule.png")
                formula = self.visualize_molecule(elements, static_path)
                
                # Create animated visualization
                animated_path = os.path.join(molecules_dir, f"{element}_molecule_animated.gif")
                self.create_animated_molecule(elements, animated_path)
                
                # Add to results
                results.append({
                    'element': element,
                    'formula': formula,
                    'static_path': static_path,
                    'animated_path': animated_path
                })
        
        # Create index file
        index_path = os.path.join(self.output_dir, 'molecular_structures.md')
        with open(index_path, 'w') as f:
            f.write("# Quantum Molecular Structures\n\n")
            f.write("This document catalogs the molecular structures of discovered quantum elements.\n\n")
            
            for result in results:
                f.write(f"## {result['element']} - {self.discovered_elements[result['element']]['name']}\n\n")
                f.write(f"**Formula:** {result['formula']}\n\n")
                f.write(f"**φ-Resonance:** {self.discovered_elements[result['element']].get('phi_resonance', 'Unknown'):.6f}\n\n")
                f.write(f"**Parent Elements:** {', '.join(self.discovered_elements[result['element']].get('parents', []))}\n\n")
                f.write(f"**Static Structure:**\n\n")
                f.write(f"![{result['element']} Molecular Structure]({os.path.relpath(result['static_path'], self.output_dir)})\n\n")
                f.write(f"**Animated Structure:**\n\n")
                f.write(f"![{result['element']} Animated Structure]({os.path.relpath(result['animated_path'], self.output_dir)})\n\n")
                f.write("---\n\n")
        
        return index_path, results
    
    def visualize_custom_molecule(self, elements):
        """Visualize a custom molecule with the given elements"""
        # Create directory for custom molecules
        custom_dir = os.path.join(self.output_dir, 'custom')
        os.makedirs(custom_dir, exist_ok=True)
        
        # Create timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Create element string
        element_str = '_'.join(elements)
        
        # Create static visualization
        static_path = os.path.join(custom_dir, f"molecule_{timestamp}_{element_str}.png")
        formula = self.visualize_molecule(elements, static_path, show_plot=True)
        
        # Create animated visualization
        animated_path = os.path.join(custom_dir, f"molecule_{timestamp}_{element_str}_animated.gif")
        self.create_animated_molecule(elements, animated_path)
        
        return static_path, animated_path, formula

def main():
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description='Visualize quantum molecular structures')
    parser.add_argument('--all', action='store_true', help='Visualize all discovered molecules')
    parser.add_argument('--elements', type=str, nargs='+', help='Elements to visualize as a molecule')
    args = parser.parse_args()
    
    # Create visualizer
    visualizer = QuantumMolecularVisualizer()
    
    if args.all:
        # Visualize all discovered molecules
        index_path, results = visualizer.visualize_discovered_molecules()
        print(f"\nAll molecular structures visualized!")
        print(f"Index file: {index_path}")
        print(f"Total molecules: {len(results)}")
    elif args.elements:
        # Visualize custom molecule
        static_path, animated_path, formula = visualizer.visualize_custom_molecule(args.elements)
        print(f"\nCustom molecular structure visualized!")
        print(f"Formula: {formula}")
        print(f"Static image: {static_path}")
        print(f"Animated image: {animated_path}")
    else:
        # Default to all discovered
        index_path, results = visualizer.visualize_discovered_molecules()
        print(f"\nAll molecular structures visualized!")
        print(f"Index file: {index_path}")
        print(f"Total molecules: {len(results)}")

if __name__ == "__main__":
    main()
