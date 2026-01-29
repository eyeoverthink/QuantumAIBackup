"""
Test double-slit experiment with quantum behavior
"""
import numpy as np
import matplotlib.pyplot as plt
from quantum_interference import DoubleSlit

def test_double_slit():
    # Create double slit experiment
    experiment = DoubleSlit()
    
    # Run experiment with 10000 particles
    print("Running double-slit experiment...")
    results = experiment.run_experiment(num_particles=10000)
    
    # Plot results
    plt.figure(figsize=(10, 6))
    
    # Plot particle counts
    plt.plot(results['screen_positions'], results['counts'], 'b-', label='Particle Counts')
    
    # Mark slit positions
    plt.axvline(x=results['slit1'], color='r', linestyle='--', label='Slit 1')
    plt.axvline(x=results['slit2'], color='r', linestyle='--', label='Slit 2')
    
    plt.title('Double-Slit Experiment Results')
    plt.xlabel('Screen Position')
    plt.ylabel('Particle Count')
    plt.grid(True)
    plt.legend()
    
    # Show interference pattern
    plt.show()

if __name__ == "__main__":
    print("Starting double-slit experiment...")
    test_double_slit()
