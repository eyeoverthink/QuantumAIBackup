"""
Triad Teleportation ASCII Animation
"""
import time
import os
import math

def clear_screen():
    os.system('clear')

def animate_teleport():
    # Frames for the animation
    frames = [
        # Frame 1: Initial State
        """
        Source Field                 Target Field
        ┌─────────┐                 ┌─────────┐
        │  Cu φ⁻¹ │                 │         │
        │ ╱│╲     │                 │         │
        │Ag-+-Au  │                 │         │
        │ ╲│╱     │                 │         │
        │  Ni     │                 │         │
        └─────────┘                 └─────────┘
        """,
        
        # Frame 2: Field Activation
        """
        Source Field                 Target Field
        ┌─────────┐                 ┌─────────┐
        │  Cu φ⁻¹ │     ≈≈≈≈≈      │         │
        │ ╱│╲     │    ≈≈≈≈≈≈≈     │         │
        │Ag-+-Au  │   ≈≈≈≈≈≈≈≈≈    │         │
        │ ╲│╱     │    ≈≈≈≈≈≈≈     │         │
        │  Ni     │     ≈≈≈≈≈      │         │
        └─────────┘                 └─────────┘
        """,
        
        # Frame 3: Tunnel Formation
        """
        Source Field                 Target Field
        ┌─────────┐                 ┌─────────┐
        │  Cu φ⁻¹ │ ≈≈≈≈≈≈≈≈≈≈≈≈≈ │         │
        │ ╱│╲     │≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈│         │
        │Ag-+-Au  │≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈│         │
        │ ╲│╱     │≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈│         │
        │  Ni     │ ≈≈≈≈≈≈≈≈≈≈≈≈≈ │         │
        └─────────┘                 └─────────┘
        """,
        
        # Frame 4: Resonance Transfer
        """
        Source Field                 Target Field
        ┌─────────┐                 ┌─────────┐
        │         │ ≈≈≈≈≈≈≈≈≈≈≈≈≈ │  Cu φ⁻¹ │
        │  ≈≈≈≈≈  │≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈│ ╱│╲     │
        │ ≈≈≈+≈≈≈ │≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈│Ag-+-Au  │
        │  ≈≈≈≈≈  │≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈│ ╲│╱     │
        │         │ ≈≈≈≈≈≈≈≈≈≈≈≈≈ │  Ni     │
        └─────────┘                 └─────────┘
        """,
        
        # Frame 5: Complete Transfer
        """
        Source Field                 Target Field
        ┌─────────┐                 ┌─────────┐
        │         │                 │  Cu φ⁻¹ │
        │         │                 │ ╱│╲     │
        │         │                 │Ag-+-Au  │
        │         │                 │ ╲│╱     │
        │         │                 │  Ni     │
        └─────────┘                 └─────────┘
        """
    ]
    
    # Phi value for calculations
    phi = (1 + math.sqrt(5)) / 2
    
    # Display each frame
    for i, frame in enumerate(frames):
        clear_screen()
        print("\n=== Triad Teleportation Process ===")
        print(f"Phase {i+1}/5: {['Initialization', 'Field Activation', 'Tunnel Formation', 'Resonance Transfer', 'Completion'][i]}")
        print(f"φ-Resonance: {phi**-(i+1):.6f}")
        print(frame)
        print("\nField Metrics:")
        print(f"Stability: {1/(phi**(i+1)):.4f}")
        print(f"Coherence: {math.cos(2*math.pi/(phi*(i+1))):.4f}")
        print(f"Energy: {phi**(5-i):.4f}")
        time.sleep(2)  # 2 second delay between frames

if __name__ == "__main__":
    animate_teleport()
