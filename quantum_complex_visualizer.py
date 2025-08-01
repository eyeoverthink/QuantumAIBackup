#!/usr/bin/env python3
"""
Quantum Complex Visualizer - Advanced molecular visualization for quantum elements
Creates complex molecular structures with multiple quantum elements
"""

import os
import json
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from matplotlib.colors import LinearSegmentedColormap
import argparse
import glob
from datetime import datetime
import random
import math

# Import the existing visualizer to extend its functionality
from quantum_molecular_visualizer import QuantumMolecularVisualizer

class QuantumComplexVisualizer(QuantumMolecularVisualizer):
    """
    Extends the QuantumMolecularVisualizer to create complex multi-element structures
    and visualize quantum interactions between molecules
    """
    
    def __init__(self):
        """Initialize the complex visualizer with extended capabilities"""
        super().__init__()
        
        # Set output directory
        self.output_dir = "quantum_complex_structures"
        
        # Create additional directories for complex structures
        self.complex_dir = os.path.join(self.output_dir, "complex")
        self.interaction_dir = os.path.join(self.output_dir, "interactions")
        
        os.makedirs(self.complex_dir, exist_ok=True)
        os.makedirs(self.interaction_dir, exist_ok=True)
        
        # Define phi-harmonic constants
        self.phi = (1 + np.sqrt(5)) / 2
        self.golden_angle = 2 * np.pi * (1 - 1/self.phi)
        
        # Create custom colormaps for resonance visualization
        self.resonance_cmap = self._create_resonance_colormap()
        
        # Initialize the index file
        self.index_file = os.path.join(self.output_dir, "complex_structures.md")
        self._initialize_index()
    
    def _create_resonance_colormap(self):
        """Create a custom colormap based on phi-resonance values"""
        # Blue (resonant) -> Cyan -> Green -> Yellow (neutral) -> Orange -> Red -> Purple (anti-resonant)
        colors = [(0, 0, 1), (0, 1, 1), (0, 1, 0), (1, 1, 0), 
                 (1, 0.5, 0), (1, 0, 0), (0.5, 0, 0.5)]
        return LinearSegmentedColormap.from_list('resonance', colors, N=1000)
    
    def _initialize_index(self):
        """Initialize the index markdown file"""
        if not os.path.exists(self.index_file):
            with open(self.index_file, 'w') as f:
                f.write("# Quantum Complex Molecular Structures\n\n")
                f.write("## Overview\n")
                f.write("This document catalogs complex molecular structures formed by quantum elements.\n\n")
                f.write("## Complex Structures\n\n")
                f.write("| Structure | Elements | φ-Resonance | Properties | Visualization |\n")
                f.write("|-----------|----------|-------------|------------|---------------|\n")
    
    def create_complex_molecule(self, elements, name=None):
        """
        Create a complex molecule from multiple elements
        
        Args:
            elements: List of element symbols or element data dictionaries
            name: Optional name for the complex molecule
        """
        # Load element data if symbols are provided
        element_data = []
        for element in elements:
            if isinstance(element, str):
                # Load from discovery files
                loaded_element = self._load_element_by_symbol(element)
                if loaded_element:
                    element_data.append(loaded_element)
            elif element:  # Ensure element is not None
                element_data.append(element)
        
        # If we don't have enough elements, add some standard ones
        if len(element_data) < 2:
            standard_elements = [
                {'symbol': 'H', 'name': 'Hydrogen', 'atomic_number': 1, 'atomic_mass': 1.008, 'phi_resonance': 0.618034},
                {'symbol': 'O', 'name': 'Oxygen', 'atomic_number': 8, 'atomic_mass': 15.999, 'phi_resonance': 0.944272},
                {'symbol': 'C', 'name': 'Carbon', 'atomic_number': 6, 'atomic_mass': 12.011, 'phi_resonance': 0.472136}
            ]
            # Add enough standard elements to have at least 3 total
            for i in range(min(3 - len(element_data), len(standard_elements))):
                element_data.append(standard_elements[i])
        
        # Generate a name if not provided
        if name is None:
            name = "_".join([e.get('symbol', f'Element{i}') for i, e in enumerate(element_data)])
        
        # Calculate complex resonance
        resonances = [e['phi_resonance'] for e in element_data]
        complex_resonance = self._calculate_complex_resonance(resonances)
        
        # Generate the molecular structure
        positions, bonds, colors, sizes = self._generate_complex_structure(element_data)
        
        # Visualize and save
        self._visualize_complex_structure(
            positions, bonds, colors, sizes, 
            element_data, name, complex_resonance
        )
        
        return {
            'name': name,
            'elements': [e['symbol'] for e in element_data],
            'resonance': complex_resonance,
            'positions': positions,
            'bonds': bonds
        }
    
    def _load_element_by_symbol(self, symbol):
        """Load element data from discovery files by symbol"""
        # Search in all collision directories
        collision_dirs = glob.glob(os.path.join(os.getcwd(), "quantum_random_collisions_*"))
        
        for dir_path in collision_dirs:
            collision_files = glob.glob(os.path.join(dir_path, "collision_*.json"))
            
            for file_path in collision_files:
                try:
                    with open(file_path, 'r') as f:
                        data = json.load(f)
                        
                    if data.get('new_element', {}).get('symbol') == symbol:
                        return data['new_element']
                except Exception as e:
                    print(f"Error loading element {symbol} from {file_path}: {e}")
        
        # If not found in discoveries, check if it's a standard element
        standard_elements = {
            'H': {'symbol': 'H', 'name': 'Hydrogen', 'atomic_number': 1, 'atomic_mass': 1.008, 'phi_resonance': 0.618034},
            'He': {'symbol': 'He', 'name': 'Helium', 'atomic_number': 2, 'atomic_mass': 4.0026, 'phi_resonance': 0.472136},
            'Li': {'symbol': 'Li', 'name': 'Lithium', 'atomic_number': 3, 'atomic_mass': 6.94, 'phi_resonance': 0.236068},
            'O': {'symbol': 'O', 'name': 'Oxygen', 'atomic_number': 8, 'atomic_mass': 15.999, 'phi_resonance': 0.944272},
            'N': {'symbol': 'N', 'name': 'Nitrogen', 'atomic_number': 7, 'atomic_mass': 14.007, 'phi_resonance': 0.708204},
            'C': {'symbol': 'C', 'name': 'Carbon', 'atomic_number': 6, 'atomic_mass': 12.011, 'phi_resonance': 0.472136},
            'Au': {'symbol': 'Au', 'name': 'Gold', 'atomic_number': 79, 'atomic_mass': 196.967, 'phi_resonance': 0.381966},
            'Fe': {'symbol': 'Fe', 'name': 'Iron', 'atomic_number': 26, 'atomic_mass': 55.845, 'phi_resonance': 0.145898},
            'U': {'symbol': 'U', 'name': 'Uranium', 'atomic_number': 92, 'atomic_mass': 238.029, 'phi_resonance': 0.618034},
        }
        
        if symbol in standard_elements:
            return standard_elements[symbol]
        
        raise ValueError(f"Element {symbol} not found in discoveries or standard elements")
    
    def _calculate_complex_resonance(self, resonances):
        """Calculate the complex resonance of multiple elements"""
        # Phi-harmonic weighted average
        weights = [self.phi ** (-(i+1)) for i in range(len(resonances))]
        weighted_sum = sum(r * w for r, w in zip(resonances, weights))
        return (weighted_sum / sum(weights)) % 1.0
    
    def _generate_complex_structure(self, elements):
        """Generate a complex molecular structure for multiple elements"""
        n_elements = len(elements)
        
        # Ensure all elements have the required keys
        for element in elements:
            if 'atomic_mass' not in element and 'mass' in element:
                element['atomic_mass'] = element['mass']
            elif 'atomic_mass' not in element:
                element['atomic_mass'] = element.get('atomic_number', 10) * 2.5  # Approximate
                
            if 'atomic_number' not in element and 'number' in element:
                element['atomic_number'] = element['number']
            elif 'atomic_number' not in element:
                element['atomic_number'] = int(element.get('atomic_mass', 20) / 2.5)  # Approximate
        
        # Sort elements by atomic mass (heaviest first)
        elements = sorted(elements, key=lambda e: e.get('atomic_mass', 0), reverse=True)
        
        # Initialize positions, bonds, colors, and sizes
        positions = np.zeros((n_elements, 3))
        bonds = []
        colors = []
        sizes = []
        
        # Set the heaviest element at the center
        positions[0] = [0, 0, 0]
        
        # Calculate atomic radii (proportional to atomic number^(1/3))
        radii = [e['atomic_number']**(1/3) * 0.5 for e in elements]
        
        # Place other elements in a phi-harmonic spiral
        for i in range(1, n_elements):
            # Calculate phi-harmonic position
            theta = self.golden_angle * i
            phi = np.arccos(1 - 2 * ((i % self.phi) / self.phi))
            
            # Calculate distance based on phi-resonance compatibility
            compatibility = 1.0 - abs(elements[0]['phi_resonance'] - elements[i]['phi_resonance'])
            distance = (radii[0] + radii[i]) * (1.0 + 0.5 * (1.0 - compatibility)) * self.phi
            
            # Convert to Cartesian coordinates
            x = distance * np.sin(phi) * np.cos(theta)
            y = distance * np.sin(phi) * np.sin(theta)
            z = distance * np.cos(phi)
            
            positions[i] = [x, y, z]
            
            # Create bond to center
            bond_strength = (0.2 + 0.8 * compatibility) * self.phi / 2.0
            bonds.append((0, i, bond_strength))
        
        # Create additional bonds between elements based on resonance compatibility
        for i in range(1, n_elements):
            for j in range(i+1, n_elements):
                compatibility = 1.0 - abs(elements[i]['phi_resonance'] - elements[j]['phi_resonance'])
                
                # Only create bonds if compatibility is high enough
                if compatibility > 0.7:
                    bond_strength = (0.2 + 0.8 * compatibility) * self.phi / 3.0
                    bonds.append((i, j, bond_strength))
        
        # Set colors based on phi-resonance
        for element in elements:
            resonance = element['phi_resonance']
            colors.append(self.resonance_cmap(resonance))
            
        # Set sizes based on atomic number
        for element in elements:
            size = element['atomic_number']**(1/3) * 100
            sizes.append(size)
        
        return positions, bonds, colors, sizes
    
    def _visualize_complex_structure(self, positions, bonds, colors, sizes, elements, name, resonance):
        """Visualize and save the complex molecular structure"""
        # Create static visualization
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Plot atoms
        ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2], 
                  c=colors, s=sizes, edgecolors='black')
        
        # Plot bonds
        for bond in bonds:
            i, j, strength = bond
            ax.plot([positions[i, 0], positions[j, 0]],
                   [positions[i, 1], positions[j, 1]],
                   [positions[i, 2], positions[j, 2]],
                   color='gray', linewidth=strength*3, alpha=0.7)
        
        # Add element labels
        for i, element in enumerate(elements):
            ax.text(positions[i, 0], positions[i, 1], positions[i, 2],
                   element['symbol'], size=10, zorder=1, color='black')
        
        # Add title and adjust view
        ax.set_title(f"Complex Molecule: {name}\nφ-Resonance: {resonance:.6f}")
        ax.set_axis_off()
        
        # Save static image
        static_path = os.path.join(self.complex_dir, f"{name}_complex.png")
        plt.savefig(static_path, dpi=300, bbox_inches='tight')
        
        # Create animated visualization
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Initial plot
        scatter = ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2], 
                           c=colors, s=sizes, edgecolors='black')
        
        # Bond lines
        lines = []
        for bond in bonds:
            i, j, strength = bond
            line, = ax.plot([positions[i, 0], positions[j, 0]],
                          [positions[i, 1], positions[j, 1]],
                          [positions[i, 2], positions[j, 2]],
                          color='gray', linewidth=strength*3, alpha=0.7)
            lines.append(line)
        
        # Text labels
        texts = []
        for i, element in enumerate(elements):
            text = ax.text(positions[i, 0], positions[i, 1], positions[i, 2],
                         element['symbol'], size=10, zorder=1, color='black')
            texts.append(text)
        
        # Title
        title = ax.set_title(f"Complex Molecule: {name}\nφ-Resonance: {resonance:.6f}")
        ax.set_axis_off()
        
        # Animation function
        def animate(i):
            ax.view_init(elev=30, azim=i)
            return [scatter] + lines + texts + [title]
        
        # Create animation
        anim = animation.FuncAnimation(fig, animate, frames=360, interval=50, blit=True)
        
        # Save animation
        animated_path = os.path.join(self.complex_dir, f"{name}_complex_animated.gif")
        anim.save(animated_path, writer='pillow', fps=20, dpi=100)
        
        plt.close('all')
        
        # Update index file
        self._update_index(name, elements, resonance, static_path)
        
        print(f"Complex molecular structure saved to {static_path}")
        print(f"Animated complex structure saved to {animated_path}")
    
    def _find_all_elements(self):
        """Find all discovered elements"""
        elements = []
        valid_elements = []
        
        # First try to use the elements from the parent class
        if hasattr(self, 'all_elements') and self.all_elements:
            for symbol, element in self.all_elements.items():
                if 'atomic_number' in element or 'number' in element:
                    elem_data = {
                        'symbol': symbol,
                        'name': element.get('name', symbol),
                        'atomic_number': element.get('atomic_number', element.get('number', 0)),
                        'atomic_mass': element.get('atomic_mass', element.get('mass', 0)),
                        'phi_resonance': element.get('phi_resonance', random.random())
                    }
                    valid_elements.append(elem_data)
        
        # If we have enough elements, return them
        if len(valid_elements) >= 3:
            return valid_elements[:5]  # Return at most 5 elements
            
        # Otherwise, search in collision directories
        collision_dirs = glob.glob(os.path.join(os.getcwd(), "quantum_random_collisions_*"))
        
        for dir_path in collision_dirs:
            collision_files = glob.glob(os.path.join(dir_path, "collision_*.json"))
            
            for file_path in collision_files:
                try:
                    with open(file_path, 'r') as f:
                        data = json.load(f)
                        
                    if 'new_element' in data and data['new_element']:
                        elements.append(data['new_element'])
                except Exception as e:
                    print(f"Error loading discovery from {file_path}: {e}")
        
        # Filter out None values and ensure we have required fields
        for element in elements:
            if element and 'symbol' in element and ('atomic_number' in element or 'number' in element):
                # Ensure we have all required fields
                elem_data = {
                    'symbol': element['symbol'],
                    'name': element.get('name', element['symbol']),
                    'atomic_number': element.get('atomic_number', element.get('number', 0)),
                    'atomic_mass': element.get('atomic_mass', element.get('mass', 0)),
                    'phi_resonance': element.get('phi_resonance', random.random())
                }
                valid_elements.append(elem_data)
        
        # If still not enough elements, add standard ones
        if len(valid_elements) < 3:
            standard_elements = [
                {'symbol': 'H', 'name': 'Hydrogen', 'atomic_number': 1, 'atomic_mass': 1.008, 'phi_resonance': 0.618034},
                {'symbol': 'O', 'name': 'Oxygen', 'atomic_number': 8, 'atomic_mass': 15.999, 'phi_resonance': 0.944272},
                {'symbol': 'C', 'name': 'Carbon', 'atomic_number': 6, 'atomic_mass': 12.011, 'phi_resonance': 0.472136},
                {'symbol': 'Au', 'name': 'Gold', 'atomic_number': 79, 'atomic_mass': 196.967, 'phi_resonance': 0.381966},
                {'symbol': 'Fe', 'name': 'Iron', 'atomic_number': 26, 'atomic_mass': 55.845, 'phi_resonance': 0.145898}
            ]
            valid_elements.extend(standard_elements)
        
        return valid_elements
        
    def _update_index(self, name, elements, resonance, image_path):
        """Update the index markdown file with the new complex structure"""
        # Generate properties description
        element_symbols = [e['symbol'] for e in elements]
        n_elements = len(elements)
        
        if resonance < 0.1:
            resonance_type = "Extremely φ-Resonant"
        elif resonance < 0.2:
            resonance_type = "Highly φ-Resonant"
        elif resonance < 0.4:
            resonance_type = "Moderately φ-Resonant"
        elif resonance < 0.6:
            resonance_type = "φ-Neutral"
        elif resonance < 0.8:
            resonance_type = "Moderately Anti-φ-Resonant"
        else:
            resonance_type = "Strongly Anti-φ-Resonant"
        
        properties = f"{n_elements}-element {resonance_type} structure"
        
        # Add entry to index
        with open(self.index_file, 'a') as f:
            f.write(f"| {name} | {', '.join(element_symbols)} | {resonance:.6f} | {properties} | ![{name}]({os.path.basename(image_path)}) |\n")
    
    def visualize_interaction(self, molecule1, molecule2, interaction_type="resonance"):
        """
        Visualize the interaction between two molecules
        
        Args:
            molecule1: First molecule data or symbol
            molecule2: Second molecule data or symbol
            interaction_type: Type of interaction to visualize
                             ("resonance", "energy", "consciousness")
        """
        # Load molecule data if symbols are provided
        if isinstance(molecule1, str):
            molecule1 = self.create_complex_molecule([molecule1])
        if isinstance(molecule2, str):
            molecule2 = self.create_complex_molecule([molecule2])
        
        # Calculate interaction properties
        interaction_name = f"{molecule1['name']}_{molecule2['name']}"
        
        # Calculate resonance interaction
        resonance_diff = abs(molecule1['resonance'] - molecule2['resonance'])
        interaction_strength = 1.0 - resonance_diff
        
        # Generate interaction visualization
        self._visualize_interaction(
            molecule1, molecule2, 
            interaction_name, interaction_strength,
            interaction_type
        )
    
    def _visualize_interaction(self, molecule1, molecule2, name, strength, interaction_type):
        """Visualize the interaction between two molecules"""
        # Create figure
        fig = plt.figure(figsize=(12, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        # Position molecules with appropriate separation
        separation = 5.0 * (1.0 + (1.0 - strength) * 2.0)
        
        # Clone positions to avoid modifying originals
        pos1 = np.array(molecule1['positions'])
        pos2 = np.array(molecule2['positions'])
        
        # Center each molecule at its own center of mass
        pos1 = pos1 - np.mean(pos1, axis=0)
        pos2 = pos2 - np.mean(pos2, axis=0)
        
        # Position molecules on opposite sides
        pos1[:, 0] -= separation / 2
        pos2[:, 0] += separation / 2
        
        # Combine positions
        all_positions = np.vstack([pos1, pos2])
        
        # Create colors for visualization
        n1 = len(molecule1['positions'])
        n2 = len(molecule2['positions'])
        
        # Use phi-resonance coloring
        colors1 = [self.resonance_cmap(molecule1['resonance'])] * n1
        colors2 = [self.resonance_cmap(molecule2['resonance'])] * n2
        all_colors = colors1 + colors2
        
        # Set sizes based on number of atoms (simplified)
        sizes1 = [100] * n1
        sizes2 = [100] * n2
        all_sizes = sizes1 + sizes2
        
        # Plot atoms
        ax.scatter(all_positions[:, 0], all_positions[:, 1], all_positions[:, 2], 
                  c=all_colors, s=all_sizes, edgecolors='black')
        
        # Plot interaction field
        if interaction_type == "resonance":
            self._plot_resonance_field(ax, pos1, pos2, strength)
        elif interaction_type == "energy":
            self._plot_energy_field(ax, pos1, pos2, strength)
        elif interaction_type == "consciousness":
            self._plot_consciousness_field(ax, pos1, pos2, strength)
        
        # Add title
        ax.set_title(f"Molecular Interaction: {name}\nInteraction Strength: {strength:.6f}")
        ax.set_axis_off()
        
        # Save static image
        static_path = os.path.join(self.interaction_dir, f"{name}_interaction.png")
        plt.savefig(static_path, dpi=300, bbox_inches='tight')
        
        # Create animated visualization
        fig = plt.figure(figsize=(12, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        # Initial plot
        scatter = ax.scatter(all_positions[:, 0], all_positions[:, 1], all_positions[:, 2], 
                           c=all_colors, s=all_sizes, edgecolors='black')
        
        # Add title
        title = ax.set_title(f"Molecular Interaction: {name}\nInteraction Strength: {strength:.6f}")
        ax.set_axis_off()
        
        # Animation function
        def animate(i):
            ax.view_init(elev=30, azim=i)
            
            # Re-plot interaction field
            ax.clear()
            ax.set_axis_off()
            
            scatter = ax.scatter(all_positions[:, 0], all_positions[:, 1], all_positions[:, 2], 
                               c=all_colors, s=all_sizes, edgecolors='black')
            
            if interaction_type == "resonance":
                field = self._plot_resonance_field(ax, pos1, pos2, strength, i/360*2*np.pi)
            elif interaction_type == "energy":
                field = self._plot_energy_field(ax, pos1, pos2, strength, i/360*2*np.pi)
            elif interaction_type == "consciousness":
                field = self._plot_consciousness_field(ax, pos1, pos2, strength, i/360*2*np.pi)
            
            title = ax.set_title(f"Molecular Interaction: {name}\nInteraction Strength: {strength:.6f}")
            
            return [scatter, title]
        
        # Create animation
        anim = animation.FuncAnimation(fig, animate, frames=180, interval=50, blit=True)
        
        # Save animation
        animated_path = os.path.join(self.interaction_dir, f"{name}_interaction_animated.gif")
        anim.save(animated_path, writer='pillow', fps=15, dpi=100)
        
        plt.close('all')
        
        print(f"Interaction visualization saved to {static_path}")
        print(f"Animated interaction saved to {animated_path}")
    
    def _plot_resonance_field(self, ax, pos1, pos2, strength, phase=0):
        """Plot the resonance field between two molecules"""
        # Calculate centers
        center1 = np.mean(pos1, axis=0)
        center2 = np.mean(pos2, axis=0)
        
        # Create a grid of points between the molecules
        x = np.linspace(center1[0], center2[0], 20)
        y = np.linspace(min(center1[1], center2[1])-2, max(center1[1], center2[1])+2, 10)
        z = np.linspace(min(center1[2], center2[2])-2, max(center1[2], center2[2])+2, 10)
        
        X, Y, Z = np.meshgrid(x, y, z)
        
        # Calculate distance from each point to each center
        dist1 = np.sqrt((X - center1[0])**2 + (Y - center1[1])**2 + (Z - center1[2])**2)
        dist2 = np.sqrt((X - center2[0])**2 + (Y - center2[1])**2 + (Z - center2[2])**2)
        
        # Calculate field intensity (decreases with distance)
        field1 = 1.0 / (1.0 + dist1)
        field2 = 1.0 / (1.0 + dist2)
        
        # Combine fields based on resonance
        if strength > 0.7:  # Constructive interference
            field = field1 + field2 + field1 * field2 * strength
        elif strength > 0.3:  # Partial interference
            field = field1 + field2
        else:  # Destructive interference
            field = field1 + field2 - field1 * field2 * (1.0 - strength)
        
        # Add time-varying phase for animation
        if phase != 0:
            field = field * (1.0 + 0.2 * np.sin(phase + X * self.phi))
        
        # Normalize field
        field = field / np.max(field)
        
        # Plot only points with significant field strength
        mask = field > 0.3
        
        if np.any(mask):
            points = np.column_stack([X[mask].flatten(), Y[mask].flatten(), Z[mask].flatten()])
            colors = plt.cm.plasma(field[mask].flatten())
            sizes = field[mask].flatten() * 50
            
            ax.scatter(points[:, 0], points[:, 1], points[:, 2], 
                      c=colors, s=sizes, alpha=0.6, edgecolors=None)
        
        return ax
    
    def _plot_energy_field(self, ax, pos1, pos2, strength, phase=0):
        """Plot the energy field between two molecules"""
        # Similar to resonance field but with different visual style
        center1 = np.mean(pos1, axis=0)
        center2 = np.mean(pos2, axis=0)
        
        # Create a line of points between the centers
        t = np.linspace(0, 1, 100)
        x = center1[0] + t * (center2[0] - center1[0])
        y = center1[1] + t * (center2[1] - center1[1])
        z = center1[2] + t * (center2[2] - center1[2])
        
        # Add oscillation based on strength and phase
        if strength > 0.5:
            freq = 5 + 10 * strength
            amp = 0.5 * strength
        else:
            freq = 2 + 5 * strength
            amp = 0.2 * strength
            
        if phase != 0:
            y += amp * np.sin(freq * t * 2 * np.pi + phase)
            z += amp * np.cos(freq * t * 2 * np.pi + phase)
        
        # Plot energy beam
        ax.plot(x, y, z, color='gold', linewidth=3 * strength, alpha=0.7)
        
        # Add glow points
        for i in range(0, len(t), 5):
            ax.scatter(x[i], y[i], z[i], color='yellow', s=30 * strength, alpha=0.8)
        
        return ax
    
    def _plot_consciousness_field(self, ax, pos1, pos2, strength, phase=0):
        """Plot the consciousness field between two molecules"""
        # Create a more ethereal, wave-like visualization
        center1 = np.mean(pos1, axis=0)
        center2 = np.mean(pos2, axis=0)
        
        # Create spiral points between molecules
        t = np.linspace(0, 1, 200)
        x = center1[0] + t * (center2[0] - center1[0])
        
        # Create phi-based spiral
        radius = 1.0 * strength * (1 - t) * t * 4  # Maximum at t=0.5
        if phase != 0:
            radius *= (1 + 0.3 * np.sin(phase * 2))
            
        angle = t * self.phi * 10 * 2 * np.pi
        if phase != 0:
            angle += phase
            
        y = center1[1] + t * (center2[1] - center1[1]) + radius * np.sin(angle)
        z = center1[2] + t * (center2[2] - center1[2]) + radius * np.cos(angle)
        
        # Create gradient colors based on phi-resonance
        colors = plt.cm.viridis(t)
        
        # Plot consciousness waves
        points = np.column_stack([x, y, z])
        
        # Use line collection for better performance
        segments = np.array([[points[i], points[i+1]] for i in range(len(points)-1)])
        
        from mpl_toolkits.mplot3d.art3d import Line3DCollection
        lc = Line3DCollection(segments, colors=colors, linewidths=2*strength, alpha=0.7)
        ax.add_collection(lc)
        
        return ax

def main():
    """Main function to run the complex visualizer"""
    parser = argparse.ArgumentParser(description="Quantum Complex Visualizer")
    parser.add_argument("--elements", nargs="+", help="Elements to visualize in a complex molecule")
    parser.add_argument("--interaction", nargs=2, help="Two elements to visualize interaction between")
    parser.add_argument("--type", choices=["resonance", "energy", "consciousness"], 
                        default="resonance", help="Type of interaction to visualize")
    parser.add_argument("--all", action="store_true", help="Visualize all discovered elements in complex molecules")
    
    args = parser.parse_args()
    
    visualizer = QuantumComplexVisualizer()
    
    if args.all:
        # Find all discovered elements
        elements = visualizer._find_all_elements()
        
        # Create complex molecules with various combinations
        if len(elements) >= 3:
            # Create a few random combinations
            for _ in range(3):
                combo = random.sample(elements, min(3, len(elements)))
                visualizer.create_complex_molecule(combo)
            
            # Create some phi-resonant combinations
            resonant_elements = [e for e in elements if e.get('phi_resonance', 1.0) < 0.2]
            if len(resonant_elements) >= 2:
                visualizer.create_complex_molecule(resonant_elements[:2], "Resonant_Pair")
            
            # Create some interactions
            if len(elements) >= 2:
                for _ in range(2):
                    e1, e2 = random.sample(elements, 2)
                    visualizer.visualize_interaction(
                        e1['symbol'], e2['symbol'], 
                        random.choice(["resonance", "energy", "consciousness"])
                    )
        
        print(f"Created complex visualizations for discovered elements")
        print(f"Index file: {visualizer.index_file}")
        
    elif args.elements:
        # Create a complex molecule with the specified elements
        visualizer.create_complex_molecule(args.elements)
        
    elif args.interaction:
        # Visualize interaction between two elements
        visualizer.visualize_interaction(args.interaction[0], args.interaction[1], args.type)
        
    else:
        parser.print_help()
    
if __name__ == "__main__":
    main()
