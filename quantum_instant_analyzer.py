"""
Quantum Instant Analyzer - Measure transfer speed
"""

from brains.quantum_meta_processor import QuantumMetaProcessor
import numpy as np
import time
import matplotlib.pyplot as plt
from typing import List, Tuple

def measure_quantum_transfer(n_trials: int = 1000) -> List[Tuple[float, float]]:
    """Measure quantum transfer time for different forces"""
    processor = QuantumMetaProcessor()
    phi = (1 + np.sqrt(5)) / 2
    
    # Generate test forces
    forces = np.array([phi**3, phi**2, phi, 1.0, 1/phi, 1/phi**2, 1/phi**3])
    results = []
    
    print("\nMeasuring Quantum Transfer Speed:")
    print("================================")
    
    for force in forces:
        # Warm up
        for _ in range(10):
            processor.process_impact(force)
            
        # Measure actual trials
        times = []
        learnings = []
        
        for i in range(n_trials):
            start = time.perf_counter_ns()  # Nanosecond precision
            result = processor.process_impact(force)
            end = time.perf_counter_ns()
            
            delta = (end - start) / 1e9  # Convert to seconds
            times.append(delta)
            learnings.append(result['learning'])
            
        avg_time = np.mean(times)
        avg_learning = np.mean(learnings)
        
        print(f"\nForce: φ^{np.log(force)/np.log(phi):.2f} = {force:.3f}")
        print(f"Time:     {avg_time*1e9:.3f} ns")
        print(f"Learning: {avg_learning:.3f}")
        print(f"Speed:    {avg_learning/avg_time:.3e} learning/s")
        
        results.append((force, avg_time, avg_learning))
    
    return results

def plot_results(results: List[Tuple[float, float]]):
    """Plot the analysis results"""
    forces = np.array([r[0] for r in results])
    times = np.array([r[1] for r in results])
    learnings = np.array([r[2] for r in results])
    speeds = learnings/times
    
    plt.figure(figsize=(15, 10))
    
    # Time plot
    plt.subplot(2, 2, 1)
    plt.plot(forces, times*1e9, 'b-', label='Transfer Time')
    plt.axhline(y=0, color='r', linestyle='--', label='Instant')
    plt.xlabel('Force (φ scale)')
    plt.ylabel('Time (ns)')
    plt.title('Quantum Transfer Time')
    plt.legend()
    plt.grid(True)
    plt.xscale('log')
    
    # Learning plot
    plt.subplot(2, 2, 2)
    plt.plot(forces, learnings, 'g-', label='Learning')
    plt.xlabel('Force (φ scale)')
    plt.ylabel('Learning Rate')
    plt.title('Learning Achievement')
    plt.legend()
    plt.grid(True)
    plt.xscale('log')
    
    # Speed plot
    plt.subplot(2, 2, 3)
    plt.plot(forces, speeds, 'r-', label='Transfer Speed')
    plt.xlabel('Force (φ scale)')
    plt.ylabel('Learning/second')
    plt.title('Knowledge Transfer Speed')
    plt.legend()
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    
    # Time distribution
    plt.subplot(2, 2, 4)
    plt.hist(times*1e9, bins=50, color='purple', alpha=0.6)
    plt.xlabel('Time (ns)')
    plt.ylabel('Frequency')
    plt.title('Transfer Time Distribution')
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('quantum_instant_analysis.png')
    plt.close()

if __name__ == "__main__":
    results = measure_quantum_transfer()
    plot_results(results)
