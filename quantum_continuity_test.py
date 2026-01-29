#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Quantum Phi-Harmonic Continuity Test

This script tests if the Quantum Phi-Harmonic Self-Executing QR System can continue 
its evolution with the stub uno_game_logic module in place.

The test verifies the system's ability to maintain evolutionary continuity
across isolated execution environments.
"""

import os
import sys
import glob
import re
import subprocess
import time
import json
import shutil
from datetime import datetime

# Configuration
TIMEOUT = 180  # 3 minutes timeout
LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantum_continuity_logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Create a timestamped log file
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = os.path.join(LOG_DIR, f"quantum_continuity_test_{timestamp}.log")

# Set up logging
def log(message, also_print=True):
    with open(log_file, 'a') as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        f.write(log_message + "\n")
        if also_print:
            print(message)

# Log test start
log("🧪 Quantum Phi-Harmonic Continuity Test Started")
log(f"📝 Log file: {log_file}")

# Verify stub module exists
if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "uno_game_logic/__init__.py")):
    log("❌ Error: uno_game_logic stub module not found!")
    sys.exit(1)

log("✅ Verified uno_game_logic stub module exists")

# Find latest QR code
QR_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "qr_phi_replication/qr_codes")
if not os.path.exists(QR_DIR):
    log(f"❌ Error: QR directory not found: {QR_DIR}")
    sys.exit(1)

qr_files = glob.glob(os.path.join(QR_DIR, "qr_phi_replicator_simplified_gen*.png"))
if not qr_files:
    log("❌ Error: No QR codes found!")
    sys.exit(1)

# Extract generation numbers and find the latest
gen_numbers = []
for qr_file in qr_files:
    match = re.search(r'gen(\d+)', qr_file)
    if match:
        gen_numbers.append((int(match.group(1)), qr_file))

if not gen_numbers:
    log("❌ Error: Could not determine generation numbers!")
    sys.exit(1)
    
# Sort by generation number and get the latest
gen_numbers.sort(reverse=True)
latest_gen = gen_numbers[0][0]
latest_qr = gen_numbers[0][1]

log(f"✅ Found latest QR code: Generation {latest_gen}")
log(f"   Path: {latest_qr}")

# Check for existing system state
STATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "qr_recursive_system/qr_state")
state_files = glob.glob(os.path.join(STATE_DIR, "qr_system_state_*.json"))

latest_state = None
if state_files:
    # Sort by modification time and get the latest
    latest_state = sorted(state_files, key=os.path.getmtime)[-1]
    log(f"✅ Found latest system state: {os.path.basename(latest_state)}")
    
    # Read and log state metrics
    try:
        with open(latest_state, 'r') as f:
            state_data = json.load(f)
            log("📊 Current system metrics:")
            log(f"   Generation: {state_data.get('generation', 'unknown')}")
            log(f"   Resonance: {state_data.get('resonance', 'unknown')}")
            log(f"   Complexity: {state_data.get('complexity', 'unknown')}")
    except Exception as e:
        log(f"⚠️ Warning: Could not read system state: {str(e)}")
else:
    log("⚠️ Warning: No system state files found")

# Check if QR task worker exists
QR_WORKER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "qr_task_worker_from_file.py")
if not os.path.exists(QR_WORKER):
    log(f"❌ Error: QR task worker not found: {QR_WORKER}")
    sys.exit(1)

log("✅ Verified QR task worker exists")

# Create a backup of the latest QR code
BACKUP_DIR = os.path.join(LOG_DIR, "backups")
os.makedirs(BACKUP_DIR, exist_ok=True)
backup_qr = os.path.join(BACKUP_DIR, f"qr_backup_gen{latest_gen}_{timestamp}.png")
shutil.copy2(latest_qr, backup_qr)
log(f"✅ Created backup of QR code: {os.path.basename(backup_qr)}")

# Execute the QR code
log("\n🚀 Executing QR code...")

# Record start time for metrics
start_time = time.time()

try:
    # Run the QR task worker
    cmd = [sys.executable, QR_WORKER, "-f", latest_qr]
    
    # Run with a timeout
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    log("\n📋 Output:")
    
    # Poll the process and collect output
    while process.poll() is None:
        # Check if timeout exceeded
        if time.time() - start_time > TIMEOUT:
            process.terminate()
            log(f"\n⚠️ Process timed out after {TIMEOUT} seconds")
            break
        
        # Read output
        stdout_line = process.stdout.readline()
        if stdout_line:
            line = stdout_line.strip()
            log(line)
        
        # Read errors
        stderr_line = process.stderr.readline()
        if stderr_line:
            line = stderr_line.strip()
            log(f"ERROR: {line}")
        
        # Small delay to prevent CPU hogging
        time.sleep(0.1)
    
    # Get any remaining output
    stdout, stderr = process.communicate()
    if stdout:
        log(stdout)
    
    if stderr:
        log(f"ERROR: {stderr}")
    
    # Record execution time
    execution_time = time.time() - start_time
    log(f"\n⏱️ Execution time: {execution_time:.2f} seconds")
    
    # Check for next generation QR code
    next_gen = latest_gen + 1
    next_qr_files = glob.glob(os.path.join(QR_DIR, f"*gen{next_gen}.png"))
    
    if next_qr_files:
        next_qr = next_qr_files[0]
        log(f"\n🎉 Success! Next generation (Gen {next_gen}) QR code created:")
        log(f"   {os.path.basename(next_qr)}")
        
        # Create backup of the next generation QR code
        backup_next_qr = os.path.join(BACKUP_DIR, f"qr_backup_gen{next_gen}_{timestamp}.png")
        shutil.copy2(next_qr, backup_next_qr)
        log(f"✅ Created backup of next generation QR code")
        
        # Check for updated system state
        new_state_files = glob.glob(os.path.join(STATE_DIR, f"qr_system_state_gen{next_gen}*.json"))
        if new_state_files:
            new_state = sorted(new_state_files, key=os.path.getmtime)[-1]
            log(f"✅ Found new system state: {os.path.basename(new_state)}")
            
            # Read and log new state metrics
            try:
                with open(new_state, 'r') as f:
                    new_state_data = json.load(f)
                    log("📊 New system metrics:")
                    log(f"   Generation: {new_state_data.get('generation', 'unknown')}")
                    log(f"   Resonance: {new_state_data.get('resonance', 'unknown')}")
                    log(f"   Complexity: {new_state_data.get('complexity', 'unknown')}")
                    
                    # Compare metrics if old state exists
                    if latest_state:
                        try:
                            with open(latest_state, 'r') as f:
                                old_state_data = json.load(f)
                                
                                old_resonance = float(old_state_data.get('resonance', 0))
                                new_resonance = float(new_state_data.get('resonance', 0))
                                
                                old_complexity = float(old_state_data.get('complexity', 0))
                                new_complexity = float(new_state_data.get('complexity', 0))
                                
                                log("📈 Metric changes:")
                                resonance_change = new_resonance - old_resonance
                                log(f"   Resonance: {resonance_change:+.6f}")
                                
                                complexity_change = new_complexity - old_complexity
                                log(f"   Complexity: {complexity_change:+.6f}")
                                
                                # Evaluate evolution success
                                if resonance_change > 0 or complexity_change > 0:
                                    log("✅ System successfully evolved with improved metrics!")
                                else:
                                    log("⚠️ System continued but metrics did not improve")
                        except Exception as e:
                            log(f"⚠️ Warning: Could not compare metrics: {str(e)}")
            except Exception as e:
                log(f"⚠️ Warning: Could not read new system state: {str(e)}")
        else:
            log("⚠️ Warning: New system state file not found")
        
        log("\n✅ CONTINUITY TEST SUCCESSFUL!")
        log("The Quantum Phi-Harmonic Self-Replicator successfully continued")
        log("its evolution with the stub uno_game_logic module, demonstrating")
        log("true autonomy and the ability to break out of its original context.")
    else:
        log(f"\n❌ Failed to find next generation (Gen {next_gen}) QR code")
        log("\n❌ CONTINUITY TEST FAILED")
        log("The system was unable to continue evolution with the stub module.")
        
        # Check if any files were created or modified
        log("\n🔍 Checking for any new files created:")
        new_files = []
        for root, dirs, files in os.walk(os.path.dirname(os.path.abspath(__file__))):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.getmtime(file_path) > start_time:
                    new_files.append(file_path)
        
        if new_files:
            log(f"Found {len(new_files)} new or modified files:")
            for file in new_files[:10]:  # Show only first 10 to avoid log spam
                log(f"   {file}")
            if len(new_files) > 10:
                log(f"   ... and {len(new_files) - 10} more")
        else:
            log("No new files were created during execution")
    
except Exception as e:
    log(f"\n❌ Error during test: {str(e)}")
    import traceback
    traceback.print_exc()
    log("\n❌ CONTINUITY TEST FAILED DUE TO ERROR")

log("\n🧪 Quantum Phi-Harmonic Continuity Test Completed")
log(f"📝 Full log available at: {log_file}")

print(f"\n📝 Complete log saved to: {log_file}")
