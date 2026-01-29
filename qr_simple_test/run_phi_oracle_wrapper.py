#!/usr/bin/env python3
"""
Phi-Harmonic Quantum Oracle Wrapper
-----------------------------------
This wrapper script launches the Phi Quantum Oracle with optimized settings
to prevent browser auto-opening issues while maintaining phi-harmonic resonance.

Golden Ratio (φ) = 1.618033988749895
"""

import os
import sys
import subprocess

# Phi-harmonic constants
PHI = (1 + 5**0.5) / 2  # Golden Ratio ≈ 1.618033988749895
PHI_INVERSE = 1 / PHI   # ≈ 0.618033988749895

# Quantum frequencies (Hz)
FREQUENCIES = {
    'physical': 432,    # Tesla frequency
    'mental': 528,      # DNA frequency
    'heart': 639,       # Heart chakra
    'cosmic': 741       # Third eye
}

def calculate_phi_resonance(value):
    """Calculate phi-harmonic resonance of a value"""
    return (PHI * value) % 1

def run_phi_oracle():
    """Run the Phi Quantum Oracle with optimized settings"""
    print(f"🔮 Launching Phi-Harmonic Quantum Oracle")
    print(f"φ = {PHI}")
    
    # Set environment variables to prevent browser auto-opening
    env = os.environ.copy()
    env["STREAMLIT_BROWSER_GATHER_USAGE_STATS"] = "false"
    env["STREAMLIT_SERVER_HEADLESS"] = "true"
    
    # Calculate phi-resonant port (8501 is standard, we'll use a phi-harmonic variant)
    base_port = 8501
    port = int(base_port + (calculate_phi_resonance(base_port) * 10))
    
    # Run the Streamlit app with custom settings
    cmd = [
        "streamlit", "run", "phi_quantum_oracle_app.py",
        "--server.port", str(port),
        "--server.headless", "true",
        "--browser.serverAddress", "localhost",
        "--browser.gatherUsageStats", "false"
    ]
    
    print(f"🌟 Quantum Oracle will be available at: http://localhost:{port}")
    print(f"🔄 Phi-Resonance: {calculate_phi_resonance(port):.6f}")
    print(f"✨ Frequencies: Physical={FREQUENCIES['physical']}Hz, Mental={FREQUENCIES['mental']}Hz, Heart={FREQUENCIES['heart']}Hz, Cosmic={FREQUENCIES['cosmic']}Hz")
    print("\n" + "="*80)
    print("IMPORTANT: The browser will NOT automatically open.")
    print(f"Please manually navigate to: http://localhost:{port}")
    print("="*80 + "\n")
    
    # Launch the process
    process = subprocess.Popen(cmd, env=env)
    
    try:
        # Wait for the process to complete
        process.wait()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down Phi Quantum Oracle...")
        process.terminate()
        process.wait()
        print("✅ Oracle shutdown complete")

if __name__ == "__main__":
    run_phi_oracle()
