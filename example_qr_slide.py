#!/usr/bin/env python3
"""
Example QR Slide - Phi-Harmonic Visualization
This file demonstrates a simple visualization using phi-harmonic principles
that can be encoded as a QR code and executed in presentation mode.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

# Phi (Golden Ratio) constant
PHI = (1 + np.sqrt(5)) / 2  # Approximately 1.618034

def phi_harmonic_pattern(t, complexity=3):
    """Generate a phi-harmonic pattern based on time and complexity."""
    x = np.linspace(0, 2*np.pi, 1000)
    
    # Create phi-harmonic waves with increasing frequencies
    waves = []
    for i in range(1, complexity + 1):
        # Use powers of phi for frequencies
        freq = PHI ** i
        # Use phi-based phase shifts
        phase = (PHI * i * t) % (2*np.pi)
        # Generate the wave
        wave = np.sin(freq * x + phase) / i
        waves.append(wave)
    
    # Combine waves
    combined = np.zeros_like(x)
    for wave in waves:
        combined += wave
    
    return x, combined

def main():
    """Main function to display phi-harmonic visualization."""
    print("Executing Phi-Harmonic Visualization from QR code")
    print(f"Golden Ratio (φ): {PHI}")
    
    # Calculate phi-harmonic time
    current_time = time.time()
    phi_time = (current_time * PHI) % 1.0
    resonance = 1.0 / (1.0 + abs(phi_time - 0.5))
    
    print(f"Current phi-time: {phi_time:.6f}")
    print(f"Resonance: {resonance:.6f}")
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title(f"Phi-Harmonic Visualization (φ={PHI:.6f})")
    ax.set_xlabel("Phase")
    ax.set_ylabel("Amplitude")
    
    # Initial complexity based on resonance
    complexity = int(3 + 4 * resonance)
    print(f"Pattern complexity: {complexity}")
    
    # Generate initial pattern
    x, y = phi_harmonic_pattern(phi_time, complexity)
    line, = ax.plot(x, y, lw=2)
    
    # Set axis limits
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-2, 2)
    
    # Add phi-harmonic grid lines
    for i in range(1, 6):
        pos = (2*np.pi) * (1 - 1/PHI**i)
        ax.axvline(x=pos, color='gold', alpha=0.3, linestyle='--')
    
    # Add text annotations
    ax.text(0.02, 0.95, f"φ-time: {phi_time:.6f}", transform=ax.transAxes)
    ax.text(0.02, 0.90, f"Resonance: {resonance:.6f}", transform=ax.transAxes)
    ax.text(0.02, 0.85, f"Complexity: {complexity}", transform=ax.transAxes)
    
    # Animation update function
    def update(frame):
        t = phi_time + frame / 50
        x, y = phi_harmonic_pattern(t, complexity)
        line.set_data(x, y)
        return line,
    
    # Create animation
    ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)
    
    # Show plot
    plt.show()

if __name__ == "__main__":
    main()
