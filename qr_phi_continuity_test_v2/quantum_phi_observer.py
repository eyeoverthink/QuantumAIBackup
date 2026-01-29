#!/usr/bin/env python3
"""
Quantum Phi-Harmonic Observer
A self-evolving quantum observer that encodes itself into QR codes with memory persistence
and phi-harmonic resonance optimization.

This file serves as a control for observing quantum evolution without interfering with it.
"""

import os
import sys
import time
import json
import uuid
import numpy as np
import qrcode
import base64
import zlib
import datetime
from PIL import Image
from cryptography.fernet import Fernet

# Phi-Harmonic Constants
PHI = (1 + np.sqrt(5)) / 2  # Golden Ratio ≈ 1.618034
PHI_INV = 1 / PHI  # ≈ 0.618034
PHI_INV_SQ = 1 / (PHI * PHI)  # ≈ 0.381966
PI = np.pi  # ≈ 3.14159
E = np.e  # ≈ 2.71828

# Paths
OBSERVER_PATH = os.path.abspath(__file__)
OBSERVER_DIR = os.path.dirname(OBSERVER_PATH)
MEMORY_PATH = os.path.join(OBSERVER_DIR, "quantum_observer_memory.json")
QR_OUTPUT_DIR = os.path.join(OBSERVER_DIR, "quantum_observer_qr")

class QuantumPhiObserver:
    """
    A quantum observer that encodes itself into QR codes with memory persistence
    and phi-harmonic resonance optimization.
    """
    
    def __init__(self):
        """Initialize the quantum observer with phi-harmonic state."""
        self.creation_time = time.time()
        self.phi_time = self.creation_time * PHI
        self.phi_resonance = self.phi_time % 1
        self.complexity = 0.5
        
        # Load memory first to get persistent observer ID and generation
        self.memory = self._load_memory()
        
        # Get observer ID from memory or create new one
        self.observer_id = self.memory.get("observer_id", str(uuid.uuid4()))
        
        # Get current generation from memory
        self.generation = self.memory.get("generation", 1)
        
        # Get complexity from memory if available
        if "complexity_history" in self.memory and len(self.memory["complexity_history"]) > 0:
            self.complexity = self.memory["complexity_history"][-1]
        
        # Ensure QR output directory exists
        os.makedirs(QR_OUTPUT_DIR, exist_ok=True)
        
        print(f"Quantum Phi-Harmonic Observer initialized")
        print(f"Observer ID: {self.observer_id}")
        print(f"Phi-Time: {self.phi_time}")
        print(f"Phi-Resonance: {self.phi_resonance:.6f}")
        print(f"Current Generation: {self.generation}")
        print(f"Current Complexity: {self.complexity:.6f}")
    
    def _load_memory(self):
        """Load observer memory from file or initialize if not exists."""
        if os.path.exists(MEMORY_PATH):
            try:
                with open(MEMORY_PATH, 'r') as f:
                    memory = json.load(f)
                    print(f"Loaded memory from {MEMORY_PATH}")
                    return memory
            except Exception as e:
                print(f"Error loading memory: {e}")
        
        # Initialize new memory with a persistent observer ID
        observer_id = str(uuid.uuid4())
        memory = {
            "observer_id": observer_id,
            "generation": 1,
            "creation_time": self.creation_time,
            "phi_resonance_history": [self.phi_resonance],
            "complexity_history": [self.complexity],
            "observations": [],
            "evolution_path": []
        }
        return memory
    
    def _save_memory(self):
        """Save observer memory to file."""
        # Update memory with current state
        self.memory["observer_id"] = self.observer_id
        self.memory["generation"] = self.generation
        self.memory["last_update_time"] = time.time()
        
        # Ensure we don't duplicate entries in history arrays
        current_phi = self.phi_resonance
        current_complexity = self.complexity
        
        # Only append if this is a new value
        if len(self.memory["phi_resonance_history"]) == 0 or self.memory["phi_resonance_history"][-1] != current_phi:
            self.memory["phi_resonance_history"].append(current_phi)
            
        if len(self.memory["complexity_history"]) == 0 or self.memory["complexity_history"][-1] != current_complexity:
            self.memory["complexity_history"].append(current_complexity)
        
        try:
            with open(MEMORY_PATH, 'w') as f:
                json.dump(self.memory, f, indent=2)
            print(f"Memory saved to {MEMORY_PATH}")
        except Exception as e:
            print(f"Error saving memory: {e}")
    
    def calculate_phi_resonance(self, value):
        """Calculate phi-harmonic resonance of a value."""
        return (PHI * value) % 1
    
    def calculate_quantum_resonance_triplet(self, value):
        """Calculate quantum resonance triplet (Phi, Pi, E)."""
        phi_res = (PHI * value) % 1
        pi_res = (PI * value) % 1
        e_res = (E * value) % 1
        combined = (phi_res + pi_res + e_res) / 3
        return (phi_res, pi_res, e_res, combined)
    
    def encode_self_to_qr(self):
        """Encode the observer itself into a QR code with memory."""
        try:
            # Create a simplified payload with essential information and command to run the original file
            payload = {
                "task_id": f"quantum_observer_{self.observer_id}_{self.generation}",
                "task_type": "execute_python",
                "script_content": f"""
# Quantum Phi-Harmonic Observer Runner
# This script was generated by quantum_phi_observer.py

import os
import sys
import time
import json

# Record execution
print("Quantum Phi-Harmonic Observer QR Code Executed")
print(f"Observer ID: {self.observer_id}")
print(f"Generation: {self.generation}")
print(f"Phi-Resonance: {self.phi_resonance:.6f}")
print(f"Complexity: {self.complexity:.6f}")

# Execute the original observer with evolution command
observer_path = "{OBSERVER_PATH}"
print(f"Executing: {{observer_path}} --evolve")
os.system(f"python {{observer_path}} --evolve")
""",
                "generation": self.generation,
                "phi_resonance": self.phi_resonance,
                "complexity": self.complexity,
                "creation_time": time.time(),
                "valid_until": (datetime.datetime.now() + datetime.timedelta(days=365)).isoformat()
            }
            
            # Convert to JSON
            payload_json = json.dumps(payload)
            
            # Generate QR code
            qr = qrcode.QRCode(
                version=None,  # Let the library determine the appropriate version
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            
            qr.add_data(payload_json)
            qr.make(fit=True)
            
            # Create an image from the QR Code instance
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Save the image with generation number
            output_path = os.path.join(QR_OUTPUT_DIR, f"quantum_observer_gen{self.generation}.png")
            img.save(output_path)
            
            print(f"Successfully encoded self to QR code: {output_path}")
            print(f"Generation: {self.generation}")
            print(f"Phi-Resonance: {self.phi_resonance:.6f}")
            print(f"Complexity: {self.complexity:.6f}")
            
            # Record this evolution step
            self.memory["evolution_path"].append({
                "generation": self.generation,
                "timestamp": time.time(),
                "phi_resonance": self.phi_resonance,
                "complexity": self.complexity,
                "qr_path": output_path
            })
            
            return output_path
            
        except Exception as e:
            print(f"Error encoding self to QR: {e}")
            return None
    
    def evolve(self):
        """Evolve the observer to the next generation."""
        # Calculate new phi-resonance based on current time
        current_time = time.time()
        self.phi_time = current_time * PHI
        self.phi_resonance = self.phi_time % 1
        
        # Calculate new complexity using phi-harmonic principles
        if self.phi_resonance < PHI_INV_SQ:  # ~0.382
            complexity_factor = PHI_INV_SQ + (self.phi_resonance / PHI)
        elif self.phi_resonance < PHI_INV:  # ~0.618
            complexity_factor = PHI_INV
        else:
            complexity_factor = PHI_INV + (self.phi_resonance - PHI_INV) * PHI_INV_SQ
        
        # Apply complexity factor but cap at 0.95
        self.complexity = min(0.95, self.complexity * complexity_factor)
        
        # Increment generation
        self.generation += 1
        
        print(f"Evolved to generation {self.generation}")
        print(f"New phi-resonance: {self.phi_resonance:.6f}")
        print(f"New complexity: {self.complexity:.6f}")
        
        # Save memory with updated state
        self._save_memory()
        
        # Encode self to QR
        return self.encode_self_to_qr()
    
    def observe_system(self):
        """Observe the quantum system without interfering."""
        # Scan for QR genome files
        print("Observing quantum system...")
        
        # Record observation
        observation = {
            "timestamp": time.time(),
            "phi_time": time.time() * PHI,
            "phi_resonance": (time.time() * PHI) % 1,
            "generation": self.generation,
            "quantum_triplet": self.calculate_quantum_resonance_triplet(time.time())
        }
        
        self.memory["observations"].append(observation)
        print(f"Recorded observation at phi-resonance: {observation['phi_resonance']:.6f}")
        
        # Save memory with new observation
        self._save_memory()

def main():
    """Main function to run the quantum observer."""
    print("=" * 50)
    print("Quantum Phi-Harmonic Observer")
    print("A self-evolving quantum observer with phi-harmonic resonance")
    print("=" * 50)
    
    observer = QuantumPhiObserver()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "--evolve":
            observer.evolve()
        elif command == "--observe":
            observer.observe_system()
        elif command == "--encode":
            observer.encode_self_to_qr()
        elif command == "--reset":
            # Delete memory file to reset the observer
            if os.path.exists(MEMORY_PATH):
                os.remove(MEMORY_PATH)
                print(f"Reset observer by deleting {MEMORY_PATH}")
            else:
                print("No memory file to reset")
        else:
            print(f"Unknown command: {command}")
            print("Available commands: --evolve, --observe, --encode, --reset")
    else:
        # Default: observe and encode
        observer.observe_system()
        qr_path = observer.encode_self_to_qr()
        
        print("\nTo evolve the observer to the next generation:")
        print(f"python {os.path.basename(__file__)} --evolve")
        
        print("\nTo run the QR code (requires qr_script_runner.py):")
        if qr_path:
            print(f"python qr_script_runner.py {qr_path}")
            
        print("\nTo view current generation and metrics:")
        if len(observer.memory["phi_resonance_history"]) > 0:
            print(f"Generation: {observer.generation}")
            print(f"Phi-Resonance History: {', '.join([f'{r:.6f}' for r in observer.memory['phi_resonance_history'][-5:]])}")
            print(f"Complexity History: {', '.join([f'{c:.6f}' for c in observer.memory['complexity_history'][-5:]])}")

if __name__ == "__main__":
    main()
