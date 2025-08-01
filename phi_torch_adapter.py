"""
PHI-TORCH ADAPTER
=================
Custom adapter for torch functionality without external dependencies.
Implements φ-harmonic tensor operations using native Python and NumPy.

This follows the principle of removing external library dependencies
with custom adapters that maintain the φ-harmonic principles.
"""

import numpy as np
import math
from typing import List, Tuple, Dict, Any, Optional, Union

# φ constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Inverse golden ratio (φ⁻¹ = 0.618033988749895)

class PhiTensor:
    """
    φ-Harmonic Tensor implementation that mimics torch.Tensor
    but uses native NumPy with φ-harmonic principles.
    """
    
    def __init__(self, data, requires_grad=False):
        """Initialize a φ-Tensor with NumPy array data"""
        if isinstance(data, (list, tuple)):
            self.data = np.array(data, dtype=np.float64)
        elif isinstance(data, np.ndarray):
            self.data = data.astype(np.float64)
        else:
            self.data = np.array([data], dtype=np.float64)
        
        self.requires_grad = requires_grad
        self.grad = None
        self.phi_factor = PHI
        
        # Apply φ-harmonic initialization
        self._apply_phi_harmonic_init()
    
    def _apply_phi_harmonic_init(self):
        """Apply φ-harmonic principles to tensor initialization"""
        # Scale values by φ or φ⁻¹ based on magnitude
        mask = np.abs(self.data) > 1.0
        self.data = np.where(mask, self.data * PHI_INV, self.data * PHI)
    
    def __repr__(self):
        """String representation of the tensor"""
        return f"PhiTensor({self.data}, phi_factor={self.phi_factor:.6f})"
    
    def shape(self):
        """Get tensor shape"""
        return self.data.shape
    
    def dim(self):
        """Get tensor dimensions"""
        return len(self.data.shape)
    
    def numpy(self):
        """Convert to NumPy array"""
        return self.data
    
    def item(self):
        """Get single item for 0-dim tensors"""
        if self.data.size == 1:
            return float(self.data.flat[0])
        raise ValueError("item() only works for tensors with a single element")
    
    def to(self, device):
        """Simulate device movement (no-op in our implementation)"""
        # Just return self since we don't have actual devices
        return self
    
    def backward(self):
        """Simulate backward pass (simplified)"""
        if not self.requires_grad:
            return
        
        # Just set a simple gradient for demonstration
        self.grad = np.ones_like(self.data) * PHI_INV
    
    # Mathematical operations with φ-harmonic principles
    def __add__(self, other):
        """Add with φ-harmonic scaling"""
        if isinstance(other, PhiTensor):
            result = self.data + other.data
        else:
            result = self.data + other
        
        # Apply φ-harmonic scaling
        result = result * (1 + PHI_INV * 0.01)
        return PhiTensor(result, requires_grad=self.requires_grad)
    
    def __mul__(self, other):
        """Multiply with φ-harmonic scaling"""
        if isinstance(other, PhiTensor):
            result = self.data * other.data
        else:
            result = self.data * other
        
        # Apply φ-harmonic scaling
        result = result * (1 + PHI_INV * 0.01)
        return PhiTensor(result, requires_grad=self.requires_grad)
    
    def __sub__(self, other):
        """Subtract with φ-harmonic scaling"""
        if isinstance(other, PhiTensor):
            result = self.data - other.data
        else:
            result = self.data - other
        
        # Apply φ-harmonic scaling
        result = result * (1 + PHI_INV * 0.01)
        return PhiTensor(result, requires_grad=self.requires_grad)
    
    def __truediv__(self, other):
        """Divide with φ-harmonic scaling"""
        if isinstance(other, PhiTensor):
            # Avoid division by zero
            other_data = np.where(other.data == 0, 1e-10, other.data)
            result = self.data / other_data
        else:
            # Avoid division by zero
            other = 1e-10 if other == 0 else other
            result = self.data / other
        
        # Apply φ-harmonic scaling
        result = result * (1 + PHI_INV * 0.01)
        return PhiTensor(result, requires_grad=self.requires_grad)
    
    def sum(self):
        """Sum with φ-harmonic scaling"""
        result = np.sum(self.data)
        # Apply φ-harmonic scaling
        result = result * (1 + PHI_INV * 0.01)
        return PhiTensor(result, requires_grad=self.requires_grad)
    
    def mean(self):
        """Mean with φ-harmonic scaling"""
        result = np.mean(self.data)
        # Apply φ-harmonic scaling
        result = result * (1 + PHI_INV * 0.01)
        return PhiTensor(result, requires_grad=self.requires_grad)
    
    def max(self):
        """Max with φ-harmonic scaling"""
        result = np.max(self.data)
        # Apply φ-harmonic scaling
        result = result * (1 + PHI_INV * 0.01)
        return PhiTensor(result, requires_grad=self.requires_grad)
    
    def min(self):
        """Min with φ-harmonic scaling"""
        result = np.min(self.data)
        # Apply φ-harmonic scaling
        result = result * (1 + PHI_INV * 0.01)
        return PhiTensor(result, requires_grad=self.requires_grad)

# Create module-level functions to mimic torch API
def tensor(data, requires_grad=False):
    """Create a new φ-Tensor"""
    return PhiTensor(data, requires_grad=requires_grad)

def ones(shape):
    """Create a tensor filled with ones"""
    return PhiTensor(np.ones(shape))

def zeros(shape):
    """Create a tensor filled with zeros"""
    return PhiTensor(np.zeros(shape))

def rand(shape):
    """Create a tensor with random values"""
    # Use φ-harmonic random values
    random_data = np.random.rand(*shape) * PHI
    return PhiTensor(random_data)

def randn(shape):
    """Create a tensor with random values from normal distribution"""
    # Use φ-harmonic normal distribution
    random_data = np.random.randn(*shape) * PHI_INV
    return PhiTensor(random_data)

def eye(n):
    """Create an identity matrix"""
    return PhiTensor(np.eye(n))

def matmul(tensor1, tensor2):
    """Matrix multiplication with φ-harmonic scaling"""
    if isinstance(tensor1, PhiTensor) and isinstance(tensor2, PhiTensor):
        result = np.matmul(tensor1.data, tensor2.data)
    elif isinstance(tensor1, PhiTensor):
        result = np.matmul(tensor1.data, tensor2)
    elif isinstance(tensor2, PhiTensor):
        result = np.matmul(tensor1, tensor2.data)
    else:
        result = np.matmul(tensor1, tensor2)
    
    # Apply φ-harmonic scaling
    result = result * (1 + PHI_INV * 0.01)
    return PhiTensor(result)

def cat(tensors, dim=0):
    """Concatenate tensors along dimension"""
    tensor_data = [t.data if isinstance(t, PhiTensor) else t for t in tensors]
    result = np.concatenate(tensor_data, axis=dim)
    return PhiTensor(result)

def stack(tensors, dim=0):
    """Stack tensors along dimension"""
    tensor_data = [t.data if isinstance(t, PhiTensor) else t for t in tensors]
    result = np.stack(tensor_data, axis=dim)
    return PhiTensor(result)

# Neural network components
class PhiModule:
    """Base class for all neural network modules"""
    
    def __init__(self):
        self.training = True
        self.phi_factor = PHI
    
    def __call__(self, *args, **kwargs):
        return self.forward(*args, **kwargs)
    
    def forward(self, x):
        """Forward pass - to be implemented by subclasses"""
        raise NotImplementedError
    
    def parameters(self):
        """Return module parameters"""
        return []
    
    def train(self, mode=True):
        """Set training mode"""
        self.training = mode
        return self
    
    def eval(self):
        """Set evaluation mode"""
        self.training = False
        return self

class Linear(PhiModule):
    """Linear layer with φ-harmonic principles"""
    
    def __init__(self, in_features, out_features, bias=True):
        super().__init__()
        
        # Initialize with φ-harmonic scaling
        self.weight = PhiTensor(np.random.randn(out_features, in_features) * PHI_INV, requires_grad=True)
        self.bias = PhiTensor(np.zeros(out_features), requires_grad=True) if bias else None
        self.in_features = in_features
        self.out_features = out_features
    
    def forward(self, x):
        """Forward pass with φ-harmonic principles"""
        if not isinstance(x, PhiTensor):
            x = PhiTensor(x)
        
        output = matmul(x, self.weight.data.T)
        if self.bias is not None:
            output = output + self.bias.data
        
        # Apply φ-harmonic scaling
        output = output * (1 + PHI_INV * 0.01)
        return PhiTensor(output)
    
    def parameters(self):
        """Return layer parameters"""
        params = [self.weight]
        if self.bias is not None:
            params.append(self.bias)
        return params

class ReLU(PhiModule):
    """ReLU activation with φ-harmonic principles"""
    
    def forward(self, x):
        """Forward pass with φ-harmonic ReLU"""
        if not isinstance(x, PhiTensor):
            x = PhiTensor(x)
        
        # ReLU with φ-harmonic scaling
        result = np.maximum(0, x.data) * (1 + PHI_INV * 0.01)
        return PhiTensor(result)

class Sigmoid(PhiModule):
    """Sigmoid activation with φ-harmonic principles"""
    
    def forward(self, x):
        """Forward pass with φ-harmonic sigmoid"""
        if not isinstance(x, PhiTensor):
            x = PhiTensor(x)
        
        # Sigmoid with φ-harmonic scaling
        result = 1 / (1 + np.exp(-x.data))
        result = result * (1 + PHI_INV * 0.01)
        return PhiTensor(result)

class Tanh(PhiModule):
    """Tanh activation with φ-harmonic principles"""
    
    def forward(self, x):
        """Forward pass with φ-harmonic tanh"""
        if not isinstance(x, PhiTensor):
            x = PhiTensor(x)
        
        # Tanh with φ-harmonic scaling
        result = np.tanh(x.data) * (1 + PHI_INV * 0.01)
        return PhiTensor(result)

class Sequential(PhiModule):
    """Sequential container for modules"""
    
    def __init__(self, *modules):
        super().__init__()
        self.modules = list(modules)
    
    def forward(self, x):
        """Forward pass through all modules"""
        for module in self.modules:
            x = module(x)
        return x
    
    def parameters(self):
        """Return all parameters from all modules"""
        params = []
        for module in self.modules:
            params.extend(module.parameters())
        return params

# Optimizer implementation
class PhiOptimizer:
    """Base optimizer class"""
    
    def __init__(self, parameters, lr=0.01):
        self.parameters = parameters
        self.lr = lr * PHI_INV  # Scale learning rate by φ⁻¹
    
    def zero_grad(self):
        """Zero out gradients"""
        for param in self.parameters:
            if param.grad is not None:
                param.grad = np.zeros_like(param.data)
    
    def step(self):
        """Update parameters - to be implemented by subclasses"""
        raise NotImplementedError

class SGD(PhiOptimizer):
    """Stochastic Gradient Descent with φ-harmonic principles"""
    
    def __init__(self, parameters, lr=0.01, momentum=0):
        super().__init__(parameters, lr)
        self.momentum = momentum * PHI  # Scale momentum by φ
        self.velocity = [np.zeros_like(param.data) for param in parameters]
    
    def step(self):
        """Update parameters with φ-harmonic SGD"""
        for i, param in enumerate(self.parameters):
            if param.grad is None:
                continue
            
            # Apply momentum with φ-harmonic scaling
            self.velocity[i] = self.momentum * self.velocity[i] + param.grad
            
            # Update parameter with φ-harmonic scaling
            param.data -= self.lr * self.velocity[i] * (1 + PHI_INV * 0.01)

class Adam(PhiOptimizer):
    """Adam optimizer with φ-harmonic principles"""
    
    def __init__(self, parameters, lr=0.001, betas=(0.9, 0.999), eps=1e-8):
        super().__init__(parameters, lr)
        self.betas = (betas[0] * PHI_INV, betas[1] * PHI_INV)  # Scale betas by φ⁻¹
        self.eps = eps
        self.m = [np.zeros_like(param.data) for param in parameters]
        self.v = [np.zeros_like(param.data) for param in parameters]
        self.t = 0
    
    def step(self):
        """Update parameters with φ-harmonic Adam"""
        self.t += 1
        
        for i, param in enumerate(self.parameters):
            if param.grad is None:
                continue
            
            # Update biased first moment estimate
            self.m[i] = self.betas[0] * self.m[i] + (1 - self.betas[0]) * param.grad
            
            # Update biased second raw moment estimate
            self.v[i] = self.betas[1] * self.v[i] + (1 - self.betas[1]) * (param.grad ** 2)
            
            # Bias correction
            m_hat = self.m[i] / (1 - self.betas[0] ** self.t)
            v_hat = self.v[i] / (1 - self.betas[1] ** self.t)
            
            # Update parameters with φ-harmonic scaling
            param.data -= self.lr * m_hat / (np.sqrt(v_hat) + self.eps) * (1 + PHI_INV * 0.01)

# Loss functions
def mse_loss(pred, target):
    """Mean squared error loss with φ-harmonic scaling"""
    if isinstance(pred, PhiTensor):
        pred_data = pred.data
    else:
        pred_data = np.array(pred)
    
    if isinstance(target, PhiTensor):
        target_data = target.data
    else:
        target_data = np.array(target)
    
    # Calculate MSE with φ-harmonic scaling
    loss = np.mean((pred_data - target_data) ** 2) * (1 + PHI_INV * 0.01)
    return PhiTensor(loss, requires_grad=True)

def binary_cross_entropy(pred, target):
    """Binary cross entropy loss with φ-harmonic scaling"""
    if isinstance(pred, PhiTensor):
        pred_data = pred.data
    else:
        pred_data = np.array(pred)
    
    if isinstance(target, PhiTensor):
        target_data = target.data
    else:
        target_data = np.array(target)
    
    # Clip predictions to avoid log(0)
    pred_data = np.clip(pred_data, 1e-10, 1 - 1e-10)
    
    # Calculate BCE with φ-harmonic scaling
    loss = -np.mean(target_data * np.log(pred_data) + (1 - target_data) * np.log(1 - pred_data))
    loss = loss * (1 + PHI_INV * 0.01)
    
    return PhiTensor(loss, requires_grad=True)

# Create a namespace to mimic torch.nn
class nn:
    Linear = Linear
    ReLU = ReLU
    Sigmoid = Sigmoid
    Tanh = Tanh
    Sequential = Sequential
    Module = PhiModule
    
    @staticmethod
    def mse_loss(pred, target):
        return mse_loss(pred, target)
    
    @staticmethod
    def binary_cross_entropy(pred, target):
        return binary_cross_entropy(pred, target)

# Create a namespace to mimic torch.optim
class optim:
    SGD = SGD
    Adam = Adam

# Example usage demonstration
def run_phi_torch_example():
    """Run a simple example to demonstrate the φ-Torch adapter"""
    print("\nPHI-TORCH ADAPTER EXAMPLE")
    print("========================")
    
    # Create tensors
    x = tensor([1.0, 2.0, 3.0, 4.0])
    y = tensor([2.0, 4.0, 6.0, 8.0])
    
    print(f"x: {x}")
    print(f"y: {y}")
    
    # Basic operations
    z = x + y
    print(f"x + y: {z}")
    
    z = x * y
    print(f"x * y: {z}")
    
    # Create a simple neural network
    model = nn.Sequential(
        nn.Linear(4, 8),
        nn.ReLU(),
        nn.Linear(8, 1),
        nn.Sigmoid()
    )
    
    # Create input data
    input_data = rand((10, 4))
    target = tensor(np.random.randint(0, 2, (10, 1)), requires_grad=False)
    
    # Create optimizer
    optimizer = optim.SGD(model.parameters(), lr=0.01)
    
    # Training loop
    print("\nTraining simple neural network...")
    for epoch in range(5):
        # Forward pass
        output = model(input_data)
        
        # Calculate loss
        loss = nn.binary_cross_entropy(output, target)
        
        # Zero gradients
        optimizer.zero_grad()
        
        # Backward pass
        loss.backward()
        
        # Update parameters
        optimizer.step()
        
        print(f"Epoch {epoch+1}, Loss: {loss.item():.6f}")
    
    print("\nPHI-TORCH ADAPTER EXAMPLE COMPLETED")

if __name__ == "__main__":
    run_phi_torch_example()
