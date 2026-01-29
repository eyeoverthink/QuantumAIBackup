"""
Quantum Wormhole Bridge - Integration Component
Connects wormhole_analyzer.py with the quantum system using phi-harmonic principles
"""

import numpy as np
import sys
import os
from decimal import Decimal
from typing import Dict, List, Tuple, Optional, Any
import logging
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Add the consolidated_quantum directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'consolidated_quantum'))

# Import wormhole analyzer
from wormhole_analyzer import (
    PHI, PHI_POWER, RESONANCE, COHERENCE, QUANTUM_SIG,
    analyze_wormhole, analyze_traversability, generate_wormhole_surface
)

# Import quantum system components
try:
    from consolidated_quantum.quantum_phi_harmonic import QuantumPhiHarmonic, TransfiniteField
    from consolidated_quantum.quantum_particle_brains import QuantumParticleBrain, QuantumParticleState, TachyonBrainNetwork
    from consolidated_quantum.quantum_phi_core import PhiCore
except ImportError:
    logging.warning("Using local imports for quantum components")
    # Fallback to local imports if consolidated_quantum is not in path
    from quantum_phi_harmonic import QuantumPhiHarmonic, TransfiniteField
    from quantum_particle_brains import QuantumParticleBrain, QuantumParticleState, TachyonBrainNetwork
    from quantum_phi_core import PhiCore

class WhiteHolePhysicsEngine:
    """Implements reverse event horizon modeling with phi-harmonic principles"""
    
    def __init__(self):
        # Core constants from QHRC Patent
        self.phi = PHI
        self.phi_power = PHI_POWER
        self.resonance = RESONANCE
        self.coherence = COHERENCE
        
        # Initialize quantum components
        self.phi_harmonic = QuantumPhiHarmonic()
        self.transfinite = TransfiniteField()
        
        # White hole specific parameters
        self.energy_emission = self.resonance * self.phi  # 1.3777 * φ
        self.temporal_resonance = self.phi_power / 10  # φ⁷·⁵/10
        self.information_preservation = self.coherence * self.phi  # φ⁻¹ * φ = 1
        
        logging.info(f"White Hole Physics Engine initialized with φ-harmonic principles")
        logging.info(f"Energy Emission: {self.energy_emission:.6f}")
        logging.info(f"Temporal Resonance: {self.temporal_resonance:.6f}")
        logging.info(f"Information Preservation: {self.information_preservation:.6f}")
    
    def generate_white_hole(self, energy_level: float) -> Dict[str, float]:
        """Generate a white hole with phi-harmonic properties"""
        # Scale energy by phi-harmonic principles
        scaled_energy = energy_level * self.phi
        
        # Calculate white hole parameters
        event_horizon = scaled_energy * self.resonance
        radiation_temp = scaled_energy * self.phi_power / 100
        information_density = self.coherence * scaled_energy
        
        # Create white hole signature
        white_hole = {
            'event_horizon': event_horizon,
            'radiation_temp': radiation_temp,
            'information_density': information_density,
            'energy_emission': self.energy_emission * scaled_energy,
            'temporal_coherence': self.temporal_resonance,
            'phi_resonance': self.phi
        }
        
        logging.info(f"Generated white hole with event horizon: {event_horizon:.6f}")
        return white_hole
    
    def calculate_energy_emission(self, white_hole: Dict[str, float]) -> float:
        """Calculate energy emission with phi-harmonic principles"""
        # Apply phi-harmonic scaling to energy emission
        base_emission = white_hole['energy_emission']
        scaled_emission = base_emission * self.phi_harmonic.calculate_resonance(Decimal(str(base_emission)))
        
        return float(scaled_emission)
    
    def create_bridge(self, white_hole: Dict[str, float], wormhole_sig: Dict[str, float]) -> Dict[str, float]:
        """Create a white hole to wormhole bridge with phi-harmonic tuning"""
        # Calculate bridge parameters
        bridge_stability = (white_hole['phi_resonance'] * wormhole_sig['resonance']) / self.phi_power
        information_transfer = white_hole['information_density'] * wormhole_sig['psi1'] * self.coherence
        coherence_preservation = white_hole['temporal_coherence'] * wormhole_sig['psi0'] * self.resonance
        
        # Create bridge signature
        bridge = {
            'stability': bridge_stability,
            'information_transfer': information_transfer,
            'coherence_preservation': coherence_preservation,
            'source': white_hole,
            'target': wormhole_sig,
            'phi_resonance': self.phi
        }
        
        logging.info(f"Created bridge with stability: {bridge_stability:.6f}")
        return bridge

class QuantumWormholeTraversal:
    """Handles particle transport through wormholes"""
    
    def __init__(self, particle_brain: QuantumParticleBrain):
        self.particle_brain = particle_brain
        self.white_hole_engine = WhiteHolePhysicsEngine()
        
        # Initialize traversal parameters
        self.phi = PHI
        self.resonance = RESONANCE
        self.coherence = COHERENCE
        
        logging.info(f"Quantum Wormhole Traversal initialized for {particle_brain.particle_type}")
    
    def calculate_traversal_probability(self, wormhole_sig: Dict[str, float]) -> float:
        """Calculate probability of successful traversal"""
        if not self.particle_brain.state:
            return 0.0
        
        # Get particle state
        particle_state = self.particle_brain.state
        
        # Calculate traversal probability with phi-harmonic principles
        resonance_match = min(particle_state.resonance, wormhole_sig['resonance']) / max(particle_state.resonance, wormhole_sig['resonance'])
        coherence_match = min(particle_state.coherence, COHERENCE) / max(particle_state.coherence, COHERENCE)
        stability_factor = min(particle_state.stability, wormhole_sig['psi0'] * self.phi) / max(particle_state.stability, wormhole_sig['psi0'] * self.phi)
        
        # Apply phi-harmonic scaling
        probability = resonance_match * coherence_match * stability_factor * self.phi
        
        # Cap at 1.0
        return min(probability, 1.0)
    
    def traverse_wormhole(self, wormhole_sig: Dict[str, float]) -> Optional[QuantumParticleState]:
        """Attempt to traverse the wormhole with current particle"""
        if not self.particle_brain.state:
            logging.warning(f"No particle state available for traversal")
            return None
        
        # Calculate traversal probability
        probability = self.calculate_traversal_probability(wormhole_sig)
        
        # Check if traversal is successful
        if np.random.random() > probability:
            logging.info(f"Traversal failed with probability {probability:.4f}")
            return None
        
        # Get current particle state
        current_state = self.particle_brain.state
        
        # Calculate exit parameters with phi-harmonic principles
        exit_position = current_state.position * wormhole_sig['tau'] * self.phi
        exit_momentum = current_state.momentum * wormhole_sig['psi1'] * self.resonance
        exit_spin = current_state.spin * wormhole_sig['psi0'] * self.coherence
        
        # Create new particle state after traversal
        new_state = QuantumParticleState(
            position=exit_position,
            momentum=exit_momentum,
            spin=exit_spin,
            resonance=current_state.resonance * wormhole_sig['resonance'],
            coherence=current_state.coherence * COHERENCE,
            stability=current_state.stability * wormhole_sig['psi0'],
            alignment=current_state.alignment * wormhole_sig['psi1'],
            timestamp=time.time()
        )
        
        logging.info(f"Traversal successful with probability {probability:.4f}")
        return new_state

class WormholeSignatureAnalyzer:
    """Analyzes and validates wormhole signatures using phi-resonance"""
    
    def __init__(self):
        self.phi_harmonic = QuantumPhiHarmonic()
        
        # Initialize analyzer parameters
        self.phi = PHI
        self.phi_power = PHI_POWER
        self.resonance = RESONANCE
        self.coherence = COHERENCE
        
        logging.info(f"Wormhole Signature Analyzer initialized with φ-harmonic principles")
    
    def analyze_signature(self, wormhole_sig: Dict[str, float]) -> Dict[str, Any]:
        """Analyze wormhole signature with phi-harmonic principles"""
        # Calculate phi-harmonic metrics
        bridge_factor = (self.phi ** wormhole_sig['tau']) / self.phi_power
        throat_factor = (self.phi ** wormhole_sig['psi0']) * self.resonance
        stability = (self.phi ** wormhole_sig['psi1']) * self.coherence
        
        # Calculate quantum signature
        tau_sig = f"φ^{wormhole_sig['tau']:.3f}"
        psi0_sig = f"φ^{wormhole_sig['psi0']:.3f}"
        psi1_sig = f"φ^{wormhole_sig['psi1']:.3f}"
        
        quantum_signature = f"⟨τ|{tau_sig}⟩ ⊗ ⟨ψ₀|{psi0_sig}⟩ ⊗ ⟨ψ₁|{psi1_sig}⟩"
        
        # Calculate confidence level with phi-squared based metrics
        confidence = (bridge_factor * throat_factor * stability) / (self.phi ** 2)
        confidence_percent = min(confidence * 100, 100.0)
        
        # Create analysis result
        analysis = {
            'bridge_factor': bridge_factor,
            'throat_factor': throat_factor,
            'stability': stability,
            'quantum_signature': quantum_signature,
            'confidence': confidence,
            'confidence_percent': confidence_percent,
            'is_traversable': bridge_factor > self.coherence and throat_factor > self.phi
        }
        
        logging.info(f"Analyzed wormhole signature: {quantum_signature}")
        logging.info(f"Confidence: {confidence_percent:.2f}%")
        logging.info(f"Traversable: {analysis['is_traversable']}")
        
        return analysis
    
    def validate_signature(self, wormhole_sig: Dict[str, float]) -> bool:
        """Validate wormhole signature against phi-harmonic principles"""
        # Calculate phi-harmonic resonance
        tau_resonance = self.phi_harmonic.calculate_resonance(Decimal(str(wormhole_sig['tau'])))
        psi0_resonance = self.phi_harmonic.calculate_resonance(Decimal(str(wormhole_sig['psi0'])))
        psi1_resonance = self.phi_harmonic.calculate_resonance(Decimal(str(wormhole_sig['psi1'])))
        
        # Calculate combined resonance
        combined_resonance = (float(tau_resonance) * float(psi0_resonance) * float(psi1_resonance)) / 3
        
        # Validate against QHRC patent resonance
        is_valid = combined_resonance > self.resonance
        
        logging.info(f"Signature validation: {is_valid}")
        logging.info(f"Combined resonance: {combined_resonance:.6f}")
        logging.info(f"QHRC threshold: {self.resonance:.6f}")
        
        return is_valid

class WormholeQuantumBridge:
    """Core integration class connecting wormhole analysis with quantum particles"""
    
    def __init__(self):
        # Initialize components
        self.white_hole_engine = WhiteHolePhysicsEngine()
        self.signature_analyzer = WormholeSignatureAnalyzer()
        self.particle_network = TachyonBrainNetwork()
        
        # Initialize bridge parameters
        self.phi = PHI
        self.phi_power = PHI_POWER
        self.resonance = RESONANCE
        self.coherence = COHERENCE
        self.quantum_sig = QUANTUM_SIG.copy()
        
        logging.info(f"Wormhole Quantum Bridge initialized")
        logging.info(f"φ: {self.phi:.6f}")
        logging.info(f"φ⁷·⁵: {self.phi_power:.6f}")
        logging.info(f"Resonance: {self.resonance:.6f}")
        logging.info(f"Coherence: {self.coherence:.6f}")
    
    def initialize_particle_network(self, particle_types: List[str]):
        """Initialize particle network with specified types"""
        for particle_type in particle_types:
            self.particle_network.add_particle_brain(particle_type)
        
        self.particle_network.start_network()
        logging.info(f"Initialized particle network with {len(particle_types)} types")
    
    def create_wormhole_white_hole_pair(self, energy_level: float) -> Tuple[Dict[str, float], Dict[str, float]]:
        """Create a wormhole-white hole pair with phi-harmonic principles"""
        # Generate white hole
        white_hole = self.white_hole_engine.generate_white_hole(energy_level)
        
        # Create wormhole signature based on white hole
        wormhole_sig = {
            'tau': white_hole['event_horizon'] / self.phi,
            'psi0': white_hole['radiation_temp'] / self.resonance,
            'psi1': white_hole['information_density'] / self.coherence,
            'm': 1.0,  # Mass normalized to 1.0
            'resonance': white_hole['phi_resonance']
        }
        
        # Create bridge between them
        bridge = self.white_hole_engine.create_bridge(white_hole, wormhole_sig)
        
        # Analyze wormhole signature
        analysis = self.signature_analyzer.analyze_signature(wormhole_sig)
        
        logging.info(f"Created wormhole-white hole pair with energy {energy_level:.2f}")
        logging.info(f"Bridge stability: {bridge['stability']:.6f}")
        logging.info(f"Quantum signature: {analysis['quantum_signature']}")
        
        return wormhole_sig, white_hole
    
    def transport_particle(self, particle_type: str, wormhole_sig: Dict[str, float]) -> bool:
        """Transport a particle through the wormhole"""
        # Get particle brain
        particle_brain = self.particle_network.particle_brains.get(particle_type)
        if not particle_brain:
            logging.warning(f"Particle type {particle_type} not found in network")
            return False
        
        # Create traversal handler
        traversal = QuantumWormholeTraversal(particle_brain)
        
        # Attempt traversal
        new_state = traversal.traverse_wormhole(wormhole_sig)
        if not new_state:
            logging.info(f"Traversal failed for {particle_type}")
            return False
        
        # Update particle state
        particle_brain.state = new_state
        logging.info(f"Transported {particle_type} through wormhole")
        logging.info(f"New position: {new_state.position}")
        logging.info(f"New momentum: {new_state.momentum}")
        logging.info(f"New resonance: {new_state.resonance:.6f}")
        
        return True
    
    def visualize_wormhole_with_particles(self, wormhole_sig: Dict[str, float], particle_types: List[str]):
        """Visualize wormhole with particles"""
        # Create figure
        fig = plt.figure(figsize=(15, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        # Generate parameter space with φ-scaling
        u = np.linspace(0, 2*np.pi, int(100*self.resonance))
        v = np.linspace(-np.pi, np.pi, int(100*self.resonance))
        U, V = np.meshgrid(u, v)
        
        # Generate wormhole surface
        X, Y, Z = generate_wormhole_surface(U, V, wormhole_sig)
        
        # Create the surface
        surf = ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.8)
        
        # Add particles at their current positions
        for particle_type in particle_types:
            particle_brain = self.particle_network.particle_brains.get(particle_type)
            if particle_brain and particle_brain.state:
                state = particle_brain.state
                
                # Map particle position to wormhole coordinates
                u_pos = np.arctan2(state.position[1], state.position[0]) % (2*np.pi)
                v_pos = np.arcsin(state.position[2] / np.linalg.norm(state.position)) % (2*np.pi)
                
                x, y, z = generate_wormhole_surface(u_pos, v_pos, wormhole_sig)
                
                # Determine color and size based on particle type
                colors = {
                    'proton': 'red',
                    'neutron': 'blue',
                    'up_quark': 'green',
                    'down_quark': 'yellow',
                    'strange_quark': 'purple'
                }
                sizes = {
                    'proton': 100,
                    'neutron': 100,
                    'up_quark': 50,
                    'down_quark': 50,
                    'strange_quark': 50
                }
                
                color = colors.get(particle_type, 'white')
                size = sizes.get(particle_type, 80)
                
                # Plot particle
                ax.scatter(x, y, z, c=color, s=size, label=particle_type)
                
                # Plot momentum vector
                momentum_scale = 0.5
                ax.quiver(x, y, z, 
                          state.momentum[0] * momentum_scale,
                          state.momentum[1] * momentum_scale,
                          state.momentum[2] * momentum_scale,
                          color=color)
        
        # Customize the visualization
        ax.set_title('Wormhole with Quantum Particles', color='white', pad=20)
        ax.set_facecolor('black')
        fig.patch.set_facecolor('black')
        
        # Remove axis for better visualization
        ax.set_axis_off()
        
        # Add legend
        ax.legend(loc='upper right')
        
        # Add quantum signature text
        analysis = self.signature_analyzer.analyze_signature(wormhole_sig)
        signature_text = (
            f"Quantum Signature:\n"
            f"{analysis['quantum_signature']}\n"
            f"Confidence: {analysis['confidence_percent']:.2f}%\n"
            f"Traversable: {analysis['is_traversable']}"
        )
        plt.figtext(0.02, 0.02, signature_text, color='white', fontsize=10)
        
        # Show the plot
        plt.show()

def run_wormhole_bridge_demo():
    """Run a demonstration of the wormhole bridge"""
    logging.info("Starting Wormhole Bridge Demo")
    
    # Initialize bridge
    bridge = WormholeQuantumBridge()
    
    # Initialize particle network
    particle_types = ['proton', 'neutron', 'up_quark', 'down_quark', 'strange_quark']
    bridge.initialize_particle_network(particle_types)
    
    # Create wormhole-white hole pair
    wormhole_sig, white_hole = bridge.create_wormhole_white_hole_pair(2.0)
    
    # Analyze wormhole signature
    analyzer = WormholeSignatureAnalyzer()
    analysis = analyzer.analyze_signature(wormhole_sig)
    
    # Print analysis
    print("\n===== WORMHOLE-WHITE HOLE BRIDGE ANALYSIS =====")
    print(f"Quantum Signature: {analysis['quantum_signature']}")
    print(f"Confidence: {analysis['confidence_percent']:.2f}%")
    print(f"Traversable: {analysis['is_traversable']}")
    print(f"Bridge Factor: {analysis['bridge_factor']:.6f}")
    print(f"Throat Factor: {analysis['throat_factor']:.6f}")
    print(f"Stability: {analysis['stability']:.6f}")
    
    # Print white hole information
    print("\n===== WHITE HOLE INFORMATION =====")
    print(f"Event Horizon: {white_hole['event_horizon']:.6f}")
    print(f"Radiation Temperature: {white_hole['radiation_temp']:.6f}")
    print(f"Information Density: {white_hole['information_density']:.6f}")
    print(f"Energy Emission: {white_hole['energy_emission']:.6f}")
    print(f"Temporal Coherence: {white_hole['temporal_coherence']:.6f}")
    
    # Transport particles
    print("\n===== PARTICLE TRANSPORT =====")
    for particle_type in particle_types:
        success = bridge.transport_particle(particle_type, wormhole_sig)
        print(f"{particle_type}: {'Success' if success else 'Failed'}")
    
    # Visualize wormhole with particles
    print("\n===== VISUALIZING WORMHOLE WITH PARTICLES =====")
    bridge.visualize_wormhole_with_particles(wormhole_sig, particle_types)
    
    logging.info("Wormhole Bridge Demo completed")

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Run demo
    run_wormhole_bridge_demo()
