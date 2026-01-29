import numpy as np
import torch
import torch.nn as nn
from typing import Dict, List, Any
import random
import copy
import json
from datetime import datetime

class ArchitectureEvolver:
    def __init__(self, model_config: Dict[str, Any], seed: int = None):
        self.model_config = model_config
        self.evolution_history = []
        if seed is not None:
            np.random.seed(seed)
            random.seed(seed)
            torch.manual_seed(seed)
    
    def evolve_population(self, population_size: int = 10, num_generations: int = 5) -> Dict[str, Any]:
        """Evolve a population of architectures and return the best one."""
        population = [copy.deepcopy(self.model_config) for _ in range(population_size)]
        best_architecture = None
        best_fitness = float('-inf')
        
        for generation in range(num_generations):
            # Evaluate and sort population by fitness
            fitness_scores = [self.evaluate_architecture(arch) for arch in population]
            sorted_population = [x for _, x in sorted(zip(fitness_scores, population), reverse=True)]
            
            # Update best architecture
            generation_best_fitness = max(fitness_scores)
            if generation_best_fitness > best_fitness:
                best_fitness = generation_best_fitness
                best_architecture = copy.deepcopy(sorted_population[0])
            
            # Record evolution history
            self.evolution_history.append({
                'generation': generation,
                'best_fitness': generation_best_fitness,
                'avg_fitness': sum(fitness_scores) / len(fitness_scores),
                'best_architecture': copy.deepcopy(sorted_population[0])
            })
            
            # Keep top performers
            elite_size = max(1, population_size // 4)
            new_population = sorted_population[:elite_size]
            
            # Generate new architectures through mutation and crossover
            while len(new_population) < population_size:
                if random.random() < 0.7:  # 70% chance of mutation
                    parent = random.choice(sorted_population[:elite_size])
                    child = copy.deepcopy(parent)
                    self.mutate_architecture(child)
                    new_population.append(child)
                else:  # 30% chance of crossover
                    parent1, parent2 = random.sample(sorted_population[:elite_size], 2)
                    child = self.crossover_architectures(parent1, parent2)
                    new_population.append(child)
            
            population = new_population
        
        return best_architecture

    def save_evolution_history(self, path: str) -> None:
        """Save evolution history to a JSON file."""
        save_data = {
            'evolution_history': self.evolution_history,
            'timestamp': datetime.now().isoformat()
        }
        with open(path, 'w') as f:
            json.dump(save_data, f, indent=2)
    
    def mutate_architecture(self, architecture: Dict[str, Any]) -> None:
        """Apply random mutations to the architecture."""
        mutations = [
            self._mutate_num_experts,
            self._mutate_expert_hidden_size,
            self._mutate_num_attention_heads,
            self._mutate_layer_connectivity
        ]
        
        # Apply 1-3 random mutations
        num_mutations = random.randint(1, 3)
        for _ in range(num_mutations):
            mutation = random.choice(mutations)
            mutation(architecture)
    
    def _mutate_num_experts(self, architecture: Dict[str, Any]) -> None:
        """Mutate the number of experts."""
        min_experts = 2
        max_experts = 8
        architecture['num_experts'] = random.randint(min_experts, max_experts)
    
    def _mutate_expert_hidden_size(self, architecture: Dict[str, Any]) -> None:
        """Mutate the hidden size of experts."""
        sizes = [128, 256, 512, 1024]
        architecture['expert_hidden_size'] = random.choice(sizes)
    
    def _mutate_num_attention_heads(self, architecture: Dict[str, Any]) -> None:
        """Mutate the number of attention heads."""
        heads = [4, 8, 12, 16]
        architecture['num_attention_heads'] = random.choice(heads)
    
    def _mutate_layer_connectivity(self, architecture: Dict[str, Any]) -> None:
        """Mutate the connectivity pattern between layers."""
        num_layers = len(architecture.get('layer_connections', []))
        if num_layers < 2:
            return
            
        # Create a list of possible connections (avoiding self-loops and backward connections)
        possible_connections = []
        for i in range(num_layers):
            for j in range(i + 1, num_layers):
                possible_connections.append((i, j))
        
        if not possible_connections:
            return
            
        # Randomly select a connection to add or remove
        connection = random.choice(possible_connections)
        
        if 'layer_connections' not in architecture:
            architecture['layer_connections'] = []
            
        if connection in architecture['layer_connections']:
            architecture['layer_connections'].remove(connection)
        else:
            architecture['layer_connections'].append(connection)
    
    def crossover_architectures(self, arch1: Dict[str, Any], arch2: Dict[str, Any]) -> Dict[str, Any]:
        """Perform crossover between two architectures."""
        child = {}
        
        # Randomly inherit properties from parents
        for key in arch1.keys():
            if isinstance(arch1[key], (int, float, str)):
                child[key] = random.choice([arch1[key], arch2[key]])
            elif isinstance(arch1[key], list):
                # For lists (like layer connections), take a random subset from both parents
                combined = list(set(arch1[key] + arch2[key]))
                num_elements = random.randint(len(combined) // 2, len(combined))
                child[key] = random.sample(combined, num_elements)
            else:
                child[key] = copy.deepcopy(random.choice([arch1[key], arch2[key]]))
        
        return child
    
    def evaluate_architecture(self, architecture: Dict[str, Any]) -> float:
        """Evaluate the fitness of an architecture."""
        # Simple heuristic-based evaluation
        score = 0.0
        
        # Reward balanced architectures
        if 4 <= architecture['num_experts'] <= 6:
            score += 1.0
            
        # Reward efficient use of attention
        if architecture['expert_hidden_size'] >= 256 and architecture['num_attention_heads'] >= 8:
            score += 1.0
            
        # Reward connectivity (but not too much)
        num_connections = len(architecture.get('layer_connections', []))
        if num_connections > 0:
            score += min(1.0, num_connections / 10.0)
            
        # Add some random noise to prevent local optima
        score += random.uniform(-0.1, 0.1)
        
        return score
