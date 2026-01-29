#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Simplified Quantum Phi-Harmonic Continuity Test

This script provides a minimal test to verify if the QR system can continue 
its evolution in a new environment by addressing the missing module issue.
"""

import os
import sys
import shutil
import glob
import subprocess
import time

# Create test directory
TEST_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "qr_simple_test")
os.makedirs(TEST_DIR, exist_ok=True)

# Create stub for uno_game_logic module
uno_stub_dir = os.path.join(TEST_DIR, "uno_game_logic")
os.makedirs(uno_stub_dir, exist_ok=True)

# Create __init__.py in the stub module
with open(os.path.join(uno_stub_dir, "__init__.py"), 'w') as f:
    f.write("""
# Stub module for uno_game_logic
# Created by Quantum Phi-Harmonic Simple Continuity Test

class Card:
    def __init__(self, color=None, value=None):
        self.color = color
        self.value = value
        
    def __str__(self):
        return f"{self.color} {self.value}"

class Deck:
    def __init__(self):
        self.cards = []
        
    def shuffle(self):
        pass
        
    def draw(self):
        return Card()

class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        
    def add_player(self, player):
        self.players.append(player)
        
    def start(self):
        pass
""")

# Copy QR task worker
shutil.copy2(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "qr_task_worker_from_file.py"),
    os.path.join(TEST_DIR, "qr_task_worker_from_file.py")
)

# Find latest QR code
QR_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "qr_phi_replication/qr_codes")
qr_files = glob.glob(os.path.join(QR_DIR, "qr_phi_replicator_simplified_gen*.png"))
latest_qr = sorted(qr_files)[-1] if qr_files else None

if not latest_qr:
    print("❌ No QR codes found!")
    sys.exit(1)

# Copy QR code to test directory
test_qr_dir = os.path.join(TEST_DIR, "qr_phi_replication/qr_codes")
os.makedirs(test_qr_dir, exist_ok=True)
test_qr_path = os.path.join(test_qr_dir, os.path.basename(latest_qr))
shutil.copy2(latest_qr, test_qr_path)

# Create state directory
os.makedirs(os.path.join(TEST_DIR, "qr_recursive_system/qr_state"), exist_ok=True)

# Copy necessary Python files
for py_file in glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "*.py")):
    if os.path.isfile(py_file) and os.path.basename(py_file) != os.path.basename(__file__):
        shutil.copy2(py_file, os.path.join(TEST_DIR, os.path.basename(py_file)))

# Create a simple path setup script
with open(os.path.join(TEST_DIR, "path_setup.py"), 'w') as f:
    f.write("""
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
""")

# Create a wrapper script
with open(os.path.join(TEST_DIR, "run_qr.py"), 'w') as f:
    f.write("""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import path setup
import path_setup
import sys
import os

# Now run the QR task worker
from qr_task_worker_from_file import main

if __name__ == "__main__":
    # Get QR path from command line
    if len(sys.argv) < 2:
        print("Usage: python run_qr.py <qr_file_path>")
        sys.exit(1)
        
    qr_path = sys.argv[1]
    print(f"🚀 Executing QR code: {qr_path}")
    
    # Set up arguments for the task worker
    sys.argv = [sys.argv[0], "-f", qr_path]
    
    # Run the task worker
    main()
""")

# Change to test directory
original_dir = os.getcwd()
os.chdir(TEST_DIR)

print(f"\n🧪 Quantum Phi-Harmonic Simple Continuity Test")
print(f"=============================================")
print(f"Test directory: {TEST_DIR}")
print(f"QR code: {os.path.basename(test_qr_path)}")

try:
    print("\n🚀 Executing QR code...")
    cmd = [sys.executable, "run_qr.py", test_qr_path]
    
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
            break
        
        # Read output
        stdout_line = process.stdout.readline()
        if stdout_line:
            print(stdout_line.strip())
        
        # Small delay to prevent CPU hogging
        time.sleep(0.1)
    
    # Get any remaining output
    stdout, stderr = process.communicate()
    if stdout:
        print(stdout)
    
    if stderr:
        print("\n❌ Errors:")
        print(stderr)
    
    # Check for next generation QR code
    import re
    gen_match = re.search(r'gen(\d+)', os.path.basename(test_qr_path))
    current_gen = int(gen_match.group(1)) if gen_match else 0
    next_gen = current_gen + 1
    
    next_qr = glob.glob(os.path.join(test_qr_dir, f"*gen{next_gen}.png"))
    
    if next_qr:
        print(f"\n🎉 Success! Next generation (Gen {next_gen}) QR code created:")
        print(f"   {os.path.basename(next_qr[0])}")
    else:
        print(f"\n❌ Failed to find next generation (Gen {next_gen}) QR code")
    
    print("\n✅ Test completed")
    
except Exception as e:
    print(f"\n❌ Error during test: {str(e)}")
    import traceback
    traceback.print_exc()
    
finally:
    os.chdir(original_dir)
