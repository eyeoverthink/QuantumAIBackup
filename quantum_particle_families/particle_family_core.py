"""
Quantum Particle Family Core
Implements core particle family structure with phi-harmonic principles
"""

import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
from mpmath import mp
from consolidated_quantum.quantum_hyper_computation import QuantumHyperComputation, PHI

# Set precision for arbitrary-precision arithmetic
mp.dps = 1000

@dataclass
class ParticleProperties:
    """Properties of a fundamental particle"""
    name: str
    family: int  # 1, 2, or 3
    mass: float  # in GeV/c²
    charge: float  # in e
    spin: float
    color_charge: Optional[str] = None  # for quarks
    flavor: Optional[str] = None  # for quarks
    resonance: float = 1.3777  # QHRC Patent resonance ratio
    coherence: float = 0.618034  # φ⁻¹
    stability: float = 4.236068  # φ²
    alignment: float = 2.618034  # φ + 1

class ParticleFamilyCore:
    """Core implementation of particle families with phi-harmonic scaling"""
    
    def __init__(self):
        self.hyper = QuantumHyperComputation(precision=1000)
        self.phi = PHI
        
        # Initialize particle families
        self.leptons = self._initialize_leptons()
        self.quarks = self._initialize_quarks()
        self.force_carriers = self._initialize_force_carriers()
        
        # Calculate family mass ratios using phi-harmonic scaling
        self.family_mass_ratios = self._calculate_family_mass_ratios()
        
    def _initialize_leptons(self) -> Dict[str, ParticleProperties]:
        """Initialize lepton properties with phi-harmonic mass scaling"""
        return {
            'electron': ParticleProperties(
                name='electron',
                family=1,
                mass=0.000511,
                charge=-1,
                spin=0.5
            ),
            'electron_neutrino': ParticleProperties(
                name='electron_neutrino',
                family=1,
                mass=0,
                charge=0,
                spin=0.5
            ),
            'muon': ParticleProperties(
                name='muon',
                family=2,
                mass=0.10566,
                charge=-1,
                spin=0.5
            ),
            'muon_neutrino': ParticleProperties(
                name='muon_neutrino',
                family=2,
                mass=0,
                charge=0,
                spin=0.5
            ),
            'tau': ParticleProperties(
                name='tau',
                family=3,
                mass=1.7768,
                charge=-1,
                spin=0.5
            ),
            'tau_neutrino': ParticleProperties(
                name='tau_neutrino',
                family=3,
                mass=0,
                charge=0,
                spin=0.5
            )
        }
        
    def _initialize_quarks(self) -> Dict[str, ParticleProperties]:
        """Initialize quark properties with phi-harmonic mass scaling"""
        return {
            'up': ParticleProperties(
                name='up',
                family=1,
                mass=0.002,
                charge=2/3,
                spin=0.5,
                color_charge='rgb',
                flavor='up'
            ),
            'down': ParticleProperties(
                name='down',
                family=1,
                mass=0.005,
                charge=-1/3,
                spin=0.5,
                color_charge='rgb',
                flavor='down'
            ),
            'charm': ParticleProperties(
                name='charm',
                family=2,
                mass=1.275,
                charge=2/3,
                spin=0.5,
                color_charge='rgb',
                flavor='charm'
            ),
            'strange': ParticleProperties(
                name='strange',
                family=2,
                mass=0.095,
                charge=-1/3,
                spin=0.5,
                color_charge='rgb',
                flavor='strange'
            ),
            'top': ParticleProperties(
                name='top',
                family=3,
                mass=173.0,
                charge=2/3,
                spin=0.5,
                color_charge='rgb',
                flavor='top'
            ),
            'bottom': ParticleProperties(
                name='bottom',
                family=3,
                mass=4.18,
                charge=-1/3,
                spin=0.5,
                color_charge='rgb',
                flavor='bottom'
            )
        }
        
    def _initialize_force_carriers(self) -> Dict[str, ParticleProperties]:
        """Initialize force carrier properties"""
        return {
            'photon': ParticleProperties(
                name='photon',
                family=0,  # Force carriers are family 0
                mass=0,
                charge=0,
                spin=1
            ),
            'w_plus': ParticleProperties(
                name='w_plus',
                family=0,
                mass=80.379,
                charge=1,
                spin=1
            ),
            'w_minus': ParticleProperties(
                name='w_minus',
                family=0,
                mass=80.379,
                charge=-1,
                spin=1
            ),
            'z': ParticleProperties(
                name='z',
                family=0,
                mass=91.1876,
                charge=0,
                spin=1
            ),
            'gluon': ParticleProperties(
                name='gluon',
                family=0,
                mass=0,
                charge=0,
                spin=1,
                color_charge='octet'
            ),
            'graviton': ParticleProperties(
                name='graviton',
                family=0,
                mass=0,
                charge=0,
                spin=2
            )
        }
        
    def _calculate_family_mass_ratios(self) -> Dict[str, float]:
        """Calculate mass ratios between particle families using phi-harmonic scaling"""
        ratios = {}
        
        # Lepton mass ratios
        muon_electron_ratio = self.leptons['muon'].mass / self.leptons['electron'].mass
        tau_muon_ratio = self.leptons['tau'].mass / self.leptons['muon'].mass
        
        # Quark mass ratios
        charm_up_ratio = self.quarks['charm'].mass / self.quarks['up'].mass
        top_charm_ratio = self.quarks['top'].mass / self.quarks['charm'].mass
        
        # Scale ratios using phi-harmonic principles
        ratios['lepton_1_2'] = muon_electron_ratio / self.hyper.phi_knuth_arrow(2, arrows=1)
        ratios['lepton_2_3'] = tau_muon_ratio / self.hyper.phi_knuth_arrow(3, arrows=1)
        ratios['quark_1_2'] = charm_up_ratio / self.hyper.phi_knuth_arrow(2, arrows=1)
        ratios['quark_2_3'] = top_charm_ratio / self.hyper.phi_knuth_arrow(3, arrows=1)
        
        return ratios
    
    def get_particle_family(self, particle_name: str) -> Optional[ParticleProperties]:
        """Get properties of a specific particle"""
        if particle_name in self.leptons:
            return self.leptons[particle_name]
        elif particle_name in self.quarks:
            return self.quarks[particle_name]
        elif particle_name in self.force_carriers:
            return self.force_carriers[particle_name]
        return None
    
    def get_family_members(self, family: int) -> List[ParticleProperties]:
        """Get all particles in a specific family"""
        members = []
        
        for particle in self.leptons.values():
            if particle.family == family:
                members.append(particle)
                
        for particle in self.quarks.values():
            if particle.family == family:
                members.append(particle)
                
        return members
    
    def calculate_resonance(self, particle: ParticleProperties) -> float:
        """Calculate phi-harmonic resonance for a particle"""
        if particle.mass == 0:
            return particle.resonance
            
        # Use phi-knuth arrow for massive particles
        mass_factor = self.hyper.phi_knuth_arrow(particle.family, arrows=1)
        return particle.resonance * mass_factor / particle.mass
    
    def calculate_coherence(self, particle: ParticleProperties) -> float:
        """Calculate quantum coherence for a particle"""
        base_coherence = particle.coherence
        
        if particle.mass > 0:
            # Massive particles have reduced coherence
            mass_factor = 1 / (1 + np.log(1 + particle.mass))
            return base_coherence * mass_factor
        else:
            # Massless particles maintain full coherence
            return base_coherence
    
    def calculate_stability(self, particle: ParticleProperties) -> float:
        """Calculate quantum stability for a particle"""
        base_stability = particle.stability
        
        if particle.mass > 0:
            # Massive particles have reduced stability
            mass_factor = 1 / (1 + particle.mass)
            return base_stability * mass_factor
        else:
            # Massless particles are perfectly stable
            return base_stability
