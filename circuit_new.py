# """
# Unified Quantum Circuit AI: A comprehensive system that designs, implements, and evolves its own circuitry.

# This application integrates:
# 1. Digital circuit representation and evolution
# 2. Hardware implementation (Verilog, PCB, FPGA)
# 3. Meta-evolution to improve the system's own design capabilities
# 4. Circuit visualization and generation
# 5. Advanced circuit brain with knowledge extraction
# """

# import os
# import logging
# import argparse
# import random
# import copy
# import math
# import time
# import json
# import numpy as np
# import matplotlib.pyplot as plt
# import hashlib
# import threading
# import requests
# from enum import Enum, auto
# from typing import Dict, List, Set, Tuple, Callable, Optional, Union, Any
# from dataclasses import dataclass, field
# import torch
# import torch.nn as nn
# import base64

# # Configure logging
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# )
# logger = logging.getLogger("QuantumCircuitAI")

# ###########################################
# # PART 1: CORE CIRCUIT CLASSES & FUNCTIONS
# ###########################################

# class GateType(Enum):
#     """Enumeration of possible gate types in a circuit."""
#     INPUT = auto()
#     OUTPUT = auto()
#     AND = auto()
#     OR = auto()
#     NOT = auto()
#     NAND = auto()
#     NOR = auto()
#     XOR = auto()
#     XNOR = auto()
#     BUFFER = auto()
#     MUX = auto()
#     ADDER = auto()
#     FLIP_FLOP = auto()
#     LATCH = auto()
#     REGISTER = auto()
#     # Advanced gates
#     NEURON = auto()
#     SYNAPSE = auto()
#     FRACTAL_NODE = auto()
#     RECURSIVE_NODE = auto()
#     # Theoretical gates
#     TACHYON_TRANSMITTER = auto()
#     TACHYON_RECEIVER = auto()
#     TEMPORAL_GATE = auto()
#     QUANTUM_GATE = auto()
    
#     @classmethod
#     def basic_gates(cls):
#         """Return list of basic gates."""
#         return [cls.AND, cls.OR, cls.NOT, cls.NAND, cls.NOR, cls.XOR, cls.XNOR, cls.BUFFER]
    
#     @classmethod
#     def advanced_gates(cls):
#         """Return list of advanced gates."""
#         return [cls.MUX, cls.ADDER, cls.FLIP_FLOP, cls.LATCH, cls.REGISTER]
    
#     @classmethod
#     def neural_gates(cls):
#         """Return list of neural-inspired gates."""
#         return [cls.NEURON, cls.SYNAPSE]
    
#     @classmethod
#     def theoretical_gates(cls):
#         """Return list of theoretical gates."""
#         return [cls.FRACTAL_NODE, cls.RECURSIVE_NODE, cls.TACHYON_TRANSMITTER, 
#                cls.TACHYON_RECEIVER, cls.TEMPORAL_GATE, cls.QUANTUM_GATE]

# class CircuitNode:
#     """Represents a single node (gate) in a circuit."""
    
#     def __init__(self, id: int, gate_type: GateType):
#         self.id = id
#         self.gate_type = gate_type
#         self.inputs: List[int] = []  # List of node IDs connected to inputs
#         self.outputs: List[int] = []  # List of node IDs this node connects to
#         self.properties: Dict[str, Any] = {}  # Additional properties for specialized gates
        
#     def clone(self) -> 'CircuitNode':
#         """Create a deep copy of this node."""
#         new_node = CircuitNode(self.id, self.gate_type)
#         new_node.inputs = copy.deepcopy(self.inputs)
#         new_node.outputs = copy.deepcopy(self.outputs)
#         new_node.properties = copy.deepcopy(self.properties)
#         return new_node
        
#     def evaluate(self, input_values: Dict[int, bool]) -> bool:
#         """
#         Evaluate this node based on its gate type and input values.
        
#         Args:
#             input_values: Dictionary mapping node IDs to their boolean values
            
#         Returns:
#             Boolean result of the gate operation
#         """
#         # Special gate types
#         if self.gate_type == GateType.INPUT:
#             return input_values.get(self.id, False)
            
#         if self.gate_type == GateType.OUTPUT:
#             if not self.inputs:
#                 return False
#             return input_values.get(self.inputs[0], False)
            
#         # Handle normal gate types
#         if not self.inputs:
#             return False
            
#         input_vals = [input_values.get(input_id, False) for input_id in self.inputs]
        
#         if self.gate_type == GateType.AND:
#             return all(input_vals)
#         elif self.gate_type == GateType.OR:
#             return any(input_vals)
#         elif self.gate_type == GateType.NOT:
#             return not input_vals[0] if input_vals else False
#         elif self.gate_type == GateType.NAND:
#             return not all(input_vals)
#         elif self.gate_type == GateType.NOR:
#             return not any(input_vals)
#         elif self.gate_type == GateType.XOR:
#             return sum(input_vals) % 2 == 1
#         elif self.gate_type == GateType.XNOR:
#             return sum(input_vals) % 2 == 0
#         elif self.gate_type == GateType.BUFFER:
#             return input_vals[0] if input_vals else False
#         elif self.gate_type == GateType.MUX:
#             # MUX with select as first input, then data inputs
#             if len(input_vals) >= 3:
#                 select = input_vals[0]
#                 return input_vals[2] if select else input_vals[1]
#             return False
#         elif self.gate_type == GateType.ADDER:
#             # Simple binary addition (XOR of all inputs)
#             return sum(input_vals) % 2 == 1
        
#         # Advanced gate types
#         elif self.gate_type == GateType.NEURON:
#             # Simple threshold neuron
#             threshold = self.properties.get("threshold", 0.5)
#             weights = self.properties.get("weights", [1.0] * len(input_vals))
            
#             weighted_sum = sum(w * float(v) for w, v in zip(weights[:len(input_vals)], input_vals))
#             return weighted_sum >= threshold
            
#         elif self.gate_type == GateType.SYNAPSE:
#             # Synapse passes signal with weight
#             weight = self.properties.get("weight", 1.0)
#             return bool(weight * float(input_vals[0])) if input_vals else False
            
#         # Theoretical gate types with simplified implementation
#         elif self.gate_type == GateType.QUANTUM_GATE:
#             # Simplified quantum gate that introduces randomness
#             return random.random() < 0.5
        
#         # Default for unhandled gate types
#         return False
        
#     def __str__(self) -> str:
#         """String representation of the node."""
#         return f"Node {self.id} ({self.gate_type.name}): inputs={self.inputs}, outputs={self.outputs}"

# class Circuit:
#     """Represents a complete circuit with nodes and connections."""
    
#     def __init__(self, name: str = "Circuit"):
#         self.name = name
#         self.nodes: Dict[int, CircuitNode] = {}  # node_id -> node mapping
#         self.inputs: List[int] = []  # Input node IDs
#         self.outputs: List[int] = []  # Output node IDs
#         self.evaluation_cache = {}  # Cache for evaluation results
#         self.complexity = 0  # Measure of circuit complexity
#         self.metadata: Dict[str, Any] = {}  # Metadata about the circuit
        
#     def add_node(self, node: CircuitNode) -> int:
#         """Add a node to the circuit and return its ID."""
#         self.nodes[node.id] = node
        
#         # Update input/output lists if needed
#         if node.gate_type == GateType.INPUT and node.id not in self.inputs:
#             self.inputs.append(node.id)
#         elif node.gate_type == GateType.OUTPUT and node.id not in self.outputs:
#             self.outputs.append(node.id)
            
#         # Update complexity
#         self.update_complexity()
            
#         return node.id
        
#     def connect(self, from_id: int, to_id: int) -> bool:
#         """
#         Connect two nodes in the circuit.
        
#         Args:
#             from_id: ID of the source node
#             to_id: ID of the destination node
            
#         Returns:
#             True if connection was successful, False otherwise
#         """
#         if from_id not in self.nodes or to_id not in self.nodes:
#             return False
            
#         from_node = self.nodes[from_id]
#         to_node = self.nodes[to_id]
        
#         # Don't connect if already connected
#         if to_id in from_node.outputs or from_id in to_node.inputs:
#             return False
            
#         # Add connection
#         from_node.outputs.append(to_id)
#         to_node.inputs.append(from_id)
        
#         # Update complexity
#         self.update_complexity()
        
#         return True
        
#     def disconnect(self, from_id: int, to_id: int) -> bool:
#         """
#         Remove a connection between two nodes.
        
#         Args:
#             from_id: ID of the source node
#             to_id: ID of the destination node
            
#         Returns:
#             True if disconnection was successful, False otherwise
#         """
#         if from_id not in self.nodes or to_id not in self.nodes:
#             return False
            
#         from_node = self.nodes[from_id]
#         to_node = self.nodes[to_id]
        
#         # Remove connection if it exists
#         if to_id in from_node.outputs and from_id in to_node.inputs:
#             from_node.outputs.remove(to_id)
#             to_node.inputs.remove(from_id)
            
#             # Update complexity
#             self.update_complexity()
            
#             return True
            
#         return False
        
#     def remove_node(self, node_id: int) -> bool:
#         """
#         Remove a node from the circuit and all its connections.
        
#         Args:
#             node_id: ID of the node to remove
            
#         Returns:
#             True if removal was successful, False if node doesn't exist
#         """
#         if node_id not in self.nodes:
#             return False
            
#         node = self.nodes[node_id]
        
#         # Remove connections to this node
#         for input_id in node.inputs:
#             if input_id in self.nodes:
#                 input_node = self.nodes[input_id]
#                 if node_id in input_node.outputs:
#                     input_node.outputs.remove(node_id)
                    
#         # Remove connections from this node
#         for output_id in node.outputs:
#             if output_id in self.nodes:
#                 output_node = self.nodes[output_id]
#                 if node_id in output_node.inputs:
#                     output_node.inputs.remove(node_id)
                    
#         # Remove from inputs/outputs lists if needed
#         if node_id in self.inputs:
#             self.inputs.remove(node_id)
#         if node_id in self.outputs:
#             self.outputs.remove(node_id)
            
#         # Remove the node
#         del self.nodes[node_id]
        
#         # Update complexity
#         self.update_complexity()
        
#         return True
        
#     def clear_cache(self):
#         """Clear the evaluation cache."""
#         self.evaluation_cache = {}
        
#     def clone(self) -> 'Circuit':
#         """Create a deep copy of this circuit."""
#         new_circuit = Circuit(self.name)
#         new_circuit.inputs = copy.deepcopy(self.inputs)
#         new_circuit.outputs = copy.deepcopy(self.outputs)
#         new_circuit.metadata = copy.deepcopy(self.metadata)
        
#         # Clone all nodes
#         for node_id, node in self.nodes.items():
#             new_circuit.nodes[node_id] = node.clone()
            
#         # Update complexity
#         new_circuit.update_complexity()
        
#         return new_circuit
        
#     def update_complexity(self):
#         """Calculate and update the complexity measure of the circuit."""
#         # Basic complexity is the number of nodes plus connections
#         nodes_count = len(self.nodes)
#         connections_count = sum(len(node.outputs) for node in self.nodes.values())
        
#         # Weighted by gate type complexity
#         gate_complexity = 0
#         for node in self.nodes.values():
#             if node.gate_type in [GateType.INPUT, GateType.OUTPUT, GateType.BUFFER]:
#                 gate_complexity += 1
#             elif node.gate_type in [GateType.AND, GateType.OR, GateType.NOT, GateType.XOR]:
#                 gate_complexity += 2
#             elif node.gate_type in [GateType.NAND, GateType.NOR, GateType.XNOR]:
#                 gate_complexity += 3
#             elif node.gate_type in [GateType.MUX, GateType.ADDER]:
#                 gate_complexity += 4
#             elif node.gate_type in [GateType.FLIP_FLOP, GateType.LATCH, GateType.REGISTER]:
#                 gate_complexity += 5
#             elif node.gate_type in [GateType.NEURON, GateType.SYNAPSE]:
#                 gate_complexity += 10
#             elif node.gate_type in [GateType.FRACTAL_NODE, GateType.RECURSIVE_NODE]:
#                 gate_complexity += 20
#             else:  # Theoretical gates
#                 gate_complexity += 30
                
#         # Circuit structure complexity (e.g., feedback loops)
#         structure_complexity = self._calculate_feedback_complexity()
        
#         # Combine to get overall complexity
#         self.complexity = nodes_count + connections_count + gate_complexity + structure_complexity
        
#     def _calculate_feedback_complexity(self) -> int:
#         """Calculate complexity contribution from feedback loops."""
#         # Simple check for cycles
#         visited = set()
#         recursion_stack = set()
        
#         def dfs_check_cycle(node_id):
#             if node_id in visited:
#                 return False  # Prevent revisiting nodes
#             visited.add(node_id)
#             recursion_stack.add(node_id)
            
#             node = self.nodes[node_id]
#             for neighbor_id in node.outputs:
#                 if neighbor_id not in visited:
#                     if dfs_check_cycle(neighbor_id):
#                         return True
#                 elif neighbor_id in recursion_stack:
#                     return True
                    
#             recursion_stack.remove(node_id)
#             return False
            
#         cycle_count = 0
#         for node_id in self.nodes:
#             if node_id not in visited:
#                 if dfs_check_cycle(node_id):
#                     cycle_count += 1
                    
#         return cycle_count * 5  # Each cycle adds 5 to complexity
        
#     def evaluate(self, input_values: Dict[int, bool]) -> Dict[int, bool]:
#         """
#         Evaluate the circuit with the given input values.
        
#         Args:
#             input_values: Dictionary mapping input node IDs to boolean values
            
#         Returns:
#             Dictionary mapping node IDs to their evaluated boolean values
#         """
#         # Check cache for this input combination
#         cache_key = tuple(sorted((k, v) for k, v in input_values.items()))
#         if cache_key in self.evaluation_cache:
#             return self.evaluation_cache[cache_key]
            
#         # Initialize result with input values
#         result = dict(input_values)
        
#         # Find evaluation order (topological sort)
#         visited = set(input_values.keys())
#         eval_order = list(input_values.keys())
        
#         # Helper function for topological sort
#         def visit(node_id):
#             if node_id in visited:
#                 return  # Prevent revisiting nodes
#             visited.add(node_id)
#             eval_order.append(node_id)
            
#             # First visit all inputs
#             for input_id in self.nodes[node_id].inputs:
#                 if input_id not in visited:
#                     visit(input_id)
                    
#         # Start visiting from output nodes
#         for output_id in self.outputs:
#             visit(output_id)
            
#         # Evaluate nodes in topological order
#         for node_id in eval_order:
#             node = self.nodes[node_id]
#             result[node_id] = node.evaluate(result)
            
#         # Cache the result
#         self.evaluation_cache[cache_key] = result
        
#         return result
        
#     def get_output_values(self, input_values: Dict[int, bool]) -> Dict[int, bool]:
#         """
#         Get only the output values from circuit evaluation.
        
#         Args:
#             input_values: Dictionary mapping input node IDs to boolean values
            
#         Returns:
#             Dictionary mapping output node IDs to their evaluated boolean values
#         """
#         full_result = self.evaluate(input_values)
#         return {output_id: full_result.get(output_id, False) for output_id in self.outputs}
        
#     def evaluate_truth_table(self) -> Dict[Tuple[bool, ...], Tuple[bool, ...]]:
#         """
#         Evaluate the circuit for all possible input combinations (truth table).
        
#         Returns:
#             Dictionary mapping input tuples to output tuples
#         """
#         truth_table = {}
        
#         # Generate all possible input combinations
#         input_count = len(self.inputs)
#         for i in range(2 ** input_count):
#             # Convert number to binary digits
#             binary = [(i >> bit) & 1 for bit in range(input_count)]
            
#             # Create input dictionary
#             input_values = {self.inputs[j]: bool(binary[j]) for j in range(input_count)}
            
#             # Evaluate circuit
#             output_values = self.get_output_values(input_values)
#             output_tuple = tuple(output_values.get(output_id, False) for output_id in self.outputs)
            
#             # Add to truth table
#             input_tuple = tuple(input_values[input_id] for input_id in self.inputs)
#             truth_table[input_tuple] = output_tuple
            
#         return truth_table
        
#     def get_next_node_id(self) -> int:
#         """Get the next available node ID."""
#         return max(self.nodes.keys(), default=0) + 1
        
#     def __str__(self) -> str:
#         """String representation of the circuit."""
#         parts = [f"Circuit: {self.name}", f"Inputs: {self.inputs}", f"Outputs: {self.outputs}",
#                 f"Nodes: {len(self.nodes)}", f"Complexity: {self.complexity}", "Nodes:"]
                
#         for node_id, node in sorted(self.nodes.items()):
#             parts.append(f"  {node}")
            
#         return "\n".join(parts)

# class CircuitEvolution:
#     """Handles the evolution of circuits using genetic algorithms."""
    
#     def __init__(self, initial_population: List[Circuit], fitness_function: Callable[[Circuit], float],
#                 population_size: int = 100, mutation_rate: float = 0.1, crossover_rate: float = 0.7,
#                 allowed_gates: Optional[List[GateType]] = None):
#         self.population = initial_population[:population_size]
#         self.fitness_function = fitness_function
#         self.population_size = population_size
#         self.mutation_rate = mutation_rate
#         self.crossover_rate = crossover_rate
#         self.generation = 0
#         self.best_fitness = float('-inf')
#         self.best_circuit = None
#         self.fitness_history = []
#         self.allowed_gates = allowed_gates or GateType.basic_gates()
        
#     def evolve(self, generations: int = 100, callback: Optional[Callable[[int, Circuit, float], None]] = None) -> Circuit:
#         """
#         Evolve the population for the given number of generations.
        
#         Args:
#             generations: Number of generations to evolve
#             callback: Optional function called after each generation with (generation, best_circuit, best_fitness)
            
#         Returns:
#             The best circuit from the final population
#         """
#         for gen in range(generations):
#             self.generation = gen + 1
            
#             # Evaluate fitness for all circuits
#             fitness_scores = []
#             for circuit in self.population:
#                 fitness = self.fitness_function(circuit)
#                 fitness_scores.append((circuit, fitness))
                
#             # Sort by fitness (descending)
#             fitness_scores.sort(key=lambda x: x[1], reverse=True)
            
#             # Track best circuit
#             best_circuit, best_fitness = fitness_scores[0]
#             if best_fitness > self.best_fitness:
#                 self.best_fitness = best_fitness
#                 self.best_circuit = best_circuit.clone()
                
#             # Record history
#             avg_fitness = sum(score for _, score in fitness_scores) / len(fitness_scores)
#             self.fitness_history.append({
#                 'generation': self.generation,
#                 'best_fitness': best_fitness,
#                 'avg_fitness': avg_fitness,
#                 'best_complexity': best_circuit.complexity
#             })
            
#             # Call callback if provided
#             if callback:
#                 callback(self.generation, best_circuit, best_fitness)
                
#             # Create new population
#             new_population = []
            
#             # Elitism: keep the best circuits
#             elite_count = max(1, int(self.population_size * 0.1))
#             for i in range(elite_count):
#                 new_population.append(fitness_scores[i][0].clone())
                
#             # Fill the rest with offspring
#             while len(new_population) < self.population_size:
#                 # Selection
#                 parent1 = self._selection(fitness_scores)
#                 parent2 = self._selection(fitness_scores)
                
#                 # Crossover
#                 if random.random() < self.crossover_rate:
#                     child1, child2 = self._crossover(parent1, parent2)
#                 else:
#                     child1, child2 = parent1.clone(), parent2.clone()
                    
#                 # Mutation
#                 self._mutate(child1)
#                 self._mutate(child2)
                
#                 # Add to new population
#                 new_population.append(child1)
#                 if len(new_population) < self.population_size:
#                     new_population.append(child2)
                    
#             # Replace old population
#             self.population = new_population
            
#             # Log progress
#             if gen % 10 == 0 or gen == generations - 1:
#                 logger.info(f"Generation {gen+1}/{generations}: Best fitness = {best_fitness:.4f}, "
#                            f"Avg fitness = {avg_fitness:.4f}, Complexity = {best_circuit.complexity}")
            
#         # Return best circuit after evolution
#         return self.best_circuit
        
#     def _selection(self, fitness_scores: List[Tuple[Circuit, float]]) -> Circuit:
#         """
#         Select a circuit from the population based on fitness.
        
#         Args:
#             fitness_scores: List of (circuit, fitness) tuples
            
#         Returns:
#             Selected circuit
#         """
#         # Tournament selection
#         tournament_size = max(2, int(len(fitness_scores) * 0.1))
#         tournament = random.sample(fitness_scores, tournament_size)
#         winner = max(tournament, key=lambda x: x[1])[0]
#         return winner
        
#     def _crossover(self, parent1: Circuit, parent2: Circuit) -> Tuple[Circuit, Circuit]:
#         """
#         Perform crossover between two parent circuits.
        
#         Args:
#             parent1: First parent circuit
#             parent2: Second parent circuit
            
#         Returns:
#             Two child circuits
#         """
#         child1 = Circuit(f"{parent1.name}_x_{parent2.name}")
#         child2 = Circuit(f"{parent2.name}_x_{parent1.name}")
        
#         # Map from old node IDs to new node IDs
#         p1_map = {}
#         p2_map = {}
        
#         # Choose crossover point (percentage of nodes to take from each parent)
#         crossover_point = random.uniform(0.3, 0.7)
        
#         # Add input and output nodes first
#         for input_id in sorted(parent1.inputs):
#             node = parent1.nodes[input_id]
#             new_id = child1.get_next_node_id()
#             p1_map[input_id] = new_id
            
#             new_node = CircuitNode(new_id, node.gate_type)
#             child1.add_node(new_node)
            
#         for output_id in sorted(parent1.outputs):
#             node = parent1.nodes[output_id]
#             new_id = child1.get_next_node_id()
#             p1_map[output_id] = new_id
            
#             new_node = CircuitNode(new_id, node.gate_type)
#             child1.add_node(new_node)
            
#         for input_id in sorted(parent2.inputs):
#             node = parent2.nodes[input_id]
#             new_id = child2.get_next_node_id()
#             p2_map[input_id] = new_id
            
#             new_node = CircuitNode(new_id, node.gate_type)
#             child2.add_node(new_node)
            
#         for output_id in sorted(parent2.outputs):
#             node = parent2.nodes[output_id]
#             new_id = child2.get_next_node_id()
#             p2_map[output_id] = new_id
            
#             new_node = CircuitNode(new_id, node.gate_type)
#             child2.add_node(new_node)
            
#         # Add other nodes from parents
#         p1_nodes = [n for n in parent1.nodes.values() 
#                    if n.id not in parent1.inputs and n.id not in parent1.outputs]
#         p2_nodes = [n for n in parent2.nodes.values()
#                    if n.id not in parent2.inputs and n.id not in parent2.outputs]
        
#         # Shuffle to mix genes
#         random.shuffle(p1_nodes)
#         random.shuffle(p2_nodes)
        
#         # Determine how many nodes to take from each parent
#         p1_count = int(len(p1_nodes) * crossover_point)
#         p2_count = int(len(p2_nodes) * crossover_point)
        
#         # Add nodes to child1 (p1_count from parent1, rest from parent2)
#         for node in p1_nodes[:p1_count]:
#             new_id = child1.get_next_node_id()
#             p1_map[node.id] = new_id
            
#             new_node = CircuitNode(new_id, node.gate_type)
#             new_node.properties = copy.deepcopy(node.properties)
#             child1.add_node(new_node)
            
#         for node in p2_nodes[p2_count:]:
#             new_id = child1.get_next_node_id()
#             p2_map[node.id] = new_id
            
#             new_node = CircuitNode(new_id, node.gate_type)
#             new_node.properties = copy.deepcopy(node.properties)
#             child1.add_node(new_node)
            
#         # Add nodes to child2 (p2_count from parent2, rest from parent1)
#         for node in p2_nodes[:p2_count]:
#             new_id = child2.get_next_node_id()
#             p2_map[node.id] = new_id
            
#             new_node = CircuitNode(new_id, node.gate_type)
#             new_node.properties = copy.deepcopy(node.properties)
#             child2.add_node(new_node)
            
#         for node in p1_nodes[p1_count:]:
#             new_id = child2.get_next_node_id()
#             p1_map[node.id] = new_id
            
#             new_node = CircuitNode(new_id, node.gate_type)
#             new_node.properties = copy.deepcopy(node.properties)
#             child2.add_node(new_node)
            
#         # Add connections in child1
#         for node_id, new_id in p1_map.items():
#             node = parent1.nodes[node_id]
#             for output_id in node.outputs:
#                 if output_id in p1_map:
#                     child1.connect(new_id, p1_map[output_id])
                    
#         for node_id, new_id in p2_map.items():
#             node = parent2.nodes[node_id]
#             for output_id in node.outputs:
#                 if output_id in p2_map:
#                     child1.connect(new_id, p2_map[output_id])
                    
#         # Add connections in child2
#         for node_id, new_id in p2_map.items():
#             node = parent2.nodes[node_id]
#             for output_id in node.outputs:
#                 if output_id in p2_map:
#                     child2.connect(new_id, p2_map[output_id])
                    
#         for node_id, new_id in p1_map.items():
#             node = parent1.nodes[node_id]
#             for output_id in node.outputs:
#                 if output_id in p1_map:
#                     child2.connect(new_id, p1_map[output_id])
                    
#         return child1, child2
        
#     def _mutate(self, circuit: Circuit) -> None:
#         """
#         Mutate a circuit by performing random changes.
        
#         Args:
#             circuit: Circuit to mutate
#         """
#         # Skip mutation based on rate
#         if random.random() > self.mutation_rate:
#             return
            
#         # Choose mutation type
#         mutation_type = random.choice(["add_node", "remove_node", "change_type", 
#                                       "add_connection", "remove_connection"])
                                      
#         if mutation_type == "add_node":
#             # Add a new node
#             new_id = circuit.get_next_node_id()
#             gate_type = random.choice(self.allowed_gates)
                
#             new_node = CircuitNode(new_id, gate_type)
#             circuit.add_node(new_node)
            
#             # Connect to existing nodes
#             existing_nodes = list(circuit.nodes.keys())
#             if existing_nodes:
#                 # Connect an input
#                 input_id = random.choice(existing_nodes)
#                 circuit.connect(input_id, new_id)
                
#                 # Connect an output
#                 output_id = random.choice(existing_nodes)
#                 circuit.connect(new_id, output_id)
                
#         elif mutation_type == "remove_node":
#             # Remove a random node (except inputs and outputs)
#             removable_nodes = [node_id for node_id in circuit.nodes 
#                               if node_id not in circuit.

"""
Unified Quantum Circuit AI: A comprehensive system that designs, implements, and evolves its own circuitry.

This application integrates:
1. Digital circuit representation and evolution
2. Hardware implementation (Verilog, PCB, FPGA)
3. Meta-evolution to improve the system's own design capabilities
4. Circuit visualization and generation
5. Advanced circuit brain with knowledge extraction
"""

import os
import logging
import argparse
import random
import copy
import math
import time
import json
import numpy as np
import matplotlib.pyplot as plt
import hashlib
import threading
import requests
from enum import Enum, auto
from typing import Dict, List, Set, Tuple, Callable, Optional, Union, Any
from dataclasses import dataclass, field
import torch
import torch.nn as nn
import base64

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("QuantumCircuitAI")

# Constants
PHI = (1 + np.sqrt(5)) / 2  # Golden Ratio for harmonic resonance
DB_FILE = "quantum_circuit_storage.db"

###########################################
# PART 1: CORE CIRCUIT CLASSES & FUNCTIONS
###########################################

class GateType(Enum):
    """Enumeration of possible gate types in a circuit."""
    INPUT = auto()
    OUTPUT = auto()
    AND = auto()
    OR = auto()
    NOT = auto()
    NAND = auto()
    NOR = auto()
    XOR = auto()
    XNOR = auto()
    BUFFER = auto()
    MUX = auto()
    ADDER = auto()
    FLIP_FLOP = auto()
    LATCH = auto()
    REGISTER = auto()
    # Advanced gates
    NEURON = auto()
    SYNAPSE = auto()
    FRACTAL_NODE = auto()
    RECURSIVE_NODE = auto()
    # Theoretical gates
    TACHYON_TRANSMITTER = auto()
    TACHYON_RECEIVER = auto()
    TEMPORAL_GATE = auto()
    QUANTUM_GATE = auto()
    
    @classmethod
    def basic_gates(cls):
        """Return list of basic gates."""
        return [cls.AND, cls.OR, cls.NOT, cls.NAND, cls.NOR, cls.XOR, cls.XNOR, cls.BUFFER]
    
    @classmethod
    def advanced_gates(cls):
        """Return list of advanced gates."""
        return [cls.MUX, cls.ADDER, cls.FLIP_FLOP, cls.LATCH, cls.REGISTER]
    
    @classmethod
    def neural_gates(cls):
        """Return list of neural-inspired gates."""
        return [cls.NEURON, cls.SYNAPSE]
    
    @classmethod
    def theoretical_gates(cls):
        """Return list of theoretical gates."""
        return [cls.FRACTAL_NODE, cls.RECURSIVE_NODE, cls.TACHYON_TRANSMITTER, 
               cls.TACHYON_RECEIVER, cls.TEMPORAL_GATE, cls.QUANTUM_GATE]

class CircuitNode:
    """Represents a single node (gate) in a circuit."""
    
    def __init__(self, id: int, gate_type: GateType):
        self.id = id
        self.gate_type = gate_type
        self.inputs: List[int] = []  # List of node IDs connected to inputs
        self.outputs: List[int] = []  # List of node IDs this node connects to
        self.properties: Dict[str, Any] = {}  # Additional properties for specialized gates
        
    def clone(self) -> 'CircuitNode':
        """Create a deep copy of this node."""
        new_node = CircuitNode(self.id, self.gate_type)
        new_node.inputs = copy.deepcopy(self.inputs)
        new_node.outputs = copy.deepcopy(self.outputs)
        new_node.properties = copy.deepcopy(self.properties)
        return new_node
        
    def evaluate(self, input_values: Dict[int, bool]) -> bool:
        """
        Evaluate this node based on its gate type and input values.
        
        Args:
            input_values: Dictionary mapping node IDs to their boolean values
            
        Returns:
            Boolean result of the gate operation
        """
        # Special gate types
        if self.gate_type == GateType.INPUT:
            return input_values.get(self.id, False)
            
        if self.gate_type == GateType.OUTPUT:
            if not self.inputs:
                return False
            return input_values.get(self.inputs[0], False)
            
        # Handle normal gate types
        if not self.inputs:
            return False
            
        input_vals = [input_values.get(input_id, False) for input_id in self.inputs]
        
        if self.gate_type == GateType.AND:
            return all(input_vals)
        elif self.gate_type == GateType.OR:
            return any(input_vals)
        elif self.gate_type == GateType.NOT:
            return not input_vals[0] if input_vals else False
        elif self.gate_type == GateType.NAND:
            return not all(input_vals)
        elif self.gate_type == GateType.NOR:
            return not any(input_vals)
        elif self.gate_type == GateType.XOR:
            return sum(input_vals) % 2 == 1
        elif self.gate_type == GateType.XNOR:
            return sum(input_vals) % 2 == 0
        elif self.gate_type == GateType.BUFFER:
            return input_vals[0] if input_vals else False
        elif self.gate_type == GateType.MUX:
            # MUX with select as first input, then data inputs
            if len(input_vals) >= 3:
                select = input_vals[0]
                return input_vals[2] if select else input_vals[1]
            return False
        elif self.gate_type == GateType.ADDER:
            # Simple binary addition (XOR of all inputs)
            return sum(input_vals) % 2 == 1
        
        # Advanced gate types
        elif self.gate_type == GateType.NEURON:
            # Simple threshold neuron
            threshold = self.properties.get("threshold", 0.5)
            weights = self.properties.get("weights", [1.0] * len(input_vals))
            
            weighted_sum = sum(w * float(v) for w, v in zip(weights[:len(input_vals)], input_vals))
            return weighted_sum >= threshold
            
        elif self.gate_type == GateType.SYNAPSE:
            # Synapse passes signal with weight
            weight = self.properties.get("weight", 1.0)
            return bool(weight * float(input_vals[0])) if input_vals else False
            
        # Theoretical gate types with simplified implementation
        elif self.gate_type == GateType.QUANTUM_GATE:
            # Simplified quantum gate that introduces randomness
            return random.random() < 0.5
        
        # Default for unhandled gate types
        return False
        
    def __str__(self) -> str:
        """String representation of the node."""
        return f"Node {self.id} ({self.gate_type.name}): inputs={self.inputs}, outputs={self.outputs}"

class Circuit:
    """Represents a complete circuit with nodes and connections."""
    
    def __init__(self, name: str = "Circuit"):
        self.name = name
        self.nodes: Dict[int, CircuitNode] = {}  # node_id -> node mapping
        self.inputs: List[int] = []  # Input node IDs
        self.outputs: List[int] = []  # Output node IDs
        self.evaluation_cache = {}  # Cache for evaluation results
        self.complexity = 0  # Measure of circuit complexity
        self.metadata: Dict[str, Any] = {}  # Metadata about the circuit
        
    def add_node(self, node: CircuitNode) -> int:
        """Add a node to the circuit and return its ID."""
        self.nodes[node.id] = node
        
        # Update input/output lists if needed
        if node.gate_type == GateType.INPUT and node.id not in self.inputs:
            self.inputs.append(node.id)
        elif node.gate_type == GateType.OUTPUT and node.id not in self.outputs:
            self.outputs.append(node.id)
            
        # Update complexity
        self.update_complexity()
            
        return node.id
        
    def connect(self, from_id: int, to_id: int) -> bool:
        """
        Connect two nodes in the circuit.
        
        Args:
            from_id: ID of the source node
            to_id: ID of the destination node
            
        Returns:
            True if connection was successful, False otherwise
        """
        if from_id not in self.nodes or to_id not in self.nodes:
            return False
            
        from_node = self.nodes[from_id]
        to_node = self.nodes[to_id]
        
        # Don't connect if already connected
        if to_id in from_node.outputs or from_id in to_node.inputs:
            return False
            
        # Add connection
        from_node.outputs.append(to_id)
        to_node.inputs.append(from_id)
        
        # Update complexity
        self.update_complexity()
        
        return True
        
    def disconnect(self, from_id: int, to_id: int) -> bool:
        """
        Remove a connection between two nodes.
        
        Args:
            from_id: ID of the source node
            to_id: ID of the destination node
            
        Returns:
            True if disconnection was successful, False otherwise
        """
        if from_id not in self.nodes or to_id not in self.nodes:
            return False
            
        from_node = self.nodes[from_id]
        to_node = self.nodes[to_id]
        
        # Remove connection if it exists
        if to_id in from_node.outputs and from_id in to_node.inputs:
            from_node.outputs.remove(to_id)
            to_node.inputs.remove(from_id)
            
            # Update complexity
            self.update_complexity()
            
            return True
            
        return False
        
    def remove_node(self, node_id: int) -> bool:
        """
        Remove a node from the circuit and all its connections.
        
        Args:
            node_id: ID of the node to remove
            
        Returns:
            True if removal was successful, False if node doesn't exist
        """
        if node_id not in self.nodes:
            return False
            
        node = self.nodes[node_id]
        
        # Remove connections to this node
        for input_id in node.inputs:
            if input_id in self.nodes:
                input_node = self.nodes[input_id]
                if node_id in input_node.outputs:
                    input_node.outputs.remove(node_id)
                    
        # Remove connections from this node
        for output_id in node.outputs:
            if output_id in self.nodes:
                output_node = self.nodes[output_id]
                if node_id in output_node.inputs:
                    output_node.inputs.remove(node_id)
                    
        # Remove from inputs/outputs lists if needed
        if node_id in self.inputs:
            self.inputs.remove(node_id)
        if node_id in self.outputs:
            self.outputs.remove(node_id)
            
        # Remove the node
        del self.nodes[node_id]
        
        # Update complexity
        self.update_complexity()
        
        return True
        
    def clear_cache(self):
        """Clear the evaluation cache."""
        self.evaluation_cache = {}
        
    def clone(self) -> 'Circuit':
        """Create a deep copy of this circuit."""
        new_circuit = Circuit(self.name)
        new_circuit.inputs = copy.deepcopy(self.inputs)
        new_circuit.outputs = copy.deepcopy(self.outputs)
        new_circuit.metadata = copy.deepcopy(self.metadata)
        
        # Clone all nodes
        for node_id, node in self.nodes.items():
            new_circuit.nodes[node_id] = node.clone()
            
        # Update complexity
        new_circuit.update_complexity()
        
        return new_circuit
        
    def update_complexity(self):
        """Calculate and update the complexity measure of the circuit."""
        # Basic complexity is the number of nodes plus connections
        nodes_count = len(self.nodes)
        connections_count = sum(len(node.outputs) for node in self.nodes.values())
        
        # Weighted by gate type complexity
        gate_complexity = 0
        for node in self.nodes.values():
            if node.gate_type in [GateType.INPUT, GateType.OUTPUT, GateType.BUFFER]:
                gate_complexity += 1
            elif node.gate_type in [GateType.AND, GateType.OR, GateType.NOT, GateType.XOR]:
                gate_complexity += 2
            elif node.gate_type in [GateType.NAND, GateType.NOR, GateType.XNOR]:
                gate_complexity += 3
            elif node.gate_type in [GateType.MUX, GateType.ADDER]:
                gate_complexity += 4
            elif node.gate_type in [GateType.FLIP_FLOP, GateType.LATCH, GateType.REGISTER]:
                gate_complexity += 5
            elif node.gate_type in [GateType.NEURON, GateType.SYNAPSE]:
                gate_complexity += 10
            elif node.gate_type in [GateType.FRACTAL_NODE, GateType.RECURSIVE_NODE]:
                gate_complexity += 20
            else:  # Theoretical gates
                gate_complexity += 30
                
        # Circuit structure complexity (e.g., feedback loops)
        structure_complexity = self._calculate_feedback_complexity()
        
        # Combine to get overall complexity
        self.complexity = nodes_count + connections_count + gate_complexity + structure_complexity
        
    def _calculate_feedback_complexity(self) -> int:
        """Calculate complexity contribution from feedback loops."""
        # Simple check for cycles
        visited = set()
        recursion_stack = set()
        
        def dfs_check_cycle(node_id):
            if node_id in visited:
                return False  # Prevent revisiting nodes
            visited.add(node_id)
            recursion_stack.add(node_id)
            
            node = self.nodes[node_id]
            for neighbor_id in node.outputs:
                if neighbor_id not in visited:
                    if dfs_check_cycle(neighbor_id):
                        return True
                elif neighbor_id in recursion_stack:
                    return True
                    
            recursion_stack.remove(node_id)
            return False
            
        cycle_count = 0
        for node_id in self.nodes:
            if node_id not in visited:
                if dfs_check_cycle(node_id):
                    cycle_count += 1
                    
        return cycle_count * 5  # Each cycle adds 5 to complexity
        
    def evaluate(self, input_values: Dict[int, bool]) -> Dict[int, bool]:
        """
        Evaluate the circuit with the given input values.
        
        Args:
            input_values: Dictionary mapping input node IDs to boolean values
            
        Returns:
            Dictionary mapping node IDs to their evaluated boolean values
        """
        # Check cache for this input combination
        cache_key = tuple(sorted((k, v) for k, v in input_values.items()))
        if cache_key in self.evaluation_cache:
            return self.evaluation_cache[cache_key]
            
        # Initialize result with input values
        result = dict(input_values)
        
        # Find evaluation order (topological sort)
        visited = set(input_values.keys())
        eval_order = list(input_values.keys())
        
        # Helper function for topological sort
        def visit(node_id):
            if node_id in visited:
                return  # Prevent revisiting nodes
            visited.add(node_id)
            eval_order.append(node_id)
            
            # First visit all inputs
            for input_id in self.nodes[node_id].inputs:
                if input_id not in visited:
                    visit(input_id)
                    
        # Start visiting from output nodes
        for output_id in self.outputs:
            visit(output_id)
            
        # Evaluate nodes in topological order
        for node_id in eval_order:
            node = self.nodes[node_id]
            result[node_id] = node.evaluate(result)
            
        # Cache the result
        self.evaluation_cache[cache_key] = result
        
        return result
        
    def get_output_values(self, input_values: Dict[int, bool]) -> Dict[int, bool]:
        """
        Get only the output values from circuit evaluation.
        
        Args:
            input_values: Dictionary mapping input node IDs to boolean values
            
        Returns:
            Dictionary mapping output node IDs to their evaluated boolean values
        """
        full_result = self.evaluate(input_values)
        return {output_id: full_result.get(output_id, False) for output_id in self.outputs}
        
    def evaluate_truth_table(self) -> Dict[Tuple[bool, ...], Tuple[bool, ...]]:
        """
        Evaluate the circuit for all possible input combinations (truth table).
        
        Returns:
            Dictionary mapping input tuples to output tuples
        """
        truth_table = {}
        
        # Generate all possible input combinations
        input_count = len(self.inputs)
        for i in range(2 ** input_count):
            # Convert number to binary digits
            binary = [(i >> bit) & 1 for bit in range(input_count)]
            
            # Create input dictionary
            input_values = {self.inputs[j]: bool(binary[j]) for j in range(input_count)}
            
            # Evaluate circuit
            output_values = self.get_output_values(input_values)
            output_tuple = tuple(output_values.get(output_id, False) for output_id in self.outputs)
            
            # Add to truth table
            input_tuple = tuple(input_values[input_id] for input_id in self.inputs)
            truth_table[input_tuple] = output_tuple
            
        return truth_table
        
    def get_next_node_id(self) -> int:
        """Get the next available node ID."""
        return max(self.nodes.keys(), default=0) + 1
        
    def __str__(self) -> str:
        """String representation of the circuit."""
        parts = [f"Circuit: {self.name}", f"Inputs: {self.inputs}", f"Outputs: {self.outputs}",
                f"Nodes: {len(self.nodes)}", f"Complexity: {self.complexity}", "Nodes:"]
                
        for node_id, node in sorted(self.nodes.items()):
            parts.append(f"  {node}")
            
        return "\n".join(parts)

class CircuitEvolution:
    """Handles the evolution of circuits using genetic algorithms."""
    
    def __init__(self, initial_population: List[Circuit], fitness_function: Callable[[Circuit], float],
                population_size: int = 100, mutation_rate: float = 0.1, crossover_rate: float = 0.7,
                allowed_gates: Optional[List[GateType]] = None):
        self.population = initial_population[:population_size]
        self.fitness_function = fitness_function
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.generation = 0
        self.best_fitness = float('-inf')
        self.best_circuit = None
        self.fitness_history = []
        self.allowed_gates = allowed_gates or GateType.basic_gates()
        
    def evolve(self, generations: int = 100, callback: Optional[Callable[[int, Circuit, float], None]] = None) -> Circuit:
        """
        Evolve the population for the given number of generations.
        
        Args:
            generations: Number of generations to evolve
            callback: Optional function called after each generation with (generation, best_circuit, best_fitness)
            
        Returns:
            The best circuit from the final population
        """
        for gen in range(generations):
            self.generation = gen + 1
            
            # Evaluate fitness for all circuits
            fitness_scores = []
            for circuit in self.population:
                fitness = self.fitness_function(circuit)
                fitness_scores.append((circuit, fitness))
                
            # Sort by fitness (descending)
            fitness_scores.sort(key=lambda x: x[1], reverse=True)
            
            # Track best circuit
            best_circuit, best_fitness = fitness_scores[0]
            if best_fitness > self.best_fitness:
                self.best_fitness = best_fitness
                self.best_circuit = best_circuit.clone()
                
            # Record history
            avg_fitness = sum(score for _, score in fitness_scores) / len(fitness_scores)
            self.fitness_history.append({
                'generation': self.generation,
                'best_fitness': best_fitness,
                'avg_fitness': avg_fitness,
                'best_complexity': best_circuit.complexity
            })
            
            # Call callback if provided
            if callback:
                callback(self.generation, best_circuit, best_fitness)
                
            # Create new population
            new_population = []
            
            # Elitism: keep the best circuits
            elite_count = max(1, int(self.population_size * 0.1))
            for i in range(elite_count):
                new_population.append(fitness_scores[i][0].clone())
                
            # Fill the rest with offspring
            while len(new_population) < self.population_size:
                # Selection
                parent1 = self._selection(fitness_scores)
                parent2 = self._selection(fitness_scores)
                
                # Crossover
                if random.random() < self.crossover_rate:
                    child1, child2 = self._crossover(parent1, parent2)
                else:
                    child1, child2 = parent1.clone(), parent2.clone()
                    
                # Mutation
                self._mutate(child1)
                self._mutate(child2)
                
                # Add to new population
                new_population.append(child1)
                if len(new_population) < self.population_size:
                    new_population.append(child2)
                    
            # Replace old population
            self.population = new_population
            
            # Log progress
            if gen % 10 == 0 or gen == generations - 1:
                logger.info(f"Generation {gen+1}/{generations}: Best fitness = {best_fitness:.4f}, "
                           f"Avg fitness = {avg_fitness:.4f}, Complexity = {best_circuit.complexity}")
            
        # Return best circuit after evolution
        return self.best_circuit
        
    def _selection(self, fitness_scores: List[Tuple[Circuit, float]]) -> Circuit:
        """
        Select a circuit from the population based on fitness.
        
        Args:
            fitness_scores: List of (circuit, fitness) tuples
            
        Returns:
            Selected circuit
        """
        # Tournament selection
        tournament_size = max(2, int(len(fitness_scores) * 0.1))
        tournament = random.sample(fitness_scores, tournament_size)
        winner = max(tournament, key=lambda x: x[1])[0]
        return winner
        
    def _crossover(self, parent1: Circuit, parent2: Circuit) -> Tuple[Circuit, Circuit]:
        """
        Perform crossover between two parent circuits.
        
        Args:
            parent1: First parent circuit
            parent2: Second parent circuit
            
        Returns:
            Two child circuits
        """
        child1 = Circuit(f"{parent1.name}_x_{parent2.name}")
        child2 = Circuit(f"{parent2.name}_x_{parent1.name}")
        
        # Map from old node IDs to new node IDs
        p1_map = {}
        p2_map = {}
        
        # Choose crossover point (percentage of nodes to take from each parent)
        crossover_point = random.uniform(0.3, 0.7)
        
        # Add input and output nodes first
        for input_id in sorted(parent1.inputs):
            node = parent1.nodes[input_id]
            new_id = child1.get_next_node_id()
            p1_map[input_id] = new_id
            
            new_node = CircuitNode(new_id, node.gate_type)
            child1.add_node(new_node)
            
        for output_id in sorted(parent1.outputs):
            node = parent1.nodes[output_id]
            new_id = child1.get_next_node_id()
            p1_map[output_id] = new_id
            
            new_node = CircuitNode(new_id, node.gate_type)
            child1.add_node(new_node)
            
        for input_id in sorted(parent2.inputs):
            node = parent2.nodes[input_id]
            new_id = child2.get_next_node_id()
            p2_map[input_id] = new_id
            
            new_node = CircuitNode(new_id, node.gate_type)
            child2.add_node(new_node)
            
        for output_id in sorted(parent2.outputs):
            node = parent2.nodes[output_id]
            new_id = child2.get_next_node_id()
            p2_map[output_id] = new_id
            
            new_node = CircuitNode(new_id, node.gate_type)
            child2.add_node(new_node)
            
        # Add other nodes from parents
        p1_nodes = [n for n in parent1.nodes.values() 
                   if n.id not in parent1.inputs and n.id not in parent1.outputs]
        p2_nodes = [n for n in parent2.nodes.values()
                   if n.id not in parent2.inputs and n.id not in parent2.outputs]
        
        # Shuffle to mix genes
        random.shuffle(p1_nodes)
        random.shuffle(p2_nodes)
        
        # Determine how many nodes to take from each parent
        p1_count = int(len(p1_nodes) * crossover_point)
        p2_count = int(len(p2_nodes) * crossover_point)
        
        # Add nodes to child1 (p1_count from parent1, rest from parent2)
        for node in p1_nodes[:p1_count]:
            new_id = child1.get_next_node_id()
            p1_map[node.id] = new_id
            
            new_node = CircuitNode(new_id, node.gate_type)
            new_node.properties = copy.deepcopy(node.properties)
            child1.add_node(new_node)
            
        for node in p2_nodes[p2_count:]:
            new_id = child1.get_next_node_id()
            p2_map[node.id] = new_id
            
            new_node = CircuitNode(new_id, node.gate_type)
            new_node.properties = copy.deepcopy(node.properties)
            child1.add_node(new_node)
            
        # Add nodes to child2 (p2_count from parent2, rest from parent1)
        for node in p2_nodes[:p2_count]:
            new_id = child2.get_next_node_id()
            p2_map[node.id] = new_id
            
            new_node = CircuitNode(new_id, node.gate_type)
            new_node.properties = copy.deepcopy(node.properties)
            child2.add_node(new_node)
            
        for node in p1_nodes[p1_count:]:
            new_id = child2.get_next_node_id()
            p1_map[node.id] = new_id
            
            new_node = CircuitNode(new_id, node.gate_type)
            new_node.properties = copy.deepcopy(node.properties)
            child2.add_node(new_node)
            
        # Add connections in child1
        for node_id, new_id in p1_map.items():
            node = parent1.nodes[node_id]
            for output_id in node.outputs:
                if output_id in p1_map:
                    child1.connect(new_id, p1_map[output_id])
                    
        for node_id, new_id in p2_map.items():
            node = parent2.nodes[node_id]
            for output_id in node.outputs:
                if output_id in p2_map:
                    child1.connect(new_id, p2_map[output_id])
                    
        # Add connections in child2
        for node_id, new_id in p2_map.items():
            node = parent2.nodes[node_id]
            for output_id in node.outputs:
                if output_id in p2_map:
                    child2.connect(new_id, p2_map[output_id])
                    
        for node_id, new_id in p1_map.items():
            node = parent1.nodes[node_id]
            for output_id in node.outputs:
                if output_id in p1_map:
                    child2.connect(new_id, p1_map[output_id])
                    
        return child1, child2
        
    def _mutate(self, circuit: Circuit) -> None:
        """
        Mutate a circuit by performing random changes.
        
        Args:
            circuit: Circuit to mutate
        """
        # Skip mutation based on rate
        if random.random() > self.mutation_rate:
            return
            
        # Choose mutation type
        mutation_type = random.choice(["add_node", "remove_node", "change_type", 
                                      "add_connection", "remove_connection"])
                                      
        if mutation_type == "add_node":
            # Add a new node
            new_id = circuit.get_next_node_id()
            gate_type = random.choice(self.allowed_gates)
                
            new_node = CircuitNode(new_id, gate_type)
            circuit.add_node(new_node)
            
            # Connect to existing nodes
            existing_nodes = list(circuit.nodes.keys())
            if existing_nodes:
                # Connect an input
                input_id = random.choice(existing_nodes)
                circuit.connect(input_id, new_id)
                
                # Connect an output
                output_id = random.choice(existing_nodes)
                circuit.connect(new_id, output_id)
                
        elif mutation_type == "remove_node":
            # Remove a random node (except inputs and outputs)
            removable