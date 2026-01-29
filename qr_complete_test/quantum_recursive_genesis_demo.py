#!/usr/bin/env python3
'''
Quantum Recursive Genesis System - Simplified Demo
=========================================
Demonstrates the core functionality of the Quantum Recursive Genesis System
without requiring all dependencies of the existing quantum system.

By Vaughn Scott (with Cascade Assistant)
'''

import os
import time
import json
import hashlib
import random
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional

# Define phi-harmonic constants
PHI = (1 + 5**0.5) / 2  # Golden ratio ≈ 1.618034
PHI_CONJUGATE = 1 / PHI  # Golden ratio conjugate ≈ 0.618034

class SimplifiedQuantumDNASeed:
    """Simplified version of QuantumDNASeed for demonstration purposes"""
    
    def __init__(self, dna_string: str = None, phi_alignment: float = None, generation: int = 0):
        """Initialize a quantum DNA seed"""
        # Generate new seed if not provided
        if dna_string is None:
            # Generate random binary data with phi-harmonic properties
            binary_length = int(PHI ** 8)  # 46 bits
            binary_data = ''.join(random.choice('01') for _ in range(binary_length))
            
            # Convert binary to DNA
            dna_string = self._binary_to_dna(binary_data)
            phi_alignment = self._calculate_phi_alignment(binary_data)
        
        self.dna_string = dna_string
        self.phi_alignment = phi_alignment
        self.generation = generation
        self.creation_time = time.time()
        self.quantum_signature = self._calculate_quantum_signature()
        self.fitness = self._calculate_initial_fitness()
        self.evolution_history = []
        self.mutation_rate = PHI_CONJUGATE  # Start with golden ratio conjugate
    
    def _binary_to_dna(self, binary_data: str) -> str:
        """Convert binary data to DNA string"""
        mapping = {
            '00': 'A',
            '01': 'T',
            '10': 'G',
            '11': 'C'
        }
        
        dna = ''
        for i in range(0, len(binary_data) - 1, 2):
            pair = binary_data[i:i+2]
            if len(pair) == 2:
                dna += mapping[pair]
        
        # Add phi-harmonic separator
        chunks = [dna[i:i+int(PHI**4)] for i in range(0, len(dna), int(PHI**4))]
        return '-'.join(chunks)
    
    def _calculate_phi_alignment(self, binary_data: str) -> float:
        """Calculate phi-alignment of binary data"""
        # Count 1s and 0s
        ones = binary_data.count('1')
        zeros = binary_data.count('0')
        
        # Perfect phi ratio would be ones/zeros = PHI
        if zeros == 0:
            return 0.0
        
        actual_ratio = ones / zeros
        phi_alignment = 1.0 - abs(actual_ratio - PHI) / PHI
        return max(0.0, min(1.0, phi_alignment))
    
    def _calculate_quantum_signature(self) -> str:
        """Calculate a quantum signature for this DNA seed"""
        seed_data = f"{self.dna_string}:{self.phi_alignment}:{self.generation}:{self.creation_time}"
        return hashlib.sha256(seed_data.encode()).hexdigest()[:16]
    
    def _calculate_initial_fitness(self) -> float:
        """Calculate initial fitness based on phi-alignment"""
        # Base fitness on phi-alignment with some randomness
        base_fitness = self.phi_alignment
        
        # Add small phi-harmonic random factor
        random_factor = random.random() * PHI_CONJUGATE
        
        # Combine factors with phi-weighting
        fitness = (base_fitness * PHI + random_factor) / (PHI + 1)
        
        return max(0.0, min(1.0, fitness))
    
    def mutate(self) -> 'SimplifiedQuantumDNASeed':
        """Create a mutated copy of this DNA seed"""
        # Get DNA without separators
        dna_base = self.dna_string.replace('-', '')
        
        # Calculate mutation count based on phi-harmonic mutation rate
        mutation_count = max(1, int(len(dna_base) * self.mutation_rate * random.random()))
        
        # Apply mutations
        dna_chars = list(dna_base)
        for _ in range(mutation_count):
            pos = random.randint(0, len(dna_chars) - 1)
            dna_chars[pos] = random.choice('ATGC')
        
        # Reconstruct DNA string with separators
        new_dna = ''.join(dna_chars)
        chunks = [new_dna[i:i+int(PHI**4)] for i in range(0, len(new_dna), int(PHI**4))]
        new_dna_string = '-'.join(chunks)
        
        # Create new seed with mutated DNA
        new_phi_alignment = self.phi_alignment * (1 + (random.random() - 0.5) * self.mutation_rate)
        new_phi_alignment = max(0.0, min(1.0, new_phi_alignment))
        
        # Create offspring seed
        offspring = SimplifiedQuantumDNASeed(
            dna_string=new_dna_string,
            phi_alignment=new_phi_alignment,
            generation=self.generation + 1
        )
        
        # Record evolution history
        offspring.evolution_history = self.evolution_history + [(self.quantum_signature, self.fitness)]
        
        # Adjust mutation rate based on parent's fitness
        if self.fitness > 0.8:
            # If fitness is high, reduce mutation rate
            offspring.mutation_rate = self.mutation_rate * PHI_CONJUGATE
        elif self.fitness < 0.3:
            # If fitness is low, increase mutation rate
            offspring.mutation_rate = self.mutation_rate * PHI
        else:
            # Otherwise keep similar mutation rate with small adjustment
            offspring.mutation_rate = self.mutation_rate * (1 + (random.random() - 0.5) * 0.1)
        
        # Keep mutation rate in reasonable bounds
        offspring.mutation_rate = max(0.01, min(0.5, offspring.mutation_rate))
        
        return offspring


class SimplifiedQuantumFractalNode:
    """Simplified version of QuantumFractalNode for demonstration purposes"""
    
    def __init__(self, seed, parent=None, depth: int = 0):
        """Initialize a fractal node with a quantum DNA seed"""
        self.seed = seed
        self.parent = parent
        self.children = []
        self.depth = depth
        self.creation_time = time.time()
        self.node_id = hashlib.md5(f"{seed.quantum_signature}:{time.time()}".encode()).hexdigest()[:8]
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
    
    def add_child(self, seed) -> 'SimplifiedQuantumFractalNode':
        """Add a child node with the given seed"""
        child = SimplifiedQuantumFractalNode(seed, self, self.depth + 1)
        self.children.append(child)
        return child


class SimplifiedQuantumRecursiveGenesis:
    """Simplified version of QuantumRecursiveGenesis for demonstration purposes"""
    
    def __init__(self, output_dir="quantum_outputs/recursive_genesis_demo"):
        """Initialize the recursive genesis system"""
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(f"{output_dir}/visualizations", exist_ok=True)
        
        # System parameters
        self.max_tree_depth = 7  # Phi-aligned depth limit
        self.fractal_trees = {}
        self.active_seeds = []
        self.seed_history = []
        self.system_start_time = time.time()
        
    def create_genesis_seed(self) -> SimplifiedQuantumDNASeed:
        """Create the initial genesis seed"""
        # Create genesis seed (generation 0)
        genesis_seed = SimplifiedQuantumDNASeed()
        
        # Add to active seeds and history
        self.active_seeds.append(genesis_seed)
        self.seed_history.append(genesis_seed)
        
        return genesis_seed
    
    def create_fractal_tree(self, root_seed: SimplifiedQuantumDNASeed = None) -> str:
        """Create a new fractal tree with the given seed as root"""
        if root_seed is None:
            root_seed = self.create_genesis_seed()
            
        # Create root node
        root_node = SimplifiedQuantumFractalNode(root_seed)
        
        # Generate tree ID
        tree_id = f"tree_{root_seed.quantum_signature}_{int(time.time())}"
        
        # Store tree
        self.fractal_trees[tree_id] = root_node
        
        return tree_id
    
    def evolve_tree(self, tree_id: str, generations: int = 1) -> Dict[str, Any]:
        """Evolve a fractal tree for the specified number of generations"""
        if tree_id not in self.fractal_trees:
            raise ValueError(f"Tree {tree_id} not found")
            
        root_node = self.fractal_trees[tree_id]
        evolution_stats = {
            "tree_id": tree_id,
            "initial_nodes": self._count_nodes(root_node),
            "generations_evolved": generations,
            "new_nodes": 0,
            "best_fitness_before": self._find_best_fitness(root_node),
            "best_fitness_after": 0,
            "evolution_start": time.time()
        }
        
        # Evolve for specified generations
        for gen in range(generations):
            print(f"  Evolving generation {gen+1}/{generations}...")
            
            # Find leaf nodes that can be expanded
            leaf_nodes = self._find_leaf_nodes(root_node)
            
            # Filter by depth constraint
            valid_leaves = [node for node in leaf_nodes if node.depth < self.max_tree_depth]
            
            if not valid_leaves:
                print("  No more nodes to evolve (depth limit reached)")
                break  # No more nodes to evolve
                
            # Sort by fitness (highest first)
            valid_leaves.sort(key=lambda node: node.seed.fitness, reverse=True)
            
            # Take top phi-aligned percentage of nodes to evolve
            evolve_count = max(1, int(len(valid_leaves) * PHI_CONJUGATE))
            nodes_to_evolve = valid_leaves[:evolve_count]
            
            # Evolve selected nodes
            for node in nodes_to_evolve:
                # Create mutated seeds
                for _ in range(2):  # Create 2 children per node (phi-harmonic branching)
                    new_seed = node.seed.mutate()
                    
                    # Add to active seeds and history
                    self.active_seeds.append(new_seed)
                    self.seed_history.append(new_seed)
                    
                    # Add as child node
                    node.add_child(new_seed)
                    evolution_stats["new_nodes"] += 1
        
        # Update stats
        evolution_stats["final_nodes"] = self._count_nodes(root_node)
        evolution_stats["best_fitness_after"] = self._find_best_fitness(root_node)
        evolution_stats["evolution_end"] = time.time()
        
        # Generate visualization
        viz_path = self.visualize_tree(tree_id)
        evolution_stats["visualization"] = viz_path
        
        return evolution_stats
    
    def _count_nodes(self, node: SimplifiedQuantumFractalNode) -> int:
        """Count total nodes in a tree"""
        count = 1  # Count this node
        for child in node.children:
            count += self._count_nodes(child)
        return count
    
    def _find_leaf_nodes(self, node: SimplifiedQuantumFractalNode) -> List[SimplifiedQuantumFractalNode]:
        """Find all leaf nodes in a tree"""
        if not node.children:
            return [node]  # This is a leaf
            
        leaves = []
        for child in node.children:
            leaves.extend(self._find_leaf_nodes(child))
            
        return leaves
    
    def _find_best_fitness(self, node: SimplifiedQuantumFractalNode) -> float:
        """Find the best fitness in a tree"""
        best = node.seed.fitness
        for child in node.children:
            child_best = self._find_best_fitness(child)
            best = max(best, child_best)
        return best
    
    def find_best_seed(self) -> SimplifiedQuantumDNASeed:
        """Find the seed with the highest fitness"""
        if not self.seed_history:
            return None
            
        return max(self.seed_history, key=lambda seed: seed.fitness)
    
    def visualize_tree(self, tree_id: str) -> str:
        """Generate a visualization of a fractal tree"""
        if tree_id not in self.fractal_trees:
            raise ValueError(f"Tree {tree_id} not found")
            
        root_node = self.fractal_trees[tree_id]
        
        # Create figure
        plt.figure(figsize=(12, 10))
        
        # Plot nodes and connections
        self._plot_node(root_node)
        
        # Add title and labels
        plt.title(f"Quantum Fractal Tree: {tree_id}\nNodes: {self._count_nodes(root_node)}, Best Fitness: {self._find_best_fitness(root_node):.4f}")
        plt.axis('equal')
        plt.grid(True, alpha=0.3)
        
        # Save visualization
        viz_path = f"{self.output_dir}/visualizations/tree_{tree_id}.png"
        plt.savefig(viz_path, dpi=300)
        plt.close()
        
        return viz_path
    
    def _plot_node(self, node: SimplifiedQuantumFractalNode, parent_pos=None):
        """Recursively plot a node and its children"""
        # Get node position
        x, y = node.phi_position
        
        # Plot connection to parent
        if parent_pos is not None:
            px, py = parent_pos
            plt.plot([px, x], [py, y], 'k-', alpha=0.5)
        
        # Plot node
        fitness_color = plt.cm.viridis(node.seed.fitness)
        plt.scatter(x, y, s=100, c=[fitness_color], alpha=0.8)
        
        # Plot children
        for child in node.children:
            self._plot_node(child, (x, y))


def main():
    """Main function to demonstrate the Quantum Recursive Genesis System"""
    print("\n===== QUANTUM RECURSIVE GENESIS SYSTEM - SIMPLIFIED DEMO =====")
    print(f"Starting demo at: {datetime.now().isoformat()}")
    
    # Create the recursive genesis system
    genesis = SimplifiedQuantumRecursiveGenesis()
    
    # Step 1: Create a fractal tree
    print("\n[1] Creating genesis seed and initial fractal tree...")
    tree_id = genesis.create_fractal_tree()
    print(f"  Created fractal tree: {tree_id}")
    
    # Step 2: Evolve the tree for multiple generations
    print("\n[2] Evolving fractal tree for 5 generations...")
    evolution_stats = genesis.evolve_tree(tree_id, 5)
    print(f"  Evolution complete:")
    print(f"  - New nodes created: {evolution_stats['new_nodes']}")
    print(f"  - Fitness improved: {evolution_stats['best_fitness_before']:.4f} → {evolution_stats['best_fitness_after']:.4f}")
    print(f"  - Visualization saved to: {evolution_stats['visualization']}")
    
    # Step 3: Find the best seed
    best_seed = genesis.find_best_seed()
    print("\n[3] Best seed information:")
    print(f"  - DNA: {best_seed.dna_string}")
    print(f"  - Phi-alignment: {best_seed.phi_alignment:.4f}")
    print(f"  - Fitness: {best_seed.fitness:.4f}")
    print(f"  - Generation: {best_seed.generation}")
    print(f"  - Quantum signature: {best_seed.quantum_signature}")
    
    # Test complete
    print("\n===== DEMO COMPLETE =====")
    print(f"Results saved to: {genesis.output_dir}")
    print("Open the visualization file to see the fractal tree structure.")


if __name__ == "__main__":
    main()
