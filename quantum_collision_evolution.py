"""
QUANTUM COLLISION EVOLUTION SYSTEM
Simulates particle collisions using φ-harmonic principles to discover new elements
"""

import numpy as np
import sys
import os
import random
import matplotlib.pyplot as plt
from datetime import datetime
from decimal import Decimal, getcontext
import matplotlib.animation as animation
from matplotlib.colors import LinearSegmentedColormap
from io import StringIO

# Set precision for φ calculations
getcontext().prec = 5000

# Add path to quantum components
sys.path.append('/Users/vaughnscott/Documents/fraymus_shit/DigitalNLP-main')
sys.path.append('/Users/vaughnscott/CascadeProjects/Fraymus_Replit_Two/quantum_visualizations')

# Import quantum components
try:
    from quantum_periodic_brain_v2 import QuantumPeriodicBrainV2
    BRAIN_VERSION = 'v2'
except ImportError:
    try:
        from quantum_periodic_brain import QuantumPeriodicBrain
        BRAIN_VERSION = 'v1'
    except ImportError:
        print("Warning: Quantum brain modules not found. Using simplified mode.")
        BRAIN_VERSION = 'simple'

class QuantumCollisionEvolution:
    def __init__(self):
        # Initialize φ constants
        self.phi = Decimal(str((1 + np.sqrt(5)) / 2))
        self.phi_powers = [float(self.phi ** i) for i in range(1, 8)]
        
        # Load ASCII periodic table
        self.ascii_table = self._load_ascii_table()
        self.ascii_lines = self.ascii_table.split('\n')
        
        # Initialize element data
        self.elements = self._initialize_elements()
        
        # Initialize quantum brain if available
        self.quantum_brain = self._initialize_quantum_brain()
        
        # Track discovered elements
        self.discovered_elements = {}
        self.collision_history = []
        
        # Directory for saving results
        self.results_dir = 'quantum_collision_results'
        os.makedirs(self.results_dir, exist_ok=True)
        
    def _load_ascii_table(self):
        """Load the ASCII periodic table for display"""
        try:
            with open('/Users/vaughnscott/Documents/fraymus_shit/Ascii_Element_Chart.txt', 'r') as f:
                return f.read()
        except FileNotFoundError:
            return "ASCII Periodic Table not found"
    
    def _initialize_elements(self):
        """Initialize element data with properties"""
        # Basic element data (abbreviated for brevity)
        elements = {
            'H': {'number': 1, 'name': 'Hydrogen', 'mass': 1.008, 'group': 1, 'period': 1},
            'He': {'number': 2, 'name': 'Helium', 'mass': 4.0026, 'group': 18, 'period': 1},
            'Li': {'number': 3, 'name': 'Lithium', 'mass': 6.94, 'group': 1, 'period': 2},
            'Be': {'number': 4, 'name': 'Beryllium', 'mass': 9.0122, 'group': 2, 'period': 2},
            'B': {'number': 5, 'name': 'Boron', 'mass': 10.81, 'group': 13, 'period': 2},
            'C': {'number': 6, 'name': 'Carbon', 'mass': 12.011, 'group': 14, 'period': 2},
            'N': {'number': 7, 'name': 'Nitrogen', 'mass': 14.007, 'group': 15, 'period': 2},
            'O': {'number': 8, 'name': 'Oxygen', 'mass': 15.999, 'group': 16, 'period': 2},
            'F': {'number': 9, 'name': 'Fluorine', 'mass': 18.998, 'group': 17, 'period': 2},
            'Ne': {'number': 10, 'name': 'Neon', 'mass': 20.180, 'group': 18, 'period': 2},
            'Na': {'number': 11, 'name': 'Sodium', 'mass': 22.990, 'group': 1, 'period': 3},
            'Mg': {'number': 12, 'name': 'Magnesium', 'mass': 24.305, 'group': 2, 'period': 3},
            'Al': {'number': 13, 'name': 'Aluminum', 'mass': 26.982, 'group': 13, 'period': 3},
            'Si': {'number': 14, 'name': 'Silicon', 'mass': 28.085, 'group': 14, 'period': 3},
            'P': {'number': 15, 'name': 'Phosphorus', 'mass': 30.974, 'group': 15, 'period': 3},
            'S': {'number': 16, 'name': 'Sulfur', 'mass': 32.06, 'group': 16, 'period': 3},
            'Cl': {'number': 17, 'name': 'Chlorine', 'mass': 35.45, 'group': 17, 'period': 3},
            'Ar': {'number': 18, 'name': 'Argon', 'mass': 39.948, 'group': 18, 'period': 3},
            'K': {'number': 19, 'name': 'Potassium', 'mass': 39.098, 'group': 1, 'period': 4},
            'Ca': {'number': 20, 'name': 'Calcium', 'mass': 40.078, 'group': 2, 'period': 4},
            'Fe': {'number': 26, 'name': 'Iron', 'mass': 55.845, 'group': 8, 'period': 4},
            'Co': {'number': 27, 'name': 'Cobalt', 'mass': 58.933, 'group': 9, 'period': 4},
            'Ni': {'number': 28, 'name': 'Nickel', 'mass': 58.693, 'group': 10, 'period': 4},
            'Cu': {'number': 29, 'name': 'Copper', 'mass': 63.546, 'group': 11, 'period': 4},
            'Zn': {'number': 30, 'name': 'Zinc', 'mass': 65.38, 'group': 12, 'period': 4},
            'Ag': {'number': 47, 'name': 'Silver', 'mass': 107.87, 'group': 11, 'period': 5},
            'Au': {'number': 79, 'name': 'Gold', 'mass': 196.97, 'group': 11, 'period': 6},
            'Pt': {'number': 78, 'name': 'Platinum', 'mass': 195.08, 'group': 10, 'period': 6},
            'Pb': {'number': 82, 'name': 'Lead', 'mass': 207.2, 'group': 14, 'period': 6},
            'U': {'number': 92, 'name': 'Uranium', 'mass': 238.03, 'group': 102, 'period': 7},
        }
        
        # Add quantum properties
        for symbol, data in elements.items():
            # Calculate φ-resonance
            phi_res = (float(self.phi) * data['mass']) % 1
            data['phi_resonance'] = phi_res
            
            # Calculate quantum conductivity
            data['conductivity'] = data['number'] * 1e5 * (1 + phi_res)
            
            # Calculate electronegativity (approximation)
            data['electronegativity'] = 0.5 + (data['group'] % 18) / 5.0
            
            # Add melting point (approximation)
            data['melting_point'] = 300 + data['number'] * 10 * (1 - phi_res)
            
            # Add density (approximation)
            data['density'] = 0.5 + data['number'] / 10
            
            # Add valence electrons (approximation)
            if data['group'] <= 2:
                data['valence'] = data['group']
            elif data['group'] >= 13:
                data['valence'] = data['group'] - 10
            else:
                data['valence'] = 2 + (data['group'] % 10)
            
            # Add quantum state
            data['quantum_state'] = np.zeros(17, dtype=np.complex128)
            phase = 2 * np.pi * float(self.phi) * data['mass']
            for i in range(17):
                data['quantum_state'][i] = np.exp(1j * phase * (i + 1) / 17)
            
        return elements
    
    def _initialize_quantum_brain(self):
        """Initialize quantum brain if available"""
        try:
            if BRAIN_VERSION == 'v2':
                return QuantumPeriodicBrainV2()
            elif BRAIN_VERSION == 'v1':
                return QuantumPeriodicBrain()
            else:
                return None
        except Exception as e:
            print(f"Warning: Could not initialize quantum brain: {e}")
            return None
    
    def select_collision_elements(self, count=2, seed=None):
        """Select elements for collision based on φ-resonance"""
        if seed is not None:
            np.random.seed(seed)
            random.seed(seed)
            
        # Get all elements
        all_elements = list(self.elements.keys())
        
        # Calculate φ-resonance for each element
        resonances = {symbol: self.elements[symbol]['phi_resonance'] for symbol in all_elements}
        
        # Sort by proximity to perfect φ-resonance (0 or 1)
        sorted_elements = sorted(all_elements, 
                                key=lambda x: min(resonances[x], 1 - resonances[x]))
        
        # Select elements with good φ-resonance
        phi_elements = sorted_elements[:int(len(sorted_elements) * 0.382)]  # Top 38.2% (1/φ)
        
        # Select random elements from the φ-resonant ones
        selected = random.sample(phi_elements, min(count, len(phi_elements)))
        
        return selected
    
    def simulate_collision(self, elements=None, energy_factor=1.0):
        """Simulate a quantum collision between elements"""
        # Select elements if not provided
        if elements is None:
            elements = self.select_collision_elements(count=random.randint(2, 3))
        
        # Get element data
        element_data = {e: self.elements[e] for e in elements}
        
        # Calculate collision parameters
        total_mass = sum(element_data[e]['mass'] for e in elements)
        total_number = sum(element_data[e]['number'] for e in elements)
        
        # Calculate energy based on φ-scaling
        energy = total_mass * float(self.phi**3) * energy_factor
        
        # Calculate φ-resonance of the collision
        collision_resonance = (float(self.phi) * total_mass) % 1
        
        # Calculate quantum state transformation
        quantum_state = np.zeros(17, dtype=np.complex128)
        for e in elements:
            quantum_state += element_data[e]['quantum_state']
        
        # Normalize
        quantum_state /= np.sqrt(np.sum(np.abs(quantum_state)**2))
        
        # Apply φ-phase transformation
        phase_shift = 2 * np.pi * collision_resonance
        quantum_state *= np.exp(1j * phase_shift)
        
        # Calculate consciousness state
        consciousness = {
            'theta': {'frequency': 432.0 * float(self.phi), 'coherence': collision_resonance, 
                      'amplitude': 0.5 + 0.5 * collision_resonance},
            'alpha': {'frequency': 528.0 * float(self.phi), 'coherence': 1 - collision_resonance,
                     'amplitude': 0.5 + 0.5 * (1 - collision_resonance)},
            'beta': {'frequency': 639.0 * float(self.phi), 'coherence': abs(0.5 - collision_resonance) * 2,
                    'amplitude': 0.5 + 0.5 * abs(0.5 - collision_resonance) * 2},
            'gamma': {'frequency': 741.0 * float(self.phi), 'coherence': min(collision_resonance, 1 - collision_resonance) * 2,
                     'amplitude': 0.5 + 0.5 * min(collision_resonance, 1 - collision_resonance) * 2}
        }
        
        # Process through quantum brain if available
        if self.quantum_brain is not None:
            try:
                # Advance epoch
                self.quantum_brain.advance_epoch()
                
                # Process collision data
                for e in elements:
                    self.quantum_brain.analyze_quantum_properties(e)
            except Exception as e:
                print(f"Warning: Quantum brain processing failed: {e}")
        
        # Determine if new element is discovered based on resonance
        # Lower threshold to increase discovery chance
        new_element = None
        if collision_resonance < 0.2 or collision_resonance > 0.8 or \
           abs(collision_resonance - 0.618) < 0.05:  # High resonance or near φ^-1
            new_element = self._discover_new_element(elements, total_mass, total_number, 
                                                   collision_resonance, quantum_state)
        
        # Prepare result
        result = {
            'elements': elements,
            'element_data': element_data,
            'total_mass': total_mass,
            'total_number': total_number,
            'energy': energy,
            'phi_resonance': collision_resonance,
            'quantum_state': quantum_state,
            'consciousness': consciousness,
            'timestamp': datetime.now().strftime('%Y%m%d_%H%M%S'),
            'new_element': new_element
        }
        
        # Add to collision history
        self.collision_history.append(result)
        
        return result
    
    def _discover_new_element(self, parent_elements, mass, number, resonance, quantum_state):
        """Discover a new element based on collision parameters"""
        # Generate new element properties using φ-harmonic principles
        phi_factor = float(self.phi) if resonance < 0.5 else 1/float(self.phi)
        
        # Apply φ-scaling to atomic number and mass
        new_number = int(number * phi_factor * (1 + 0.1 * (resonance - 0.5)))
        new_mass = mass * phi_factor * (1 + 0.05 * (resonance - 0.5))
        
        # Check if this is close to an existing element
        for symbol, data in self.elements.items():
            if abs(data['number'] - new_number) < 0.5:
                # Too close to existing element, no discovery
                return None
        
        # Generate new element symbol (first letters of parents + φ)
        symbol_base = ''.join([e[0] for e in parent_elements])
        if len(symbol_base) == 1:
            symbol_base += 'φ'
        elif len(symbol_base) > 2:
            symbol_base = symbol_base[:2]
        
        # Check if symbol exists, append number if needed
        symbol = symbol_base
        counter = 1
        while symbol in self.elements or symbol in self.discovered_elements:
            symbol = f"{symbol_base}{counter}"
            counter += 1
        
        # Generate name
        parent_names = [self.elements[e]['name'] for e in parent_elements]
        name_base = ''.join([n[:4] for n in parent_names])
        name = f"{name_base}ium"
        
        # Determine group and period based on quantum number
        group = 1 + (new_number % 18)
        period = 1 + (new_number // 18)
        
        # Create new element data
        new_element = {
            'symbol': symbol,
            'name': name,
            'number': new_number,
            'mass': new_mass,
            'group': group,
            'period': period,
            'phi_resonance': (float(self.phi) * new_mass) % 1,
            'parents': parent_elements,
            'discovery_time': datetime.now().strftime('%Y%m%d_%H%M%S'),
            'quantum_state': quantum_state
        }
        
        # Add to discovered elements
        self.discovered_elements[symbol] = new_element
        
        # Update ASCII table
        self._update_ascii_table(new_element)
        
        return new_element
    
    def _update_ascii_table(self, new_element):
        """Update ASCII table with new element"""
        # Create a new ASCII representation for the element
        symbol = new_element['symbol']
        name = new_element['name']
        mass = f"{new_element['mass']:.4f}"
        number = str(new_element['number'])
        
        # Create ASCII box for the element
        box_width = max(len(symbol), len(name), len(mass), len(number)) + 4
        box_width = max(box_width, 10)  # Minimum width
        
        box = [
            "+" + "-" * box_width + "+",
            "|" + number.center(box_width) + "|",
            "|" + symbol.center(box_width) + "|",
            "|" + name.center(box_width) + "|",
            "|" + mass.center(box_width) + "|",
            "+" + "-" * box_width + "+"
        ]
        
        # Create a new file for quantum discoveries if it doesn't exist
        discoveries_file = '/Users/vaughnscott/Documents/fraymus_shit/Quantum_Discoveries.txt'
        
        # Write discovery information
        with open(discoveries_file, 'a+') as f:
            f.write(f"\n{'='*60}\n")
            f.write(f"NEW ELEMENT DISCOVERED: {new_element['symbol']} - {new_element['name']}\n")
            f.write(f"{'='*60}\n\n")
            
            # Write ASCII box
            for line in box:
                f.write(line + "\n")
            f.write("\n")
            
            # Write detailed properties
            f.write(f"PROPERTIES:\n")
            f.write(f"Atomic Number: {new_element['number']}\n")
            f.write(f"Mass: {new_element['mass']:.4f}\n")
            f.write(f"Group: {new_element['group']}, Period: {new_element['period']}\n")
            f.write(f"φ-Resonance: {new_element['phi_resonance']:.6f}\n")
            f.write(f"Parent Elements: {', '.join(new_element['parents'])}\n")
            f.write(f"Discovery Time: {new_element['discovery_time']}\n\n")
            
            # Add quantum properties
            f.write(f"QUANTUM PROPERTIES:\n")
            f.write(f"φ-Harmonic Frequency: {432.0 * float(self.phi) * new_element['phi_resonance']:.2f} Hz\n")
            f.write(f"Quantum Stability: {1.0 - abs(0.5 - new_element['phi_resonance']):.4f}\n")
            f.write(f"Resonance Type: {'φ-Resonant' if new_element['phi_resonance'] < 0.1 else 'Anti-φ-Resonant' if new_element['phi_resonance'] > 0.9 else 'φ-Neutral'}\n\n")
            
        # Also create a standalone file for this element
        element_file = f"/Users/vaughnscott/Documents/fraymus_shit/elements/{new_element['symbol']}.txt"
        os.makedirs(os.path.dirname(element_file), exist_ok=True)
        
        with open(element_file, 'w') as f:
            f.write(f"{new_element['symbol']} - {new_element['name']}\n")
            f.write(f"{'='*60}\n\n")
            
            # Write ASCII box
            for line in box:
                f.write(line + "\n")
            f.write("\n")
            
            # Write all properties in JSON-like format
            for key, value in new_element.items():
                if key == 'quantum_state':
                    continue  # Skip complex arrays
                f.write(f"{key}: {value}\n")
                
        return box
    
    def visualize_collision(self, result, save_path=None):
        """Visualize the quantum collision"""
        # Create figure with multiple subplots
        fig = plt.figure(figsize=(15, 10))
        
        # Plot 1: Element information
        ax1 = fig.add_subplot(221)
        ax1.axis('off')
        elements_text = "Collision Elements:\n\n"
        for e in result['elements']:
            data = result['element_data'][e]
            elements_text += f"{e}: {data['name']} (Z={data['number']}, Mass={data['mass']:.4f})\n"
        
        elements_text += f"\nTotal Mass: {result['total_mass']:.4f} u\n"
        elements_text += f"Total Atomic Number: {result['total_number']}\n"
        elements_text += f"Collision Energy: {result['energy']:.2e} φ-units\n"
        elements_text += f"φ-Resonance: {result['phi_resonance']:.6f}\n"
        
        if result['new_element']:
            elements_text += f"\nNEW ELEMENT DISCOVERED!\n"
            elements_text += f"{result['new_element']['symbol']}: {result['new_element']['name']}\n"
            elements_text += f"Z={result['new_element']['number']}, Mass={result['new_element']['mass']:.4f}\n"
        
        ax1.text(0.05, 0.95, elements_text, transform=ax1.transAxes, 
                fontsize=10, verticalalignment='top')
        
        # Plot 2: Quantum state visualization
        ax2 = fig.add_subplot(222)
        quantum_state = result['quantum_state']
        amplitudes = np.abs(quantum_state)
        phases = np.angle(quantum_state)
        
        # Create color map based on phases
        colors = []
        for phase in phases:
            # Map phase (-π to π) to hue (0 to 1)
            hue = (phase + np.pi) / (2 * np.pi)
            # Create RGB color (simplified HSV to RGB)
            r = np.abs(1 - 2 * np.abs(hue - 1/6))
            g = np.abs(1 - 2 * np.abs(hue - 3/6))
            b = np.abs(1 - 2 * np.abs(hue - 5/6))
            colors.append((r, g, b))
        
        # Plot bars with colors
        bars = ax2.bar(range(1, 18), amplitudes, color=colors)
        
        # Add phase markers
        for i, (amp, phase) in enumerate(zip(amplitudes, phases)):
            ax2.text(i+1, amp + 0.02, f"{phase:.2f}", ha='center', fontsize=8)
        
        ax2.set_title('Quantum State')
        ax2.set_xlabel('Quantum Number')
        ax2.set_ylabel('Amplitude')
        ax2.set_ylim(0, 1.1)
        
        # Plot 3: Consciousness state
        ax3 = fig.add_subplot(223)
        consciousness = result['consciousness']
        waves = list(consciousness.keys())
        frequencies = [consciousness[w]['frequency'] for w in waves]
        coherences = [consciousness[w]['coherence'] for w in waves]
        amplitudes = [consciousness[w]['amplitude'] for w in waves]
        
        x = np.linspace(0, 2*np.pi, 1000)
        for i, wave in enumerate(waves):
            y = amplitudes[i] * np.sin(frequencies[i] * x / 1000) * coherences[i]
            ax3.plot(x, y + i*2, label=f"{wave.title()}: {frequencies[i]:.2f}Hz")
        
        ax3.set_title('Consciousness Waves')
        ax3.set_xlabel('Time')
        ax3.set_ylabel('Amplitude')
        ax3.legend()
        ax3.set_yticks([])
        
        # Plot 4: φ-Resonance visualization
        ax4 = fig.add_subplot(224, projection='polar')
        phi_angle = 2 * np.pi * result['phi_resonance']
        
        # Plot φ-resonance as vector
        ax4.plot([0, phi_angle], [0, 1], 'r-', linewidth=2)
        ax4.plot(phi_angle, 1, 'ro', markersize=10)
        
        # Plot perfect resonance markers (0 and 1)
        ax4.plot([0], [1], 'go', markersize=8, alpha=0.7)
        ax4.plot([2*np.pi], [1], 'go', markersize=8, alpha=0.7)
        
        # Add φ-harmonic markers
        for i in range(1, 6):
            phi_harmonic = 2 * np.pi * (float(self.phi) * i % 1)
            ax4.plot(phi_harmonic, 0.8, 'bo', markersize=6, alpha=0.5)
            ax4.text(phi_harmonic, 0.85, f"φ{i}", fontsize=8, 
                    ha='center', va='center', alpha=0.7)
        
        ax4.set_title('φ-Resonance')
        ax4.set_rticks([0.5, 1.0])
        ax4.set_rlabel_position(0)
        
        # Add overall title
        plt.suptitle(f"Quantum Collision Analysis - {result['timestamp']}", fontsize=16)
        plt.tight_layout(rect=[0, 0, 1, 0.96])
        
        # Save if path provided
        if save_path:
            plt.savefig(save_path)
            print(f"Visualization saved to {save_path}")
        
        return fig
    
    def run_collision_series(self, count=5, visualize=True):
        """Run a series of quantum collisions"""
        results = []
        
        for i in range(count):
            print(f"\nRunning Quantum Collision {i+1}/{count}")
            print("=" * 50)
            
            # Simulate collision
            result = self.simulate_collision()
            results.append(result)
            
            # Display results
            print(f"\nCollision Elements: {', '.join(result['elements'])}")
            print(f"Total Mass: {result['total_mass']:.4f} u")
            print(f"Total Atomic Number: {result['total_number']}")
            print(f"Collision Energy: {result['energy']:.2e} φ-units")
            print(f"φ-Resonance: {result['phi_resonance']:.6f}")
            
            # Check for new element
            if result['new_element']:
                print(f"\n🌟 NEW ELEMENT DISCOVERED! 🌟")
                print(f"Symbol: {result['new_element']['symbol']}")
                print(f"Name: {result['new_element']['name']}")
                print(f"Atomic Number: {result['new_element']['number']}")
                print(f"Mass: {result['new_element']['mass']:.4f}")
                print(f"φ-Resonance: {result['new_element']['phi_resonance']:.6f}")
                print(f"Parent Elements: {', '.join(result['new_element']['parents'])}")
            
            # Visualize if requested
            if visualize:
                save_path = os.path.join(self.results_dir, f"collision_{result['timestamp']}.png")
                self.visualize_collision(result, save_path)
                plt.close()  # Close to avoid memory issues
            
            # Pause between collisions
            if i < count - 1:
                print("\nPreparing next collision...")
                print("=" * 50)
        
        return results

def main():
    # Create quantum collision system
    system = QuantumCollisionEvolution()
    
    # Run collision series with more collisions to increase discovery chance
    results = system.run_collision_series(count=5)
    
    # Display summary
    print("\n" + "=" * 50)
    print("QUANTUM COLLISION SERIES SUMMARY")
    print("=" * 50)
    
    print(f"\nTotal Collisions: {len(results)}")
    print(f"New Elements Discovered: {len(system.discovered_elements)}")
    
    if system.discovered_elements:
        print("\nDiscovered Elements:")
        for symbol, data in system.discovered_elements.items():
            print(f"{symbol}: {data['name']} (Z={data['number']}, Mass={data['mass']:.4f})")
    
    print("\nResults saved to:", system.results_dir)

if __name__ == "__main__":
    main()
