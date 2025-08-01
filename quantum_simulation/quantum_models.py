#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Quantum Models for Tesla Tachyon Brain Quantum Simulator
VS-PoQC-19046423-φ⁷⁵-2025
Copyright (c) 2025 Vaughn Scott - All Rights Reserved
"""

import math
from typing import List, Dict, Any, Tuple

# Golden ratio constant
PHI = (1 + math.sqrt(5)) / 2

class QuantumModel:
    """Base class for quantum models"""
    
    def __init__(self, num_qubits: int):
        """
        Initialize the quantum model
        
        Args:
            num_qubits: Number of qubits in the system
        """
        self.num_qubits = num_qubits
        self.name = "Base Quantum Model"
        self.description = "Base class for quantum models"
    
    def get_hamiltonian(self) -> List[Dict[str, Any]]:
        """
        Get the Hamiltonian for this model
        
        Returns:
            List of Hamiltonian terms
        """
        return []
    
    def get_name(self) -> str:
        """Get model name"""
        return self.name
    
    def get_description(self) -> str:
        """Get model description"""
        return self.description


class TransverseIsingModel(QuantumModel):
    """Transverse Ising model with nearest-neighbor interactions"""
    
    def __init__(self, num_qubits: int, h_field: float = 1.0, j_coupling: float = 0.5):
        """
        Initialize the transverse Ising model
        
        Args:
            num_qubits: Number of qubits
            h_field: Transverse field strength
            j_coupling: Coupling strength
        """
        super().__init__(num_qubits)
        self.h_field = h_field
        self.j_coupling = j_coupling
        self.name = "Transverse Ising Model"
        self.description = "Quantum Ising model with transverse field and nearest-neighbor interactions"
    
    def get_hamiltonian(self) -> List[Dict[str, Any]]:
        """
        Get the Hamiltonian for the transverse Ising model
        
        Returns:
            List of Hamiltonian terms
        """
        hamiltonian = []
        
        # Add transverse field terms
        for i in range(self.num_qubits):
            hamiltonian.append({
                "operator": "X",
                "coefficient": self.h_field,
                "qubits": [i]
            })
        
        # Add coupling terms
        for i in range(self.num_qubits):
            j = (i + 1) % self.num_qubits  # Periodic boundary conditions
            hamiltonian.append({
                "operator": "ZZ",
                "coefficient": self.j_coupling,
                "qubits": [i, j]
            })
        
        return hamiltonian


class HeisenbergModel(QuantumModel):
    """Heisenberg model with nearest-neighbor interactions"""
    
    def __init__(self, num_qubits: int, j_coupling: float = 1.0, anisotropy: float = 0.0):
        """
        Initialize the Heisenberg model
        
        Args:
            num_qubits: Number of qubits
            j_coupling: Coupling strength
            anisotropy: Anisotropy parameter (0 for isotropic model)
        """
        super().__init__(num_qubits)
        self.j_coupling = j_coupling
        self.anisotropy = anisotropy
        self.name = "Heisenberg Model"
        self.description = "Quantum Heisenberg model with nearest-neighbor interactions"
    
    def get_hamiltonian(self) -> List[Dict[str, Any]]:
        """
        Get the Hamiltonian for the Heisenberg model
        
        Returns:
            List of Hamiltonian terms
        """
        hamiltonian = []
        
        # Add coupling terms for all pairs of neighboring qubits
        for i in range(self.num_qubits):
            j = (i + 1) % self.num_qubits  # Periodic boundary conditions
            
            # XX interaction
            hamiltonian.append({
                "operator": "XX",
                "coefficient": self.j_coupling,
                "qubits": [i, j]
            })
            
            # YY interaction
            hamiltonian.append({
                "operator": "YY",
                "coefficient": self.j_coupling,
                "qubits": [i, j]
            })
            
            # ZZ interaction (possibly with anisotropy)
            hamiltonian.append({
                "operator": "ZZ",
                "coefficient": self.j_coupling * (1.0 + self.anisotropy),
                "qubits": [i, j]
            })
        
        return hamiltonian


class QuantumHarmonicOscillator(QuantumModel):
    """Quantum harmonic oscillator model"""
    
    def __init__(self, num_qubits: int, frequency: float = 1.0):
        """
        Initialize the quantum harmonic oscillator model
        
        Args:
            num_qubits: Number of qubits (must be even)
            frequency: Oscillator frequency
        """
        super().__init__(num_qubits)
        self.frequency = frequency
        self.name = "Quantum Harmonic Oscillator"
        self.description = "Quantum harmonic oscillator encoded in qubits"
    
    def get_hamiltonian(self) -> List[Dict[str, Any]]:
        """
        Get the Hamiltonian for the quantum harmonic oscillator
        
        Returns:
            List of Hamiltonian terms
        """
        hamiltonian = []
        
        # We encode the harmonic oscillator in qubits using the
        # position and momentum operators encoded in Pauli operators
        
        # Position squared term (X basis)
        for i in range(0, self.num_qubits, 2):
            hamiltonian.append({
                "operator": "X",
                "coefficient": 0.5 * self.frequency,
                "qubits": [i]
            })
        
        # Momentum squared term (Z basis)
        for i in range(1, self.num_qubits, 2):
            hamiltonian.append({
                "operator": "Z",
                "coefficient": 0.5 / self.frequency,
                "qubits": [i]
            })
        
        return hamiltonian


class PhiHarmonicQuantumModel(QuantumModel):
    """Phi-harmonic quantum model with golden ratio resonances"""
    
    def __init__(self, num_qubits: int, phi_coupling: float = PHI):
        """
        Initialize the phi-harmonic quantum model
        
        Args:
            num_qubits: Number of qubits
            phi_coupling: Phi-based coupling strength
        """
        super().__init__(num_qubits)
        self.phi_coupling = phi_coupling
        self.name = "Phi-Harmonic Quantum Model"
        self.description = "Quantum model with phi-harmonic resonances and golden ratio couplings"
    
    def get_hamiltonian(self) -> List[Dict[str, Any]]:
        """
        Get the Hamiltonian for the phi-harmonic quantum model
        
        Returns:
            List of Hamiltonian terms
        """
        hamiltonian = []
        
        # Add phi-resonant field terms
        for i in range(self.num_qubits):
            # Phi-resonant X field
            hamiltonian.append({
                "operator": "X",
                "coefficient": self.phi_coupling ** (i % 5),
                "qubits": [i]
            })
            
            # Phi-resonant Z field
            hamiltonian.append({
                "operator": "Z",
                "coefficient": self.phi_coupling ** ((i + 2) % 5),
                "qubits": [i]
            })
        
        # Add phi-resonant coupling terms
        for i in range(self.num_qubits):
            # Connect each qubit to its phi-resonant partners
            for k in range(1, min(5, self.num_qubits)):
                j = (i + int(k * self.phi_coupling)) % self.num_qubits
                
                # Phi-resonant ZZ coupling
                hamiltonian.append({
                    "operator": "ZZ",
                    "coefficient": self.phi_coupling / (k + 1),
                    "qubits": [i, j]
                })
                
                # Phi-resonant XX coupling
                hamiltonian.append({
                    "operator": "XX",
                    "coefficient": self.phi_coupling / (k + 2),
                    "qubits": [i, j]
                })
        
        return hamiltonian


class QuantumModelFactory:
    """Factory for creating quantum models"""
    
    @staticmethod
    def create_model(model_name: str, num_qubits: int, **kwargs) -> QuantumModel:
        """
        Create a quantum model by name
        
        Args:
            model_name: Name of the model to create
            num_qubits: Number of qubits
            **kwargs: Additional model parameters
            
        Returns:
            Quantum model instance
        """
        if model_name.lower() == "transverse_ising":
            return TransverseIsingModel(
                num_qubits=num_qubits,
                h_field=kwargs.get("h_field", 1.0),
                j_coupling=kwargs.get("j_coupling", 0.5)
            )
        elif model_name.lower() == "heisenberg":
            return HeisenbergModel(
                num_qubits=num_qubits,
                j_coupling=kwargs.get("j_coupling", 1.0),
                anisotropy=kwargs.get("anisotropy", 0.0)
            )
        elif model_name.lower() == "harmonic_oscillator":
            return QuantumHarmonicOscillator(
                num_qubits=num_qubits,
                frequency=kwargs.get("frequency", 1.0)
            )
        elif model_name.lower() == "phi_harmonic":
            return PhiHarmonicQuantumModel(
                num_qubits=num_qubits,
                phi_coupling=kwargs.get("phi_coupling", PHI)
            )
        else:
            raise ValueError(f"Unknown model: {model_name}")
    
    @staticmethod
    def list_available_models() -> List[str]:
        """
        List available quantum models
        
        Returns:
            List of available model names
        """
        return [
            "transverse_ising",
            "heisenberg",
            "harmonic_oscillator",
            "phi_harmonic"
        ]
