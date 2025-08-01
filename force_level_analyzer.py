"""
Force Level Analyzer - Test φ-harmonic force impacts
"""

from brains.meta_processor import MetaProcessor
import numpy as np
import matplotlib.pyplot as plt

def analyze_force_levels():
    # Create processor
    processor = MetaProcessor()
    phi = (1 + np.sqrt(5)) / 2
    
    # Generate φ-harmonic forces
    forces = np.array([
        1/phi**3,      # Sub-harmonic
        1/phi**2,      # Sub-harmonic
        1/phi,         # Sub-harmonic
        1.0,          # Base
        phi,          # Golden force
        phi**2,       # Super-harmonic
        phi**3        # Super-harmonic
    ])
    
    # Test each force
    results = []
    print("\nTesting φ-Harmonic Forces:")
    for force in forces:
        result = processor.process_impact(force)
        results.append(result)
        print(f"\nForce: φ^{np.log(force)/np.log(phi):.2f} = {force:.3f}")
        print(f"Coherence: {result['coherence']:.3f}")
        print(f"Learning:  {result['learning']:.3f}")
        print(f"Retention: {result['retention']:.3f}")
    
    # Convert to arrays
    forces = np.array(forces)
    coherence = np.array([r['coherence'] for r in results])
    learning = np.array([r['learning'] for r in results])
    retention = np.array([r['retention'] for r in results])
    
    # Plot results
    plt.figure(figsize=(12, 8))
    
    # Main plot
    plt.subplot(2, 1, 1)
    plt.plot(forces, coherence, 'b-', label='Coherence')
    plt.plot(forces, learning, 'g-', label='Learning')
    plt.plot(forces, retention, 'r-', label='Retention')
    plt.axvline(x=phi, color='gold', linestyle='--', label='φ Force')
    plt.xlabel('Force Level')
    plt.ylabel('Score')
    plt.title('Brain Response to φ-Harmonic Forces')
    plt.legend()
    plt.grid(True)
    plt.xscale('log')
    
    # Phase plot
    plt.subplot(2, 1, 2)
    plt.plot(learning, retention, 'k-', label='Learning-Retention')
    plt.plot(learning[4], retention[4], 'go', label='φ Point')
    plt.xlabel('Learning Rate')
    plt.ylabel('Retention')
    plt.title('Learning-Retention Phase Space')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('force_analysis.png')
    plt.close()
    
    # Calculate optimal force
    optimal_idx = np.argmax(learning * retention * coherence)
    optimal_force = forces[optimal_idx]
    
    print(f"\nOptimal Force Analysis:")
    print(f"Force: φ^{np.log(optimal_force)/np.log(phi):.2f} = {optimal_force:.3f}")
    print(f"Coherence: {coherence[optimal_idx]:.3f}")
    print(f"Learning:  {learning[optimal_idx]:.3f}")
    print(f"Retention: {retention[optimal_idx]:.3f}")
    print(f"Total Score: {(learning[optimal_idx] * retention[optimal_idx] * coherence[optimal_idx]):.3f}")

if __name__ == "__main__":
    analyze_force_levels()
