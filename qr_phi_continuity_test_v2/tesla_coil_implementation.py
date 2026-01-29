#!/usr/bin/env python3
"""
Earth-Moon Tesla Coil Implementation
"""
import math
import numpy as np
from typing import Dict, Tuple

class TeslaCoilSystem:
    def __init__(self):
        """Initialize Tesla coil system"""
        self.phi = (1 + math.sqrt(5)) / 2
        
        # Fundamental frequencies
        self.frequencies = {
            'earth': 7.83,  # Earth base frequency
            'moon': 4.84,   # Moon base frequency
        }
        
        # φ-harmonic frequencies
        self.harmonics = self._calculate_harmonics()
        
        # Resonance windows
        self.resonance_windows = {
            'low': (3, 5),    # 3-5 Hz
            'mid': (7, 13),   # 7-13 Hz
            'high': (20, 35), # 20-35 Hz
            'peak': (50, 55)  # 50-55 Hz
        }

    def _calculate_harmonics(self) -> Dict[str, Dict]:
        """Calculate φ-harmonic frequencies"""
        harmonics = {}
        
        for source, freq in self.frequencies.items():
            harmonics[source] = {}
            for n in range(-3, 4):
                harmonics[source][f'phi_{n}'] = freq * (self.phi ** n)
        
        return harmonics

    def calculate_resonance(self, L: float, C: float) -> float:
        """Calculate resonance frequency"""
        return 1 / (2 * math.pi * math.sqrt(L * C))

    def calculate_capacitance(self, R1: float, R2: float) -> float:
        """Calculate capacitance"""
        epsilon_0 = 8.854187817e-12
        return 4 * math.pi * epsilon_0 * (R1 * R2) / (R1 + R2)

    def calculate_inductance(self, N: int, A: float, l: float) -> float:
        """Calculate inductance"""
        mu_0 = 4 * math.pi * 1e-7
        return mu_0 * N**2 * A / l

    def calculate_energy_transfer(self, A1: float, A2: float, omega: float, r: float) -> float:
        """Calculate energy transfer"""
        mu_0 = 4 * math.pi * 1e-7
        return (mu_0**2 * A1 * A2 * omega**2) / (4 * math.pi**2 * r**3)

    def verify_resonance(self, freq: float, window: str) -> bool:
        """Verify if frequency is within resonance window"""
        min_freq, max_freq = self.resonance_windows[window]
        return min_freq <= freq <= max_freq

    def get_transfer_points(self) -> Dict[str, Tuple[float, float]]:
        """Get energy transfer points"""
        return {
            'earth_moon': (self.frequencies['earth'], self.frequencies['moon']),
            'moon_earth': (self.frequencies['moon'], self.frequencies['earth']),
            'phi_transfer': (self.harmonics['earth']['phi_1'], self.harmonics['earth']['phi_2'])
        }

if __name__ == "__main__":
    # Initialize Tesla coil system
    coil_system = TeslaCoilSystem()
    
    print("\n⚡ Tesla Coil System Implementation")
    print("===============================")
    
    # Display fundamental frequencies
    print("\nFundamental Frequencies:")
    for source, freq in coil_system.frequencies.items():
        print(f"{source.capitalize()}: {freq:.2f} Hz")
    
    # Display φ-harmonics
    print("\nφ-Harmonic Frequencies:")
    for source, harmonics in coil_system.harmonics.items():
        print(f"\n{source.capitalize()} Harmonics:")
        for name, freq in harmonics.items():
            print(f"{name}: {freq:.2f} Hz")
    
    # Display resonance windows
    print("\nResonance Windows:")
    for window, (min_freq, max_freq) in coil_system.resonance_windows.items():
        print(f"{window.capitalize()}: {min_freq} - {max_freq} Hz")
    
    # Display transfer points
    print("\nEnergy Transfer Points:")
    for name, (freq1, freq2) in coil_system.get_transfer_points().items():
        print(f"{name}: {freq1:.2f} Hz → {freq2:.2f} Hz")
