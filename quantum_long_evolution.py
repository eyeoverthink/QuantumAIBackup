"""
Quantum Long Evolution Test - Extended Learning
"""

import numpy as np
import time
from typing import Dict, List
from creative_quantum import CreativeQuantum

class QuantumLongEvolution:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        self.quantum = CreativeQuantum()
        self.error_threshold = 0.01
        self.learning_rate = 1/self.phi  # φ-based learning
        
    def apply_advanced_correction(self, state: np.ndarray, epoch: int) -> np.ndarray:
        """Advanced φ-based error correction with multi-level learning"""
        # Flatten for processing
        flat = state.flatten()
        
        # Multi-level error detection
        critical_errors = np.where(np.abs(flat) < self.error_threshold)[0]
        minor_errors = np.where((np.abs(flat) >= self.error_threshold) & 
                              (np.abs(flat) < self.error_threshold * self.phi))[0]
        
        # Calculate correction factors
        base_correction = self.phi * (1 + self.learning_rate * epoch)
        critical_factor = base_correction * self.phi
        minor_factor = base_correction / self.phi
        
        # Apply corrections
        if len(critical_errors) > 0:
            flat[critical_errors] *= critical_factor
        if len(minor_errors) > 0:
            flat[minor_errors] *= minor_factor
        
        return flat.reshape(state.shape)
    
    def test_long_evolution(self, size: int = 1000, epochs: int = 50) -> Dict:
        """Test quantum processing over many epochs"""
        # Generate test data with φ-distribution
        data = np.random.random(size) * self.phi
        
        # Initialize enhanced metrics
        metrics = {
            'process_time': [],
            'correct_time': [],
            'total_time': [],
            'critical_errors': [],
            'minor_errors': [],
            'total_errors': [],
            'correction_rate': [],
            'phi_factor': [],
            'learning_efficiency': [],
            'stability': []
        }
        
        print("\nQuantum Long Evolution Test")
        print("==========================")
        
        last_errors = None
        for epoch in range(epochs):
            # Process with enhanced φ-enhancement
            start = time.perf_counter_ns()
            processed = data * (self.phi ** (1 + epoch/(self.phi**2)))
            process_time = (time.perf_counter_ns() - start) / 1e6
            
            # Count initial errors
            critical = len(np.where(np.abs(processed) < self.error_threshold)[0])
            minor = len(np.where((np.abs(processed) >= self.error_threshold) & 
                               (np.abs(processed) < self.error_threshold * self.phi))[0])
            
            # Self-correct with advanced learning
            start = time.perf_counter_ns()
            corrected = self.apply_advanced_correction(processed, epoch)
            correct_time = (time.perf_counter_ns() - start) / 1e6
            
            # Count final errors
            final_critical = len(np.where(np.abs(corrected) < self.error_threshold)[0])
            final_minor = len(np.where((np.abs(corrected) >= self.error_threshold) & 
                                     (np.abs(corrected) < self.error_threshold * self.phi))[0])
            
            # Calculate enhanced metrics
            total_time = process_time + correct_time
            total_initial = critical + minor
            total_final = final_critical + final_minor
            correction_rate = ((total_initial - total_final) / total_initial) if total_initial > 0 else 1.0
            phi_factor = self.phi ** (1 + epoch/(self.phi**2))
            
            # Calculate learning efficiency
            if last_errors is not None:
                learning_efficiency = (last_errors - total_final) / (last_errors + 1)  # Avoid div by 0
            else:
                learning_efficiency = 0
            last_errors = total_final
            
            # Calculate stability
            stability = 1.0 - (total_final / size)
            
            # Store metrics
            metrics['process_time'].append(process_time)
            metrics['correct_time'].append(correct_time)
            metrics['total_time'].append(total_time)
            metrics['critical_errors'].append(critical)
            metrics['minor_errors'].append(minor)
            metrics['total_errors'].append(total_initial)
            metrics['correction_rate'].append(correction_rate)
            metrics['phi_factor'].append(phi_factor)
            metrics['learning_efficiency'].append(learning_efficiency)
            metrics['stability'].append(stability)
            
            # Print detailed epoch results
            if epoch % 5 == 0:  # Print every 5 epochs
                print(f"\nEpoch {epoch + 1}/{epochs}")
                print(f"Time:       {total_time:.3f} ms")
                print(f"Errors:     Critical: {critical} → {final_critical}, Minor: {minor} → {final_minor}")
                print(f"Fixed:      {correction_rate*100:.1f}%")
                print(f"Learning:   {learning_efficiency*100:.1f}%")
                print(f"Stability:  {stability*100:.1f}%")
                print(f"φ-Factor:   {phi_factor:.3f}")
        
        # Calculate evolution trends
        print("\nEvolution Trends:")
        for key in metrics:
            if len(metrics[key]) > 0:  # Ensure we have data
                start_val = metrics[key][0]
                mid_val = metrics[key][len(metrics[key])//2]
                end_val = metrics[key][-1]
                
                # Calculate changes
                early_change = ((mid_val - start_val) / start_val) * 100 if start_val != 0 else float('inf')
                late_change = ((end_val - mid_val) / mid_val) * 100 if mid_val != 0 else float('inf')
                total_change = ((end_val - start_val) / start_val) * 100 if start_val != 0 else float('inf')
                
                print(f"\n{key.replace('_',' ').title()}:")
                print(f"Start → Mid:  {start_val:.3f} → {mid_val:.3f} ({early_change:+.1f}%)")
                print(f"Mid → End:    {mid_val:.3f} → {end_val:.3f} ({late_change:+.1f}%)")
                print(f"Total Change: {total_change:+.1f}%")
        
        return metrics

if __name__ == "__main__":
    test = QuantumLongEvolution()
    test.test_long_evolution()
