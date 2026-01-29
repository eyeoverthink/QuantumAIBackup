#!/usr/bin/env python3
'''
Quantum Fractal Node
=================
Implements the fractal node structure for the Quantum Recursive Genesis System.
Each node represents a point in the fractal tree with its own DNA seed and phi-harmonic properties.

By Vaughn Scott (with Cascade Assistant)
'''

import time
import uuid
from typing import Dict, List, Tuple, Any, Optional
import numpy as np

# Import phi-harmonic constants
from quantum_recursive_genesis import PHI, PHI_CONJUGATE

class QuantumFractalNode:
    """Represents a node in the quantum fractal tree"""
    
    def __init__(self, seed, parent=None, depth: int = 0):
        """Initialize a fractal node with a quantum DNA seed"""
        self.seed = seed
        self.parent = parent
        self.children = []
        self.depth = depth
        self.creation_time = time.time()
        self.node_id = str(uuid.uuid4())[:8]
        self.phi_position = self._calculate_phi_position()
        
    def _calculate_phi_position(self) -> Tuple[float, float]:
        """Calculate phi-harmonic position for visualization"""
        if self.parent is None:
            return (0.0, 0.0)  # Root at center
        
        # Calculate position based on parent's position and phi-harmonic spacing
        parent_x, parent_y = self.parent.phi_position
        
        # Use phi and depth to determine distance from parent
        distance = PHI ** (1 / (self.depth + 1))
        
        # Use seed's quantum signature to determine angle
        angle = int(self.seed.quantum_signature[:4], 16) / 0xFFFF * 2 * np.pi
        
        # Calculate new position
        x = parent_x + distance * np.cos(angle)
        y = parent_y + distance * np.sin(angle)
        
        return (x, y)
    
    def add_child(self, seed) -> 'QuantumFractalNode':
        """Add a child node with the given seed"""
        child = QuantumFractalNode(seed, self, self.depth + 1)
        self.children.append(child)
        return child
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert node to dictionary for serialization"""
        return {
            "seed": self.seed.to_dict(),
            "depth": self.depth,
            "creation_time": self.creation_time,
            "node_id": self.node_id,
            "phi_position": self.phi_position,
            "children": [child.to_dict() for child in self.children]
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any], parent=None) -> 'QuantumFractalNode':
        """Create node from dictionary"""
        from quantum_recursive_genesis import QuantumDNASeed
        
        seed = QuantumDNASeed.from_dict(data["seed"])
        node = cls(seed, parent, data["depth"])
        node.creation_time = data["creation_time"]
        node.node_id = data["node_id"]
        node.phi_position = tuple(data["phi_position"])
        
        # Recursively create children
        for child_data in data["children"]:
            child = cls.from_dict(child_data, node)
            node.children.append(child)
            
        return node
