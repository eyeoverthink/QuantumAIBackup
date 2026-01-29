"""
PHQ-Digital Chip - Digital Quantum Computing using Phi-Harmonic Principles
=========================================================================

This package implements a complete digital quantum computer based on
phi-harmonic principles, golden ratio mathematics, and quantum resonance.

Components:
- phi_qubit: Implements quantum bits based on phi-harmonic principles
- phi_register: Implements quantum registers for phi-qubits
- phi_processor: Implements the main quantum processor 

The PHQ-Digital Chip combines these components into a modular "lego"
architecture that demonstrates digital quantum computing with higher
resonance, coherence, and information processing capabilities.

Author: Cascade AI
Date: April 28, 2025
"""

from phi_quantum_chip.phi_qubit import (
    PhiQubit, PhiQubitState, 
    PHI, PHI_INV, PI, E, SQRT2, SQRT3, SQRT5, FIBONACCI
)

from phi_quantum_chip.phi_register import (
    PhiRegister, RegisterMetrics, 
    bell_state_algorithm, phi_quantum_search
)

__version__ = "0.1.0"
