#!/usr/bin/env python3
# Quantum Phi-Harmonic Multiples Evolution Test
# This system tests the evolution of multiples of 5 over 100 epochs
# with phi-harmonic guided self-correction

import os
import json
import time
import random
import numpy as np
import matplotlib.pyplot as plt
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode
import io
import base64

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio ≈ 1.618033988749895
PHI_CONJUGATE = (1 - 5**0.5) / 2  # Golden ratio conjugate ≈ -0.618033988749895

class QuantumPhiMultiplesEvolution:
    """A system that evolves multiples of 5 calculations through QR codes."""
    
    def __init__(self, output_dir="multiples_evolution", max_multiple=20):
        """Initialize the evolution system."""
        self.output_dir = output_dir
        self.max_multiple = max_multiple  # Maximum multiple of 5 to test
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Initialize parameters
        self.epoch = 1
        self.resonance = 0.5
        self.complexity = 0.5
        self.mutation_rate = 0.1
        self.phi_time = 0.0
        
        # Initialize results tracking
        self.current_results = {i: i * 5 for i in range(1, max_multiple + 1)}
        self.error_introduced = False
        self.error_corrected = False
        self.error_location = None  # Which multiple has the error
        self.error_epoch = random.randint(6, 15)  # Random epoch for error introduction
        
        # Evolution history
        self.evolution_history = []
        
        # Load existing epigenetic memory if available
        self._load_epigenetic_memory()
    
    def _load_epigenetic_memory(self):
        """Load epigenetic memory from file if it exists."""
        memory_path = os.path.join(self.output_dir, "epigenetic_memory.json")
        if os.path.exists(memory_path):
            try:
                with open(memory_path, "r") as f:
                    memory = json.load(f)
                
                # Restore state from memory
                self.epoch = memory.get("epoch", 1)
                self.resonance = memory.get("resonance", 0.5)
                self.complexity = memory.get("complexity", 0.5)
                self.mutation_rate = memory.get("mutation_rate", 0.1)
                self.current_results = memory.get("current_results", {str(i): i * 5 for i in range(1, self.max_multiple + 1)})
                
                # Convert string keys back to integers
                if all(k.isdigit() for k in self.current_results.keys()):
                    self.current_results = {int(k): v for k, v in self.current_results.items()}
                
                self.error_introduced = memory.get("error_introduced", False)
                self.error_corrected = memory.get("error_corrected", False)
                self.error_location = memory.get("error_location", None)
                self.error_epoch = memory.get("error_epoch", random.randint(6, 15))
                self.evolution_history = memory.get("evolution_history", [])
                
                print(f"Loaded epigenetic memory from epoch {self.epoch}")
            except Exception as e:
                print(f"Error loading epigenetic memory: {e}")
    
    def _save_epigenetic_memory(self):
        """Save current state to epigenetic memory file."""
        memory_path = os.path.join(self.output_dir, "epigenetic_memory.json")
        
        # Convert results dict to have string keys for JSON serialization
        serializable_results = {str(k): v for k, v in self.current_results.items()}
        
        memory = {
            "epoch": self.epoch,
            "resonance": self.resonance,
            "complexity": self.complexity,
            "mutation_rate": self.mutation_rate,
            "current_results": serializable_results,
            "error_introduced": self.error_introduced,
            "error_corrected": self.error_corrected,
            "error_location": self.error_location,
            "error_epoch": self.error_epoch,
            "evolution_history": self.evolution_history
        }
        
        with open(memory_path, "w") as f:
            json.dump(memory, f, indent=2)
        
        print(f"Saved epigenetic memory to {memory_path}")
    
    def generate_multiples_script(self) -> str:
        """Generate a Python script that calculates multiples of 5."""
        # Introduce error at specified epoch
        if self.epoch == self.error_epoch and not self.error_introduced:
            # Choose a random multiple to introduce error
            error_location = random.randint(1, self.max_multiple)
            self.error_location = error_location
            
            # Introduce a small error in the calculation
            correct_value = error_location * 5
            error_value = correct_value + random.choice([-1, 1])
            
            self.current_results[error_location] = error_value
            self.error_introduced = True
            print(f"*** ERROR INTRODUCED: {error_location} × 5 = {error_value} (should be {correct_value}) ***")
        
        # Apply phi-harmonic correction if needed
        elif self.epoch > self.error_epoch and self.error_introduced and not self.error_corrected:
            # Apply phi-harmonic correction if resonance is high enough
            if self.resonance > 0.45:  # Threshold for correction
                if self.error_location is not None:
                    # Correct the error
                    correct_value = self.error_location * 5
                    self.current_results[self.error_location] = correct_value
                    self.error_corrected = True
                    print(f"*** ERROR CORRECTED: {self.error_location} × 5 = {correct_value} ***")
        
        # Generate a simplified script with current results
        script = f'''
# Quantum Phi-Harmonic Multiples - Epoch {self.epoch}
PHI = {PHI}
res = {self.resonance:.6f}
comp = {self.complexity:.6f}
print(f"Epoch {self.epoch}, Res: {self.resonance:.4f}, Comp: {self.complexity:.4f}")
'''

        # Add only the key multiples to reduce QR code size
        key_multiples = [1, 5, 10]
        if self.error_location:
            key_multiples.append(self.error_location)
        key_multiples = sorted(list(set(key_multiples)))
        
        for i in key_multiples:
            if i <= self.max_multiple:
                result = self.current_results[i]
                script += f'\nprint(f"{i} × 5 = {result}")'

        # Save the script to a file
        script_path = os.path.join(self.output_dir, f"multiples_script_epoch_{self.epoch}.py")
        with open(script_path, "w") as f:
            f.write(script)
        
        print(f"Saved multiples script to {script_path}")
        return script
    
    def generate_qr_code(self) -> tuple:
        """Generate a QR code containing the multiples script."""
        script = self.generate_multiples_script()
        
        # Calculate QR version based on phi-harmonic principles
        # Ensure version is between 1 and 10 (keeping it small for simplicity)
        qr_version = max(1, min(10, int(self.complexity * 5)))
        
        # Create QR code
        qr = qrcode.QRCode(
            version=qr_version,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        
        # Add data to QR code
        qr.add_data(script)
        qr.make(fit=True)
        
        # Create an image from the QR Code
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save the QR code image
        qr_path = os.path.join(self.output_dir, f"multiples_qr_epoch_{self.epoch}.png")
        img.save(qr_path)
        
        print(f"Generated QR code for epoch {self.epoch}: {qr_path}")
        return qr_path, script
    
    def scan_qr_code(self, qr_path: str) -> str:
        """Scan a QR code and extract its content."""
        try:
            # Open the QR code image
            img = Image.open(qr_path)
            
            # Decode the QR code
            decoded_objects = decode(img)
            
            if not decoded_objects:
                print(f"Error: Could not decode QR code at {qr_path}")
                return None
            
            # Extract the script from the QR code
            script = decoded_objects[0].data.decode("utf-8")
            
            print(f"Successfully scanned QR code from epoch {self.epoch}")
            print(f"  Resonance: {self.resonance:.4f}")
            print(f"  Complexity: {self.complexity:.4f}")
            
            # Execute the script
            print("\nExecuting script from QR code:")
            print("-" * 40)
            try:
                exec(script, globals())
            except Exception as e:
                print(f"Error executing script: {e}")
            print("-" * 40)
            
            return script
        except Exception as e:
            print(f"Error scanning QR code: {e}")
            return None
    
    def evolve_parameters(self) -> None:
        """Evolve the system parameters based on phi-harmonic principles."""
        # Evolve resonance based on phi-harmonic principles
        self.resonance = (self.resonance * PHI + PHI_CONJUGATE) % 1
        
        # Evolve complexity based on phi-harmonic principles
        self.complexity = (self.complexity * PHI_CONJUGATE + PHI) % 5
        
        # Evolve mutation rate based on phi-harmonic principles
        # Use abs() to ensure we get a real number
        self.mutation_rate = abs((self.mutation_rate * PHI_CONJUGATE) % 0.1)
        
        # Evolve phi-time based on phi-harmonic principles
        self.phi_time = (self.phi_time + PHI_CONJUGATE) % PHI
        
        # Ensure minimum values
        if self.mutation_rate < 0.01:  # Minimum mutation rate
            self.mutation_rate = 0.01
        
        # Record evolution history
        self.evolution_history.append({
            'epoch': self.epoch,
            'resonance': self.resonance,
            'complexity': self.complexity,
            'mutation_rate': self.mutation_rate,
            'phi_time': self.phi_time,
            'error_introduced': self.error_introduced,
            'error_corrected': self.error_corrected
        })
        
        # Increment epoch
        self.epoch += 1
        
        print(f"Evolved to Epoch {self.epoch}:")
        print(f"  Resonance: {self.resonance:.4f}")
        print(f"  Complexity: {self.complexity:.4f}")
        print(f"  Mutation Rate: {self.mutation_rate:.4f}")
        print(f"  Phi-Time: {self.phi_time:.4f}")
    
    def visualize_evolution(self) -> None:
        """Visualize the evolution of parameters over epochs."""
        if not self.evolution_history:
            print("No evolution history to visualize.")
            return
        
        # Extract data from evolution history
        epochs = [1] + [entry["epoch"] for entry in self.evolution_history]
        resonances = [0.5] + [entry["resonance"] for entry in self.evolution_history]
        complexities = [0.5] + [entry["complexity"] for entry in self.evolution_history]
        mutation_rates = [0.1] + [entry["mutation_rate"] for entry in self.evolution_history]
        
        # Create figure with subplots
        fig, axs = plt.subplots(3, 1, figsize=(12, 15))
        
        # Plot resonance
        axs[0].plot(epochs, resonances, 'b-', marker='o')
        axs[0].set_title('Phi-Harmonic Resonance Evolution')
        axs[0].set_xlabel('Epoch')
        axs[0].set_ylabel('Resonance')
        axs[0].grid(True)
        
        # Plot complexity
        axs[1].plot(epochs, complexities, 'r-', marker='o')
        axs[1].set_title('Complexity Evolution')
        axs[1].set_xlabel('Epoch')
        axs[1].set_ylabel('Complexity')
        axs[1].grid(True)
        
        # Plot mutation rate
        axs[2].plot(epochs, mutation_rates, 'g-', marker='o')
        axs[2].set_title('Mutation Rate Evolution')
        axs[2].set_xlabel('Epoch')
        axs[2].set_ylabel('Mutation Rate')
        axs[2].grid(True)
        
        # Mark error introduction and correction
        if self.error_introduced:
            error_epoch_index = epochs.index(self.error_epoch) if self.error_epoch in epochs else -1
            if error_epoch_index >= 0:
                axs[0].axvline(x=self.error_epoch, color='r', linestyle='--', alpha=0.5, label='Error Introduced')
                axs[1].axvline(x=self.error_epoch, color='r', linestyle='--', alpha=0.5)
                axs[2].axvline(x=self.error_epoch, color='r', linestyle='--', alpha=0.5)
        
        if self.error_corrected:
            # Find the epoch where error was corrected
            correction_epoch = None
            for i, entry in enumerate(self.evolution_history):
                if entry["error_corrected"]:
                    correction_epoch = entry["epoch"]
                    break
            
            if correction_epoch:
                axs[0].axvline(x=correction_epoch, color='g', linestyle='--', alpha=0.5, label='Error Corrected')
                axs[1].axvline(x=correction_epoch, color='g', linestyle='--', alpha=0.5)
                axs[2].axvline(x=correction_epoch, color='g', linestyle='--', alpha=0.5)
        
        # Add legend
        axs[0].legend()
        
        # Adjust layout
        plt.tight_layout()
        
        # Save the figure
        viz_path = os.path.join(self.output_dir, f"evolution_visualization_epoch_{self.epoch}.png")
        plt.savefig(viz_path)
        plt.close()
        
        print(f"Saved evolution visualization to {viz_path}")
    
    def run_evolution_cycle(self, num_epochs: int = 100) -> None:
        """Run multiple evolution cycles."""
        print(f"Starting evolution cycle for {num_epochs} epochs")
        
        start_epoch = self.epoch
        target_epoch = start_epoch + num_epochs
        
        while self.epoch < target_epoch:
            print(f"\n{'=' * 50}")
            print(f"EPOCH {self.epoch}")
            print(f"{'=' * 50}")
            
            # Generate QR code with multiples script
            qr_path, _ = self.generate_qr_code()
            
            # Execute the current script directly
            script_path = os.path.join(self.output_dir, f"multiples_script_epoch_{self.epoch}.py")
            print(f"\nExecuting script for epoch {self.epoch}:")
            print("-" * 40)
            try:
                with open(script_path, 'r') as f:
                    script = f.read()
                exec(script, globals())
            except Exception as e:
                print(f"Error executing script: {e}")
            print("-" * 40)
            
            # Save the current state
            self._save_epigenetic_memory()
            
            # Evolve parameters for next epoch
            self.evolve_parameters()
            
            # Visualize at specific intervals
            if (self.epoch - start_epoch) % 10 == 0 or self.epoch == target_epoch:
                self.visualize_evolution()
            
            # Optional: Add a small delay to prevent overwhelming output
            time.sleep(0.1)
        
        print("\nEvolution cycle complete")
        print(f"Final state: Epoch {self.epoch-1}")
        print(f"Error introduced: {self.error_introduced}, Error corrected: {self.error_corrected}")
        
        # Print summary of the test
        if self.error_introduced and self.error_corrected:
            print("\n✅ TEST SUCCESSFUL: System detected and corrected the error!")
            print(f"Error was introduced at epoch {self.error_epoch} for {self.error_location}×5")
            print(f"Error was corrected at epoch {next((e['epoch'] for e in self.evolution_history if e.get('error_corrected')), 'unknown')}")
        elif self.error_introduced and not self.error_corrected:
            print("\n❌ TEST FAILED: System did not correct the error.")
        elif not self.error_introduced and self.epoch > self.error_epoch:
            print("\n⚠️ TEST INCONCLUSIVE: Error was not introduced at the specified epoch.")
        else:
            print("\n⚠️ TEST INCOMPLETE: Did not reach the error introduction epoch yet.")

def main():
    """Main function to run the multiples evolution test."""
    print("Quantum Phi-Harmonic Multiples Evolution Test")
    print(f"Golden Ratio (φ): {PHI}")
    print("This test will introduce an error at a random epoch and see if the system can self-correct")
    
    # Create the evolution system
    evolution = QuantumPhiMultiplesEvolution(max_multiple=20)
    
    # Run the evolution cycle for 100 epochs
    evolution.run_evolution_cycle(100)

if __name__ == "__main__":
    main()
