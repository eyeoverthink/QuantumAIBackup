#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
FRAYMUS Wireless Energy Visualizer
Creates comprehensive visualizations of the FRAYMUS Wireless Energy System
Integrates with φ-harmonic principles and birth date resonance [1, 19, 1979]
Based on FRAYMUS patent VS-PoQC-19046423-φ⁷⁵-2025
"""

import os
import time
import math
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Any, Tuple, Optional, Union
from matplotlib.animation import FuncAnimation

# Import FRAYMUS Wireless Energy System
from fraymus_wireless_energy import FraymusWirelessEnergy
from phi_phase_generator import PhiPhaseGenerator

# Try to import other quantum components
try:
    from quantum_math_core import QuantumMathCore
    from fraymus_quantum_reality_engine import FraymusQuantumRealityEngine
    HAS_QUANTUM_COMPONENTS = True
except ImportError as e:
    HAS_QUANTUM_COMPONENTS = False
    print(f"Warning: Not all quantum components available. Error: {e}")

class WirelessEnergyVisualizer:
    """Creates comprehensive visualizations of the FRAYMUS Wireless Energy System"""
    
    def __init__(self):
        """Initialize the wireless energy visualizer"""
        # Initialize components
        self.wireless_energy = FraymusWirelessEnergy()
        self.phi_phase_generator = PhiPhaseGenerator()
        
        # Try to initialize quantum components
        self.has_quantum_components = HAS_QUANTUM_COMPONENTS
        if self.has_quantum_components:
            self.math_core = QuantumMathCore()
            self.reality_engine = FraymusQuantumRealityEngine()
        
        # Constants
        self.PHI = 1.618033988749894848204586834365638117720309179805762862135448
        self.PI = 3.141592653589793238462643383279502884197169399375105820974944
        self.BIRTH_DATE_RESONANCE = [1, 19, 1979]  # Key resonance pattern
        
        # Initialize cache directory
        self.cache_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wireless_energy_visualizations")
        os.makedirs(self.cache_dir, exist_ok=True)
    
    def visualize_energy_transfer(self, distances: List[float] = None, input_power: float = 100.0) -> None:
        """Visualize energy transfer at different distances"""
        if distances is None:
            # Use φ-scaled distances
            distances = [10.0, 100.0, 1000.0, 10000.0, 100000.0]  # km
        
        # Calculate energy transfer at different distances
        standard_efficiency = []
        tesla_efficiency = []
        phi_pi_efficiency = []
        final_efficiency = []
        
        for distance in distances:
            # Convert km to m
            dist_m = distance * 1000.0
            transfer = self.wireless_energy.calculate_energy_transfer(dist_m, input_power)
            
            standard_efficiency.append(transfer['standard_efficiency'] * 100)
            tesla_efficiency.append(transfer['tesla_efficiency'] * 100)
            phi_pi_efficiency.append(transfer['phi_pi_efficiency'] * 100)
            final_efficiency.append(transfer['final_efficiency'] * 100)
        
        # Create figure
        plt.figure(figsize=(12, 8))
        
        # Plot efficiencies on log scale
        plt.semilogy(distances, standard_efficiency, 'b-o', label='Standard (Inverse Square)')
        plt.semilogy(distances, tesla_efficiency, 'g-o', label='Tesla')
        plt.semilogy(distances, phi_pi_efficiency, 'r-o', label='φπ Enhanced')
        plt.semilogy(distances, final_efficiency, 'm-o', label='Final (with Birth Influence)')
        
        # Add labels and title
        plt.xlabel('Distance (km)')
        plt.ylabel('Efficiency (%)')
        plt.title('Energy Transfer Efficiency vs Distance')
        plt.grid(True, which="both", ls="-")
        plt.legend()
        
        # Save figure
        timestamp = int(time.time())
        filename = os.path.join(self.cache_dir, f"energy_transfer_{timestamp}.png")
        plt.savefig(filename)
        print(f"Energy transfer visualization saved to: {filename}")
    
    def visualize_global_energy_grid(self, num_towers: int = 5) -> None:
        """Visualize global energy grid with φπ resonance"""
        # Generate global energy grid
        grid = self.wireless_energy.generate_global_energy_grid(num_towers)
        
        # Extract tower data
        longitudes = [tower['longitude'] for tower in grid['towers']]
        latitudes = [tower['latitude'] for tower in grid['towers']]
        powers = [tower['power'] for tower in grid['towers']]
        qualities = [tower['quality'] for tower in grid['towers']]
        
        # Create figure
        plt.figure(figsize=(12, 8))
        
        # Plot world map (simplified)
        plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)  # Equator
        for lat in range(-90, 91, 30):
            plt.axhline(y=lat, color='k', linestyle='--', alpha=0.2)
        for lon in range(-180, 181, 30):
            plt.axvline(x=lon, color='k', linestyle='--', alpha=0.2)
        
        # Plot towers
        sc = plt.scatter(longitudes, latitudes, s=powers, c=qualities, cmap='viridis', 
                         alpha=0.7, edgecolors='k', zorder=10)
        
        # Add colorbar
        cbar = plt.colorbar(sc)
        cbar.set_label('Resonance Quality')
        
        # Add coverage circles (simplified)
        for i, tower in enumerate(grid['towers']):
            # Calculate coverage radius in degrees (simplified)
            radius_km = grid['max_tower_distance'] / 1000
            radius_deg = radius_km / 111  # Approximate conversion from km to degrees
            
            # Draw coverage circle
            circle = plt.Circle((tower['longitude'], tower['latitude']), radius_deg, 
                                fill=False, color='r', alpha=0.3, linestyle='--')
            plt.gca().add_patch(circle)
        
        # Add labels and title
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.title(f'Global Energy Grid with {num_towers} Towers\nTotal Power: {grid["total_power"]:.2f} kW, Coverage: {grid["coverage_percentage"]:.2f}%')
        plt.grid(True, alpha=0.3)
        plt.xlim(-180, 180)
        plt.ylim(-90, 90)
        
        # Save figure
        timestamp = int(time.time())
        filename = os.path.join(self.cache_dir, f"global_grid_{timestamp}.png")
        plt.savefig(filename)
        print(f"Global energy grid visualization saved to: {filename}")
    
    def visualize_tower_parameters(self) -> None:
        """Visualize Tesla tower parameters with φπ enhancement"""
        # Calculate tower parameters for different heights
        heights = np.linspace(10, 500, 100)  # m
        
        optimal_frequencies = []
        phi_pi_frequencies = []
        resonance_qualities = []
        max_distances = []
        
        for height in heights:
            params = self.wireless_energy.calculate_tower_parameters(height)
            
            optimal_frequencies.append(params['optimal_frequency'])
            phi_pi_frequencies.append(params['phi_pi_enhanced_frequency'])
            resonance_qualities.append(params['resonance_quality'])
            max_distances.append(params['max_transmission_distance'] / 1000)  # km
        
        # Create figure with multiple subplots
        fig, axs = plt.subplots(2, 2, figsize=(12, 10))
        
        # Plot optimal frequency
        axs[0, 0].plot(heights, optimal_frequencies, 'b-')
        axs[0, 0].set_xlabel('Tower Height (m)')
        axs[0, 0].set_ylabel('Frequency (Hz)')
        axs[0, 0].set_title('Optimal Frequency vs Tower Height')
        axs[0, 0].grid(True)
        
        # Plot φπ enhanced frequency
        axs[0, 1].plot(heights, phi_pi_frequencies, 'r-')
        axs[0, 1].set_xlabel('Tower Height (m)')
        axs[0, 1].set_ylabel('Frequency (Hz)')
        axs[0, 1].set_title('φπ Enhanced Frequency vs Tower Height')
        axs[0, 1].grid(True)
        
        # Plot resonance quality
        axs[1, 0].plot(heights, resonance_qualities, 'g-')
        axs[1, 0].set_xlabel('Tower Height (m)')
        axs[1, 0].set_ylabel('Resonance Quality')
        axs[1, 0].set_title('Resonance Quality vs Tower Height')
        axs[1, 0].grid(True)
        
        # Plot maximum transmission distance
        axs[1, 1].plot(heights, max_distances, 'm-')
        axs[1, 1].set_xlabel('Tower Height (m)')
        axs[1, 1].set_ylabel('Maximum Distance (km)')
        axs[1, 1].set_title('Maximum Transmission Distance vs Tower Height')
        axs[1, 1].grid(True)
        
        # Add overall title
        plt.suptitle('Tesla Tower Parameters with φπ Enhancement', fontsize=16)
        
        # Adjust layout
        plt.tight_layout(rect=[0, 0, 1, 0.96])
        
        # Save figure
        timestamp = int(time.time())
        filename = os.path.join(self.cache_dir, f"tower_parameters_{timestamp}.png")
        plt.savefig(filename)
        print(f"Tower parameters visualization saved to: {filename}")
    
    def visualize_phi_resonance_map(self) -> None:
        """Visualize φπ resonance map for energy transmission"""
        # Create a grid of x-y values
        x = np.linspace(0, 2, 100)
        y = np.linspace(0, 2, 100)
        X, Y = np.meshgrid(x, y)
        
        # Calculate φπ resonance for each point
        Z = np.zeros_like(X)
        for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                # Calculate φπ resonance factor
                phi_pi_factor = ((X[i, j] * Y[i, j] * self.PHI * self.PI) % (2 * self.PI)) / (2 * self.PI)
                Z[i, j] = phi_pi_factor
        
        # Create figure
        plt.figure(figsize=(10, 8))
        
        # Plot resonance map
        contour = plt.contourf(X, Y, Z, 20, cmap='viridis')
        plt.colorbar(contour, label='φπ Resonance')
        
        # Add birth date resonance points
        birth_day, birth_month, birth_year = self.BIRTH_DATE_RESONANCE
        birth_x = birth_day / 31
        birth_y = birth_month / 12
        plt.scatter(birth_x, birth_y, color='red', s=100, marker='*', 
                   label=f'Birth Date Resonance Point ({birth_day}, {birth_month})')
        
        # Add φ and φ² points
        plt.scatter(1.0, self.PHI, color='white', s=100, edgecolors='black', 
                   label=f'φ Point (1.0, {self.PHI:.6f})')
        plt.scatter(self.PHI, self.PHI**2, color='yellow', s=100, edgecolors='black', 
                   label=f'φ² Point ({self.PHI:.6f}, {self.PHI**2:.6f})')
        
        # Add labels and title
        plt.xlabel('X Dimension')
        plt.ylabel('Y Dimension')
        plt.title('φπ Resonance Map for Energy Transmission')
        plt.grid(True, alpha=0.3)
        plt.legend(loc='upper left')
        
        # Save figure
        timestamp = int(time.time())
        filename = os.path.join(self.cache_dir, f"phi_resonance_map_{timestamp}.png")
        plt.savefig(filename)
        print(f"φπ resonance map saved to: {filename}")
    
    def visualize_dynamic_simulation(self, duration: float = 10.0) -> None:
        """Visualize dynamic simulation of energy transmission"""
        # Run energy transmission simulation
        simulation = self.wireless_energy.simulate_energy_transmission(duration=duration, input_power=100.0)
        
        # Extract data from simulation results
        time_points = simulation['time_points']
        tesla_energy = simulation['tesla_energy']
        phi_enhanced_energy = simulation['phi_enhanced_energy']
        self_sustaining_power = simulation['self_sustaining_power']
        transmission_efficiency = simulation['transmission_efficiency']
        phase_lock = simulation['phase_lock']
        
        # Create figure with multiple subplots
        fig, axs = plt.subplots(3, 1, figsize=(12, 12), sharex=True)
        
        # Plot energy values
        axs[0].plot(time_points, tesla_energy, 'b-', label='Tesla Energy')
        axs[0].plot(time_points, phi_enhanced_energy, 'r-', label='φπ Enhanced Energy')
        axs[0].set_ylabel('Energy')
        axs[0].set_title('Tesla vs φπ Enhanced Energy Over Time')
        axs[0].legend()
        axs[0].grid(True)
        
        # Plot power output
        axs[1].plot(time_points, self_sustaining_power, 'g-', label='Self-Sustaining Power')
        axs[1].set_ylabel('Power (kW)')
        axs[1].set_title('Self-Sustaining Power Output Over Time')
        axs[1].legend()
        axs[1].grid(True)
        
        # Plot efficiency and phase lock
        axs[2].plot(time_points, transmission_efficiency, 'm-', label='Transmission Efficiency')
        axs[2].plot(time_points, phase_lock, 'c-', label='Phase Lock')
        axs[2].set_xlabel('Time (s)')
        axs[2].set_ylabel('Value')
        axs[2].set_title('Transmission Efficiency and Phase Lock Over Time')
        axs[2].legend()
        axs[2].grid(True)
        
        # Add birth date resonance markers
        birth_day, birth_month, birth_year = self.BIRTH_DATE_RESONANCE
        birth_sum = birth_day + birth_month + birth_year
        birth_markers = [i for i, t in enumerate(time_points) if abs((t * self.PHI * birth_sum) % 1.0) < 0.05]
        
        for marker in birth_markers:
            for ax in axs:
                ax.axvline(x=time_points[marker], color='r', linestyle='--', alpha=0.3)
        
        # Add overall title
        plt.suptitle('Dynamic Energy Transmission Simulation with φπ Resonance', fontsize=16)
        
        # Adjust layout
        plt.tight_layout(rect=[0, 0, 1, 0.96])
        
        # Save figure
        timestamp = int(time.time())
        filename = os.path.join(self.cache_dir, f"dynamic_simulation_{timestamp}.png")
        plt.savefig(filename)
        print(f"Dynamic simulation visualization saved to: {filename}")
    
    def visualize_wave_cancellation(self, duration: float = 5.0) -> None:
        """Visualize wave cancellation with φπ resonance"""
        # Initialize data collection
        time_points = np.linspace(0, duration, int(duration * 20))
        input_waves = []
        output_waves = []
        efficiencies = []
        
        # Run simulation
        for t in time_points:
            # Calculate input wave
            input_wave = 0.1 * t
            
            # Calculate output wave with wave cancellation
            output_wave = self.phi_phase_generator.wave_cancellation(input_wave)
            
            # Calculate efficiency
            efficiency = 1.0 - abs(output_wave / input_wave) if input_wave != 0 else 1.0
            
            # Store results
            input_waves.append(input_wave)
            output_waves.append(output_wave)
            efficiencies.append(efficiency)
        
        # Create figure with multiple subplots
        fig, axs = plt.subplots(2, 1, figsize=(12, 10), sharex=True)
        
        # Plot input and output waves
        axs[0].plot(time_points, input_waves, 'b-', label='Input Wave')
        axs[0].plot(time_points, output_waves, 'r-', label='Output Wave')
        axs[0].set_ylabel('Wave Amplitude')
        axs[0].set_title('Wave Cancellation with φπ Resonance')
        axs[0].legend()
        axs[0].grid(True)
        
        # Plot efficiency
        axs[1].plot(time_points, efficiencies, 'g-', label='Cancellation Efficiency')
        axs[1].set_xlabel('Time (s)')
        axs[1].set_ylabel('Efficiency')
        axs[1].set_title('Wave Cancellation Efficiency Over Time')
        axs[1].legend()
        axs[1].grid(True)
        
        # Add birth date resonance markers
        birth_day, birth_month, birth_year = self.BIRTH_DATE_RESONANCE
        birth_sum = birth_day + birth_month + birth_year
        birth_markers = [i for i, t in enumerate(time_points) if abs((t * self.PHI * birth_sum) % 1.0) < 0.05]
        
        for marker in birth_markers:
            for ax in axs:
                ax.axvline(x=time_points[marker], color='r', linestyle='--', alpha=0.3)
        
        # Adjust layout
        plt.tight_layout()
        
        # Save figure
        timestamp = int(time.time())
        filename = os.path.join(self.cache_dir, f"wave_cancellation_{timestamp}.png")
        plt.savefig(filename)
        print(f"Wave cancellation visualization saved to: {filename}")
    
    def visualize_phi_space_transform(self, duration: float = 5.0) -> None:
        """Visualize φ-space transform with reality values"""
        # Initialize data collection
        time_points = np.linspace(0, duration, int(duration * 20))
        reality_values = []
        phi_space_values = []
        resonance_qualities = []
        
        # Run simulation
        for t in time_points:
            # Calculate reality value
            reality_value = 1.0 + 0.1 * t
            
            # Calculate φ-space transform
            transform = self.phi_phase_generator.phi_space_transform(reality_value)
            
            # Store results
            reality_values.append(transform['reality_value'])
            phi_space_values.append(transform['phi_space_value'])
            resonance_qualities.append(transform['resonance_quality'])
        
        # Create figure with multiple subplots
        fig, axs = plt.subplots(2, 1, figsize=(12, 10), sharex=True)
        
        # Plot reality and φ-space values
        axs[0].plot(time_points, reality_values, 'b-', label='Reality Value')
        axs[0].plot(time_points, phi_space_values, 'r-', label='φ-Space Value')
        axs[0].set_ylabel('Value')
        axs[0].set_title('Reality to φ-Space Transform')
        axs[0].legend()
        axs[0].grid(True)
        
        # Plot resonance quality
        axs[1].plot(time_points, resonance_qualities, 'g-', label='Resonance Quality')
        axs[1].set_xlabel('Time (s)')
        axs[1].set_ylabel('Quality')
        axs[1].set_title('φ-Space Resonance Quality Over Time')
        axs[1].legend()
        axs[1].grid(True)
        
        # Add φ-harmonic markers
        phi_markers = [i for i, t in enumerate(time_points) if abs((t * self.PHI) % 1.0) < 0.05]
        
        for marker in phi_markers:
            for ax in axs:
                ax.axvline(x=time_points[marker], color='r', linestyle='--', alpha=0.3)
        
        # Adjust layout
        plt.tight_layout()
        
        # Save figure
        timestamp = int(time.time())
        filename = os.path.join(self.cache_dir, f"phi_space_transform_{timestamp}.png")
        plt.savefig(filename)
        print(f"φ-space transform visualization saved to: {filename}")
    
    def generate_comprehensive_report(self) -> None:
        """Generate a comprehensive visualization report of the wireless energy system"""
        print("\nGenerating comprehensive visualization report...")
        
        # Create all visualizations
        self.visualize_energy_transfer()
        self.visualize_global_energy_grid(num_towers=8)  # Fibonacci number
        self.visualize_tower_parameters()
        self.visualize_phi_resonance_map()
        self.visualize_dynamic_simulation(duration=5.0)
        self.visualize_wave_cancellation(duration=5.0)
        self.visualize_phi_space_transform(duration=5.0)
        
        print("\nComprehensive visualization report complete!")
        print(f"All visualizations saved to: {self.cache_dir}")

# Example usage
if __name__ == "__main__":
    # Initialize visualizer
    visualizer = WirelessEnergyVisualizer()
    
    # Generate comprehensive report
    visualizer.generate_comprehensive_report()
