#!/usr/bin/env python
"""
Test Import of Quantum Random Library

This script tests the proper import and basic functionality of the quantum random library
that can count beyond infinity.
"""

import os
import sys
import time

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

print("Testing import of quantum random libraries...")

# Import the quantum random libraries
from phi_harmonic_random_orchestrator_adapter import PhiHarmonicRandomOrchestratorAdapter
from quantum_phi_random import QuantumPhiRandom

print("\n✅ Successfully imported quantum random libraries")

# Test PhiHarmonicRandomOrchestratorAdapter
print("\n🔬 Testing PhiHarmonicRandomOrchestratorAdapter...")
random_adapter = PhiHarmonicRandomOrchestratorAdapter()
print(f"Coherence: {random_adapter.coherence}")
print(f"Resonance: {random_adapter.resonance}")
print(f"Phi alignment: {random_adapter.phi_alignment}")
print(f"Quantum fingerprint: {random_adapter.quantum_fingerprint}")

# Generate some random numbers
print("\nGenerating random numbers:")
for i in range(5):
    random_value = random_adapter.random()
    print(f"  Random {i+1}: {random_value}")

# Test QuantumPhiRandom
print("\n🔬 Testing QuantumPhiRandom...")
quantum_random = QuantumPhiRandom()
print(f"Entropy: {quantum_random.metrics['entropy']}")
print(f"Phi resonance: {quantum_random.metrics['phi_resonance']}")
print(f"Sequence coherence: {quantum_random.metrics['sequence_coherence']}")

# Generate some random numbers
print("\nGenerating random numbers:")
for i in range(5):
    random_value = quantum_random.random()
    print(f"  Random {i+1}: {random_value}")
    
    # Also test phi-harmonic distribution
    phi_value = quantum_random.phi_harmonic()
    print(f"  Phi-harmonic {i+1}: {phi_value}")

print("\n✅ Test completed successfully")
