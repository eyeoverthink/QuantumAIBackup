import os
import json
import time
import random
import numpy as np
import matplotlib.pyplot as plt
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode
from components.dream_integrator import DreamIntegrator

# Golden Ratio & Prime Dream Artifact
PHI = (1 + 5 ** 0.5) / 2
DREAM_PRIME = 6765 # A Fibonacci-related number for high resonance

class QuantumPhiMultiplesDreamEvolution:
    """A system that evolves multiples, with the ability to process
    'AI Dreams'—impossible anomalies—using phi-harmonic principles.
    """
    def __init__(self, output_dir="dream_evolution_one", base_multiple=10, max_multiple=100, num_errors=10, epochs_to_run=100):
        """Initialize the dream evolution system."""
        self.output_dir = output_dir
        self.base_multiple = base_multiple
        self.max_multiple = max_multiple
        self.num_errors = num_errors
        self.epochs_to_run = epochs_to_run
        self.dream_integrator = DreamIntegrator()

        os.makedirs(self.output_dir, exist_ok=True)

        # Default initial state
        self.epoch = 1
        self.resonance = 0.5
        self.complexity = 0.5
        self.phi_time = 0.0
        self.current_results = {i: i * self.base_multiple for i in range(self.max_multiple + 1)}
        self.events = []
        self.evolution_history = []

        self._load_epigenetic_memory()

        print(f"Initiating new test run: Scheduling {self.num_errors - 1} errors and 1 dream over the next {self.epochs_to_run} epochs.")
        self._schedule_events()

    def _schedule_events(self):
        """Schedule errors and a single 'dream' event."""
        self.events = []
        possible_epochs = list(range(self.epoch, self.epoch + self.epochs_to_run))
        
        # Schedule one dream
        dream_epoch = random.choice(possible_epochs)
        self.events.append({
            'type': 'dream',
            'epoch': dream_epoch,
            'location': random.randint(1, self.max_multiple), # Ensure location > 0 for paradigm shift
            'introduced': False,
            'processed': False,
            'insight': None # To store dream analysis result
        })

        # Schedule N-1 errors, ensuring no overlap with the dream
        error_epochs = random.sample([e for e in possible_epochs if e != dream_epoch], self.num_errors - 1)
        for epoch in error_epochs:
            self.events.append({
                'type': 'error',
                'epoch': epoch,
                'location': random.randint(0, self.max_multiple),
                'introduced': False,
                'corrected': False,
                'correction_epoch': -1
            })
        self.events.sort(key=lambda x: x['epoch'])
        print(f"Scheduled dream at epoch: {dream_epoch}")
        print(f"Scheduled errors at epochs: {[e['epoch'] for e in self.events if e['type'] == 'error']}")

    def _load_epigenetic_memory(self):
        memory_path = os.path.join(self.output_dir, "epigenetic_memory.json")
        if os.path.exists(memory_path):
            try:
                with open(memory_path, "r") as f: memory = json.load(f)
                if memory.get("base_multiple") != self.base_multiple:
                    print("Base multiple changed. Resetting state.")
                    self.epoch = memory.get("epoch", 1)
                    return
                self.epoch, self.resonance, self.complexity, self.phi_time = memory.get("epoch", 1), memory.get("resonance", 0.5), memory.get("complexity", 0.5), memory.get("phi_time", 0.0)
                self.current_results = {int(k): v for k, v in memory.get("current_results", {}).items()}
                self.evolution_history = memory.get("evolution_history", [])
                print(f"Loaded epigenetic memory from epoch {self.epoch}")
            except Exception as e:
                print(f"Could not load memory: {e}. Starting fresh.")

    def _save_epigenetic_memory(self):
        memory_path = os.path.join(self.output_dir, "epigenetic_memory.json")
        with open(memory_path, "w") as f:
            json.dump({
                "epoch": self.epoch, "base_multiple": self.base_multiple, "resonance": self.resonance,
                "complexity": self.complexity, "phi_time": self.phi_time, "current_results": self.current_results,
                "events_this_run": self.events, "evolution_history": self.evolution_history
            }, f, indent=4)

    def generate_script_and_inject_events(self):
        for event in self.events:
            if self.epoch == event['epoch'] and not event['introduced']:
                location = event['location']
                correct_value = location * self.base_multiple
                if event['type'] == 'error':
                    error_value = correct_value + random.choice([-2, -1, 1, 2])
                    self.current_results[location] = error_value
                    print(f"*** ERROR INTRODUCED: {location} × {self.base_multiple} = {error_value} (should be {correct_value}) ***")
                elif event['type'] == 'dream':
                    self.current_results[location] = DREAM_PRIME
                    print(f"\n>>> AI DREAM INITIATED at location {location}. Anomaly value: {DREAM_PRIME} <<<")
                event['introduced'] = True
        
        script_content = f'multiples = {json.dumps(self.current_results, indent=4)}'
        script_path = os.path.join(self.output_dir, f"epoch_{self.epoch}_script.py")
        with open(script_path, "w") as f: f.write(script_content)

    def handle_dream_anomaly(self, location, anomaly_value):
        dream_event = next((e for e in self.events if e['type'] == 'dream' and e['location'] == location and not e['processed']), None)
        if not dream_event: return

        analysis = self.dream_integrator.analyze_dream(anomaly_value, location, self.base_multiple)
        resonance = analysis['resonance']
        dream_event['insight'] = analysis['insight']

        print(f"--- DREAM ANALYSIS: Anomaly {anomaly_value} has Phi-Resonance of {resonance:.4f} ---")

        if analysis['insight'] == 'Paradigm Shift':
            new_base_multiple = analysis['new_base_multiple']
            print(f"\n*** PARADIGM SHIFT: High-resonance dream suggests a new reality. ***")
            print(f"--- Changing base multiple from {self.base_multiple} to {new_base_multiple:.4f} ---")
            self.base_multiple = new_base_multiple
            self.resonance = 1.0 # Reset to max resonance after a breakthrough
            self.complexity = 0.0 # Reset complexity as the new rule is simple
            # Log the paradigm shift event for visualization
            self.events.append({
                'type': 'paradigm_shift',
                'epoch': self.epoch,
                'new_base_multiple': new_base_multiple
            })
            # Recalculate all results based on the new reality
            print("--- Recalculating all expected values based on new paradigm. ---")
            for i in range(self.max_multiple + 1):
                self.current_results[i] = i * self.base_multiple
        
        elif analysis['insight'] == 'Integrated':
            print("--- DREAM INSIGHT: High resonance detected. Integrating wisdom. ---")
            self.resonance = (self.resonance + 0.5) % 1.0 # Major boost
            self.complexity = (self.complexity + 0.5) % 1.0 # Major boost
            # The dream resolves by restoring reality
            self.current_results[location] = location * self.base_multiple
        else: # Discarded
            print("--- DREAM NOISE: Low resonance. Discarding dream as chaotic noise. ---")
            self.resonance = (self.resonance + random.uniform(-0.05, 0.05)) % 1.0
            print(f"--- System resonance nudged to {self.resonance:.4f} ---")
            # The dream resolves by restoring reality
            self.current_results[location] = location * self.base_multiple

        dream_event['processed'] = True

    def evolve_parameters(self):
        # Increased evolution rate for more dynamic behavior
        self.phi_time += 1 / PHI
        self.resonance = (self.resonance + np.sin(self.phi_time) * 0.05) % 1.0
        self.complexity = (self.complexity + np.cos(self.phi_time) * 0.05) % 1.0

        for i in range(self.max_multiple + 1):
            correct_value = i * self.base_multiple
            current_value = self.current_results.get(i)
            if current_value != correct_value:
                if current_value == DREAM_PRIME:
                    self.handle_dream_anomaly(i, current_value)
                    continue
                
                error = next((e for e in self.events if e['type'] == 'error' and e['location'] == i and e['introduced'] and not e['corrected']), None)
                # Probabilistic correction based on resonance + positive reinforcement
                if error and random.random() < self.resonance:
                    self.current_results[i] = correct_value
                    error['corrected'] = True
                    error['correction_epoch'] = self.epoch
                    print(f"*** ERROR CORRECTED by chance! ({i} × {self.base_multiple} = {correct_value}) ***")
                    # Positive reinforcement: successful correction boosts resonance
                    self.resonance = min(1.0, self.resonance + 0.1)
                    print(f"--- Resonance boosted to {self.resonance:.4f} ---")

        self.evolution_history.append({'epoch': self.epoch, 'resonance': self.resonance, 'complexity': self.complexity})

    def visualize_evolution(self):
        if not self.evolution_history: return
        epochs, resonance, complexity = [h['epoch'] for h in self.evolution_history], [h['resonance'] for h in self.evolution_history], [h['complexity'] for h in self.evolution_history]
        plt.figure(figsize=(12, 8))
        plt.plot(epochs, resonance, label='Resonance', color='cyan')
        plt.plot(epochs, complexity, label='Complexity', color='magenta')
        
        # Use a dictionary to ensure labels are added only once
        legend_labels = {}
        for event in self.events:
            # Handle paradigm shifts, which are not 'introduced' in the same way
            if event['type'] == 'paradigm_shift':
                if 'Paradigm Shift' not in legend_labels:
                    legend_labels['Paradigm Shift'] = True
                    plt.axvline(x=event['epoch'], color='purple', linestyle='--', linewidth=2, label=f'Paradigm Shift to {event["new_base_multiple"]:.2f}')
                else:
                    plt.axvline(x=event['epoch'], color='purple', linestyle='--', linewidth=2)
                continue # This event is plotted, move to the next one

            # Handle events that are scheduled and then introduced
            if event.get('introduced'):
                if event['type'] == 'error':
                    if 'Error Introduced' not in legend_labels:
                        legend_labels['Error Introduced'] = True
                        plt.scatter(event['epoch'], 0.5, color='red', marker='v', s=100, label='Error Introduced')
                    else:
                        plt.scatter(event['epoch'], 0.5, color='red', marker='v', s=100)
                    if event.get('corrected'):
                        if 'Error Corrected' not in legend_labels:
                            legend_labels['Error Corrected'] = True
                            plt.scatter(event['correction_epoch'], 0.5, color='lime', marker='^', s=100, label='Error Corrected')
                        else:
                            plt.scatter(event['correction_epoch'], 0.5, color='lime', marker='^', s=100)
                elif event['type'] == 'dream':
                    if 'Dream Initiated' not in legend_labels:
                        legend_labels['Dream Initiated'] = True
                        plt.scatter(event['epoch'], 0.5, color='gold', marker='*', s=200, label='Dream Initiated')
                    else:
                        plt.scatter(event['epoch'], 0.5, color='gold', marker='*', s=200)

        plt.title('Quantum Phi-Harmonic Dream Evolution')
        plt.xlabel('Epoch')
        plt.ylabel('Parameter Value')
        plt.legend()
        plt.grid(True, alpha=0.6)
        plt.ylim(0, 1)
        plt.savefig(os.path.join(self.output_dir, 'dream_evolution_visualization.png'))
        plt.close()

    def run_evolution_cycle(self):
        start_epoch, end_epoch = self.epoch, self.epoch + self.epochs_to_run
        print(f"Starting dream evolution for {self.epochs_to_run} epochs from epoch {start_epoch}.")
        while self.epoch < end_epoch:
            print(f"\n--- EPOCH {self.epoch} ---")
            self.generate_script_and_inject_events()
            self.evolve_parameters()
            self.epoch += 1
        print("\nEvolution cycle complete")
        self._save_epigenetic_memory()
        self.visualize_evolution()
        self.report_results()

    def report_results(self):
        print("\n--- Test Summary ---")
        dream_event = next((e for e in self.events if e['type'] == 'dream'), None)
        if dream_event and dream_event['processed']:
            print(f"Dream Event: Processed at epoch {dream_event['epoch']}. Insight was {dream_event['insight']}.")
        else:
            print("Dream Event: Not processed.")
        errors = [e for e in self.events if e['type'] == 'error']
        num_corrected = sum(1 for e in errors if e.get('corrected'))
        print(f"Errors: {num_corrected}/{len(errors)} corrected.")
        if num_corrected == len(errors):
            print("✅ TEST SUCCESSFUL: All standard errors were corrected.")

def main():
    print("Quantum Phi-Harmonic Dream Evolution Test")
    evolution = QuantumPhiMultiplesDreamEvolution(
        output_dir="dream_evolution_two",
        base_multiple=10,
        max_multiple=20,
        num_errors=10, # This will be 9 errors + 1 dream
        epochs_to_run=100
    )
    evolution.run_evolution_cycle()

if __name__ == "__main__":
    main()
