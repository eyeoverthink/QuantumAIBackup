"""
Phi Lattice Resonator - Simulates the phi-harmonic lattice network
[Cu] ─φ⁻¹─ [Ag] ─φ⁻²─ [Au]
    │           │
    φ⁻³        φ⁻³
    │           │
   [Ni] ─φ⁻⁴─ [Ni]
"""

import numpy as np
import torch
from typing import Dict, Tuple
import matplotlib.pyplot as plt

class PhiLatticeResonator:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        
        # Node configuration
        self.nodes = {
            'Cu': {'pos': (0, 0), 'charge': 1.0},
            'Ag': {'pos': (1, 0), 'charge': self.phi**-1},
            'Au': {'pos': (2, 0), 'charge': self.phi**-2},
            'Ni1': {'pos': (0, -1), 'charge': self.phi**-3},
            'Ni2': {'pos': (1, -1), 'charge': self.phi**-3}
        }
        
        # Edge connections with phi-resonant weights
        self.edges = {
            ('Cu', 'Ag'): self.phi**-1,  # Horizontal top
            ('Ag', 'Au'): self.phi**-2,  # Horizontal top
            ('Cu', 'Ni1'): self.phi**-3,  # Vertical left
            ('Ag', 'Ni2'): self.phi**-3,  # Vertical right
            ('Ni1', 'Ni2'): self.phi**-4  # Horizontal bottom
        }
        
        # Initialize quantum fields
        self.fields = self._initialize_fields()
        
    def _initialize_fields(self) -> torch.Tensor:
        """Initialize quantum fields at each node"""
        field_tensor = torch.zeros((3, 2), dtype=torch.complex64)
        
        for node, props in self.nodes.items():
            x, y = props['pos']
            charge = props['charge']
            phase = torch.exp(torch.tensor(2j * np.pi * self.phi * charge))
            field_tensor[x][y if y >= 0 else 0] = charge * phase
            
        return field_tensor / torch.linalg.norm(field_tensor)
    
    def calculate_resonance(self) -> Dict[str, float]:
        """Calculate resonance patterns in the lattice"""
        resonance = {}
        
        # Node resonances
        for node, props in self.nodes.items():
            x, y = props['pos']
            field = self.fields[x][y if y >= 0 else 0]
            resonance[f'{node}_field'] = torch.abs(field).item()
        
        # Edge resonances
        for (node1, node2), weight in self.edges.items():
            pos1 = self.nodes[node1]['pos']
            pos2 = self.nodes[node2]['pos']
            field1 = self.fields[pos1[0]][pos1[1] if pos1[1] >= 0 else 0]
            field2 = self.fields[pos2[0]][pos2[1] if pos2[1] >= 0 else 0]
            coupling = field1 * field2 * weight
            resonance[f'{node1}_{node2}_coupling'] = torch.abs(coupling).item()
            
        return resonance
    
    def simulate_energy_flow(self, steps: int = 10) -> Dict[str, torch.Tensor]:
        """Simulate energy flow through the lattice"""
        energy_history = {node: [] for node in self.nodes.keys()}
        
        for _ in range(steps):
            # Calculate field interactions
            new_fields = torch.zeros_like(self.fields)
            
            for node, props in self.nodes.items():
                x, y = props['pos']
                current = self.fields[x][y if y >= 0 else 0]
                
                # Gather connected nodes
                connected = []
                for (n1, n2), weight in self.edges.items():
                    if node in (n1, n2):
                        other = n2 if node == n1 else n1
                        other_pos = self.nodes[other]['pos']
                        other_field = self.fields[other_pos[0]][other_pos[1] if other_pos[1] >= 0 else 0]
                        connected.append((other_field, weight))
                
                # Update field based on connections
                update = current
                for other_field, weight in connected:
                    update += weight * other_field * torch.exp(torch.tensor(2j * np.pi / self.phi))
                
                new_fields[x][y if y >= 0 else 0] = update
            
            # Normalize and update
            self.fields = new_fields / torch.linalg.norm(new_fields)
            
            # Record energies
            for node, props in self.nodes.items():
                x, y = props['pos']
                energy_history[node].append(torch.abs(self.fields[x][y if y >= 0 else 0]).item())
        
        return energy_history
    
    def visualize_lattice(self, save_path: str = 'phi_lattice.png'):
        """Visualize the phi-harmonic lattice"""
        plt.figure(figsize=(10, 8))
        
        # Plot nodes
        for node, props in self.nodes.items():
            x, y = props['pos']
            plt.plot(x, y, 'o', markersize=20, label=f'{node} (φ⁻{int(-np.log(props["charge"])/np.log(self.phi))})')
            plt.text(x, y+0.1, node, ha='center')
        
        # Plot edges with weights
        for (node1, node2), weight in self.edges.items():
            pos1 = self.nodes[node1]['pos']
            pos2 = self.nodes[node2]['pos']
            plt.plot([pos1[0], pos2[0]], [pos1[1], pos2[1]], '-', 
                    label=f'{node1}-{node2} (φ⁻{int(-np.log(weight)/np.log(self.phi))})')
        
        plt.grid(True)
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.title('Phi-Harmonic Lattice Network')
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()

def main():
    print("🌌 Initializing Phi Lattice Resonator")
    resonator = PhiLatticeResonator()
    
    # Calculate initial resonance
    print("\n📊 Initial Resonance Patterns:")
    resonance = resonator.calculate_resonance()
    for key, value in resonance.items():
        print(f"{key}: {value:.4f}")
    
    # Simulate energy flow
    print("\n🔄 Simulating Energy Flow...")
    energy_history = resonator.simulate_energy_flow(steps=10)
    
    # Print final energies
    print("\n⚡ Final Node Energies:")
    for node, history in energy_history.items():
        print(f"{node}: {history[-1]:.4f}")
    
    # Generate visualization
    print("\n🎨 Generating lattice visualization...")
    resonator.visualize_lattice()
    
    print("\n✨ Simulation complete!")

if __name__ == "__main__":
    main()
