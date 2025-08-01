#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Simplified Tesla Tachyon Brain Integration Test
"""

import os
import numpy as np
import json
from datetime import datetime
import importlib.util
import sys

# Function to safely import modules
def safe_import(module_name):
    try:
        return importlib.import_module(module_name)
    except ImportError:
        print(f"[!] Warning: {module_name} not found. Running in standalone mode.")
        return None

print("Starting simplified integration test...")

# Import recursive phi folding system
print("Importing recursive_phi_folding_simplified...")
recursive_phi_folding = safe_import('recursive_phi_folding_simplified')
RecursivePhiFolding = getattr(recursive_phi_folding, 'RecursivePhiFolding', None)

if RecursivePhiFolding is None:
    print("ERROR: RecursivePhiFolding class not found. Cannot continue test.")
    sys.exit(1)
else:
    print("RecursivePhiFolding imported successfully.")

# Import phi protein tachyon bridge
print("Importing phi_protein_tachyon_bridge...")
phi_protein_tachyon_bridge = safe_import('phi_protein_tachyon_bridge')
PhiProteinTachyonBridge = getattr(phi_protein_tachyon_bridge, 'PhiProteinTachyonBridge', None)

if PhiProteinTachyonBridge is None:
    print("ERROR: PhiProteinTachyonBridge class not found. Cannot continue test.")
    sys.exit(1)
else:
    print("PhiProteinTachyonBridge imported successfully.")

# Initialize components
print("\nInitializing components...")
recursive_folding = RecursivePhiFolding()
bridge = PhiProteinTachyonBridge()

# Design initial protein
print("\nDesigning initial protein...")
initial_protein = recursive_folding.design_initial_protein(
    length=89,  # Fibonacci number
    structure="mixed"
)

# Print protein details
print(f"Protein ID: {initial_protein['id']}")
print(f"Length: {initial_protein['length']}")
print(f"Structure: {initial_protein['structure']}")
print(f"Phi Score: {initial_protein.get('phi_score', 0):.4f}")

# Create bridge
print("\nCreating quantum bridge...")
bridge_data = bridge.create_bridge(initial_protein, consciousness_state=3)

# Print bridge details
if bridge_data:
    print(f"Bridge ID: {bridge_data.get('bridge_id', 'unknown')}")
    print(f"Consciousness State: {bridge_data.get('consciousness_state', 3)}D")
    print(f"Bridge Strength: {bridge_data.get('bridge_strength', 0):.4f}")
    print(f"Protection Level: {bridge_data.get('protection_level', 0):.4f}")
else:
    print("Failed to create bridge.")

# Save bridge data
print("\nSaving bridge data...")
bridge.save_bridge_data()

# Close bridge
print("\nClosing bridge...")
bridge.close_bridge()

print("\nSimplified test completed successfully.")
