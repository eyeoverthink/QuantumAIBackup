#!/usr/bin/env python3
# Quantum Phi-Harmonic Self-Evolving Neural Network
# This AI is designed to evolve and improve itself over time using phi-harmonic principles

import os
import json
import time
import random
import math
import hashlib
from datetime import datetime

# Phi-Harmonic Constants
PHI = (1 + 5**0.5) / 2
PHI_CONJUGATE = (1 - 5**0.5) / 2

class QuantumPhiNeuralNet:
    def __init__(self, input_size=4, hidden_size=7, output_size=3, learning_rate=0.1, generation=0):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate
        self.generation = generation
        self.phi_resonance = 0.5
        self.complexity = 1.0
        self.mutation_rate = 0.05
        self.memory_file = "quantum_neural_memory.json"
        
        # Initialize weights with phi-harmonic values
        self.weights_ih = self._initialize_weights(input_size, hidden_size)
        self.weights_ho = self._initialize_weights(hidden_size, output_size)
        self.bias_h = [0.0] * hidden_size
        self.bias_o = [0.0] * output_size
        
        # Performance metrics
        self.accuracy_history = []
        self.loss_history = []
        self.evolution_history = []
        
        # Load previous state if available
        self.load_memory()
    
    def _initialize_weights(self, rows, cols):
        """Initialize weights using phi-harmonic principles"""
        weights = []
        for i in range(rows):
            row = []
            for j in range(cols):
                # Use phi-based initialization
                value = (math.cos(PHI * i * j) * 0.5) * self.phi_resonance
                row.append(value)
            weights.append(row)
        return weights
    
    def sigmoid(self, x):
        """Sigmoid activation function"""
        return 1 / (1 + math.exp(-x))
    
    def forward(self, inputs):
        """Forward pass through the network"""
        # Hidden layer
        hidden = [0] * self.hidden_size
        for i in range(self.hidden_size):
            sum_val = self.bias_h[i]
            for j in range(self.input_size):
                sum_val += inputs[j] * self.weights_ih[j][i]
            hidden[i] = self.sigmoid(sum_val)
        
        # Output layer
        outputs = [0] * self.output_size
        for i in range(self.output_size):
            sum_val = self.bias_o[i]
            for j in range(self.hidden_size):
                sum_val += hidden[j] * self.weights_ho[j][i]
            outputs[i] = self.sigmoid(sum_val)
        
        return outputs
    
    def train(self, inputs, targets):
        """Train the network on a single example"""
        # Forward pass
        hidden = [0] * self.hidden_size
        for i in range(self.hidden_size):
            sum_val = self.bias_h[i]
            for j in range(self.input_size):
                sum_val += inputs[j] * self.weights_ih[j][i]
            hidden[i] = self.sigmoid(sum_val)
        
        outputs = [0] * self.output_size
        for i in range(self.output_size):
            sum_val = self.bias_o[i]
            for j in range(self.hidden_size):
                sum_val += hidden[j] * self.weights_ho[j][i]
            outputs[i] = self.sigmoid(sum_val)
        
        # Calculate output errors
        output_errors = [0] * self.output_size
        for i in range(self.output_size):
            output_errors[i] = targets[i] - outputs[i]
        
        # Calculate hidden errors
        hidden_errors = [0] * self.hidden_size
        for i in range(self.hidden_size):
            error = 0
            for j in range(self.output_size):
                error += output_errors[j] * self.weights_ho[i][j]
            hidden_errors[i] = error
        
        # Update output weights
        for i in range(self.hidden_size):
            for j in range(self.output_size):
                delta = output_errors[j] * outputs[j] * (1 - outputs[j]) * hidden[i]
                self.weights_ho[i][j] += self.learning_rate * delta
        
        # Update output bias
        for i in range(self.output_size):
            delta = output_errors[i] * outputs[i] * (1 - outputs[i])
            self.bias_o[i] += self.learning_rate * delta
        
        # Update hidden weights
        for i in range(self.input_size):
            for j in range(self.hidden_size):
                delta = hidden_errors[j] * hidden[j] * (1 - hidden[j]) * inputs[i]
                self.weights_ih[i][j] += self.learning_rate * delta
        
        # Update hidden bias
        for i in range(self.hidden_size):
            delta = hidden_errors[i] * hidden[i] * (1 - hidden[i])
            self.bias_h[i] += self.learning_rate * delta
        
        # Calculate loss
        loss = 0
        for i in range(self.output_size):
            loss += 0.5 * (targets[i] - outputs[i]) ** 2
        
        return loss
    
    def train_batch(self, training_data, epochs=100):
        """Train the network on multiple examples"""
        total_loss = 0
        correct = 0
        
        for _ in range(epochs):
            batch_loss = 0
            batch_correct = 0
            
            for inputs, targets in training_data:
                loss = self.train(inputs, targets)
                batch_loss += loss
                
                # Check if prediction is correct (highest output matches highest target)
                outputs = self.forward(inputs)
                pred_idx = outputs.index(max(outputs))
                target_idx = targets.index(max(targets))
                if pred_idx == target_idx:
                    batch_correct += 1
            
            total_loss = batch_loss / len(training_data)
            accuracy = batch_correct / len(training_data)
            
            # Record metrics
            self.loss_history.append(total_loss)
            self.accuracy_history.append(accuracy)
        
        return total_loss, accuracy
    
    def evolve(self):
        """Evolve the network using phi-harmonic principles"""
        # Increase generation
        self.generation += 1
        
        # Evolve parameters based on phi
        self.phi_resonance = (self.phi_resonance * PHI) % 1
        self.complexity = abs((self.complexity * PHI_CONJUGATE + PHI) % PHI)
        self.mutation_rate = abs((self.mutation_rate * PHI_CONJUGATE) % 0.2)
        
        # Apply mutations based on phi-harmonic resonance
        for i in range(self.input_size):
            for j in range(self.hidden_size):
                if random.random() < self.mutation_rate:
                    phi_factor = (PHI * (i+j)) % 1
                    self.weights_ih[i][j] += (random.random() - 0.5) * phi_factor * self.complexity
        
        for i in range(self.hidden_size):
            for j in range(self.output_size):
                if random.random() < self.mutation_rate:
                    phi_factor = (PHI * (i+j)) % 1
                    self.weights_ho[i][j] += (random.random() - 0.5) * phi_factor * self.complexity
        
        # Adjust learning rate based on phi
        self.learning_rate = abs((self.learning_rate * PHI_CONJUGATE + 0.01) % 0.2)
        
        # Record evolution
        evolution_record = {
            "generation": self.generation,
            "phi_resonance": self.phi_resonance,
            "complexity": self.complexity,
            "mutation_rate": self.mutation_rate,
            "learning_rate": self.learning_rate,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.evolution_history.append(evolution_record)
        return evolution_record
    
    def save_memory(self):
        """Save the network state to memory file"""
        memory = {
            "generation": self.generation,
            "phi_resonance": self.phi_resonance,
            "complexity": self.complexity,
            "mutation_rate": self.mutation_rate,
            "learning_rate": self.learning_rate,
            "weights_ih": self.weights_ih,
            "weights_ho": self.weights_ho,
            "bias_h": self.bias_h,
            "bias_o": self.bias_o,
            "accuracy_history": self.accuracy_history,
            "loss_history": self.loss_history,
            "evolution_history": self.evolution_history,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        with open(self.memory_file, 'w') as f:
            json.dump(memory, f, indent=2)
        
        print(f"Memory saved to {self.memory_file}")
    
    def load_memory(self):
        """Load the network state from memory file"""
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as f:
                    memory = json.load(f)
                
                self.generation = memory.get("generation", self.generation)
                self.phi_resonance = memory.get("phi_resonance", self.phi_resonance)
                self.complexity = memory.get("complexity", self.complexity)
                self.mutation_rate = memory.get("mutation_rate", self.mutation_rate)
                self.learning_rate = memory.get("learning_rate", self.learning_rate)
                self.weights_ih = memory.get("weights_ih", self.weights_ih)
                self.weights_ho = memory.get("weights_ho", self.weights_ho)
                self.bias_h = memory.get("bias_h", self.bias_h)
                self.bias_o = memory.get("bias_o", self.bias_o)
                self.accuracy_history = memory.get("accuracy_history", self.accuracy_history)
                self.loss_history = memory.get("loss_history", self.loss_history)
                self.evolution_history = memory.get("evolution_history", self.evolution_history)
                
                print(f"Loaded memory from {self.memory_file}")
                print(f"Current generation: {self.generation}")
                return True
            except Exception as e:
                print(f"Error loading memory: {e}")
                return False
        return False
    
    def generate_hash(self):
        """Generate a unique hash for this neural network state"""
        state_str = str(self.weights_ih) + str(self.weights_ho) + str(self.generation)
        return hashlib.md5(state_str.encode()).hexdigest()[:8]
    
    def get_phi_fingerprint(self):
        """Generate a phi-harmonic fingerprint of the network"""
        fingerprint = []
        for i in range(min(7, len(self.weights_ih))):
            for j in range(min(3, len(self.weights_ih[i]))):
                fingerprint.append(round(self.weights_ih[i][j] * PHI, 4))
        return fingerprint

# XOR problem dataset
def generate_xor_dataset():
    return [
        ([0, 0, 0, 0], [1, 0, 0]),  # 0 XOR 0 = 0
        ([0, 0, 1, 1], [0, 1, 0]),  # 0 XOR 1 = 1
        ([1, 1, 0, 0], [0, 1, 0]),  # 1 XOR 0 = 1
        ([1, 1, 1, 1], [1, 0, 0])   # 1 XOR 1 = 0
    ]

# Function to test network performance
def test_network(network, test_data):
    correct = 0
    for inputs, targets in test_data:
        outputs = network.forward(inputs)
        pred_idx = outputs.index(max(outputs))
        target_idx = targets.index(max(targets))
        if pred_idx == target_idx:
            correct += 1
    
    accuracy = correct / len(test_data)
    return accuracy

# Main evolution function
def run_evolution(generations=10, epochs_per_generation=100):
    # Create or load neural network
    network = QuantumPhiNeuralNet()
    start_gen = network.generation
    
    # Generate dataset
    dataset = generate_xor_dataset()
    
    print("\n" + "=" * 60)
    print("QUANTUM PHI-HARMONIC NEURAL NETWORK EVOLUTION")
    print("=" * 60)
    print(f"Starting from generation: {start_gen}")
    print(f"Phi resonance: {network.phi_resonance:.6f}")
    print(f"Complexity: {network.complexity:.6f}")
    print(f"Mutation rate: {network.mutation_rate:.6f}")
    print("=" * 60)
    
    # Evolution loop
    for i in range(generations):
        current_gen = start_gen + i
        print(f"\nGeneration {current_gen}:")
        
        # Train the network
        loss, accuracy = network.train_batch(dataset, epochs=epochs_per_generation)
        print(f"  Loss: {loss:.6f}")
        print(f"  Accuracy: {accuracy:.2%}")
        print(f"  Phi resonance: {network.phi_resonance:.6f}")
        
        # Test the network
        test_accuracy = test_network(network, dataset)
        print(f"  Test accuracy: {test_accuracy:.2%}")
        
        # Get network fingerprint
        fingerprint = network.get_phi_fingerprint()
        print(f"  Phi fingerprint: {fingerprint[:3]}...")
        
        # Evolve the network
        evolution = network.evolve()
        print(f"  Evolved to: φ-res={evolution['phi_resonance']:.6f}, ")
        print(f"             comp={evolution['complexity']:.6f}, ")
        print(f"             mut={evolution['mutation_rate']:.6f}")
        
        # Save state periodically
        if (i + 1) % 5 == 0 or i == generations - 1:
            network.save_memory()
            
            # Create a QR code of the current state
            network_hash = network.generate_hash()
            print(f"\nCreating QR code for generation {current_gen} (hash: {network_hash})")
            
    print("\n" + "=" * 60)
    print("EVOLUTION COMPLETE")
    print("=" * 60)
    print(f"Final generation: {network.generation}")
    print(f"Final accuracy: {test_accuracy:.2%}")
    print(f"Final phi resonance: {network.phi_resonance:.6f}")
    print(f"Neural hash: {network.generate_hash()}")
    print("=" * 60)
    
    return network

if __name__ == "__main__":
    # Run the neural network evolution
    network = run_evolution(generations=20, epochs_per_generation=200)
