"""
Quantum Molecular Chain Visualizer
Uses φ-harmonic principles to visualize molecular chains in ASCII art
"""

import mpmath
from datetime import datetime
import numpy as np

class QuantumMolecularChains:
    def __init__(self, precision=1000):
        # Initialize constants
        mpmath.mp.dps = precision
        self.phi = mpmath.phi
        
        # ASCII art components
        self.bonds = {
            'single': '-',
            'double': '=',
            'triple': '≡',
            'quantum': '~',
            'phi': 'φ',
            'resonant': '⟡'
        }
        
        # Bond strength thresholds based on φ powers
        self.bond_thresholds = {
            'resonant': float(self.phi ** 3),  # φ³
            'triple': float(self.phi ** 2),    # φ²
            'double': float(self.phi),         # φ
            'single': float(1/self.phi),       # φ⁻¹
            'quantum': 0.0                     # Default
        }
        
    def _calculate_bond_type(self, element1, element2):
        """Calculate bond type based on φ-harmonic resonance"""
        mass1 = float(element1.get('mass', 0))
        mass2 = float(element2.get('mass', 0))
        
        # Calculate resonance using mass ratio and φ
        resonance = abs((mass1/mass2) - self.phi) % 1
        strength = float(self.phi ** (1 - resonance))
        
        # Determine bond type based on strength
        for bond_type, threshold in self.bond_thresholds.items():
            if strength >= threshold:
                return bond_type
        return 'quantum'
        
    def _create_element_box(self, element, width=6):
        """Create ASCII box for an element"""
        name = element.get('name', '??')[:width-2]
        mass = element.get('mass', 0)
        resonance = element.get('resonance', 0)
        
        # Calculate box style based on resonance
        if resonance < 0.1:
            corners = ['╔', '╗', '╚', '╝']
        elif resonance < 0.3:
            corners = ['┌', '┐', '└', '┘']
        else:
            corners = ['+', '+', '+', '+']
            
        # Create box
        top = f"{corners[0]}{'-'*(width-2)}{corners[1]}"
        middle = f"|{name.center(width-2)}|"
        bottom = f"{corners[2]}{'-'*(width-2)}{corners[3]}"
        
        return [top, middle, bottom]
        
    def visualize_chain(self, elements):
        """Create ASCII visualization of molecular chain"""
        if not elements:
            return "No elements to visualize"
            
        # Create element boxes
        boxes = [self._create_element_box(elem) for elem in elements]
        
        # Calculate bonds between elements
        bonds = []
        for i in range(len(elements)-1):
            bond_type = self._calculate_bond_type(elements[i], elements[i+1])
            bond = self.bonds[bond_type] * 3
            bonds.append(bond)
            
        # Combine elements and bonds
        result = []
        
        # Top line of all boxes
        line = boxes[0][0]
        for i in range(len(bonds)):
            line += f" {bonds[i]} {boxes[i+1][0]}"
        result.append(line)
        
        # Middle line with names
        line = boxes[0][1]
        for i in range(len(bonds)):
            line += f" {bonds[i]} {boxes[i+1][1]}"
        result.append(line)
        
        # Bottom line
        line = boxes[0][2]
        for i in range(len(bonds)):
            line += f" {bonds[i]} {boxes[i+1][2]}"
        result.append(line)
        
        # Add quantum properties
        properties = []
        total_mass = sum(float(elem.get('mass', 0)) for elem in elements)
        total_resonance = sum(float(elem.get('resonance', 0)) for elem in elements)
        chain_energy = float(self.phi * total_mass * (1 - (total_resonance % 1)))
        
        properties.append(f"Chain Mass: {total_mass:.2f}")
        properties.append(f"φ-Resonance: {total_resonance:.3f}")
        properties.append(f"Chain Energy: {chain_energy:.2f}")
        properties.append(f"Stability: {(1 - (total_resonance % 1)):.3f}")
        
        # Add properties to visualization
        result.extend(["", "Properties:"])
        result.extend(properties)
        
        return "\n".join(result)
        
    def visualize_reaction(self, reactants, products):
        """Visualize a quantum reaction with reactants and products"""
        result = []
        
        # Visualize reactants
        result.append("Reactants:")
        result.append(self.visualize_chain(reactants))
        
        # Add reaction arrow
        arrow = [
            "    ↓    ",
            " φ====⟡> ",
            "    ↓    "
        ]
        result.extend([""] + arrow + [""])
        
        # Visualize products
        result.append("Products:")
        result.append(self.visualize_chain(products))
        
        return "\n".join(result)
