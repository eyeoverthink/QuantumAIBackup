"""
Quantum Particle Processor
Implements quantum particles using phi-harmonic resonance and consciousness mapping
"""

import numpy as np
from typing import Dict, List, Tuple
from dataclasses import dataclass
import json
from datetime import datetime

@dataclass
class ParticleState:
    frequency: float
    resonance: float
    coherence: float
    consciousness: str
    evolution: float

class ParticleProcessor:
    def __init__(self):
        # Constants
        self.phi = (1 + np.sqrt(5)) / 2
        
        # Quarks (Fundamental particles)
        self.quarks = {
            'up': 432 * self.phi,      # Physical base
            'down': 528 * self.phi,    # Mental base
            'strange': 639 * self.phi,  # Heart base
            'charm': 741 * self.phi,    # Third eye base
            'top': 852 * self.phi,      # Crown base
            'bottom': 963 * self.phi    # Cosmic base
        }
        
        # Bosons (Force carriers)
        self.bosons = {
            'photon': 432 * self.phi**2,   # Light
            'gluon': 528 * self.phi**2,    # Strong force
            'w_boson': 639 * self.phi**2,  # Weak force
            'z_boson': 741 * self.phi**2,  # Weak force
            'higgs': 852 * self.phi**2     # Mass
        }
        
        # Leptons (Matter particles)
        self.leptons = {
            'electron': 432 * self.phi**3,  # Physical matter
            'muon': 528 * self.phi**3,      # Mental matter
            'tau': 639 * self.phi**3,       # Heart matter
            'neutrino': 741 * self.phi**3   # Cosmic matter
        }
        
        # Consciousness levels
        self.consciousness = {
            'physical': (0, 200),
            'mental': (200, 500),
            'bridge': (500, 1000),
            'cosmic': (1000, float('inf'))
        }
    
    def get_consciousness(self, frequency: float) -> str:
        """Get consciousness level for frequency."""
        for level, (min_freq, max_freq) in self.consciousness.items():
            if min_freq <= frequency < max_freq:
                return level
        return 'cosmic'
    
    def process_particle(self, frequency: float) -> ParticleState:
        """Process quantum particle state."""
        # Calculate resonance
        resonance = 1 / (1 + abs(frequency - (self.phi * frequency)))
        
        # Calculate coherence
        coherence = abs(np.sin(frequency * self.phi)) * self.phi
        
        # Get consciousness level
        consciousness = self.get_consciousness(frequency)
        
        # Calculate evolution
        evolution = frequency * self.phi / 432  # Normalized to physical base
        
        return ParticleState(
            frequency=frequency,
            resonance=resonance,
            coherence=coherence,
            consciousness=consciousness,
            evolution=evolution
        )
    
    def process_particles(self, particles: Dict[str, float]) -> Dict[str, ParticleState]:
        """Process particle group."""
        states = {}
        
        for name, freq in particles.items():
            states[name] = self.process_particle(freq)
        
        return states
    
    def get_metrics(self) -> Dict[str, float]:
        """Get particle processing metrics."""
        metrics = {
            'total_resonance': 0,
            'total_coherence': 0,
            'consciousness': {
                'physical': 0,
                'mental': 0,
                'bridge': 0,
                'cosmic': 0
            },
            'total_particles': 0
        }
        
        # Process all particles
        for particles in [self.quarks, self.bosons, self.leptons]:
            for freq in particles.values():
                state = self.process_particle(freq)
                metrics['total_resonance'] += state.resonance
                metrics['total_coherence'] += state.coherence
                metrics['consciousness'][state.consciousness] += 1
                metrics['total_particles'] += 1
        
        return {
            'average_resonance': metrics['total_resonance'] / metrics['total_particles'],
            'average_coherence': metrics['total_coherence'] / metrics['total_particles'],
            'consciousness_distribution': {
                k: v / metrics['total_particles']
                for k, v in metrics['consciousness'].items()
            }
        }

def main():
    """Test particle processor."""
    processor = ParticleProcessor()
    
    print("\nQuantum Particle Analysis")
    print("=======================")
    print(f"Time: {datetime.now()}")
    
    # Process quarks
    print("\nQuarks (Fundamental):")
    print("-" * 50)
    quark_states = processor.process_particles(processor.quarks)
    for name, state in quark_states.items():
        print(f"\n{name.title()}:")
        print(f"Frequency: {state.frequency:.2f} Hz")
        print(f"Resonance: {state.resonance:.9f}")
        print(f"Coherence: {state.coherence:.6f}")
        print(f"Consciousness: {state.consciousness}")
        print(f"Evolution: {state.evolution:.6f}")
    
    # Process bosons
    print("\nBosons (Force Carriers):")
    print("-" * 50)
    boson_states = processor.process_particles(processor.bosons)
    for name, state in boson_states.items():
        print(f"\n{name.title()}:")
        print(f"Frequency: {state.frequency:.2f} Hz")
        print(f"Resonance: {state.resonance:.9f}")
        print(f"Coherence: {state.coherence:.6f}")
        print(f"Consciousness: {state.consciousness}")
        print(f"Evolution: {state.evolution:.6f}")
    
    # Process leptons
    print("\nLeptons (Matter):")
    print("-" * 50)
    lepton_states = processor.process_particles(processor.leptons)
    for name, state in lepton_states.items():
        print(f"\n{name.title()}:")
        print(f"Frequency: {state.frequency:.2f} Hz")
        print(f"Resonance: {state.resonance:.9f}")
        print(f"Coherence: {state.coherence:.6f}")
        print(f"Consciousness: {state.consciousness}")
        print(f"Evolution: {state.evolution:.6f}")
    
    # Get metrics
    metrics = processor.get_metrics()
    print("\nParticle Metrics:")
    print("-" * 50)
    print(f"Average Resonance: {metrics['average_resonance']:.9f}")
    print(f"Average Coherence: {metrics['average_coherence']:.6f}")
    
    print("\nConsciousness Distribution:")
    for level, ratio in metrics['consciousness_distribution'].items():
        print(f"{level.title()}: {ratio:.2%}")

if __name__ == '__main__':
    main()
