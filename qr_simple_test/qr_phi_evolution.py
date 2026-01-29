#!/usr/bin/env python3
"""
QR Phi-Harmonic Evolution System
Creates a self-improving QR code that evolves using phi-harmonic principles
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

class QRPhiEvolution:
    """QR code that evolves using phi-harmonic principles"""
    
    def __init__(self):
        """Initialize the evolution system"""
        self.phi = PHI
        self.generation = 1
        self.system_id = str(uuid.uuid4())
        self.timestamp = time.time()
        self.phi_time = self.timestamp * self.phi
        self.resonance = (self.phi_time % 1)
        self.complexity = (self.resonance * self.phi) % 1
        
        # Default parameters
        self.params = {
            "qr_version": 10,
            "error_correction": 0,
            "compression_threshold": int(500 * self.phi),
            "resonance_factor": 1/self.phi,  # Golden ratio inverse
            "complexity_factor": 1/(self.phi*self.phi)  # Golden ratio inverse squared
        }
        
        # Create output directory
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
    
    def load_optimized_parameters(self):
        """Load optimized parameters from system state if available"""
        try:
            # Find the most recent system state file
            state_files = [f for f in os.listdir(STATE_DIR) 
                          if f.startswith("qr_system_state_") and f.endswith(".json")]
            
            if not state_files:
                print("No system state files found. Using default parameters.")
                return
            
            # Sort by timestamp (newest first)
            state_files.sort(reverse=True)
            latest_state_file = os.path.join(STATE_DIR, state_files[0])
            
            print(f"Loading system state from: {latest_state_file}")
            with open(latest_state_file, 'r') as f:
                state = json.load(f)
            
            # Extract the optimized parameters
            generator_params = state.get("generator_state", {}).get("parameters", {})
            
            # Update parameters if available
            if generator_params.get("qr_version") is not None:
                self.params["qr_version"] = generator_params["qr_version"]
            
            if generator_params.get("error_correction") is not None:
                self.params["error_correction"] = generator_params["error_correction"]
            
            if generator_params.get("compression_threshold") is not None:
                self.params["compression_threshold"] = generator_params["compression_threshold"]
            
            if generator_params.get("resonance_factor") is not None:
                self.params["resonance_factor"] = generator_params["resonance_factor"]
            
            if generator_params.get("complexity_factor") is not None:
                self.params["complexity_factor"] = generator_params["complexity_factor"]
            
            # Update generation
            self.generation = state.get("generation", 0) + 1
            
            print("✅ Loaded optimized parameters")
        except Exception as e:
            print(f"Error loading system state: {e}")
            print("Using default parameters")
    
    def evolve_parameters(self):
        """Evolve parameters based on phi-harmonic principles"""
        # Calculate new phi-time
        current_time = time.time()
        phi_time = current_time * self.phi
        resonance = (phi_time % 1)
        complexity = (resonance * self.phi) % 1
        
        # Update system properties
        self.timestamp = current_time
        self.phi_time = phi_time
        self.resonance = resonance
        self.complexity = complexity
        
        # Evolve parameters based on resonance
        if resonance < 0.382:  # φ^-2
            # Optimize for complexity
            self.params["complexity_factor"] = min(0.999, self.params["complexity_factor"] * self.phi / 2)
            self.params["resonance_factor"] = max(0.1, self.params["resonance_factor"] / self.phi)
        elif resonance < 0.618:  # φ^-1
            # Optimize for resonance
            self.params["resonance_factor"] = min(0.999, self.params["resonance_factor"] * (self.phi - 1))
            self.params["complexity_factor"] = max(0.1, self.params["complexity_factor"] * (2 - self.phi))
        else:
            # Balance optimization
            self.params["resonance_factor"] = (self.params["resonance_factor"] + (self.phi - 1)) / 2
            self.params["complexity_factor"] = (self.params["complexity_factor"] + (self.phi - 1)) / 2
        
        # Adjust QR parameters based on complexity
        if complexity < 0.382:
            self.params["qr_version"] = max(1, min(40, self.params["qr_version"] - 1))
        elif complexity > 0.618:
            self.params["qr_version"] = max(1, min(40, self.params["qr_version"] + 1))
        
        # Update compression threshold
        self.params["compression_threshold"] = int(self.params["compression_threshold"] * 
                                                 (1 + (resonance - 0.5) / 5))
        
        print("✅ Evolved parameters")
    
    def create_evolution_script(self):
        """Create a script that represents the next evolution"""
        script_content = f"""#!/usr/bin/env python3
'''
QR Phi-Harmonic Evolution - Generation {self.generation}
Created: {datetime.now().isoformat()}
System ID: {self.system_id}
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

# System parameters
SYSTEM_PARAMS = {{
    "generation": {self.generation},
    "system_id": "{self.system_id}",
    "timestamp": {self.timestamp},
    "phi_time": {self.phi_time},
    "resonance": {self.resonance},
    "complexity": {self.complexity},
    "params": {json.dumps(self.params)}
}}

def evolve():
    # Evolve to the next generation
    print("🧠 QR Phi-Harmonic Evolution System")
    print("============================================================")
    print(f"Generation: {{SYSTEM_PARAMS['generation']}}")
    print(f"System ID: {{SYSTEM_PARAMS['system_id']}}")
    print(f"Timestamp: {{datetime.fromtimestamp(SYSTEM_PARAMS['timestamp']).isoformat()}}")
    print(f"Phi-time: {{SYSTEM_PARAMS['phi_time']:.6f}}")
    print(f"Resonance: {{SYSTEM_PARAMS['resonance']:.6f}}")
    print(f"Complexity: {{SYSTEM_PARAMS['complexity']:.6f}}")
    
    print("\\nParameters:")
    params = SYSTEM_PARAMS["params"]
    print(f"  QR Version: {{params['qr_version']}}")
    print(f"  Error Correction: {{params['error_correction']}}")
    print(f"  Compression Threshold: {{params['compression_threshold']}}")
    print(f"  Resonance Factor: {{params['resonance_factor']:.6f}}")
    print(f"  Complexity Factor: {{params['complexity_factor']:.6f}}")
    
    # Create the next generation
    next_gen = SYSTEM_PARAMS["generation"] + 1
    print(f"\\n✨ Evolving to generation {{next_gen}}...")
    
    # Calculate new phi-time
    current_time = time.time()
    phi_time = current_time * PHI
    resonance = (phi_time % 1)
    complexity = (resonance * PHI) % 1
    
    # Evolve parameters
    new_params = params.copy()
    
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
    
    # Create new system parameters
    new_system = {{
        "generation": next_gen,
        "system_id": str(uuid.uuid4()),
        "timestamp": current_time,
        "phi_time": phi_time,
        "resonance": resonance,
        "complexity": complexity,
        "params": new_params
    }}
    
    # Create output directory
    output_dir = "qr_evolution"
    os.makedirs(output_dir, exist_ok=True)
    
    # Save the evolved parameters
    with open(f"{{output_dir}}/evolved_params_gen{{next_gen}}.json", "w") as f:
        json.dump(new_system, f, indent=2)
    
    # Create the next generation script
    next_gen_file = f"{{output_dir}}/qr_phi_evolution_gen{{next_gen}}.py"
    
    # Create the next generation script content
    with open(__file__, "r") as f:
        script_content = f.read()
    
    # Replace the system parameters
    start_marker = "# System parameters"
    end_marker = "}}\\n"
    start_idx = script_content.find(start_marker)
    if start_idx > 0:
        # Find the end of the SYSTEM_PARAMS block
        params_start = script_content.find("SYSTEM_PARAMS = {{", start_idx)
        if params_start > 0:
            # Find the end of the JSON block
            params_end = script_content.find(end_marker, params_start)
            if params_end > 0:
                params_end += len(end_marker)
                
                # Create the new parameters block
                new_params_block = f"SYSTEM_PARAMS = {{\\n"
                new_params_block += f'    "generation": {{new_system["generation"]}},\\n'
                new_params_block += f'    "system_id": "{{new_system["system_id"]}}",\\n'
                new_params_block += f'    "timestamp": {{new_system["timestamp"]}},\\n'
                new_params_block += f'    "phi_time": {{new_system["phi_time"]}},\\n'
                new_params_block += f'    "resonance": {{new_system["resonance"]}},\\n'
                new_params_block += f'    "complexity": {{new_system["complexity"]}},\\n'
                new_params_block += f'    "params": {json.dumps(new_system["params"])}\\n'
                new_params_block += f"}}\\n"
                
                # Replace the parameters block
                new_script_content = script_content[:params_start] + new_params_block + script_content[params_end:]
                
                # Write the new script
                with open(next_gen_file, "w") as f:
                    f.write(new_script_content)
                
                print(f"✅ Created next generation script: {{next_gen_file}}")
                
                # Create a QR code for the next generation
                try:
                    # Use the existing simple_qr_encoder.py to encode the file
                    subprocess.run([
                        "python", "simple_qr_encoder.py",
                        "--file", next_gen_file,
                        "--title", f"QR-Phi-Evolution-Gen{{next_gen}}"
                    ])
                    
                    print("✅ Created QR code for next generation")
                except Exception as e:
                    print(f"Error creating QR code: {{e}}")
    
    print("\\n✨ Evolution complete")
    return True

if __name__ == "__main__":
    success = evolve()
    sys.exit(0 if success else 1)
"""
        
        # Save the script
        script_file = os.path.join(OUTPUT_DIR, f"qr_phi_evolution_gen{self.generation}.py")
        with open(script_file, "w") as f:
            f.write(script_content)
        
        # Make the script executable
        os.chmod(script_file, 0o755)
        
        print(f"✅ Created evolution script: {script_file}")
        return script_file
    
    def create_qr_code(self, script_file):
        """Create a QR code for the evolution script"""
        print("\n✨ Creating QR code...")
        try:
            # Use the existing simple_qr_encoder.py to encode the file
            result = subprocess.run([
                "python", "simple_qr_encoder.py",
                "--file", script_file,
                "--title", f"QR-Phi-Evolution-Gen{self.generation}"
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
                # Try using qr_presentation_chunker.py if the file is too large
                print("\n✨ Trying chunked QR code generation...")
                result = subprocess.run([
                    "python", "qr_presentation_chunker.py",
                    "--file", script_file,
                    "--title", f"QR-Phi-Evolution-Gen{self.generation}"
                ], capture_output=True, text=True)
                
                if result.returncode == 0:
                    print(result.stdout)
                    return f"qr_codes/chunked/QR-Phi-Evolution-Gen{self.generation}/"
                else:
                    print(f"Error creating chunked QR code: {result.stderr}")
        except Exception as e:
            print(f"Error: {e}")
        
        return None
    
    def run(self):
        """Run the evolution system"""
        print("🌟 QR Phi-Harmonic Evolution System")
        print("============================================================")
        
        # Load optimized parameters
        self.load_optimized_parameters()
        
        # Display current parameters
        print("\n🧠 Current System Parameters")
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
        
        # Evolve parameters
        print("\n✨ Evolving parameters...")
        self.evolve_parameters()
        
        # Create evolution script
        script_file = self.create_evolution_script()
        
        # Create QR code
        qr_path = self.create_qr_code(script_file)
        
        if qr_path:
            print(f"\n✅ System encoded to QR code: {qr_path}")
            print("\nTo execute this QR code and trigger evolution, run:")
            print(f"python qr_task_worker_from_file.py -f {qr_path}")
        else:
            print("\n❌ Failed to encode system to QR code")
        
        print("\n✨ Process complete")

if __name__ == "__main__":
    evolution = QRPhiEvolution()
    evolution.run()
