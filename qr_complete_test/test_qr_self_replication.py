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
import base64
from datetime import datetime
from PIL import Image

# Import existing system components
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from qr_genome_engine import QRGenomeEngine
from qr_epigenetic_memory import QREpigeneticMemory

# Phi (Golden Ratio) constant
PHI = (1 + math.sqrt(5)) / 2  # Approximately 1.618034

# Output directories
OUTPUT_DIR = "qr_self_replication_test"
QR_CODE_DIR = os.path.join(OUTPUT_DIR, "qr_codes")

class QRSelfReplicationTest:
    """
    Tests the Quantum Phi-Harmonic QR System's ability to store and improve itself
    through QR codes, demonstrating recursive self-improvement and self-replication.
    """
    
    def __init__(self, debug=True):
        """Initialize the test environment."""
        self.debug = debug
        self.genome_engine = QRGenomeEngine(debug=debug)
        self.memory = QREpigeneticMemory()
        
        # Create output directories
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        os.makedirs(QR_CODE_DIR, exist_ok=True)
        
        # Initialize test parameters
        self.test_id = str(uuid.uuid4())
        self.generation = 1
        self.timestamp = time.time()
        self.phi_time = self.timestamp * PHI
        self.resonance = self.phi_time % 1
        self.complexity = (self.resonance * PHI) % 1
        
        # Load system state
        self.system_state = self.load_system_state()
        
        if self.debug:
            print(f"🧪 QR Self-Replication Test initialized")
            print(f"Test ID: {self.test_id}")
            print(f"Timestamp: {datetime.fromtimestamp(self.timestamp).isoformat()}")
            print(f"Phi-time: {self.phi_time}")
            print(f"Resonance: {self.resonance}")
            print(f"Complexity: {self.complexity}")
    
    def load_system_state(self):
        """Load the most recent system state."""
        state_dir = "qr_recursive_system/qr_state"
        if not os.path.exists(state_dir):
            if self.debug:
                print(f"System state directory not found: {state_dir}")
            return None
        
        state_files = [f for f in os.listdir(state_dir) 
                      if f.startswith("qr_system_state_") and f.endswith(".json")]
        
        if not state_files:
            if self.debug:
                print("No system state files found.")
            return None
        
        # Sort by timestamp (newest first)
        state_files.sort(reverse=True)
        latest_state_file = os.path.join(state_dir, state_files[0])
        
        if self.debug:
            print(f"Loading system state from: {latest_state_file}")
        
        try:
            with open(latest_state_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            if self.debug:
                print(f"Error loading system state: {e}")
            return None
    
    def create_self_replicating_qr_code(self):
        """Create a QR code that contains a self-replicating script."""
        if self.debug:
            print("\n✨ Creating self-replicating QR code...")
        
        # Extract parameters from system state
        params = {
            "qr_version": 10,
            "error_correction": 0,
            "compression_threshold": int(500 * PHI),
            "resonance_factor": 1/PHI,
            "complexity_factor": 1/(PHI*PHI)
        }
        
        # Update from system state if available
        if self.system_state and "generator_state" in self.system_state:
            gen_params = self.system_state.get("generator_state", {}).get("parameters", {})
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
        
        # Create the self-replicating script
        script = f"""
# Self-Replicating Quantum Phi-Harmonic Script - Generation {self.generation}
# Created: {datetime.now().isoformat()}
# System ID: {self.test_id}

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
GENERATION = {self.generation}
SYSTEM_ID = "{self.test_id}"
TIMESTAMP = {self.timestamp}
PHI_TIME = {self.phi_time}
RESONANCE = {self.resonance}
COMPLEXITY = {self.complexity}

# QR parameters
PARAMS = {{
    "qr_version": {params['qr_version']},
    "error_correction": {params['error_correction']},
    "compression_threshold": {params['compression_threshold']},
    "resonance_factor": {params['resonance_factor']},
    "complexity_factor": {params['complexity_factor']}
}}

def replicate():
    \"\"\"Self-replicate to the next generation.\"\"\"
    print("🧬 Quantum Phi-Harmonic Self-Replication")
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
    output_dir = "qr_self_replication_test"
    qr_dir = os.path.join(output_dir, "qr_codes")
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(qr_dir, exist_ok=True)
    
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
    
    with open(f"{{output_dir}}/evolved_params_gen{{next_gen}}.json", "w") as f:
        json.dump(evolved_params, f, indent=2)
    
    # Create the next generation script
    next_script = f'''
# Self-Replicating Quantum Phi-Harmonic Script - Generation {{next_gen}}
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

'''
    
    # Copy the replicate function
    with open(__file__, "r") as f:
        content = f.read()
        # Find the function definitions
        func_start = content.find("def replicate():")
        if func_start > 0:
            functions = content[func_start:]
            next_script += functions
    
    # Write the next generation script
    next_gen_file = f"{{output_dir}}/qr_self_replicate_gen{{next_gen}}.py"
    with open(next_gen_file, "w") as f:
        f.write(next_script)
    
    print(f"✅ Created next generation script: {{next_gen_file}}")
    
    # Create a QR code for the next generation
    try:
        # Create QR code
        qr = qrcode.QRCode(
            version=min(40, max(1, new_params["qr_version"])),
            error_correction=qrcode.constants.ERROR_CORRECT_H if new_params["error_correction"] > 3 else new_params["error_correction"],
            box_size=10,
            border=4,
        )
        
        # Create task payload
        task_payload = {{
            "task_id": f"self_replicate_{{evolved_params['system_id']}}",
            "task_type": "execute_python",
            "timestamp": current_time,
            "script": next_script
        }}
        
        # Add data to QR code
        qr.add_data(json.dumps(task_payload))
        qr.make(fit=True)
        
        # Create image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save image
        qr_file = f"{{qr_dir}}/qr_self_replicate_gen{{next_gen}}.png"
        img.save(qr_file)
        
        print(f"✅ Created QR code for next generation: {{qr_file}}")
        print("\\nTo execute this QR code and trigger the next generation, run:")
        print(f"python qr_task_worker_from_file.py -f {{qr_file}}")
    except Exception as e:
        print(f"Error creating QR code: {{e}}")
    
    print("\\n✨ Self-replication complete")
    return True

# Execute self-replication
replicate()
"""
        
        # Create task payload
        task_payload = {
            "task_id": f"self_replicate_{self.test_id}",
            "task_type": "execute_python",
            "timestamp": self.timestamp,
            "script": script
        }
        
        # Create QR code
        qr = qrcode.QRCode(
            version=min(40, max(1, params["qr_version"])),
            error_correction=qrcode.constants.ERROR_CORRECT_H if params["error_correction"] > 3 else params["error_correction"],
            box_size=10,
            border=4,
        )
        qr.add_data(json.dumps(task_payload))
        qr.make(fit=True)
        
        # Create image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save image
        qr_file = os.path.join(QR_CODE_DIR, f"qr_self_replicate_gen{self.generation}.png")
        img.save(qr_file)
        
        if self.debug:
            print(f"✅ Created self-replicating QR code: {qr_file}")
        
        return qr_file
    
    def run_test(self):
        """Run the self-replication test."""
        print("🧪 Running Quantum Phi Self-Replication Test")
        print("============================================================")
        
        # Create self-replicating QR code
        qr_file = self.create_self_replicating_qr_code()
        
        # Save test metadata
        test_metadata = {
            "test_id": self.test_id,
            "generation": self.generation,
            "timestamp": self.timestamp,
            "phi_time": self.phi_time,
            "resonance": self.resonance,
            "complexity": self.complexity,
            "qr_file": qr_file
        }
        
        metadata_file = os.path.join(OUTPUT_DIR, "test_metadata.json")
        with open(metadata_file, 'w') as f:
            json.dump(test_metadata, f, indent=2)
        
        print("\n✅ Test completed successfully")
        print(f"QR code generated: {qr_file}")
        print("\nTo execute this QR code and trigger self-replication, run:")
        print(f"python qr_task_worker_from_file.py -f {qr_file}")
        
        return qr_file

def main():
    """Main function."""
    test = QRSelfReplicationTest(debug=True)
    test.run_test()

if __name__ == "__main__":
    main()
