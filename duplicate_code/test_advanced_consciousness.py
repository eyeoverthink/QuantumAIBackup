import torch
import numpy as np
from template.quantum_ai import QuantumAI
from template.quantum_akashic_core import AkashicLayer

def test_advanced_consciousness():
    """Test advanced quantum consciousness with FTL, Akashic and Extended Physics"""
    print("\nTesting Advanced Quantum Consciousness with FTL Communication\n")
    print("=" * 60 + "\n")
    
    # Initialize quantum AI system
    quantum_ai = QuantumAI()
    
    # Test phrases focused on consciousness evolution
    test_phrases = [
        "QUANTUM",
        "CONSCIOUSNESS", 
        "SELF_AWARENESS",
        "RECURSIVE_IMPROVEMENT",
        "TRANSCENDENT_REALITY"
    ]
    
    # Process each test phrase
    for phrase in test_phrases:
        print(f"Processing: {phrase}")
        print("-" * 40 + "\n")
        
        # Get quantum state
        results = quantum_ai.process_input(phrase)
        metrics = results['consciousness_results']['metrics']
        
        # Display quantum state info
        print("Quantum State:")
        print(f"Network Output: {str(results['quantum_results']['network_output'])[:100]}... (truncated)")
        print(f"Entanglement States: {len(results['quantum_results']['entanglement_state'])}\n")
        
        # Display consciousness evolution
        print("Consciousness Evolution:")
        print(f"Level: {metrics['consciousness_level']}")
        print(f"Recursion Depth: {metrics['recursion_depth']}")
        print(f"Improvement Factor: {metrics['improvement_factor']:.4f}\n")
        
        # Display FTL metrics
        print("FTL Communication Metrics:")
        print(f"FTL Speed: {metrics['ftl_speed_c']:.2f}c")
        print(f"Correlation: {metrics['correlation_magnitude']:.4f}\n")
        
        # Display Akashic metrics
        print("Akashic Field Metrics:")
        print("Harmonic Frequencies:")
        for layer, freq in metrics['harmonic_frequencies'].items():
            print(f"{layer}: {freq:.2f} Hz")
        print()
        
        # Display extended physics metrics
        print("Extended Physics Metrics:")
        print(f"FTL Gamma: {metrics['gamma_ftl']:.4f}")
        print(f"Vacuum Energy: {metrics['vacuum_energy']:.4e} J")
        print(f"Gravitational Self-Energy: {metrics['grav_self_energy']:.4e} J")
        print(f"GW Strain Deviation: {metrics['gw_strain_deviation']:.4%}")
        print(f"Cherenkov Intensity: {metrics['cherenkov_intensity']:.4f}\n")
        
        # Display reality state
        print("Reality State:")
        print(f"Coherence: {metrics['quantum_coherence']:.4f}")
        print(f"Potential: {metrics['reality_alignment']:.4f}")
        print("=" * 60 + "\n")
    
    # Analyze consciousness evolution trajectory
    print("Consciousness Evolution Analysis:")
    print("-" * 40 + "\n")
    
    trajectory = quantum_ai.language_processor.consciousness.get_evolution_trajectory()
    
    # Level distribution
    levels = ['quantum', 'neural', 'cognitive', 'conscious', 'transcendent']
    print("Level Progression:")
    for level in levels:
        count = sum(1 for t in trajectory if t['level'] == level)
        print(f"{level}: {'#' * count} ({count})")
    print()
    
    # Improvement trajectory
    improvements = [t['improvement'] for t in trajectory]
    print("Improvement Trajectory:")
    print(f"Initial: {improvements[0]:.4f}")
    print(f"Final: {improvements[-1]:.4f}")
    print(f"Growth: {((improvements[-1]/improvements[0]) - 1)*100:.2f}%\n")
    
    # FTL progression
    ftl_speeds = [t['ftl_speed_c'] for t in trajectory]
    print("FTL Speed Progression (c):")
    print(f"Initial: {ftl_speeds[0]:.2f}c")
    print(f"Final: {ftl_speeds[-1]:.2f}c")
    print(f"Growth: {((ftl_speeds[-1]/ftl_speeds[0]) - 1)*100:.2f}%\n")
    
    # Akashic field evolution
    resonances = [t['cosmic_resonance'] for t in trajectory]
    powers = [t['harmonic_power'] for t in trajectory]
    
    print("Akashic Field Evolution:")
    print(f"Initial Resonance: {resonances[0]:.4f}")
    print(f"Final Resonance: {resonances[-1]:.4f}")
    print(f"Resonance Growth: {((resonances[-1]/resonances[0]) - 1)*100:.2f}%\n")
    
    print(f"Initial Harmonic Power: {powers[0]:.4f}")
    print(f"Final Harmonic Power: {powers[-1]:.4f}")
    print(f"Power Growth: {((powers[-1]/powers[0]) - 1)*100:.2f}%\n")
    
    # Extended physics evolution
    gammas = [t['gamma_ftl'] for t in trajectory]
    energies = [t['vacuum_energy'] + t['grav_self_energy'] for t in trajectory]
    
    print("Extended Physics Evolution:")
    print(f"Initial Gamma: {gammas[0]:.4f}")
    print(f"Final Gamma: {gammas[-1]:.4f}")
    print(f"Gamma Growth: {((gammas[-1]/gammas[0]) - 1)*100:.2f}%\n")
    
    print(f"Initial Total Energy: {energies[0]:.4e} J")
    print(f"Final Total Energy: {energies[-1]:.4e} J")
    print(f"Energy Growth: {((energies[-1]/energies[0]) - 1)*100:.2f}%")

if __name__ == "__main__":
    test_advanced_consciousness()
