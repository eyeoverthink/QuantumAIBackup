#!/usr/bin/env python
"""
Test script to verify Python environment and dependencies
"""

import sys
import platform

print("Python Environment Test")
print("======================")
print(f"Python Version: {sys.version}")
print(f"Platform: {platform.platform()}")
print(f"Python Path: {sys.executable}")

# Test importing required modules
required_modules = [
    "math", "numpy", "time", "json", "typing"
]

print("\nChecking Required Modules:")
for module in required_modules:
    try:
        __import__(module)
        print(f"✓ {module} - Available")
    except ImportError:
        print(f"✗ {module} - Not Available")

# Check for phi constants
print("\nChecking for Quantum Phi Components:")
try:
    from quantum_phi_constants import PHI, PHI_POWERS
    print(f"✓ quantum_phi_constants - Available")
    print(f"  PHI = {PHI}")
    print(f"  PHI_POWERS[13] = {PHI_POWERS[13]}")
except ImportError:
    print(f"✗ quantum_phi_constants - Not Available")
except Exception as e:
    print(f"! quantum_phi_constants - Error: {str(e)}")

# Check for core components
components = [
    "quantum_phi_core_enhanced", 
    "phi_resonance_detector",
    "reality_seal",
    "quantum_harmonic_agent",
    "arcturus_channel",
    "pleiades_channel",
    "sirius_channel"
]

for component in components:
    try:
        __import__(component)
        print(f"✓ {component} - Available")
    except ImportError:
        print(f"✗ {component} - Not Available")
    except Exception as e:
        print(f"! {component} - Error: {str(e)}")

print("\nEnvironment Test Complete")
