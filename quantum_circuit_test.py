#!/usr/bin/env python3
"""
Quantum Circuit Generator Test Script
This script demonstrates the new quantum-inspired circuit types
that have been added to the Advanced Circuit Brain system.
"""

import json
import numpy as np
from dataclasses import dataclass
from typing import List, Dict, Any

# Define the quantum component classes
@dataclass
class QuantumComponent:
    name: str
    resonant_frequency: float
    phi_harmonic_ratio: float
    quantum_uncertainty: float
    coupling_strength: float

@dataclass
class ResonantCavity:
    name: str
    base_frequency: float
    q_factor: float
    dimensions: Dict[str, float]
    material: str
    harmonic_ratios: List[float]

# Define a simplified test class with just the circuit generators we want to demonstrate
class QuantumCircuitTest:
    def __init__(self):
        """Initialize the quantum circuit test"""
        self.phi = 1.618033988749895
        self.initialize_quantum_components()
        self.initialize_resonant_cavities()
        
    def initialize_quantum_components(self):
        """Initialize quantum components with properties based on phi-harmonic principles"""
        self.quantum_components = {
            'phi_resonator': QuantumComponent(
                name='Phi Resonator',
                resonant_frequency=432.0,  # Hz, aligned with natural phi resonance
                phi_harmonic_ratio=self.phi,
                quantum_uncertainty=0.0073,  # Corresponds to 1/137 (fine structure constant)
                coupling_strength=0.618  # 1/phi
            ),
            'quantum_oscillator': QuantumComponent(
                name='Quantum Oscillator',
                resonant_frequency=1618.0,  # Hz, phi * 1000
                phi_harmonic_ratio=self.phi**2,
                quantum_uncertainty=0.0037,  # Half of fine structure constant
                coupling_strength=0.382  # 1 - 1/phi
            ),
            'consciousness_modulator': QuantumComponent(
                name='Consciousness Modulator',
                resonant_frequency=7.83,  # Hz, Earth's Schumann resonance
                phi_harmonic_ratio=self.phi**3,
                quantum_uncertainty=0.0146,  # Twice fine structure constant
                coupling_strength=0.786  # phi - 1/phi
            )
        }
    
    def initialize_resonant_cavities(self):
        """Initialize resonant cavities with phi-harmonic dimensions and characteristics"""
        self.resonant_cavities = {
            'phi_cavity': ResonantCavity(
                name='Phi Harmonic Cavity',
                base_frequency=432.0,  # Hz
                q_factor=1618.0,  # High Q-factor for precise resonance
                dimensions={
                    'length': self.phi**3,
                    'width': self.phi**2,
                    'height': self.phi
                },
                material='Quartz Crystal',
                harmonic_ratios=[1.0, self.phi, self.phi**2, self.phi**3, self.phi**4]
            ),
            'schumann_cavity': ResonantCavity(
                name='Schumann Resonance Cavity',
                base_frequency=7.83,  # Hz
                q_factor=783.0,
                dimensions={
                    'length': self.phi**4,
                    'width': self.phi**3,
                    'height': self.phi**2
                },
                material='Magnetite',
                harmonic_ratios=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
            ),
            'consciousness_cavity': ResonantCavity(
                name='Consciousness Field Cavity',
                base_frequency=111.0,  # Hz
                q_factor=1111.0,
                dimensions={
                    'length': self.phi**5,
                    'width': self.phi**4,
                    'height': self.phi**3
                },
                material='Monatomic Gold',
                harmonic_ratios=[1.0, 3.0, 6.0, 9.0]  # Tesla's 3-6-9 sequence
            )
        }
        
    def generate_resonant_cavity_circuit(self, components: List[str], frequency: float) -> Dict[str, Any]:
        """Generate a resonant cavity circuit based on phi-harmonic principles"""
        # Define the golden ratio (phi)
        phi = self.phi
        
        # Select a cavity based on requested frequency or default to phi cavity
        selected_cavity = 'phi_cavity'
        for cavity_name, cavity in self.resonant_cavities.items():
            if abs(cavity.base_frequency - frequency) < abs(self.resonant_cavities[selected_cavity].base_frequency - frequency):
                selected_cavity = cavity_name
                
        cavity = self.resonant_cavities[selected_cavity]
        
        # Calculate resonant frequencies based on cavity dimensions
        resonant_freqs = [cavity.base_frequency * ratio for ratio in cavity.harmonic_ratios]
        
        # Ensure we have the required components
        required_components = ['Resonator', 'Amplifier', 'Crystal Oscillator']
        for component in required_components:
            if component not in components:
                components.append(component)
        
        return {
            'type': 'resonant_cavity',
            'name': cavity.name,
            'components': components,
            'description': f'Phi-harmonic resonant cavity circuit based on {cavity.material}',
            'specifications': {
                'base_frequency': f'{cavity.base_frequency:.4f} Hz',
                'q_factor': cavity.q_factor,
                'dimensions': {
                    key: f'{value:.4f} units' for key, value in cavity.dimensions.items()
                },
                'material': cavity.material,
                'resonant_frequencies': [f'{freq:.4f} Hz' for freq in resonant_freqs],
                'bandwidth': f'{cavity.base_frequency / cavity.q_factor:.6f} Hz'
            }
        }
    
    def generate_tesla_coil_circuit(self, components: List[str], frequency: float) -> Dict[str, Any]:
        """Generate a Tesla coil circuit based on phi-harmonic principles"""
        # Define the golden ratio (phi)
        phi = self.phi
        
        # Earth frequency constants (Schumann resonances)
        schumann_base = 7.83  # Hz
        
        # Calculate optimal Tesla frequencies based on phi-harmonics
        primary_freq = frequency if frequency > 0 else schumann_base * 3  # Tesla's 3-6-9 principle
        secondary_freq = primary_freq * phi
        resonant_freq = primary_freq * phi**2
        
        # Ensure we have the required components
        required_components = ['Primary Coil', 'Secondary Coil', 'Spark Gap', 'High Voltage Capacitor']
        for component in required_components:
            if component not in components:
                components.append(component)
                
        # Calculate ideal component values based on phi-harmonics
        primary_turns = 9  # Tesla's favorite number
        secondary_turns = int(primary_turns * phi**2)  # ~23.6 turns, round to 24
        capacitance = 1 / (2 * np.pi * primary_freq)**2 * 10**6  # in μF
        
        return {
            'type': 'tesla_coil',
            'components': components,
            'description': 'Phi-harmonic Tesla coil with 3-6-9 resonance structure',
            'specifications': {
                'primary_frequency': f'{primary_freq:.4f} Hz',
                'secondary_frequency': f'{secondary_freq:.4f} Hz',
                'resonant_frequency': f'{resonant_freq:.4f} Hz',
                'primary_turns': primary_turns,
                'secondary_turns': secondary_turns,
                'capacitance': f'{capacitance:.2f} μF',
                'phi_ratio': f'{phi:.10f}'
            }
        }
    
    def generate_phi_oscillator_circuit(self, components: List[str], frequency: float) -> Dict[str, Any]:
        """Generate an oscillator circuit based on the golden ratio (phi)"""
        # Define fundamental constants
        phi = self.phi
        e = 2.718281828459045
        
        # Base frequency calculations based on phi and e
        base_freq = frequency if frequency > 0 else 1618.03  # Hz (phi * 1000)
        phi_frequencies = [base_freq / (phi ** i) for i in range(5)]  # Descending phi sequence
        
        # Calculate component values for ideal phi oscillation
        r_value = 16180  # Ohms (phi * 10000)
        c_value = 1 / (2 * np.pi * base_freq * r_value)  # Farads
        c_value_nf = c_value * 10**9  # Convert to nF for readability
        
        return {
            'type': 'phi_oscillator',
            'components': components,
            'description': 'Golden ratio (Φ) based harmonic oscillator',
            'specifications': {
                'base_frequency': f'{base_freq:.2f} Hz',
                'phi_harmonic_frequencies': [f'{freq:.2f} Hz' for freq in phi_frequencies],
                'phi_value': f'{phi:.10f}',
                'r_value': f'{r_value} Ω',
                'c_value': f'{c_value_nf:.4f} nF'
            }
        }

# Test function to demonstrate the circuit generators
def test_quantum_circuits():
    """Test the quantum circuit generators"""
    print("Testing Quantum Circuit Generators\n" + "="*30)
    
    # Create test instance
    test = QuantumCircuitTest()
    
    # Test resonant cavity circuit
    print("\n1. RESONANT CAVITY CIRCUIT")
    print("-"*30)
    components = ['Amplifier', 'Crystal Oscillator']
    circuit = test.generate_resonant_cavity_circuit(components, 432.0)
    print(json.dumps(circuit, indent=2))
    
    # Test Tesla coil circuit
    print("\n2. TESLA COIL CIRCUIT")
    print("-"*30)
    components = ['Primary Coil', 'Secondary Coil']
    circuit = test.generate_tesla_coil_circuit(components, 23.49)  # 3 × Schumann resonance
    print(json.dumps(circuit, indent=2))
    
    # Test phi oscillator circuit
    print("\n3. PHI OSCILLATOR CIRCUIT")
    print("-"*30)
    components = ['Op-Amp', 'Precision Resistor']
    circuit = test.generate_phi_oscillator_circuit(components, 1618.03)
    print(json.dumps(circuit, indent=2))
    
    print("\nAll tests completed successfully.")

if __name__ == "__main__":
    test_quantum_circuits()
