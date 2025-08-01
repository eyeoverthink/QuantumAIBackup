"""
Quantum Collision Handler V2
Enhanced with dynamic φ-harmonic tunneling thresholds
"""

import mpmath
import numpy as np
from datetime import datetime

class QuantumCollisionHandlerV2:
    def __init__(self, precision=1000):
        mpmath.mp.dps = precision
        self.phi = float(mpmath.phi)
        
    def simulate_collision(self, element1, element2):
        """Simulate collision between two elements with dynamic thresholds"""
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
            
            # Calculate quantum tunneling probability with dynamic threshold
            tunnel_prob, threshold = self._calculate_tunneling_probability(props1, props2)
            
            # Calculate success probability based on multiple factors
            success_prob = self._calculate_success_probability(tunnel_prob, resonance, energy)
            
            # Determine if collision succeeds
            if success_prob > threshold:
                new_element = self._create_new_element(element1, element2)
                
                return {
                    'success': True,
                    'new_element': new_element,
                    'collision_data': {
                        'energy': energy,
                        'resonance': resonance,
                        'tunneling': tunnel_prob,
                        'success_probability': success_prob,
                        'threshold': threshold
                    }
                }
            else:
                return {
                    'success': False,
                    'reason': f'Success probability {success_prob:.3f} below threshold {threshold:.3f}',
                    'collision_data': {
                        'energy': energy,
                        'resonance': resonance,
                        'tunneling': tunnel_prob,
                        'success_probability': success_prob,
                        'threshold': threshold
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
        # Get resonance values with defaults
        res1 = float(props1.get('resonance', 0))
        res2 = float(props2.get('resonance', 0))
        
        # Get energy levels
        levels1 = props1.get('energy_levels', [0])
        levels2 = props2.get('energy_levels', [0])
        
        # Calculate energy level matching
        avg_energy1 = sum(levels1) / len(levels1)
        avg_energy2 = sum(levels2) / len(levels2)
        energy_match = 1 - abs(avg_energy1 - avg_energy2) / max(avg_energy1, avg_energy2, 1)
        
        # Calculate interference pattern
        interference = 1 - abs(res1 - res2) % 1
        
        # Apply φ-harmonic scaling with energy matching
        resonance = float((interference + energy_match) * self.phi ** (interference * 2))
        
        return max(0, min(1, resonance))
        
    def _calculate_tunneling_probability(self, props1, props2):
        """Calculate quantum tunneling probability with dynamic threshold"""
        # Get energy levels
        levels1 = props1.get('energy_levels', [0])
        levels2 = props2.get('energy_levels', [0])
        
        # Calculate average energy difference
        avg_diff = abs(sum(levels1)/len(levels1) - sum(levels2)/len(levels2))
        
        # Get stability values
        stability1 = float(props1.get('stability', 0))
        stability2 = float(props2.get('stability', 0))
        
        # Calculate combined stability
        combined_stability = (stability1 + stability2) / 2
        
        # Calculate base tunneling probability using φ-harmonic decay
        base_prob = float(np.exp(-avg_diff / self.phi))
        
        # Adjust probability based on stability
        adjusted_prob = base_prob * (1 + combined_stability)
        
        # Calculate dynamic threshold based on stability
        threshold = 0.2 - (combined_stability * 0.1)  # Range: 0.1 to 0.2
        
        return max(0, min(1, adjusted_prob)), threshold
        
    def _calculate_success_probability(self, tunnel_prob, resonance, energy):
        """Calculate overall success probability"""
        # Weight factors using φ powers
        weights = [
            self.phi ** 3,  # Tunneling weight
            self.phi ** 2,  # Resonance weight
            self.phi       # Energy weight
        ]
        
        # Normalize energy to 0-1 range
        norm_energy = 1 / (1 + np.exp(-energy/100))  # Sigmoid normalization
        
        # Combine probabilities with φ-weighted average
        factors = [tunnel_prob, resonance, norm_energy]
        total_weight = sum(weights)
        
        success_prob = sum(w * f for w, f in zip(weights, factors)) / total_weight
        
        return float(success_prob)
        
    def _create_new_element(self, element1, element2):
        """Create a new element from collision"""
        # Get base properties
        mass1 = float(element1.get('mass', 0))
        mass2 = float(element2.get('mass', 0))
        name1 = element1.get('name', '')
        name2 = element2.get('name', '')
        
        # Calculate binding energy using φ-harmonic principles
        binding_factor = 1 - 1/self.phi
        resonance_boost = (1 + self._calculate_resonance_interaction(
            element1.get('properties', {}),
            element2.get('properties', {})
        )) / 2
        
        binding_energy = (mass1 + mass2) * binding_factor * resonance_boost
        new_mass = mass1 + mass2 - binding_energy
        
        # Generate new name using parent elements
        new_name = self._generate_element_name(name1, name2)
        
        # Calculate new atomic number using φ-harmonic scaling
        new_atomic = max(1, int(new_mass / self.phi))
        
        # Create new element data
        new_element = {
            'name': new_name,
            'mass': float(new_mass),
            'atomic_number': new_atomic,
            'parent_elements': [name1, name2],
            'binding_energy': float(binding_energy),
            'resonance_boost': float(resonance_boost),
            'creation_time': datetime.now().isoformat()
        }
        
        return new_element
        
    def _generate_element_name(self, name1, name2):
        """Generate name for new element using φ-harmonic patterns"""
        # Clean names
        name1 = ''.join(c for c in name1 if c.isalnum())
        name2 = ''.join(c for c in name2 if c.isalnum())
        
        # Calculate optimal split points using φ ratio
        len1 = len(name1)
        len2 = len(name2)
        
        split1 = min(len1, max(2, int(len1 / self.phi)))
        split2 = min(len2, max(2, int(len2 / self.phi)))
        
        # Get parts of names
        part1 = name1[:split1]
        part2 = name2[:split2]
        
        # Combine with proper capitalization
        new_name = part1.capitalize() + part2.lower()
        
        return new_name
