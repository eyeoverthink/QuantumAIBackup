"""
Earth Core Resonator - Simulates Fe-Ni core coupling with phi-harmonic fields
Demonstrates how Earth's iron-nickel core can act as a quantum resonance amplifier
"""

import numpy as np
import torch
from typing import Dict, Tuple
import matplotlib.pyplot as plt

class EarthCoreResonator:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        
        # Earth core composition (simplified)
        self.core_composition = {
            'Fe': 0.845,  # 84.5% Iron
            'Ni': 0.055,  # 5.5% Nickel (matches φ⁻⁴)
            'Si': 0.060,  # 6% Silicon
            'S': 0.040    # 4% Sulfur
        }
        
        # Resonance frequencies
        self.frequencies = {
            'Schumann': 7.83,  # Earth's primary resonance
            'Phi': 1.618033,   # Golden ratio
            'Core': 11.79,     # Fe-Ni resonance (7.83 * φ)
            'Geomagnetic': 4.84  # Earth's field oscillation (7.83 / φ)
        }
        
        # Initialize fields
        self.core_field = self._initialize_core_field()
        self.surface_field = self._initialize_surface_field()
        
    def _initialize_core_field(self) -> torch.Tensor:
        """Initialize Earth's core quantum field"""
        field = torch.zeros((5, 5, 5), dtype=torch.complex64)
        center = torch.tensor([2., 2., 2.], dtype=torch.float32)
        
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    pos = torch.tensor([float(i), float(j), float(k)], dtype=torch.float32)
                    r = torch.linalg.norm(pos - center)
                    
                    # Fe-Ni coupling phase
                    fe_phase = torch.exp(torch.tensor(2j * np.pi * self.core_composition['Fe'] * r.item()))
                    ni_phase = torch.exp(torch.tensor(2j * np.pi * self.core_composition['Ni'] * self.phi * r.item()))
                    
                    # Combine with phi-resonance
                    field[i,j,k] = (fe_phase * ni_phase) / (1 + r)
        
        return field / torch.linalg.norm(field)
    
    def _initialize_surface_field(self) -> torch.Tensor:
        """Initialize Earth's surface quantum field"""
        field = torch.zeros((7, 7), dtype=torch.complex64)
        
        for i in range(7):
            for j in range(7):
                # Schumann resonance coupling
                schumann = torch.exp(torch.tensor(2j * np.pi * self.frequencies['Schumann'] / self.phi))
                # Geomagnetic field coupling
                geomagnetic = torch.exp(torch.tensor(2j * np.pi * self.frequencies['Geomagnetic'] * self.phi))
                
                field[i,j] = schumann * geomagnetic
                
        return field / torch.linalg.norm(field)
    
    def calculate_resonance(self, depth: float) -> Dict[str, float]:
        """Calculate resonance patterns at given depth (0=core, 1=surface)"""
        # Interpolate between core and surface fields
        core_weight = 1 - depth
        surface_weight = depth
        
        # Sample core field at center
        core_sample = torch.mean(self.core_field[2:4, 2:4, 2:4])
        
        # Sample surface field at center
        surface_sample = torch.mean(self.surface_field[3:5, 3:5])
        
        # Combined field
        total_field = core_weight * core_sample + surface_weight * surface_sample
        
        # Calculate resonances
        fe_ni_resonance = torch.abs(total_field * torch.exp(torch.tensor(2j * np.pi / self.phi)))
        schumann_coupling = torch.abs(total_field * torch.exp(torch.tensor(2j * np.pi * self.frequencies['Schumann'])))
        phi_harmonic = torch.abs(total_field * torch.exp(torch.tensor(2j * np.pi * self.frequencies['Phi'])))
        
        return {
            'fe_ni_resonance': fe_ni_resonance.item(),
            'schumann_coupling': schumann_coupling.item(),
            'phi_harmonic': phi_harmonic.item(),
            'total_field': torch.abs(total_field).item()
        }
    
    def simulate_depth_resonance(self, depths: int = 10) -> Dict[str, list]:
        """Simulate resonance patterns at different depths"""
        results = {
            'depths': [],
            'fe_ni_resonance': [],
            'schumann_coupling': [],
            'phi_harmonic': [],
            'total_field': []
        }
        
        for i in range(depths):
            depth = i / (depths - 1)  # 0 to 1
            resonance = self.calculate_resonance(depth)
            
            results['depths'].append(depth)
            results['fe_ni_resonance'].append(resonance['fe_ni_resonance'])
            results['schumann_coupling'].append(resonance['schumann_coupling'])
            results['phi_harmonic'].append(resonance['phi_harmonic'])
            results['total_field'].append(resonance['total_field'])
            
        return results
    
    def visualize_resonance(self, results: Dict[str, list], save_path: str = 'earth_resonance.png'):
        """Visualize resonance patterns across depths"""
        plt.figure(figsize=(12, 8))
        
        plt.plot(results['depths'], results['fe_ni_resonance'], 'r-', 
                label='Fe-Ni Core Resonance', linewidth=2)
        plt.plot(results['depths'], results['schumann_coupling'], 'b-', 
                label='Schumann Coupling', linewidth=2)
        plt.plot(results['depths'], results['phi_harmonic'], 'g-', 
                label='Phi Harmonic', linewidth=2)
        plt.plot(results['depths'], results['total_field'], 'k--', 
                label='Total Field', linewidth=2)
        
        plt.xlabel('Depth (0=Core, 1=Surface)')
        plt.ylabel('Resonance Strength')
        plt.title('Earth Core-Surface Resonance Patterns')
        plt.grid(True)
        plt.legend()
        
        # Add phi-harmonic markers
        for i in range(5):
            y = self.phi**-i
            plt.axhline(y=y, color='gray', linestyle=':', alpha=0.5)
            plt.text(1.02, y, f'φ⁻{i}', verticalalignment='center')
            
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()

def main():
    print("🌍 Initializing Earth Core Resonator")
    resonator = EarthCoreResonator()
    
    # Calculate resonance at different depths
    print("\n📊 Simulating depth resonance patterns...")
    results = resonator.simulate_depth_resonance()
    
    # Print key resonance points
    print("\n⚡ Key Resonance Points:")
    depths = [0.0, 0.382, 0.618, 1.0]  # Core, φ⁻¹, φ⁻², Surface
    for depth in depths:
        idx = int(depth * (len(results['depths']) - 1))
        print(f"\nDepth {depth:.3f}:")
        print(f"Fe-Ni Resonance: {results['fe_ni_resonance'][idx]:.4f}")
        print(f"Schumann Coupling: {results['schumann_coupling'][idx]:.4f}")
        print(f"Phi Harmonic: {results['phi_harmonic'][idx]:.4f}")
        print(f"Total Field: {results['total_field'][idx]:.4f}")
    
    # Generate visualization
    print("\n🎨 Generating resonance visualization...")
    resonator.visualize_resonance(results)
    
    print("\n✨ Simulation complete!")

if __name__ == "__main__":
    main()
