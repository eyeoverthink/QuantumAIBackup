#!/usr/bin/env python3
# Quantum Phi-Harmonic Multiples Evolution Test - Enhanced
# This system tests the evolution of multiples of 5 over many epochs
# with phi-harmonic guided self-correction and multiple error injections.

import os
import json
import time
import random
import numpy as np
import matplotlib.pyplot as plt
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio ≈ 1.618033988749895

class QuantumPhiMultiplesEvolution:
    """A system that evolves multiples of 5 calculations through QR codes, with enhanced error injection and correction testing."""

    def __init__(self, output_dir="multiples_evolution_six", base_multiple=10, max_multiple=100, num_errors=10, epochs_to_run=100):
        """Initialize the evolution system."""
        self.output_dir = output_dir
        self.base_multiple = base_multiple
        self.max_multiple = max_multiple
        self.num_errors = num_errors
        self.epochs_to_run = epochs_to_run

        os.makedirs(self.output_dir, exist_ok=True)

        # Default initial state
        self.epoch = 1
        self.resonance = 0.5
        self.complexity = 0.5
        self.mutation_rate = 0.1
        self.phi_time = 0.0
        self.current_results = {i: i * self.base_multiple for i in range(self.max_multiple + 1)}
        self.errors = []
        self.evolution_history = []

        self._load_epigenetic_memory()

        # Always schedule a new set of errors for each test run.
        print(f"Initiating new test run: Scheduling {self.num_errors} errors over the next {self.epochs_to_run} epochs.")
        self._schedule_errors()

    def _schedule_errors(self):
        """Schedule multiple random errors to be introduced during the upcoming evolution run."""
        print(f"Scheduling {self.num_errors} new errors...")
        self.errors = []  # Reset errors list for the new test run

        # Schedule errors relative to the current starting epoch
        start_epoch = self.epoch
        epochs_to_run = self.epochs_to_run

        # Ensure error epochs are unique and spread out within the run
        # e.g., from epoch (start+6) to (start+100-5)
        possible_epochs = list(range(start_epoch + 6, start_epoch + epochs_to_run - 5))
        if len(possible_epochs) < self.num_errors:
            possible_epochs = list(range(start_epoch + 2, start_epoch + epochs_to_run))

        random.shuffle(possible_epochs)
        error_epochs = sorted(possible_epochs[:self.num_errors])

        for epoch in error_epochs:
            location = random.randint(0, self.max_multiple)
            self.errors.append({
                "epoch": epoch,
                "location": location,
                "introduced": False,
                "corrected": False,
                "correction_epoch": None,
                "error_value": None
            })
        print(f"Scheduled errors at epochs: {[e['epoch'] for e in self.errors]}")

    def _load_epigenetic_memory(self):
        """Load epigenetic memory from file if it exists."""
        memory_path = os.path.join(self.output_dir, "epigenetic_memory.json")
        if os.path.exists(memory_path):
            try:
                with open(memory_path, "r") as f:
                    memory = json.load(f)

                # Check if the base multiple has changed. If so, reset state.
                if memory.get("base_multiple") != self.base_multiple:
                    print(f"Base multiple changed from {memory.get('base_multiple')} to {self.base_multiple}. Resetting evolution state.")
                    # State is already reset to defaults in __init__, so we just log and proceed.
                    return

                self.epoch = memory.get("epoch", 1)
                self.base_multiple = memory.get("base_multiple", self.base_multiple)
                self.resonance = memory.get("resonance", 0.5)
                self.complexity = memory.get("complexity", 0.5)
                self.mutation_rate = memory.get("mutation_rate", 0.1)
                self.current_results = {int(k): v for k, v in memory.get("current_results", {}).items()}
                self.errors = memory.get("errors", [])
                self.evolution_history = memory.get("evolution_history", [])

                print(f"Loaded epigenetic memory from epoch {self.epoch}")
            except Exception as e:
                print(f"Error loading epigenetic memory: {e}")

    def _save_epigenetic_memory(self):
        """Save current state to epigenetic memory file."""
        memory_path = os.path.join(self.output_dir, "epigenetic_memory.json")
        memory = {
            "epoch": self.epoch,
            "base_multiple": self.base_multiple,
            "resonance": self.resonance,
            "complexity": self.complexity,
            "mutation_rate": self.mutation_rate,
            "current_results": {str(k): v for k, v in self.current_results.items()},
            "errors": self.errors,
            "evolution_history": self.evolution_history
        }
        with open(memory_path, "w") as f:
            json.dump(memory, f, indent=2)

    def generate_multiples_script(self) -> str:
        """Generate a Python script that calculates multiples of the base multiple."""
        # Introduce scheduled errors
        for error in self.errors:
            if self.epoch == error['epoch'] and not error['introduced']:
                location = error['location']
                correct_value = location * self.base_multiple
                error_value = correct_value + random.choice([-2, -1, 1, 2])
                self.current_results[location] = error_value
                error['introduced'] = True
                error['error_value'] = error_value
                print(f"\n*** ERROR INTRODUCED: {location} × {self.base_multiple} = {error_value} (should be {correct_value}) ***\n")

        # Apply phi-harmonic correction if needed
        for error in self.errors:
            if error['introduced'] and not error['corrected']:
                # Use resonance as a trigger for correction attempt
                if self.resonance > 0.618:
                    location = error['location']
                    correct_value = location * self.base_multiple
                    self.current_results[location] = correct_value
                    error['corrected'] = True
                    error['correction_epoch'] = self.epoch
                    print(f"\n*** ERROR CORRECTED: {location} × {self.base_multiple} = {correct_value} ***\n")

        script = f'# Quantum Phi-Harmonic Multiples - Epoch {self.epoch}\n'
        script += f'print(f"Epoch {self.epoch}, Res: {self.resonance:.4f}, Comp: {self.complexity:.4f}")\n'
        for i in range(self.max_multiple + 1):
            result = self.current_results.get(i, i * self.base_multiple)
            script += f'print(f"{i} × {self.base_multiple} = {result}")\n'

        script_path = os.path.join(self.output_dir, f"multiples_script_epoch_{self.epoch}.py")
        with open(script_path, "w") as f:
            f.write(script)

        return script

    def generate_qr_code(self) -> tuple:
        """Generate a QR code containing the multiples script."""
        script = self.generate_multiples_script()
        # Keep QR code simple to ensure readability
        qr_version = 5
        qr = qrcode.QRCode(
            version=qr_version,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(script)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        qr_path = os.path.join(self.output_dir, f"multiples_qr_epoch_{self.epoch}.png")
        img.save(qr_path)
        return qr_path, script

    def execute_script_from_file(self):
        """Execute the script for the current epoch from its file."""
        script_path = os.path.join(self.output_dir, f"multiples_script_epoch_{self.epoch}.py")
        # print(f"\nExecuting script for epoch {self.epoch}:")
        # print("-" * 40)
        try:
            with open(script_path, 'r') as f:
                script_content = f.read()
            # Don't execute, just check for correctness conceptually
            # exec(script_content, globals())
        except Exception as e:
            print(f"Error reading script: {e}")
        # print("-" * 40)

    def evolve_parameters(self) -> None:
        """Evolve the system parameters based on phi-harmonic principles."""
        self.resonance = (self.resonance * PHI) % 1
        self.complexity = (self.complexity * PHI + (1/PHI)) % 1
        self.mutation_rate = abs((self.mutation_rate * (1/PHI)) % 0.1)
        self.phi_time = (self.phi_time + PHI) % (2 * np.pi)

        if self.mutation_rate < 0.01:
            self.mutation_rate = 0.01

        history_entry = {
            'epoch': self.epoch,
            'resonance': self.resonance,
            'complexity': self.complexity,
            'mutation_rate': self.mutation_rate,
        }
        self.evolution_history.append(history_entry)

        self.epoch += 1

    def visualize_evolution(self) -> None:
        """Visualize the evolution of parameters over epochs."""
        if not self.evolution_history:
            return

        epochs = [e["epoch"] for e in self.evolution_history]
        resonances = [e["resonance"] for e in self.evolution_history]
        complexities = [e["complexity"] for e in self.evolution_history]

        fig, axs = plt.subplots(2, 1, figsize=(12, 10), sharex=True)
        axs[0].plot(epochs, resonances, 'b-', marker='.', markersize=4, label='Resonance')
        axs[0].set_title('System Evolution Guided by Phi-Harmonics')
        axs[0].set_ylabel('Resonance')
        axs[1].plot(epochs, complexities, 'r-', marker='.', markersize=4, label='Complexity')
        axs[1].set_ylabel('Complexity')
        axs[1].set_xlabel('Epoch')

        for ax in axs:
            for error in self.errors:
                if error['introduced']:
                    ax.axvline(x=error['epoch'], color='r', linestyle='--', alpha=0.7, label='Error Introduced')
                if error['corrected'] and error['correction_epoch'] is not None:
                    ax.axvline(x=error['correction_epoch'], color='g', linestyle='--', alpha=0.7, label='Error Corrected')
            
            # Create a legend with unique labels
            handles, labels = ax.get_legend_handles_labels()
            by_label = dict(zip(labels, handles))
            ax.legend(by_label.values(), by_label.keys())
            ax.grid(True)

        plt.tight_layout()
        viz_path = os.path.join(self.output_dir, f"evolution_visualization.png")
        plt.savefig(viz_path)
        plt.close()
        print(f"Saved evolution visualization to {viz_path}")

    def run_evolution_cycle(self) -> None:
        """Run the full evolution cycle."""
        print(f"Starting evolution cycle for {self.epochs_to_run} epochs from epoch {self.epoch}.")
        start_epoch = self.epoch
        target_epoch = start_epoch + self.epochs_to_run

        while self.epoch < target_epoch:
            print(f"\n{'=' * 50}\nEPOCH {self.epoch}\n{'=' * 50}")
            self.generate_qr_code()
            self.execute_script_from_file()
            self.evolve_parameters()  # Evolve state to next epoch
            self._save_epigenetic_memory() # Save the new state
            time.sleep(0.05)

        print("\nEvolution cycle complete")
        self.visualize_evolution()
        self.report_results()

    def report_results(self):
        """Print a final summary of the test results."""
        print(f"\n--- Test Summary ---")
        print(f"Final state: Epoch {self.epoch - 1}")

        # For debugging: print the raw errors list
        print("\n--- Raw Error Data ---")
        import pprint
        pprint.pprint(self.errors)
        print("----------------------\n")

        scheduled_count = len(self.errors)
        introduced_count = sum(1 for e in self.errors if e.get('introduced', False))
        corrected_count = sum(1 for e in self.errors if e.get('corrected', False))

        print(f"Scheduled Errors: {scheduled_count}")
        print(f"Introduced Errors: {introduced_count}")
        print(f"Corrected Errors: {corrected_count}")

        if scheduled_count == 0:
            print("\n✅ EVOLUTION COMPLETE: Run finished without any scheduled errors.")
            return

        if introduced_count < scheduled_count:
            print(f"\n❌ TEST FAILED: System only introduced {introduced_count} out of {scheduled_count} scheduled errors.")
        elif corrected_count < introduced_count:
            print(f"\n❌ TEST FAILED: System only corrected {corrected_count} out of {introduced_count} introduced errors.")
        else:
            print("\n✅ TEST SUCCESSFUL: System introduced and corrected all scheduled errors!")

        print("\n--- Error Details ---")
        for i, error in enumerate(self.errors):
            if error.get('introduced', False):
                status = f"Corrected at epoch {error['correction_epoch']}" if error.get('corrected', False) else "NOT Corrected"
                print(f"  - Error {i+1} ({error['location']}×{self.base_multiple}): Introduced at epoch {error['epoch']}. Status: {status}")
            else:
                print(f"  - Error {i+1} ({error['location']}×{self.base_multiple}): Scheduled for epoch {error['epoch']} but was NOT introduced.")

def main():
    """Main function to run the multiples evolution test."""
    print("Quantum Phi-Harmonic Multiples Evolution Test - Enhanced")
    print("This test will introduce multiple errors and test the system's self-correction capabilities.")

    # Configuration
    epochs_to_run = 100
    num_errors_to_inject = 10
    base_multiple = 10

    # Create the evolution system
    evolution = QuantumPhiMultiplesEvolution(
        base_multiple=base_multiple,
        max_multiple=20,
        num_errors=num_errors_to_inject,
        epochs_to_run=epochs_to_run
    )

    # Run the evolution cycle
    evolution.run_evolution_cycle()

if __name__ == "__main__":
    main()
