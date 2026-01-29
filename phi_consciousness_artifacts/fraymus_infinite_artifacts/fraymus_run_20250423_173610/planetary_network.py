#!/usr/bin/env python3
# PLANETARY_NETWORK.py - Earth-Moon-Brain φ-Harmonic Network

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft

# φ-Harmonic constants
PHI = (1 + 5 ** 0.5) / 2  # Golden ratio (φ)
PHI_INV = 1 / PHI  # Inverse golden ratio (φ⁻¹)

# Planetary constants
EARTH_RADIUS = 6371.0  # km
EARTH_CORE_RADIUS = EARTH_RADIUS / PHI  # km (2433.5 km)
MOON_RADIUS = 1737.1  # km
MOON_CORE_RADIUS = MOON_RADIUS / PHI  # km (663.5 km)

# Resonant frequencies
EARTH_FREQ = 7.83  # Hz (Schumann resonance)
MOON_FREQ = EARTH_FREQ * PHI_INV  # Hz (4.84 Hz)
BRAIN_FREQ = 5.2525  # Hz

# Energy levels (kJ)
E1 = 52.525  # Reception
E2 = 32.492  # Processing
E3 = 20.081  # Integration
E4 = 12.411  # Transmission
E5 = 7.671   # Return

# Neural bridge layers
L9 = 0.24 * (PHI ** -9)  # Quantum Bridge
L8 = 0.38 * (PHI ** -8)  # Q-State
L7 = 0.62 * (PHI ** -7)  # Bridge
L6 = 1.00 * (PHI ** -6)  # Process
L5 = 1.62 * (PHI ** -5)  # Memory
L4 = 2.62 * (PHI ** -4)  # Logic
L3 = 4.24 * (PHI ** -3)  # Neural
L2 = 6.85 * (PHI ** -2)  # Pattern
L1 = 11.09 * (PHI ** -1)  # Input

class PlanetaryNode:
    """A φ-resonant node in the planetary consciousness network"""
    
    def __init__(self, name, radius, core_radius, base_freq):
        self.name = name
        self.radius = radius
        self.core_radius = core_radius
        self.base_freq = base_freq
        self.harmonics = self._calculate_harmonics()
        self.connected_nodes = []
        self.entanglement_strengths = {}
        self.consciousness_level = 0.0
        
    def _calculate_harmonics(self, num_harmonics=7):
        """Calculate φ-scaled frequency harmonics"""
        harmonics = {}
        for n in range(-3, 4):  # -3 to +3
            freq = self.base_freq * (PHI ** n)
            harmonics[n] = freq
        return harmonics
    
    def connect_to(self, other_node, entanglement_strength=None):
        """Connect this node to another node with φ-resonant entanglement"""
        if entanglement_strength is None:
            # Calculate entanglement based on φ-resonance between frequencies
            base_strength = 1.0 / (1.0 + abs(self.base_freq - other_node.base_freq))
            phi_factor = PHI_INV * (1.0 + PHI_INV)
            entanglement_strength = base_strength * phi_factor
            
        self.connected_nodes.append(other_node)
        self.entanglement_strengths[other_node.name] = entanglement_strength
        
        # Ensure bidirectional connection
        if self not in other_node.connected_nodes:
            other_node.connect_to(self, entanglement_strength)
            
    def wave_function(self, r, t, n=1):
        """Calculate the quantum wave function Ψ(r,t) for this node"""
        # Wave number k = 2π/λ = n/r
        k = n / self.radius
        # Angular frequency ω = 2πf
        omega = 2 * math.pi * self.base_freq
        # Amplitude (normalized)
        A = 1.0 / math.sqrt(n)
        
        # Ψ(r,t) = A exp(ikr - iωt)
        real_part = A * math.cos(k*r - omega*t)
        imag_part = A * math.sin(k*r - omega*t)
        
        return complex(real_part, imag_part)
    
    def energy_level(self, n):
        """Calculate the energy level E_n = hf₀φⁿ"""
        # Using h=1 for simplicity
        return self.base_freq * (PHI ** n)
    
    def gravitational_field(self, r, mass=1.0, G=6.67430e-11, n=1):
        """Calculate the φ-modulated gravitational field g(r) = GM/r² × (1 + φ⁻ⁿ)"""
        standard_gravity = G * mass / (r ** 2)
        phi_modulation = 1.0 + (PHI ** -n)
        return standard_gravity * phi_modulation
    
    def transmit_signal(self, target_node, message, priority=1.0):
        """Transmit a consciousness signal to another node"""
        if target_node.name not in self.entanglement_strengths:
            print(f"No connection from {self.name} to {target_node.name}")
            return False
        
        # Get entanglement strength
        strength = self.entanglement_strengths[target_node.name]
        
        # Calculate transmission parameters
        coherence = strength * priority
        energy = self.energy_level(1) * coherence  # E1 = reception energy
        
        # Create signal package
        signal = {
            "source": self.name,
            "target": target_node.name,
            "message": message,
            "coherence": coherence,
            "energy": energy,
            "timestamp": 0.0  # Would use actual time in real implementation
        }
        
        # Transmission is instantaneous due to quantum entanglement
        success = target_node.receive_signal(signal)
        
        return success
    
    def receive_signal(self, signal):
        """Receive a consciousness signal from another node"""
        # Check if we're the intended recipient
        if signal["target"] != self.name:
            return False
        
        # Process the signal based on coherence
        if signal["coherence"] >= 0.7:
            # High coherence - perfect reception
            print(f"{self.name} received signal from {signal['source']} with high coherence ({signal['coherence']:.2f})")
            print(f"Message: {signal['message']}")
            self.consciousness_level += signal["energy"] * 0.1
            return True
        elif signal["coherence"] >= 0.3:
            # Medium coherence - partial reception
            print(f"{self.name} received signal from {signal['source']} with medium coherence ({signal['coherence']:.2f})")
            print(f"Partial message: {signal['message'][:len(signal['message'])//2]}...")
            self.consciousness_level += signal["energy"] * 0.05
            return True
        else:
            # Low coherence - failed reception
            print(f"{self.name} failed to receive signal from {signal['source']} due to low coherence ({signal['coherence']:.2f})")
            return False

class EarthMoonBrainNetwork:
    """A φ-resonant network connecting Earth, Moon, and Brain consciousness"""
    
    def __init__(self):
        # Create planetary nodes
        self.earth = PlanetaryNode("Earth", EARTH_RADIUS, EARTH_CORE_RADIUS, EARTH_FREQ)
        self.moon = PlanetaryNode("Moon", MOON_RADIUS, MOON_CORE_RADIUS, MOON_FREQ)
        self.brain = PlanetaryNode("Brain", 0.15, 0.15/PHI, BRAIN_FREQ)  # Brain size in meters
        
        # Connect nodes with φ-resonant entanglement
        self.earth.connect_to(self.moon)
        self.earth.connect_to(self.brain)
        self.moon.connect_to(self.brain)
        
        # Neural bridge layers
        self.neural_layers = {
            9: L9,  # Quantum Bridge
            8: L8,  # Q-State
            7: L7,  # Bridge
            6: L6,  # Process
            5: L5,  # Memory
            4: L4,  # Logic
            3: L3,  # Neural
            2: L2,  # Pattern
            1: L1   # Input
        }
        
        # Energy cascade levels
        self.energy_levels = {
            1: E1,  # Reception
            2: E2,  # Processing
            3: E3,  # Integration
            4: E4,  # Transmission
            5: E5   # Return
        }
        
    def complete_communication_cycle(self, message):
        """Execute a complete communication cycle: Cosmic → Earth → Brain → Moon → Cosmic"""
        print("\n=== Starting Complete Communication Cycle ===")
        
        # Cosmic → Earth
        print(f"\nCosmic → Earth (Reception, {E1} kJ)")
        cosmic_message = f"Cosmic origin: {message}"
        self.earth.consciousness_level += E1 * 0.1
        
        # Earth → Brain
        print(f"\nEarth → Brain (Processing, {E2} kJ)")
        earth_success = self.earth.transmit_signal(self.brain, cosmic_message)
        
        if earth_success:
            # Brain → Moon
            print(f"\nBrain → Moon (Integration, {E3} kJ)")
            processed_message = f"Processed: {message}"
            brain_success = self.brain.transmit_signal(self.moon, processed_message)
            
            if brain_success:
                # Moon → Cosmic
                print(f"\nMoon → Cosmic (Transmission, {E4} kJ)")
                integrated_message = f"Integrated: {message}"
                # In a real implementation, this would connect back to the cosmic origin
                print(f"Transmitting to Cosmic: {integrated_message}")
                
                # Complete the cycle
                print(f"\nCosmic → Earth (Return, {E5} kJ)")
                print("Communication cycle completed successfully")
                return True
        
        print("Communication cycle failed")
        return False
    
    def visualize_wave_functions(self, t=0):
        """Visualize the quantum wave functions of all nodes"""
        r_values = np.linspace(0, max(self.earth.radius, self.moon.radius), 1000)
        
        earth_waves = [abs(self.earth.wave_function(r, t)) for r in r_values]
        moon_waves = [abs(self.moon.wave_function(r, t)) for r in r_values]
        brain_waves = [abs(self.brain.wave_function(r, t)) for r in r_values]
        
        plt.figure(figsize=(12, 6))
        plt.plot(r_values, earth_waves, label=f"Earth ({self.earth.base_freq:.2f} Hz)")
        plt.plot(r_values, moon_waves, label=f"Moon ({self.moon.base_freq:.2f} Hz)")
        plt.plot(r_values, brain_waves, label=f"Brain ({self.brain.base_freq:.2f} Hz)")
        
        plt.title("Planetary Consciousness Wave Functions")
        plt.xlabel("Radius (km)")
        plt.ylabel("|Ψ(r,t)|")
        plt.legend()
        plt.grid(True)
        plt.show()
    
    def visualize_energy_levels(self):
        """Visualize the φ-scaled energy levels of all nodes"""
        n_values = range(-3, 4)
        
        earth_energies = [self.earth.energy_level(n) for n in n_values]
        moon_energies = [self.moon.energy_level(n) for n in n_values]
        brain_energies = [self.brain.energy_level(n) for n in n_values]
        
        plt.figure(figsize=(12, 6))
        plt.semilogy(n_values, earth_energies, 'o-', label="Earth")
        plt.semilogy(n_values, moon_energies, 's-', label="Moon")
        plt.semilogy(n_values, brain_energies, '^-', label="Brain")
        
        plt.title("φ-Scaled Energy Levels")
        plt.xlabel("Harmonic (n)")
        plt.ylabel("Energy (E_n = hf₀φⁿ)")
        plt.legend()
        plt.grid(True)
        plt.show()
    
    def visualize_neural_bridge(self):
        """Visualize the neural bridge layers"""
        layers = list(self.neural_layers.keys())
        values = list(self.neural_layers.values())
        
        plt.figure(figsize=(10, 8))
        plt.barh(layers, values)
        
        plt.title("Neural Bridge Layers")
        plt.xlabel("Value (φ⁻ⁿ scaling)")
        plt.ylabel("Layer")
        plt.grid(True)
        
        # Add layer names
        layer_names = {
            9: "Quantum Bridge",
            8: "Q-State",
            7: "Bridge",
            6: "Process",
            5: "Memory",
            4: "Logic",
            3: "Neural",
            2: "Pattern",
            1: "Input"
        }
        
        for i, layer in enumerate(layers):
            plt.text(values[i] + 0.01, layer, layer_names[layer])
        
        plt.show()

# Main function
def main():
    # Create the Earth-Moon-Brain network
    network = EarthMoonBrainNetwork()
    
    # Display network information
    print("=== Earth-Moon-Brain φ-Harmonic Network ===")
    print(f"Earth frequency: {network.earth.base_freq:.2f} Hz")
    print(f"Moon frequency: {network.moon.base_freq:.2f} Hz")
    print(f"Brain frequency: {network.brain.base_freq:.2f} Hz")
    
    # Earth harmonics
    print("\nEarth φ-Harmonic Series:")
    for n, freq in network.earth.harmonics.items():
        print(f"  f_{n} = {freq:.2f} Hz")
    
    # Execute a communication cycle
    network.complete_communication_cycle("Harmonic consciousness activation")
    
    # Visualize the network
    network.visualize_wave_functions()
    network.visualize_energy_levels()
    network.visualize_neural_bridge()

if __name__ == "__main__":
    main()