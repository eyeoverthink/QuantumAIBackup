

    def to_dict(self):
        """Convert circuit to dictionary for serialization"""
        return {
            "name": self.name,
            "nodes": {str(node_id): node.to_dict() for node_id, node in self.nodes.items()},
            "inputs": self.inputs,
            "outputs": self.outputs,
            "next_node_id": self.next_node_id,
            "generation": self.generation,
            "fitness": self.fitness,
            "complexity": self.complexity,
            "complexity_level": self.complexity_level.name,
            "metadata": self.metadata,
            "subcircuits": {str(sc_id): sc.to_dict() for sc_id, sc in self.subcircuits.items()},
            "recursion_depth": self.recursion_depth,
            "patterns": [pattern.name for pattern in self.patterns]
        }
        
    @classmethod
    def from_dict(cls, data):
        """Create circuit from dictionary"""
        circuit = cls(data["name"])
        
        # Basic properties
        circuit.inputs = data["inputs"]
        circuit.outputs = data["outputs"]
        circuit.next_node_id = data["next_node_id"]
        circuit.generation = data["generation"]
        circuit.fitness = data["fitness"]
        circuit.complexity = data["complexity"]
        circuit.complexity_level = ComplexityLevel[data["complexity_level"]]
        circuit.metadata = data["metadata"]
        circuit.recursion_depth = data["recursion_depth"]
        
        # Add nodes
        for node_id_str, node_data in data["nodes"].items():
            node_id = int(node_id_str)
            circuit.nodes[node_id] = CircuitNode.from_dict(node_data)
        
        # Add subcircuits (recursively)
        for sc_id_str, sc_data in data["subcircuits"].items():
            sc_id = int(sc_id_str)
            circuit.subcircuits[sc_id] = Circuit.from_dict(sc_data)
            circuit.subcircuits[sc_id].parent_circuit = circuit
        
        return circuit

    def save(self, filename):
        """Save circuit to file"""
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
            
    @classmethod
    def load(cls, filename):
        """Load circuit from file"""
        with open(filename, 'rb') as f:
            return pickle.load(f)
            
    def save_json(self, filename):
        """Save circuit as JSON"""
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)
            
    @classmethod
    def load_json(cls, filename):
        """Load circuit from JSON"""
        with open(filename, 'r') as f:
            data = json.load(f)
        return cls.from_dict(data)

    def mutate(self, mutation_rate=0.1):
        """Apply random mutations to the circuit"""
        # Copy the circuit
        mutated = copy.deepcopy(self)
        mutated.generation += 1
        
        # Mutations we can apply
        mutations = [
            self._mutate_add_node,
            self._mutate_remove_node,
            self._mutate_add_connection,
            self._mutate_remove_connection,
            self._mutate_change_gate_type,
            self._mutate_adjust_parameters
        ]
        
        # Apply mutations based on mutation rate
        for mutation_func in mutations:
            if random.random() < mutation_rate:
                mutation_func(mutated)
                
        # Recalculate complexity
        mutated.calculate_complexity()
        
        return mutated

    def _mutate_add_node(self, circuit):
        """Mutation: Add a new node"""
        # Choose a random gate type
        gate_types = list(GateType)
        gate_type = random.choice(gate_types)
        
        # Add the node
        node_id = circuit.add_node(gate_type)
        
        # If it's not an input or output, try to connect it
        if gate_type not in [GateType.INPUT, GateType.OUTPUT]:
            # Try to connect to random existing nodes
            if circuit.nodes:
                # Choose random source and target for connections
                if random.random() < 0.7 and circuit.nodes:
                    source_id = random.choice(list(circuit.nodes.keys()))
                    circuit.connect(source_id, node_id)
                    
                if random.random() < 0.7 and circuit.nodes:
                    target_id = random.choice(list(circuit.nodes.keys()))
                    circuit.connect(node_id, target_id)

    def _mutate_remove_node(self, circuit):
        """Mutation: Remove a random node"""
        # Don't remove if there are too few nodes
        if len(circuit.nodes) <= 3:
            return
            
        # Don't remove inputs or outputs
        removable_nodes = [node_id for node_id in circuit.nodes 
                        if node_id not in circuit.inputs and node_id not in circuit.outputs]
        
        if removable_nodes:
            node_id = random.choice(removable_nodes)
            circuit.remove_node(node_id)

    def _mutate_add_connection(self, circuit):
        """Mutation: Add a new connection between existing nodes"""
        if len(circuit.nodes) < 2:
            return
            
        # Try to find valid source and target nodes
        for _ in range(10):  # Try up to 10 times
            source_id = random.choice(list(circuit.nodes.keys()))
            target_id = random.choice(list(circuit.nodes.keys()))
            
            # Don't connect to self or from output or to input
            if (source_id != target_id and 
                source_id not in circuit.outputs and
                target_id not in circuit.inputs):
                
                # Check for existing connection
                if target_id not in circuit.nodes[source_id].outputs:
                    circuit.connect(source_id, target_id)
                    break

    def _mutate_remove_connection(self, circuit):
        """Mutation: Remove a random connection"""
        # Find all connections
        connections = []
        for node_id, node in circuit.nodes.items():
            for output_id in node.outputs:
                connections.append((node_id, output_id))
        
        if connections:
            source_id, target_id = random.choice(connections)
            circuit.disconnect(source_id, target_id)

    def _mutate_change_gate_type(self, circuit):
        """Mutation: Change the gate type of a random node"""
        # Don't modify inputs or outputs
        modifiable_nodes = [node_id for node_id in circuit.nodes 
                            if node_id not in circuit.inputs and node_id not in circuit.outputs]
        
        if modifiable_nodes:
            node_id = random.choice(modifiable_nodes)
            
            # Choose a new gate type that isn't INPUT or OUTPUT
            gate_types = [gt for gt in GateType if gt not in [GateType.INPUT, GateType.OUTPUT]]
            new_gate_type = random.choice(gate_types)
            
            circuit.nodes[node_id].gate_type = new_gate_type

    def _mutate_adjust_parameters(self, circuit):
        """Mutation: Adjust parameters of a random node"""
        if not circuit.nodes:
            return
            
        node_id = random.choice(list(circuit.nodes.keys()))
        node = circuit.nodes[node_id]
        
        # Adjust parameters based on gate type
        if node.gate_type == GateType.NEURON:
            # Adjust activation threshold
            node.activation_threshold = max(0.1, min(0.9, node.activation_threshold + random.uniform(-0.2, 0.2)))
            
            # Adjust weights
            for input_id in node.inputs:
                weight_key = str(input_id)
                if weight_key in node.weights:
                    node.weights[weight_key] = max(0.0, min(1.0, node.weights[weight_key] + random.uniform(-0.2, 0.2)))
        
        elif node.gate_type == GateType.SYNAPSE:
            # Adjust strength
            strength = node.parameters.get("strength", 0.5)
            node.parameters["strength"] = max(0.0, min(1.0, strength + random.uniform(-0.2, 0.2)))
        
        elif node.gate_type == GateType.QUANTUM_GATE:
            # Toggle collapsed state
            node.parameters["collapsed"] = not node.parameters.get("collapsed", True)
        
        elif node.gate_type in [GateType.TACHYON_TRANSMITTER, GateType.TACHYON_RECEIVER]:
            # Adjust temporal offset
            node.temporal_offset = max(-5, min(5, node.temporal_offset + random.randint(-2, 2)))

    def crossover(self, other_circuit):
        """Create a new circuit by combining this one with another"""
        # Create a new circuit
        child = Circuit(f"{self.name}x{other_circuit.name}")
        child.generation = max(self.generation, other_circuit.generation) + 1
        
        # Copy all nodes from both parents
        # For simplicity, we'll use node IDs directly, but in a real implementation
        # you'd want to remap them to avoid conflicts
        
        # Randomly choose which nodes to include
        for node_id, node in self.nodes.items():
            if random.random() < 0.5:  # 50% chance to include each node
                child.nodes[node_id] = copy.deepcopy(node)
        
        for node_id, node in other_circuit.nodes.items():
            if node_id not in child.nodes and random.random() < 0.5:
                child.nodes[node_id] = copy.deepcopy(node)
        
        # Make sure we have the necessary input and output nodes
        for input_id in self.inputs:
            if input_id not in child.nodes:
                child.nodes[input_id] = copy.deepcopy(self.nodes[input_id])
                
        for output_id in self.outputs:
            if output_id not in child.nodes:
                child.nodes[output_id] = copy.deepcopy(self.nodes[output_id])
        
        # Update child's inputs and outputs
        child.inputs = list(set(child.inputs + self.inputs))
        child.outputs = list(set(child.outputs + self.outputs))
        
        # Make sure connections point to existing nodes
        for node_id, node in list(child.nodes.items()):
            # Filter inputs
            node.inputs = [input_id for input_id in node.inputs if input_id in child.nodes]
            
            # Filter outputs
            node.outputs = [output_id for output_id in node.outputs if output_id in child.nodes]
        
        # Set next node ID
        child.next_node_id = max(child.nodes.keys()) + 1 if child.nodes else 0
        
        # Calculate complexity
        child.calculate_complexity()
        
        return child

    def generate_code(self):
        """Generate Python code representation of this circuit"""
        lines = []
        lines.append("# Generated Circuit Code")
        lines.append(f"# Name: {self.name}")
        lines.append(f"# Complexity: {self.complexity}")
        lines.append(f"# Generation: {self.generation}")
        lines.append("")
        
        lines.append("def build_circuit():")
        lines.append("    # Create new circuit")
        lines.append(f"    circuit = Circuit(\"{self.name}\")")
        lines.append("")
        
        # Add nodes
        lines.append("    # Add nodes")
        for node_id, node in sorted(self.nodes.items()):
            lines.append(f"    node_{node_id} = circuit.add_node(GateType.{node.gate_type.name})")
            
            # Add node parameters if any
            if node.parameters:
                for key, value in node.parameters.items():
                    lines.append(f"    circuit.nodes[node_{node_id}].parameters[\"{key}\"] = {value}")
                    
            # Add weights if any
            if node.weights:
                for input_id, weight in node.weights.items():
                    lines.append(f"    circuit.nodes[node_{node_id}].weights[\"{input_id}\"] = {weight}")
        
        lines.append("")
        
        # Add connections
        lines.append("    # Add connections")
        for node_id, node in sorted(self.nodes.items()):
            for output_id in node.outputs:
                lines.append(f"    circuit.connect({node_id}, {output_id})")
        
        lines.append("")
        lines.append("    return circuit")
        
        self.code_representation = "\n".join(lines)
        return self.code_representation

    def visualize(self, filename=None):
        """Visualize the circuit using matplotlib"""
        import networkx as nx
        import matplotlib.pyplot as plt
        
        # Create a graph
        G = nx.DiGraph()
        
        # Add nodes
        colors = []
        for node_id, node in self.nodes.items():
            G.add_node(node_id)
            
            # Assign colors based on gate type
            if node.gate_type == GateType.INPUT:
                colors.append('green')
            elif node.gate_type == GateType.OUTPUT:
                colors.append('red')
            elif node.gate_type in [GateType.NEURON, GateType.SYNAPSE, 
                                GateType.DENDRITE, GateType.AXON]:
                colors.append('purple')
            elif node.gate_type in [GateType.FRACTAL_NODE, GateType.RECURSIVE_NODE]:
                colors.append('blue')
            elif node.gate_type in [GateType.TACHYON_TRANSMITTER, GateType.TACHYON_RECEIVER,
                                GateType.TEMPORAL_GATE, GateType.QUANTUM_GATE]:
                colors.append('cyan')
            else:
                colors.append('gray')
        
        # Add edges
        for node_id, node in self.nodes.items():
            for output_id in node.outputs:
                G.add_edge(node_id, output_id)
        
        # Create plot
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(G, seed=42)
        nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=500)
        nx.draw_networkx_edges(G, pos, width=1.0, arrowsize=15)
        nx.draw_networkx_labels(G, pos)
        
        plt.title(f"Circuit: {self.name} (Complexity: {self.complexity})")
        plt.axis('off')
        
        if filename:
            plt.savefig(filename)
        else:
            plt.show()


class CircuitEvolution:
    """Manages the evolution of circuits using genetic algorithms"""
    
    def __init__(self, population_size=50, mutation_rate=0.2, elite_size=5):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.elite_size = elite_size
        self.generation = 0
        self.population = []
        self.best_circuit = None
        self.fitness_history = []
        
    def initialize_population(self, template_circuit, variations=10):
        """Initialize population with variations of the template circuit"""
        self.population = [template_circuit]
        
        # Create variations
        for _ in range(self.population_size - 1):
            # Start with a copy of the template
            circuit = copy.deepcopy(template_circuit)
            
            # Apply random mutations
            for _ in range(variations):
                circuit = circuit.mutate(self.mutation_rate)
                
            circuit.name = f"Gen0_Circuit{_}"
            self.population.append(circuit)
            
        self.generation = 0
        
    def evaluate_fitness(self, fitness_function):
        """Evaluate fitness of all circuits using the provided function"""
        for circuit in self.population:
            circuit.fitness = fitness_function(circuit)
            
        # Sort population by fitness (descending)
        self.population.sort(key=lambda c: c.fitness, reverse=True)
        
        # Update best circuit
        if not self.best_circuit or self.population[0].fitness > self.best_circuit.fitness:
            self.best_circuit = copy.deepcopy(self.population[0])
            
        # Record average fitness
        avg_fitness = sum(circuit.fitness for circuit in self.population) / len(self.population)
        self.fitness_history.append((self.generation, avg_fitness, self.population[0].fitness))
        
    def select_parent(self):
        """Select a parent using tournament selection"""
        tournament_size = 3
        tournament = random.sample(self.population, tournament_size)
        return max(tournament, key=lambda circuit: circuit.fitness)
        
    def evolve_generation(self):
        """Create a new generation through selection, crossover, and mutation"""
        new_population = []
        
        # Keep elite circuits
        elite_count = min(self.elite_size, len(self.population))
        new_population.extend(copy.deepcopy(self.population[:elite_count]))
        
        # Create the rest through crossover and mutation
        while len(new_population) < self.population_size:
            # Select parents
            parent1 = self.select_parent()
            parent2 = self.select_parent()
            
            # Create child through crossover
            child = parent1.crossover(parent2)
            
            # Apply mutation
            if random.random() < self.mutation_rate:
                child = child.mutate(self.mutation_rate)
                
            child.name = f"Gen{self.generation + 1}_Circuit{len(new_population)}"
            new_population.append(child)
            
        self.population = new_population
        self.generation += 1
        
    def run_evolution(self, fitness_function, generations=100, target_fitness=None):
        """Run the evolutionary algorithm for a number of generations"""
        for generation in range(generations):
            # Evaluate fitness
            self.evaluate_fitness(fitness_function)
            
            # Log progress
            best_fitness = self.population[0].fitness
            avg_fitness = sum(circuit.fitness for circuit in self.population) / len(self.population)
            logger.info(f"Generation {self.generation}: Best fitness = {best_fitness:.4f}, Avg fitness = {avg_fitness:.4f}")
            
            # Check if we've reached target fitness
            if target_fitness is not None and best_fitness >= target_fitness:
                logger.info(f"Target fitness reached at generation {self.generation}")
                break
                
            # Create next generation
            self.evolve_generation()
            
        # Final evaluation
        self.evaluate_fitness(fitness_function)
        return self.best_circuit
        
    def plot_fitness_history(self, filename=None):
        """Plot the fitness history"""
        if not self.fitness_history:
            return
            
        generations, avg_fitness, best_fitness = zip(*self.fitness_history)
        
        plt.figure(figsize=(10, 6))
        plt.plot(generations, avg_fitness, label='Average Fitness')
        plt.plot(generations, best_fitness, label='Best Fitness')
        plt.xlabel('Generation')
        plt.ylabel('Fitness')
        plt.title('Fitness over Generations')
        plt.legend()
        plt.grid(True)
        
        if filename:
            plt.savefig(filename)
        else:
            plt.show()


def create_template_circuit(input_size=2, output_size=1, hidden_layers=1, nodes_per_layer=3):
    """Create a template circuit with the specified architecture"""
    circuit = Circuit("Template")
    
    # Add input nodes
    input_nodes = []
    for i in range(input_size):
        node_id = circuit.add_node(GateType.INPUT)
        input_nodes.append(node_id)
    
    # Add hidden layers
    prev_layer = input_nodes
    
    for layer in range(hidden_layers):
        current_layer = []
        
        for i in range(nodes_per_layer):
            # Alternate between different gate types for variety
            if i % 5 == 0:
                gate_type = GateType.AND
            elif i % 5 == 1:
                gate_type = GateType.OR
            elif i % 5 == 2:
                gate_type = GateType.XOR
            elif i % 5 == 3:
                gate_type = GateType.NAND
            else:
                gate_type = GateType.NOR
                
            node_id = circuit.add_node(gate_type)
            current_layer.append(node_id)
            
            # Connect to all nodes in previous layer
            for prev_id in prev_layer:
                circuit.connect(prev_id, node_id)
        
        prev_layer = current_layer
    
    # Add output nodes
    output_nodes = []
    for i in range(output_size):
        node_id = circuit.add_node(GateType.OUTPUT)
        output_nodes.append(node_id)
        
        # Connect all nodes from last hidden layer to this output
        for prev_id in prev_layer:
            circuit.connect(prev_id, node_id)
    
    # Calculate complexity
    circuit.calculate_complexity()
    
    return circuit

def create_xor_fitness_function():
    """Create a fitness function for the XOR problem"""
    
    def fitness_function(circuit):
        # XOR training data
        training_data = [
            ([False, False], [False]),
            ([False, True], [True]),
            ([True, False], [True]),
            ([True, True], [False])
        ]
        
        # Count correct outputs
        correct = 0
        for inputs, expected in training_data:
            outputs = circuit.simulate(inputs)
            if outputs == expected:
                correct += 1
                
        # Base fitness on correct count
        fitness = correct / len(training_data)
        
        # Penalty for complexity
        complexity_penalty = 0.01 * circuit.complexity / 100
        fitness = max(0, fitness - complexity_penalty)
        
        return fitness
        
    return fitness_function

def create_adder_fitness_function():
    """Create a fitness function for a binary adder"""
    
    def fitness_function(circuit):
        # Training data for a full adder (2 bits + carry in, outputs sum + carry out)
        training_data = [
            ([False, False, False], [False, False]),  # 0 + 0 + 0 = 0, carry 0
            ([False, False, True], [True, False]),    # 0 + 0 + 1 = 1, carry 0
            ([False, True, False], [True, False]),    # 0 + 1 + 0 = 1, carry 0
            ([False, True, True], [False, True]),     # 0 + 1 + 1 = 0, carry 1
            ([True, False, False], [True, False]),    # 1 + 0 + 0 = 1, carry 0
            ([True, False, True], [False, True]),     # 1 + 0 + 1 = 0, carry 1
            ([True, True, False], [False, True]),     # 1 + 1 + 0 = 0, carry 1
            ([True, True, True], [True, True])        # 1 + 1 + 1 = 1, carry 1
        ]
        
        # Count correct outputs
        correct_sum = 0
        correct_carry = 0
        
        for inputs, expected in training_data:
            outputs = circuit.simulate(inputs)
            
            if len(outputs) >= 1 and outputs[0] == expected[0]:
                correct_sum += 1
                
            if len(outputs) >= 2 and outputs[1] == expected[1]:
                correct_carry += 1
                
        # Calculate fitness based on correctness
        fitness = (correct_sum + correct_carry) / (2 * len(training_data))
        
        # Penalty for excessive complexity
        complexity_penalty = 0.01 * circuit.complexity / 100
        fitness = max(0, fitness - complexity_penalty)
        
        return fitness
        
    return fitness_function

def run_xor_example():
    """Example: Evolve a circuit to solve the XOR problem"""
    logger.info("Running XOR example...")
    
    # Create template circuit
    template = create_template_circuit(input_size=2, output_size=1, hidden_layers=1, nodes_per_layer=3)
    
    # Create evolution manager
    evolution = CircuitEvolution(population_size=100, mutation_rate=0.2, elite_size=10)
    evolution.initialize_population(template)
    
    # Create fitness function
    fitness_function = create_xor_fitness_function()
    
    # Run evolution
    best_circuit = evolution.run_evolution(fitness_function, generations=50, target_fitness=0.99)
    
    # Test the best circuit
    logger.info("Testing best circuit:")
    
    for inputs in [[False, False], [False, True], [True, False], [True, True]]:
        outputs = best_circuit.simulate(inputs)
        logger.info(f"Inputs: {inputs}, Output: {outputs}")
    
    # Save results
    best_circuit.save("xor_circuit.pkl")
    evolution.plot_fitness_history("xor_fitness.png")
    best_circuit.visualize("xor_circuit.png")
    
    return best_circuit

def run_neural_circuit_example():
    """Example: Evolve a neural-like circuit for pattern recognition"""
    logger.info("Running neural circuit example...")
    
    # Create template circuit with some neural components
    circuit = Circuit("NeuralTemplate")
    
    # Add input nodes
    input_nodes = []
    for i in range(4):
        node_id = circuit.add_node(GateType.INPUT)
        input_nodes.append(node_id)
    
    # Add hidden layer with neurons
    hidden_nodes = []
    for i in range(3):
        node_id = circuit.add_node(GateType.NEURON)
        hidden_nodes.append(node_id)
        
        # Connect all inputs to this neuron with random weights
        for input_id in input_nodes:
            circuit.connect(input_id, node_id)
            weight_key = str(input_id)
            circuit.nodes[node_id].weights[weight_key] = random.uniform(0.1, 0.9)
    
    # Add output neuron
    output_id = circuit.add_node(GateType.OUTPUT)
    
    # Connect hidden nodes to output
    for hidden_id in hidden_nodes:
        circuit.connect(hidden_id, output_id)
    
    # Calculate complexity
    circuit.calculate_complexity()
    
    # Create patterns for recognition (e.g., detecting if there are more 1s than 0s)
    patterns = []
    for _ in range(20):
        inputs = [random.choice([True, False]) for _ in range(4)]
        expected = [sum(inputs) > 2]  # True if more than half are True
        patterns.append((inputs, expected))
    
    # Create evolution manager
    evolution = CircuitEvolution(population_size=150, mutation_rate=0.25, elite_size=15)
    evolution.initialize_population(circuit)
    
    # Create fitness function
    fitness_function = create_pattern_recognition_fitness_function(patterns)
    
    # Run evolution
    best_circuit = evolution.run_evolution(fitness_function, generations=50, target_fitness=0.95)
    
    # Test the best circuit
    logger.info("Testing best neural circuit:")
    
    for i, (inputs, expected) in enumerate(patterns[:5]):  # Test first 5 patterns
        outputs = best_circuit.simulate(inputs)
        logger.info(f"Pattern {i}: Inputs: {inputs}, Expected: {expected}, Output: {outputs}")
    
    # Save results
    best_circuit.save("neural_circuit.pkl")
    evolution.plot_fitness_history("neural_fitness.png")
    best_circuit.visualize("neural_circuit.png")
    
    return best_circuit

def create_pattern_recognition_fitness_function(patterns):
    """Create a fitness function for recognizing specific input patterns"""
    
    def fitness_function(circuit):
        correct = 0
        
        for inputs, expected in patterns:
            outputs = circuit.simulate(inputs)
            
            if outputs[0] == expected[0]:
                correct += 1
                
        fitness = correct / len(patterns)
        
        # Small bonus for neural components
        neural_count = sum(1 for node in circuit.nodes.values() 
                          if node.gate_type in [GateType.NEURON, GateType.SYNAPSE])
        neural_bonus = 0.01 * neural_count / len(circuit.nodes) if circuit.nodes else 0
        
        # Penalty for excessive complexity
        complexity_penalty = 0.01 * circuit.complexity / 100
        
        fitness = min(1.0, fitness + neural_bonus - complexity_penalty)
        
        return fitness
        
    return fitness_function

def run_fractal_circuit_example():
    """Example: Create and visualize a fractal circuit"""
    logger.info("Running fractal circuit example...")
    
    # Create a simple seed circuit
    seed = Circuit("FractalSeed")
    
    # Add nodes to seed
    input_id = seed.add_node(GateType.INPUT)
    fractal_id = seed.add_node(GateType.FRACTAL_NODE)
    output_id = seed.add_node(GateType.OUTPUT)
    
    # Connect nodes
    seed.connect(input_id, fractal_id)
    seed.connect(fractal_id, output_id)
    
    # Create a fractal pattern
    pattern = FractalPattern("SimpleFractal", seed, max_depth=3)
    
    # Create a base circuit
    circuit = Circuit("FractalCircuit")
    
    # Add nodes
    input_id = circuit.add_node(GateType.INPUT)
    fractal_id = circuit.add_node(GateType.FRACTAL_NODE)
    output_id = circuit.add_node(GateType.OUTPUT)
    
    # Connect nodes
    circuit.connect(input_id, fractal_id)
    circuit.connect(fractal_id, output_id)
    
    # Apply fractal pattern
    pattern.apply_to_circuit(circuit, fractal_id)
    
    # Calculate complexity
    circuit.calculate_complexity()
    
    logger.info(f"Fractal circuit complexity: {circuit.complexity}")
    
    # Visualize
    circuit.visualize("fractal_circuit.png")
    
    return circuit

def run_tachyon_circuit_example():
    """Example: Create a circuit with tachyon-inspired components"""
    logger.info("Running tachyon circuit example...")
    
    circuit = Circuit("TachyonCircuit")
    
    # Add nodes
    input_id = circuit.add_node(GateType.INPUT)
    
    # Add tachyon transmitter and receiver
    transmitter_id = circuit.add_node(GateType.TACHYON_TRANSMITTER)
    receiver_id = circuit.add_node(GateType.TACHYON_RECEIVER)
    
    # Add temporal gate
    temporal_id = circuit.add_node(GateType.TEMPORAL_GATE)
    
    # Add output
    output_id = circuit.add_node(GateType.OUTPUT)
    
    # Connect nodes
    circuit.connect(input_id, transmitter_id)
    circuit.connect(input_id, temporal_id)
    circuit.connect(transmitter_id, receiver_id)
    circuit.connect(receiver_id, temporal_id)
    circuit.connect(temporal_id, output_id)
    
    # Set up entanglement between transmitter and receiver
    circuit.nodes[transmitter_id].entangled_nodes.append(receiver_id)
    circuit.nodes[receiver_id].entangled_nodes.append(transmitter_id)
    
    # Set temporal offset for receiver (looks into the "past")
    circuit.nodes[receiver_id].temporal_offset = -1
    
    # Calculate complexity
    circuit.calculate_complexity()
    
    logger.info(f"Tachyon circuit complexity: {circuit.complexity}")
    
    # Visualize
    circuit.visualize("tachyon_circuit.png")
    
    # Test the circuit
    logger.info("Testing tachyon circuit (results are theoretical):")
    
    # Simulate with multiple steps to allow temporal effects
    inputs_sequence = [[False], [True], [False], [True], [True]]
    
    for i, inputs in enumerate(inputs_sequence):
        outputs = circuit.simulate(inputs, steps=3, use_tachyon=True)
        logger.info(f"Step {i}: Inputs: {inputs}, Outputs: {outputs}")
    
    return circuit

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="MetaCircuit Evolution")
    parser.add_argument('--example', type=str, choices=['xor', 'adder', 'neural', 'fractal', 'tachyon', 'all'],
                      default='xor', help='Example to run')
    args = parser.parse_args()
    
    logger.info("Starting MetaCircuit Evolution")
    
    if args.example == 'xor' or args.example == 'all':
        run_xor_example()
        
    if args.example == 'adder' or args.example == 'all':
        run_adder_fitness_function()
        
    if args.example == 'neural' or args.example == 'all':
        run_neural_circuit_example()
        
    if args.example == 'fractal' or args.example == 'all':
        run_fractal_circuit_example()
        
    if args.example == 'tachyon' or args.example == 'all':
        run_tachyon_circuit_example()
    
    logger.info("MetaCircuit Evolution completed")

if __name__ == "__main__":
    main()
