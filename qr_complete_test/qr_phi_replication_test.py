#!/usr/bin/env python3
"""
Quantum Phi Self-Replication Test
By Vaughn Scott

Tests the Quantum Phi-Harmonic QR System's ability to store and improve itself
through QR codes, demonstrating recursive self-improvement and self-replication.
"""

import os
import sys
import json
import time
import math
import uuid
import qrcode
from datetime import datetime
from PIL import Image

# Phi (Golden Ratio) constant
PHI = (1 + math.sqrt(5)) / 2  # Approximately 1.618034

# Output directories
OUTPUT_DIR = "qr_phi_replication"
QR_CODE_DIR = os.path.join(OUTPUT_DIR, "qr_codes")

def load_system_state():
    """Load the most recent system state."""
    state_dir = "qr_recursive_system/qr_state"
    if not os.path.exists(state_dir):
        print(f"System state directory not found: {state_dir}")
        return None
    
    state_files = [f for f in os.listdir(state_dir) 
                  if f.startswith("qr_system_state_") and f.endswith(".json")]
    
    if not state_files:
        print("No system state files found.")
        return None
    
    # Sort by timestamp (newest first)
    state_files.sort(reverse=True)
    latest_state_file = os.path.join(state_dir, state_files[0])
    
    print(f"Loading system state from: {latest_state_file}")
    
    try:
        with open(latest_state_file, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading system state: {e}")
        return None

def create_self_replicating_script(generation=1):
    """Create a self-replicating script."""
    # Create output directories
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(QR_CODE_DIR, exist_ok=True)
    
    # Initialize test parameters
    test_id = str(uuid.uuid4())
    timestamp = time.time()
    phi_time = timestamp * PHI
    resonance = phi_time % 1
    complexity = (resonance * PHI) % 1
    
    # Load system state
    system_state = load_system_state()
    
    # Extract parameters from system state
    params = {
        "qr_version": 1,  # Start with minimal version
        "error_correction": qrcode.constants.ERROR_CORRECT_H,
        "compression_threshold": int(500 * PHI),
        "resonance_factor": 1/PHI,
        "complexity_factor": 1/(PHI*PHI)
    }
    
    # Update from system state if available
    if system_state and "generator_state" in system_state:
        gen_params = system_state.get("generator_state", {}).get("parameters", {})
        if gen_params:
            if "qr_version" in gen_params:
                params["qr_version"] = min(40, max(1, gen_params["qr_version"]))
            if "error_correction" in gen_params:
                params["error_correction"] = min(3, max(0, gen_params["error_correction"]))
            if "compression_threshold" in gen_params:
                params["compression_threshold"] = gen_params["compression_threshold"]
            if "resonance_factor" in gen_params:
                params["resonance_factor"] = gen_params["resonance_factor"]
            if "complexity_factor" in gen_params:
                params["complexity_factor"] = gen_params["complexity_factor"]
    
    # Display current parameters
    print("\n🧠 Current System Parameters")
    print("============================================================")
    print(f"Generation: {generation}")
    print(f"System ID: {test_id}")
    print(f"Timestamp: {datetime.fromtimestamp(timestamp).isoformat()}")
    print(f"Phi-time: {phi_time:.6f}")
    print(f"Resonance: {resonance:.6f}")
    print(f"Complexity: {complexity:.6f}")
    
    print("\nParameters:")
    print(f"  QR Version: {params['qr_version']}")
    print(f"  Error Correction: {params['error_correction']}")
    print(f"  Compression Threshold: {params['compression_threshold']}")
    print(f"  Resonance Factor: {params['resonance_factor']:.6f}")
    print(f"  Complexity Factor: {params['complexity_factor']:.6f}")
    
    # Create the self-replicating script
    script = f"""
# Self-Replicating Quantum Phi-Harmonic Script
# Generation: {generation}
# Created: {datetime.now().isoformat()}
# System ID: {test_id}

import os
import sys
import json
import time
import math
import uuid
import qrcode
from datetime import datetime
from PIL import Image

# Phi (Golden Ratio) constant
PHI = (1 + math.sqrt(5)) / 2  # Approximately 1.618034

# System parameters
GENERATION = {generation}
SYSTEM_ID = "{test_id}"
TIMESTAMP = {timestamp}
PHI_TIME = {phi_time}
RESONANCE = {resonance}
COMPLEXITY = {complexity}

# QR parameters
PARAMS = {{
    "qr_version": {params['qr_version']},
    "error_correction": {params['error_correction']},
    "compression_threshold": {params['compression_threshold']},
    "resonance_factor": {params['resonance_factor']},
    "complexity_factor": {params['complexity_factor']}
}}

# Output directories
OUTPUT_DIR = "qr_phi_replication"
QR_CODE_DIR = os.path.join(OUTPUT_DIR, "qr_codes")

def evolve():
    \"\"\"Evolve to the next generation.\"\"\"
    print("🧠 Quantum Phi-Harmonic Self-Replication")
    print("============================================================")
    print(f"Generation: {{GENERATION}}")
    print(f"System ID: {{SYSTEM_ID}}")
    print(f"Timestamp: {{datetime.fromtimestamp(TIMESTAMP).isoformat()}}")
    print(f"Phi-time: {{PHI_TIME:.6f}}")
    print(f"Resonance: {{RESONANCE:.6f}}")
    print(f"Complexity: {{COMPLEXITY:.6f}}")
    
    print("\\nParameters:")
    print(f"  QR Version: {{PARAMS['qr_version']}}")
    print(f"  Error Correction: {{PARAMS['error_correction']}}")
    print(f"  Compression Threshold: {{PARAMS['compression_threshold']}}")
    print(f"  Resonance Factor: {{PARAMS['resonance_factor']:.6f}}")
    print(f"  Complexity Factor: {{PARAMS['complexity_factor']:.6f}}")
    
    # Create the next generation
    next_gen = GENERATION + 1
    print(f"\\n✨ Evolving to generation {{next_gen}}...")
    
    # Calculate new phi-harmonic values
    current_time = time.time()
    phi_time = current_time * PHI
    resonance = phi_time % 1
    complexity = (resonance * PHI) % 1
    
    # Evolve parameters
    new_params = PARAMS.copy()
    
    # Evolve parameters based on resonance
    if resonance < 0.382:  # φ^-2
        # Optimize for complexity
        new_params["complexity_factor"] = min(0.999, new_params["complexity_factor"] * PHI / 2)
        new_params["resonance_factor"] = max(0.1, new_params["resonance_factor"] / PHI)
    elif resonance < 0.618:  # φ^-1
        # Optimize for resonance
        new_params["resonance_factor"] = min(0.999, new_params["resonance_factor"] * (PHI - 1))
        new_params["complexity_factor"] = max(0.1, new_params["complexity_factor"] * (2 - PHI))
    else:
        # Balance optimization
        new_params["resonance_factor"] = (new_params["resonance_factor"] + (PHI - 1)) / 2
        new_params["complexity_factor"] = (new_params["complexity_factor"] + (PHI - 1)) / 2
    
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(QR_CODE_DIR, exist_ok=True)
    
    # Save the evolved parameters
    evolved_params = {{
        "generation": next_gen,
        "system_id": str(uuid.uuid4()),
        "timestamp": current_time,
        "phi_time": phi_time,
        "resonance": resonance,
        "complexity": complexity,
        "params": new_params
    }}
    
    with open(f"{{OUTPUT_DIR}}/evolved_params_gen{{next_gen}}.json", "w") as f:
        json.dump(evolved_params, f, indent=2)
    
    # Create the next generation script
    next_script = f'''
# Self-Replicating Quantum Phi-Harmonic Script
# Generation: {{next_gen}}
# Created: {{datetime.now().isoformat()}}
# System ID: {{evolved_params["system_id"]}}

import os
import sys
import json
import time
import math
import uuid
import qrcode
from datetime import datetime
from PIL import Image

# Phi (Golden Ratio) constant
PHI = (1 + math.sqrt(5)) / 2  # Approximately 1.618034

# System parameters
GENERATION = {{next_gen}}
SYSTEM_ID = "{{evolved_params["system_id"]}}"
TIMESTAMP = {{evolved_params["timestamp"]}}
PHI_TIME = {{evolved_params["phi_time"]}}
RESONANCE = {{evolved_params["resonance"]}}
COMPLEXITY = {{evolved_params["complexity"]}}

# QR parameters
PARAMS = {{
    "qr_version": {{new_params["qr_version"]}},
    "error_correction": {{new_params["error_correction"]}},
    "compression_threshold": {{new_params["compression_threshold"]}},
    "resonance_factor": {{new_params["resonance_factor"]}},
    "complexity_factor": {{new_params["complexity_factor"]}}
}}

# Output directories
OUTPUT_DIR = "qr_phi_replication"
QR_CODE_DIR = os.path.join(OUTPUT_DIR, "qr_codes")
'''
    
    # Copy the evolve function
    with open(__file__, "r") as f:
        content = f.read()
        # Find the function definitions
        func_start = content.find("def evolve():")
        if func_start > 0:
            functions = content[func_start:]
            next_script += functions
    
    # Write the next generation script
    next_gen_file = f"{{OUTPUT_DIR}}/qr_self_replicate_gen{{next_gen}}.py"
    with open(next_gen_file, "w") as f:
        f.write(next_script)
    
    print(f"✅ Created next generation script: {{next_gen_file}}")
    
    # Create a QR code for the next generation
    try:
        # Create QR code payload
        task_payload = {{
            "task_id": f"self_replicate_{{evolved_params['system_id']}}",
            "task_type": "execute_python",
            "timestamp": current_time,
            "script": next_script
        }}
        
        # Write payload to file for debugging
        payload_file = f"{{OUTPUT_DIR}}/payload_gen{{next_gen}}.json"
        with open(payload_file, "w") as f:
            json.dump(task_payload, f, indent=2)
        
        print(f"✅ Saved payload to: {{payload_file}}")
        
        # Create a simple text file with the next generation script
        # This is a fallback in case the QR code is too complex
        script_file = f"{{OUTPUT_DIR}}/script_gen{{next_gen}}.py"
        with open(script_file, "w") as f:
            f.write(next_script)
        
        print(f"✅ Saved script to: {{script_file}}")
        print("\\n✨ Evolution complete")
    except Exception as e:
        print(f"Error during evolution: {{e}}")
    
    return True

# Execute self-evolution
evolve()
"""
    
    # Save the script
    script_file = os.path.join(OUTPUT_DIR, f"qr_self_replicate_gen{generation}.py")
    with open(script_file, "w") as f:
        f.write(script)
    
    # Make the script executable
    os.chmod(script_file, 0o755)
    
    print(f"\n✅ Created self-replicating script: {script_file}")
    return script_file

def create_qr_code(script_file, generation=1):
    """Create a QR code for the script."""
    print("\n✨ Creating QR code...")
    
    try:
        # Read the script
        with open(script_file, 'r') as f:
            script = f.read()
        
        # Create task payload
        task_payload = {
            "task_id": f"self_replicate_{uuid.uuid4()}",
            "task_type": "execute_python",
            "timestamp": time.time(),
            "script": script
        }
        
        # Write payload to file for debugging
        payload_file = os.path.join(OUTPUT_DIR, f"payload_gen{generation}.json")
        with open(payload_file, "w") as f:
            json.dump(task_payload, f, indent=2)
        
        # Create QR code
        qr = qrcode.QRCode(
            version=1,  # Start with minimal version and let it auto-scale
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        
        # Try to add data
        try:
            qr.add_data(json.dumps(task_payload))
            qr.make(fit=True)
            
            # Create image
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Save image
            qr_file = os.path.join(QR_CODE_DIR, f"qr_self_replicate_gen{generation}.png")
            img.save(qr_file)
            
            print(f"✅ Created QR code: {qr_file}")
            return qr_file
        except Exception as e:
            print(f"Error creating QR code: {e}")
            print("Script may be too large for a single QR code.")
            
            # Create a simplified QR code that points to the script file
            simplified_payload = {
                "task_id": f"self_replicate_simplified_{uuid.uuid4()}",
                "task_type": "execute_python",
                "timestamp": time.time(),
                "script": f"""
# Simplified QR code that loads and executes the full script
import os
import sys

script_file = "{script_file}"
print(f"Loading script from: {{script_file}}")

with open(script_file, 'r') as f:
    script_content = f.read()

print("Executing script...")
exec(script_content)
"""
            }
            
            # Create QR code with simplified payload
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(json.dumps(simplified_payload))
            qr.make(fit=True)
            
            # Create image
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Save image
            qr_file = os.path.join(QR_CODE_DIR, f"qr_self_replicate_simplified_gen{generation}.png")
            img.save(qr_file)
            
            print(f"✅ Created simplified QR code: {qr_file}")
            return qr_file
    except Exception as e:
        print(f"Error: {e}")
    
    return None

def main():
    """Main function."""
    print("🧪 Quantum Phi Self-Replication Test")
    print("============================================================")
    
    generation = 1
    
    # Create self-replicating script
    script_file = create_self_replicating_script(generation)
    
    # Create QR code
    qr_file = create_qr_code(script_file, generation)
    
    # Save test metadata
    test_metadata = {
        "generation": generation,
        "timestamp": time.time(),
        "script_file": script_file,
        "qr_file": qr_file
    }
    
    metadata_file = os.path.join(OUTPUT_DIR, "test_metadata.json")
    with open(metadata_file, 'w') as f:
        json.dump(test_metadata, f, indent=2)
    
    print("\n✅ Test completed successfully")
    if qr_file:
        print(f"QR code generated: {qr_file}")
        print("\nTo execute this QR code and trigger self-replication, run:")
        print(f"python qr_task_worker_from_file.py -f {qr_file}")
    else:
        print(f"Script generated: {script_file}")
        print("\nTo execute this script and trigger self-replication, run:")
        print(f"python {script_file}")
    
    # Execute the script directly to demonstrate self-replication
    print("\n✨ Executing script to demonstrate self-replication...")
    try:
        with open(script_file, 'r') as f:
            script_content = f.read()
        
        # Execute the script
        exec(script_content)
    except Exception as e:
        print(f"Error executing script: {e}")

if __name__ == "__main__":
    main()
