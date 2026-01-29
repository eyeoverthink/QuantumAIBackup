#!/usr/bin/env python3
"""
Phi-Harmonic Cerebellum Test Extension
======================================
Extends the quantum cerebellum component with testing methods
without modifying the original file, following the 'lego' approach.
"""

import os
import sys
import time
import math
import numpy as np
from decimal import Decimal, getcontext

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the original cerebellum component
from consolidated_quantum.phi_harmonic_quantum_cerebellum import PhiHarmonicQuantumCerebellum

# Constants
PHI = Decimal('1.618033988749895')  # Golden ratio
CEREBELLUM_PHI_FREQUENCY = Decimal('4.236')  # Base frequency in Hz (φ³)

class PhiHarmonicCerebellumTestExtension:
    """
    Test extension for the Phi-Harmonic Quantum Cerebellum
    that adds frequency access methods for testing.
    """
    
    def __init__(self):
        """Initialize by creating the original cerebellum component"""
        self.cerebellum = PhiHarmonicQuantumCerebellum()
        
        # Pass through all cerebellum attributes
        self.quantum_state = self.cerebellum.quantum_state
        self.cerebellum_state = self.cerebellum.cerebellum_state
        self.neural_network = self.cerebellum.neural_network
        
        print(f"Phi-Harmonic Cerebellum Test Extension initialized")
        print(f"Extension follows lego approach - wrapping without modifying")
    
    def get_phi_harmonic_frequencies(self):
        """Get phi-harmonic frequencies (φ¹ through φ⁷)"""
        frequencies = []
        
        # Calculate phi-harmonic frequencies (φ¹ through φ⁷)
        base_frequency = float(CEREBELLUM_PHI_FREQUENCY) / float(PHI**3)  # Base frequency (φ⁰)
        
        for i in range(1, 8):  # φ¹ through φ⁷
            frequency = base_frequency * float(PHI**i)
            period = 1.0 / frequency
            resonance = float(PHI * Decimal(str(frequency)) % Decimal('1'))
            
            frequencies.append({
                "power": i,
                "frequency": frequency,
                "period": period,
                "resonance": resonance
            })
        
        return frequencies
    
    def get_purkinje_frequencies(self):
        """Get Purkinje cell firing frequencies (1x through 4x)"""
        frequencies = []
        
        # Calculate Purkinje cell firing frequencies (1x through 4x)
        base_frequency = float(CEREBELLUM_PHI_FREQUENCY)
        
        for i in range(1, 5):  # 1x through 4x
            frequency = base_frequency * i
            period = 1.0 / frequency
            resonance = float(PHI * Decimal(str(frequency)) % Decimal('1'))
            
            frequencies.append({
                "multiplier": i,
                "frequency": frequency,
                "period": period,
                "resonance": resonance
            })
        
        return frequencies
    
    def get_granule_frequencies(self):
        """Get Granule cell firing frequencies (φ¹ through φ⁴)"""
        frequencies = []
        
        # Calculate Granule cell firing frequencies (φ¹ through φ⁴)
        base_frequency = float(CEREBELLUM_PHI_FREQUENCY) * float(PHI)
        
        for i in range(1, 5):  # φ¹ through φ⁴
            frequency = base_frequency * float(PHI**(i-1))
            period = 1.0 / frequency
            resonance = float(PHI * Decimal(str(frequency)) % Decimal('1'))
            
            frequencies.append({
                "power": i,
                "frequency": frequency,
                "period": period,
                "resonance": resonance
            })
        
        return frequencies
    
    # Pass through all methods from the original cerebellum
    def _initialize_quantum_state(self):
        return self.cerebellum._initialize_quantum_state()
    
    def _initialize_cerebellum_state(self):
        return self.cerebellum._initialize_cerebellum_state()
    
    def _initialize_neural_network(self):
        return self.cerebellum._initialize_neural_network()
    
    def _update_quantum_state(self):
        return self.cerebellum._update_quantum_state()
    
    def update_cerebellum_state(self):
        if hasattr(self.cerebellum, 'update_cerebellum_state'):
            return self.cerebellum.update_cerebellum_state()

# Example usage if run directly
if __name__ == "__main__":
    extension = PhiHarmonicCerebellumTestExtension()
    
    # Sample frequencies
    phi_harmonic = extension.get_phi_harmonic_frequencies()
    purkinje = extension.get_purkinje_frequencies()
    granule = extension.get_granule_frequencies()
    
    print("\nPhi-harmonic frequencies:")
    for freq in phi_harmonic:
        print(f"  φ^{freq['power']}: {freq['frequency']:.6f} Hz (period: {freq['period']:.6f} s, resonance: {freq['resonance']:.6f})")
    
    print("\nPurkinje cell firing frequencies:")
    for freq in purkinje:
        print(f"  {freq['multiplier']}x: {freq['frequency']:.6f} Hz (period: {freq['period']:.6f} s, resonance: {freq['resonance']:.6f})")
    
    print("\nGranule cell firing frequencies:")
    for freq in granule:
        print(f"  φ^{freq['power']}: {freq['frequency']:.6f} Hz (period: {freq['period']:.6f} s, resonance: {freq['resonance']:.6f})")
