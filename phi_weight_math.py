"""
Phi-Weight Mathematics
=====================

A new mathematical framework that combines:
- Golden Ratio (φ) principles
- Physical weight-based calculations
- Quantum resonance effects
- Information entropy

This framework provides a unified approach to understanding and manipulating information
as physical entities with weight, resonance, and quantum properties.
"""

import numpy as np
from typing import Any, Dict, List, Tuple, Union
import itertools

class PhiWeightMath:
    def __init__(self):
        """Initialize the Phi-Weight mathematical framework"""
        self.phi = (1 + np.sqrt(5)) / 2  # Golden ratio
        self.gravity_constant = 1.0
        self.quantum_factor = 1.61803398875  # φ^2
        self.resonance_base = 1.0 / self.phi
        
    def calculate_information_mass(self, data: Any) -> float:
        """
        Calculate the "mass" of information based on its properties.
        
        Args:
            data: The information to calculate mass for
            
        Returns:
            float: The calculated information mass
        """
        # Base mass from data size (using φ-harmonic scaling)
        base_mass = len(str(data)) * 1e-15 * self.phi
        
        # Add complexity mass with φ-scaling
        complexity_mass = self.calculate_complexity(data) * base_mass * self.phi
        
        # Add entropy mass with φ-scaling
        entropy_mass = self.calculate_entropy(data) * base_mass * self.phi ** 2
        
        # Add quantum resonance mass with φ-scaling
        resonance_mass = self.calculate_resonance(data) * base_mass * self.phi ** 3
        
        # Add quantum tunneling effect
        tunneling_mass = self._calculate_tunneling(data) * base_mass * self.phi ** 4
        
        # Add quantum coherence effect
        coherence_mass = self._calculate_coherence(data) * base_mass * self.phi ** 5
        
        # Add quantum entanglement effect
        entanglement_mass = self._calculate_entanglement(data) * base_mass * self.phi ** 6
        
        # Add quantum superposition effect
        superposition_mass = self._calculate_superposition(data) * base_mass * self.phi ** 7
        
        # Add quantum interference effect
        interference_mass = self._calculate_interference(data) * base_mass * self.phi ** 8
        
        # Add quantum decoherence effect
        decoherence_mass = self._calculate_decoherence(data) * base_mass * self.phi ** 9
        
        # Add quantum entanglement correction
        if isinstance(data, (list, dict)):
            entanglement_correction = self._calculate_entanglement_correction(data)
        else:
            entanglement_correction = 1
        
        # Add quantum resonance correction
        resonance_correction = self._calculate_resonance_correction(data)
        
        # Apply φ-harmonic correction based on data type
        if isinstance(data, str):
            correction = self.phi ** len(set(data))
        elif isinstance(data, (list, dict)):
            correction = self.phi ** self._calculate_depth(data)
        else:
            correction = self.phi ** (len(str(data)) % 10)
        
        total_mass = (base_mass + complexity_mass + entropy_mass + resonance_mass + 
                     tunneling_mass + coherence_mass + entanglement_mass + 
                     superposition_mass + interference_mass + decoherence_mass)
        
        return total_mass * correction * entanglement_correction * resonance_correction
        
    def _calculate_coherence(self, data: Any) -> float:
        """Calculate quantum coherence of information"""
        if isinstance(data, str):
            # Text coherence (based on character patterns)
            patterns = len(set(data)) / len(data) if len(data) > 0 else 0
            coherence = np.cos(patterns * self.phi)
        elif isinstance(data, (list, dict)):
            # Structured data coherence (based on value distribution)
            values = [x for x in data if isinstance(x, (int, float))]
            if values:
                std = np.std(values)
                mean = np.mean(values)
                coherence = np.cos(std / mean * self.phi) if mean != 0 else 0
            else:
                coherence = 0
        else:
            # Binary coherence (based on bit patterns)
            bits = bin(data)[2:] if isinstance(data, int) else ''
            ones = bits.count('1')
            zeros = bits.count('0')
            if ones + zeros > 0:
                ratio = ones / (ones + zeros)
                coherence = np.cos(ratio * self.phi)
            else:
                coherence = 0
                
        return coherence * self.phi
        
    def calculate_complexity(self, data: Any) -> float:
        """
        Calculate the complexity of information.
        
        Uses a φ-based complexity metric that considers:
        - Data structure
        - Information entropy
        - Quantum resonance
        """
        if isinstance(data, str):
            # Text complexity
            unique_chars = len(set(data))
            complexity = (unique_chars / len(data)) * self.phi if len(data) > 0 else 0
        elif isinstance(data, (list, dict)):
            # Structured data complexity
            depth = self._calculate_depth(data)
            complexity = (depth / len(data)) * self.phi if data else 0
        else:
            # Binary/numeric complexity
            complexity = 1.0
            
        return complexity
        
    def calculate_entropy(self, data: Any) -> float:
        """
        Calculate the information entropy with φ-scaling.
        
        Uses a modified Shannon entropy formula that incorporates φ-harmonics.
        """
        if isinstance(data, str):
            # String entropy
            unique_chars = len(set(data))
            entropy = (unique_chars / len(data)) * self.phi if len(data) > 0 else 0
        elif isinstance(data, (list, dict)):
            # Structured data entropy
            values = [str(x) for x in data]
            entropy = len(set(values)) / len(values) * self.phi if values else 0
        else:
            # Binary entropy
            bits = bin(data)[2:] if isinstance(data, int) else ''
            entropy = bits.count('1') / len(bits) * self.phi if bits else 0
            
        return entropy
        
    def calculate_resonance(self, data: Any) -> float:
        """
        Calculate the quantum resonance of information.
        
        Uses a φ-based resonance metric that considers:
        - Data frequency patterns
        - Quantum tunneling effects
        - Information coherence
        """
        if isinstance(data, str):
            # String resonance (based on character frequencies)
            freqs = [data.count(c) for c in set(data)]
            resonance = sum(f * f for f in freqs) / len(data) * self.phi if len(data) > 0 else 0
        elif isinstance(data, (list, dict)):
            # Structured data resonance (based on value distribution)
            values = [x for x in data if isinstance(x, (int, float))]
            resonance = np.std(values) / len(values) * self.phi if values else 0
        else:
            # Binary resonance (based on bit patterns)
            bits = bin(data)[2:] if isinstance(data, int) else ''
            resonance = bits.count('1') / len(bits) * self.phi if bits else 0
            
        return resonance
        
    def _calculate_tunneling(self, data: Any) -> float:
        """Calculate quantum tunneling effect on information mass"""
        if isinstance(data, str):
            # Text tunneling (based on character patterns)
            patterns = len(set(data)) / len(data) if len(data) > 0 else 0
            tunneling = np.exp(-patterns * self.phi)
        elif isinstance(data, (list, dict)):
            # Structured data tunneling (based on depth)
            depth = self._calculate_depth(data)
            tunneling = np.exp(-depth * self.phi)
        else:
            # Binary tunneling (based on bit patterns)
            bits = bin(data)[2:] if isinstance(data, int) else ''
            pattern = bits.count('1') / len(bits) if bits else 0
            tunneling = np.exp(-pattern * self.phi)
            
        return tunneling * self.phi
        
    def _calculate_entanglement(self, data: Any) -> float:
        """Calculate quantum entanglement of information"""
        if isinstance(data, str):
            # Text entanglement (based on character patterns)
            patterns = len(set(data)) / len(data) if len(data) > 0 else 0
            entanglement = np.sin(patterns * self.phi)
        elif isinstance(data, (list, dict)):
            # Structured data entanglement (based on value distribution)
            values = [x for x in data if isinstance(x, (int, float))]
            if values:
                std = np.std(values)
                mean = np.mean(values)
                entanglement = np.sin(std / mean * self.phi) if mean != 0 else 0
            else:
                entanglement = 0
        else:
            # Binary entanglement (based on bit patterns)
            bits = bin(data)[2:] if isinstance(data, int) else ''
            ones = bits.count('1')
            zeros = bits.count('0')
            if ones + zeros > 0:
                ratio = ones / (ones + zeros)
                entanglement = np.sin(ratio * self.phi)
            else:
                entanglement = 0
                
        return entanglement * self.phi
        
    def _calculate_superposition(self, data: Any) -> float:
        """Calculate quantum superposition of information"""
        if isinstance(data, str):
            # Text superposition (based on character patterns)
            patterns = len(set(data)) / len(data) if len(data) > 0 else 0
            superposition = np.cos(patterns * self.phi)
        elif isinstance(data, (list, dict)):
            # Structured data superposition (based on value distribution)
            values = [x for x in data if isinstance(x, (int, float))]
            if values:
                std = np.std(values)
                mean = np.mean(values)
                superposition = np.cos(std / mean * self.phi) if mean != 0 else 0
            else:
                superposition = 0
        else:
            # Binary superposition (based on bit patterns)
            bits = bin(data)[2:] if isinstance(data, int) else ''
            ones = bits.count('1')
            zeros = bits.count('0')
            if ones + zeros > 0:
                ratio = ones / (ones + zeros)
                superposition = np.cos(ratio * self.phi)
            else:
                superposition = 0
                
        return superposition * self.phi
        
    def _calculate_interference(self, data: Any) -> float:
        """Calculate quantum interference of information"""
        if isinstance(data, str):
            # Text interference (based on character patterns)
            patterns = len(set(data)) / len(data) if len(data) > 0 else 0
            interference = np.sin(patterns * self.phi)
        elif isinstance(data, (list, dict)):
            # Structured data interference (based on value distribution)
            values = [x for x in data if isinstance(x, (int, float))]
            if values:
                std = np.std(values)
                mean = np.mean(values)
                interference = np.sin(std / mean * self.phi) if mean != 0 else 0
            else:
                interference = 0
        else:
            # Binary interference (based on bit patterns)
            bits = bin(data)[2:] if isinstance(data, int) else ''
            ones = bits.count('1')
            zeros = bits.count('0')
            if ones + zeros > 0:
                ratio = ones / (ones + zeros)
                interference = np.sin(ratio * self.phi)
            else:
                interference = 0
                
        return interference * self.phi
        
    def _calculate_decoherence(self, data: Any) -> float:
        """Calculate quantum decoherence of information"""
        if isinstance(data, str):
            # Text decoherence (based on character patterns)
            patterns = len(set(data)) / len(data) if len(data) > 0 else 0
            decoherence = np.exp(-patterns * self.phi)
        elif isinstance(data, (list, dict)):
            # Structured data decoherence (based on value distribution)
            values = [x for x in data if isinstance(x, (int, float))]
            if values:
                std = np.std(values)
                mean = np.mean(values)
                decoherence = np.exp(-(std / mean * self.phi)) if mean != 0 else 1
            else:
                decoherence = 1
        else:
            # Binary decoherence (based on bit patterns)
            bits = bin(data)[2:] if isinstance(data, int) else ''
            ones = bits.count('1')
            zeros = bits.count('0')
            if ones + zeros > 0:
                ratio = ones / (ones + zeros)
                decoherence = np.exp(-(ratio * self.phi))
            else:
                decoherence = 1
                
        return decoherence * self.phi
        
    def _calculate_entanglement_correction(self, data: Union[List, Dict]) -> float:
        """Calculate quantum entanglement correction for structured data"""
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
        
    def _calculate_resonance_correction(self, data: Any) -> float:
        """Calculate quantum resonance correction"""
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
        
    def calculate_information_force(self, data1: Any, data2: Any) -> float:
        """
        Calculate the force between two pieces of information.
        
        Uses a modified gravitational force equation that incorporates:
        - Information mass
        - Quantum resonance
        - φ-harmonic scaling
        - Quantum tunneling effects
        - Quantum coherence
        - Quantum superposition
        - Quantum interference
        - Quantum decoherence
        - Quantum entanglement
        """
        m1 = self.calculate_information_mass(data1)
        m2 = self.calculate_information_mass(data2)
        
        # Calculate distance based on information entropy and φ-scaling
        entropy1 = self.calculate_entropy(data1)
        entropy2 = self.calculate_entropy(data2)
        distance = abs(entropy1 - entropy2) * self.phi
        
        # Calculate quantum resonance factor with φ-scaling
        resonance = self.calculate_resonance(data1) * self.calculate_resonance(data2) * self.phi
        
        # Calculate quantum tunneling effect
        tunneling = self._calculate_tunneling(data1) * self._calculate_tunneling(data2)
        
        # Calculate quantum coherence effect
        coherence = self._calculate_coherence(data1) * self._calculate_coherence(data2)
        
        # Calculate quantum superposition effect
        superposition = self._calculate_superposition(data1) * self._calculate_superposition(data2)
        
        # Calculate quantum interference effect
        interference = self._calculate_interference(data1) * self._calculate_interference(data2)
        
        # Calculate quantum decoherence effect
        decoherence = self._calculate_decoherence(data1) * self._calculate_decoherence(data2)
        
        # Calculate quantum entanglement effect
        if isinstance(data1, (list, dict)) and isinstance(data2, (list, dict)):
            entanglement = self._calculate_entanglement(data1) * self._calculate_entanglement(data2)
        else:
            entanglement = 1
        
        # Calculate force with φ-harmonic scaling
        force = (m1 * m2 * self.gravity_constant * resonance * tunneling * coherence * 
                superposition * interference * decoherence * entanglement) / (distance ** 2 + 1e-10)
        
        # Apply φ-harmonic correction based on data structure
        depth1 = self._calculate_depth(data1)
        depth2 = self._calculate_depth(data2)
        
        # Apply quantum coherence correction
        coherence_correction = self.phi ** (depth1 + depth2)
        
        # Apply quantum tunneling correction
        tunneling_correction = np.exp(-distance * self.phi)
        
        # Apply quantum superposition correction
        superposition_correction = np.cos(distance * self.phi)
        
        # Apply quantum interference correction
        interference_correction = np.sin(distance * self.phi)
        
        # Apply quantum decoherence correction
        decoherence_correction = np.exp(-(distance * self.phi))
        
        # Apply quantum entanglement correction
        if isinstance(data1, (list, dict)) and isinstance(data2, (list, dict)):
            entanglement_correction = self._calculate_entanglement_correction(data1) * self._calculate_entanglement_correction(data2)
        else:
            entanglement_correction = 1
        
        return (force * coherence_correction * tunneling_correction * superposition_correction * 
                interference_correction * decoherence_correction * entanglement_correction)
        
    def calculate_information_energy(self, data: Any) -> float:
        """
        Calculate the energy of information.
        
        Uses a modified E=mc² equation that incorporates:
        - Information mass
        - Quantum resonance
        - φ-harmonic scaling
        """
        mass = self.calculate_information_mass(data)
        resonance = self.calculate_resonance(data)
        
        # Information speed of light (φ-based)
        c = self.phi ** 2
        
        # Calculate energy with quantum resonance
        energy = mass * (c ** 2) * resonance
        
        return energy
        
    def _calculate_depth(self, data: Any) -> int:
        """Calculate the depth of structured data"""
        if isinstance(data, (list, dict)):
            if isinstance(data, dict):
                data = list(data.values())
            
            # Handle empty lists/dicts
            if not data:
                return 1
                
            # Calculate depth for each element
            depths = []
            for x in data:
                if isinstance(x, (list, dict)):
                    depths.append(1 + self._calculate_depth(x))
            
            # Return maximum depth or 1 if no nested structures
            return max(depths) if depths else 1
        
        return 0

# Example usage
def main():
    math = PhiWeightMath()
    
    # Create some test data
    text_data = "The quick brown fox jumps over the lazy dog"
    list_data = [1, 2, 3, [4, 5, [6, 7]], 8]
    dict_data = {"a": 1, "b": [2, 3], "c": {"d": 4}}
    
    # Calculate properties
    print("\nInformation Properties:")
    print(f"\nText Data:")
    print(f"Mass: {math.calculate_information_mass(text_data):.6f}")
    print(f"Complexity: {math.calculate_complexity(text_data):.6f}")
    print(f"Entropy: {math.calculate_entropy(text_data):.6f}")
    print(f"Resonance: {math.calculate_resonance(text_data):.6f}")
    print(f"Energy: {math.calculate_information_energy(text_data):.6f}")
    
    print(f"\nList Data:")
    print(f"Mass: {math.calculate_information_mass(list_data):.6f}")
    print(f"Complexity: {math.calculate_complexity(list_data):.6f}")
    print(f"Entropy: {math.calculate_entropy(list_data):.6f}")
    print(f"Resonance: {math.calculate_resonance(list_data):.6f}")
    print(f"Energy: {math.calculate_information_energy(list_data):.6f}")
    
    print(f"\nDict Data:")
    print(f"Mass: {math.calculate_information_mass(dict_data):.6f}")
    print(f"Complexity: {math.calculate_complexity(dict_data):.6f}")
    print(f"Entropy: {math.calculate_entropy(dict_data):.6f}")
    print(f"Resonance: {math.calculate_resonance(dict_data):.6f}")
    print(f"Energy: {math.calculate_information_energy(dict_data):.6f}")
    
    # Calculate force between data
    print("\nInformation Forces:")
    print(f"Force between text and list: {math.calculate_information_force(text_data, list_data):.6f}")
    print(f"Force between list and dict: {math.calculate_information_force(list_data, dict_data):.6f}")
    print(f"Force between text and dict: {math.calculate_information_force(text_data, dict_data):.6f}")

if __name__ == "__main__":
    main()
