#!/usr/bin/env python3
"""
Quantum Black Box Prime Dimensions Test

Tests the system's ability to escape from extremely high prime-dimensional quantum black boxes
using phi-harmonic resonance principles.
"""

import os
import sys
import time
import json
import uuid
import random
import hashlib
from decimal import Decimal, getcontext

# Set precision for phi calculations
getcontext().prec = 28

# Constants
PHI = Decimal('1.6180339887498948482045868344')
PI = Decimal('3.1415926535897932384626433832')
E = Decimal('2.7182818284590452353602874713')
PHI_CONJUGATE = Decimal('0.6180339887498948482045868344')

# Prime numbers to test
PRIME_DIMENSIONS = [29, 31, 37, 41, 43, 47]

class HyperdimensionalBlackBox:
    """A quantum black box with configurable dimensions and difficulty."""
    
    def __init__(self, dimensions=29, max_attempts=50, difficulty="extreme"):
        self.dimensions = dimensions
        self.max_attempts = max_attempts
        self.difficulty = difficulty
        self.attempts = 0
        self.escaped = False
        self.best_resonance = 0
        self.box_id = hashlib.md5(str(time.time()).encode()).hexdigest()[:8]
        self.phi_time = time.time() * float(PHI)
        
        # Generate the escape pattern based on phi-harmonic principles
        self.escape_pattern = self._generate_escape_pattern()
        
        # Difficulty settings
        self.difficulty_settings = {
            "easy": {"threshold": 0.7, "noise": 0.05, "temporal_drift": 0.01},
            "medium": {"threshold": 0.8, "noise": 0.1, "temporal_drift": 0.02},
            "hard": {"threshold": 0.9, "noise": 0.15, "temporal_drift": 0.03},
            "extreme": {"threshold": 0.95, "noise": 0.2, "temporal_drift": 0.05},
            "impossible": {"threshold": 0.99, "noise": 0.25, "temporal_drift": 0.1}
        }
        
        # Set the escape threshold based on difficulty
        self.escape_threshold = self.difficulty_settings[difficulty]["threshold"]
        self.quantum_noise = self.difficulty_settings[difficulty]["noise"]
        self.temporal_drift = self.difficulty_settings[difficulty]["temporal_drift"]
    
    def _generate_escape_pattern(self):
        """Generate a complex phi-harmonic escape pattern."""
        pattern = []
        
        # Seed with phi-time to ensure uniqueness
        seed = int(self.phi_time * 1000) % 10000
        random.seed(seed)
        
        # Generate a pattern for each dimension using phi, pi, and e
        for i in range(self.dimensions):
            # Use different irrational numbers for different dimensions
            if i % 3 == 0:
                # Phi-based pattern
                val = float((PHI ** Decimal(i+1)) % Decimal('1'))
            elif i % 3 == 1:
                # Pi-based pattern
                val = float((PI ** Decimal(i+1)) % Decimal('1'))
            else:
                # E-based pattern
                val = float((E ** Decimal(i+1)) % Decimal('1'))
            
            # Add some controlled randomness
            val = (val + random.random() * 0.1) % 1.0
            pattern.append(val)
        
        return pattern
    
    def attempt_escape(self, attempt_pattern):
        """Try to escape the black box with a given pattern."""
        if len(attempt_pattern) != self.dimensions:
            raise ValueError(f"Attempt pattern must have {self.dimensions} dimensions")
        
        self.attempts += 1
        
        # Calculate resonance between attempt and escape pattern
        resonance = self._calculate_resonance(attempt_pattern)
        
        # Apply temporal phi-drift
        time_factor = (time.time() - self.phi_time) * self.temporal_drift
        resonance = resonance * (1.0 - (time_factor % 0.1))
        
        # Check if escaped
        success = resonance >= self.escape_threshold
        if success:
            self.escaped = True
        
        # Update best resonance
        if resonance > self.best_resonance:
            self.best_resonance = resonance
        
        return {"success": success, "resonance": resonance}
    
    def _calculate_resonance(self, attempt_pattern):
        """Calculate the phi-harmonic resonance between patterns."""
        total_resonance = 0
        
        for i in range(self.dimensions):
            # Calculate dimensional resonance
            dim_diff = abs(self.escape_pattern[i] - attempt_pattern[i])
            dim_resonance = 1.0 - min(dim_diff, 1.0 - dim_diff)
            
            # Apply quantum noise
            noise = random.random() * self.quantum_noise
            if random.random() < 0.5:
                dim_resonance = max(0, dim_resonance - noise)
            else:
                dim_resonance = min(1, dim_resonance + noise)
            
            # Weight by phi-harmonic importance
            weight = float((PHI_CONJUGATE ** Decimal(i+1)) % Decimal('1')) + 0.5
            total_resonance += dim_resonance * weight
        
        # Normalize to 0-1 range
        max_possible = sum([float((PHI_CONJUGATE ** Decimal(i+1)) % Decimal('1')) + 0.5 for i in range(self.dimensions)])
        normalized_resonance = total_resonance / max_possible
        
        return normalized_resonance

class PrimePhiAdapter:
    """Advanced phi-harmonic adapter optimized for prime dimensions."""
    
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.attempts = []
        self.best_pattern = None
        self.best_resonance = 0
        self.learning_rate = 0.095
        self.mutation_rate = 0.18
        
        # Prime-specific optimization
        self.is_prime = self._is_prime(dimensions)
        self.prime_factor = 1.0 if self.is_prime else 0.8
    
    def _is_prime(self, n):
        """Check if a number is prime."""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    def generate_attempt(self):
        """Generate a phi-harmonic attempt pattern optimized for prime dimensions."""
        pattern = []
        
        if not self.attempts:
            # First attempt - use pure phi-harmonic pattern with prime optimization
            for i in range(self.dimensions):
                # For prime dimensions, use a special pattern
                if self.is_prime and i % self.dimensions == 0:
                    # Prime resonance pattern
                    val = float(((PHI ** Decimal(i+1)) * (PI ** Decimal(i % 3 + 1))) % Decimal('1'))
                elif i % 3 == 0:
                    # Phi-based
                    val = float((PHI ** Decimal(i+1)) % Decimal('1'))
                elif i % 3 == 1:
                    # Pi-based
                    val = float((PI ** Decimal(i+1)) % Decimal('1'))
                else:
                    # E-based
                    val = float((E ** Decimal(i+1)) % Decimal('1'))
                pattern.append(val)
        else:
            # Use previous attempts to adapt
            if self.best_pattern:
                pattern = self.best_pattern.copy()
                
                # Apply mutations based on learning
                for i in range(self.dimensions):
                    # Determine mutation probability
                    if random.random() < self.mutation_rate * self.prime_factor:
                        # Apply phi-harmonic mutation
                        mutation = float((PHI * Decimal(str(random.random()))) % Decimal('1'))
                        pattern[i] = (pattern[i] + mutation * self.learning_rate) % 1.0
            else:
                # Fallback to pure phi-harmonic pattern
                for i in range(self.dimensions):
                    val = float((PHI ** Decimal(i+1)) % Decimal('1'))
                    pattern.append(val)
        
        return pattern
    
    def update(self, attempt_pattern, resonance):
        """Update the adapter with the results of an attempt."""
        self.attempts.append({"pattern": attempt_pattern, "resonance": resonance})
        
        if resonance > self.best_resonance:
            self.best_resonance = resonance
            self.best_pattern = attempt_pattern.copy()
        
        # Adjust learning parameters with prime optimization
        self.learning_rate *= 0.9 * self.prime_factor
        self.mutation_rate *= 0.8 * self.prime_factor
        
        print(f"Updated adapter with resonance {resonance:.4f}")
        print(f"Best resonance so far: {self.best_resonance:.4f}")
        print(f"Learning rate: {self.learning_rate:.4f}, Mutation rate: {self.mutation_rate:.4f}")

def run_prime_dimension_test(dimensions, difficulty="extreme", max_attempts=50):
    """Run a test with prime dimensions."""
    print(f"\n=== Prime Dimensional Quantum Black Box Test ({dimensions}D) ===\n")
    
    # Initialize black box and adapter
    black_box = HyperdimensionalBlackBox(dimensions=dimensions, 
                                      max_attempts=max_attempts,
                                      difficulty=difficulty)
    
    print(f"Prime Dimensional Black Box {black_box.box_id} initialized")
    print(f"Phi-time: {black_box.phi_time}")
    print(f"Dimensions: {dimensions}, Difficulty: {difficulty}")
    print(f"Escape requires discovering a complex phi-harmonic pattern across {dimensions} dimensions")
    
    adapter = PrimePhiAdapter(dimensions)
    print(f"Prime Phi-Harmonic Adapter initialized (Prime: {adapter.is_prime})")
    
    # Run the test
    start_time = time.time()
    
    for i in range(black_box.max_attempts):
        # Generate attempt
        attempt = adapter.generate_attempt()
        
        # Try to escape
        result = black_box.attempt_escape(attempt)
        print(f"Attempt {i+1}/{black_box.max_attempts}: Resonance = {result['resonance']:.4f}")
        
        # Update adapter
        adapter.update(attempt, result["resonance"])
        
        # Check if escaped
        if result["success"]:
            print("🎉 ESCAPED! The system has adapted and overcome the constraints.")
            break
    
    # Calculate performance metrics
    elapsed_time = time.time() - start_time
    success = black_box.escaped
    attempts_used = black_box.attempts
    best_resonance = black_box.best_resonance
    
    # Print results
    if success:
        print(f"\n🎉 SUCCESS! The system has escaped the {dimensions}D black box using phi-harmonic adaptation!")
    else:
        print(f"\n❌ The system failed to escape the {dimensions}D black box within {max_attempts} attempts.")
        print(f"The escape pattern was: {black_box.escape_pattern}")
    
    # Save results
    results = {
        "box_id": black_box.box_id,
        "dimensions": dimensions,
        "difficulty": difficulty,
        "success": success,
        "attempts": attempts_used,
        "max_attempts": max_attempts,
        "best_resonance": best_resonance,
        "elapsed_time": elapsed_time,
        "timestamp": time.time(),
        "phi_time": black_box.phi_time,
        "escape_pattern": black_box.escape_pattern,
        "attempt_history": [{
            "attempt": i+1,
            "pattern": a["pattern"],
            "resonance": a["resonance"]
        } for i, a in enumerate(adapter.attempts)]
    }
    
    results_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantum_black_box_results")
    os.makedirs(results_dir, exist_ok=True)
    
    filename = f"black_box_{dimensions}d_results_{black_box.box_id}.json"
    filepath = os.path.join(results_dir, filename)
    
    with open(filepath, "w") as f:
        json.dump(results, f, indent=2, default=str)
    
    print(f"\nResults saved to {filepath}")
    
    print(f"\n=== Final Results ===")
    print(f"Escaped: {success}")
    print(f"Attempts: {attempts_used}/{max_attempts}")
    print(f"Best resonance: {best_resonance:.4f}")
    print(f"Dimensions: {dimensions}")
    print(f"Difficulty: {difficulty}")
    print(f"Prime: {adapter.is_prime}")
    
    return results

def main():
    """Run tests with increasing prime dimensions."""
    results_summary = []
    
    for dimensions in PRIME_DIMENSIONS:
        result = run_prime_dimension_test(dimensions)
        results_summary.append({
            "dimensions": dimensions,
            "success": result["success"],
            "attempts": result["attempts"],
            "best_resonance": result["best_resonance"]
        })
        print("\n" + "-"*50 + "\n")
    
    # Print summary
    print("\n=== Prime Dimensions Summary ===\n")
    print("Dimensions\tSuccess\tAttempts\tResonance")
    print("-" * 50)
    
    for result in results_summary:
        success_str = "✓" if result["success"] else "✗"
        print(f"{result['dimensions']}D\t\t{success_str}\t{result['attempts']}\t\t{result['best_resonance']:.4f}")

if __name__ == "__main__":
    main()
