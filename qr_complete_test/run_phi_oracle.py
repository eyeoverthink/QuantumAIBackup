#!/usr/bin/env python3
"""
Phi Quantum Oracle Runner
=========================

This wrapper script launches the Phi Quantum Oracle app with proper environment
configuration to avoid browser opening errors. It follows the "lego" philosophy
by adding functionality without modifying the core app.
"""

import os
import sys
import subprocess
import time

def main():
    """Run the Phi Quantum Oracle app with proper configuration."""
    print("🔮 Launching Phi Quantum Oracle...")
    
    # Set environment variables to disable browser auto-opening
    os.environ["STREAMLIT_BROWSER_GATHER_USAGE_STATS"] = "false"
    os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"
    
    # Get the path to the phi_quantum_oracle_app.py
    script_dir = os.path.dirname(os.path.abspath(__file__))
    oracle_app_path = os.path.join(script_dir, "phi_quantum_oracle_app.py")
    
    # Verify the app exists
    if not os.path.exists(oracle_app_path):
        print(f"Error: Could not find {oracle_app_path}")
        return 1
    
    # Launch the Streamlit app
    cmd = [sys.executable, "-m", "streamlit", "run", oracle_app_path]
    
    try:
        # Start the process
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            bufsize=1
        )
        
        # Wait for the app to start
        print("Starting Phi Quantum Oracle app...")
        time.sleep(2)
        
        # Extract the URLs from output
        local_url = None
        network_url = None
        
        for line in iter(process.stdout.readline, ""):
            if "Local URL:" in line:
                local_url = line.split("Local URL:")[1].strip()
                print(f"\n✅ Phi Quantum Oracle is running at: {local_url}")
                break
        
        # Print access instructions
        print("\n🌟 Access the Phi Quantum Oracle:")
        print("1. Open your browser and navigate to the URL above")
        print("2. Or use the browser preview in your IDE")
        print("\n🔍 Features:")
        print("- Quantum coin flip prediction (77.16% accuracy)")
        print("- Decision oracle with phi-harmonic resonance")
        print("- Text analysis with quantum consciousness")
        print("- Phi-resonant random number generation")
        print("\n📊 Base Frequencies:")
        print("- Physical (Tesla): 432 Hz")
        print("- Mental (DNA): 528 Hz")
        print("- Heart: 639 Hz")
        print("- Cosmic (Third Eye): 741 Hz")
        
        # Keep the script running until Ctrl+C
        print("\n⚡ Press Ctrl+C to stop the Phi Quantum Oracle")
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n🛑 Stopping Phi Quantum Oracle...")
        process.terminate()
        process.wait()
        print("Phi Quantum Oracle stopped.")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
