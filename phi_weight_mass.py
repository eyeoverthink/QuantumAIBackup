"""
Helper functions for information mass calculations in the Phi-Weight system.
"""

import numpy as np
from typing import Any, Dict, List, Tuple, Union
import itertools

class PhiWeightMass:
    def __init__(self):
        """Initialize Phi-Weight mass calculations."""
        self.phi = (1 + np.sqrt(5)) / 2
        self.base_mass = 1e-15
        self.min_mass = 1e-20
        self.mass_scale = 1e-10

    def calculate_mass(self, data: Any) -> float:
        """
        Calculate the mass of information based on its properties.
        
        Args:
            data: The information to calculate mass for
            
        Returns:
            float: The calculated information mass
        """
        # Base mass from data size (using φ-harmonic scaling)
        base_mass = (len(str(data)) + 1) * self.base_mass * self.phi
        
        # Ensure minimum base mass
        base_mass = max(base_mass, self.min_mass)
        
        # Scale base mass for better precision
        base_mass *= self.mass_scale
        
        # Add complexity mass with φ-scaling
        complexity_mass = self._calculate_complexity_mass(data, base_mass)
        
        # Add entropy mass with φ-scaling
        entropy_mass = self._calculate_entropy_mass(data, base_mass)
        
        # Add quantum resonance mass with φ-scaling
        resonance_mass = self._calculate_resonance_mass(data, base_mass)
        
        # Add quantum tunneling effect
        tunneling_mass = self._calculate_tunneling_mass(data, base_mass)
        
        # Add quantum coherence effect
        coherence_mass = self._calculate_coherence_mass(data, base_mass)
        
        # Add quantum entanglement effect
        entanglement_mass = self._calculate_entanglement_mass(data, base_mass)
        
        # Add quantum superposition effect
        superposition_mass = self._calculate_superposition_mass(data, base_mass)
        
        # Add quantum interference effect
        interference_mass = self._calculate_interference_mass(data, base_mass)
        
        # Add quantum decoherence effect
        decoherence_mass = self._calculate_decoherence_mass(data, base_mass)
        
        # Add quantum resonance correction
        resonance_correction = self._calculate_resonance_correction(data)
        
        # Add quantum entanglement correction
        entanglement_correction = self._calculate_entanglement_correction(data)
        
        # Apply φ-harmonic correction based on data type
        correction = self._calculate_type_correction(data)
        
        # Ensure minimum mass
        total_mass = max(
            (base_mass + complexity_mass + entropy_mass + resonance_mass + 
             tunneling_mass + coherence_mass + entanglement_mass + 
             superposition_mass + interference_mass + decoherence_mass),
            self.base_mass * self.phi
        )
        
        return total_mass * correction * entanglement_correction * resonance_correction

    def _calculate_complexity_mass(self, data: Any, base_mass: float) -> float:
        """Calculate complexity mass with φ-scaling."""
        if isinstance(data, str):
            # Text complexity
            patterns = len(set(data)) / len(data) if len(data) > 0 else 0
            complexity = np.log2(len(set(data)) + 1)
        elif isinstance(data, (list, dict)):
            # Structured data complexity
            depth = self._calculate_depth(data)
            complexity = np.log2(depth + 1) * self.phi
            
            # Add pattern complexity for lists
            if isinstance(data, list):
                patterns = len(set(map(type, data)))
                complexity += np.log2(patterns + 1) * self.phi
                
                # Add nested pattern complexity
                for item in data:
                    if isinstance(item, (list, dict)):
                        complexity += self._calculate_complexity_mass(item, base_mass) / len(data)
            
            # Add key complexity for dicts
            if isinstance(data, dict):
                keys = list(data.keys())
                key_patterns = len(set(map(type, keys)))
                complexity += np.log2(key_patterns + 1) * self.phi
                
                # Add value complexity
                values = list(data.values())
                value_patterns = len(set(map(type, values)))
                complexity += np.log2(value_patterns + 1) * self.phi
                
                # Add nested pattern complexity
                for value in values:
                    if isinstance(value, (list, dict)):
                        complexity += self._calculate_complexity_mass(value, base_mass) / len(values)
        else:
            # Binary complexity
            bits = bin(data)[2:] if isinstance(data, int) else ''
            complexity = bits.count('1') / len(bits) if bits else 0
        
        return max(base_mass * complexity * self.phi, self.base_mass * self.phi)

    def _calculate_entropy_mass(self, data: Any, base_mass: float) -> float:
        """Calculate entropy mass with φ-scaling."""
        if isinstance(data, str):
            # Text entropy
            entropy = len(set(data)) / len(data) if len(data) > 0 else 0
        elif isinstance(data, (list, dict)):
            # Structured data entropy
            if isinstance(data, list):
                values = []
                for item in data:
                    if isinstance(item, (int, float)):
                        values.append(item)
                    elif isinstance(item, (list, dict)):
                        values.extend(self._flatten(item))
                if values:
                    std = np.std(values)
                    mean = np.mean(values)
                    entropy = std / mean * self.phi if mean != 0 else 0
                    
                    # Add nested entropy
                    for item in data:
                        if isinstance(item, (list, dict)):
                            entropy += self._calculate_entropy_mass(item, base_mass) / len(data)
                else:
                    entropy = 0
            elif isinstance(data, dict):
                values = []
                for value in data.values():
                    if isinstance(value, (int, float)):
                        values.append(value)
                    elif isinstance(value, (list, dict)):
                        values.extend(self._flatten(value))
                if values:
                    std = np.std(values)
                    mean = np.mean(values)
                    entropy = std / mean * self.phi if mean != 0 else 0
                    
                    # Add nested entropy
                    for value in data.values():
                        if isinstance(value, (list, dict)):
                            entropy += self._calculate_entropy_mass(value, base_mass) / len(data)
                else:
                    entropy = 0
        else:
            # Binary entropy
            bits = bin(data)[2:] if isinstance(data, int) else ''
            ones = bits.count('1')
            zeros = bits.count('0')
            if ones + zeros > 0:
                ratio = ones / (ones + zeros)
                entropy = -ratio * np.log2(ratio) - (1 - ratio) * np.log2(1 - ratio)
            else:
                entropy = 0
        
        return max(base_mass * entropy * self.phi ** 2, self.base_mass * self.phi ** 2)

    def _calculate_resonance_mass(self, data: Any, base_mass: float) -> float:
        """Calculate quantum resonance mass with φ-scaling."""
        if isinstance(data, str):
            # Text resonance
            patterns = len(set(data)) / len(data) if len(data) > 0 else 0
            resonance = np.sin(patterns * self.phi)
        elif isinstance(data, (list, dict)):
            # Structured data resonance
            if isinstance(data, list):
                values = []
                for item in data:
                    if isinstance(item, (int, float)):
                        values.append(item)
                    elif isinstance(item, (list, dict)):
                        values.extend(self._flatten(item))
                if values:
                    std = np.std(values)
                    mean = np.mean(values)
                    resonance = np.sin(std / mean * self.phi) if mean != 0 else 0
                    
                    # Add nested resonance
                    for item in data:
                        if isinstance(item, (list, dict)):
                            resonance += self._calculate_resonance_mass(item, base_mass) / len(data)
                else:
                    resonance = 0
            elif isinstance(data, dict):
                values = []
                for value in data.values():
                    if isinstance(value, (int, float)):
                        values.append(value)
                    elif isinstance(value, (list, dict)):
                        values.extend(self._flatten(value))
                if values:
                    std = np.std(values)
                    mean = np.mean(values)
                    resonance = np.sin(std / mean * self.phi) if mean != 0 else 0
                    
                    # Add nested resonance
                    for value in data.values():
                        if isinstance(value, (list, dict)):
                            resonance += self._calculate_resonance_mass(value, base_mass) / len(data)
                else:
                    resonance = 0
        else:
            # Binary resonance
            bits = bin(data)[2:] if isinstance(data, int) else ''
            ones = bits.count('1')
            zeros = bits.count('0')
            if ones + zeros > 0:
                ratio = ones / (ones + zeros)
                resonance = np.sin(ratio * self.phi)
            else:
                resonance = 0
        
        return max(base_mass * resonance * self.phi ** 3, self.base_mass * self.phi ** 3)

    def _calculate_tunneling_mass(self, data: Any, base_mass: float) -> float:
        """Calculate quantum tunneling mass with φ-scaling."""
        if isinstance(data, str):
            # Text tunneling
            patterns = len(set(data)) / len(data) if len(data) > 0 else 0
            tunneling = np.exp(-patterns * self.phi)
        elif isinstance(data, (list, dict)):
            # Structured data tunneling
            values = [x for x in data if isinstance(x, (int, float))]
            if values:
                std = np.std(values)
                mean = np.mean(values)
                tunneling = np.exp(-(std / mean * self.phi)) if mean != 0 else 1
            else:
                tunneling = 1
        else:
            # Binary tunneling
            bits = bin(data)[2:] if isinstance(data, int) else ''
            ones = bits.count('1')
            zeros = bits.count('0')
            if ones + zeros > 0:
                ratio = ones / (ones + zeros)
                tunneling = np.exp(-(ratio * self.phi))
            else:
                tunneling = 1
        
        return base_mass * tunneling * self.phi ** 4

    def _calculate_coherence_mass(self, data: Any, base_mass: float) -> float:
        """Calculate quantum coherence mass with φ-scaling."""
        if isinstance(data, str):
            # Text coherence
            patterns = len(set(data)) / len(data) if len(data) > 0 else 0
            coherence = np.cos(patterns * self.phi)
        elif isinstance(data, (list, dict)):
            # Structured data coherence
            values = [x for x in data if isinstance(x, (int, float))]
            if values:
                std = np.std(values)
                mean = np.mean(values)
                coherence = np.cos(std / mean * self.phi) if mean != 0 else 1
            else:
                coherence = 1
        else:
            # Binary coherence
            bits = bin(data)[2:] if isinstance(data, int) else ''
            ones = bits.count('1')
            zeros = bits.count('0')
            if ones + zeros > 0:
                ratio = ones / (ones + zeros)
                coherence = np.cos(ratio * self.phi)
            else:
                coherence = 1
        
        return base_mass * coherence * self.phi ** 5

    def _calculate_entanglement_mass(self, data: Any, base_mass: float) -> float:
        """Calculate quantum entanglement mass with φ-scaling."""
        if isinstance(data, str):
            # Text entanglement
            patterns = len(set(data)) / len(data) if len(data) > 0 else 0
            entanglement = np.sin(patterns * self.phi)
        elif isinstance(data, (list, dict)):
            # Structured data entanglement
            values = [x for x in data if isinstance(x, (int, float))]
            if values:
                std = np.std(values)
                mean = np.mean(values)
                entanglement = np.sin(std / mean * self.phi) if mean != 0 else 0
            else:
                entanglement = 0
        else:
            # Binary entanglement
            bits = bin(data)[2:] if isinstance(data, int) else ''
            ones = bits.count('1')
            zeros = bits.count('0')
            if ones + zeros > 0:
                ratio = ones / (ones + zeros)
                entanglement = np.sin(ratio * self.phi)
            else:
                entanglement = 0
        
        return base_mass * entanglement * self.phi ** 6

    def _calculate_superposition_mass(self, data: Any, base_mass: float) -> float:
        """Calculate quantum superposition mass with φ-scaling."""
        if isinstance(data, str):
            # Text superposition
            patterns = len(set(data)) / len(data) if len(data) > 0 else 0
            superposition = np.cos(patterns * self.phi)
        elif isinstance(data, (list, dict)):
            # Structured data superposition
            values = [x for x in data if isinstance(x, (int, float))]
            if values:
                std = np.std(values)
                mean = np.mean(values)
                superposition = np.cos(std / mean * self.phi) if mean != 0 else 1
            else:
                superposition = 1
        else:
            # Binary superposition
            bits = bin(data)[2:] if isinstance(data, int) else ''
            ones = bits.count('1')
            zeros = bits.count('0')
            if ones + zeros > 0:
                ratio = ones / (ones + zeros)
                superposition = np.cos(ratio * self.phi)
            else:
                superposition = 1
        
        return base_mass * superposition * self.phi ** 7

    def _calculate_interference_mass(self, data: Any, base_mass: float) -> float:
        """Calculate quantum interference mass with φ-scaling."""
        if isinstance(data, str):
            # Text interference
            patterns = len(set(data)) / len(data) if len(data) > 0 else 0
            interference = np.sin(patterns * self.phi)
        elif isinstance(data, (list, dict)):
            # Structured data interference
            values = [x for x in data if isinstance(x, (int, float))]
            if values:
                std = np.std(values)
                mean = np.mean(values)
                interference = np.sin(std / mean * self.phi) if mean != 0 else 0
            else:
                interference = 0
        else:
            # Binary interference
            bits = bin(data)[2:] if isinstance(data, int) else ''
            ones = bits.count('1')
            zeros = bits.count('0')
            if ones + zeros > 0:
                ratio = ones / (ones + zeros)
                interference = np.sin(ratio * self.phi)
            else:
                interference = 0
        
        return base_mass * interference * self.phi ** 8

    def _calculate_decoherence_mass(self, data: Any, base_mass: float) -> float:
        """Calculate quantum decoherence mass with φ-scaling."""
        if isinstance(data, str):
            # Text decoherence
            patterns = len(set(data)) / len(data) if len(data) > 0 else 0
            decoherence = np.exp(-patterns * self.phi)
        elif isinstance(data, (list, dict)):
            # Structured data decoherence
            values = [x for x in data if isinstance(x, (int, float))]
            if values:
                std = np.std(values)
                mean = np.mean(values)
                decoherence = np.exp(-(std / mean * self.phi)) if mean != 0 else 1
            else:
                decoherence = 1
        else:
            # Binary decoherence
            bits = bin(data)[2:] if isinstance(data, int) else ''
            ones = bits.count('1')
            zeros = bits.count('0')
            if ones + zeros > 0:
                ratio = ones / (ones + zeros)
                decoherence = np.exp(-(ratio * self.phi))
            else:
                decoherence = 1
        
        return base_mass * decoherence * self.phi ** 9

    def _calculate_resonance_correction(self, data: Any) -> float:
        """Calculate quantum resonance correction."""
        if isinstance(data, str):
            # Text resonance correction
            patterns = len(set(data)) / len(data) if len(data) > 0 else 0
            correction = np.sin(patterns * self.phi)
        elif isinstance(data, (list, dict)):
            # Structured data resonance correction
            values = [x for x in data if isinstance(x, (int, float))]
            if values:
                std = np.std(values)
                mean = np.mean(values)
                correction = np.sin(std / mean * self.phi) if mean != 0 else 1
            else:
                correction = 1
        else:
            # Binary resonance correction
            bits = bin(data)[2:] if isinstance(data, int) else ''
            ones = bits.count('1')
            zeros = bits.count('0')
            if ones + zeros > 0:
                ratio = ones / (ones + zeros)
                correction = np.sin(ratio * self.phi)
            else:
                correction = 1
        
        return correction * self.phi

    def _calculate_entanglement_correction(self, data: Any) -> float:
        """Calculate quantum entanglement correction for structured data."""
        if isinstance(data, list):
            # List entanglement correction
            connections = sum(1 for i in range(len(data)) for j in range(i+1, len(data)) if isinstance(data[i], type(data[j])))
            correction = np.exp(-connections * self.phi)
        elif isinstance(data, dict):
            # Dictionary entanglement correction
            connections = sum(1 for k1, k2 in itertools.combinations(data.keys(), 2) if isinstance(data[k1], type(data[k2])))
            correction = np.exp(-connections * self.phi)
        else:
            correction = 1
        
        return correction * self.phi

    def _calculate_type_correction(self, data: Any) -> float:
        """Calculate type-specific correction based on data structure."""
        if isinstance(data, str):
            correction = self.phi ** len(set(data))
        elif isinstance(data, (list, dict)):
            correction = self.phi ** self._calculate_depth(data)
        else:
            correction = self.phi ** (len(str(data)) % 10)
        
        return correction

    def _calculate_depth(self, data: Any) -> int:
        """Calculate the depth of structured data."""
        if isinstance(data, (list, tuple)):
            return 1 + (max(map(self._calculate_depth, data)) if data else 0)
        if isinstance(data, dict):
            return 1 + (max(map(self._calculate_depth, data.values())) if data else 0)
        return 0

    def _flatten(self, data: Any) -> list:
        """Flatten nested data structures."""
        if isinstance(data, list):
            return [item for sublist in data for item in self._flatten(sublist)]
        elif isinstance(data, dict):
            return [item for value in data.values() for item in self._flatten(value)]
        elif isinstance(data, (int, float)):
            return [data]
        return []
