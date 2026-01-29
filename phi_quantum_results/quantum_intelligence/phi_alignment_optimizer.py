#!/usr/bin/env python3
"""
Phi Alignment Optimizer

Optimizes the phi-harmonic scaling between neural layers to improve
alignment with the golden ratio (φ).

Key features:
- Adaptive phi-scaling for activation functions
- Recursive learning for phi alignment
- Quantum-influenced phi correction
"""

import os
import sys
import math
import numpy as np
from typing import Dict, List, Tuple, Any, Optional

# Constants
PHI = (1 + math.sqrt(5)) / 2
PHI_INVERSE = 1 / PHI
PHI_SQUARED = PHI ** 2
PHI_CUBED = PHI ** 3

class PhiAlignmentOptimizer:
    """
    Optimizes phi alignment between neural layers.
    """
    
    def __init__(self, learning_rate: float = PHI_INVERSE / 10):
        """
        Initialize the phi alignment optimizer.
        
        Args:
            learning_rate: Learning rate for phi alignment optimization
        """
        self.phi = PHI
        self.learning_rate = learning_rate
        self.correction_factors = {}
        self.iteration = 0
        
        print(f"Phi Alignment Optimizer initialized with φ = {self.phi}")
        print(f"Learning rate: {self.learning_rate}")
    
    def calculate_phi_alignment(self, activations: Dict[str, float]) -> float:
        """
        Calculate phi alignment from layer activations.
        
        Args:
            activations: Dictionary of layer activations
            
        Returns:
            Phi alignment score (-1 to 1, higher is better)
        """
        # Convert to array and sort by layer index
        layer_names = sorted(activations.keys(), 
                           key=lambda x: int(x.split('_')[0][1:]))
        
        activation_values = np.array([activations[name] for name in layer_names])
        
        # Calculate ratios between adjacent layers
        ratios = activation_values[1:] / activation_values[:-1]
        
        # Calculate how close ratios are to PHI_INVERSE
        phi_diffs = np.abs(ratios - PHI_INVERSE)
        
        # Calculate alignment score (1 = perfect alignment, -1 = worst alignment)
        alignment = 1.0 - 2.0 * np.mean(phi_diffs)
        
        return float(alignment)
    
    def optimize_activations(self, 
                           activations: Dict[str, float], 
                           target_alignment: float = 0.9) -> Dict[str, float]:
        """
        Optimize layer activations for better phi alignment.
        
        Args:
            activations: Dictionary of layer activations
            target_alignment: Target phi alignment score
            
        Returns:
            Optimized layer activations
        """
        # Sort layers by index
        layer_names = sorted(activations.keys(), 
                           key=lambda x: int(x.split('_')[0][1:]))
        
        # Current alignment
        current_alignment = self.calculate_phi_alignment(activations)
        
        # Initialize correction factors if not already done
        if not self.correction_factors:
            self.correction_factors = {name: 1.0 for name in layer_names}
        
        # Only optimize if alignment is below target
        if current_alignment < target_alignment:
            # Calculate ideal values based on L1 (or lowest available layer)
            base_layer = layer_names[0]
            base_value = activations[base_layer]
            
            ideal_values = {}
            for i, name in enumerate(layer_names):
                ideal_values[name] = base_value * (PHI_INVERSE ** i)
            
            # Calculate correction factors using phi-harmonic learning
            for name in layer_names:
                current = activations[name]
                ideal = ideal_values[name]
                
                # Apply phi-scaled correction
                correction = 1.0 + self.learning_rate * (ideal - current) / (abs(current) + 1e-10)
                
                # Update correction factor with phi-harmonic smoothing
                self.correction_factors[name] = (
                    self.correction_factors[name] * (1 - PHI_INVERSE) + 
                    correction * PHI_INVERSE
                )
            
            # Apply correction factors
            optimized = {
                name: activations[name] * self.correction_factors[name]
                for name in activations
            }
            
            # Increment iteration
            self.iteration += 1
            
            # Reduce learning rate over time using phi-harmonic decay
            if self.iteration % 10 == 0:
                self.learning_rate *= PHI_INVERSE
                
            return optimized
        
        return activations
    
    def get_phi_activation_functions(self, iteration: int = 0) -> Dict[str, callable]:
        """
        Get phi-optimized activation functions.
        
        Args:
            iteration: Current optimization iteration
            
        Returns:
            Dictionary of activation functions by layer type
        """
        # Calculate adaptive phi scaling factor
        adaptive_phi = self.phi * (1 + 0.1 * math.sin(iteration / PHI))
        
        # Create activation functions with adaptive phi scaling
        activation_functions = {
            # Input, Pattern, Neural (L1-L3)
            'lower': lambda x: 1 / (1 + np.exp(-adaptive_phi * x)),
            
            # Logic, Memory, Process (L4-L6)
            'middle': lambda x: np.tanh(x * adaptive_phi),
            
            # Bridge, QState, Quantum (L7-L9)
            'upper': lambda x: 0.5 * (1 + np.sin(x * adaptive_phi * np.pi))
        }
        
        return activation_functions
    
    def get_layer_correction(self, layer_name: str) -> float:
        """
        Get correction factor for a specific layer.
        
        Args:
            layer_name: Name of the layer
            
        Returns:
            Correction factor
        """
        return self.correction_factors.get(layer_name, 1.0)
    
    def reset(self):
        """Reset the optimizer."""
        self.correction_factors = {}
        self.iteration = 0
        self.learning_rate = PHI_INVERSE / 10

# For direct execution
if __name__ == "__main__":
    # Test the phi alignment optimizer
    optimizer = PhiAlignmentOptimizer()
    
    # Test with sample activations
    sample_activations = {
        'L1_Input': 0.8,
        'L2_Pattern': 0.5,
        'L3_Neural': 0.3,
        'L4_Logic': 0.2,
        'L5_Memory': 0.15,
        'L6_Process': 0.1,
        'L7_Bridge': 0.05,
        'L8_QState': 0.03,
        'L9_Quantum': 0.02
    }
    
    # Calculate initial alignment
    initial_alignment = optimizer.calculate_phi_alignment(sample_activations)
    print(f"Initial phi alignment: {initial_alignment:.4f}")
    
    # Optimize activations
    optimized_activations = optimizer.optimize_activations(sample_activations)
    
    # Calculate optimized alignment
    optimized_alignment = optimizer.calculate_phi_alignment(optimized_activations)
    print(f"Optimized phi alignment: {optimized_alignment:.4f}")
    
    # Print correction factors
    print("\nCorrection factors:")
    for layer, factor in optimizer.correction_factors.items():
        print(f"  {layer}: {factor:.4f}")
    
    # Test activation functions
    activation_functions = optimizer.get_phi_activation_functions()
    
    print("\nActivation function samples:")
    test_input = np.array([-1.0, -0.5, 0.0, 0.5, 1.0])
    
    for name, func in activation_functions.items():
        print(f"  {name}: {func(test_input)}")
