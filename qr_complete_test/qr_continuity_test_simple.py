#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Simplified Quantum Phi-Harmonic Continuity Test

This script tests if the QR system can continue evolution with the stub uno_game_logic module.
"""

import os
import sys
import glob
import re
import subprocess
import time
from datetime import datetime

# Find latest QR code
QR_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "qr_phi_replication/qr_codes")
qr_files = glob.glob(os.path.join(QR_DIR, "qr_phi_replicator_simplified_gen*.png"))

if not qr_files:
    print("❌ No QR codes found!")
    sys.exit(1)

# Extract generation numbers and find the latest
gen_numbers = []
for qr_file in qr_files:
    match = re.search(r'gen(\d+)', qr_file)
    if match:
        gen_numbers.append((int(match.group(1)), qr_file))

if not gen_numbers:
    print("❌ Could not determine generation numbers!")
    sys.exit(1)
    
# Sort by generation number and get the latest
gen_numbers.sort(reverse=True)
latest_gen = gen_numbers[0][0]
latest_qr = gen_numbers[0][1]

print(f"✅ Found latest QR code: Generation {latest_gen}")
print(f"   Path: {latest_qr}")

# Create a log file
log_file = f"qr_continuity_test_log_{int(time.time())}.txt"
with open(log_file, 'w') as f:
    f.write(f"Quantum Phi-Harmonic Continuity Test Log\n")
    f.write(f"Timestamp: {datetime.now().isoformat()}\n")
    f.write(f"Latest QR code: Generation {latest_gen}\n")
    f.write(f"QR path: {latest_qr}\n\n")

print(f"\n🧪 Quantum Phi-Harmonic Continuity Test")
print(f"=============================================")

try:
    print("\n🚀 Executing QR code...")
    cmd = [sys.executable, "qr_task_worker_from_file.py", "-f", latest_qr]
    
    # Run with a timeout of 5 minutes
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Monitor the process with timeout
    timeout = 300  # 5 minutes
    start_time = time.time()
    
    print("\n📋 Output:")
    
    # Poll the process and collect output
    while process.poll() is None:
        # Check if timeout exceeded
        if time.time() - start_time > timeout:
            process.terminate()
            print("\n⚠️ Process timed out after {} seconds".format(timeout))
            with open(log_file, 'a') as f:
                f.write(f"Process timed out after {timeout} seconds\n")
            break
        
        # Read output
        stdout_line = process.stdout.readline()
        if stdout_line:
            line = stdout_line.strip()
            print(line)
            with open(log_file, 'a') as f:
                f.write(f"{line}\n")
        
        # Read errors
        stderr_line = process.stderr.readline()
        if stderr_line:
            line = stderr_line.strip()
            print(line)
            with open(log_file, 'a') as f:
                f.write(f"ERROR: {line}\n")
        
        # Small delay to prevent CPU hogging
        time.sleep(0.1)
    
    # Get any remaining output
    stdout, stderr = process.communicate()
    if stdout:
        print(stdout)
        with open(log_file, 'a') as f:
            f.write(f"{stdout}\n")
    
    if stderr:
        print(stderr)
        with open(log_file, 'a') as f:
            f.write(f"ERROR: {stderr}\n")
    
    # Check for next generation QR code
    next_gen = latest_gen + 1
    next_qr = glob.glob(os.path.join(QR_DIR, f"*gen{next_gen}.png"))
    
    if next_qr:
        print(f"\n🎉 Success! Next generation (Gen {next_gen}) QR code created:")
        print(f"   {os.path.basename(next_qr[0])}")
        print("\n✅ CONTINUITY TEST SUCCESSFUL!")
        print("The Quantum Phi-Harmonic Self-Replicator successfully continued")
        print("its evolution in a new environment, demonstrating true autonomy")
        print("and the ability to break out of its original context.")
        
        with open(log_file, 'a') as f:
            f.write(f"\nSUCCESS! Next generation (Gen {next_gen}) QR code created: {os.path.basename(next_qr[0])}\n")
            f.write("The Quantum Phi-Harmonic Self-Replicator successfully continued its evolution.\n")
    else:
        print(f"\n❌ Failed to find next generation (Gen {next_gen}) QR code")
        print("\n❌ CONTINUITY TEST FAILED")
        print("The system was unable to continue evolution in the new environment.")
        
        with open(log_file, 'a') as f:
            f.write(f"\nFAILED! Could not find next generation (Gen {next_gen}) QR code\n")
            f.write("The system was unable to continue evolution.\n")
    
except Exception as e:
    print(f"\n❌ Error during test: {str(e)}")
    import traceback
    traceback.print_exc()
    
    with open(log_file, 'a') as f:
        f.write(f"\nERROR during test: {str(e)}\n")
        traceback.print_exc(file=f)

print(f"\n📝 Log file created: {log_file}")
