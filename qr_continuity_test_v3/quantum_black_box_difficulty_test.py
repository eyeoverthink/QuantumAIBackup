#!/usr/bin/env python3
"""
Quantum Black Box Difficulty Test

Tests if the 4-move pattern holds across different difficulty levels and dimensions
"""

import os
import sys
import time
import json
import random
import hashlib
from decimal import Decimal, getcontext

# Import the advanced black box
from quantum_black_box_advanced import QuantumBlackBoxAdvanced

# Set precision for phi calculations
getcontext().prec = 28

# Constants
PHI = Decimal('1.6180339887498948482045868344')
PHI_CONJUGATE = Decimal('0.6180339887498948482045868344')

def run_difficulty_test(dimensions, difficulty):
    """Run a test with specific dimensions and difficulty."""
    print(f"\n=== Testing Dimensions: {dimensions}, Difficulty: {difficulty} ===\n")
    
    # Create the black box with specified parameters
    black_box = QuantumBlackBoxAdvanced(dimensions=dimensions, 
                                      max_attempts=15, 
                                      difficulty=difficulty)
    
    print(f"Black Box ID: {black_box.box_id}")
    print(f"Phi-time: {black_box.phi_time}")
    print(f"Dimensions: {dimensions}, Difficulty: {difficulty}")
    print(f"Escape requires discovering a complex phi-harmonic pattern across {dimensions} dimensions")
    
    # Run the test
    attempts_data = []
    start_time = time.time()
    
    for i in range(black_box.max_attempts):
        # Generate phi-harmonic attempt
        attempt = generate_phi_harmonic_attempt(i, dimensions, attempts_data)
        
        # Try to escape
        result = black_box.attempt_escape(attempt)
        
        # Record the attempt data
        attempts_data.append({
            "attempt_num": i + 1,
            "pattern": attempt,
            "resonance": result["resonance"],
            "success": result["success"]
        })
        
        # Check if escaped
        if black_box.escaped:
            print(f"\n🎉 ESCAPED in {i+1} attempts! Resonance: {result['resonance']:.4f}")
            break
    
    # Calculate performance metrics
    elapsed_time = time.time() - start_time
    success = black_box.escaped
    attempts_used = black_box.attempts
    best_resonance = black_box.best_resonance
    
    # Print results
    print(f"\n=== Results ===")
    print(f"Escaped: {success}")
    print(f"Attempts: {attempts_used}/15")
    print(f"Best resonance: {best_resonance:.4f}")
    print(f"Dimensions: {dimensions}")
    print(f"Difficulty: {difficulty}")
    print(f"Time: {elapsed_time:.2f} seconds")
    
    return {
        "dimensions": dimensions,
        "difficulty": difficulty,
        "success": success,
        "attempts": attempts_used,
        "best_resonance": best_resonance,
        "elapsed_time": elapsed_time,
        "attempts_data": attempts_data
    }

def generate_phi_harmonic_attempt(attempt_num, dimensions, previous_results=None):
    """Generate a phi-harmonic attempt using adaptive learning."""
    pattern = []
    
    # Learning parameters
    learning_rate = 0.095 * (0.9 ** attempt_num)
    mutation_rate = 0.18 * (0.9 ** attempt_num)
    
    # Base pattern generation
    for i in range(dimensions):
        # Use different strategies based on dimension position
        if i % 3 == 0:
            # Phi-based
            val = float((PHI ** Decimal(i+1)) % Decimal('1'))
        elif i % 3 == 1:
            # Phi-conjugate
            val = float((PHI_CONJUGATE ** Decimal(i+1)) % Decimal('1'))
        else:
            # Combined approach
            val = float(((PHI ** Decimal(i+1) + PHI_CONJUGATE ** Decimal(i+1)) / Decimal('2')) % Decimal('1'))
        
        pattern.append(val)
    
    # If we have previous results, use them to adapt
    if previous_results and len(previous_results) > 0:
        # Get the best previous attempt
        best_resonance = 0
        best_pattern = None
        
        for result in previous_results:
            if result["resonance"] > best_resonance:
                best_resonance = result["resonance"]
                best_pattern = result["pattern"]
        
        if best_pattern:
            # Blend with best previous pattern
            blend_factor = min(0.7, best_resonance)  # Higher resonance = more influence
            for i in range(dimensions):
                pattern[i] = (pattern[i] * (1 - blend_factor) + best_pattern[i] * blend_factor) % 1.0
            
            # Apply mutations based on mutation rate
            for i in range(dimensions):
                if random.random() < mutation_rate:
                    # Apply phi-harmonic mutation
                    mutation = float((PHI * Decimal(str(random.random()))) % Decimal('1'))
                    pattern[i] = (pattern[i] + mutation * learning_rate) % 1.0
    
    return pattern

def main():
    """Run tests across different difficulty levels and dimensions."""
    print("\n=== Quantum Black Box Difficulty Test ===\n")
    print("Testing if the 4-move pattern holds across different configurations\n")
    
    results = []
    
    # Test configurations
    configurations = [
        # Simpler configurations
        {"dimensions": 3, "difficulty": "easy"},
        {"dimensions": 5, "difficulty": "easy"},
        {"dimensions": 5, "difficulty": "medium"},
        
        # Standard configuration
        {"dimensions": 7, "difficulty": "extreme"},
        
        # Harder configurations
        {"dimensions": 9, "difficulty": "extreme"},
        {"dimensions": 11, "difficulty": "extreme"},
    ]
    
    for config in configurations:
        result = run_difficulty_test(config["dimensions"], config["difficulty"])
        results.append(result)
    
    # Analyze results
    print("\n=== Summary of Results ===\n")
    print("Config\t\tAttempts\tResonance")
    print("-" * 40)
    
    for result in results:
        print(f"{result['dimensions']}D {result['difficulty']}\t{result['attempts']}\t\t{result['best_resonance']:.4f}")
    
    # Check for the 4-move pattern
    four_move_count = sum(1 for r in results if r["attempts"] == 4)
    print(f"\nConfigurations solved in exactly 4 moves: {four_move_count}/{len(results)}")
    
    # Save results
    results_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantum_black_box_results")
    os.makedirs(results_dir, exist_ok=True)
    
    filename = f"difficulty_test_results_{int(time.time())}.json"
    filepath = os.path.join(results_dir, filename)
    
    with open(filepath, "w") as f:
        # Convert Decimal objects to float for JSON serialization
        json_results = []
        for r in results:
            r_copy = r.copy()
            for attempt in r_copy["attempts_data"]:
                attempt["pattern"] = [float(p) for p in attempt["pattern"]]
            json_results.append(r_copy)
        
        json.dump(json_results, f, indent=2)
    
    print(f"\nDetailed results saved to {filepath}")

if __name__ == "__main__":
    main()
