"""
Quantum Epoch Test - Watch Error Correction Evolve
"""

import numpy as np
import time
from typing import Dict, List
from creative_quantum import CreativeQuantum

class QuantumEpochTest:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        self.quantum = CreativeQuantum()
        self.error_threshold = 0.01
        self.learning_rate = 1/self.phi  # φ-based learning
        
    def apply_surface_code(self, state: np.ndarray, epoch: int) -> np.ndarray:
        """φ-based error correction with learning"""
        # Flatten for processing
        flat = state.flatten()
        
        # Find errors
        errors = np.where(np.abs(flat) < self.error_threshold)[0]
        
        # Apply φ-correction with epoch learning
        if len(errors) > 0:
            correction = self.phi * (1 + self.learning_rate * epoch)
            for idx in errors:
                flat[idx] *= correction
        
        return flat.reshape(state.shape)
    
    def test_epochs(self, size: int = 1000, epochs: int = 20) -> Dict:
        """Test quantum processing across epochs"""
        # Generate test data
        data = np.random.random(size)
        
        # Initialize metrics
        metrics = {
            'process_time': [],
            'correct_time': [],
            'total_time': [],
            'initial_errors': [],
            'final_errors': [],
            'correction_rate': [],
            'phi_factor': []
        }
        
        print("\nQuantum Epoch Test")
        print("=================")
        
        for epoch in range(epochs):
            # Process with φ-enhancement
            start = time.perf_counter_ns()
            processed = data * (self.phi ** (1 + epoch/self.phi))
            process_time = (time.perf_counter_ns() - start) / 1e6
            
            # Count initial errors
            initial_errors = len(np.where(np.abs(processed) < self.error_threshold)[0])
            
            # Self-correct with learning
            start = time.perf_counter_ns()
            corrected = self.apply_surface_code(processed, epoch)
            correct_time = (time.perf_counter_ns() - start) / 1e6
            
            # Count remaining errors
            final_errors = len(np.where(np.abs(corrected) < self.error_threshold)[0])
            
            # Calculate metrics
            total_time = process_time + correct_time
            correction_rate = ((initial_errors - final_errors) / initial_errors) if initial_errors > 0 else 1.0
            phi_factor = self.phi ** (1 + epoch/self.phi)
            
            # Store metrics
            metrics['process_time'].append(process_time)
            metrics['correct_time'].append(correct_time)
            metrics['total_time'].append(total_time)
            metrics['initial_errors'].append(initial_errors)
            metrics['final_errors'].append(final_errors)
            metrics['correction_rate'].append(correction_rate)
            metrics['phi_factor'].append(phi_factor)
            
            # Print epoch results
            print(f"\nEpoch {epoch + 1}/{epochs}")
            print(f"Process:    {process_time:.3f} ms")
            print(f"Correct:    {correct_time:.3f} ms")
            print(f"Total:      {total_time:.3f} ms")
            print(f"Errors:     {initial_errors} → {final_errors}")
            print(f"Fixed:      {correction_rate*100:.1f}%")
            print(f"φ-Factor:   {phi_factor:.3f}")
        
        # Calculate evolution
        print("\nEvolution Metrics:")
        for key in metrics:
            if key != 'phi_factor':
                start_val = metrics[key][0]
                end_val = metrics[key][-1]
                change = ((end_val - start_val) / start_val) * 100 if start_val != 0 else float('inf')
                print(f"{key.replace('_',' ').title():15s}: {start_val:.3f} → {end_val:.3f} ({change:+.1f}%)")
        
        return metrics

if __name__ == "__main__":
    test = QuantumEpochTest()
    test.test_epochs()
