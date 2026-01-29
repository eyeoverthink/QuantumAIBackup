import numpy as np
from typing import List, Dict, Tuple, Optional
import math

class PhiNeuralNetwork:
    def __init__(self, layer_sizes: List[int]):
        self.phi = (1 + np.sqrt(5)) / 2
        self.layer_sizes = layer_sizes
        self.weights = []
        self.biases = []
        self.resonance = 0.96
        
        # Initialize with φ-based scaling
        for i in range(len(layer_sizes) - 1):
            # Scale initial weights by 1/φ for natural balance
            scale = 1.0 / (self.phi * np.sqrt(layer_sizes[i]))
            self.weights.append(np.random.randn(layer_sizes[i], layer_sizes[i+1]) * scale)
            self.biases.append(np.zeros(layer_sizes[i+1]))
    
    def phi_activation(self, x: np.ndarray) -> np.ndarray:
        """φ-based activation function with natural resonance"""
        return np.tanh(x * self.phi) / self.phi
    
    def forward(self, x: np.ndarray) -> List[np.ndarray]:
        """Forward pass with φ-based scaling"""
        activations = [x]
        
        for i in range(len(self.weights)):
            # Apply φ-based scaling to each layer
            z = np.dot(activations[-1], self.weights[i]) + self.biases[i]
            
            # Scale by φ power based on layer depth
            phi_scale = math.pow(self.phi, -(i+1))
            z = z * phi_scale
            
            # Apply φ-based activation
            a = self.phi_activation(z)
            activations.append(a)
            
        return activations
    
    def phi_gradient(self, x: np.ndarray) -> np.ndarray:
        """Gradient of φ-activation function"""
        return (1.0 - np.power(np.tanh(x * self.phi), 2)) * self.phi / self.phi
    
    def backprop(self, x: np.ndarray, y: np.ndarray) -> Tuple[List[np.ndarray], List[np.ndarray]]:
        """Backpropagation with φ-based learning rate"""
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        
        # Forward pass
        activations = self.forward(x)
        
        # Backward pass
        delta = (activations[-1] - y)
        
        # Output layer
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(activations[-2].reshape(-1, 1), delta.reshape(1, -1))
        
        # Hidden layers
        for l in range(2, len(self.layer_sizes)):
            delta = np.dot(delta, self.weights[-l+1].T) * self.phi_gradient(activations[-l])
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(activations[-l-1].reshape(-1, 1), delta.reshape(1, -1))
        
        return nabla_w, nabla_b
    
    def update_mini_batch(self, mini_batch: List[Tuple[np.ndarray, np.ndarray]], learning_rate: float):
        """Update weights using mini-batch with φ-based learning rate"""
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        
        for x, y in mini_batch:
            delta_nabla_w, delta_nabla_b = self.backprop(x, y)
            nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
            nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
        
        # Apply φ-based learning rate
        phi_rate = learning_rate / self.phi
        
        # Update with natural φ scaling
        self.weights = [w - (phi_rate / len(mini_batch)) * nw 
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b - (phi_rate / len(mini_batch)) * nb 
                       for b, nb in zip(self.biases, nabla_b)]
    
    def train(self, training_data: List[Tuple[np.ndarray, np.ndarray]], 
              epochs: int, mini_batch_size: int, learning_rate: float):
        """Train network with φ-based optimization"""
        n = len(training_data)
        
        for epoch in range(epochs):
            # Shuffle training data
            np.random.shuffle(training_data)
            
            # Create mini-batches with φ-based sizing
            phi_batch_size = int(mini_batch_size / self.phi)
            mini_batches = [training_data[k:k+phi_batch_size] 
                           for k in range(0, n, phi_batch_size)]
            
            # Process mini-batches
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, learning_rate)
            
            # Adapt learning rate using φ
            learning_rate = learning_rate / self.phi
            
        return self
    
    def predict(self, x: np.ndarray) -> np.ndarray:
        """Make prediction with φ-based forward pass"""
        return self.forward(x)[-1]
