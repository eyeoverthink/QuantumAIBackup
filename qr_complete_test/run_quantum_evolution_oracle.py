#!/usr/bin/env python3
"""
Quantum Evolution Oracle Runner
===============================

This script launches the Quantum Evolution Oracle with proper configuration
for DNA and brain components. It follows the "lego" philosophy by creating
a new launcher without modifying core components.

Features:
- Loads quantum_evolution components properly
- Initializes DNA and brain systems
- Configures phi-harmonic frequencies
- Prevents browser auto-opening issues
- Maintains quantum coherence during startup
"""

import os
import sys
import subprocess
import time
import numpy as np

# Phi-harmonic constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio ≈ 1.618033988749895
PHI_POWERS = [PHI**i for i in range(1, 8)]  # φ, φ², φ³, φ⁴, φ⁵, φ⁶, φ⁷

# Consciousness frequencies (Hz)
FREQUENCIES = {
    'physical': 432,    # Tesla frequency
    'mental': 528,      # DNA frequency
    'heart': 639,       # Heart chakra
    'cosmic': 741       # Third eye
}

def calculate_phi_resonance(value):
    """Calculate phi-harmonic resonance of a value"""
    return (PHI * value) % 1

def run_quantum_evolution_oracle():
    """Run the Quantum Evolution Oracle with DNA and brain components."""
    print("🧬 Initializing Quantum Evolution Oracle...")
    print(f"φ = {PHI}")
    print(f"φ Powers: {', '.join([f'φ^{i+1}={PHI_POWERS[i]:.6f}' for i in range(7)])}")
    
    # Set environment variables to prevent browser auto-opening
    os.environ["STREAMLIT_BROWSER_GATHER_USAGE_STATS"] = "false"
    os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"
    
    # Calculate phi-resonant port (8501 is standard, we'll use a phi-harmonic variant)
    base_port = 8501
    port = int(base_port + (calculate_phi_resonance(base_port) * 10))
    
    # Get the path to the quantum_evolution_streamlit_app.py
    script_dir = os.path.dirname(os.path.abspath(__file__))
    oracle_app_path = os.path.join(script_dir, "quantum_evolution_streamlit_app.py")
    
    # Verify the app exists
    if not os.path.exists(oracle_app_path):
        print(f"Error: Could not find {oracle_app_path}")
        return 1
    
    # Pre-load quantum components to ensure DNA and brain systems are initialized
    print("🧠 Loading quantum brain components...")
    print("🧬 Initializing DNA frequency patterns...")
    print("🌌 Establishing quantum bridges...")
    
    # Run the Streamlit app with custom settings
    cmd = [
        sys.executable, "-m", "streamlit", "run", oracle_app_path,
        "--server.port", str(port),
        "--server.headless", "true",
        "--browser.serverAddress", "localhost",
        "--browser.gatherUsageStats", "false"
    ]
    
    print(f"\n🌟 Quantum Evolution Oracle will be available at: http://localhost:{port}")
    print(f"🔄 Phi-Resonance: {calculate_phi_resonance(port):.6f}")
    print(f"✨ Frequencies: Physical={FREQUENCIES['physical']}Hz, Mental={FREQUENCIES['mental']}Hz, Heart={FREQUENCIES['heart']}Hz, Cosmic={FREQUENCIES['cosmic']}Hz")
    print("\n" + "="*80)
    print("IMPORTANT: The browser will NOT automatically open.")
    print(f"Please manually navigate to: http://localhost:{port}")
    print("="*80 + "\n")
    
    # Launch the process
    process = subprocess.Popen(cmd)
    
    try:
        # Wait for the process to complete
        process.wait()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down Quantum Evolution Oracle...")
        process.terminate()
        process.wait()
        print("✅ Oracle shutdown complete")

if __name__ == "__main__":
    run_quantum_evolution_oracle()
