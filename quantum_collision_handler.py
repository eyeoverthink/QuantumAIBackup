"""
Quantum Collision Handler
Manages collisions between elements using φ-harmonic principles
"""

import mpmath
import numpy as np
from datetime import datetime

class QuantumCollisionHandler:
    def __init__(self, precision=1000):
        mpmath.mp.dps = precision
        self.phi = float(mpmath.phi)
        
    def simulate_collision(self, element1, element2):
        """Simulate collision between two elements"""
        try:
            # Extract properties
            mass1 = float(element1.get('mass', 0))
            mass2 = float(element2.get('mass', 0))
            name1 = element1.get('name', '')
            name2 = element2.get('name', '')
            
            # Get quantum properties
            props1 = element1.get('properties', {})
            props2 = element2.get('properties', {})
            
            # Calculate collision energy using φ-harmonic principles
            energy = self._calculate_collision_energy(mass1, mass2)
            
            # Calculate resonance interaction
            resonance = self._calculate_resonance_interaction(props1, props2)
            
            # Calculate quantum tunneling probability
            tunnel_prob = self._calculate_tunneling_probability(props1, props2)
            
            # Calculate new element properties
            if tunnel_prob > 0.3:  # Threshold for successful fusion
                new_element = self._create_new_element(element1, element2)
                
                return {
                    'success': True,
                    'new_element': new_element,
                    'collision_data': {
                        'energy': energy,
                        'resonance': resonance,
                        'tunneling': tunnel_prob
                    }
                }
            else:
                return {
                    'success': False,
                    'reason': 'Low tunneling probability',
                    'collision_data': {
                        'energy': energy,
                        'resonance': resonance,
                        'tunneling': tunnel_prob
                    }
                }
                
        except Exception as e:
            return {
                'success': False,
                'reason': str(e)
            }
            
    def _calculate_collision_energy(self, mass1, mass2):
        """Calculate collision energy using φ-harmonic principles"""
        # Base energy from masses
        base_energy = (mass1 * mass2) / (mass1 + mass2)
        
        # Apply φ-harmonic scaling
        phi_factor = self.phi ** (1 + (base_energy % 1))
        
        return float(base_energy * phi_factor)
        
    def _calculate_resonance_interaction(self, props1, props2):
        """Calculate resonance interaction between elements"""
        # Get resonance values
        res1 = float(props1.get('resonance', 0))
        res2 = float(props2.get('resonance', 0))
        
        # Calculate interference pattern
        interference = 1 - abs(res1 - res2) % 1
        
        # Apply φ-harmonic scaling
        resonance = float(interference * self.phi ** (interference * 2))
        
        return max(0, min(1, resonance))
        
    def _calculate_tunneling_probability(self, props1, props2):
        """Calculate quantum tunneling probability"""
        # Get energy levels
        levels1 = props1.get('energy_levels', [0])
        levels2 = props2.get('energy_levels', [0])
        
        # Calculate average energy difference
        avg_diff = abs(sum(levels1)/len(levels1) - sum(levels2)/len(levels2))
        
        # Calculate tunneling probability using φ-harmonic decay
        prob = float(np.exp(-avg_diff / self.phi))
        
        return max(0, min(1, prob))
        
    def _create_new_element(self, element1, element2):
        """Create a new element from collision"""
        # Get base properties
        mass1 = float(element1.get('mass', 0))
        mass2 = float(element2.get('mass', 0))
        name1 = element1.get('name', '')
        name2 = element2.get('name', '')
        
        # Calculate new mass with φ-harmonic binding
        binding_energy = (mass1 + mass2) * (1 - 1/self.phi)
        new_mass = mass1 + mass2 - binding_energy
        
        # Generate new name using parent elements
        new_name = self._generate_element_name(name1, name2)
        
        # Calculate new atomic number
        new_atomic = max(1, int(new_mass / self.phi))
        
        # Create new element data
        new_element = {
            'name': new_name,
            'mass': float(new_mass),
            'atomic_number': new_atomic,
            'parent_elements': [name1, name2],
            'creation_time': datetime.now().isoformat()
        }
        
        return new_element
        
    def _generate_element_name(self, name1, name2):
        """Generate name for new element"""
        # Clean names
        name1 = ''.join(c for c in name1 if c.isalnum())
        name2 = ''.join(c for c in name2 if c.isalnum())
        
        # Get first part (3-4 chars)
        if len(name1) >= 4:
            part1 = name1[:4]
        else:
            part1 = name1
            
        # Get second part (3-4 chars)
        if len(name2) >= 4:
            part2 = name2[:4]
        else:
            part2 = name2
            
        # Combine with proper capitalization
        new_name = part1.capitalize() + part2.lower()
        
        return new_name
