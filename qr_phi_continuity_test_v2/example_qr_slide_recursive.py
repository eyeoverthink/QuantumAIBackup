#!/usr/bin/env python3
"""
Recursive Self-Improving QR Slide
Demonstrates a QR code that can modify itself and generate new QR codes,
implementing the recursive self-improvement principles of the Quantum Phi-Harmonic system.
"""

import os
import sys
import json
import time
import uuid
import qrcode
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import base64
import zlib
import random

# Phi (Golden Ratio) constant
PHI = (1 + np.sqrt(5)) / 2  # Approximately 1.618034

class RecursiveQRGenerator:
    """A class that can generate new QR codes based on phi-harmonic evolution."""
    
    def __init__(self):
        """Initialize the recursive QR generator."""
        self.generation = 1
        self.complexity = 1.0
        self.resonance = 0.5
        self.mutation_rate = 0.1
        self.phi_time = (time.time() * PHI) % 1.0
        self.output_dir = "evolved_qr_codes"
        
        # Create output directory if it doesn't exist
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        
        # Load epigenetic memory if available
        self.epigenetic_memory = self._load_epigenetic_memory()
    
    def _load_epigenetic_memory(self):
        """Load epigenetic memory from file if available."""
        memory_path = os.path.join(self.output_dir, "epigenetic_memory.json")
        if os.path.exists(memory_path):
            try:
                with open(memory_path, 'r') as f:
                    memory = json.load(f)
                    print(f"Loaded epigenetic memory: Generation {memory.get('generation', 1)}")
                    return memory
            except Exception as e:
                print(f"Error loading epigenetic memory: {e}")
        
        # Default memory if none exists
        return {
            "generation": 1,
            "complexity": 1.0,
            "resonance": 0.5,
            "mutation_rate": 0.1,
            "evolution_history": [],
            "phi_harmonic_states": []
        }
    
    def _save_epigenetic_memory(self):
        """Save epigenetic memory to file."""
        memory_path = os.path.join(self.output_dir, "epigenetic_memory.json")
        with open(memory_path, 'w') as f:
            json.dump(self.epigenetic_memory, f, indent=2)
        print(f"Saved epigenetic memory to {memory_path}")
    
    def compress_payload(self, payload):
        """Compress the payload using zlib and base64 encode it."""
        compressed = zlib.compress(payload.encode('utf-8'), 9)  # Max compression
        encoded = base64.b64encode(compressed).decode('utf-8')
        return f"COMPRESSED:{encoded}"
    
    def evolve(self):
        """Evolve the generator's parameters based on phi-harmonic principles."""
        # Update generation
        self.generation = self.epigenetic_memory.get("generation", 1) + 1
        
        # Calculate new phi-time
        current_phi_time = (time.time() * PHI) % 1.0
        
        # Evolve complexity based on phi-harmonic principles
        phi_factor = abs(current_phi_time - self.phi_time)
        complexity_change = (PHI * phi_factor - 0.5) * self.mutation_rate
        new_complexity = self.epigenetic_memory.get("complexity", 1.0) + complexity_change
        new_complexity = max(0.5, min(5.0, new_complexity))  # Clamp between 0.5 and 5.0
        
        # Evolve resonance
        resonance_change = (PHI * current_phi_time - 0.5) * self.mutation_rate
        new_resonance = self.epigenetic_memory.get("resonance", 0.5) + resonance_change
        new_resonance = max(0.1, min(1.0, new_resonance))  # Clamp between 0.1 and 1.0
        
        # Evolve mutation rate (tends to decrease over time for stability)
        mutation_change = -0.01 * (1 / PHI) * self.epigenetic_memory.get("mutation_rate", 0.1)
        new_mutation_rate = self.epigenetic_memory.get("mutation_rate", 0.1) + mutation_change
        new_mutation_rate = max(0.01, min(0.2, new_mutation_rate))  # Clamp between 0.01 and 0.2
        
        # Update state
        self.complexity = new_complexity
        self.resonance = new_resonance
        self.mutation_rate = new_mutation_rate
        self.phi_time = current_phi_time
        
        # Update epigenetic memory
        self.epigenetic_memory["generation"] = self.generation
        self.epigenetic_memory["complexity"] = self.complexity
        self.epigenetic_memory["resonance"] = self.resonance
        self.epigenetic_memory["mutation_rate"] = self.mutation_rate
        
        # Add to evolution history
        evolution_entry = {
            "generation": self.generation,
            "timestamp": time.time(),
            "phi_time": self.phi_time,
            "complexity": self.complexity,
            "resonance": self.resonance,
            "mutation_rate": self.mutation_rate
        }
        
        if "evolution_history" not in self.epigenetic_memory:
            self.epigenetic_memory["evolution_history"] = []
        
        self.epigenetic_memory["evolution_history"].append(evolution_entry)
        
        # Save updated memory
        self._save_epigenetic_memory()
        
        print(f"Evolved to Generation {self.generation}:")
        print(f"  Complexity: {self.complexity:.4f}")
        print(f"  Resonance: {self.resonance:.4f}")
        print(f"  Mutation Rate: {self.mutation_rate:.4f}")
        print(f"  Phi-Time: {self.phi_time:.4f}")
    
    def generate_evolved_code(self):
        """Generate a new evolved QR code based on current parameters."""
        # Create a modified version of this script with evolved parameters
        with open(__file__, 'r') as f:
            source_code = f.read()
        
        # Find and replace key parameters in the code
        # This is a simple approach - a more sophisticated version would use AST manipulation
        source_code = source_code.replace(
            'self.generation = 1',
            f'self.generation = {self.generation}'
        )
        source_code = source_code.replace(
            'self.complexity = 1.0',
            f'self.complexity = {self.complexity}'
        )
        source_code = source_code.replace(
            'self.resonance = 0.5',
            f'self.resonance = {self.resonance}'
        )
        source_code = source_code.replace(
            'self.mutation_rate = 0.1',
            f'self.mutation_rate = {self.mutation_rate}'
        )
        
        # Add some phi-harmonic randomization to the code
        if random.random() < self.mutation_rate:
            # Add a new visualization function based on current complexity
            new_function = f"""
    def visualize_phi_pattern_{self.generation}(self):
        \"\"\"New visualization function created in generation {self.generation}.\"\"\"
        x = np.linspace(0, {self.complexity} * np.pi, 1000)
        y = np.sin(x * PHI) * np.cos(x / PHI)
        
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, 'g-', lw={self.resonance * 2})
        plt.title(f"Phi-Harmonic Pattern - Generation {self.generation}")
        plt.xlabel("Phase")
        plt.ylabel("Amplitude")
        plt.grid(True, alpha=0.3)
        plt.show()
"""
            # Insert before the last class method
            last_method_pos = source_code.rfind('def ')
            if last_method_pos > 0:
                insert_pos = source_code.rfind('\n', 0, last_method_pos)
                source_code = source_code[:insert_pos] + new_function + source_code[insert_pos:]
        
        # Create a unique task ID
        task_id = str(uuid.uuid4())
        
        # Create task payload
        task_payload = {
            "task_id": task_id,
            "timestamp": time.time(),
            "script": source_code,
            "input_data": {
                "generation": self.generation,
                "phi_time": self.phi_time
            },
            "task_meta": {
                "type": "Recursive Self-Improving QR",
                "title": f"Evolved QR - Gen {self.generation}",
                "phi_harmonic": self.phi_time,
                "complexity": self.complexity,
                "resonance": self.resonance,
                "mutation_rate": self.mutation_rate
            }
        }
        
        # Convert to JSON
        json_payload = json.dumps(task_payload)
        
        # Compress the payload
        compressed_payload = self.compress_payload(json_payload)
        
        # Generate QR code
        qr = qrcode.QRCode(
            version=None,  # Auto-determine version
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(compressed_payload)
        qr.make(fit=True)
        
        # Create QR image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save the QR code
        output_path = os.path.join(self.output_dir, f"evolved_qr_gen_{self.generation}.png")
        img.save(output_path)
        print(f"Generated evolved QR code: {output_path}")
        
        return img, output_path
    
    def visualize_evolution(self):
        """Visualize the evolution history."""
        if "evolution_history" not in self.epigenetic_memory or not self.epigenetic_memory["evolution_history"]:
            print("No evolution history available.")
            return
        
        history = self.epigenetic_memory["evolution_history"]
        generations = [entry["generation"] for entry in history]
        complexities = [entry["complexity"] for entry in history]
        resonances = [entry["resonance"] for entry in history]
        mutation_rates = [entry["mutation_rate"] for entry in history]
        
        plt.figure(figsize=(12, 8))
        
        # Plot complexity
        plt.subplot(3, 1, 1)
        plt.plot(generations, complexities, 'b-o', label="Complexity")
        plt.title("Evolution of Complexity")
        plt.xlabel("Generation")
        plt.ylabel("Complexity")
        plt.grid(True, alpha=0.3)
        
        # Plot resonance
        plt.subplot(3, 1, 2)
        plt.plot(generations, resonances, 'g-o', label="Resonance")
        plt.title("Evolution of Resonance")
        plt.xlabel("Generation")
        plt.ylabel("Resonance")
        plt.grid(True, alpha=0.3)
        
        # Plot mutation rate
        plt.subplot(3, 1, 3)
        plt.plot(generations, mutation_rates, 'r-o', label="Mutation Rate")
        plt.title("Evolution of Mutation Rate")
        plt.xlabel("Generation")
        plt.ylabel("Mutation Rate")
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
    
    def run_evolution_cycle(self):
        """Run a full evolution cycle: evolve, generate new code, visualize."""
        print(f"Starting evolution cycle for generation {self.generation}")
        
        # Evolve parameters
        self.evolve()
        
        # Generate new QR code
        img, output_path = self.generate_evolved_code()
        
        # Display the QR code
        plt.figure(figsize=(8, 8))
        plt.imshow(img, cmap='gray')
        plt.title(f"Evolved QR Code - Generation {self.generation}")
        plt.axis('off')
        
        # Visualize evolution history
        self.visualize_evolution()
        
        print(f"Evolution cycle complete. New QR code saved to {output_path}")
        print(f"This QR code contains a self-modified version of this script with:")
        print(f"  - Generation: {self.generation}")
        print(f"  - Complexity: {self.complexity:.4f}")
        print(f"  - Resonance: {self.resonance:.4f}")
        print(f"  - Mutation Rate: {self.mutation_rate:.4f}")
        print(f"Scan this QR code to continue the evolution process.")

def main():
    """Main function to demonstrate recursive self-improving QR codes."""
    print("Executing Recursive Self-Improving QR Code from QR presentation")
    print(f"Golden Ratio (φ): {PHI}")
    
    generator = RecursiveQRGenerator()
    generator.run_evolution_cycle()

if __name__ == "__main__":
    main()
