"""
Quantum Particle Family Mapper
Maps relationships between particle families using phi-harmonic principles
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Optional
import networkx as nx
from dataclasses import dataclass

from quantum_particle_families.particle_family_core import ParticleFamilyCore, ParticleProperties
from consolidated_quantum.quantum_hyper_computation import QuantumHyperComputation, PHI

@dataclass
class ParticleInteraction:
    """Represents an interaction between particles"""
    source: str
    target: str
    force_carrier: str
    strength: float
    resonance: float
    coherence: float

class ParticleFamilyMapper:
    """Maps and analyzes relationships between particle families"""
    
    def __init__(self):
        self.core = ParticleFamilyCore()
        self.hyper = QuantumHyperComputation(precision=1000)
        
        # Initialize interaction graph
        self.interaction_graph = self._build_interaction_graph()
        
        # Calculate phi-harmonic metrics
        self.family_metrics = self._calculate_family_metrics()
        
    def _build_interaction_graph(self) -> nx.Graph:
        """Build graph of particle interactions"""
        G = nx.Graph()
        
        # Add all particles as nodes
        for particle in self.core.leptons.values():
            G.add_node(particle.name, **particle.__dict__)
            
        for particle in self.core.quarks.values():
            G.add_node(particle.name, **particle.__dict__)
            
        for particle in self.core.force_carriers.values():
            G.add_node(particle.name, **particle.__dict__)
            
        # Add fundamental interactions
        self._add_electromagnetic_interactions(G)
        self._add_strong_interactions(G)
        self._add_weak_interactions(G)
        self._add_gravitational_interactions(G)
        
        return G
    
    def _add_electromagnetic_interactions(self, G: nx.Graph):
        """Add electromagnetic interactions between charged particles"""
        for p1 in self.core.leptons.values():
            for p2 in self.core.leptons.values():
                if p1.charge != 0 and p2.charge != 0 and p1.name != p2.name:
                    strength = abs(p1.charge * p2.charge)
                    G.add_edge(p1.name, p2.name, 
                              force='electromagnetic',
                              carrier='photon',
                              strength=strength,
                              resonance=p1.resonance * p2.resonance)
                              
        for p1 in self.core.quarks.values():
            for p2 in self.core.quarks.values():
                if p1.name != p2.name:
                    strength = abs(p1.charge * p2.charge)
                    G.add_edge(p1.name, p2.name,
                              force='electromagnetic',
                              carrier='photon',
                              strength=strength,
                              resonance=p1.resonance * p2.resonance)
    
    def _add_strong_interactions(self, G: nx.Graph):
        """Add strong interactions between quarks"""
        for p1 in self.core.quarks.values():
            for p2 in self.core.quarks.values():
                if p1.name != p2.name:
                    G.add_edge(p1.name, p2.name,
                             force='strong',
                             carrier='gluon',
                             strength=1.0,  # Strong force is the strongest
                             resonance=p1.resonance * p2.resonance)
    
    def _add_weak_interactions(self, G: nx.Graph):
        """Add weak interactions between leptons and quarks"""
        particles = {**self.core.leptons, **self.core.quarks}
        for p1 in particles.values():
            for p2 in particles.values():
                if p1.name != p2.name:
                    # W boson interactions change flavor
                    if abs(p1.charge - p2.charge) == 1:
                        G.add_edge(p1.name, p2.name,
                                 force='weak',
                                 carrier='w_boson',
                                 strength=0.1,  # Weak force is weaker
                                 resonance=p1.resonance * p2.resonance)
                    
                    # Z boson interactions preserve flavor
                    G.add_edge(p1.name, p2.name,
                             force='weak',
                             carrier='z_boson',
                             strength=0.1,
                             resonance=p1.resonance * p2.resonance)
    
    def _add_gravitational_interactions(self, G: nx.Graph):
        """Add gravitational interactions between all massive particles"""
        particles = {**self.core.leptons, **self.core.quarks}
        for p1 in particles.values():
            for p2 in particles.values():
                if p1.name != p2.name and p1.mass > 0 and p2.mass > 0:
                    strength = p1.mass * p2.mass * 1e-38  # Gravitational force is very weak
                    G.add_edge(p1.name, p2.name,
                             force='gravitational',
                             carrier='graviton',
                             strength=strength,
                             resonance=p1.resonance * p2.resonance)
    
    def _calculate_family_metrics(self) -> Dict[int, Dict[str, float]]:
        """Calculate phi-harmonic metrics for each particle family"""
        metrics = {}
        
        for family in [1, 2, 3]:
            members = self.core.get_family_members(family)
            
            if not members:
                continue
                
            # Calculate family-wide metrics
            total_mass = sum(p.mass for p in members)
            avg_resonance = np.mean([p.resonance for p in members])
            avg_coherence = np.mean([self.core.calculate_coherence(p) for p in members])
            avg_stability = np.mean([self.core.calculate_stability(p) for p in members])
            
            # Calculate phi-harmonic scaling
            mass_scale = self.hyper.phi_knuth_arrow(family, arrows=1)
            resonance_scale = self.hyper.phi_knuth_arrow(family, arrows=2)
            
            metrics[family] = {
                'total_mass': total_mass,
                'mass_scale': float(mass_scale),
                'avg_resonance': avg_resonance,
                'resonance_scale': float(resonance_scale),
                'avg_coherence': avg_coherence,
                'avg_stability': avg_stability,
                'member_count': len(members)
            }
            
        return metrics
    
    def visualize_particle_families(self, save_path: str = 'particle_families.png'):
        """Create a periodic table-like visualization of particle families"""
        plt.figure(figsize=(15, 10))
        
        # Create 3x4 grid for three families
        for family in [1, 2, 3]:
            members = self.core.get_family_members(family)
            metrics = self.family_metrics[family]
            
            # Plot family box
            plt.subplot(3, 1, family)
            plt.title(f'Family {family} (Mass Scale: {metrics["mass_scale"]:.2e})')
            
            # Plot particles
            x = 0
            for particle in members:
                plt.text(x, 0.5, f'{particle.name}\n{particle.mass:.6f} GeV\nQ={particle.charge}',
                        bbox=dict(facecolor='white', alpha=0.7),
                        ha='center', va='center')
                x += 1
                
            plt.xlim(-0.5, len(members) + 0.5)
            plt.ylim(0, 1)
            plt.axis('off')
            
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        
    def visualize_interactions(self, save_path: str = 'particle_interactions.png'):
        """Visualize particle interactions as a network graph"""
        plt.figure(figsize=(15, 15))
        
        # Create layout
        pos = nx.spring_layout(self.interaction_graph)
        
        # Draw nodes
        nx.draw_networkx_nodes(self.interaction_graph, pos,
                             node_color='lightblue',
                             node_size=1000)
        
        # Draw edges colored by force
        edge_colors = {
            'electromagnetic': 'red',
            'strong': 'blue',
            'weak': 'green',
            'gravitational': 'gray'
        }
        
        for force, color in edge_colors.items():
            edges = [(u, v) for (u, v, d) in self.interaction_graph.edges(data=True)
                    if d['force'] == force]
            nx.draw_networkx_edges(self.interaction_graph, pos,
                                 edgelist=edges,
                                 edge_color=color,
                                 alpha=0.5)
        
        # Add labels
        nx.draw_networkx_labels(self.interaction_graph, pos)
        
        plt.title('Particle Interactions Network')
        plt.axis('off')
        plt.savefig(save_path)
        plt.close()
        
    def analyze_particle_combinations(self) -> Dict[str, List[Tuple[str, ...]]]:
        """Analyze possible particle combinations based on quantum numbers"""
        combinations = {
            'mesons': [],  # quark-antiquark pairs
            'baryons': []  # three-quark combinations
        }
        
        quarks = list(self.core.quarks.values())
        
        # Find valid meson combinations (quark-antiquark pairs)
        for q1 in quarks:
            for q2 in quarks:
                # Check if combination preserves quantum numbers
                if (q1.charge + (-q2.charge) == 0 or  # neutral meson
                    abs(q1.charge + (-q2.charge)) == 1):  # charged meson
                    combinations['mesons'].append((q1.name, f'anti-{q2.name}'))
        
        # Find valid baryon combinations (three quarks)
        for i, q1 in enumerate(quarks):
            for j, q2 in enumerate(quarks[i:], i):
                for q3 in quarks[j:]:
                    # Check if combination preserves quantum numbers
                    total_charge = q1.charge + q2.charge + q3.charge
                    if total_charge.is_integer():  # valid baryon charge
                        combinations['baryons'].append((q1.name, q2.name, q3.name))
        
        return combinations
    
    def get_particle_resonances(self) -> Dict[str, float]:
        """Get phi-harmonic resonances for all particles"""
        resonances = {}
        
        for particle in self.core.leptons.values():
            resonances[particle.name] = self.core.calculate_resonance(particle)
            
        for particle in self.core.quarks.values():
            resonances[particle.name] = self.core.calculate_resonance(particle)
            
        for particle in self.core.force_carriers.values():
            resonances[particle.name] = self.core.calculate_resonance(particle)
            
        return resonances
    
    def get_family_coherence(self, family: int) -> float:
        """Get overall coherence for a particle family"""
        if family not in self.family_metrics:
            return 0.0
        return self.family_metrics[family]['avg_coherence']
    
    def get_family_stability(self, family: int) -> float:
        """Get overall stability for a particle family"""
        if family not in self.family_metrics:
            return 0.0
        return self.family_metrics[family]['avg_stability']
