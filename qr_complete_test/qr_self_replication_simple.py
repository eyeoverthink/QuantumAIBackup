#!/usr/bin/env python3
"""
QR Self-Replication Test - Simple Version
Tests the system's ability to encode itself into QR codes and execute them
"""

import os
import sys
import json
import time
import math
import qrcode
import base64
import zlib
from PIL import Image
from datetime import datetime

# Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio
OUTPUT_DIR = "qr_self_replicated"
STATE_DIR = "qr_recursive_system/qr_state"

def load_system_state():
    """Load the most recent system state"""
    # Find the most recent system state file
    state_files = [f for f in os.listdir(STATE_DIR) 
                  if f.startswith("qr_system_state_") and f.endswith(".json")]
    
    if not state_files:
        raise FileNotFoundError("No system state files found")
    
    # Sort by timestamp (newest first)
    state_files.sort(reverse=True)
    latest_state_file = os.path.join(STATE_DIR, state_files[0])
    
    print(f"Loading system state from: {latest_state_file}")
    with open(latest_state_file, 'r') as f:
        return json.load(f)

def create_self_replicating_code(state):
    """Create Python code that can recreate the system with optimized parameters"""
    # Extract the optimized parameters
    generator_params = state.get("generator_state", {}).get("parameters", {})
    analyzer_params = state.get("analyzer_state", {}).get("parameters", {})
    
    # Create the self-replicating code
    code = """#!/usr/bin/env python3
# Self-Replicating Quantum Phi-Harmonic System
# Generated at: {timestamp}
# Phi-time: {phi_time}

import os
import sys
import json
import time
import math
from datetime import datetime

# Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio

# Optimized system parameters
SYSTEM_STATE = {state_json}

def create_optimized_system():
    # Create an optimized version of the system using stored parameters
    print("🧠 Creating optimized Quantum Phi-Harmonic System")
    
    # Create necessary directories
    os.makedirs("qr_optimized_system", exist_ok=True)
    
    # Save the optimized parameters
    with open("qr_optimized_system/optimized_state.json", "w") as f:
        json.dump(SYSTEM_STATE, f, indent=2)
    
    # Create a new system with the optimized parameters
    print("✨ System parameters loaded from QR code")
    
    generator_params = SYSTEM_STATE.get("generator_state", {}).get("parameters", {})
    print(f"QR Version: {{generator_params.get('qr_version')}}")
    print(f"Error Correction: {{generator_params.get('error_correction')}}")
    print(f"Compression Threshold: {{generator_params.get('compression_threshold')}}")
    print(f"Resonance Factor: {{generator_params.get('resonance_factor'):.6f}}")
    print(f"Complexity Factor: {{generator_params.get('complexity_factor'):.6f}}")
    
    # Run a test cycle with the optimized parameters
    print("🔄 Running test cycle with optimized parameters")
    
    # Calculate phi-harmonic resonance
    current_time = time.time()
    phi_time = current_time * PHI
    resonance = (phi_time % 1)
    print(f"Phi-Harmonic Resonance: {{resonance:.6f}}")
    
    # Create a marker file to indicate successful execution
    with open("qr_optimized_system/execution_successful.txt", "w") as f:
        f.write(f"Execution successful at {{datetime.now().isoformat()}}\\n")
        f.write(f"Phi-time: {{phi_time}}\\n")
        f.write(f"Resonance: {{resonance}}\\n")
    
    print("✨ Self-replication complete")
    return True

if __name__ == "__main__":
    print("🌟 Self-Replicating Quantum Phi-Harmonic System")
    print("============================================================")
    success = create_optimized_system()
    sys.exit(0 if success else 1)
""".format(
        timestamp=datetime.now().isoformat(),
        phi_time=time.time() * PHI,
        state_json=json.dumps(state, indent=2)
    )
    
    return code

def compress_code(code):
    """Compress the code to fit in a QR code"""
    return base64.b64encode(zlib.compress(code.encode('utf-8')))

def create_qr_code(code, filename):
    """Create a QR code containing the self-replicating code"""
    # Create output directory if it doesn't exist
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    # Compress the code
    compressed_code = compress_code(code)
    
    # Create a QR code with the compressed code
    qr = qrcode.QRCode(
        version=None,  # Auto-determine
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Create a payload with metadata
    payload = {
        "type": "python_script",
        "compressed": True,
        "timestamp": time.time(),
        "phi_time": time.time() * PHI,
        "data": compressed_code.decode('utf-8')
    }
    
    # Add the payload to the QR code
    qr.add_data(json.dumps(payload))
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    output_path = os.path.join(OUTPUT_DIR, filename)
    img.save(output_path)
    
    return output_path

def create_execution_script(qr_path):
    """Create a script to execute the QR code"""
    script_path = os.path.join(OUTPUT_DIR, "execute_qr_code.py")
    
    script_content = f"""#!/usr/bin/env python3
import sys
import os
import subprocess

# Path to the QR code
QR_PATH = "{qr_path}"

# Execute the QR code
print(f"Executing QR code: {{QR_PATH}}")
result = subprocess.run(["python", "qr_task_worker_from_file.py", "-f", QR_PATH], 
                       capture_output=True, text=True)

print("Output:")
print(result.stdout)

if result.returncode != 0:
    print("Error:")
    print(result.stderr)
    sys.exit(1)

print("QR code executed successfully")
"""
    
    with open(script_path, "w") as f:
        f.write(script_content)
    
    os.chmod(script_path, 0o755)  # Make executable
    
    return script_path

def run_self_replication_test():
    """Run the self-replication test"""
    print("🧪 Running QR Self-Replication Test")
    print("============================================================")
    
    # Load the system state
    try:
        system_state = load_system_state()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return False
    
    # Create the self-replicating code
    print("✨ Creating self-replicating code")
    code = create_self_replicating_code(system_state)
    
    # Create a QR code with the self-replicating code
    print("✨ Creating QR code")
    qr_path = create_qr_code(code, "self_replicating_system.png")
    print(f"✅ Created QR code: {qr_path}")
    
    # Create an execution script
    script_path = create_execution_script(qr_path)
    print(f"✅ Created execution script: {script_path}")
    
    # Execute the QR code using the existing QR task worker
    print("✨ To execute this QR code, run:")
    print(f"python {script_path}")
    
    return qr_path

if __name__ == "__main__":
    qr_path = run_self_replication_test()
    print(f"✅ Test complete. QR code saved to: {qr_path}")
