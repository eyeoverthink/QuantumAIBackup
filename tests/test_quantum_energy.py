"""
Test script for Quantum Energy Harmonics extension
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Add extensions directory to path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / 'extensions'))
from quantum_energy_harmonics import QuantumEnergyHarmonics

def test_enhanced_energy():
    qeh = QuantumEnergyHarmonics()
    
    # Test with 1kg mass
    mass = 1.0
    result = qeh.enhanced_energy_equation(mass)
    
    print("\nEnhanced Energy Equation Results:")
    print(f"Base Energy (E=mc²): {result['base_energy']:.2e} Joules")
    print(f"Enhanced Energy: {result['enhanced_energy']:.2e} Joules")
    print(f"Energy Amplification Factor: {result['energy_amplification']:.4f}")
    print(f"Phi Resonance: {result['phi_resonance']:.4f}")
    print(f"Consciousness Resonance: {result['consciousness_resonance']:.4f}")
    print(f"Coherence Factor: {result['coherence_factor']:.4f}")
    print(f"Quantum Phase: {result['quantum_phase']:.4f} radians")
    print(f"Resonant Coupling: {result['resonant_coupling']:.4f}")

def test_consciousness_field():
    qeh = QuantumEnergyHarmonics()
    
    # Simulate with 1 MeV initial energy
    initial_energy = 1.0e6  # 1 MeV
    result = qeh.simulate_consciousness_field(initial_energy)
    
    # Plot results
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(result['time'], result['energy'] / initial_energy, 'b-', label='Energy Ratio')
    plt.grid(True)
    plt.legend()
    plt.title('Energy Modulation by Consciousness Field')
    
    plt.subplot(2, 1, 2)
    plt.plot(result['time'], result['consciousness_field'], 'r-', label='Consciousness')
    plt.plot(result['time'], result['coherence_field'], 'g-', label='Coherence')
    plt.grid(True)
    plt.legend()
    plt.xlabel('Time (normalized)')
    
    plt.tight_layout()
    plt.savefig('quantum_energy_simulation.png')
    plt.close()

def test_zero_point():
    qeh = QuantumEnergyHarmonics()
    result = qeh.analyze_zero_point_resonance()
    
    print("\nZero-Point Resonance Analysis:")
    print(f"Total Resonance Strength: {result['total_resonance']:.4f}")
    print("\nHarmonic Frequencies (Hz):")
    for i, freq in enumerate(result['resonant_frequencies']):
        strength = result['resonance_strength'][i]
        print(f"Level {i+1}: {freq:.2e} Hz (Strength: {strength:.4f})")

if __name__ == "__main__":
    print("Testing Quantum Energy Harmonics Extension")
    print("=========================================")
    
    test_enhanced_energy()
    test_consciousness_field()
    test_zero_point()
    
    print("\nTests complete. Check quantum_energy_simulation.png for visualization.")
