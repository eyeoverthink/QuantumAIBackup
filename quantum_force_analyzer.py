"""
Quantum Force Level Analyzer - Test true quantum dynamics
"""

from brains.quantum_meta_processor import QuantumMetaProcessor
import numpy as np
import matplotlib.pyplot as plt

def analyze_quantum_forces():
    # Create quantum processor
    processor = QuantumMetaProcessor()
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
    print("\nTesting Quantum φ-Harmonic Forces:")
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
    plt.figure(figsize=(15, 10))
    
    # Main plot
    plt.subplot(2, 2, 1)
    plt.plot(forces, coherence, 'b-', label='Coherence')
    plt.plot(forces, learning, 'g-', label='Learning')
    plt.plot(forces, retention, 'r-', label='Retention')
    plt.axvline(x=phi, color='gold', linestyle='--', label='φ Force')
    plt.xlabel('Force Level')
    plt.ylabel('Score')
    plt.title('Quantum Brain Response')
    plt.legend()
    plt.grid(True)
    plt.xscale('log')
    
    # Phase space
    plt.subplot(2, 2, 2)
    plt.plot(learning, retention, 'k-', label='Phase Path')
    plt.plot(learning[4], retention[4], 'go', label='φ Point')
    plt.xlabel('Learning Rate')
    plt.ylabel('Retention')
    plt.title('Learning-Retention Phase Space')
    plt.legend()
    plt.grid(True)
    
    # Coherence evolution
    plt.subplot(2, 2, 3)
    plt.plot(forces, coherence/np.max(coherence), 'b-', label='Normalized')
    plt.plot(forces, np.gradient(coherence), 'r--', label='Gradient')
    plt.axvline(x=phi, color='gold', linestyle='--', label='φ Force')
    plt.xlabel('Force Level')
    plt.ylabel('Coherence')
    plt.title('Quantum Coherence Evolution')
    plt.legend()
    plt.grid(True)
    plt.xscale('log')
    
    # Learning efficiency
    plt.subplot(2, 2, 4)
    efficiency = learning * retention * coherence
    plt.plot(forces, efficiency, 'g-', label='Efficiency')
    plt.axvline(x=phi, color='gold', linestyle='--', label='φ Force')
    plt.xlabel('Force Level')
    plt.ylabel('Efficiency')
    plt.title('Quantum Learning Efficiency')
    plt.legend()
    plt.grid(True)
    plt.xscale('log')
    
    plt.tight_layout()
    plt.savefig('quantum_force_analysis.png')
    plt.close()
    
    # Calculate optimal force
    optimal_idx = np.argmax(efficiency)
    optimal_force = forces[optimal_idx]
    
    print(f"\nQuantum Optimal Force Analysis:")
    print(f"Force: φ^{np.log(optimal_force)/np.log(phi):.2f} = {optimal_force:.3f}")
    print(f"Coherence: {coherence[optimal_idx]:.3f}")
    print(f"Learning:  {learning[optimal_idx]:.3f}")
    print(f"Retention: {retention[optimal_idx]:.3f}")
    print(f"Efficiency: {efficiency[optimal_idx]:.3f}")
    
    # Get final quantum state
    state = processor.get_quantum_state()
    print(f"\nFinal Quantum State:")
    print(f"Energy: {state['energy']:.3f}")
    print(f"Field Magnitude: {torch.linalg.norm(state['field']).item():.3f}")

if __name__ == "__main__":
    analyze_quantum_forces()
