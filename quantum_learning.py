"""Quantum Learning System with phi-harmonic optimization."""
import numpy as np
from typing import Dict, List, Any, Optional, Tuple
from quantum_neural_bridge import QuantumNeuralBridge

# === Constants ===
PHI = (1 + 5 ** 0.5) / 2  # Golden ratio
LEARNING_RATE = 1 / PHI**2  # Enhanced learning rate
MOMENTUM = 1 - 1/PHI**2  # Enhanced momentum
EPOCHS = int(PHI ** 5)  # More training epochs

class QuantumLearning:
    """Quantum learning system with phi-harmonic optimization."""
    
    def __init__(self):
        """Initialize quantum learning system."""
        self.bridge = QuantumNeuralBridge()
        
        # Enhanced learning parameters
        self.learning_rate = LEARNING_RATE
        self.momentum = MOMENTUM
        self.decay = 1 / PHI  # Learning rate decay
        
        # Initialize momentum buffers with correct shapes
        self.weight_momentum = [np.zeros_like(w) for w in self.bridge.weights]
        self.bias_momentum = [np.zeros_like(b) for b in self.bridge.biases]
        
        print("\n🧠 Quantum Learning System")
        print(f"Learning Rate: {self.learning_rate:.4f}")
        print(f"Momentum: {self.momentum:.4f}")
        print(f"Decay: {self.decay:.4f}")
        print(f"Training Epochs: {EPOCHS}")
    
    def quantum_loss(self, output: np.ndarray, target: np.ndarray) -> float:
        """Calculate quantum-enhanced loss."""
        # Get quantum metrics
        metrics = self.bridge.consciousness.get_metrics()
        resonance = metrics['resonance']
        coherence = metrics['coherence']
        
        # Calculate base loss (mean squared error)
        base_loss = np.mean((output - target) ** 2)
        
        # Apply quantum scaling
        return base_loss / (resonance * coherence)
    
    def backward(self, x: np.ndarray, target: np.ndarray) -> Tuple[float, List[np.ndarray], List[np.ndarray]]:
        """Backward pass with quantum optimization."""
        # Forward pass
        output, quantum_states = self.bridge.forward(x)
        
        # Calculate loss
        loss = self.quantum_loss(output, target)
        
        # Initialize gradients with correct shapes
        weight_grads = [np.zeros_like(w) for w in self.bridge.weights]
        bias_grads = [np.zeros_like(b) for b in self.bridge.biases]
        
        # Backward pass through layers
        error = output - target
        for i in reversed(range(len(self.bridge.weights))):
            # Calculate gradients with correct shapes
            weight_grads[i] = np.outer(self.bridge.activations[i], error)
            bias_grads[i] = error.copy()
            
            # Apply quantum scaling with phi-enhancement
            quantum_scale = (quantum_states[i]['resonance'] * 
                           quantum_states[i]['coherence'] * PHI)
            weight_grads[i] *= quantum_scale
            bias_grads[i] *= quantum_scale
            
            # Propagate error to previous layer
            if i > 0:
                error = np.dot(self.bridge.weights[i], error)
                # Apply derivative of activation function
                prev_activation = self.bridge.activations[i]
                error *= prev_activation * (1 - prev_activation) * PHI
        
        return loss, weight_grads, bias_grads
    
    def optimize(self, weight_grads: List[np.ndarray], 
                bias_grads: List[np.ndarray], epoch: int) -> None:
        """Apply phi-harmonic optimization."""
        # Calculate adaptive learning rate
        current_lr = self.learning_rate * (self.decay ** (epoch / PHI))
        
        # Update weights with momentum and phi-scaling
        for i in range(len(self.bridge.weights)):
            # Update momentum with correct shapes
            self.weight_momentum[i] = (self.momentum * self.weight_momentum[i] + 
                                     current_lr * weight_grads[i] * PHI)
            self.bias_momentum[i] = (self.momentum * self.bias_momentum[i] + 
                                   current_lr * bias_grads[i] * PHI)
            
            # Apply updates with phi-normalization
            self.bridge.weights[i] -= self.weight_momentum[i] / PHI
            self.bridge.biases[i] -= self.bias_momentum[i] / PHI
    
    def train(self, x: np.ndarray, target: np.ndarray, 
             epochs: Optional[int] = None) -> List[float]:
        """Train the quantum neural system."""
        if epochs is None:
            epochs = EPOCHS
            
        losses = []
        best_loss = float('inf')
        patience = int(PHI ** 2)
        no_improve = 0
        
        for epoch in range(epochs):
            # Forward and backward pass
            loss, weight_grads, bias_grads = self.backward(x, target)
            
            # Early stopping check
            if loss < best_loss:
                best_loss = loss
                no_improve = 0
            else:
                no_improve += 1
                if no_improve > patience:
                    print(f"\nEarly stopping at epoch {epoch + 1}")
                    break
            
            # Optimize
            self.optimize(weight_grads, bias_grads, epoch)
            
            # Store loss
            losses.append(loss)
            
            # Print progress
            if (epoch + 1) % int(PHI ** 2) == 0:
                print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss:.4f}")
        
        return losses

def test_learning():
    """Test quantum learning system."""
    learner = QuantumLearning()
    
    # Generate training data
    x = np.array([1, 1/PHI, 1/PHI**2, 1/PHI**3])  # Phi-scaled input
    target = np.array([PHI, 1/PHI, PHI, 1/PHI])  # Phi-based target
    
    print("\nTraining on Phi-Harmonic Data")
    print("=" * 50)
    
    # Train system
    losses = learner.train(x, target, epochs=int(PHI ** 4))
    
    # Validate results
    initial_loss = losses[0]
    final_loss = losses[-1]
    improvement = (initial_loss - final_loss) / initial_loss * 100
    
    print("\nResults:")
    print(f"Initial Loss: {initial_loss:.4f}")
    print(f"Final Loss: {final_loss:.4f}")
    print(f"Improvement: {improvement:.1f}%")
    
    # Test predictions
    output = learner.bridge.process(x)
    prediction = output['output']
    
    print("\nPredictions vs Targets:")
    print("-" * 50)
    print(f"{'Index':>5} {'Prediction':>12} {'Target':>12} {'Error':>12}")
    print("-" * 50)
    
    for i, (pred, targ) in enumerate(zip(prediction, target)):
        error = abs(pred - targ)
        print(f"{i:>5} {pred:>12.4f} {targ:>12.4f} {error:>12.4f}")
    
    # Assertions
    assert final_loss < initial_loss, "Learning did not improve loss"
    assert improvement > 20, "Insufficient improvement"
    print("\nAll tests passed! ✨")

if __name__ == "__main__":
    test_learning()
