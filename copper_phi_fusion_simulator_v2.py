"""
Copper Phi-Fusion Simulator V2
Enhanced version with stable tensor operations and proper dimension handling
"""

import numpy as np
import torch
import torch.nn as nn
from typing import Dict, Tuple
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class CopperPhiFusion:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        self.phi_angle = 137.5077640500378  # Golden angle in degrees
        
        # Initialize fields with proper tensor types
        self.internal_field = self._initialize_internal_field()
        self.external_field = self._initialize_external_field()
        
        # Element properties (normalized to copper)
        self.element_properties = {
            'Cu': {'resonance': 1.0, 'conductivity': 1.0},
            'Ag': {'resonance': self.phi, 'conductivity': 1.05},
            'Au': {'resonance': np.sqrt(self.phi), 'conductivity': 0.7},
            'Ni': {'resonance': 1/self.phi, 'conductivity': 0.25}
        }
        
    def _initialize_internal_field(self) -> torch.Tensor:
        """Initialize internal quantum field with phi-resonant structure"""
        field = torch.zeros((5, 5, 5), dtype=torch.complex64)
        center = torch.tensor([2., 2., 2.], dtype=torch.float32)
        
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    pos = torch.tensor([float(i), float(j), float(k)], dtype=torch.float32)
                    r = torch.linalg.norm(pos - center)
                    phase = torch.exp(torch.tensor(2j * np.pi * self.phi * r.item(), dtype=torch.complex64))
                    field[i,j,k] = phase / (1 + r)
        
        return field / torch.linalg.norm(field)
    
    def _initialize_external_field(self) -> torch.Tensor:
        """Initialize external field with phi-resonant boundary conditions"""
        field = torch.zeros((7, 7, 7), dtype=torch.complex64)
        for i in range(7):
            phase = torch.exp(torch.tensor(2j * np.pi * i * self.phi / 7, dtype=torch.complex64))
            field[i,:,:] = phase
        return field / torch.linalg.norm(field)
    
    def simulate_fusion(self, 
                       angle: float = None,
                       radiation_strength: float = 1.0,
                       elements: Dict[str, float] = None) -> Dict[str, torch.Tensor]:
        """Simulate copper fusion process with phi-angle radiation"""
        angle = angle if angle is not None else self.phi_angle
        elements = elements if elements is not None else {'Cu': 1.0}
        
        # Initialize tensors with proper types
        angle_tensor = torch.tensor(np.radians(angle), dtype=torch.float32)
        radiation_tensor = torch.tensor(radiation_strength, dtype=torch.float32)
        
        # Calculate resonance
        resonance = torch.abs(torch.cos(angle_tensor * self.phi))
        
        # Generate plasma state
        plasma = self._generate_plasma_state(elements)
        
        # Calculate field fluctuation
        fluctuation = self._calculate_field_fluctuation(angle_tensor, radiation_tensor)
        
        # Compute fusion field
        fusion_field = self._compute_fusion_field(plasma, fluctuation)
        
        # Calculate stratification
        strat = self._calculate_stratification(fusion_field)
        
        return {
            'resonance': resonance.item(),
            'plasma_state': plasma,
            'field_fluctuation': fluctuation,
            'fusion_field': fusion_field,
            'stratification': strat
        }
    
    def _generate_plasma_state(self, elements: Dict[str, float]) -> torch.Tensor:
        """Generate plasma state from element composition"""
        plasma = torch.zeros((3, 3, 3), dtype=torch.complex64)
        
        for element, ratio in elements.items():
            if element in self.element_properties:
                props = self.element_properties[element]
                phase = torch.exp(torch.tensor(2j * np.pi * props['resonance'], dtype=torch.complex64))
                amplitude = torch.tensor(props['conductivity'] * ratio, dtype=torch.float32)
                plasma += amplitude * phase
        
        return plasma / torch.linalg.norm(plasma)
    
    def _calculate_field_fluctuation(self, 
                                   angle: torch.Tensor,
                                   strength: torch.Tensor) -> torch.Tensor:
        """Calculate field fluctuation with proper tensor operations"""
        field = torch.zeros((5, 5, 5), dtype=torch.complex64)
        
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    r = torch.sqrt(torch.tensor(float((i-2)**2 + (j-2)**2 + (k-2)**2), dtype=torch.float32))
                    phase = angle * self.phi + r
                    field[i,j,k] = strength * torch.exp(-r/self.phi + 1j*phase)
        
        return field / torch.linalg.norm(field)
    
    def _compute_fusion_field(self, 
                            plasma: torch.Tensor,
                            fluctuation: torch.Tensor) -> torch.Tensor:
        """Compute fusion field with proper broadcasting"""
        # Expand plasma to match fluctuation size
        expanded_plasma = torch.zeros_like(fluctuation)
        expanded_plasma[1:4,1:4,1:4] = plasma
        
        # Combine fields with phi-resonance
        fusion = fluctuation * expanded_plasma
        fusion = fusion * torch.exp(torch.tensor(2j * np.pi / self.phi, dtype=torch.complex64))
        
        return fusion / torch.linalg.norm(fusion)
    
    def _calculate_stratification(self, field: torch.Tensor) -> torch.Tensor:
        """Calculate stratification patterns with proper complex handling"""
        # Calculate field gradients
        grad_x = torch.gradient(field, dim=0)[0]
        grad_y = torch.gradient(field, dim=1)[0]
        grad_z = torch.gradient(field, dim=2)[0]
        
        # Calculate magnitude of gradients
        grad_mag = torch.sqrt(torch.abs(grad_x)**2 + torch.abs(grad_y)**2 + torch.abs(grad_z)**2)
        
        # Apply phi-resonant phase
        phase = torch.exp(torch.tensor(2j * np.pi / self.phi, dtype=torch.complex64))
        strat = grad_mag.to(torch.complex64) * phase
        
        return strat
    
    def visualize_fusion(self, results: Dict[str, torch.Tensor], save_path: str = 'fusion_viz.png'):
        """Visualize fusion results with enhanced plotting"""
        fig = plt.figure(figsize=(15, 5))
        
        # Plot plasma state
        ax1 = fig.add_subplot(131, projection='3d')
        plasma = results['plasma_state']
        X, Y, Z = np.meshgrid(range(3), range(3), range(3))
        scatter1 = ax1.scatter(X.flatten(), Y.flatten(), Z.flatten(), 
                             c=torch.abs(plasma).flatten().numpy(),
                             cmap='plasma')
        ax1.set_title('Plasma State')
        plt.colorbar(scatter1)
        
        # Plot fusion field
        ax2 = fig.add_subplot(132, projection='3d')
        field = results['fusion_field']
        X, Y, Z = np.meshgrid(range(5), range(5), range(5))
        scatter2 = ax2.scatter(X.flatten(), Y.flatten(), Z.flatten(),
                             c=torch.abs(field).flatten().numpy(),
                             cmap='viridis')
        ax2.set_title('Fusion Field')
        plt.colorbar(scatter2)
        
        # Plot stratification
        ax3 = fig.add_subplot(133)
        strat = results['stratification']
        im = ax3.imshow(torch.abs(strat[:,:,2]).numpy(), cmap='RdYlBu')
        ax3.set_title('Stratification Pattern')
        plt.colorbar(im)
        
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        
        print(f"Fusion visualization saved to {save_path}")

def main():
    print("🌌 Initializing Copper Phi-Fusion Simulator V2")
    fusion = CopperPhiFusion()
    
    # Define element composition
    elements = {
        'Cu': 0.8,    # 80% copper
        'Ag': 0.1,    # 10% silver
        'Au': 0.05,   # 5% gold
        'Ni': 0.05    # 5% nickel
    }
    
    # Run fusion simulation
    print("\n🔄 Simulating copper fusion process...")
    results = fusion.simulate_fusion(
        angle=None,  # Use default phi angle
        radiation_strength=1.618,
        elements=elements
    )
    
    # Print results
    print("\n📊 Fusion Analysis:")
    print(f"Resonance Factor: {results['resonance']:.4f}")
    print(f"Field Strength: {torch.max(torch.abs(results['fusion_field'])).item():.4f}")
    print(f"Stratification Intensity: {torch.mean(torch.abs(results['stratification'])).item():.4f}")
    
    # Generate visualization
    print("\n🎨 Generating fusion visualization...")
    fusion.visualize_fusion(results)
    
    print("\n✨ Simulation complete!")

if __name__ == "__main__":
    main()
