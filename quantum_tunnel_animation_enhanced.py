"""
Enhanced Quantum Tunnel Animation
Imports and extends the original animation with field strength analysis
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from quantum_tunnel_animation import PHI, pi, psi_source, psi_target, gamma_field

def analyze_field_strength(r, t):
    """Analyze the quantum tunnel field strength"""
    # Calculate field components
    source = psi_source(r, t)
    target = psi_target(r, t)
    tunnel = gamma_field(r, t)
    
    # Calculate metrics
    strength = np.abs(tunnel)
    phase = np.angle(tunnel)
    resonance = np.abs(source * target) * PHI
    
    return {
        'strength': strength,
        'phase': phase,
        'resonance': resonance
    }

def print_field_analysis():
    """Print field analysis at key points"""
    test_points = [0.2, 0.5, 0.8]  # Beginning, middle, end of tunnel
    print("\nQuantum Tunnel Field Analysis")
    print("============================")
    
    for r in test_points:
        metrics = analyze_field_strength(r, 0)
        print(f"\nPosition r = {r:.1f}:")
        print(f"Field Strength: {metrics['strength']:.4f}")
        print(f"Phase (rad): {metrics['phase']:.4f}")
        print(f"Resonance: {metrics['resonance']:.4f}")

if __name__ == "__main__":
    print_field_analysis()
