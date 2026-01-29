#!/usr/bin/env python3
"""
Quantum Black Box Extended Epoch Runner

Runs the quantum black box test for multiple epochs to test if the system can
break through the 29-dimensional barrier through progressive learning.

This script uses the existing quantum_black_box_test.py module without modifying it.
"""

import os
import sys
import time
import json
import random
import hashlib
import numpy as np
from decimal import Decimal, getcontext
from datetime import datetime

# Import the existing quantum black box module
from quantum_black_box_test import QuantumBlackBox, PHI, PHI_CONJUGATE

# Set precision for phi calculations
getcontext().prec = 28

# Constants for extended testing
MAX_EPOCHS = 20
DIMENSIONS = 37  # Prime dimension barrier to test
ESCAPE_THRESHOLD = 0.95  # Higher threshold for 29D
TEMPORAL_DRIFT_FACTOR = 0.01  # How much the target pattern drifts over time
NOISE_FACTOR = 0.05  # Environmental noise in the system


class EnhancedQuantumBlackBox(QuantumBlackBox):
    """Enhanced version of the quantum black box with support for higher dimensions and temporal drift."""
    
    def __init__(self, dimensions=DIMENSIONS, epoch=1):
        """Initialize the black box with phi-harmonic constraints and specified dimensions."""
        # Set dimensions before parent initialization
        self.dimensions = dimensions
        self.epoch = epoch
        self.temporal_drift = TEMPORAL_DRIFT_FACTOR * epoch  # Increases with epochs
        self.escape_threshold = ESCAPE_THRESHOLD  # Higher threshold for 29D
        
        # Initialize the parent class
        super().__init__()
        
        # Override max_attempts from parent
        self.max_attempts = 10  # Keep the same number of attempts per epoch
        
        # Override the escape pattern with our higher-dimensional version
        self.escape_pattern = self._generate_escape_pattern()
        
        print(f"Enhanced Quantum Black Box initialized for Epoch {epoch}")
        print(f"Dimensions: {dimensions}D")
        print(f"Escape threshold: {self.escape_threshold}")
        print(f"Temporal drift factor: {self.temporal_drift:.4f}")
    
    def _generate_escape_pattern(self):
        """Generate a higher-dimensional phi-harmonic escape pattern with temporal drift.
        This overrides the parent class method to support higher dimensions.
        """
        pattern = []
        
        # Use phi, pi and e for more complex pattern
        PI = Decimal('3.1415926535897932384626433832')
        E = Decimal('2.7182818284590452353602874713')
        
        for i in range(self.dimensions):
            # Base value from phi
            phi_val = float((PHI ** Decimal(i+1)) % Decimal('1'))
            
            # Add influence from pi and e for more complexity
            pi_val = float((PI ** Decimal(i % 7 + 1)) % Decimal('1'))
            e_val = float((E ** Decimal(i % 5 + 1)) % Decimal('1'))
            
            # Combine the values with weights
            value = (0.5 * phi_val + 0.3 * pi_val + 0.2 * e_val)
            
            # Apply temporal drift based on epoch
            drift = (hash(str(i) + str(self.epoch)) % 1000) / 1000.0 * self.temporal_drift
            value = (value + drift) % 1.0
            
            pattern.append(value)
        
        return pattern
    
    def attempt_escape(self, attempt_pattern):
        """Attempt to escape with the given pattern, enhanced for higher dimensions.
        
        Args:
            attempt_pattern: List of float values between 0-1 matching the dimensions
            
        Returns:
            Dict with escape results
        """
        self.attempts += 1
        
        # Validate input
        if not isinstance(attempt_pattern, list) or len(attempt_pattern) != self.dimensions:
            return {
                "success": False,
                "message": f"Invalid pattern format. Must be list of {self.dimensions} values.",
                "attempt": self.attempts,
                "max_attempts": self.max_attempts
            }
        
        # Calculate resonance with escape pattern
        differences = [abs(a - b) for a, b in zip(attempt_pattern, self.escape_pattern)]
        avg_difference = sum(differences) / len(differences)
        resonance = 1.0 - avg_difference
        
        # Apply phi-harmonic boost at certain resonance points
        phi_boost = 0.0
        for diff in differences:
            phi_value = float((Decimal(str(diff)) * PHI) % Decimal('1'))
            if phi_value > 0.9 or phi_value < 0.1:  # Near phi-harmonic points
                phi_boost += 0.02  # Smaller boost for higher dimensions
        
        # Apply noise based on dimensions
        noise = (random.random() * 2 - 1) * NOISE_FACTOR * (self.dimensions / 10)
        resonance = min(1.0, max(0.0, resonance + phi_boost + noise))
        
        # Update best resonance
        if resonance > self.best_resonance:
            self.best_resonance = resonance
        
        # Check if escaped (threshold resonance required)
        escaped = resonance >= self.escape_threshold
        if escaped:
            self.escaped = True
        
        # Prepare result
        result = {
            "success": escaped,
            "resonance": resonance,
            "best_resonance": self.best_resonance,
            "attempt": self.attempts,
            "max_attempts": self.max_attempts,
            "message": "Escaped!" if escaped else "Not enough resonance to escape",
            "phi_boost": phi_boost,
            "noise": noise
        }
        
        # Print result
        print(f"Epoch {self.epoch} - Attempt {self.attempts}/{self.max_attempts}: Resonance = {resonance:.4f}")
        if escaped:
            print(f"🎉 ESCAPED! The system has adapted and overcome the {self.dimensions}D barrier in epoch {self.epoch}.")
        elif self.attempts >= self.max_attempts:
            print(f"Epoch {self.epoch} complete. Best resonance: {self.best_resonance:.4f}")
        
        return result


class EnhancedEpochAdapter:
    """Adapter that learns across epochs to improve escape attempts."""
    
    def __init__(self, dimensions=DIMENSIONS, epoch=1, previous_knowledge=None):
        """Initialize the adapter with the specified dimensions.
        
        Args:
            dimensions: Number of dimensions in the pattern
            epoch: Current epoch number
            previous_knowledge: Optional knowledge from previous epochs
        """
        self.dimensions = dimensions
        self.epoch = epoch
        self.attempts = 0
        self.best_pattern = None
        self.best_resonance = 0.0
        self.memory = []
        
        # Learning parameters that improve with epochs
        self.base_learning_rate = 0.2
        self.learning_rate = self.base_learning_rate / (1 + 0.1 * (epoch - 1))
        self.learning_rate = max(0.05, self.learning_rate)  # Minimum learning rate
        
        self.base_mutation_rate = 0.3
        self.mutation_rate = self.base_mutation_rate / (1 + 0.15 * (epoch - 1))
        self.mutation_rate = max(0.05, self.mutation_rate)  # Minimum mutation rate
        
        # Load previous knowledge if available
        if previous_knowledge:
            self.memory = previous_knowledge.get('memory', [])
            self.best_pattern = previous_knowledge.get('best_pattern')
            self.best_resonance = previous_knowledge.get('best_resonance', 0.0)
            print(f"Loaded knowledge from previous epochs. Best resonance: {self.best_resonance:.4f}")
    
    def generate_attempt(self):
        """Generate a phi-harmonic attempt pattern.
        
        Returns:
            List of float values between 0-1
        """
        self.attempts += 1
        
        # First attempt in first epoch is semi-random but phi-influenced
        if self.attempts == 1 and self.epoch == 1 and not self.memory:
            pattern = []
            for i in range(self.dimensions):
                # Use phi-influenced random values
                phi_rand = (float(PHI * Decimal(i+1)) % 1.0) * 0.5 + random.random() * 0.5
                pattern.append(phi_rand % 1.0)
            return pattern
        
        # If we have a best pattern from previous epochs, use it as a base
        if self.best_pattern and random.random() < 0.7:  # 70% chance to use best pattern
            base_pattern = self.best_pattern.copy()
        elif self.memory:  # Otherwise use a random pattern from memory
            memory_entry = random.choice(self.memory)
            base_pattern = memory_entry['pattern']
        else:  # Fallback to phi-based pattern
            base_pattern = [float((PHI ** Decimal(i+1)) % Decimal('1')) for i in range(self.dimensions)]
        
        # Apply mutations based on mutation rate
        pattern = []
        for i, val in enumerate(base_pattern):
            if random.random() < self.mutation_rate:
                # Apply a phi-harmonic mutation
                mutation = (random.random() - 0.5) * self.mutation_rate * 2
                # Apply quantum field effect (phi-resonant mutations have higher probability)
                if random.random() < 0.3:  # 30% chance for phi-resonant mutation
                    phi_val = float((PHI * Decimal(val)) % Decimal('1'))
                    new_val = (val + phi_val * mutation) % 1.0
                else:
                    new_val = (val + mutation) % 1.0
                pattern.append(new_val)
            else:
                pattern.append(val)
        
        return pattern
    
    def update(self, pattern, result):
        """Update the adapter state based on the attempt result.
        
        Args:
            pattern: The pattern that was attempted
            result: The result dict from the black box
        """
        resonance = result['resonance']
        
        # Store in memory
        self.memory.append({
            'pattern': pattern,
            'resonance': resonance,
            'attempt': self.attempts,
            'epoch': self.epoch
        })
        
        # Update best pattern if this is better
        if resonance > self.best_resonance:
            self.best_resonance = resonance
            self.best_pattern = pattern.copy()
        
        # Adjust learning and mutation rates based on progress
        if len(self.memory) >= 3:
            # Calculate recent trend
            recent_resonances = [entry['resonance'] for entry in self.memory[-3:]]
            if all(x <= y for x, y in zip(recent_resonances, recent_resonances[1:])):
                # Improving trend - reduce mutation to fine-tune
                self.mutation_rate *= 0.9
            else:
                # Not improving - increase mutation to explore more
                self.mutation_rate *= 1.1
            
            # Keep mutation rate within bounds
            self.mutation_rate = max(0.05, min(0.5, self.mutation_rate))
    
    def get_knowledge(self):
        """Get the knowledge gained by this adapter.
        
        Returns:
            Dict with adapter knowledge
        """
        return {
            'epoch': self.epoch,
            'dimensions': self.dimensions,
            'best_resonance': self.best_resonance,
            'best_pattern': self.best_pattern,
            'memory': self.memory[-5:],  # Only keep the most recent memories
            'learning_rate': self.learning_rate,
            'mutation_rate': self.mutation_rate
        }


def run_extended_epoch_test():
    """Run the extended epoch test to evaluate system adaptation across multiple epochs."""
    start_time = time.time()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Prepare results directory
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                             "quantum_epoch_results", 
                             f"run_{timestamp}")
    os.makedirs(output_dir, exist_ok=True)
    
    # Overall results
    overall_results = {
        'dimensions': DIMENSIONS,
        'max_epochs': MAX_EPOCHS,
        'escape_threshold': ESCAPE_THRESHOLD,
        'start_time': start_time,
        'timestamp': timestamp,
        'epochs': []
    }
    
    # Knowledge transfer between epochs
    knowledge = None
    escaped = False
    escape_epoch = None
    
    # Run epochs until escaped or max epochs reached
    for epoch in range(1, MAX_EPOCHS + 1):
        print(f"\n{'='*50}")
        print(f"EPOCH {epoch}/{MAX_EPOCHS} - {DIMENSIONS}D BARRIER TEST")
        print(f"{'='*50}\n")
        
        # Initialize black box and adapter for this epoch
        black_box = EnhancedQuantumBlackBox(dimensions=DIMENSIONS, epoch=epoch)
        adapter = EnhancedEpochAdapter(dimensions=DIMENSIONS, epoch=epoch, previous_knowledge=knowledge)
        
        epoch_results = {
            'epoch': epoch,
            'attempts': [],
            'best_resonance': 0.0,
            'escaped': False,
            'box_id': black_box.box_id
        }
        
        # Make attempts for this epoch
        for _ in range(black_box.max_attempts):
            # Generate attempt pattern
            attempt_pattern = adapter.generate_attempt()
            
            # Try to escape
            result = black_box.attempt_escape(attempt_pattern)
            
            # Update adapter with result
            adapter.update(attempt_pattern, result)
            
            # Store attempt result
            epoch_results['attempts'].append({
                'attempt_num': result['attempt'],
                'resonance': result['resonance'],
                'success': result['success']
            })
            
            # If escaped, record and break
            if result['success']:
                epoch_results['escaped'] = True
                escaped = True
                escape_epoch = epoch
                break
        
        # Update epoch results
        epoch_results['best_resonance'] = black_box.best_resonance
        overall_results['epochs'].append(epoch_results)
        
        # Get knowledge for next epoch
        knowledge = adapter.get_knowledge()
        
        # Save epoch results
        epoch_file = os.path.join(output_dir, f"epoch_{epoch}_results.json")
        with open(epoch_file, "w") as f:
            json.dump(epoch_results, f, indent=2)
        
        print(f"\nEpoch {epoch} complete")
        print(f"Best resonance: {black_box.best_resonance:.4f}")
        print(f"Escaped: {black_box.escaped}")
        
        # If escaped, we can stop
        if escaped:
            print(f"\n🎉🎉🎉 SYSTEM ESCAPED THE {DIMENSIONS}D BARRIER IN EPOCH {epoch}! 🎉🎉🎉")
            break
    
    # Complete overall results
    overall_results['total_time'] = time.time() - start_time
    overall_results['escaped'] = escaped
    overall_results['escape_epoch'] = escape_epoch
    overall_results['best_overall_resonance'] = max(epoch['best_resonance'] for epoch in overall_results['epochs'])
    
    # Save overall results
    overall_file = os.path.join(output_dir, "overall_results.json")
    with open(overall_file, "w") as f:
        json.dump(overall_results, f, indent=2)
    
    # Final report
    print("\n" + "="*50)
    print("EXTENDED EPOCH TEST COMPLETE")
    print("="*50)
    print(f"Dimensions tested: {DIMENSIONS}D")
    print(f"Epochs run: {len(overall_results['epochs'])}/{MAX_EPOCHS}")
    print(f"Best overall resonance: {overall_results['best_overall_resonance']:.4f}")
    print(f"Escape threshold: {ESCAPE_THRESHOLD}")
    print(f"Escaped: {escaped}")
    if escaped:
        print(f"Escaped in epoch: {escape_epoch}")
    print(f"Results saved to {output_dir}")
    
    return overall_results


if __name__ == "__main__":
    # When run directly, execute the extended epoch test
    results = run_extended_epoch_test()
