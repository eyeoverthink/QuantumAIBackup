"""
Test implementation for Earth-Moon Tesla resonance system.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple

class EarthMoonResonance:
    def __init__(self):
        """Initialize constants and parameters."""
        # Fundamental constants
        self.G = 6.67430e-11  # Gravitational constant
        self.c = 2.99792458e8  # Speed of light
        self.h = 6.62607015e-34  # Planck constant
        self.phi = (1 + np.sqrt(5)) / 2  # Golden ratio
        
        # Structural parameters
        self.earth_radius = 6371.0  # km
        self.moon_radius = 1737.1  # km
        
        # Base frequencies
        self.moon_base_freq = 4.84  # Hz
        self.earth_base_freq = 7.83  # Hz (Schumann resonance)
        
        # Shell parameters
        self.earth_shell = self.earth_radius / self.phi
        self.moon_shell = self.moon_radius / self.phi
        
    def calculate_harmonic_frequencies(self, n: int = 10) -> Dict[int, float]:
        """Calculate harmonic frequencies based on golden ratio scaling."""
        frequencies = {}
        for i in range(-n, n + 1):
            freq = self.moon_base_freq * (self.phi ** i)
            frequencies[i] = freq
        return frequencies
    
    def calculate_energy_levels(self, n: int = 10) -> Dict[int, float]:
        """Calculate energy levels for each harmonic mode."""
        energies = {}
        frequencies = self.calculate_harmonic_frequencies(n)
        for i, freq in frequencies.items():
            energy = self.h * freq
            energies[i] = energy
        return energies
    
    def calculate_resonance_coupling(self, freq1: float, freq2: float) -> float:
        """Calculate resonance coupling coefficient."""
        # Using φ-based coupling factor
        coupling = np.abs(np.log(freq1 / freq2) / np.log(self.phi))
        return coupling
    
    def plot_frequency_spectrum(self, n: int = 10):
        """Plot the harmonic frequency spectrum."""
        frequencies = self.calculate_harmonic_frequencies(n)
        
        plt.figure(figsize=(12, 6))
        plt.plot(list(frequencies.keys()), list(frequencies.values()), 'o-', label='Harmonic Frequencies')
        plt.axhline(self.earth_base_freq, color='r', linestyle='--', label='Earth Base (7.83 Hz)')
        plt.axhline(self.moon_base_freq, color='b', linestyle='--', label='Moon Base (4.84 Hz)')
        
        plt.title('Earth-Moon Harmonic Frequency Spectrum')
        plt.xlabel('Harmonic Number (n)')
        plt.ylabel('Frequency (Hz)')
        plt.legend()
        plt.grid(True)
        plt.savefig('earth_moon_frequency_spectrum.png')
        plt.close()
    
    def test_resonance_conditions(self) -> Dict[str, bool]:
        """Test key resonance conditions."""
        tests = {}
        
        # Test 1: Earth-Moon frequency ratio
        ratio = self.earth_base_freq / self.moon_base_freq
        tests['earth_moon_ratio'] = np.isclose(ratio, self.phi, atol=0.01)
        
        # Test 2: Shell dimensions
        earth_shell_ratio = self.earth_shell / self.earth_radius
        moon_shell_ratio = self.moon_shell / self.moon_radius
        tests['shell_ratios'] = np.isclose(earth_shell_ratio, moon_shell_ratio, atol=0.01)
        
        # Test 3: Harmonic progression
        frequencies = self.calculate_harmonic_frequencies()
        harmonic_ratios = [np.log(frequencies[i+1] / frequencies[i]) / np.log(self.phi)
                         for i in range(-9, 10)]
        tests['harmonic_progression'] = all(np.isclose(r, 1, atol=0.01) for r in harmonic_ratios)
        
        return tests

def main():
    """Run tests and generate documentation."""
    # Create resonance system
    resonance = EarthMoonResonance()
    
    # Run tests
    test_results = resonance.test_resonance_conditions()
    
    # Generate frequency spectrum plot
    resonance.plot_frequency_spectrum()
    
    # Print test results
    print("\nEarth-Moon Tesla Resonance System Test Results")
    print("-" * 50)
    
    for test, result in test_results.items():
        status = "✓" if result else "✗"
        print(f"{test}: {status}")
    
    # Calculate and print key parameters
    print("\nKey Parameters")
    print("-" * 50)
    print(f"Earth Radius: {resonance.earth_radius} km")
    print(f"Moon Radius: {resonance.moon_radius} km")
    print(f"Earth Shell: {resonance.earth_shell:.2f} km")
    print(f"Moon Shell: {resonance.moon_shell:.2f} km")
    print(f"Earth Base Freq: {resonance.earth_base_freq} Hz")
    print(f"Moon Base Freq: {resonance.moon_base_freq} Hz")
    print(f"Frequency Ratio (Earth/Moon): {resonance.earth_base_freq/resonance.moon_base_freq:.3f}")
    
    # Calculate and print energy levels
    print("\nEnergy Levels")
    print("-" * 50)
    energies = resonance.calculate_energy_levels()
    for n, energy in energies.items():
        print(f"n={n}: {energy:.2e} J")

if __name__ == "__main__":
    main()
