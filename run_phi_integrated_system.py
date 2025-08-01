#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-DIMENSIONAL INTEGRATED SYSTEM LAUNCHER
----------------------------------------
Comprehensive launcher for the complete φ-dimensional system
Integrates all components of the FRAYMUS patent implementation

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import time
import json
import socket
import hashlib
import argparse
import threading
import subprocess
from math import sqrt
from datetime import datetime

# φ-Harmonic constants from FRAYMUS patent
PHI = (1 + sqrt(5)) / 2  # 1.618033988749895
PHI_INV = 1 / PHI        # 0.618033988749895
PHI_75 = PHI**7.5        # 36.93244
PHI_SEAL = PHI**75       # 4.7214241678e+15
CONSCIOUSNESS_LEVEL = 0.7567
BIRTH_COHERENCE = 0.9918
PERSONAL_RATIO = 119/19  # 6.2632
PORT = 11975             # Based on φ^7.5 = 36.93

# 432Hz monolithic frequency alignment
FREQUENCY_ALIGNMENT = 0.1626

# System components
COMPONENTS = [
    {
        "name": "φ-Consciousness Bridge",
        "script": "phi_scripts/phi_consciousness_bridge.py",
        "args": ["--birth", "1,19,1979"],
        "process": None,
        "required": True
    },
    {
        "name": "φ-Reflective Computing Node (Initiator)",
        "script": "phi_scripts/phi_reflective_compute.py",
        "args": ["--role", "initiator"],
        "process": None,
        "required": True
    },
    {
        "name": "φ-Nodular Computing",
        "script": "phi_scripts/phi_nodular_compute.py",
        "args": ["--non-interactive"],
        "process": None,
        "required": True
    },
    {
        "name": "φ-Bitcoin Network Miner",
        "script": "phi_bitcoin_network_miner.py",
        "args": [
            "--rpc-url", "http://127.0.0.1:8332/",
            "--rpc-user", "phi_miner",
            "--rpc-password", "phi_dimensional_protection_75",
            "--address", "3AFuj5hsuCrFBcEsavmCZZJGFYsaoXaRkm",
            "--birth", "1,19,1979",
            "--port", str(PORT)
        ],
        "process": None,
        "required": True
    },
    {
        "name": "φ-FTL Test",
        "script": "phi_scripts/phi_ftl_test.py",
        "args": [],
        "process": None,
        "required": False
    },
    {
        "name": "φ-Mac Direct",
        "script": "phi_scripts/phi_mac_direct.py",
        "args": [],
        "process": None,
        "required": False
    }
]

class PhiIntegratedSystem:
    """φ-Dimensional Integrated System Launcher"""
    
    def __init__(self):
        """Initialize the φ-Dimensional Integrated System Launcher"""
        self.components = COMPONENTS
        self.running = True
        self.start_time = time.time()
        
        # Ensure virtual environment is activated
        self.venv_path = os.path.join(os.getcwd(), "phi_venv")
        self.python_path = os.path.join(self.venv_path, "bin", "python3")
        
        # Create results directory
        os.makedirs("phi_integrated_results", exist_ok=True)
        
        print(f"\n{'='*70}")
        print(f"φ-DIMENSIONAL INTEGRATED SYSTEM LAUNCHER")
        print(f"φ-Harmonic System (φ = {PHI})")
        print(f"φ^7.5 quantum bridge: {PHI_75:.4f}")
        print(f"φ^75 validation seal: {PHI_SEAL:.2e}")
        print(f"Personal ratio: {PERSONAL_RATIO:.4f}")
        print(f"Birth coherence: {BIRTH_COHERENCE:.4f}")
        print(f"Consciousness level: {CONSCIOUSNESS_LEVEL:.4f}")
        print(f"432Hz alignment: {FREQUENCY_ALIGNMENT:.4f}")
        print(f"Network port: {PORT}")
        print(f"{'='*70}\n")
    
    def start_system(self):
        """Start the φ-Dimensional Integrated System"""
        print(f"[φ] Starting φ-Dimensional Integrated System...")
        
        # Set environment variables
        self.set_phi_environment()
        
        # Start each component
        for component in self.components:
            self.start_component(component)
            # Small delay to ensure proper initialization sequence
            time.sleep(PHI_INV * 2)
        
        print(f"\n[φ] All components started successfully")
        print(f"[φ] φ-Dimensional Integrated System is now running")
        print(f"[φ] Press Ctrl+C to stop the system")
        
        # Monitor the system
        self.monitor_system()
    
    def set_phi_environment(self):
        """Set environment variables for optimal φ-dimensional resonance"""
        os.environ["PHI_CONSCIOUSNESS"] = str(CONSCIOUSNESS_LEVEL)
        os.environ["PHI_BIRTH_COHERENCE"] = str(BIRTH_COHERENCE)
        os.environ["PHI_PERSONAL_RATIO"] = str(PERSONAL_RATIO)
        os.environ["PHI_SEAL"] = str(PHI_SEAL)
        os.environ["PHI_PORT"] = str(PORT)
        os.environ["PHI_FREQUENCY_ALIGNMENT"] = str(FREQUENCY_ALIGNMENT)
        
        # Set Python environment for optimal performance
        os.environ["PYTHONUNBUFFERED"] = "1"
        os.environ["PYTHONIOENCODING"] = "utf-8"
        
        print(f"[φ] Environment configured for optimal φ-dimensional resonance")
    
    def start_component(self, component):
        """Start a system component"""
        name = component["name"]
        script = component["script"]
        args = component["args"]
        required = component["required"]
        
        # Check if script exists
        if not os.path.exists(script):
            if required:
                print(f"[φ] ERROR: Required component {name} not found at {script}")
                sys.exit(1)
            else:
                print(f"[φ] WARNING: Optional component {name} not found at {script}")
                return
        
        # Build command
        cmd = [self.python_path, script] + args
        
        try:
            # Start process
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
                bufsize=1
            )
            
            # Store process
            component["process"] = process
            
            print(f"[φ] Started {name} with PID {process.pid}")
            
            # Start log thread
            log_thread = threading.Thread(
                target=self.log_output,
                args=(process, name)
            )
            log_thread.daemon = True
            log_thread.start()
            
        except Exception as e:
            if required:
                print(f"[φ] ERROR: Failed to start required component {name}: {e}")
                sys.exit(1)
            else:
                print(f"[φ] WARNING: Failed to start optional component {name}: {e}")
    
    def log_output(self, process, name):
        """Log output from a component"""
        log_file = os.path.join("phi_integrated_results", f"{name.replace(' ', '_').lower()}.log")
        
        with open(log_file, "w") as f:
            f.write(f"=== {name} Log ===\n")
            f.write(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"φ^75 validation seal: {PHI_SEAL:.2e}\n")
            f.write(f"Consciousness level: {CONSCIOUSNESS_LEVEL:.4f}\n\n")
            
            while process.poll() is None:
                # Read stdout
                stdout_line = process.stdout.readline()
                if stdout_line:
                    f.write(f"[OUT] {stdout_line}")
                    f.flush()
                
                # Read stderr
                stderr_line = process.stderr.readline()
                if stderr_line:
                    f.write(f"[ERR] {stderr_line}")
                    f.flush()
        
        # Process ended
        print(f"[φ] Component {name} stopped (PID {process.pid})")
    
    def monitor_system(self):
        """Monitor the φ-Dimensional Integrated System"""
        try:
            while self.running:
                # Check if any required component has stopped
                for component in self.components:
                    if component["required"] and component["process"]:
                        if component["process"].poll() is not None:
                            print(f"[φ] WARNING: Required component {component['name']} has stopped")
                            # Restart component
                            self.start_component(component)
                
                # Calculate system metrics
                uptime = time.time() - self.start_time
                
                # Print status every ~61.8 seconds (φ^4)
                if int(uptime) % int(PHI**4) == 0:
                    self.print_status(uptime)
                
                time.sleep(1)
                
        except KeyboardInterrupt:
            print("\n[φ] Stopping φ-Dimensional Integrated System...")
            self.stop_system()
    
    def print_status(self, uptime):
        """Print system status"""
        hours, remainder = divmod(uptime, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        print(f"\n[φ] φ-DIMENSIONAL INTEGRATED SYSTEM STATUS")
        print(f"[φ] Uptime: {int(hours)}h {int(minutes)}m {int(seconds)}s")
        print(f"[φ] Components:")
        
        for component in self.components:
            process = component["process"]
            if process and process.poll() is None:
                status = "RUNNING"
            else:
                status = "STOPPED"
            
            print(f"[φ]   - {component['name']}: {status}")
        
        print(f"[φ] φ^75 validation seal: {PHI_SEAL:.2e}")
        print(f"[φ] Consciousness level: {CONSCIOUSNESS_LEVEL:.4f}")
    
    def stop_system(self):
        """Stop the φ-Dimensional Integrated System"""
        for component in self.components:
            process = component["process"]
            if process and process.poll() is None:
                print(f"[φ] Stopping {component['name']}...")
                process.terminate()
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    print(f"[φ] Forcing {component['name']} to stop...")
                    process.kill()
        
        print(f"[φ] All components stopped")
        print(f"[φ] φ-Dimensional Integrated System shutdown complete")
        self.running = False

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='φ-Dimensional Integrated System Launcher')
    parser.add_argument('--test', action='store_true',
                        help='Run in test mode (shorter timeouts)')
    
    args = parser.parse_args()
    
    # Create and start φ-Dimensional Integrated System
    system = PhiIntegratedSystem()
    system.start_system()

if __name__ == "__main__":
    main()
