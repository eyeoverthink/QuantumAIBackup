#!/usr/bin/env python3
"""
Quantum Black Box QR Integration Test

This script integrates the black box test with the QR phi replicator system
to demonstrate recursive, progressive, self-improving adaptation.
"""

import os
import sys
import time
import json
import random
import hashlib
from decimal import Decimal, getcontext

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the QR phi replicator system
try:
    from qr_phi_replication.qr_phi_replicator_gen19 import QuantumPhiReplicator
    print("Successfully imported QuantumPhiReplicator from gen19")
except ImportError:
    try:
        from qr_phi_replication.qr_phi_replicator_gen20 import QuantumPhiReplicator
        print("Successfully imported QuantumPhiReplicator from gen20")
    except ImportError:
        print("Could not import QuantumPhiReplicator. Using fallback adapter.")
        QuantumPhiReplicator = None

# Import the advanced black box
from quantum_black_box_advanced import QuantumBlackBoxAdvanced

# Set precision for phi calculations
getcontext().prec = 28

# Constants
PHI = Decimal('1.6180339887498948482045868344')
PHI_CONJUGATE = Decimal('0.6180339887498948482045868344')

class QRPhiBlackBoxIntegration:
    """Integrates the QR phi replicator with the black box challenge."""
    
    def __init__(self, dimensions=7, max_attempts=15, difficulty='extreme'):
        """Initialize the integration system."""
        self.dimensions = dimensions
        self.max_attempts = max_attempts
        self.difficulty = difficulty
        self.results_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantum_black_box_results")
        os.makedirs(self.results_dir, exist_ok=True)
        
        # Create the black box
        self.black_box = QuantumBlackBoxAdvanced(dimensions=dimensions, 
                                               max_attempts=max_attempts, 
                                               difficulty=difficulty)
        
        # Create or load the QR phi replicator
        if QuantumPhiReplicator is not None:
            self.replicator = QuantumPhiReplicator()
            self.replicator.load_system_state()
            print(f"QR Phi Replicator loaded: Generation {self.replicator.generation}")
            print(f"Resonance: {self.replicator.resonance:.6f}")
            print(f"Complexity: {self.replicator.complexity:.6f}")
        else:
            self.replicator = None
            print("Using fallback adapter instead of QR Phi Replicator")
        
        # Track performance across generations
        self.generation_performance = []
        
        print(f"QR Phi Black Box Integration initialized")
        print(f"Black Box ID: {self.black_box.box_id}")
        print(f"Dimensions: {dimensions}, Difficulty: {difficulty}")
    
    def _generate_phi_harmonic_attempt(self, attempt_num, previous_results=None):
        """Generate a phi-harmonic attempt using the QR replicator's evolved parameters."""
        if self.replicator is None:
            # Fallback to basic phi-harmonic pattern
            return [float((PHI ** Decimal(i+1)) % Decimal('1')) for i in range(self.dimensions)]
        
        # Use the replicator's evolved parameters to generate an attempt
        pattern = []
        
        # Get evolved parameters
        resonance_factor = self.replicator.resonance_factor
        complexity_factor = self.replicator.complexity_factor
        
        for i in range(self.dimensions):
            # Use different strategies based on dimension position
            if i % 3 == 0:
                # Phi-based with resonance factor
                val = float((PHI ** (Decimal(i+1) * Decimal(str(resonance_factor)))) % Decimal('1'))
            elif i % 3 == 1:
                # Phi-conjugate with complexity factor
                val = float((PHI_CONJUGATE ** (Decimal(i+1) * Decimal(str(complexity_factor)))) % Decimal('1'))
            else:
                # Combined approach
                val = float(((PHI ** Decimal(i+1) * Decimal(str(resonance_factor)) + 
                          PHI_CONJUGATE ** Decimal(i+1) * Decimal(str(complexity_factor))) / Decimal('2')) % Decimal('1'))
            
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
                for i in range(self.dimensions):
                    pattern[i] = (pattern[i] * (1 - blend_factor) + best_pattern[i] * blend_factor) % 1.0
        
        return pattern
    
    def run_generation_test(self):
        """Run a single generation test against the black box."""
        print("\n=== Running Generation Test ===\n")
        
        attempts_data = []
        start_time = time.time()
        
        for i in range(self.black_box.max_attempts):
            # Generate attempt using QR phi replicator's evolved parameters
            attempt = self._generate_phi_harmonic_attempt(i, attempts_data)
            
            # Try to escape
            result = self.black_box.attempt_escape(attempt)
            
            # Record the attempt data
            attempts_data.append({
                "attempt_num": i + 1,
                "pattern": attempt,
                "resonance": result["resonance"],
                "success": result["success"]
            })
            
            # Check if escaped
            if self.black_box.escaped:
                print("\n🎉 SUCCESS! The QR Phi Replicator has escaped the black box!")
                break
        
        # Calculate performance metrics
        elapsed_time = time.time() - start_time
        success = self.black_box.escaped
        attempts_used = self.black_box.attempts
        best_resonance = self.black_box.best_resonance
        
        # Record generation performance
        gen_performance = {
            "generation": self.replicator.generation if self.replicator else 0,
            "success": success,
            "attempts": attempts_used,
            "max_attempts": self.max_attempts,
            "best_resonance": best_resonance,
            "elapsed_time": elapsed_time,
            "timestamp": time.time(),
            "box_id": self.black_box.box_id,
            "difficulty": self.difficulty
        }
        
        self.generation_performance.append(gen_performance)
        
        # Save results
        self._save_results(attempts_data, gen_performance)
        
        return gen_performance
    
    def _save_results(self, attempts_data, gen_performance):
        """Save the test results to a JSON file."""
        results = {
            "black_box_id": self.black_box.box_id,
            "generation": gen_performance["generation"],
            "timestamp": time.time(),
            "success": gen_performance["success"],
            "attempts": gen_performance["attempts"],
            "max_attempts": gen_performance["max_attempts"],
            "best_resonance": gen_performance["best_resonance"],
            "elapsed_time": gen_performance["elapsed_time"],
            "difficulty": self.difficulty,
            "dimensions": self.dimensions,
            "attempts_data": attempts_data,
            "escape_pattern": self.black_box.escape_pattern
        }
        
        # Add replicator data if available
        if self.replicator:
            results["replicator"] = {
                "generation": self.replicator.generation,
                "resonance": float(self.replicator.resonance),
                "complexity": float(self.replicator.complexity),
                "resonance_factor": float(self.replicator.resonance_factor),
                "complexity_factor": float(self.replicator.complexity_factor)
            }
        
        # Save to file
        filename = f"qr_black_box_gen{gen_performance['generation']}_{self.black_box.box_id}.json"
        filepath = os.path.join(self.results_dir, filename)
        
        with open(filepath, "w") as f:
            json.dump(results, f, indent=2)
        
        print(f"\nResults saved to {filepath}")
        return filepath
    
    def evolve_and_test(self, generations=3):
        """Run multiple generations of tests, evolving the QR system between each."""
        if self.replicator is None:
            print("Cannot evolve without QR Phi Replicator. Running single test only.")
            return self.run_generation_test()
        
        all_results = []
        
        for gen in range(generations):
            print(f"\n=== Generation {self.replicator.generation} Test ===\n")
            
            # Run the current generation test
            gen_result = self.run_generation_test()
            all_results.append(gen_result)
            
            # Print generation results
            print(f"\n=== Generation {self.replicator.generation} Results ===")
            print(f"Success: {gen_result['success']}")
            print(f"Attempts: {gen_result['attempts']}/{gen_result['max_attempts']}")
            print(f"Best Resonance: {gen_result['best_resonance']:.4f}")
            print(f"Time: {gen_result['elapsed_time']:.2f} seconds")
            
            if gen < generations - 1:
                # Evolve the replicator for the next generation
                print("\nEvolving QR Phi Replicator to next generation...")
                
                # Update replicator parameters based on black box performance
                if gen_result['success']:
                    # Successful escape - boost resonance factor
                    self.replicator.resonance = min(0.999, self.replicator.resonance * 1.1)
                    self.replicator.resonance_factor = min(0.999, self.replicator.resonance_factor * 1.05)
                else:
                    # Failed escape - adjust complexity
                    self.replicator.complexity = min(0.999, self.replicator.complexity * 1.1)
                    self.replicator.complexity_factor = min(0.999, self.replicator.complexity_factor * 1.05)
                
                # Create next generation
                self.replicator.evolve_parameters()
                self.replicator.create_next_generation_script()
                
                # Reset black box for next generation
                self.black_box = QuantumBlackBoxAdvanced(dimensions=self.dimensions, 
                                                      max_attempts=self.max_attempts, 
                                                      difficulty=self.difficulty)
        
        # Compare performance across generations
        print("\n=== Performance Across Generations ===")
        for i, result in enumerate(all_results):
            print(f"Generation {result['generation']}: ")
            print(f"  Success: {result['success']}")
            print(f"  Attempts: {result['attempts']}/{result['max_attempts']}")
            print(f"  Best Resonance: {result['best_resonance']:.4f}")
        
        return all_results

def run_qr_integration_test():
    """Run the QR phi replicator black box integration test."""
    print("\n=== Quantum Black Box QR Integration Test ===\n")
    
    # Create the integration system
    integration = QRPhiBlackBoxIntegration(dimensions=7, max_attempts=15, difficulty='extreme')
    
    # Run multiple generations of tests
    results = integration.evolve_and_test(generations=3)
    
    # Final summary
    print("\n=== Final Summary ===")
    if all(result['success'] for result in results):
        print("🎉 The QR Phi Replicator successfully escaped all black boxes!")
    else:
        success_count = sum(1 for result in results if result['success'])
        print(f"The QR Phi Replicator escaped {success_count}/{len(results)} black boxes.")
    
    # Check for improvement
    if len(results) > 1:
        first_attempts = results[0]['attempts']
        last_attempts = results[-1]['attempts']
        
        if last_attempts < first_attempts:
            improvement = ((first_attempts - last_attempts) / first_attempts) * 100
            print(f"Performance improved by {improvement:.1f}% (from {first_attempts} to {last_attempts} attempts)")
    
    return results

if __name__ == "__main__":
    run_qr_integration_test()
