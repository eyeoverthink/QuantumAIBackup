"""
Quantum Element Registry
Handles element registration and compatibility checking with φ-harmonic principles
"""

import mpmath
import numpy as np
from datetime import datetime

class QuantumElementRegistry:
    def __init__(self, precision=1000):
        mpmath.mp.dps = precision
        self.phi = float(mpmath.phi)
        
        # Initialize registries
        self.base_elements = {}
        self.discovered_elements = {}
        
        # Initialize base elements with quantum properties
        self._initialize_base_elements()
        
    def _initialize_base_elements(self):
        """Initialize base elements with quantum properties"""
        base_elements = {
            'H': {'mass': 1.008, 'atomic_number': 1},
            'He': {'mass': 4.003, 'atomic_number': 2},
            'Li': {'mass': 6.941, 'atomic_number': 3},
            'Be': {'mass': 9.012, 'atomic_number': 4},
            'B': {'mass': 10.811, 'atomic_number': 5},
            'C': {'mass': 12.011, 'atomic_number': 6},
            'N': {'mass': 14.007, 'atomic_number': 7},
            'O': {'mass': 15.999, 'atomic_number': 8},
            'F': {'mass': 18.998, 'atomic_number': 9},
            'Ne': {'mass': 20.180, 'atomic_number': 10},
            'Na': {'mass': 22.990, 'atomic_number': 11},
            'Mg': {'mass': 24.305, 'atomic_number': 12},
            'Al': {'mass': 26.982, 'atomic_number': 13},
            'Si': {'mass': 28.086, 'atomic_number': 14},
            'P': {'mass': 30.974, 'atomic_number': 15},
            'S': {'mass': 32.065, 'atomic_number': 16},
            'Cl': {'mass': 35.453, 'atomic_number': 17},
            'Ar': {'mass': 39.948, 'atomic_number': 18},
            'K': {'mass': 39.098, 'atomic_number': 19},
            'Ca': {'mass': 40.078, 'atomic_number': 20},
            'Fe': {'mass': 55.845, 'atomic_number': 26},
            'Co': {'mass': 58.933, 'atomic_number': 27},
            'Ni': {'mass': 58.693, 'atomic_number': 28},
            'Cu': {'mass': 63.546, 'atomic_number': 29},
            'Zn': {'mass': 65.380, 'atomic_number': 30},
            'Ag': {'mass': 107.868, 'atomic_number': 47},
            'Pt': {'mass': 195.084, 'atomic_number': 78},
            'Au': {'mass': 196.967, 'atomic_number': 79},
            'Pb': {'mass': 207.200, 'atomic_number': 82},
            'U': {'mass': 238.029, 'atomic_number': 92}
        }
        
        # Add quantum properties to each base element
        for name, data in base_elements.items():
            data['name'] = name
            data['properties'] = self._calculate_quantum_properties(data)
            self.base_elements[name] = data
            
    def _calculate_quantum_properties(self, element_data):
        """Calculate quantum properties for an element"""
        mass = float(element_data.get('mass', 0))
        atomic_number = float(element_data.get('atomic_number', 1))
        
        # Calculate electron configuration
        shells = self._calculate_electron_shells(mass, atomic_number)
        
        # Calculate quantum numbers
        n = len(shells)  # Principal quantum number
        l = min(n-1, 3)  # Angular momentum quantum number
        ml = list(range(-l, l+1))  # Magnetic quantum number
        
        # Calculate resonance properties
        base_freq = (mass * self.phi) % 1000
        resonance = 1 - (abs(mass/atomic_number - self.phi) % 1)
        
        # Calculate stability
        stability = self._calculate_stability(mass, atomic_number)
        
        # Calculate energy levels
        energy_levels = []
        for i in range(1, n+1):
            energy = (mass * self.phi ** i) % 100
            if energy > 0:
                energy_levels.append(energy)
        
        return {
            'electron_shells': shells,
            'quantum_numbers': {
                'n': n,
                'l': l,
                'ml': ml
            },
            'resonance': resonance,
            'base_frequency': base_freq,
            'stability': stability,
            'energy_levels': energy_levels
        }
        
    def _calculate_electron_shells(self, mass, atomic_number):
        """Calculate electron shell configuration"""
        shells = []
        remaining_electrons = atomic_number
        shell_number = 1
        
        while remaining_electrons > 0 and shell_number <= 7:
            # Each shell can hold 2n² electrons
            capacity = 2 * (shell_number ** 2)
            electrons = min(capacity, remaining_electrons)
            
            if electrons > 0:
                shells.append(electrons)
                
            remaining_electrons -= electrons
            shell_number += 1
            
        return shells
        
    def _calculate_stability(self, mass, atomic_number):
        """Calculate element stability using φ-harmonic principles"""
        if atomic_number <= 0:
            return 0.0
            
        # More stable when mass/atomic_number ratio is closer to φ
        mass_ratio = mass / max(1, atomic_number)
        stability = 1 - abs(mass_ratio - self.phi) % 1
        return float(stability)
        
    def register_discovered_element(self, name, properties):
        """Register a newly discovered element"""
        if name not in self.discovered_elements:
            # Ensure required properties exist
            if 'mass' not in properties:
                raise ValueError(f"Missing mass for element {name}")
                
            # Calculate atomic number based on mass
            atomic_number = max(1, int(properties['mass'] / self.phi))
            properties['atomic_number'] = atomic_number
            
            # Calculate all quantum properties
            quantum_props = self._calculate_quantum_properties({
                'mass': properties['mass'],
                'atomic_number': atomic_number
            })
            
            # Update properties
            properties['name'] = name
            properties['properties'] = quantum_props
            
            self.discovered_elements[name] = properties
            return True
        return False
        
    def get_element_data(self, name):
        """Get element data from either base or discovered elements"""
        if name in self.base_elements:
            return self.base_elements[name]
        elif name in self.discovered_elements:
            return self.discovered_elements[name]
        return None
        
    def calculate_compatibility(self, element1, element2):
        """Calculate compatibility between two elements"""
        data1 = self.get_element_data(element1)
        data2 = self.get_element_data(element2)
        
        if not data1 or not data2:
            return 0.0
            
        try:
            # Get quantum properties
            props1 = data1.get('properties', {})
            props2 = data2.get('properties', {})
            
            if not props1 or not props2:
                # Recalculate properties if missing
                props1 = self._calculate_quantum_properties(data1)
                props2 = self._calculate_quantum_properties(data2)
            
            # Calculate resonance compatibility
            resonance1 = props1.get('resonance', 0)
            resonance2 = props2.get('resonance', 0)
            resonance_diff = abs(resonance1 - resonance2)
            resonance_comp = 1 - (resonance_diff % 1)
            
            # Calculate shell compatibility
            shells1 = props1.get('electron_shells', [])
            shells2 = props2.get('electron_shells', [])
            if shells1 and shells2:
                shell_comp = 1 - abs(len(shells1) - len(shells2)) / max(len(shells1), len(shells2))
            else:
                shell_comp = 0.0
            
            # Calculate frequency compatibility
            freq1 = props1.get('base_frequency', 0)
            freq2 = props2.get('base_frequency', 0)
            freq_diff = abs(freq1 - freq2)
            freq_comp = 1 - (freq_diff / 1000)
            
            # Calculate stability contribution
            stability1 = props1.get('stability', 0)
            stability2 = props2.get('stability', 0)
            stability_comp = (stability1 + stability2) / 2
            
            # Calculate energy level compatibility
            energy1 = props1.get('energy_levels', [])
            energy2 = props2.get('energy_levels', [])
            if energy1 and energy2:
                energy_diff = abs(len(energy1) - len(energy2)) / max(len(energy1), len(energy2))
                energy_comp = 1 - energy_diff
            else:
                energy_comp = 0.0
            
            # Combine all factors with φ-weighted average
            weights = [self.phi ** 4, self.phi ** 3, self.phi ** 2, self.phi, 1.0]
            factors = [resonance_comp, shell_comp, freq_comp, stability_comp, energy_comp]
            
            total_weight = sum(weights)
            compatibility = sum(w * f for w, f in zip(weights, factors)) / total_weight
            
            return float(compatibility)
            
        except Exception as e:
            print(f"Warning: Compatibility calculation failed: {str(e)}")
            return 0.0
