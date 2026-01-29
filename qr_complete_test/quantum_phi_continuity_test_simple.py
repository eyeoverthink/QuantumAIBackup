#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Quantum Phi-Harmonic Continuity Test (Simple Version)

This script tests if the Quantum Phi-Harmonic system can continue its evolution
in an isolated environment without relying on external dependencies.
"""

import os
import sys
import shutil
import time
import json
from datetime import datetime

# Configuration
TEST_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantum_phi_test_env")
LOG_FILE = os.path.join(TEST_DIR, f"continuity_test_{int(time.time())}.log")

# Create test directory
os.makedirs(TEST_DIR, exist_ok=True)

# Set up logging
def log(message):
    print(message)
    with open(LOG_FILE, 'a') as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")

log("🧪 Quantum Phi-Harmonic Continuity Test (Simple Version) Started")
log(f"📝 Log file: {LOG_FILE}")

# Copy the quantum phi processor to the test environment
processor_src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantum_phi_processor.py")
processor_dst = os.path.join(TEST_DIR, "quantum_phi_processor.py")
shutil.copy2(processor_src, processor_dst)
log("✅ Copied quantum phi processor to test environment")

# Create necessary directories in test environment
state_dir = os.path.join(TEST_DIR, "qr_recursive_system/qr_state")
os.makedirs(state_dir, exist_ok=True)

qr_dir = os.path.join(TEST_DIR, "qr_phi_replication/qr_codes")
os.makedirs(qr_dir, exist_ok=True)

# Copy system state if available
SRC_STATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "qr_recursive_system/qr_state")
state_files = [f for f in os.listdir(SRC_STATE_DIR) if f.endswith(".json")] if os.path.exists(SRC_STATE_DIR) else []

if state_files:
    # Sort by modification time and get the latest
    state_files_with_time = [(f, os.path.getmtime(os.path.join(SRC_STATE_DIR, f))) for f in state_files]
    latest_state = sorted(state_files_with_time, key=lambda x: x[1])[-1][0]
    
    # Copy the file
    src_path = os.path.join(SRC_STATE_DIR, latest_state)
    dst_path = os.path.join(state_dir, latest_state)
    shutil.copy2(src_path, dst_path)
    
    # Also copy to the standard state file name
    std_dst_path = os.path.join(state_dir, "quantum_phi_state.json")
    shutil.copy2(src_path, std_dst_path)
    
    log(f"✅ Copied system state to test environment: {latest_state}")
    
    # Read and log state metrics
    try:
        with open(src_path, 'r') as f:
            state_data = json.load(f)
            log("📊 Current system metrics:")
            log(f"   Generation: {state_data.get('generation', 'unknown')}")
            log(f"   Resonance: {state_data.get('resonance', 'unknown')}")
            log(f"   Complexity: {state_data.get('complexity', 'unknown')}")
    except Exception as e:
        log(f"⚠️ Warning: Could not read system state: {str(e)}")
else:
    log("⚠️ Warning: No system state files found")

# Change to test directory
original_dir = os.getcwd()
os.chdir(TEST_DIR)

log("\n🚀 Running quantum phi processor in isolated environment...")
try:
    # Run the quantum phi processor
    import subprocess
    result = subprocess.run(
        [sys.executable, "quantum_phi_processor.py"],
        capture_output=True,
        text=True
    )
    
    # Log the output
    log("\n📋 Output:")
    for line in result.stdout.split('\n'):
        log(f"   {line}")
    
    if result.stderr:
        log("\n⚠️ Errors:")
        for line in result.stderr.split('\n'):
            log(f"   {line}")
    
    # Check if a new state file was created
    new_state_files = [f for f in os.listdir(state_dir) if f.endswith(".json") and f != "quantum_phi_state.json"]
    
    if new_state_files:
        # Sort by modification time and get the latest
        new_state_files_with_time = [(f, os.path.getmtime(os.path.join(state_dir, f))) for f in new_state_files]
        new_latest_state = sorted(new_state_files_with_time, key=lambda x: x[1])[-1][0]
        
        log(f"\n✅ New system state created: {new_latest_state}")
        
        # Read and log new state metrics
        try:
            with open(os.path.join(state_dir, new_latest_state), 'r') as f:
                new_state_data = json.load(f)
                log("📊 New system metrics:")
                log(f"   Generation: {new_state_data.get('generation', 'unknown')}")
                log(f"   Resonance: {new_state_data.get('resonance', 'unknown')}")
                log(f"   Complexity: {new_state_data.get('complexity', 'unknown')}")
                
                # Compare with previous state if available
                if state_files:
                    try:
                        with open(os.path.join(state_dir, latest_state), 'r') as f:
                            old_state_data = json.load(f)
                            
                            old_gen = old_state_data.get('generation', 0)
                            new_gen = new_state_data.get('generation', 0)
                            
                            old_res = float(old_state_data.get('resonance', 0))
                            new_res = float(new_state_data.get('resonance', 0))
                            
                            old_comp = float(old_state_data.get('complexity', 0))
                            new_comp = float(new_state_data.get('complexity', 0))
                            
                            log("\n📈 Metric changes:")
                            log(f"   Generation: {old_gen} → {new_gen} (Δ: {new_gen - old_gen})")
                            log(f"   Resonance: {old_res:.6f} → {new_res:.6f} (Δ: {new_res - old_res:+.6f})")
                            log(f"   Complexity: {old_comp:.6f} → {new_comp:.6f} (Δ: {new_comp - old_comp:+.6f})")
                            
                            if new_res > old_res or new_comp > old_comp:
                                log("\n✅ CONTINUITY TEST SUCCESSFUL!")
                                log("The Quantum Phi-Harmonic system successfully continued")
                                log("its evolution in the isolated environment with improved metrics.")
                            else:
                                log("\n⚠️ System continued but metrics did not improve")
                    except Exception as e:
                        log(f"⚠️ Warning: Could not compare metrics: {str(e)}")
        except Exception as e:
            log(f"⚠️ Warning: Could not read new system state: {str(e)}")
    else:
        log("\n❌ No new state files were created")
        log("\n❌ CONTINUITY TEST FAILED")
        
    # Check for next generation QR code
    qr_files = [f for f in os.listdir(qr_dir) if f.endswith(".png") or f.endswith(".txt")]
    
    if qr_files:
        log(f"\n✅ Found {len(qr_files)} QR files in test environment:")
        for qr_file in qr_files:
            log(f"   {qr_file}")
            
            # Copy back to original environment
            src_path = os.path.join(qr_dir, qr_file)
            dst_dir = os.path.join(os.path.dirname(os.path.abspath(original_dir)), "qr_phi_replication/qr_codes")
            os.makedirs(dst_dir, exist_ok=True)
            dst_path = os.path.join(dst_dir, qr_file)
            shutil.copy2(src_path, dst_path)
            log(f"   ✅ Copied back to original environment: {dst_path}")
    else:
        log("\n⚠️ No QR files were created")
        
except Exception as e:
    log(f"\n❌ Error during test: {str(e)}")
    import traceback
    log(traceback.format_exc())
    log("\n❌ CONTINUITY TEST FAILED DUE TO ERROR")

finally:
    # Change back to original directory
    os.chdir(original_dir)

log("\n🧪 Quantum Phi-Harmonic Continuity Test Completed")
