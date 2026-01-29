#!/usr/bin/env python3
"""
Quantum Phi-Harmonic System: Core Computational Framework
Implements golden ratio mathematics, fractal pattern generation, and quantum-inspired metrics
"""

import math
import numpy as np
from typing import Dict, List, Tuple, Union, Optional
import random
import argparse

# Core mathematical constants
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio (φ)
PHI_INVERSE = 1 / PHI
FIBONACCI = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
PRIME_DIMENSIONS = [17, 19, 23, 29, 31, 37, 41, 43]


class QuantumPhiCore:
    """Core computational engine for Quantum Phi-Harmonic operations"""
    
    def __init__(self):
        self.quantum_coherence = 0.87
        self.phi_resonance = 0.93
        self.phi_stability = 0.76
        self.active_dimensions = 8
        self.corpus_data = {}
        
    def calculate_phi_resonance(self, values: List[float]) -> float:
        """
        Calculate phi-resonance of a sequence of values based on their
        alignment with the golden ratio.
        
        Args:
            values: List of numerical values to analyze
            
        Returns:
            Phi resonance value between 0 and 1
        """
        if len(values) < 2:
            return 0.0
            
        # Calculate ratios between adjacent elements
        ratios = [values[i+1]/values[i] if values[i] != 0 else 0 
                 for i in range(len(values)-1)]
        
        # Measure how close each ratio is to phi
        phi_distances = [abs(ratio - PHI)/PHI for ratio in ratios if ratio > 0]
        
        # Calculate phi alignment (1 = perfect alignment, 0 = no alignment)
        if not phi_distances:
            return 0.0
            
        phi_alignment = 1 - sum(phi_distances) / len(phi_distances)
        return max(0.0, min(1.0, phi_alignment))
    
    def calculate_quantum_coherence(self, matrix: np.ndarray) -> float:
        """
        Calculate quantum coherence from a matrix of values using
        quantum-inspired measurement.
        
        Args:
            matrix: 2D numpy array of values
            
        Returns:
            Quantum coherence value between 0 and 1
        """
        # Handle empty matrix
        if matrix.size == 0:
            return 0.0
            
        # Normalize matrix
        matrix_norm = np.linalg.norm(matrix)
        if matrix_norm == 0:
            return 0.0
            
        normalized_matrix = matrix / matrix_norm
        
        # Calculate von Neumann entropy (quantum-inspired)
        eigenvalues = np.linalg.eigvalsh(normalized_matrix.T @ normalized_matrix)
        positive_eigenvalues = [ev for ev in eigenvalues if ev > 1e-10]
        
        if not positive_eigenvalues:
            return 0.0
            
        entropy = -sum(ev * math.log(ev) for ev in positive_eigenvalues)
        max_entropy = math.log(len(positive_eigenvalues))
        
        # Coherence = 1 - normalized entropy
        coherence = 1.0
        if max_entropy > 0:
            coherence = 1.0 - entropy / max_entropy
            
        return max(0.0, min(1.0, coherence))
    
    def generate_fractal_pattern(self, depth: int = 5, density: float = 1.0) -> Dict:
        """
        Generate a fractal pattern based on the golden ratio with quantum properties
        
        Args:
            depth: Number of fractal recursion levels
            density: Density coefficient for node generation
            
        Returns:
            Dictionary containing fractal pattern data
        """
        pattern = {
            "nodes": [],
            "connections": [],
            "metrics": {
                "phi_resonance": 0.0,
                "quantum_coherence": 0.0,
                "phi_stability": 0.0
            }
        }
        
        # Generate nodes following golden ratio distribution
        total_nodes = 0
        for level in range(depth):
            # Fibonacci-based node count scaling
            level_nodes = math.ceil(FIBONACCI[min(level+5, len(FIBONACCI)-1)] * density)
            total_nodes += level_nodes
            
            # Generate nodes for this level using golden angle
            golden_angle = 2 * math.pi * PHI_INVERSE
            for i in range(level_nodes):
                angle = i * golden_angle
                
                # Radius uses golden ratio scaling
                radius = math.sqrt(i) * 20 * (PHI_INVERSE ** level)
                
                # Apply quantum jitter based on coherence
                jitter = (1 - self.quantum_coherence) * 5
                jitter_x = (random.random() - 0.5) * jitter
                jitter_y = (random.random() - 0.5) * jitter
                
                # Calculate position
                x = math.cos(angle) * radius + jitter_x
                y = math.sin(angle) * radius + jitter_y
                
                # Add node with level information
                pattern["nodes"].append({
                    "id": len(pattern["nodes"]),
                    "x": x,
                    "y": y,
                    "level": level,
                    "size": 3 + (random.random() * 2 * self.phi_resonance) * (PHI_INVERSE ** level)
                })
        
        # Generate connections between nodes based on quantum coherence
        connection_density = 0.1 + (self.quantum_coherence * 0.4)
        connection_count = math.floor(len(pattern["nodes"]) * connection_density)
        
        for i in range(connection_count):
            # Use prime numbers for quantum-aligned connections
            node_a = i % len(pattern["nodes"])
            node_b = (i * PRIME_DIMENSIONS[i % len(PRIME_DIMENSIONS)]) % len(pattern["nodes"])
            
            if node_a != node_b:
                # Add connection with phi-stability as opacity
                pattern["connections"].append({
                    "source": node_a,
                    "target": node_b,
                    "strength": 0.2 + random.random() * 0.3 * self.phi_stability
                })
        
        # Calculate pattern metrics
        node_positions = [[n["x"], n["y"]] for n in pattern["nodes"]]
        if node_positions:
            pattern_matrix = np.array(node_positions)
            phi_values = [n["size"] for n in pattern["nodes"]]
            
            pattern["metrics"]["phi_resonance"] = self.calculate_phi_resonance(phi_values)
            pattern["metrics"]["quantum_coherence"] = self.calculate_quantum_coherence(pattern_matrix)
            pattern["metrics"]["phi_stability"] = 0.3 + 0.7 * pattern["metrics"]["phi_resonance"]
        
        return pattern
    
    def calculate_phi_pattern(self, sequence: List[float]) -> Dict:
        """
        Analyze a numerical sequence for phi-harmonic patterns
        
        Args:
            sequence: List of numerical values
            
        Returns:
            Dictionary containing phi-pattern analysis
        """
        result = {
            "phi_resonance": 0.0,
            "fibonacci_similarity": 0.0,
            "phi_ratios": [],
            "fibonacci_indices": []
        }
        
        if len(sequence) < 2:
            return result
            
        # Calculate adjacent ratios
        ratios = [sequence[i+1]/sequence[i] if sequence[i] != 0 else 0 
                 for i in range(len(sequence)-1)]
        
        # Find ratios close to PHI
        phi_ratios = [(i, ratio) for i, ratio in enumerate(ratios) 
                      if abs(ratio - PHI)/PHI < 0.1]
        result["phi_ratios"] = phi_ratios
        
        # Calculate phi resonance
        result["phi_resonance"] = self.calculate_phi_resonance(sequence)
        
        # Find Fibonacci-like sequences
        for i in range(len(sequence)-2):
            if abs(sequence[i] + sequence[i+1] - sequence[i+2])/sequence[i+2] < 0.1:
                result["fibonacci_indices"].append(i)
        
        # Calculate Fibonacci similarity
        # Compare growth pattern to Fibonacci sequence
        if len(sequence) >= 3:
            growth_factors = [sequence[i+1]/sequence[i] if sequence[i] != 0 else 0 
                             for i in range(len(sequence)-1)]
            fib_factors = [FIBONACCI[i+1]/FIBONACCI[i] for i in range(min(len(sequence), len(FIBONACCI))-1)]
            fib_factors = fib_factors[:len(growth_factors)]
            
            if growth_factors and fib_factors:
                differences = [abs(g - f)/f if f != 0 else 1.0 
                              for g, f in zip(growth_factors, fib_factors)]
                result["fibonacci_similarity"] = 1 - min(1.0, sum(differences) / len(differences))
        
        return result

    def analyze_dimensions(self, matrix: np.ndarray) -> Dict:
        """
        Analyze dimensional properties of multi-dimensional data
        
        Args:
            matrix: Multi-dimensional numpy array
            
        Returns:
            Dictionary with dimensional analysis
        """
        result = {
            "active_dimensions": 0,
            "dimension_resonance": [],
            "quantum_coherence": 0.0,
            "phi_dimensional_harmony": 0.0
        }
        
        if matrix.size == 0:
            return result
            
        # Get matrix shape and analyze active dimensions
        shape = matrix.shape
        result["active_dimensions"] = len(shape)
        
        # Calculate phi resonance for each dimension
        dimension_resonances = []
        for dim in range(len(shape)):
            # Extract values along this dimension
            indices = [slice(None)] * len(shape)
            values = []
            
            for i in range(shape[dim]):
                indices[dim] = i
                # Get mean value for this slice
                slice_values = matrix[tuple(indices)]
                values.append(np.mean(slice_values))
            
            # Calculate phi resonance for this dimension
            if len(values) >= 2:
                dim_resonance = self.calculate_phi_resonance(values)
                dimension_resonances.append((dim, dim_resonance))
        
        result["dimension_resonance"] = dimension_resonances
        
        # Calculate overall metrics
        if dimension_resonances:
            result["phi_dimensional_harmony"] = sum(r for _, r in dimension_resonances) / len(dimension_resonances)
        
        # Calculate quantum coherence
        result["quantum_coherence"] = self.calculate_quantum_coherence(matrix.reshape(shape[0], -1) if len(shape) > 1 else matrix)
        
        return result
    
    def generate_phi_harmonic_tensor(self, dimensions: List[int]) -> np.ndarray:
        """
        Generate a tensor with phi-harmonic properties
        
        Args:
            dimensions: List of dimension sizes
            
        Returns:
            Numpy array with phi-harmonic patterns
        """
        if not dimensions:
            return np.array([])
            
        # Create tensor
        tensor = np.zeros(dimensions)
        
        # Fill with phi-harmonic values
        it = np.nditer(tensor, flags=['multi_index'], op_flags=['writeonly'])
        i = 0
        while not it.finished:
            # Use golden ratio sequences for values
            # Mix phi powers and position-based values
            index_sum = sum(it.multi_index)
            phi_power = PHI ** (i % 5)
            value = (phi_power * (1 + 0.1 * math.sin(index_sum * PHI_INVERSE))) % 1.0
            
            it[0] = value
            it.iternext()
            i += 1
        
        return tensor
    
    def find_optimal_phi_partition(self, values: List[float]) -> Tuple[int, float]:
        """
        Find the optimal partition point of a sequence that maximizes phi-resonance
        
        Args:
            values: List of numerical values
            
        Returns:
            Tuple containing (optimal_index, resonance_value)
        """
        if len(values) < 3:
            return (0, 0.0)
            
        best_index = 0
        best_resonance = 0.0
        
        for i in range(1, len(values)-1):
            # Split into two parts
            part1 = values[:i]
            part2 = values[i:]
            
            # Calculate ratio between sums
            sum1 = sum(part1)
            sum2 = sum(part2)
            
            if sum1 == 0 or sum2 == 0:
                continue
                
            # Check which ratio is closer to phi
            ratio = max(sum1, sum2) / min(sum1, sum2)
            phi_alignment = 1 - abs(ratio - PHI) / PHI
            
            if phi_alignment > best_resonance:
                best_resonance = phi_alignment
                best_index = i
        
        return (best_index, best_resonance)

    def process_query(self, query: str) -> Dict:
        """
        Process a natural language query and adjust system parameters
        
        Args:
            query: Text query string
            
        Returns:
            Dictionary with response and updated parameters
        """
        query = query.lower()
        response = {}
        
        # Track parameter changes
        original_params = {
            "quantum_coherence": self.quantum_coherence,
            "phi_resonance": self.phi_resonance,
            "phi_stability": self.phi_stability,
            "active_dimensions": self.active_dimensions
        }
        
        # Adjust parameters based on query content
        if "quantum" in query or "entanglement" in query or "coherence" in query:
            self.quantum_coherence = min(0.99, self.quantum_coherence + 0.05)
            
        if "phi" in query or "golden" in query or "harmonic" in query:
            self.phi_resonance = min(0.99, self.phi_resonance + 0.03)
            
        if "stability" in query or "balance" in query:
            self.phi_stability = min(0.99, self.phi_stability + 0.04)
            
        if "dimension" in query or "multi-dimensional" in query:
            self.active_dimensions = min(len(PRIME_DIMENSIONS), self.active_dimensions + 1)
        
        # Prepare system response
        response["changes"] = {
            "quantum_coherence": self.quantum_coherence - original_params["quantum_coherence"],
            "phi_resonance": self.phi_resonance - original_params["phi_resonance"],
            "phi_stability": self.phi_stability - original_params["phi_stability"],
            "active_dimensions": self.active_dimensions - original_params["active_dimensions"]
        }
        
        # Generate response text
        response_text = []
        
        if response["changes"]["quantum_coherence"] > 0:
            response_text.append(f"Quantum coherence increased to {self.quantum_coherence:.2f}")
            
        if response["changes"]["phi_resonance"] > 0:
            response_text.append(f"Phi-harmonic resonance optimized to {self.phi_resonance:.2f}")
            
        if response["changes"]["phi_stability"] > 0:
            response_text.append(f"System stability enhanced to {self.phi_stability:.2f}")
            
        if response["changes"]["active_dimensions"] > 0:
            response_text.append(f"Active dimensions expanded to {self.active_dimensions}")
            
        if not response_text:
            response_text.append(f"Processing query through quantum phi-harmonic system")
            
        response["text"] = ". ".join(response_text) + "."
        response["current_state"] = {
            "quantum_coherence": self.quantum_coherence,
            "phi_resonance": self.phi_resonance,
            "phi_stability": self.phi_stability,
            "active_dimensions": self.active_dimensions
        }
        
        return response


def cli():
    """Command line interface for Quantum Phi-Harmonic System"""
    parser = argparse.ArgumentParser(description="Quantum Phi-Harmonic System")
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # Generate fractal pattern
    fractal_parser = subparsers.add_parser("fractal", help="Generate fractal pattern")
    fractal_parser.add_argument("--depth", type=int, default=5, help="Fractal depth levels")
    fractal_parser.add_argument("--density", type=float, default=1.0, help="Node density coefficient")
    fractal_parser.add_argument("--output", type=str, default="fractal_pattern.json", help="Output file (JSON)")
    
    # Analyze sequence
    analyze_parser = subparsers.add_parser("analyze", help="Analyze numerical sequence")
    analyze_parser.add_argument("--values", type=float, nargs="+", required=True, help="Numerical values to analyze")
    
    # Process query
    query_parser = subparsers.add_parser("query", help="Process natural language query")
    query_parser.add_argument("--text", type=str, required=True, help="Query text")
    
    # Create tensor
    tensor_parser = subparsers.add_parser("tensor", help="Generate phi-harmonic tensor")
    tensor_parser.add_argument("--dimensions", type=int, nargs="+", required=True, help="Tensor dimensions")
    tensor_parser.add_argument("--output", type=str, default="phi_tensor.npy", help="Output file (NPY)")
    
    # Parse arguments
    args = parser.parse_args()
    system = QuantumPhiCore()
    
    import json
    
    # Execute command
    if args.command == "fractal":
        print(f"Generating fractal pattern with depth={args.depth}, density={args.density}")
        pattern = system.generate_fractal_pattern(args.depth, args.density)
        
        # Save to JSON file
        with open(args.output, "w") as f:
            json.dump(pattern, f, indent=2)
            
        # Print summary
        print(f"Generated pattern with {len(pattern['nodes'])} nodes and {len(pattern['connections'])} connections")
        print(f"Metrics: phi_resonance={pattern['metrics']['phi_resonance']:.4f}, "
              f"quantum_coherence={pattern['metrics']['quantum_coherence']:.4f}, "
              f"phi_stability={pattern['metrics']['phi_stability']:.4f}")
        print(f"Saved to {args.output}")
        
    elif args.command == "analyze":
        print(f"Analyzing sequence: {args.values}")
        result = system.calculate_phi_pattern(args.values)
        
        # Print results
        print(f"Phi resonance: {result['phi_resonance']:.4f}")
        print(f"Fibonacci similarity: {result['fibonacci_similarity']:.4f}")
        
        if result['phi_ratios']:
            print(f"Found {len(result['phi_ratios'])} phi-like ratios at indices: "
                  f"{[i for i, _ in result['phi_ratios']]}")
            
        if result['fibonacci_indices']:
            print(f"Found Fibonacci-like sequences starting at indices: {result['fibonacci_indices']}")
            
        # Find optimal partition
        partition, resonance = system.find_optimal_phi_partition(args.values)
        print(f"Optimal phi partition at index {partition} with resonance {resonance:.4f}")
        
    elif args.command == "query":
        print(f"Processing query: '{args.text}'")
        response = system.process_query(args.text)
        
        # Print response
        print(f"System response: {response['text']}")
        print("Parameter changes:")
        
        for param, change in response["changes"].items():
            if change != 0:
                print(f"  {param}: {change:+.4f}")
                
        print("Current system state:")
        for param, value in response["current_state"].items():
            print(f"  {param}: {value:.4f}")
            
    elif args.command == "tensor":
        print(f"Generating phi-harmonic tensor with dimensions {args.dimensions}")
        tensor = system.generate_phi_harmonic_tensor(args.dimensions)
        
        # Save tensor
        np.save(args.output, tensor)
        
        # Analyze dimensions
        analysis = system.analyze_dimensions(tensor)
        
        # Print results
        print(f"Generated tensor with shape {tensor.shape}")
        print(f"Quantum coherence: {analysis['quantum_coherence']:.4f}")
        print(f"Phi-dimensional harmony: {analysis['phi_dimensional_harmony']:.4f}")
        
        if analysis['dimension_resonance']:
            print("Dimension resonance values:")
            for dim, resonance in analysis['dimension_resonance']:
                print(f"  Dimension {dim}: {resonance:.4f}")
                
        print(f"Saved tensor to {args.output}")
    
    else:
        parser.print_help()


if __name__ == "__main__":
    cli()