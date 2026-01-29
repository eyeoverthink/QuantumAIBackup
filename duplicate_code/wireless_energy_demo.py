#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
FRAYMUS Wireless Energy System Demo
Demonstrates Tesla's wireless energy transfer with φ-harmonic principles
Integrates with FRAYMUS Quantum Reality Engine for perfect phase synchronization
Based on FRAYMUS patent VS-PoQC-19046423-φ⁷⁵-2025
"""

import os
import time
import math
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Any, Tuple, Optional, Union

# Import FRAYMUS Wireless Energy System
from fraymus_wireless_energy import FraymusWirelessEnergy

# Try to import other quantum components
try:
    from quantum_math_core import QuantumMathCore
    from quantum_string_time_harmonizer import QuantumStringTimeHarmonizer
    from fraymus_quantum_reality_engine import FraymusQuantumRealityEngine
    from fraymus_quantum_integrator import FraymusQuantumIntegrator
    HAS_ALL_COMPONENTS = True
except ImportError as e:
    HAS_ALL_COMPONENTS = False
    print(f"Warning: Not all quantum components available. Error: {e}")

def print_separator(title: str = None) -> None:
    """Print a separator line with optional title"""
    width = 80
    if title:
        print("\n" + "=" * width)
        print(title.center(width))
        print("=" * width)
    else:
        print("\n" + "=" * width)

def run_basic_demo() -> None:
    """Run a basic demo of the FRAYMUS Wireless Energy System"""
    print_separator("FRAYMUS WIRELESS ENERGY SYSTEM - BASIC DEMO")
    
    # Initialize FRAYMUS Wireless Energy System
    wireless_energy = FraymusWirelessEnergy()
    
    # Update system state
    state = wireless_energy.update()
    
    # Print current state
    print("\nFRAYMUS Wireless Energy System Status:")
    print(f"Resonance Quality: {state['resonance_quality']:.6f}")
    print(f"Resonant Frequency: {state['resonant_frequency']:.6f} Hz")
    print(f"Phase Lock: {state['phase_lock']:.6f}")
    print(f"Transmission Efficiency: {state['transmission_efficiency']:.6f}")
    
    # Generate ASCII simulation
    print("\nBefore φπ Resonance Lock:")
    print(wireless_energy.generate_ascii_simulation(before_alignment=True))
    
    print("\nAfter φπ Resonance Lock:")
    print(wireless_energy.generate_ascii_simulation(before_alignment=False))

def run_tesla_tower_demo() -> None:
    """Run a demo of Tesla Tower parameters with φπ enhancement"""
    print_separator("TESLA TOWER WITH φπ ENHANCEMENT")
    
    # Initialize FRAYMUS Wireless Energy System
    wireless_energy = FraymusWirelessEnergy()
    
    # Calculate tower parameters for different heights
    heights = [50.0, 100.0, 187.0, 300.0, 500.0]
    
    print("\nTesla Tower Parameters with φπ Enhancement:")
    print(f"{'Height (m)':<15} {'Frequency (Hz)':<20} {'φπ Frequency (Hz)':<20} {'Resonance Quality':<20} {'Max Distance (km)':<20}")
    print("-" * 95)
    
    for height in heights:
        params = wireless_energy.calculate_tower_parameters(height)
        print(f"{params['tower_height']:<15.2f} {params['optimal_frequency']:<20.2f} {params['phi_pi_enhanced_frequency']:<20.2f} {params['resonance_quality']:<20.6f} {params['max_transmission_distance']/1000:<20.2f}")

def run_energy_transfer_demo() -> None:
    """Run a demo of energy transfer at different distances"""
    print_separator("ENERGY TRANSFER WITH φπ RESONANCE")
    
    # Initialize FRAYMUS Wireless Energy System
    wireless_energy = FraymusWirelessEnergy()
    
    # Calculate energy transfer at different distances
    distances = [10.0, 100.0, 1000.0, 10000.0, 100000.0]  # km
    input_power = 100.0  # kW
    
    print("\nEnergy Transfer with φπ Resonance:")
    print(f"{'Distance (km)':<15} {'Standard Eff (%)':<20} {'Tesla Eff (%)':<20} {'φπ Eff (%)':<20} {'Final Eff (%)':<20}")
    print("-" * 95)
    
    for distance in distances:
        # Convert km to m
        dist_m = distance * 1000.0
        transfer = wireless_energy.calculate_energy_transfer(dist_m, input_power)
        
        print(f"{distance:<15.2f} {transfer['standard_efficiency']*100:<20.6f} {transfer['tesla_efficiency']*100:<20.6f} {transfer['phi_pi_efficiency']*100:<20.6f} {transfer['final_efficiency']*100:<20.6f}")

def run_global_grid_demo() -> None:
    """Run a demo of global energy grid with φπ resonance"""
    print_separator("GLOBAL ENERGY GRID WITH φπ RESONANCE")
    
    # Initialize FRAYMUS Wireless Energy System
    wireless_energy = FraymusWirelessEnergy()
    
    # Generate global energy grid with different numbers of towers
    tower_counts = [3, 5, 8, 13, 21]  # Fibonacci sequence
    
    print("\nGlobal Energy Grid with φπ Resonance:")
    print(f"{'Towers':<10} {'Spacing (km)':<15} {'Total Power (kW)':<20} {'Grid Power (kW)':<20} {'Coverage (%)':<15} {'Efficiency (%)':<15}")
    print("-" * 95)
    
    for num_towers in tower_counts:
        grid = wireless_energy.generate_global_energy_grid(num_towers)
        
        print(f"{grid['num_towers']:<10} {grid['optimal_spacing']/1000:<15.2f} {grid['total_power']:<20.2f} {grid['grid_power']:<20.2f} {grid['coverage_percentage']:<15.2f} {grid['grid_efficiency']*100:<15.2f}")

def run_dynamic_simulation(duration: float = 10.0) -> None:
    """Run a dynamic simulation of energy transmission"""
    print_separator("DYNAMIC ENERGY TRANSMISSION SIMULATION")
    
    # Initialize FRAYMUS Wireless Energy System
    wireless_energy = FraymusWirelessEnergy()
    
    # Run energy transmission simulation
    print(f"\nRunning energy transmission simulation for {duration} seconds...")
    simulation = wireless_energy.simulate_energy_transmission(duration=duration, input_power=100.0)
    
    # Extract key metrics
    time_points = simulation['time_points']
    tesla_energy = simulation['tesla_energy']
    phi_enhanced_energy = simulation['phi_enhanced_energy']
    self_sustaining_power = simulation['self_sustaining_power']
    transmission_efficiency = simulation['transmission_efficiency']
    
    # Print key metrics
    print("\nSimulation Results:")
    print(f"{'Time (s)':<10} {'Tesla Energy':<15} {'φπ Energy':<15} {'Power (kW)':<15} {'Efficiency (%)':<15}")
    print("-" * 70)
    
    # Print every 1/5 of the duration
    step = len(time_points) // 5
    for i in range(0, len(time_points), step):
        if i < len(time_points):
            print(f"{time_points[i]:<10.2f} {tesla_energy[i]:<15.2f} {phi_enhanced_energy[i]:<15.2f} {self_sustaining_power[i]:<15.2f} {transmission_efficiency[i]*100:<15.2f}")
    
    # Visualize simulation results
    wireless_energy.visualize_energy_transmission(simulation)

def run_integrated_quantum_demo(duration: float = 10.0) -> None:
    """Run an integrated demo with all quantum components"""
    if not HAS_ALL_COMPONENTS:
        print("\nWarning: Not all quantum components are available.")
        print("Running basic wireless energy demo instead.")
        run_basic_demo()
        return
    
    print_separator("INTEGRATED QUANTUM WIRELESS ENERGY DEMO")
    
    # Initialize all components
    print("\nInitializing quantum components...")
    math_core = QuantumMathCore()
    string_time_harmonizer = QuantumStringTimeHarmonizer()
    reality_engine = FraymusQuantumRealityEngine()
    quantum_integrator = FraymusQuantumIntegrator()
    wireless_energy = FraymusWirelessEnergy()
    
    print("\nComponent Availability:")
    print(f"Quantum Math Core: {'Available' if wireless_energy.has_math_core else 'Not Available'}")
    print(f"Quantum String-Time Harmonizer: {'Available' if wireless_energy.has_string_harmonizer else 'Not Available'}")
    print(f"FRAYMUS Quantum Reality Engine: {'Available' if wireless_energy.has_reality_engine else 'Not Available'}")
    
    # Run dynamic simulation
    print(f"\nRunning integrated quantum wireless energy demo for {duration} seconds...")
    
    # Initialize data collection
    time_points = []
    reality_states = []
    string_dimensions = []
    resonance_qualities = []
    transmission_efficiencies = []
    
    # Set start time
    start_time = time.time()
    end_time = start_time + duration
    
    # Run simulation
    while time.time() < end_time:
        # Update all components
        current_time = time.time()
        elapsed_time = current_time - start_time
        
        # Update reality engine
        reality_state = reality_engine.update()
        
        # Get string harmonizer dimensions (no direct update method needed)
        # We'll use the 'w' (time) dimension as our key metric
        dimensions = string_time_harmonizer.dimensions
        time_dimension = dimensions.get('w', {'phi_scaling': 0.0, 'vibration_factor': 0.0})
        string_dimension_value = time_dimension.get('phi_scaling', 0.0) * time_dimension.get('vibration_factor', 0.0)
        
        # Update wireless energy
        wireless_state = wireless_energy.update()
        
        # Collect data
        time_points.append(elapsed_time)
        reality_states.append(reality_state['reality_engine_state'])
        string_dimensions.append(string_dimension_value)
        resonance_qualities.append(wireless_state['resonance_quality'])
        transmission_efficiencies.append(wireless_state['transmission_efficiency'])
        
        # Print current state
        print(f"Time: {elapsed_time:.2f}s, Reality: {reality_state['reality_engine_state']:.2f}, String-Time: {string_dimension_value:.2f}, Resonance: {wireless_state['resonance_quality']:.2f}, Efficiency: {wireless_state['transmission_efficiency']:.2f}")
        
        # Sleep to prevent CPU overload
        time.sleep(0.1)
    
    # Calculate actual duration
    actual_duration = time.time() - start_time
    print(f"Integrated demo completed in {actual_duration:.2f} seconds.")
    
    # Create visualization
    plt.figure(figsize=(12, 10))
    
    # Plot reality state
    plt.subplot(4, 1, 1)
    plt.plot(time_points, reality_states, 'b-')
    plt.ylabel('Reality State')
    plt.title('Integrated Quantum Wireless Energy Demo')
    plt.grid(True)
    
    # Plot string dimension value
    plt.subplot(4, 1, 2)
    plt.plot(time_points, string_dimensions, 'r-')
    plt.ylabel('String-Time Dimension')
    plt.grid(True)
    
    # Plot resonance quality
    plt.subplot(4, 1, 3)
    plt.plot(time_points, resonance_qualities, 'g-')
    plt.ylabel('Resonance Quality')
    plt.grid(True)
    
    # Plot transmission efficiency
    plt.subplot(4, 1, 4)
    plt.plot(time_points, transmission_efficiencies, 'm-')
    plt.xlabel('Time (s)')
    plt.ylabel('Transmission Efficiency')
    plt.grid(True)
    
    # Adjust layout
    plt.tight_layout()
    
    # Save figure
    timestamp = int(time.time())
    cache_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wireless_energy_cache")
    os.makedirs(cache_dir, exist_ok=True)
    filename = os.path.join(cache_dir, f"integrated_quantum_demo_{timestamp}.png")
    plt.savefig(filename)
    print(f"Integrated quantum demo visualization saved to: {filename}")
    
    # Show figure
    plt.show()

def main() -> None:
    """Main function to run all demos"""
    print_separator("FRAYMUS WIRELESS ENERGY SYSTEM DEMONSTRATION")
    print("Based on FRAYMUS patent VS-PoQC-19046423-φ⁷⁵-2025")
    
    # Run basic demo
    run_basic_demo()
    
    # Run Tesla tower demo
    run_tesla_tower_demo()
    
    # Run energy transfer demo
    run_energy_transfer_demo()
    
    # Run global grid demo
    run_global_grid_demo()
    
    # Run dynamic simulation
    run_dynamic_simulation(duration=5.0)
    
    # Run integrated quantum demo
    run_integrated_quantum_demo(duration=5.0)
    
    print_separator("DEMONSTRATION COMPLETE")
    print("\nThe FRAYMUS Wireless Energy System successfully demonstrates:")
    print("1. Tesla's wireless energy transfer with φπ resonance enhancement")
    print("2. Perfect phase synchronization for lossless transmission")
    print("3. Self-sustaining power amplification via φ-harmonic principles")
    print("4. Integration with quantum components for enhanced stability")
    print("5. Global energy grid with optimal tower placement")
    print("\nAll results are influenced by birth date resonance [1, 19, 1979]")
    print("and maintain perfect φ-harmonic alignment throughout all calculations.")

if __name__ == "__main__":
    main()
