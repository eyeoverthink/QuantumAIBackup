import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define PHI directly instead of importing
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio (phi)

# Constants
G = 6.67430e-11  # Gravitational constant
c = 299792458    # Speed of light

# Test different quantum signatures
signatures = [
    {
        'name': 'Original',
        'tau': 1.313,      # Temporal component
        'psi0': 1.549,     # Primary component
        'psi1': 1.034,     # Secondary component
        'm': 1.000,        # Mass component
        'resonance': 1.465197  # Truth resonance
    },
    {
        'name': 'High Temporal',
        'tau': 1.618,      # Higher temporal component
        'psi0': 1.549,     # Same primary component
        'psi1': 1.034,     # Same secondary component
        'm': 1.000,        # Same mass component
        'resonance': 1.5   # Adjusted resonance
    },
    {
        'name': 'High Outflow',
        'tau': 1.313,      # Same temporal component
        'psi0': 1.889,     # Higher primary component
        'psi1': 1.034,     # Same secondary component
        'm': 1.000,        # Same mass component
        'resonance': 1.5   # Adjusted resonance
    }
]

def analyze_white_hole(sig):
    """Analyze the white hole quantum signature"""
    print(f"\n===== WHITE HOLE QUANTUM ANALYSIS: {sig['name']} =====")
    print(f"Temporal (τ): φ^{sig['tau']:.3f}")
    print(f"Primary (ψ₀): φ^{sig['psi0']:.3f}")
    print(f"Secondary (ψ₁): φ^{sig['psi1']:.3f}")
    print(f"Mass (M): φ^{sig['m']:.3f}")
    print(f"Truth Resonance: {sig['resonance']:.6f}")
    
    # Calculate white hole characteristics
    temporal_factor = PHI ** sig['tau']
    outflow_factor = PHI ** sig['psi0']
    quantum_factor = PHI ** sig['psi1']
    
    print("\n===== WHITE HOLE CHARACTERISTICS =====")
    print(f"Time Reversal Factor: {temporal_factor:.3f}")
    print(f"Matter Outflow Rate: {outflow_factor:.3f}")
    print(f"Quantum Tunneling Strength: {quantum_factor:.3f}")
    
    return temporal_factor, outflow_factor, quantum_factor

def visualize_white_hole(sig, save_path=None):
    """Create 3D visualization of white hole spacetime"""
    # Calculate key factors
    temporal_factor, outflow_factor, quantum_factor = analyze_white_hole(sig)
    
    # Create a grid of points
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    
    # Create figure and 3D axis
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Calculate parameters from quantum signature
    temporal = sig['tau']
    outflow = sig['psi0']
    quantum = sig['psi1']
    
    # Calculate distance from origin
    R = np.sqrt(X**2 + Y**2)
    
    # Calculate white hole spacetime
    with np.errstate(divide='ignore', invalid='ignore'):
        # Inverted black hole metric for white hole
        Z = outflow * np.exp(-R/temporal) * (1 + np.sin(R*quantum))
        
        # Add quantum fluctuations
        quantum_noise = np.random.normal(0, 0.1, Z.shape) * quantum
        Z += quantum_noise
    
    # Fix infinite values
    Z[np.isinf(Z)] = np.nan
    Z[np.isnan(Z)] = np.nanmax(Z)
    
    # Create the surface with custom colormap
    surf = ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.8)
    
    # Add outflow particles
    if outflow > 1.4:  # Strong outflow
        num_particles = int(outflow * 200)
        heights = np.linspace(0, np.max(Z), num_particles)
        for h in heights:
            angle = np.random.uniform(0, 2*np.pi)
            r = np.random.uniform(0, 3)
            x = r * np.cos(angle)
            y = r * np.sin(angle)
            size = np.random.uniform(10, 30)
            ax.scatter(x, y, h, c='white', s=size, alpha=0.6)
    
    # Add quantum tunneling effects
    if quantum > 1.0:
        for _ in range(20):
            angle = np.linspace(0, 2*np.pi, 50)
            r = np.random.uniform(1, 4)
            x = r * np.cos(angle)
            y = r * np.sin(angle)
            z = np.random.uniform(0, np.max(Z)) * np.ones_like(angle)
            ax.plot(x, y, z, 'cyan', alpha=0.3)
    
    # Add outflow streams
    theta = np.linspace(0, 2*np.pi, 16)
    for t in theta:
        r = np.linspace(0, 5, 100)
        x = r * np.cos(t)
        y = r * np.sin(t)
        z = outflow * np.exp(-r/temporal) * 2
        ax.plot(x, y, z, 'yellow', alpha=0.4)
    
    # Customize the visualization
    ax.set_title(f'White Hole Quantum Analysis: {sig["name"]}', color='white', pad=20)
    ax.set_facecolor('black')
    fig.patch.set_facecolor('black')
    
    # Add quantum signature text
    signature_text = f"Quantum Signature:\n⟨τ|φ^{sig['tau']}⟩ ⊗ ⟨ψ₀|φ^{sig['psi0']}⟩ ⊗ ⟨ψ₁|φ^{sig['psi1']}⟩ ⊗ ⟨M|φ⟩"
    plt.figtext(0.02, 0.02, signature_text, color='white', fontsize=10)
    
    # Add resonance indicator
    resonance_color = 'yellow' if sig['resonance'] > 1.4 else 'red'
    plt.figtext(0.02, 0.15, f"Resonance: {sig['resonance']:.6f}", 
                color=resonance_color, fontsize=10)
    
    # Save or show the plot
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
        plt.close()
        print(f"Saved visualization to {save_path}")
    else:
        plt.show()

def main():
    print("\n🌟 WHITE HOLE QUANTUM ANALYZER - EXPERIMENT 🌟")
    print("=" * 50)
    
    # Test different signatures
    for i, sig in enumerate(signatures):
        print(f"\nTesting Signature {i+1}: {sig['name']}")
        
        # Create output directory if it doesn't exist
        import os
        os.makedirs("white_hole_results", exist_ok=True)
        
        # Generate visualization and save
        save_path = f"white_hole_results/white_hole_{sig['name'].lower().replace(' ', '_')}.png"
        visualize_white_hole(sig, save_path)
        
        # Provide interpretation
        print("\n===== INTERPRETATION =====")
        if sig['resonance'] > 1.4:
            print("✨ STRONG WHITE HOLE SIGNATURE DETECTED!")
            print(f"Temporal component (τ): {sig['tau']:.3f}")
            print(f"Outflow potential (ψ₀): {sig['psi0']:.3f}")
            print(f"Quantum tunneling (ψ₁): {sig['psi1']:.3f}")
        else:
            print("⚠️ Moderate white hole characteristics")
            print("Configuration may be unstable or transitioning.")
    
    print("\n✅ Experiment complete! Check the white_hole_results folder.")

if __name__ == "__main__":
    main()
