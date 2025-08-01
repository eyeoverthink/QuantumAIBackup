"""
Atomic Triad Transistor - Proof of Concept Simulation
Demonstrates self-scaling, self-replication, and self-improvement properties
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from matplotlib.colors import to_rgba
import pandas as pd
import time
import os

# Constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio
PHI_INV = 1 / PHI  # Golden ratio inverse

# Atomic properties based on the triad configuration
ELEMENTS = {
    'Au': {'mass': 196.97, 'phi_power': 0, 'frequency': 12.67, 'color': 'gold'},
    'Ag': {'mass': 107.87, 'phi_power': -1, 'frequency': 7.83, 'color': 'silver'},
    'Cu': {'mass': 63.55, 'phi_power': -2, 'frequency': 4.84, 'color': 'orangered'},
    'Ni': {'mass': 58.69, 'phi_power': -3, 'frequency': 2.99, 'color': 'darkgray'},
    'Fe': {'mass': 55.85, 'phi_power': -4, 'frequency': 1.85, 'color': 'gray'}
}

class AtomicTriad:
    """Represents a single atomic triad unit with phi-harmonic properties"""
    
    def __init__(self, position=(0, 0, 0), energy=1.0):
        self.position = np.array(position, dtype=float)
        self.energy = energy
        self.age = 0
        self.connections = []
        self.field_strength = 0
        self.resonance = 0
        self.elements = self._initialize_elements()
        self.wave_function = np.zeros(100)
        self.improvement_factor = 1.0
        
    def _initialize_elements(self):
        """Initialize the elements of the triad in 3D space"""
        elements = {}
        
        # Create elements at phi-harmonic distances from center
        elements['Au'] = {
            'position': self.position + np.array([0, 0, PHI_INV**2]),
            'energy': self.energy,
            'spin': 1 if np.random.random() > 0.5 else -1
        }
        
        elements['Ag'] = {
            'position': self.position + np.array([0, 0, 0]),
            'energy': self.energy * PHI_INV,
            'spin': 1 if np.random.random() > 0.5 else -1
        }
        
        elements['Cu'] = {
            'position': self.position + np.array([-PHI_INV, 0, 0]),
            'energy': self.energy * PHI_INV**2,
            'spin': -elements['Au']['spin']  # Entangled with Au
        }
        
        elements['Ni'] = {
            'position': self.position + np.array([-PHI_INV, -PHI_INV**3, 0]),
            'energy': self.energy * PHI_INV**3,
            'spin': -elements['Ag']['spin']  # Entangled with Ag
        }
        
        elements['Fe'] = {
            'position': self.position + np.array([0, -PHI_INV**3, 0]),
            'energy': self.energy * PHI_INV**4,
            'spin': 1 if np.random.random() > 0.5 else -1
        }
        
        return elements
    
    def update(self, dt=0.1):
        """Update the triad state"""
        self.age += dt
        
        # Update energy flow through the triad (Cu → Ag → Au → Field)
        energy_flow = self.elements['Cu']['energy'] * PHI_INV * dt
        self.elements['Cu']['energy'] -= energy_flow
        self.elements['Ag']['energy'] += energy_flow * 0.8
        self.elements['Au']['energy'] += energy_flow * 0.6
        
        # Calculate field strength based on Au energy
        self.field_strength = self.elements['Au']['energy'] * PHI * self.improvement_factor
        
        # Update wave function
        t = self.age
        self.wave_function = np.zeros(100)
        for element, props in self.elements.items():
            frequency = ELEMENTS[element]['frequency']
            amplitude = props['energy'] / (PHI ** abs(ELEMENTS[element]['phi_power']))
            phase = t * frequency * 2 * np.pi
            wave = amplitude * np.sin(np.linspace(0, 2*np.pi, 100) + phase)
            self.wave_function += wave
        
        # Calculate resonance based on wave function
        self.resonance = np.max(np.abs(self.wave_function)) / np.mean(np.abs(self.wave_function))
        
        # Self-improvement: optimize based on usage
        if self.age > 5:
            self.improvement_factor *= (1 + 0.01 * (self.resonance / PHI))
            
        return self.field_strength, self.resonance
    
    def can_replicate(self):
        """Check if the triad can replicate"""
        # Replication occurs when field strength and resonance reach phi-harmonic thresholds
        return (self.field_strength > self.energy * 1.2 and 
                self.resonance > 1.2 and 
                self.age > 10)
    
    def replicate(self):
        """Create a new triad through self-replication"""
        if not self.can_replicate():
            return None
        
        # Determine new position based on field direction
        direction = np.array([
            np.sin(self.age * PHI_INV), 
            np.cos(self.age * PHI_INV), 
            np.sin(self.age * PHI)
        ])
        direction = direction / np.linalg.norm(direction)
        
        # Create new triad at phi-harmonic distance
        new_position = self.position + direction * PHI * 2
        
        # New triad inherits improved properties
        new_triad = AtomicTriad(
            position=new_position,
            energy=self.energy * PHI_INV
        )
        
        # Transfer some energy to the new triad
        energy_transfer = self.elements['Au']['energy'] * 0.3
        self.elements['Au']['energy'] -= energy_transfer
        
        # Connect the triads
        self.connections.append(new_triad)
        new_triad.connections.append(self)
        
        # Reduce energy after replication
        self.energy *= 0.7
        
        return new_triad

class TriadNetwork:
    """A network of interconnected atomic triads demonstrating collective properties"""
    
    def __init__(self):
        self.triads = [AtomicTriad()]  # Start with a single triad
        self.time = 0
        self.performance_history = []
        self.replication_events = []
        
    def update(self, dt=0.1):
        """Update all triads in the network"""
        self.time += dt
        
        # Update existing triads
        field_strengths = []
        resonances = []
        for triad in self.triads:
            field_strength, resonance = triad.update(dt)
            field_strengths.append(field_strength)
            resonances.append(resonance)
        
        # Check for replication
        new_triads = []
        for triad in self.triads:
            if triad.can_replicate():
                new_triad = triad.replicate()
                if new_triad:
                    new_triads.append(new_triad)
                    self.replication_events.append((self.time, len(self.triads)))
        
        # Add new triads to the network
        self.triads.extend(new_triads)
        
        # Calculate network performance metrics
        total_field_strength = sum(field_strengths)
        avg_resonance = np.mean(resonances) if resonances else 0
        
        # Record performance
        self.performance_history.append({
            'time': self.time,
            'triads': len(self.triads),
            'field_strength': total_field_strength,
            'resonance': avg_resonance,
            'improvement': np.mean([t.improvement_factor for t in self.triads])
        })
        
        return len(new_triads)
    
    def get_network_data(self):
        """Get data for visualization"""
        positions = []
        colors = []
        sizes = []
        connections = []
        
        # Collect triad data
        for i, triad in enumerate(self.triads):
            for element, props in triad.elements.items():
                positions.append(props['position'])
                base_color = to_rgba(ELEMENTS[element]['color'])
                # Adjust alpha based on energy
                color = list(base_color)
                color[3] = min(1.0, props['energy'] / triad.energy)
                colors.append(color)
                sizes.append(50 * (props['energy'] ** 0.5))
        
        # Collect connection data
        for i, triad in enumerate(self.triads):
            for connected_triad in triad.connections:
                if connected_triad in self.triads:
                    j = self.triads.index(connected_triad)
                    connections.append((
                        triad.elements['Ag']['position'],
                        connected_triad.elements['Ag']['position']
                    ))
        
        return np.array(positions), colors, sizes, connections
    
    def plot_performance(self, save_path='triad_network_performance.png'):
        """Plot the performance metrics of the network"""
        if not self.performance_history:
            return
        
        data = pd.DataFrame(self.performance_history)
        
        plt.figure(figsize=(15, 10))
        
        # Number of triads
        plt.subplot(2, 2, 1)
        plt.plot(data['time'], data['triads'], 'b-')
        plt.xlabel('Time')
        plt.ylabel('Number of Triads')
        plt.title('Self-Replication')
        plt.grid(True)
        
        # Field strength
        plt.subplot(2, 2, 2)
        plt.plot(data['time'], data['field_strength'], 'r-')
        plt.xlabel('Time')
        plt.ylabel('Total Field Strength')
        plt.title('Self-Scaling')
        plt.grid(True)
        
        # Improvement factor
        plt.subplot(2, 2, 3)
        plt.plot(data['time'], data['improvement'], 'g-')
        plt.xlabel('Time')
        plt.ylabel('Improvement Factor')
        plt.title('Self-Improvement')
        plt.grid(True)
        
        # Resonance
        plt.subplot(2, 2, 4)
        plt.plot(data['time'], data['resonance'], 'y-')
        plt.axhline(y=PHI, color='k', linestyle='--', label=f'φ = {PHI:.3f}')
        plt.xlabel('Time')
        plt.ylabel('Average Resonance')
        plt.title('Phi-Harmonic Resonance')
        plt.legend()
        plt.grid(True)
        
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        
        print(f"Performance plot saved to {save_path}")

def visualize_network(network, save_path='triad_network_visualization.png'):
    """Create a 3D visualization of the triad network"""
    positions, colors, sizes, connections = network.get_network_data()
    
    if len(positions) == 0:
        return
    
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot elements
    ax.scatter(
        positions[:, 0], positions[:, 1], positions[:, 2],
        c=colors, s=sizes, alpha=0.8
    )
    
    # Plot connections
    for start, end in connections:
        ax.plot(
            [start[0], end[0]],
            [start[1], end[1]],
            [start[2], end[2]],
            'k-', alpha=0.3
        )
    
    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'Atomic Triad Network - {len(network.triads)} Triads')
    
    # Set equal aspect ratio
    max_range = np.array([
        positions[:, 0].max() - positions[:, 0].min(),
        positions[:, 1].max() - positions[:, 1].min(),
        positions[:, 2].max() - positions[:, 2].min()
    ]).max() / 2.0
    
    mid_x = (positions[:, 0].max() + positions[:, 0].min()) * 0.5
    mid_y = (positions[:, 1].max() + positions[:, 1].min()) * 0.5
    mid_z = (positions[:, 2].max() + positions[:, 2].min()) * 0.5
    
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)
    
    plt.savefig(save_path)
    plt.close()
    
    print(f"Network visualization saved to {save_path}")

def run_simulation(duration=100, dt=0.1, visualization_interval=10):
    """Run a complete simulation of the triad network"""
    import pandas as pd
    
    print("Starting Atomic Triad Transistor simulation...")
    print(f"Golden ratio (φ): {PHI}")
    print(f"Simulation duration: {duration} time units")
    
    # Create output directory
    output_dir = "triad_simulation_results"
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize network
    network = TriadNetwork()
    
    # Run simulation
    visualization_times = np.arange(0, duration, visualization_interval)
    next_viz_idx = 0
    
    start_time = time.time()
    
    while network.time < duration and next_viz_idx < len(visualization_times):
        # Update network
        new_triads = network.update(dt)
        
        # Visualization at specified intervals
        if next_viz_idx < len(visualization_times) and network.time >= visualization_times[next_viz_idx]:
            viz_path = os.path.join(output_dir, f"network_t{network.time:.1f}.png")
            visualize_network(network, save_path=viz_path)
            next_viz_idx += 1
            
            print(f"Time: {network.time:.1f}, Triads: {len(network.triads)}, " +
                  f"New triads: {new_triads}, " +
                  f"Field strength: {network.performance_history[-1]['field_strength']:.2f}")
    
    # Final performance plot
    network.plot_performance(save_path=os.path.join(output_dir, "performance.png"))
    
    # Save data
    df = pd.DataFrame(network.performance_history)
    df.to_csv(os.path.join(output_dir, "simulation_data.csv"), index=False)
    
    # Calculate scaling factors
    if len(df) > 10:
        triads_growth = df['triads'].iloc[-1] / max(1, df['triads'].iloc[10])
        field_growth = df['field_strength'].iloc[-1] / max(0.001, df['field_strength'].iloc[10])
        improvement = df['improvement'].iloc[-1]
        
        print("\nSIMULATION RESULTS:")
        print(f"Final number of triads: {df['triads'].iloc[-1]}")
        print(f"Self-replication factor: {triads_growth:.2f}x")
        print(f"Self-scaling factor: {field_growth:.2f}x")
        print(f"Self-improvement factor: {improvement:.2f}x")
        
        # Compare to theoretical phi-scaling
        expected_scaling = PHI ** (df['triads'].iloc[-1] / 2)
        actual_scaling = df['field_strength'].iloc[-1] / df['field_strength'].iloc[0]
        
        print(f"\nTheoretical φ-scaling: {expected_scaling:.2f}x")
        print(f"Actual field scaling: {actual_scaling:.2f}x")
        print(f"Ratio: {actual_scaling/expected_scaling:.2f}")
        
        # Check if results match phi-harmonic theory
        phi_accuracy = min(100, 100 * (1 - abs(actual_scaling/expected_scaling - 1)))
        print(f"\nPhi-harmonic accuracy: {phi_accuracy:.1f}%")
        
        if phi_accuracy > 90:
            print("\n✓ PROOF SUCCESSFUL: The simulation confirms phi-harmonic scaling!")
        else:
            print("\n✗ PROOF INCONCLUSIVE: Results deviate from phi-harmonic theory")
    
    elapsed = time.time() - start_time
    print(f"\nSimulation completed in {elapsed:.2f} seconds")
    print(f"Results saved to {output_dir}/")

if __name__ == "__main__":
    run_simulation(duration=100, dt=0.1, visualization_interval=10)
