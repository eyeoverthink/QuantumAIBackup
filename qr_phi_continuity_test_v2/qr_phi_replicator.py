#!/usr/bin/env python3
"""
Quantum Phi-Harmonic Self-Replicator
By Vaughn Scott

A self-replicating system that leverages quantum phi-harmonic principles
to evolve and improve itself through QR codes.

This script:
1. Generates a self-contained script with phi-harmonic evolution logic
2. Creates QR codes that can be executed by the QR task worker
3. Implements fallback mechanisms for large scripts
4. Ensures proper encapsulation of all variables and functions
"""

import os
import sys
import json
import time
import math
import uuid
import qrcode
import base64
import zlib
from datetime import datetime
from PIL import Image

# Phi (Golden Ratio) constant
PHI = (1 + math.sqrt(5)) / 2  # Approximately 1.618034

# Output directories
OUTPUT_DIR = "qr_phi_replication"
QR_CODE_DIR = os.path.join(OUTPUT_DIR, "qr_codes")


class QuantumPhiReplicator:
    """
    A self-replicating system that leverages quantum phi-harmonic principles
    to evolve and improve itself through QR codes.
    """
    
    def __init__(self, generation=1, debug=True):
        """Initialize the replicator."""
        self.debug = debug
        self.generation = generation
        self.system_id = str(uuid.uuid4())
        self.timestamp = time.time()
        self.phi_time = self.timestamp * PHI
        self.resonance = self.phi_time % 1
        self.complexity = (self.resonance * PHI) % 1
        
        # Create output directories
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        os.makedirs(QR_CODE_DIR, exist_ok=True)
        
        # Initialize parameters with phi-harmonic defaults
        self.params = {
            "qr_version": 1,  # Start with minimal version
            "error_correction": qrcode.constants.ERROR_CORRECT_H,
            "compression_threshold": int(500 * PHI),
            "resonance_factor": 1/PHI,
            "complexity_factor": 1/(PHI*PHI)
        }
        
        # Load system state
        self.system_state = self.load_system_state()
        self.update_params_from_state()
        
        if self.debug:
            self.print_status()
    
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
    
    def update_params_from_state(self):
        """Update parameters from system state."""
        if self.system_state and "generator_state" in self.system_state:
            gen_params = self.system_state.get("generator_state", {}).get("parameters", {})
            if gen_params:
                if "qr_version" in gen_params:
                    self.params["qr_version"] = min(40, max(1, gen_params["qr_version"]))
                if "error_correction" in gen_params:
                    self.params["error_correction"] = min(3, max(0, gen_params["error_correction"]))
                if "compression_threshold" in gen_params:
                    self.params["compression_threshold"] = gen_params["compression_threshold"]
                if "resonance_factor" in gen_params:
                    self.params["resonance_factor"] = gen_params["resonance_factor"]
                if "complexity_factor" in gen_params:
                    self.params["complexity_factor"] = gen_params["complexity_factor"]
    
    def print_status(self):
        """Print the current status."""
        print("\n🧠 Quantum Phi-Harmonic Self-Replicator")
        print("============================================================")
        print(f"Generation: {self.generation}")
        print(f"System ID: {self.system_id}")
        print(f"Timestamp: {datetime.fromtimestamp(self.timestamp).isoformat()}")
        print(f"Phi-time: {self.phi_time:.6f}")
        print(f"Resonance: {self.resonance:.6f}")
        print(f"Complexity: {self.complexity:.6f}")
        
        print("\nParameters:")
        print(f"  QR Version: {self.params['qr_version']}")
        print(f"  Error Correction: {self.params['error_correction']}")
        print(f"  Compression Threshold: {self.params['compression_threshold']}")
        print(f"  Resonance Factor: {self.params['resonance_factor']:.6f}")
        print(f"  Complexity Factor: {self.params['complexity_factor']:.6f}")
    
    def evolve_parameters(self):
        """Evolve parameters based on phi-harmonic principles."""
        # Calculate new phi-harmonic values
        current_time = time.time()
        phi_time = current_time * PHI
        resonance = phi_time % 1
        complexity = (resonance * PHI) % 1
        
        # Create new parameter set
        new_params = self.params.copy()
        
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
        
        return {
            "generation": self.generation + 1,
            "system_id": str(uuid.uuid4()),
            "timestamp": current_time,
            "phi_time": phi_time,
            "resonance": resonance,
            "complexity": complexity,
            "params": new_params
        }
    
    def create_next_generation_script(self, evolved_data):
        """Create the next generation script."""
        # Get the current script content
        with open(__file__, 'r') as f:
            current_script = f.read()
        
        # Extract the class and function definitions
        class_start = current_script.find("class QuantumPhiReplicator:")
        if class_start < 0:
            raise ValueError("Could not find QuantumPhiReplicator class in script")
        
        class_def = current_script[class_start:]
        
        # Create the next generation script
        next_script = f"""#!/usr/bin/env python3
\"\"\"
Quantum Phi-Harmonic Self-Replicator - Generation {evolved_data['generation']}
By Vaughn Scott

A self-replicating system that leverages quantum phi-harmonic principles
to evolve and improve itself through QR codes.

This script:
1. Generates a self-contained script with phi-harmonic evolution logic
2. Creates QR codes that can be executed by the QR task worker
3. Implements fallback mechanisms for large scripts
4. Ensures proper encapsulation of all variables and functions
\"\"\"

import os
import sys
import json
import time
import math
import uuid
import qrcode
import base64
import zlib
from datetime import datetime
from PIL import Image

# Phi (Golden Ratio) constant
PHI = (1 + math.sqrt(5)) / 2  # Approximately 1.618034

# Output directories
OUTPUT_DIR = "qr_phi_replication"
QR_CODE_DIR = os.path.join(OUTPUT_DIR, "qr_codes")

{class_def}

def main():
    \"\"\"Main function.\"\"\"
    # Create a replicator with the evolved parameters
    replicator = QuantumPhiReplicator(
        generation={evolved_data['generation']},
        debug=True
    )
    
    # Override parameters with evolved values
    replicator.system_id = "{evolved_data['system_id']}"
    replicator.timestamp = {evolved_data['timestamp']}
    replicator.phi_time = {evolved_data['phi_time']}
    replicator.resonance = {evolved_data['resonance']}
    replicator.complexity = {evolved_data['complexity']}
    
    # Update parameters
    replicator.params = {{
        "qr_version": {evolved_data['params']['qr_version']},
        "error_correction": {evolved_data['params']['error_correction']},
        "compression_threshold": {evolved_data['params']['compression_threshold']},
        "resonance_factor": {evolved_data['params']['resonance_factor']},
        "complexity_factor": {evolved_data['params']['complexity_factor']}
    }}
    
    # Print status
    replicator.print_status()
    
    # Replicate
    replicator.replicate()

if __name__ == "__main__":
    main()
"""
        
        # Save the next generation script
        script_file = os.path.join(OUTPUT_DIR, f"qr_phi_replicator_gen{evolved_data['generation']}.py")
        with open(script_file, 'w') as f:
            f.write(next_script)
        
        # Make the script executable
        os.chmod(script_file, 0o755)
        
        if self.debug:
            print(f"\n✅ Created next generation script: {script_file}")
        
        return script_file
    
    def create_qr_code(self, script_file, evolved_data):
        """Create a QR code for the script."""
        if self.debug:
            print("\n✨ Creating QR code...")
        
        try:
            # Read the script
            with open(script_file, 'r') as f:
                script = f.read()
            
            # Create task payload
            task_payload = {
                "task_id": f"phi_replicate_{evolved_data['system_id']}",
                "task_type": "execute_python",
                "timestamp": evolved_data['timestamp'],
                "script": script
            }
            
            # Write payload to file for debugging
            payload_file = os.path.join(OUTPUT_DIR, f"payload_gen{evolved_data['generation']}.json")
            with open(payload_file, 'w') as f:
                json.dump(task_payload, f, indent=2)
            
            # Check if compression is needed
            script_size = len(json.dumps(task_payload))
            if script_size > self.params["compression_threshold"]:
                if self.debug:
                    print(f"Script size ({script_size} bytes) exceeds compression threshold ({self.params['compression_threshold']} bytes)")
                    print("Creating simplified QR code...")
                
                # Create a simplified QR code that points to the script file
                simplified_payload = {
                    "task_id": f"phi_replicate_simplified_{evolved_data['system_id']}",
                    "task_type": "execute_python",
                    "timestamp": evolved_data['timestamp'],
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
                qr_file = os.path.join(QR_CODE_DIR, f"qr_phi_replicator_simplified_gen{evolved_data['generation']}.png")
                img.save(qr_file)
                
                if self.debug:
                    print(f"✅ Created simplified QR code: {qr_file}")
                return qr_file
            else:
                # Create QR code with full payload
                qr = qrcode.QRCode(
                    version=min(40, max(1, self.params["qr_version"])),
                    error_correction=qrcode.constants.ERROR_CORRECT_H if self.params["error_correction"] > 3 else self.params["error_correction"],
                    box_size=10,
                    border=4,
                )
                
                try:
                    qr.add_data(json.dumps(task_payload))
                    qr.make(fit=True)
                    
                    # Create image
                    img = qr.make_image(fill_color="black", back_color="white")
                    
                    # Save image
                    qr_file = os.path.join(QR_CODE_DIR, f"qr_phi_replicator_gen{evolved_data['generation']}.png")
                    img.save(qr_file)
                    
                    if self.debug:
                        print(f"✅ Created QR code: {qr_file}")
                    return qr_file
                except Exception as e:
                    if self.debug:
                        print(f"Error creating QR code: {e}")
                        print("Falling back to simplified QR code...")
                    
                    # Fall back to simplified QR code
                    return self.create_qr_code(script_file, evolved_data)
        except Exception as e:
            if self.debug:
                print(f"Error: {e}")
        
        return None
    
    def replicate(self):
        """Replicate to the next generation."""
        if self.debug:
            print("\n✨ Replicating to next generation...")
        
        # Evolve parameters
        evolved_data = self.evolve_parameters()
        
        # Save the evolved parameters
        params_file = os.path.join(OUTPUT_DIR, f"evolved_params_gen{evolved_data['generation']}.json")
        with open(params_file, 'w') as f:
            json.dump(evolved_data, f, indent=2)
        
        if self.debug:
            print(f"✅ Saved evolved parameters: {params_file}")
        
        # Create the next generation script
        script_file = self.create_next_generation_script(evolved_data)
        
        # Create QR code
        qr_file = self.create_qr_code(script_file, evolved_data)
        
        # Save replication metadata
        replication_metadata = {
            "original_generation": self.generation,
            "next_generation": evolved_data['generation'],
            "timestamp": time.time(),
            "script_file": script_file,
            "qr_file": qr_file
        }
        
        metadata_file = os.path.join(OUTPUT_DIR, f"replication_metadata_gen{self.generation}_to_gen{evolved_data['generation']}.json")
        with open(metadata_file, 'w') as f:
            json.dump(replication_metadata, f, indent=2)
        
        if self.debug:
            print("\n✅ Replication completed successfully")
            if qr_file:
                print(f"QR code generated: {qr_file}")
                print("\nTo execute this QR code and trigger the next generation, run:")
                print(f"python qr_task_worker_from_file.py -f {qr_file}")
            else:
                print(f"Script generated: {script_file}")
                print("\nTo execute this script and trigger the next generation, run:")
                print(f"python {script_file}")
        
        return {
            "success": True,
            "evolved_data": evolved_data,
            "script_file": script_file,
            "qr_file": qr_file
        }


def main():
    """Main function."""
    print("🧪 Quantum Phi-Harmonic Self-Replicator")
    print("============================================================")
    
    # Create a replicator
    replicator = QuantumPhiReplicator(generation=1, debug=True)
    
    # Replicate
    replicator.replicate()


if __name__ == "__main__":
    main()
