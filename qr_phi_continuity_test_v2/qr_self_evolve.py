#!/usr/bin/env python3
"""
QR Self-Evolution System
Creates a QR code that contains a self-evolving script based on phi-harmonic principles
"""

import os
import sys
import json
import time
import math
import uuid
import subprocess
from datetime import datetime

# Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio
OUTPUT_DIR = "qr_evolution"
STATE_DIR = "qr_recursive_system/qr_state"

def load_system_state():
    """Load the most recent system state"""
    # Find the most recent system state file
    state_files = [f for f in os.listdir(STATE_DIR) 
                  if f.startswith("qr_system_state_") and f.endswith(".json")]
    
    if not state_files:
        print("No system state files found. Using default parameters.")
        return None
    
    # Sort by timestamp (newest first)
    state_files.sort(reverse=True)
    latest_state_file = os.path.join(STATE_DIR, state_files[0])
    
    print(f"Loading system state from: {latest_state_file}")
    with open(latest_state_file, 'r') as f:
        return json.load(f)

def create_self_evolving_script():
    """Create a script that can evolve itself"""
    # Create output directory
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    # Load system state
    system_state = load_system_state()
    
    # Extract parameters or use defaults
    generation = 1
    if system_state:
        generation = system_state.get("generation", 0) + 1
    
    # Generate system ID
    system_id = str(uuid.uuid4())
    
    # Calculate phi-harmonic values
    timestamp = time.time()
    phi_time = timestamp * PHI
    resonance = phi_time % 1
    complexity = (resonance * PHI) % 1
    
    # Set parameters
    params = {
        "qr_version": 10,
        "error_correction": 0,
        "compression_threshold": int(500 * PHI),
        "resonance_factor": 1/PHI,  # Golden ratio inverse
        "complexity_factor": 1/(PHI*PHI)  # Golden ratio inverse squared
    }
    
    # Update from system state if available
    if system_state and "generator_state" in system_state:
        gen_params = system_state.get("generator_state", {}).get("parameters", {})
        if gen_params:
            if "qr_version" in gen_params:
                params["qr_version"] = gen_params["qr_version"]
            if "error_correction" in gen_params:
                params["error_correction"] = gen_params["error_correction"]
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
    print(f"System ID: {system_id}")
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
    
    # Evolve parameters based on resonance
    if resonance < 0.382:  # φ^-2
        # Optimize for complexity
        params["complexity_factor"] = min(0.999, params["complexity_factor"] * PHI / 2)
        params["resonance_factor"] = max(0.1, params["resonance_factor"] / PHI)
    elif resonance < 0.618:  # φ^-1
        # Optimize for resonance
        params["resonance_factor"] = min(0.999, params["resonance_factor"] * (PHI - 1))
        params["complexity_factor"] = max(0.1, params["complexity_factor"] * (2 - PHI))
    else:
        # Balance optimization
        params["resonance_factor"] = (params["resonance_factor"] + (PHI - 1)) / 2
        params["complexity_factor"] = (params["complexity_factor"] + (PHI - 1)) / 2
    
    # Adjust QR parameters based on complexity
    if complexity < 0.382:
        params["qr_version"] = max(1, min(40, params["qr_version"] - 1))
    elif complexity > 0.618:
        params["qr_version"] = max(1, min(40, params["qr_version"] + 1))
    
    # Update compression threshold
    params["compression_threshold"] = int(params["compression_threshold"] * 
                                       (1 + (resonance - 0.5) / 5))
    
    # Create the self-evolving script
    script_content = f"""#!/usr/bin/env python3
'''
QR Self-Evolution System - Generation {generation}
Created: {datetime.now().isoformat()}
System ID: {system_id}
'''

import os
import sys
import json
import time
import math
import uuid
import subprocess
from datetime import datetime

# Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio
OUTPUT_DIR = "qr_evolution"

# System parameters
GENERATION = {generation}
SYSTEM_ID = "{system_id}"
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

def evolve():
    # Self-evolving function
    print("🧠 QR Self-Evolution System")
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
    
    # Adjust QR parameters based on complexity
    if complexity < 0.382:
        new_params["qr_version"] = max(1, min(40, new_params["qr_version"] - 1))
    elif complexity > 0.618:
        new_params["qr_version"] = max(1, min(40, new_params["qr_version"] + 1))
    
    # Update compression threshold
    new_params["compression_threshold"] = int(new_params["compression_threshold"] * 
                                           (1 + (resonance - 0.5) / 5))
    
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
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
    next_script = f'''#!/usr/bin/env python3
'''
QR Self-Evolution System - Generation {{next_gen}}
Created: {{datetime.now().isoformat()}}
System ID: {{evolved_params["system_id"]}}
'''

import os
import sys
import json
import time
import math
import uuid
import subprocess
from datetime import datetime

# Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio
OUTPUT_DIR = "qr_evolution"

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

'''
    
    # Copy the rest of this file (functions)
    with open(__file__, "r") as f:
        content = f.read()
        # Find the function definitions
        func_start = content.find("def evolve():")
        if func_start > 0:
            functions = content[func_start:]
            next_script += functions
    
    # Write the next generation script
    next_gen_file = f"{{OUTPUT_DIR}}/qr_self_evolve_gen{{next_gen}}.py"
    with open(next_gen_file, "w") as f:
        f.write(next_script)
    
    print(f"✅ Created next generation script: {{next_gen_file}}")
    
    # Create a QR code for the next generation
    try:
        # Use the existing simple_qr_encoder.py to encode the file
        subprocess.run([
            "python", "simple_qr_encoder.py",
            "--file", next_gen_file,
            "--title", f"QR-Self-Evolution-Gen{{next_gen}}"
        ])
        
        print("✅ Created QR code for next generation")
        print("\\nTo execute the next generation, scan the QR code with qr_task_worker_from_file.py")
    except Exception as e:
        print(f"Error creating QR code: {{e}}")
    
    print("\\n✨ Evolution complete")
    return True

if __name__ == "__main__":
    success = evolve()
    sys.exit(0 if success else 1)
"""
    
    # Save the script
    script_file = os.path.join(OUTPUT_DIR, f"qr_self_evolve_gen{generation}.py")
    with open(script_file, "w") as f:
        f.write(script_content)
    
    # Make the script executable
    os.chmod(script_file, 0o755)
    
    print(f"✅ Created self-evolving script: {script_file}")
    return script_file

def create_qr_code(script_file):
    """Create a QR code for the self-evolving script"""
    print("\n✨ Creating QR code...")
    try:
        # Use the existing simple_qr_encoder.py to encode the file
        result = subprocess.run([
            "python", "simple_qr_encoder.py",
            "--file", script_file,
            "--title", f"QR-Self-Evolution"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(result.stdout)
            # Extract QR code path from output
            for line in result.stdout.split('\n'):
                if line.startswith("Created QR code:"):
                    qr_path = line.split(":", 1)[1].strip()
                    return qr_path
        else:
            print(f"Error creating QR code: {result.stderr}")
    except Exception as e:
        print(f"Error: {e}")
    
    return None

def main():
    """Main function"""
    print("🌟 QR Self-Evolution System")
    print("============================================================")
    
    # Create self-evolving script
    script_file = create_self_evolving_script()
    
    # Create QR code
    qr_path = create_qr_code(script_file)
    
    if qr_path:
        print(f"\n✅ System encoded to QR code: {qr_path}")
        print("\nTo execute this QR code and trigger evolution, run:")
        print(f"python qr_task_worker_from_file.py -f {qr_path}")
    else:
        print("\n❌ Failed to encode system to QR code")
    
    print("\n✨ Process complete")

if __name__ == "__main__":
    main()
