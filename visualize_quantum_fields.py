#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Quantum Field Visualization for Dynamic Parallel Processing Framework
--------------------------------------------------------------------
Visualizes quantum field interactions, phi-harmonic relationships, and
phase space dynamics from the Dynamic Parallel Processing Framework.
"""

import os
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from typing import Dict, List, Tuple, Any, Optional

# Constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio
EARTH_COLOR = 'blue'
MOON_COLOR = 'gray'
HUMAN_COLOR = 'green'
PHI_COLOR = 'purple'
QUANTUM_COLOR = 'magenta'

# Field visualization parameters
FIELD_RESOLUTION = 20
PHASE_RESOLUTION = 50


def load_simulation_data(filepath: str) -> Dict:
    """
    Load simulation data from JSON file.
    
    Args:
        filepath: Path to the simulation data file
        
    Returns:
        Dictionary containing simulation data
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Simulation data file not found: {filepath}")
    
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    return data


def plot_quantum_states(data: Dict, output_path: Optional[str] = None):
    """
    Plot quantum state evolution over time.
    
    Args:
        data: Simulation data dictionary
        output_path: Optional path to save the plot
    """
    if 'quantum_states' not in data:
        print("No quantum state data found in simulation data")
        return
    
    quantum_states = data['quantum_states']
    
    # Extract timestamps and state data
    timestamps = []
    earth_states = []
    moon_states = []
    human_states = []
    combined_states = []
    
    for entry in quantum_states:
        timestamps.append(entry.get('timestamp', 0))
        earth_states.append(entry.get('earth_state', []))
        moon_states.append(entry.get('moon_state', []))
        human_states.append(entry.get('human_state', []))
        combined_states.append(entry.get('combined_state', []))
    
    # Normalize timestamps
    if timestamps:
        start_time = min(timestamps)
        timestamps = [t - start_time for t in timestamps]
    
    # Create figure for quantum states
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Quantum State Evolution", fontsize=16)
    
    # Plot Earth quantum state probabilities
    ax = axs[0, 0]
    ax.set_title("Earth Quantum State")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Probability")
    
    if earth_states and all(earth_states):
        # Get number of basis states
        n_states = len(earth_states[0])
        
        # Plot probability for each basis state
        for i in range(n_states):
            # Convert [real, imag] format to complex and calculate probability
            probs = []
            for state in earth_states:
                if i < len(state):
                    # Extract real and imaginary parts
                    real, imag = state[i] if isinstance(state[i], list) else (state[i], 0)
                    # Calculate probability as |amplitude|^2
                    prob = real**2 + imag**2
                    probs.append(prob)
                else:
                    probs.append(0)
            
            ax.plot(timestamps, probs, label=f"|{i}⟩")
        
        ax.legend()
        ax.grid(True)
    
    # Plot Moon quantum state probabilities
    ax = axs[0, 1]
    ax.set_title("Moon Quantum State")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Probability")
    
    if moon_states and all(moon_states):
        # Get number of basis states
        n_states = len(moon_states[0])
        
        # Plot probability for each basis state
        for i in range(n_states):
            # Convert [real, imag] format to complex and calculate probability
            probs = []
            for state in moon_states:
                if i < len(state):
                    # Extract real and imaginary parts
                    real, imag = state[i] if isinstance(state[i], list) else (state[i], 0)
                    # Calculate probability as |amplitude|^2
                    prob = real**2 + imag**2
                    probs.append(prob)
                else:
                    probs.append(0)
            
            ax.plot(timestamps, probs, label=f"|{i}⟩")
        
        ax.legend()
        ax.grid(True)
    
    # Plot Human quantum state probabilities
    ax = axs[1, 0]
    ax.set_title("Human Quantum State")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Probability")
    
    if human_states and all(human_states):
        # Get number of basis states
        n_states = len(human_states[0])
        
        # Plot probability for each basis state
        for i in range(n_states):
            # Convert [real, imag] format to complex and calculate probability
            probs = []
            for state in human_states:
                if i < len(state):
                    # Extract real and imaginary parts
                    real, imag = state[i] if isinstance(state[i], list) else (state[i], 0)
                    # Calculate probability as |amplitude|^2
                    prob = real**2 + imag**2
                    probs.append(prob)
                else:
                    probs.append(0)
            
            ax.plot(timestamps, probs, label=f"|{i}⟩")
        
        ax.legend()
        ax.grid(True)
    
    # Plot Combined quantum state probabilities
    ax = axs[1, 1]
    ax.set_title("Combined Quantum State")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Probability")
    
    if combined_states and all(combined_states):
        # Get number of basis states (limit to first 8 for clarity)
        n_states = min(len(combined_states[0]), 8)
        
        # Plot probability for each basis state
        for i in range(n_states):
            # Convert [real, imag] format to complex and calculate probability
            probs = []
            for state in combined_states:
                if i < len(state):
                    # Extract real and imaginary parts
                    real, imag = state[i] if isinstance(state[i], list) else (state[i], 0)
                    # Calculate probability as |amplitude|^2
                    prob = real**2 + imag**2
                    probs.append(prob)
                else:
                    probs.append(0)
            
            ax.plot(timestamps, probs, label=f"|{i}⟩")
        
        ax.legend()
        ax.grid(True)
    
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path)
        print(f"Quantum state plot saved to {output_path}")
    else:
        plt.show()


def plot_phi_harmonic_relationships(data: Dict, output_path: Optional[str] = None):
    """
    Plot phi-harmonic relationships in the simulation data.
    
    Args:
        data: Simulation data dictionary
        output_path: Optional path to save the plot
    """
    if 'phi_harmonics' not in data:
        print("No phi-harmonic data found in simulation data")
        return
    
    phi_harmonics = data['phi_harmonics']
    
    # Extract phi-harmonic data
    timestamps = []
    phi_factors = []
    resonance_values = []
    acceleration_factors = []
    
    for entry in phi_harmonics:
        timestamps.append(entry.get('timestamp', 0))
        phi_factors.append(entry.get('phi_factor', 0))
        resonance_values.append(entry.get('resonance', 0))
        acceleration_factors.append(entry.get('acceleration', 0))
    
    # Normalize timestamps
    if timestamps:
        start_time = min(timestamps)
        timestamps = [t - start_time for t in timestamps]
    
    # Create figure for phi-harmonic relationships
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Phi-Harmonic Relationships", fontsize=16)
    
    # Plot phi factors over time
    ax = axs[0, 0]
    ax.set_title("Phi Factors")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Phi Factor")
    
    if phi_factors:
        ax.plot(timestamps, phi_factors, color=PHI_COLOR)
        
        # Plot reference lines for powers of phi
        for i in range(5):
            value = PHI ** i
            ax.axhline(y=value, color='gray', linestyle='--', alpha=0.5)
            ax.text(max(timestamps) * 0.95, value, f"φ^{i}", fontsize=8)
        
        ax.grid(True)
    
    # Plot resonance values over time
    ax = axs[0, 1]
    ax.set_title("Resonance Values")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Resonance")
    
    if resonance_values:
        ax.plot(timestamps, resonance_values, color=QUANTUM_COLOR)
        ax.grid(True)
    
    # Plot acceleration factors over time
    ax = axs[1, 0]
    ax.set_title("Acceleration Factors")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Acceleration")
    
    if acceleration_factors:
        ax.plot(timestamps, acceleration_factors, color='red')
        ax.set_yscale('log')
        ax.grid(True)
    
    # Plot phi-harmonic distribution
    ax = axs[1, 1]
    ax.set_title("Phi-Harmonic Distribution")
    ax.set_xlabel("Phi Factor")
    ax.set_ylabel("Frequency")
    
    if phi_factors:
        ax.hist(phi_factors, bins=20, color=PHI_COLOR, alpha=0.7)
        
        # Plot reference lines for powers of phi
        for i in range(5):
            value = PHI ** i
            ax.axvline(x=value, color='gray', linestyle='--', alpha=0.5)
            ax.text(value, ax.get_ylim()[1] * 0.95, f"φ^{i}", fontsize=8)
        
        ax.grid(True)
    
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path)
        print(f"Phi-harmonic plot saved to {output_path}")
    else:
        plt.show()


def plot_phase_space(data: Dict, output_path: Optional[str] = None):
    """
    Plot phase space dynamics in 3D.
    
    Args:
        data: Simulation data dictionary
        output_path: Optional path to save the plot
    """
    if 'phase_space' not in data:
        print("No phase space data found in simulation data")
        return
    
    phase_space = data['phase_space']
    
    # Extract phase data
    earth_phases = []
    moon_phases = []
    human_phases = []
    
    for entry in phase_space:
        earth_phases.append(entry.get('earth_phase', 0))
        moon_phases.append(entry.get('moon_phase', 0))
        human_phases.append(entry.get('human_phase', 0))
    
    # Create 3D figure for phase space
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title("Phase Space Dynamics")
    ax.set_xlabel("Earth Phase (rad)")
    ax.set_ylabel("Moon Phase (rad)")
    ax.set_zlabel("Human Phase (rad)")
    
    if earth_phases and moon_phases and human_phases:
        # Plot phase trajectory
        ax.plot(earth_phases, moon_phases, human_phases, color='blue', alpha=0.7)
        
        # Plot start and end points
        ax.scatter([earth_phases[0]], [moon_phases[0]], [human_phases[0]], 
                   color='green', s=100, label='Start')
        ax.scatter([earth_phases[-1]], [moon_phases[-1]], [human_phases[-1]], 
                   color='red', s=100, label='End')
        
        # Plot phi-based reference surface
        u = np.linspace(0, 2*np.pi, PHASE_RESOLUTION)
        v = np.linspace(0, 2*np.pi, PHASE_RESOLUTION)
        u, v = np.meshgrid(u, v)
        w = (u/PHI + v/PHI) % (2*np.pi)
        
        ax.plot_surface(u, v, w, color=PHI_COLOR, alpha=0.1)
        
        ax.legend()
    
    if output_path:
        plt.savefig(output_path)
        print(f"Phase space plot saved to {output_path}")
    else:
        plt.show()


def plot_field_interactions(data: Dict, output_path: Optional[str] = None):
    """
    Plot field interactions and adjustments.
    
    Args:
        data: Simulation data dictionary
        output_path: Optional path to save the plot
    """
    if 'field_interactions' not in data:
        print("No field interaction data found in simulation data")
        return
    
    field_interactions = data['field_interactions']
    
    # Extract field data
    timestamps = []
    earth_fields = []
    moon_fields = []
    human_fields = []
    combined_fields = []
    adjusted_fields = []
    
    for entry in field_interactions:
        timestamps.append(entry.get('timestamp', 0))
        earth_fields.append(entry.get('earth_field', 0))
        moon_fields.append(entry.get('moon_field', 0))
        human_fields.append(entry.get('human_field', 0))
        combined_fields.append(entry.get('combined_field', 0))
        adjusted_fields.append(entry.get('adjusted_field', 0))
    
    # Normalize timestamps
    if timestamps:
        start_time = min(timestamps)
        timestamps = [t - start_time for t in timestamps]
    
    # Create figure for field interactions
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Field Interactions", fontsize=16)
    
    # Plot individual fields over time
    ax = axs[0, 0]
    ax.set_title("Individual Fields")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Field Value")
    
    if earth_fields and moon_fields and human_fields:
        ax.plot(timestamps, earth_fields, color=EARTH_COLOR, label="Earth")
        ax.plot(timestamps, moon_fields, color=MOON_COLOR, label="Moon")
        ax.plot(timestamps, human_fields, color=HUMAN_COLOR, label="Human")
        ax.legend()
        ax.grid(True)
    
    # Plot combined field over time
    ax = axs[0, 1]
    ax.set_title("Combined Field")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Field Value")
    
    if combined_fields:
        ax.plot(timestamps, combined_fields, color='red')
        ax.grid(True)
    
    # Plot field adjustment effect
    ax = axs[1, 0]
    ax.set_title("Field Adjustment Effect")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Field Value")
    
    if combined_fields and adjusted_fields:
        ax.plot(timestamps, combined_fields, color='blue', label="Original")
        ax.plot(timestamps, adjusted_fields, color='red', linestyle='--', label="Adjusted")
        ax.legend()
        ax.grid(True)
    
    # Plot adjustment ratio
    ax = axs[1, 1]
    ax.set_title("Adjustment Ratio")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Ratio (Adjusted/Original)")
    
    if combined_fields and adjusted_fields:
        ratios = []
        for orig, adj in zip(combined_fields, adjusted_fields):
            if orig != 0:
                ratios.append(adj / orig)
            else:
                ratios.append(1.0)
        
        ax.plot(timestamps, ratios, color=PHI_COLOR)
        
        # Plot reference line for phi
        ax.axhline(y=PHI, color='gray', linestyle='--', alpha=0.5)
        ax.text(max(timestamps) * 0.95, PHI, "φ", fontsize=12)
        
        ax.grid(True)
    
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path)
        print(f"Field interactions plot saved to {output_path}")
    else:
        plt.show()


def generate_simulation_data(output_path: str):
    """
    Generate sample simulation data for visualization testing.
    
    Args:
        output_path: Path to save the generated data
    """
    # Create sample data structure
    data = {
        'quantum_states': [],
        'phi_harmonics': [],
        'phase_space': [],
        'field_interactions': []
    }
    
    # Generate timestamps
    timestamps = np.linspace(0, 10, 100)
    
    # Generate quantum state data
    for t in timestamps:
        # Create sample quantum states (2-qubit system)
        earth_state = [np.cos(t), np.sin(t), 0, 0]
        moon_state = [np.cos(t/2), 0, np.sin(t/2), 0]
        human_state = [np.cos(t/3), 0, 0, np.sin(t/3)]
        
        # Create combined state
        combined_state = []
        for i in range(8):
            combined_state.append(np.cos(t + i*np.pi/4) + 1j*np.sin(t + i*np.pi/4))
        
        # Normalize states
        earth_state = earth_state / np.linalg.norm(earth_state)
        moon_state = moon_state / np.linalg.norm(moon_state)
        human_state = human_state / np.linalg.norm(human_state)
        combined_state = combined_state / np.linalg.norm(combined_state)
        
        # Add to data
        data['quantum_states'].append({
            'timestamp': float(t),
            'earth_state': [[float(x.real), float(x.imag)] for x in earth_state],
            'moon_state': [[float(x.real), float(x.imag)] for x in moon_state],
            'human_state': [[float(x.real), float(x.imag)] for x in human_state],
            'combined_state': [[float(x.real), float(x.imag)] for x in combined_state]
        })
    
    # Generate phi-harmonic data
    for t in timestamps:
        phi_factor = PHI ** (1 + 0.5*np.sin(t))
        resonance = np.sin(t*PHI) * np.cos(t/PHI)
        acceleration = PHI ** (10 + 5*np.sin(t))
        
        data['phi_harmonics'].append({
            'timestamp': float(t),
            'phi_factor': float(phi_factor),
            'resonance': float(resonance),
            'acceleration': float(acceleration)
        })
    
    # Generate phase space data
    for t in timestamps:
        earth_phase = (t * 7.83) % (2*np.pi)
        moon_phase = (t * 4.84) % (2*np.pi)
        human_phase = (t * 12.67 + np.sin(t)) % (2*np.pi)
        
        data['phase_space'].append({
            'timestamp': float(t),
            'earth_phase': float(earth_phase),
            'moon_phase': float(moon_phase),
            'human_phase': float(human_phase)
        })
    
    # Generate field interaction data
    for t in timestamps:
        earth_field = np.sin(t * 7.83)
        moon_field = np.sin(t * 4.84)
        human_field = np.sin(t * 12.67)
        combined_field = earth_field + moon_field + human_field
        adjusted_field = combined_field * PHI
        
        data['field_interactions'].append({
            'timestamp': float(t),
            'earth_field': float(earth_field),
            'moon_field': float(moon_field),
            'human_field': float(human_field),
            'combined_field': float(combined_field),
            'adjusted_field': float(adjusted_field)
        })
    
    # Save data to file
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Sample simulation data saved to {output_path}")
    return data


def main():
    """Main function to run the visualization"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Visualize quantum fields from simulation data")
    parser.add_argument("--data", type=str, default="simulation_data.json",
                       help="Path to simulation data JSON file")
    parser.add_argument("--generate", action="store_true",
                       help="Generate sample simulation data")
    parser.add_argument("--output-dir", type=str, default=".",
                       help="Directory to save output plots")
    parser.add_argument("--plot-type", type=str, choices=["all", "quantum", "phi", "phase", "field"],
                       default="all", help="Type of plot to generate")
    
    args = parser.parse_args()
    
    # Generate sample data if requested
    if args.generate:
        data = generate_simulation_data(args.data)
    else:
        # Load simulation data
        try:
            data = load_simulation_data(args.data)
        except FileNotFoundError:
            print(f"Simulation data file not found: {args.data}")
            print("Generating sample data instead...")
            data = generate_simulation_data(args.data)
    
    # Create output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Generate plots based on plot type
    if args.plot_type in ["all", "quantum"]:
        output_path = os.path.join(args.output_dir, "quantum_states.png")
        plot_quantum_states(data, output_path)
    
    if args.plot_type in ["all", "phi"]:
        output_path = os.path.join(args.output_dir, "phi_harmonics.png")
        plot_phi_harmonic_relationships(data, output_path)
    
    if args.plot_type in ["all", "phase"]:
        output_path = os.path.join(args.output_dir, "phase_space.png")
        plot_phase_space(data, output_path)
    
    if args.plot_type in ["all", "field"]:
        output_path = os.path.join(args.output_dir, "field_interactions.png")
        plot_field_interactions(data, output_path)
    
    print("Visualization complete!")


if __name__ == "__main__":
    main()
