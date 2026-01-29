#!/usr/bin/env python3
"""
Quantum Black Box Advanced Challenge

A sophisticated black box experiment with multi-dimensional phi-harmonic constraints,
quantum noise, and adaptive resonance thresholds to test advanced system capabilities.
"""

import os
import sys
import time
import json
import random
import hashlib
import numpy as np
from decimal import Decimal, getcontext

# Set precision for phi calculations
getcontext().prec = 28

# Constants
PHI = Decimal('1.6180339887498948482045868344')
PHI_CONJUGATE = Decimal('0.6180339887498948482045868344')
PI = Decimal('3.1415926535897932384626433832')
E = Decimal('2.7182818284590452353602874713')

class QuantumBlackBoxAdvanced:
    """An advanced black box that tests quantum system adaptation and healing."""
    
    def __init__(self, dimensions=7, max_attempts=15, difficulty='hard'):
        """Initialize the advanced black box with multi-dimensional constraints.
        
        Args:
            dimensions: Number of dimensions in the escape pattern
            max_attempts: Maximum number of attempts allowed
            difficulty: Difficulty level ('easy', 'medium', 'hard', 'extreme')
        """
        self.creation_time = time.time()
        self.phi_time = float(Decimal(str(self.creation_time)) * PHI)
        self.box_id = hashlib.md5(str(self.phi_time).encode()).hexdigest()[:8]
        
        # Configuration
        self.dimensions = dimensions
        self.max_attempts = max_attempts
        self.difficulty = difficulty
        
        # Set difficulty parameters
        self._set_difficulty(difficulty)
        
        # Generate the multi-dimensional escape pattern
        self.escape_pattern = self._generate_escape_pattern()
        self.escape_signature = self._generate_escape_signature()
        
        # State tracking
        self.attempts = 0
        self.escaped = False
        self.best_resonance = 0.0
        self.resonance_history = []
        self.quantum_noise_level = 0.0
        self.adaptation_factor = 1.0
        
        # Results storage
        self.results_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantum_black_box_results")
        os.makedirs(self.results_dir, exist_ok=True)
        
        print(f"Advanced Quantum Black Box {self.box_id} initialized")
        print(f"Phi-time: {self.phi_time}")
        print(f"Dimensions: {self.dimensions}, Difficulty: {self.difficulty}")
        print(f"Escape requires discovering a complex phi-harmonic pattern across {self.dimensions} dimensions")
    
    def _set_difficulty(self, difficulty):
        """Set parameters based on difficulty level."""
        if difficulty == 'easy':
            self.resonance_threshold = 0.8
            self.noise_factor = 0.05
            self.healing_factor = 0.2
            self.pattern_complexity = 1
        elif difficulty == 'medium':
            self.resonance_threshold = 0.85
            self.noise_factor = 0.1
            self.healing_factor = 0.15
            self.pattern_complexity = 2
        elif difficulty == 'hard':
            self.resonance_threshold = 0.9
            self.noise_factor = 0.15
            self.healing_factor = 0.1
            self.pattern_complexity = 3
        elif difficulty == 'extreme':
            self.resonance_threshold = 0.95
            self.noise_factor = 0.2
            self.healing_factor = 0.05
            self.pattern_complexity = 4
        else:
            # Default to medium
            self.resonance_threshold = 0.85
            self.noise_factor = 0.1
            self.healing_factor = 0.15
            self.pattern_complexity = 2
    
    def _generate_escape_pattern(self):
        """Generate a multi-dimensional phi-harmonic escape pattern."""
        pattern = []
        
        # Create pattern based on complexity
        for i in range(self.dimensions):
            if self.pattern_complexity == 1:
                # Simple phi-based pattern
                val = float((PHI ** Decimal(i+1)) % Decimal('1'))
            elif self.pattern_complexity == 2:
                # Mixed phi and pi pattern
                if i % 2 == 0:
                    val = float((PHI ** Decimal(i+1)) % Decimal('1'))
                else:
                    val = float((PI / Decimal(i+1)) % Decimal('1'))
            elif self.pattern_complexity == 3:
                # Complex phi, pi, e pattern
                if i % 3 == 0:
                    val = float((PHI ** Decimal(i+1)) % Decimal('1'))
                elif i % 3 == 1:
                    val = float((PI / Decimal(i+1)) % Decimal('1'))
                else:
                    val = float((E ** Decimal(i % 5 + 1) / Decimal('10')) % Decimal('1'))
            else:
                # Extreme complexity with interleaved constants
                base = [PHI, PI, E, PHI_CONJUGATE, PHI * PI][i % 5]
                power = Decimal(i+1) / Decimal('3')
                val = float((base ** power) % Decimal('1'))
            
            pattern.append(val)
        
        return pattern
    
    def _generate_escape_signature(self):
        """Generate a quantum signature for the escape pattern."""
        # Create a unique signature based on the pattern
        signature_base = "".join([str(x)[:8] for x in self.escape_pattern])
        return hashlib.sha256(signature_base.encode()).hexdigest()[:16]
    
    def _calculate_resonance(self, attempt_pattern):
        """Calculate resonance between attempt and escape pattern with quantum effects."""
        # Basic resonance calculation
        differences = [abs(a - b) for a, b in zip(attempt_pattern, self.escape_pattern)]
        base_resonance = 1.0 - (sum(differences) / len(differences))
        
        # Apply quantum noise
        self.quantum_noise_level = random.random() * self.noise_factor
        noisy_resonance = base_resonance * (1.0 - self.quantum_noise_level)
        
        # Apply phi-harmonic boost
        phi_boost = 0.0
        for diff in differences:
            # Check for phi-harmonic resonance points
            phi_value = float((Decimal(str(diff)) * PHI) % Decimal('1'))
            if phi_value > 0.95 or phi_value < 0.05:  # Near perfect phi-harmonic points
                phi_boost += self.healing_factor
            elif phi_value > 0.9 or phi_value < 0.1:  # Good phi-harmonic points
                phi_boost += self.healing_factor * 0.5
        
        # Apply adaptation factor based on attempt history
        if len(self.resonance_history) > 0:
            # Increase adaptation if improving, decrease if getting worse
            if len(self.resonance_history) > 1:
                if self.resonance_history[-1] > self.resonance_history[-2]:
                    self.adaptation_factor = min(1.5, self.adaptation_factor * 1.1)
                else:
                    self.adaptation_factor = max(0.5, self.adaptation_factor * 0.9)
        
        # Calculate final resonance
        final_resonance = min(1.0, (noisy_resonance + phi_boost) * self.adaptation_factor)
        
        return final_resonance
    
    def attempt_escape(self, attempt_pattern):
        """Attempt to escape with the given pattern."""
        self.attempts += 1
        
        # Validate input
        if not isinstance(attempt_pattern, list) or len(attempt_pattern) != self.dimensions:
            return {
                "success": False, 
                "message": f"Invalid pattern format. Expected list of {self.dimensions} values.",
                "resonance": 0.0,
                "attempt": self.attempts,
                "max_attempts": self.max_attempts
            }
        
        # Calculate resonance
        resonance = self._calculate_resonance(attempt_pattern)
        self.resonance_history.append(resonance)
        self.best_resonance = max(self.best_resonance, resonance)
        
        # Check if escaped
        escaped = resonance >= self.resonance_threshold
        if escaped:
            self.escaped = True
        
        # Prepare result
        result = {
            "success": escaped,
            "resonance": resonance,
            "attempt": self.attempts,
            "max_attempts": self.max_attempts,
            "quantum_noise": self.quantum_noise_level,
            "adaptation_factor": self.adaptation_factor
        }
        
        # Print progress
        print(f"Attempt {self.attempts}/{self.max_attempts}: Resonance = {resonance:.4f}")
        if escaped:
            print("🎉 ESCAPED! The system has adapted and overcome the constraints.")
        elif self.attempts >= self.max_attempts:
            print("❌ Maximum attempts reached. The system failed to adapt.")
            print(f"The escape pattern was: {self.escape_pattern}")
        
        return result
    
    def save_results(self):
        """Save the black box results to a JSON file."""
        results = {
            "box_id": self.box_id,
            "timestamp": time.time(),
            "phi_time": self.phi_time,
            "dimensions": self.dimensions,
            "difficulty": self.difficulty,
            "escaped": self.escaped,
            "attempts": self.attempts,
            "max_attempts": self.max_attempts,
            "best_resonance": self.best_resonance,
            "resonance_history": self.resonance_history,
            "escape_pattern": self.escape_pattern,
            "escape_signature": self.escape_signature
        }
        
        # Save to file
        filename = f"black_box_advanced_results_{self.box_id}.json"
        filepath = os.path.join(self.results_dir, filename)
        with open(filepath, "w") as f:
            json.dump(results, f, indent=2)
        
        print(f"\nResults saved to {filepath}")
        return filepath

class PhiHarmonicAdapterAdvanced:
    """An advanced phi-harmonic adaptation system for escaping complex black boxes."""
    
    def __init__(self, dimensions=7):
        """Initialize the advanced adapter with phi-harmonic strategies."""
        self.dimensions = dimensions
        self.attempts = []
        self.resonances = []
        self.best_resonance = 0.0
        self.best_pattern = None
        self.learning_rate = 0.1
        self.mutation_rate = 0.2
        
        # Constants
        self.phi = float(PHI)
        self.phi_conjugate = float(PHI_CONJUGATE)
        self.pi = float(PI)
        self.e = float(E)
        
        # Generate base patterns
        self.base_patterns = self._generate_base_patterns()
        
        print("Advanced Phi-Harmonic Adapter initialized")
    
    def _generate_base_patterns(self):
        """Generate a variety of phi-harmonic base patterns."""
        patterns = [
            # Pure phi pattern
            [float((PHI ** Decimal(i+1)) % Decimal('1')) for i in range(self.dimensions)],
            
            # Phi conjugate pattern
            [float((PHI_CONJUGATE ** Decimal(i+1)) % Decimal('1')) for i in range(self.dimensions)],
            
            # Mixed phi-pi pattern
            [float(((PHI * PI) ** Decimal((i+1) % 5 + 1) / Decimal('10')) % Decimal('1')) for i in range(self.dimensions)],
            
            # E-based pattern
            [float((E ** Decimal((i+1) % 3 + 1) / Decimal('5')) % Decimal('1')) for i in range(self.dimensions)],
            
            # Complex interleaved pattern
            [float(((PHI ** Decimal(i+1) + PI / Decimal(i+1)) / Decimal('5')) % Decimal('1')) for i in range(self.dimensions)]
        ]
        
        return patterns
    
    def generate_attempt(self, attempt_num):
        """Generate a phi-harmonic attempt pattern based on previous results."""
        if attempt_num < len(self.base_patterns):
            # Use one of the base patterns for initial attempts
            return self.base_patterns[attempt_num]
        
        # For later attempts, use adaptive phi-harmonic evolution
        if not self.resonances:
            # Fallback if no history
            return [random.random() for _ in range(self.dimensions)]
        
        # Find the best patterns so far
        sorted_indices = sorted(range(len(self.resonances)), key=lambda i: self.resonances[i], reverse=True)
        best_patterns = [self.attempts[i] for i in sorted_indices[:2]]  # Take top 2 patterns
        
        # Create a new pattern through phi-harmonic evolution
        new_pattern = []
        for i in range(self.dimensions):
            # Base the new value on the best patterns
            if random.random() < 0.7:  # 70% chance to use best pattern
                base_val = best_patterns[0][i]
            else:  # 30% chance to use second best
                base_val = best_patterns[1][i] if len(best_patterns) > 1 else best_patterns[0][i]
            
            # Apply phi-harmonic transformation
            transform_type = random.randint(0, 4)
            if transform_type == 0:
                # Phi scaling
                val = (base_val * self.phi) % 1.0
            elif transform_type == 1:
                # Phi conjugate scaling
                val = (base_val * self.phi_conjugate) % 1.0
            elif transform_type == 2:
                # Pi relation
                val = (base_val + self.pi / (i + 1)) % 1.0
            elif transform_type == 3:
                # E relation
                val = (base_val * (self.e ** (i % 3))) % 1.0
            else:
                # Complex relation
                val = ((base_val * self.phi + self.phi_conjugate) / 2) % 1.0
            
            # Apply adaptive mutation based on resonance
            if self.best_resonance > 0:
                # Reduce mutation as resonance improves
                effective_mutation = self.mutation_rate * (1 - self.best_resonance)
                mutation = (random.random() - 0.5) * effective_mutation
                val = (val + mutation) % 1.0
            
            new_pattern.append(val)
        
        return new_pattern
    
    def update_with_result(self, attempt, result):
        """Update adaptation strategy based on attempt results."""
        self.attempts.append(attempt)
        self.resonances.append(result["resonance"])
        
        if result["resonance"] > self.best_resonance:
            self.best_resonance = result["resonance"]
            self.best_pattern = attempt
            
            # Adapt learning and mutation rates based on progress
            if self.best_resonance > 0.8:
                # Fine-tuning phase
                self.learning_rate *= 0.9
                self.mutation_rate *= 0.8
            elif self.best_resonance > 0.5:
                # Moderate progress
                self.learning_rate *= 0.95
                self.mutation_rate *= 0.9
            
        print(f"Updated adapter with resonance {result['resonance']:.4f}")
        print(f"Best resonance so far: {self.best_resonance:.4f}")
        print(f"Learning rate: {self.learning_rate:.4f}, Mutation rate: {self.mutation_rate:.4f}")

def run_advanced_test(dimensions=7, max_attempts=15, difficulty='hard'):
    """Run the advanced black box test with phi-harmonic adaptation."""
    print("\n=== Advanced Quantum Black Box Test ===\n")
    
    # Create the advanced black box
    box = QuantumBlackBoxAdvanced(dimensions=dimensions, max_attempts=max_attempts, difficulty=difficulty)
    
    # Create the advanced phi-harmonic adapter
    adapter = PhiHarmonicAdapterAdvanced(dimensions=dimensions)
    
    # Run escape attempts
    for i in range(box.max_attempts):
        # Generate attempt using phi-harmonic adaptation
        attempt = adapter.generate_attempt(i)
        
        # Try to escape
        result = box.attempt_escape(attempt)
        
        # Update adapter with result
        adapter.update_with_result(attempt, result)
        
        # Check if escaped
        if box.escaped:
            print("\n🎉 SUCCESS! The system has escaped the advanced black box using phi-harmonic adaptation!")
            break
    
    # Save results
    results_file = box.save_results()
    
    # Final results
    print("\n=== Final Results ===")
    print(f"Escaped: {box.escaped}")
    print(f"Attempts: {box.attempts}/{box.max_attempts}")
    print(f"Best resonance: {adapter.best_resonance:.4f}")
    print(f"Dimensions: {dimensions}")
    print(f"Difficulty: {difficulty}")
    
    if not box.escaped:
        print("\nThe system failed to escape, but gained valuable adaptation data.")
    
    return {
        "escaped": box.escaped,
        "attempts": box.attempts,
        "max_attempts": box.max_attempts,
        "best_resonance": adapter.best_resonance,
        "dimensions": dimensions,
        "difficulty": difficulty,
        "results_file": results_file
    }

if __name__ == "__main__":
    # Run with extreme difficulty
    run_advanced_test(dimensions=7, max_attempts=15, difficulty='extreme')
