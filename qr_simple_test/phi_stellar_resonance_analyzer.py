#!/usr/bin/env python3
"""
PHI-STELLAR RESONANCE ANALYZER
==============================
Decodes stellar information through φ-dimensional color resonance patterns.

This system analyzes spectral data from stars not as discrete elements
but as unified resonance color fields, revealing the deeper information
embedded in stellar light signatures.

Author: Vaughn Scott
Date: April 26, 2025
φ^75 Validation Seal: 4721424167835397.0
"""

import os
import sys
import time
import json
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

# === φ-Dimensional Constants ===
PHI = (1 + 5 ** 0.5) / 2  # φ ≈ 1.618033988749895
PHI_INVERSE = 1 / PHI     # 1/φ ≈ 0.618033988749895
PHI_SQUARED = PHI ** 2    # φ² ≈ 2.618033988749895
PHI_CUBED = PHI ** 3      # φ³ ≈ 4.236067977499790
PHI_75 = PHI ** 7.5       # φ^7.5 ≈ 36.93238055064196
PHI_VALIDATION_SEAL = PHI ** 75  # φ^75 validation seal
BIRTH_COHERENCE = 0.9918

# === Stellar Resonance Constants ===
HYDROGEN_RESONANCE = 656.28  # nm (H-alpha line)
HELIUM_RESONANCE = 587.56    # nm (He I line)
OXYGEN_RESONANCE = 630.03    # nm (O I line)
SODIUM_RESONANCE = 589.59    # nm (Na D lines)
CALCIUM_RESONANCE = 422.67   # nm (Ca K line)

# === Star Types and their φ-Resonance Templates ===
STAR_TYPE_RESONANCE = {
    'O': {'temp_range': (30000, 60000), 'phi_template': 0.056619},  # Hot blue stars
    'B': {'temp_range': (10000, 30000), 'phi_template': 0.144718},  # Blue-white stars
    'A': {'temp_range': (7500, 10000), 'phi_template': 0.236068},   # White stars
    'F': {'temp_range': (6000, 7500), 'phi_template': 0.381966},    # Yellow-white stars
    'G': {'temp_range': (5000, 6000), 'phi_template': 0.618034},    # Yellow stars (Sun)
    'K': {'temp_range': (3500, 5000), 'phi_template': 0.763932},    # Orange stars
    'M': {'temp_range': (2000, 3500), 'phi_template': 0.927864},    # Red dwarf stars
}

class PhiStellarResonanceAnalyzer:
    """
    Analyzer for decoding stellar information through φ-dimensional color resonance patterns.
    """
    
    def __init__(self):
        """Initialize the φ-Stellar Resonance Analyzer."""
        self.results_dir = Path("stellar_resonance_results")
        self.results_dir.mkdir(exist_ok=True)
        
        print(f"φ-Stellar Resonance Analyzer initialized")
        print(f"φ^75 Validation Seal: {PHI_VALIDATION_SEAL}")
        print(f"Birth Coherence: {BIRTH_COHERENCE}")
    
    def load_spectrum(self, star_name, temperature=None, spectrum_data=None):
        """
        Load or generate a stellar spectrum.
        
        Args:
            star_name: Name of the star
            temperature: Temperature of the star in Kelvin (optional)
            spectrum_data: Raw spectrum data if available (optional)
            
        Returns:
            dict: Stellar spectrum information
        """
        # If spectrum data provided, use it
        if spectrum_data is not None:
            return {
                'name': star_name,
                'temperature': temperature,
                'spectrum': spectrum_data
            }
        
        # If no spectrum data, generate simulated data
        if temperature is None:
            # Default to Sun-like (G-type) star if no temperature specified
            temperature = 5778  # Sun's temperature in Kelvin
        
        # Determine star type from temperature
        star_type = self._get_star_type(temperature)
        
        # Generate simulated spectrum based on temperature and star type
        wavelengths = np.linspace(380, 780, 200)  # visible spectrum 380-780 nm
        
        # Planck's black body radiation formula (simplified)
        h = 6.63e-34  # Planck constant
        c = 3.0e8     # Speed of light
        k = 1.38e-23  # Boltzmann constant
        
        # Convert wavelength to meters
        wavelengths_m = wavelengths * 1e-9
        
        # Generate spectrum using Planck's law
        spectrum = []
        for wl in wavelengths_m:
            # Black body radiation formula
            intensity = (2.0 * h * c**2) / ((wl**5) * (np.exp((h*c)/(wl*k*temperature)) - 1.0))
            spectrum.append(intensity)
        
        # Normalize spectrum
        spectrum = np.array(spectrum)
        spectrum = spectrum / np.max(spectrum)
        
        # Add absorption lines based on star type
        spectrum = self._add_absorption_lines(wavelengths, spectrum, star_type)
        
        return {
            'name': star_name,
            'temperature': temperature,
            'type': star_type,
            'wavelengths': wavelengths.tolist(),
            'spectrum': spectrum.tolist()
        }
    
    def _get_star_type(self, temperature):
        """Determine star type from temperature."""
        for star_type, data in STAR_TYPE_RESONANCE.items():
            min_temp, max_temp = data['temp_range']
            if min_temp <= temperature <= max_temp:
                return star_type
        
        # Default to G-type (Sun-like) if temperature out of range
        return 'G'
    
    def _add_absorption_lines(self, wavelengths, spectrum, star_type):
        """Add absorption lines to the spectrum based on star type."""
        # Dictionary mapping star types to prominent absorption lines
        absorption_lines = {
            'O': [HYDROGEN_RESONANCE * 0.99, HELIUM_RESONANCE * 1.01],
            'B': [HYDROGEN_RESONANCE, HELIUM_RESONANCE],
            'A': [HYDROGEN_RESONANCE * 1.01, CALCIUM_RESONANCE * 0.99],
            'F': [HYDROGEN_RESONANCE * 1.02, CALCIUM_RESONANCE],
            'G': [SODIUM_RESONANCE, CALCIUM_RESONANCE * 1.01],  # Sun-like
            'K': [SODIUM_RESONANCE * 1.01, CALCIUM_RESONANCE * 1.02],
            'M': [SODIUM_RESONANCE * 1.02, OXYGEN_RESONANCE]
        }
        
        # Add absorption lines as dips in the spectrum
        for line in absorption_lines.get(star_type, []):
            # Find closest wavelength index
            idx = np.argmin(np.abs(wavelengths - line))
            
            # Create absorption dip
            width = 5  # width of absorption line in indices
            for i in range(max(0, idx-width), min(len(spectrum), idx+width+1)):
                # Gaussian-like absorption profile
                distance = abs(i - idx)
                if distance == 0:
                    # Center of line has maximum absorption
                    spectrum[i] *= 0.2  # 80% absorption at center
                else:
                    # Absorption falls off with distance from center
                    spectrum[i] *= 1 - 0.8 * np.exp(-(distance**2) / (2 * (width/2)**2))
        
        return spectrum
    
    def analyze_resonance(self, stellar_data):
        """
        Analyze the φ-dimensional resonance patterns in stellar spectrum.
        
        Args:
            stellar_data: Dict with stellar spectrum information
            
        Returns:
            dict: Resonance analysis results
        """
        print(f"Analyzing φ-dimensional resonance for {stellar_data['name']}...")
        
        wavelengths = np.array(stellar_data['wavelengths'])
        spectrum = np.array(stellar_data['spectrum'])
        
        # === 1. Calculate φ-Resonance Template ===
        star_type = stellar_data.get('type', self._get_star_type(stellar_data['temperature']))
        phi_template = STAR_TYPE_RESONANCE[star_type]['phi_template']
        
        # === 2. Calculate φ-Resonance Values ===
        # Divide spectrum into φ sections and analyze resonance in each
        num_sections = int(PHI_CUBED)  # ~4 sections
        section_size = len(wavelengths) // num_sections
        
        resonance_values = []
        for i in range(num_sections):
            start_idx = i * section_size
            end_idx = min((i + 1) * section_size, len(wavelengths))
            
            section_wavelengths = wavelengths[start_idx:end_idx]
            section_spectrum = spectrum[start_idx:end_idx]
            
            # Calculate resonance as modulation by phi
            section_mean = np.mean(section_spectrum)
            resonance = (section_mean * PHI) % 1
            resonance_values.append(resonance)
        
        # === 3. Calculate Color Resonance ===
        # Map wavelengths to RGB color space
        red_region = (620, 780)   # Red wavelength range (nm)
        green_region = (500, 620) # Green wavelength range (nm)
        blue_region = (380, 500)  # Blue wavelength range (nm)
        
        # Calculate color channel intensities based on spectrum
        red_intensity = self._calculate_color_intensity(wavelengths, spectrum, red_region)
        green_intensity = self._calculate_color_intensity(wavelengths, spectrum, green_region)
        blue_intensity = self._calculate_color_intensity(wavelengths, spectrum, blue_region)
        
        # Normalize color values
        max_intensity = max(red_intensity, green_intensity, blue_intensity)
        if max_intensity > 0:
            red = red_intensity / max_intensity
            green = green_intensity / max_intensity
            blue = blue_intensity / max_intensity
        else:
            red, green, blue = 0, 0, 0
        
        # Calculate color resonance as phi-modulation of RGB values
        color_resonance = ((red * PHI) % 1 + (green * PHI_SQUARED) % 1 + (blue * PHI_CUBED) % 1) / 3
        
        # === 4. Calculate Quantum Metrics ===
        # Phi-resonance ratio
        phi_resonance = (phi_template * BIRTH_COHERENCE) % 1
        
        # Element resonance (how strongly it resonates with known elements)
        element_resonances = self._calculate_element_resonances(wavelengths, spectrum)
        
        # Coherence with Earth's frequency (7.83 Hz Schumann resonance)
        earth_coherence = (phi_resonance * 7.83) % 1
        
        # Consciousness potential (φ-resonance aligned with birth coherence)
        consciousness = (phi_resonance * BIRTH_COHERENCE) % 1
        
        # Information density (derived from resonance pattern complexity)
        # Higher values indicate more complex information patterns
        resonance_std = np.std(resonance_values)
        information_density = resonance_std * PHI_SQUARED
        
        # === 5. Prepare Results ===
        resonance_analysis = {
            'star_name': stellar_data['name'],
            'temperature': stellar_data['temperature'],
            'star_type': star_type,
            'phi_template': phi_template,
            'phi_resonance': phi_resonance,
            'color_resonance': color_resonance,
            'rgb_values': {
                'red': float(red),
                'green': float(green),
                'blue': float(blue)
            },
            'section_resonances': [float(r) for r in resonance_values],
            'element_resonances': element_resonances,
            'quantum_metrics': {
                'earth_coherence': float(earth_coherence),
                'consciousness': float(consciousness),
                'information_density': float(information_density)
            },
            'phi_validation_seal': PHI_VALIDATION_SEAL,
            'timestamp': datetime.now().isoformat()
        }
        
        print(f"φ-Resonance analysis complete for {stellar_data['name']}")
        print(f"Star Type: {star_type} (φ-template: {phi_template:.6f})")
        print(f"φ-Resonance: {phi_resonance:.6f}")
        print(f"Color Resonance: {color_resonance:.6f}")
        print(f"Consciousness: {consciousness:.6f}")
        print(f"Information Density: {information_density:.6f}")
        
        return resonance_analysis
    
    def _calculate_color_intensity(self, wavelengths, spectrum, color_region):
        """Calculate intensity of a color channel based on wavelength region."""
        min_wl, max_wl = color_region
        in_range = (wavelengths >= min_wl) & (wavelengths <= max_wl)
        
        if not np.any(in_range):
            return 0
            
        return np.mean(np.array(spectrum)[in_range])
    
    def _calculate_element_resonances(self, wavelengths, spectrum):
        """Calculate resonance with known stellar elements."""
        elements = {
            'hydrogen': HYDROGEN_RESONANCE,
            'helium': HELIUM_RESONANCE,
            'oxygen': OXYGEN_RESONANCE,
            'sodium': SODIUM_RESONANCE,
            'calcium': CALCIUM_RESONANCE
        }
        
        resonances = {}
        for element, resonance_line in elements.items():
            # Find closest wavelength index
            idx = np.argmin(np.abs(wavelengths - resonance_line))
            
            # Calculate resonance based on absorption at that wavelength
            # Lower spectrum value means stronger absorption
            absorption_strength = 1 - spectrum[idx]
            
            # Apply phi-modulation
            phi_resonance = (absorption_strength * PHI) % 1
            resonances[element] = float(phi_resonance)
        
        return resonances
    
    def visualize_resonance(self, stellar_data, resonance_analysis):
        """
        Visualize the stellar spectrum and φ-resonance patterns.
        
        Args:
            stellar_data: Dict with stellar spectrum information
            resonance_analysis: Dict with resonance analysis results
            
        Returns:
            str: Path to the saved visualization file
        """
        plt.figure(figsize=(12, 8))
        
        # === 1. Spectrum Plot ===
        plt.subplot(2, 1, 1)
        wavelengths = stellar_data['wavelengths']
        spectrum = stellar_data['spectrum']
        
        plt.plot(wavelengths, spectrum)
        plt.title(f"φ-Dimensional Stellar Resonance: {stellar_data['name']} (Type {resonance_analysis['star_type']})")
        plt.xlabel("Wavelength (nm)")
        plt.ylabel("Relative Intensity")
        
        # Add vertical lines for key element resonances
        elements = {
            'H': HYDROGEN_RESONANCE,
            'He': HELIUM_RESONANCE,
            'O': OXYGEN_RESONANCE,
            'Na': SODIUM_RESONANCE,
            'Ca': CALCIUM_RESONANCE
        }
        
        for element, wavelength in elements.items():
            if min(wavelengths) <= wavelength <= max(wavelengths):
                plt.axvline(x=wavelength, color='r', linestyle='--', alpha=0.5)
                plt.text(wavelength, 0.1, element, rotation=90, alpha=0.7)
        
        # === 2. Resonance Pattern Plot ===
        plt.subplot(2, 1, 2)
        
        # Plot section resonances
        section_resonances = resonance_analysis['section_resonances']
        x = np.arange(len(section_resonances))
        plt.bar(x, section_resonances, color='skyblue', alpha=0.7)
        
        # Add phi-resonance line
        plt.axhline(y=resonance_analysis['phi_resonance'], color='r', linestyle='-', label=f"φ-Resonance: {resonance_analysis['phi_resonance']:.6f}")
        
        # Add consciousness line
        plt.axhline(y=resonance_analysis['quantum_metrics']['consciousness'], color='g', linestyle=':', label=f"Consciousness: {resonance_analysis['quantum_metrics']['consciousness']:.6f}")
        
        plt.xlabel("Spectrum Sections")
        plt.ylabel("φ-Resonance Value")
        plt.legend()
        
        # === 3. Add Information Box ===
        info_text = (
            f"Star: {stellar_data['name']}\n"
            f"Type: {resonance_analysis['star_type']} ({stellar_data['temperature']} K)\n"
            f"φ-Template: {resonance_analysis['phi_template']:.6f}\n"
            f"Color-Resonance: {resonance_analysis['color_resonance']:.6f}\n"
            f"Information Density: {resonance_analysis['quantum_metrics']['information_density']:.6f}\n"
            f"Earth Coherence: {resonance_analysis['quantum_metrics']['earth_coherence']:.6f}\n"
            f"RGB: ({resonance_analysis['rgb_values']['red']:.2f}, "
            f"{resonance_analysis['rgb_values']['green']:.2f}, "
            f"{resonance_analysis['rgb_values']['blue']:.2f})"
        )
        
        plt.figtext(0.15, 0.01, info_text, bbox=dict(facecolor='white', alpha=0.5))
        
        # Add validation seal
        plt.figtext(0.85, 0.01, f"φ^75 Seal: {PHI_VALIDATION_SEAL:.1e}", fontsize=8)
        
        plt.tight_layout()
        
        # Save visualization
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"stellar_resonance_{stellar_data['name']}_{timestamp}.png"
        filepath = self.results_dir / filename
        plt.savefig(filepath)
        plt.close()
        
        print(f"Visualization saved to {filepath}")
        return str(filepath)
    
    def save_analysis(self, stellar_data, resonance_analysis):
        """
        Save resonance analysis to file.
        
        Args:
            stellar_data: Dict with stellar spectrum information
            resonance_analysis: Dict with resonance analysis results
            
        Returns:
            str: Path to the saved analysis file
        """
        # Combine stellar data and resonance analysis
        combined_data = {
            'stellar_data': stellar_data,
            'resonance_analysis': resonance_analysis
        }
        
        # Generate filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"stellar_resonance_analysis_{stellar_data['name']}_{timestamp}.json"
        filepath = self.results_dir / filename
        
        # Save to file
        with open(filepath, 'w') as f:
            json.dump(combined_data, f, indent=2)
        
        print(f"Analysis saved to {filepath}")
        return str(filepath)
    
    def analyze_star(self, star_name, temperature=None, spectrum_data=None):
        """
        Complete workflow to analyze a star.
        
        Args:
            star_name: Name of the star
            temperature: Temperature of the star in Kelvin (optional)
            spectrum_data: Raw spectrum data if available (optional)
            
        Returns:
            dict: Results including file paths to saved analysis and visualization
        """
        # Step 1: Load/generate spectrum
        stellar_data = self.load_spectrum(star_name, temperature, spectrum_data)
        
        # Step 2: Analyze resonance
        resonance_analysis = self.analyze_resonance(stellar_data)
        
        # Step 3: Visualize results
        visualization_path = self.visualize_resonance(stellar_data, resonance_analysis)
        
        # Step 4: Save analysis
        analysis_path = self.save_analysis(stellar_data, resonance_analysis)
        
        return {
            'stellar_data': stellar_data,
            'resonance_analysis': resonance_analysis,
            'visualization_path': visualization_path,
            'analysis_path': analysis_path
        }

def run_system():
    """Run the φ-Stellar Resonance Analyzer in interactive mode."""
    print("\n" + "="*80)
    print("φ-STELLAR RESONANCE ANALYZER")
    print("Decoding stellar information through φ-dimensional color resonance patterns")
    print(f"φ^75 Validation Seal: {PHI_VALIDATION_SEAL}")
    print("="*80 + "\n")
    
    # Initialize analyzer
    analyzer = PhiStellarResonanceAnalyzer()
    
    # Sample stars for analysis
    default_stars = [
        {"name": "Sun", "type": "G", "temperature": 5778},
        {"name": "Sirius", "type": "A", "temperature": 9940},
        {"name": "Betelgeuse", "type": "M", "temperature": 3500},
        {"name": "Rigel", "type": "B", "temperature": 12100},
        {"name": "Vega", "type": "A", "temperature": 9602}
    ]
    
    print("\nAvailable Stars for Analysis:")
    for i, star in enumerate(default_stars, 1):
        print(f"{i}. {star['name']} (Type {star['type']}, {star['temperature']} K)")
    
    # Command interface
    print("\nφ-Stellar Resonance Analyzer Interface")
    print("-" * 50)
    print("Available commands:")
    print("  analyze <star_number> - Analyze a star from the list")
    print("  custom <name> <temperature> - Analyze a custom star")
    print("  batch - Analyze all sample stars")
    print("  help - Show this help message")
    print("  exit - Exit the program")
    print("-" * 50 + "\n")
    
    while True:
        try:
            command = input("Command: ").strip().lower()
            
            if command.startswith("analyze"):
                parts = command.split()
                if len(parts) < 2:
                    print("Please specify star number: analyze <star_number>")
                    continue
                
                try:
                    star_num = int(parts[1])
                    if 1 <= star_num <= len(default_stars):
                        star = default_stars[star_num - 1]
                        analyzer.analyze_star(star["name"], star["temperature"])
                    else:
                        print(f"Invalid star number. Please choose 1-{len(default_stars)}")
                except ValueError:
                    print("Invalid star number. Please enter a number.")
            
            elif command.startswith("custom"):
                parts = command.split()
                if len(parts) < 3:
                    print("Please specify star name and temperature: custom <name> <temperature>")
                    continue
                
                name = parts[1]
                try:
                    temperature = float(parts[2])
                    analyzer.analyze_star(name, temperature)
                except ValueError:
                    print("Invalid temperature. Please enter a number.")
            
            elif command == "batch":
                print("\nBatch analyzing all sample stars...\n")
                for star in default_stars:
                    analyzer.analyze_star(star["name"], star["temperature"])
                    print()  # Add blank line between stars
                print("Batch analysis complete.")
            
            elif command == "help":
                print("\nφ-Stellar Resonance Analyzer Interface")
                print("-" * 50)
                print("Available commands:")
                print("  analyze <star_number> - Analyze a star from the list")
                print("  custom <name> <temperature> - Analyze a custom star")
                print("  batch - Analyze all sample stars")
                print("  help - Show this help message")
                print("  exit - Exit the program")
                print("-" * 50)
            
            elif command in ["exit", "quit", "q"]:
                print("Exiting φ-Stellar Resonance Analyzer...")
                break
            
            else:
                print(f"Unknown command: {command}")
        
        except KeyboardInterrupt:
            print("\nExiting φ-Stellar Resonance Analyzer...")
            break
        
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    run_system()
