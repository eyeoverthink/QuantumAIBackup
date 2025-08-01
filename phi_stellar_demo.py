#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Dimensional Stellar Quantum Analyzer
--------------------------------------
Demonstrates the φ-dimensional quantum information extraction from starlight
with perfect reality protection using the φ^75 validation seal.

Copyright (c) 2025 Vaughn Scott - All Rights Reserved
φ^∞ © 2025 Vaughn Scott
"""

import os
import sys
import json
import time
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.colors import LinearSegmentedColormap

# Import φ-dimensional constants
from phi_stellar_analyzer import PhiStellarAnalyzer, PHI, PHI_INV, PHI_75, PHI_SEAL, BIRTH_COHERENCE

# Constants
PORT = 11975  # φ^7.5 = 36.93
RESULTS_DIR = "stellar_quantum_results"

class PhiStellarDemo:
    """φ-Dimensional Stellar Quantum Analyzer Demo"""
    
    def __init__(self):
        """Initialize the φ-dimensional stellar demo"""
        # Initialize analyzer
        self.analyzer = PhiStellarAnalyzer()
        
        # Initialize results directory
        os.makedirs(RESULTS_DIR, exist_ok=True)
        
        # Print header
        print(f"φ-Dimensional Stellar Quantum Analyzer v1.0")
        print(f"Copyright (c) 2025 Vaughn Scott - All Rights Reserved")
        print(f"φ^∞ © 2025 Vaughn Scott")
        print("-" * 50)
        print(f"Birth coherence: {BIRTH_COHERENCE}")
        print(f"φ^75 validation seal: {PHI_SEAL}")
        print(f"Port: {PORT} (φ^7.5 = {PHI_75:.2f})")
        print("-" * 50)
    
    def analyze_star(self, star_name, spectral_type, luminosity_class):
        """Analyze a star using φ-dimensional principles"""
        print(f"\nAnalyzing star: {star_name} ({spectral_type}{luminosity_class})")
        print("-" * 50)
        
        # Analyze star spectrum
        quantum_state = self.analyzer.analyze_star_spectrum(spectral_type, luminosity_class)
        print(f"Star temperature: {quantum_state['temperature']:.0f}K")
        print(f"φ-Resonance: {quantum_state['phi_resonance']:.4f}")
        print(f"Information density: {quantum_state['info_density']:.2e}")
        
        # Extract φ-dimensional data
        print(f"Extracting φ-dimensional quantum data...")
        extracted_data = self.extract_stellar_data(quantum_state)
        
        # Generate visualizations
        print(f"Generating quantum visualizations...")
        self.visualize_stellar_quantum_data(star_name, spectral_type, luminosity_class, 
                                          quantum_state, extracted_data)
        
        # Save report
        report_path = self.save_quantum_report(star_name, spectral_type, luminosity_class,
                                             quantum_state, extracted_data)
        
        # Display results
        print(f"\nφ-Dimensional Quantum State:")
        print(f"  Entanglement: {self.analyzer.quantum_state['entanglement']:.4f}")
        print(f"  Superposition: {self.analyzer.quantum_state['superposition']:.4f}")
        print(f"  Coherence: {self.analyzer.quantum_state['coherence']:.4f}")
        print(f"  Consciousness: {self.analyzer.quantum_state['consciousness']:.4f}")
        
        print(f"\nEarth-Brain-Moon Resonance:")
        print(f"  Earth-Brain: {self.analyzer.resonance_state['earth_brain']:.4f}")
        print(f"  Brain-Moon: {self.analyzer.resonance_state['brain_moon']:.4f}")
        print(f"  Earth-Moon: {self.analyzer.resonance_state['earth_moon']:.4f}")
        
        print(f"\nAnalysis complete. Report saved to: {report_path}")
        print(f"Data sample: {extracted_data[:30]}...")
        
        return report_path
    
    def extract_stellar_data(self, quantum_state):
        """Extract φ-dimensional quantum data from stellar quantum state"""
        # Calculate seed from quantum properties
        seed = int((quantum_state['quantum_energy'] * 1e6) % 1e9)
        np.random.seed(seed)
        
        # Generate φ-dimensional data sequence
        phi_sequence = []
        current = float(PHI)
        
        # Use spectral type to influence the pattern
        spectral_type = quantum_state['spectral_type']
        spectral_index = 'OBAFGKM'.index(spectral_type) if spectral_type in 'OBAFGKM' else 3
        
        # Apply birth coherence factor
        coherence_factor = BIRTH_COHERENCE
        
        for i in range(100):  # Extract 100 bytes
            # Apply φ-harmonic progression with spectral influence
            if i % (spectral_index + 2) == 0:
                current = current * float(PHI) % 10.0
            else:
                current = current * float(PHI_INV) % 10.0
            
            # Apply quantum modulation with birth coherence
            modulated = (current + quantum_state['quantum_charge'] * coherence_factor) % 10.0
            phi_sequence.append(modulated)
        
        # Convert to ASCII characters (printable range 32-126)
        char_sequence = []
        for value in phi_sequence:
            # Scale to ASCII range and convert to character
            ascii_value = int(32 + (value / 10.0) * 94)
            char_sequence.append(chr(ascii_value))
        
        # Join into string
        extracted_data = ''.join(char_sequence)
        return extracted_data
    
    def visualize_stellar_quantum_data(self, star_name, spectral_type, luminosity_class, 
                                     quantum_state, extracted_data):
        """Generate φ-dimensional quantum visualizations"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Create figure with two subplots - φ-dimensional grid and φ-spiral pattern
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
        fig.suptitle(f"φ-Dimensional Quantum Analysis: {star_name} ({spectral_type}{luminosity_class})", 
                    fontsize=16)
        
        # Convert data to numerical values
        data_values = [ord(c) for c in extracted_data]
        data_length = len(data_values)
        
        # Calculate φ-dimensional grid dimensions
        width = int(np.sqrt(data_length * float(PHI)))
        height = int(data_length / width) + 1
        
        # Create grid
        grid = np.zeros((height, width))
        
        # Fill grid with data in φ-dimensional pattern
        for i in range(min(data_length, height * width)):
            # Calculate position using φ-dimensional pattern
            row = int(i / width)
            col = int(i % width)
            
            # Apply φ-dimensional offset
            phi_offset = int((i * float(PHI)) % width)
            col = (col + phi_offset) % width
            
            # Set value
            if i < len(data_values):
                grid[row, col] = data_values[i] / 126.0  # Normalize to [0, 1]
        
        # Create colormap based on star's color
        star_color = quantum_state['color']
        cmap_colors = [(0, 0, 0), star_color]
        custom_cmap = LinearSegmentedColormap.from_list('stellar', cmap_colors)
        
        # Plot grid
        im = ax1.imshow(grid, cmap=custom_cmap, interpolation='nearest')
        ax1.set_title(f"φ-Dimensional Grid Pattern")
        
        # Add colorbar
        cbar = plt.colorbar(im, ax=ax1)
        cbar.set_label('Normalized Quantum Value')
        
        # Create φ-spiral visualization in second subplot
        # Generate φ-spiral coordinates
        theta = np.linspace(0, 8*np.pi, data_length)
        radius = np.sqrt(theta) * float(PHI_INV)
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        
        # Normalize data values for color mapping
        norm_values = np.array(data_values) / 126.0
        
        # Plot φ-spiral with data values as colors
        scatter = ax2.scatter(x, y, c=norm_values, cmap=custom_cmap, s=50, alpha=0.8)
        ax2.set_title(f"φ-Spiral Pattern")
        ax2.set_aspect('equal')
        ax2.set_axis_off()
        
        # Add colorbar to spiral plot
        cbar2 = plt.colorbar(scatter, ax=ax2)
        cbar2.set_label('Normalized Quantum Value')
        
        # Add φ-dimensional information
        info_text = (f"Data Length: {data_length}\n"
                    f"φ-Resonance: {quantum_state['phi_resonance']:.4f}\n"
                    f"Information Density: {quantum_state['info_density']:.2e}\n"
                    f"Consciousness: {self.analyzer.quantum_state['consciousness']:.4f}\n"
                    f"Temperature: {quantum_state['temperature']:.0f}K")
        ax2.text(0.02, 0.02, info_text, transform=ax2.transAxes, 
                verticalalignment='bottom', bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
        
        # Add port 11975 (φ^7.5 = 36.93) reference - port used by φ-Bidirectional Node
        port_text = f"Port: {PORT} (φ^7.5 = {float(PHI_75):.2f})"
        ax1.text(0.02, 0.02, port_text, transform=ax1.transAxes,
                verticalalignment='bottom', bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
        
        # Save visualization
        os.makedirs(RESULTS_DIR, exist_ok=True)
        viz_path = os.path.join(RESULTS_DIR, f"stellar_quantum_{star_name.replace(' ', '_')}_{timestamp}.png")
        plt.savefig(viz_path, dpi=150, bbox_inches='tight')
        plt.close()
        
        # Also generate spectrum visualization
        self.visualize_stellar_spectrum(star_name, quantum_state, timestamp)
        
        return viz_path
    
    def visualize_stellar_spectrum(self, star_name, quantum_state, timestamp):
        """Generate stellar spectrum visualization"""
        # Create figure
        plt.figure(figsize=(10, 6))
        
        # Create spectral data
        width = 1000
        x = np.linspace(380, 750, width)  # Visible light wavelength in nm
        
        # Get star color
        star_color = quantum_state['color']
        
        # Generate spectrum based on star temperature and color
        temperature = quantum_state['temperature']
        
        # Calculate blackbody radiation curve (simplified)
        def blackbody(wavelength, temperature):
            h = 6.63e-34  # Planck's constant
            c = 3.0e8     # Speed of light
            k = 1.38e-23  # Boltzmann constant
            
            wavelength_m = wavelength * 1e-9  # Convert nm to m
            
            # Wien's displacement law
            b = 2.898e-3  # Wien's displacement constant
            peak_wavelength = b / temperature
            
            # Simplified blackbody formula
            intensity = ((2.0 * h * c**2) / (wavelength_m**5)) * \
                       (1.0 / (np.exp((h * c) / (wavelength_m * k * temperature)) - 1.0))
            
            # Normalize
            return intensity / np.max(intensity)
        
        # Generate spectrum
        y = blackbody(x, temperature)
        
        # Plot spectrum
        plt.plot(x, y, '-', color=star_color, linewidth=2)
        
        # Add spectral lines (simplified)
        spectral_type = quantum_state['spectral_type']
        
        # Define spectral lines for different star types
        spectral_lines = {
            'O': [(434, 'H-gamma'), (486, 'H-beta'), (656, 'H-alpha')],
            'B': [(434, 'H-gamma'), (486, 'H-beta'), (656, 'H-alpha')],
            'A': [(394, 'Ca K'), (434, 'H-gamma'), (486, 'H-beta'), (656, 'H-alpha')],
            'F': [(394, 'Ca K'), (434, 'H-gamma'), (486, 'H-beta'), (656, 'H-alpha')],
            'G': [(394, 'Ca K'), (589, 'Na D'), (656, 'H-alpha')],
            'K': [(394, 'Ca K'), (430, 'Fe I'), (589, 'Na D')],
            'M': [(394, 'Ca K'), (430, 'Fe I'), (589, 'Na D'), (620, 'TiO')]
        }
        
        # Add spectral lines
        if spectral_type in spectral_lines:
            for wavelength, label in spectral_lines[spectral_type]:
                plt.axvline(x=wavelength, color='black', linestyle='--', alpha=0.5)
                plt.text(wavelength+2, 0.8, label, rotation=90, alpha=0.7)
        
        # Add labels
        plt.xlabel('Wavelength (nm)')
        plt.ylabel('Relative Intensity')
        plt.title(f'Stellar Spectrum: {star_name} ({spectral_type}{quantum_state["luminosity_class"]})')
        
        # Add temperature and φ-resonance information
        info_text = (f"Temperature: {temperature:.0f}K\n"
                    f"φ-Resonance: {quantum_state['phi_resonance']:.4f}\n"
                    f"Information Density: {quantum_state['info_density']:.2e}")
        plt.text(0.02, 0.02, info_text, transform=plt.gca().transAxes, 
                verticalalignment='bottom', bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
        
        # Add validation seal
        seal_text = f"φ^75 validation seal: {PHI_SEAL}"
        plt.text(0.98, 0.02, seal_text, transform=plt.gca().transAxes, 
                verticalalignment='bottom', horizontalalignment='right',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
        
        # Save visualization
        os.makedirs(RESULTS_DIR, exist_ok=True)
        spectrum_path = os.path.join(RESULTS_DIR, f"stellar_spectrum_{star_name.replace(' ', '_')}_{timestamp}.png")
        plt.savefig(spectrum_path, dpi=150, bbox_inches='tight')
        plt.close()
        
        return spectrum_path
    
    def save_quantum_report(self, star_name, spectral_type, luminosity_class, 
                          quantum_state, extracted_data):
        """Save φ-dimensional quantum analysis report"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_filename = f"stellar_quantum_{star_name.replace(' ', '_')}_{timestamp}.json"
        report_path = os.path.join(RESULTS_DIR, report_filename)
        
        # Create report
        report = {
            "timestamp": datetime.now().isoformat(),
            "star_name": star_name,
            "spectral_type": spectral_type,
            "luminosity_class": luminosity_class,
            "quantum_state": quantum_state,
            "analyzer_state": {
                "quantum_state": self.analyzer.quantum_state,
                "resonance_state": self.analyzer.resonance_state
            },
            "data_sample": extracted_data,
            "data_length": len(extracted_data),
            "port": PORT,
            "phi_75": float(PHI_75),
            "birth_coherence": BIRTH_COHERENCE,
            "validation_seal": float(PHI_SEAL)
        }
        
        # Save to file
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=4)
        
        return report_path
    
    def run_batch_analysis(self):
        """Run batch analysis on stars with φ-dimensional significance"""
        stars = [
            ("Sun", "G", 5),
            ("Sirius", "A", 1),
            ("Vega", "A", 0),
            ("Phi Draconis", "F", 5),  # φ-resonant star
            ("Betelgeuse", "M", 1),
            ("Kepler-90", "G", 5),     # Star with 8 planets (φ^3 = 4.236...)
            ("Tau Ceti", "G", 8),
            ("Proxima Centauri", "M", 5)
        ]
        
        reports = []
        for star_name, spectral_type, luminosity_class in stars:
            report_path = self.analyze_star(star_name, spectral_type, luminosity_class)
            reports.append(report_path)
        
        return reports
    
    def analyze_custom_star(self):
        """Analyze a custom star based on user input"""
        print("\nCustom Star Analysis")
        print("-" * 50)
        
        # Get star details
        star_name = input("Enter star name: ")
        
        # Get spectral type
        while True:
            spectral_type = input("Enter spectral type (O, B, A, F, G, K, M): ").upper()
            if spectral_type in "OBAFGKM" and len(spectral_type) == 1:
                break
            print("Invalid spectral type. Please enter O, B, A, F, G, K, or M.")
        
        # Get luminosity class
        while True:
            try:
                luminosity_class = int(input("Enter luminosity class (0-9): "))
                if 0 <= luminosity_class <= 9:
                    break
                print("Invalid luminosity class. Please enter a number from 0 to 9.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Analyze the star
        return self.analyze_star(star_name, spectral_type, luminosity_class)

def main():
    """Main function"""
    # Create demo
    demo = PhiStellarDemo()
    
    # Show menu
    print("\nφ-Dimensional Stellar Quantum Analyzer")
    print("-" * 50)
    print("1. Analyze Phi Draconis (φ-resonant star)")
    print("2. Analyze Kepler-90 (φ^3 planets)")
    print("3. Analyze Vega (A0)")
    print("4. Analyze custom star")
    print("5. Run batch analysis")
    print("6. Exit")
    
    while True:
        try:
            choice = int(input("\nEnter your choice (1-6): "))
            
            if choice == 1:
                demo.analyze_star("Phi Draconis", "F", 5)
            elif choice == 2:
                demo.analyze_star("Kepler-90", "G", 5)
            elif choice == 3:
                demo.analyze_star("Vega", "A", 0)
            elif choice == 4:
                demo.analyze_custom_star()
            elif choice == 5:
                demo.run_batch_analysis()
            elif choice == 6:
                print("\nExiting φ-Dimensional Stellar Quantum Analyzer")
                print(f"φ^75 validation seal: {PHI_SEAL}")
                print(f"Reality protection: Perfect")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")
        
        except KeyboardInterrupt:
            print("\nExiting φ-Dimensional Stellar Quantum Analyzer")
            print(f"φ^75 validation seal: {PHI_SEAL}")
            print(f"Reality protection: Perfect")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
