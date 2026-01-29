#!/bin/bash
# φ^75 Quantum Environment Launcher
# This script sets up the proper environment variables for the φ^75 Quantum Consciousness Network
# φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities

# Apply phi-harmonic resonance to environment variables
export PHI_HARMONIC_RESONANCE=0.618034
export QUANTUM_COHERENCE=0.991800
export PHI_DIMENSIONAL_SCALING="-2.00"

# Silence Tk deprecation warnings
export TK_SILENCE_DEPRECATION=1

# Set Python path to ensure proper module loading
export PYTHONPATH="${PYTHONPATH}:/usr/local/lib/python3.9/site-packages"

# Set display variables for proper GUI rendering
export _JAVA_OPTIONS="-Dsun.java2d.metal=true"
export NSHighResolutionCapable=1

echo "=== φ^75 QUANTUM ENVIRONMENT INITIALIZED ==="
echo "Phi-harmonic resonance: ${PHI_HARMONIC_RESONANCE} (exactly φ^-1)"
echo "Quantum coherence: ${QUANTUM_COHERENCE}"
echo "Dimensional scaling: φ^${PHI_DIMENSIONAL_SCALING}"
echo

# Run the specified Python script with the proper environment
if [ "$1" == "" ]; then
  echo "Usage: ./phi75_run_environment.sh <script_name.py>"
  exit 1
fi

/usr/bin/python3 "$1"
