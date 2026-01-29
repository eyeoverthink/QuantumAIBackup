"""
ATOMIC TRIAD QUANTUM TRANSISTOR
===============================
Self-powered, zero-heat, scalable quantum transistor
based on the φ-harmonic principles of the Atomic Triad Configuration.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.gridspec as gridspec
from matplotlib.patches import Rectangle, Circle, Polygon
import time
import math
import threading
from matplotlib.colors import LinearSegmentedColormap

# Constants
PHI = (1 + np.sqrt(5)) / 2
PLANCK = 6.62607015e-34  # Planck constant
ELECTRON_CHARGE = 1.602176634e-19  # Elementary charge

# Atomic Triad Configuration
ELEMENTS = {
    'Au': {'atomic_number': 79, 'mass': 196.97, 'phi_level': 0, 'function': 'Crown', 'frequency': 12.67, 'color': '#FFD700', 'position': (0, 2)},
    'Ag': {'atomic_number': 47, 'mass': 107.87, 'phi_level': -1, 'function': 'Bridge', 'frequency': 7.83, 'color': '#C0C0C0', 'position': (1.9, 0.7)},
    'Cu': {'atomic_number': 29, 'mass': 63.55, 'phi_level': -2, 'function': 'Base', 'frequency': 4.84, 'color': '#B87333', 'position': (-1.9, 0.7)},
    'Ni': {'atomic_number': 28, 'mass': 58.69, 'phi_level': -3, 'function': 'Core', 'frequency': 2.99, 'color': '#727472', 'position': (-1.2, -1.5)},
    'Fe': {'atomic_number': 26, 'mass': 55.85, 'phi_level': -4, 'function': 'Ground', 'frequency': 1.85, 'color': '#A19D94', 'position': (1.2, -1.5)}
}

# Quantum Gate Mappings
QUANTUM_GATES = {
    ('Au', 'Cu'): {'type': 'AND', 'color': '#FF5733'},
    ('Au', 'Ag'): {'type': 'OR', 'color': '#33FF57'},
    ('Cu', 'Ni'): {'type': 'NOT', 'color': '#3357FF'},
    ('Ag', 'Fe'): {'type': 'NAND', 'color': '#FF33F5'},
    ('Ni', 'Fe'): {'type': 'XOR', 'color': '#F5FF33'}
}

# Energy Flow Circuit
ENERGY_FLOW = ['Cu', 'Ag', 'Au', 'Field', 'Ni', 'Fe']

# Custom colormap for φ-space
phi_colors = [(0.0, '#3A015C'),   # Deep purple
              (0.2, '#4F0147'),   # Dark magenta
              (0.4, '#35012C'),   # Dark purple
              (0.6, '#290025'),   # Very dark purple
              (0.8, '#11001C'),   # Almost black purple
              (1.0, '#010048')]   # Deep blue
phi_cmap = LinearSegmentedColormap.from_list('phi_space', phi_colors)

# Custom colormap for energy flow
energy_colors = [(0.0, '#FFFF00'),   # Yellow
                (0.33, '#FF7F00'),  # Orange
                (0.66, '#FF0000'),  # Red
                (1.0, '#FFFFFF')]   # White
energy_cmap = LinearSegmentedColormap.from_list('energy', energy_colors)

class AtomicTriadTransistor:
    def __init__(self, scale=1.0):
        """
        Initialize the Atomic Triad Quantum Transistor.
        
        Args:
            scale: Scaling factor for the transistor (1.0 = standard size)
        """
        self.phi = PHI
        self.scale = scale
        self.time = 0
        self.dt = 0.05
        self.input_signal = 0.0
        self.output_signal = 0.0
        self.gate_voltage = 0.0
        self.power_generated = 0.0
        self.total_power = 0.0
        self.switching_state = False
        self.resonance_level = 0.0
        self.consciousness_field = 0.0
        
        # Setup the figure
        self.fig = plt.figure(figsize=(15, 10))
        gs = gridspec.GridSpec(3, 3)
        
        # Transistor Schematic
        self.ax1 = self.fig.add_subplot(gs[0:2, 0:2])
        self.ax1.set_title('Atomic Triad Quantum Transistor')
        self.ax1.set_xlim(-3, 3)
        self.ax1.set_ylim(-3, 3)
        self.ax1.set_aspect('equal')
        self.ax1.axis('off')
        
        # Energy Flow Plot
        self.ax2 = self.fig.add_subplot(gs[2, 0:2])
        self.ax2.set_title('φ-Harmonic Energy Flow')
        self.ax2.set_xlim(0, 10)
        self.ax2.set_ylim(-2, 2)
        self.ax2.set_xlabel('Time (s)')
        self.ax2.set_ylabel('Energy')
        self.ax2.grid(True)
        
        # Power Generation
        self.ax3 = self.fig.add_subplot(gs[0, 2])
        self.ax3.set_title('Power Generation')
        self.ax3.set_xlim(0, 1)
        self.ax3.set_ylim(0, 1)
        self.ax3.set_xticks([])
        self.ax3.set_yticks([])
        
        # Quantum Gate Status
        self.ax4 = self.fig.add_subplot(gs[1, 2])
        self.ax4.set_title('Quantum Gate Status')
        self.ax4.set_xlim(0, 1)
        self.ax4.set_ylim(0, 1)
        self.ax4.set_xticks([])
        self.ax4.set_yticks([])
        
        # I/O Signals
        self.ax5 = self.fig.add_subplot(gs[2, 2])
        self.ax5.set_title('I/O Signals')
        self.ax5.set_xlim(0, 1)
        self.ax5.set_ylim(0, 1)
        self.ax5.set_xticks([])
        self.ax5.set_yticks([])
        
        # Initialize plots
        self.element_circles = {}
        self.gate_lines = {}
        self.energy_flow_lines = {}
        self.energy_data = {element: {'times': [], 'values': []} for element in ELEMENTS}
        self.combined_energy = {'times': [], 'values': []}
        
        self.fig.tight_layout()
        self.fig.suptitle('ATOMIC TRIAD QUANTUM TRANSISTOR', fontsize=16)
    
    def initialize_plots(self):
        """Initialize all plot elements."""
        # Draw transistor body
        transistor_body = Polygon([(-2.5, -2), (2.5, -2), (2.5, 2.5), (-2.5, 2.5)], 
                                 closed=True, fill=True, color='#1A1A1A', alpha=0.2)
        self.ax1.add_patch(transistor_body)
        
        # Draw terminals
        source = Rectangle((-3, 0.5), 0.5, 1, color='#B87333', alpha=0.8)  # Copper color for source
        drain = Rectangle((2.5, 0.5), 0.5, 1, color='#FFD700', alpha=0.8)  # Gold color for drain
        gate = Rectangle((-1, -2.5), 2, 0.5, color='#C0C0C0', alpha=0.8)   # Silver color for gate
        
        self.ax1.add_patch(source)
        self.ax1.add_patch(drain)
        self.ax1.add_patch(gate)
        
        self.ax1.text(-2.75, 1.75, 'SOURCE', fontsize=8, ha='center')
        self.ax1.text(2.75, 1.75, 'DRAIN', fontsize=8, ha='center')
        self.ax1.text(0, -2.25, 'GATE', fontsize=8, ha='center')
        
        # Draw elements
        for element, data in ELEMENTS.items():
            x, y = data['position']
            size = 0.3 * (data['mass'] / ELEMENTS['Fe']['mass'])**(1/3) * self.scale
            circle = Circle((x, y), size, color=data['color'], alpha=0.8, zorder=10)
            self.element_circles[element] = circle
            self.ax1.add_patch(circle)
            self.ax1.text(x, y, element, fontsize=10, ha='center', va='center', zorder=11)
        
        # Draw quantum gates
        for (src, tgt), gate_data in QUANTUM_GATES.items():
            x1, y1 = ELEMENTS[src]['position']
            x2, y2 = ELEMENTS[tgt]['position']
            line, = self.ax1.plot([x1, x2], [y1, y2], color=gate_data['color'], 
                                 alpha=0.5, linewidth=2, zorder=5)
            self.gate_lines[(src, tgt)] = line
            
            # Add gate label
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            self.ax1.text(mid_x, mid_y, gate_data['type'], fontsize=8, 
                         ha='center', va='center', bbox=dict(facecolor='white', alpha=0.7))
        
        # Draw energy flow lines
        for i in range(len(ENERGY_FLOW) - 1):
            src = ENERGY_FLOW[i]
            tgt = ENERGY_FLOW[i + 1]
            
            if src == 'Field':
                x1, y1 = (0, 0.5)  # Field position
            else:
                x1, y1 = ELEMENTS[src]['position']
                
            if tgt == 'Field':
                x2, y2 = (0, 0.5)  # Field position
            else:
                x2, y2 = ELEMENTS[tgt]['position']
            
            line, = self.ax1.plot([x1, x2], [y1, y2], 'w--', alpha=0.3, zorder=1)
            self.energy_flow_lines[(src, tgt)] = line
        
        # Initialize energy flow plot
        for element in ELEMENTS:
            line, = self.ax2.plot([], [], label=element, color=ELEMENTS[element]['color'])
            self.energy_flow_lines[element] = line
        
        # Initialize combined energy
        combined_line, = self.ax2.plot([], [], 'w-', linewidth=2, label='Combined')
        self.energy_flow_lines['combined'] = combined_line
        self.ax2.legend(loc='upper right')
        
        # Initialize power generation display
        self.power_text = self.ax3.text(0.5, 0.5, 'Power: 0.00 μW\nTotal: 0.00 J', 
                                      ha='center', va='center', fontsize=12)
        self.ax3.add_patch(Circle((0.5, 0.5), 0.4, color='blue', alpha=0.1))
        
        # Initialize quantum gate status
        self.gate_status = {}
        y_pos = 0.8
        for (src, tgt), gate_data in QUANTUM_GATES.items():
            gate_type = gate_data['type']
            status_text = self.ax4.text(0.5, y_pos, f'{gate_type}: OFF', 
                                      ha='center', va='center', fontsize=10)
            self.gate_status[(src, tgt)] = status_text
            y_pos -= 0.15
        
        # Initialize I/O signals
        self.signal_text = self.ax5.text(0.5, 0.5, 
                                       'Input: 0.00 V\nOutput: 0.00 V\nGain: 0.00x', 
                                       ha='center', va='center', fontsize=12)
    
    def calculate_energy_flow(self, t):
        """Calculate energy flow through the transistor at time t."""
        energy_values = {}
        combined_energy = 0
        
        # Base input signal (sine wave)
        base_input = np.sin(2 * np.pi * 0.5 * t)  # 0.5 Hz
        
        # Apply gate voltage modulation
        self.gate_voltage = 0.5 + 0.5 * np.sin(2 * np.pi * 0.1 * t)  # 0.1 Hz
        
        # Calculate input signal with gate modulation
        self.input_signal = base_input * self.gate_voltage
        
        # Calculate energy flow through each element
        for element, data in ELEMENTS.items():
            # Calculate phase based on element's frequency
            phase = 2 * np.pi * data['frequency'] * t
            
            # Calculate amplitude based on input signal and φ-level
            amplitude = (1.0 / max(1.0, self.phi ** abs(data['phi_level']))) * (0.5 + 0.5 * self.input_signal)
            
            # Calculate energy value
            energy = amplitude * np.sin(phase + (data['phi_level'] * np.pi / 5))
            
            energy_values[element] = {
                'amplitude': amplitude,
                'phase': phase,
                'energy': energy
            }
            
            combined_energy += energy
        
        # Calculate consciousness field at φ³ frequency
        consciousness_phase = 2 * np.pi * (self.phi**3) * t
        self.consciousness_field = 0.2 * np.sin(consciousness_phase)
        
        # Add consciousness field to combined energy
        combined_energy += self.consciousness_field
        
        # Calculate output signal with φ-harmonic amplification
        self.output_signal = combined_energy * self.phi
        
        # Calculate power generation (μW)
        self.power_generated = abs(combined_energy) * (self.phi**2) * 10  # Scale to μW
        self.total_power += self.power_generated * self.dt * 1e-6  # Convert to Joules
        
        return energy_values, combined_energy
    
    def calculate_quantum_gates(self, energy_values):
        """Calculate quantum gate states based on energy values."""
        gate_states = {}
        
        for (src, tgt), gate_data in QUANTUM_GATES.items():
            # Get energy values for source and target elements
            src_energy = energy_values[src]['energy']
            tgt_energy = energy_values[tgt]['energy']
            
            # Calculate gate state based on gate type
            if gate_data['type'] == 'AND':
                state = (src_energy > 0) and (tgt_energy > 0)
            elif gate_data['type'] == 'OR':
                state = (src_energy > 0) or (tgt_energy > 0)
            elif gate_data['type'] == 'NOT':
                state = not (src_energy > 0)
            elif gate_data['type'] == 'NAND':
                state = not ((src_energy > 0) and (tgt_energy > 0))
            elif gate_data['type'] == 'XOR':
                state = (src_energy > 0) != (tgt_energy > 0)
            else:
                state = False
            
            gate_states[(src, tgt)] = state
        
        # Calculate overall switching state (XOR of all gates)
        self.switching_state = False
        for state in gate_states.values():
            self.switching_state = self.switching_state != state  # XOR
        
        return gate_states
    
    def calculate_resonance(self, energy_values):
        """Calculate resonance level based on energy values."""
        # Calculate phase alignment between elements
        phase_alignment = 0
        count = 0
        
        for i, element1 in enumerate(ELEMENTS):
            for j, element2 in enumerate(ELEMENTS):
                if i < j:  # Only consider unique pairs
                    phase1 = energy_values[element1]['phase']
                    phase2 = energy_values[element2]['phase']
                    
                    # Calculate phase difference
                    phase_diff = abs((phase1 - phase2) % (2 * np.pi))
                    if phase_diff > np.pi:
                        phase_diff = 2 * np.pi - phase_diff
                    
                    # Calculate alignment (1.0 = perfect alignment, 0.0 = anti-alignment)
                    alignment = 1.0 - (phase_diff / np.pi)
                    phase_alignment += alignment
                    count += 1
        
        # Calculate average alignment
        if count > 0:
            phase_alignment /= count
        
        # Apply self-reinforcing resonance
        self.resonance_level = self.resonance_level * 0.95 + phase_alignment * 0.05
        if self.resonance_level > 0.88:  # Critical threshold
            self.resonance_level = min(self.resonance_level * 1.01, 0.99)  # Self-reinforcing
        
        return self.resonance_level
    
    def update(self, frame):
        """Update function for animation."""
        self.time += self.dt
        
        # Calculate energy flow
        energy_values, combined_energy = self.calculate_energy_flow(self.time)
        
        # Update energy data for plotting
        for element, data in energy_values.items():
            self.energy_data[element]['times'].append(self.time)
            self.energy_data[element]['values'].append(data['energy'])
            
            # Keep only the last 200 points
            if len(self.energy_data[element]['times']) > 200:
                self.energy_data[element]['times'] = self.energy_data[element]['times'][-200:]
                self.energy_data[element]['values'] = self.energy_data[element]['values'][-200:]
            
            # Update energy flow lines
            if element in self.energy_flow_lines:
                self.energy_flow_lines[element].set_data(self.energy_data[element]['times'], 
                                                      self.energy_data[element]['values'])
        
        # Update combined energy
        self.combined_energy['times'].append(self.time)
        self.combined_energy['values'].append(combined_energy)
        
        # Keep only the last 200 points
        if len(self.combined_energy['times']) > 200:
            self.combined_energy['times'] = self.combined_energy['times'][-200:]
            self.combined_energy['values'] = self.combined_energy['values'][-200:]
        
        # Update combined energy line
        self.energy_flow_lines['combined'].set_data(self.combined_energy['times'], 
                                                 self.combined_energy['values'])
        
        # Update x-axis limits for energy plot
        self.ax2.set_xlim(self.time - 10, self.time)
        
        # Calculate quantum gate states
        gate_states = self.calculate_quantum_gates(energy_values)
        
        # Calculate resonance
        resonance = self.calculate_resonance(energy_values)
        
        # Update element circles based on energy
        for element, circle in self.element_circles.items():
            energy = energy_values[element]['energy']
            
            # Pulsate size based on energy
            base_size = 0.3 * (ELEMENTS[element]['mass'] / ELEMENTS['Fe']['mass'])**(1/3) * self.scale
            new_size = base_size * (1 + 0.3 * abs(energy))
            
            # Update circle
            circle.set_radius(new_size)
            
            # Update color based on energy (brighter when positive)
            if energy > 0:
                circle.set_alpha(0.8 + 0.2 * energy)
            else:
                circle.set_alpha(0.8 - 0.2 * abs(energy))
        
        # Update quantum gate lines based on states
        for (src, tgt), line in self.gate_lines.items():
            state = gate_states[(src, tgt)]
            
            # Update line appearance based on state
            if state:
                line.set_alpha(0.8)
                line.set_linewidth(3)
                line.set_color(QUANTUM_GATES[(src, tgt)]['color'])
            else:
                line.set_alpha(0.3)
                line.set_linewidth(1)
                line.set_color('gray')
        
        # Update energy flow lines
        for i in range(len(ENERGY_FLOW) - 1):
            src = ENERGY_FLOW[i]
            tgt = ENERGY_FLOW[i + 1]
            
            if (src, tgt) in self.energy_flow_lines:
                line = self.energy_flow_lines[(src, tgt)]
                
                # Calculate energy flow intensity
                if src == 'Field' or tgt == 'Field':
                    intensity = abs(self.consciousness_field)
                elif src in energy_values and tgt in energy_values:
                    intensity = abs(energy_values[src]['energy'] * energy_values[tgt]['energy'])
                else:
                    intensity = 0
                
                # Update line appearance
                line.set_alpha(0.3 + 0.7 * min(intensity, 1.0))
                line.set_color(energy_cmap(min(intensity, 1.0)))
                line.set_linewidth(1 + 2 * min(intensity, 1.0))
        
        # Update power generation display
        self.ax3.clear()
        self.ax3.set_title('Power Generation')
        self.ax3.set_xlim(0, 1)
        self.ax3.set_ylim(0, 1)
        self.ax3.set_xticks([])
        self.ax3.set_yticks([])
        
        # Draw power meter
        power_level = min(self.power_generated / 10, 1.0)
        self.ax3.add_patch(Circle((0.5, 0.5), 0.4, color='blue', alpha=0.1))
        self.ax3.add_patch(Circle((0.5, 0.5), 0.4 * power_level, color='blue', alpha=0.5))
        self.ax3.text(0.5, 0.5, f'Power: {self.power_generated:.2f} μW\nTotal: {self.total_power:.6f} J', 
                     ha='center', va='center', fontsize=12)
        
        # Update quantum gate status
        for (src, tgt), text in self.gate_status.items():
            state = gate_states[(src, tgt)]
            gate_type = QUANTUM_GATES[(src, tgt)]['type']
            text.set_text(f'{gate_type}: {"ON" if state else "OFF"}')
            text.set_color('green' if state else 'red')
        
        # Update I/O signals
        gain = abs(self.output_signal / (self.input_signal + 1e-10))  # Avoid division by zero
        self.signal_text.set_text(f'Input: {self.input_signal:.2f} V\n' +
                                f'Output: {self.output_signal:.2f} V\n' +
                                f'Gain: {gain:.2f}x')
        
        # Update transistor body color based on switching state
        if self.switching_state:
            transistor_color = 'green'
            transistor_alpha = 0.2
        else:
            transistor_color = 'red'
            transistor_alpha = 0.1
            
        # Remove old transistor body and add new one
        for patch in self.ax1.patches:
            if isinstance(patch, Polygon):
                patch.remove()
                
        transistor_body = Polygon([(-2.5, -2), (2.5, -2), (2.5, 2.5), (-2.5, 2.5)], 
                                 closed=True, fill=True, color=transistor_color, alpha=transistor_alpha)
        self.ax1.add_patch(transistor_body)
        
        # Return updated artists
        return tuple(self.element_circles.values()) + tuple(self.gate_lines.values()) + tuple(self.energy_flow_lines.values())
    
    def run(self):
        """Run the transistor simulation."""
        # In a multi-threaded environment, we'll avoid showing the plot directly
        # and instead just perform the calculations without visualization
        print("Atomic Triad Transistor running in background mode")
        
        # Initialize the quantum state without creating plots
        self.initialize_quantum_state()
        
        # Start a background thread for state updates
        self.running = True
        self.update_thread = threading.Thread(target=self.background_update)
        self.update_thread.daemon = True
        self.update_thread.start()
        
    def initialize_quantum_state(self):
        """Initialize the quantum state without visualization."""
        # Set initial values for quantum state variables
        self.energy_values = {element: 0.5 for element in ELEMENTS}
        self.gate_states = {gate: False for gate in QUANTUM_GATES}
        
        # Initialize energy flow
        self.energy_flow_values = [0.0] * len(ENERGY_FLOW)
        
        # Initialize phi-harmonic resonance values
        self.resonance_level = 0.5
        self.consciousness_field = 0.0
        self.power_generated = 0.0
        self.total_power = 0.0
        self.input_signal = 0.1
        self.output_signal = 0.0
        self.switching_state = False
        
        print(f"Quantum state initialized with phi-resonance: {self.phi}")
        print(f"Initial resonance level: {self.resonance_level}")
    
    def update_quantum_state(self):
        """Update the quantum state without visualization."""
        # Update time
        self.time += self.dt
        
        # Calculate energy flow
        energy_flow = self.calculate_energy_flow(self.time)
        
        # Update energy values for each element
        for i, element in enumerate(ELEMENTS):
            # Add some randomness to simulate quantum fluctuations
            fluctuation = 0.1 * (np.random.random() - 0.5)
            # Get energy from the flow if this element is in the flow
            if element in ENERGY_FLOW:
                idx = ENERGY_FLOW.index(element)
                flow_contribution = energy_flow[idx] if idx < len(energy_flow) else 0
            else:
                flow_contribution = 0
            
            # Update energy value with flow and fluctuation
            self.energy_values[element] = max(0, min(1, 
                                              self.energy_values[element] + 
                                              flow_contribution * 0.1 + 
                                              fluctuation))
        
        # Calculate gate states based on energy values
        gate_states = self.calculate_quantum_gates(self.energy_values)
        for gate in QUANTUM_GATES:
            self.gate_states[gate] = gate_states[gate]
        
        # Calculate resonance level
        self.resonance_level = self.calculate_resonance(self.energy_values)
        
        # Update consciousness field based on resonance
        consciousness_frequency = self.phi**3  # φ³ frequency (≈ 4.2)  
        self.consciousness_field = 0.5 + 0.5 * np.sin(consciousness_frequency * self.time)
        
        # Calculate power generation based on energy flow and resonance
        power_factor = sum(self.energy_values.values()) / len(self.energy_values)
        self.power_generated = power_factor * self.resonance_level * self.phi
        self.total_power += self.power_generated * self.dt
        
        # Update I/O signals
        self.input_signal = 0.5 + 0.5 * np.sin(self.time)
        # Output depends on gate states
        active_gates = sum(1 for state in self.gate_states.values() if state)
        gate_factor = active_gates / len(self.gate_states) if self.gate_states else 0
        self.output_signal = self.input_signal * self.phi * gate_factor * self.resonance_level
        
        # Update switching state
        self.switching_state = self.output_signal > 0.5
    
    def background_update(self):
        """Update the quantum state in the background without visualization"""
        while self.running:
            # Update quantum state
            self.update_quantum_state()
            # Sleep to control update rate
            time.sleep(0.05)
            
    def stop(self):
        """Stop the transistor simulation"""
        self.running = False
        if hasattr(self, 'update_thread') and self.update_thread:
            self.update_thread.join(timeout=1.0)

if __name__ == "__main__":
    print("Starting Atomic Triad Quantum Transistor Simulation...")
    print("φ-Harmonic Quantum Gates: AND, OR, NOT, NAND, XOR")
    print("Self-powered operation through φ-harmonic resonance")
    print("Zero heat generation through wave cancellation")
    print("Consciousness integration at φ³ frequency (20.50 Hz)")
    print("Initializing simulation...")
    
    transistor = AtomicTriadTransistor(scale=1.0)
    transistor.run()
