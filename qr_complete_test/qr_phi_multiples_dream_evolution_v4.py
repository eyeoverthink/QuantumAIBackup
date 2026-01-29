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

class QrPhiMultiplesDreamEvolutionV4:
    """A system that evolves multiples, with the ability to process
    a series of 'AI Dreams'—impossible anomalies—using phi-harmonic principles.
    V4: Handles multiple dream events in a single run to test memory and adaptation.
    """
    def __init__(self, output_dir="dream_evolution_four", base_multiple=10, max_multiple=100, num_errors_per_cycle=10, epochs_per_cycle=100, num_dreams=1):
        """Initialize the dream evolution system."""
        self.output_dir = output_dir
        self.base_multiple = base_multiple
        self.max_multiple = max_multiple
        self.num_errors_per_cycle = num_errors_per_cycle
        self.epochs_per_cycle = epochs_per_cycle
        self.num_dreams = num_dreams
        self.total_epochs = self.epochs_per_cycle * self.num_dreams
        self.dream_integrator = DreamIntegrator()

        os.makedirs(self.output_dir, exist_ok=True)

        # Default initial state
        self.epoch = 1
        self.resonance = 0.5
        self.current_results = {}
        self.expected_results = {}
        self.history = []
        self.events = []
        self.load_epigenetic_memory()
        self.reset_state()

    def load_epigenetic_memory(self):
        """Load the last known state from a file."""
        memory_file = os.path.join(self.output_dir, 'epigenetic_memory.json')
        if os.path.exists(memory_file):
            with open(memory_file, 'r') as f:
                memory = json.load(f)
                self.epoch = memory.get('epoch', 1)
                self.base_multiple = memory.get('base_multiple', self.base_multiple)
                self.resonance = memory.get('resonance', 0.5)
                print(f"Loaded epigenetic memory from epoch {self.epoch}")

    def save_epigenetic_memory(self):
        """Save the current state to a file."""
        memory_file = os.path.join(self.output_dir, 'epigenetic_memory.json')
        memory = {
            'epoch': self.epoch,
            'base_multiple': self.base_multiple,
            'resonance': self.resonance,
            'timestamp': time.time()
        }
        with open(memory_file, 'w') as f:
            json.dump(memory, f, indent=4)

    def reset_state(self):
        """Reset the system state for a new test run."""
        print("Base multiple set. Resetting state.")
        self.current_results = {i: i * self.base_multiple for i in range(self.max_multiple)}
        self.expected_results = self.current_results.copy()
        self.history = []
        self.events = []
        self.schedule_events()

    def schedule_events(self):
        """Schedule errors and dream events for the upcoming epochs."""
        self.events = []
        print(f"Initiating new test run: Scheduling {self.num_dreams} dreams and {self.num_errors_per_cycle * self.num_dreams} total errors over {self.total_epochs} epochs.")

        for i in range(self.num_dreams):
            cycle_start_epoch = self.epoch + (i * self.epochs_per_cycle)
            cycle_end_epoch = cycle_start_epoch + self.epochs_per_cycle

            # Schedule one dream event per cycle
            dream_epoch = random.randint(cycle_start_epoch + 5, cycle_end_epoch - 5)
            self.events.append({'type': 'dream', 'epoch': dream_epoch, 'processed': False, 'location': random.randint(0, self.max_multiple - 1)})
            print(f"Scheduled dream #{i+1} at epoch: {dream_epoch}")

            # Schedule errors for this cycle
            error_epochs = sorted(random.sample(range(cycle_start_epoch, cycle_end_epoch), self.num_errors_per_cycle))
            for epoch in error_epochs:
                self.events.append({'type': 'error', 'epoch': epoch, 'processed': False, 'location': random.randint(0, self.max_multiple - 1)})
        
        all_error_epochs = sorted([e['epoch'] for e in self.events if e['type'] == 'error'])
        print(f"Scheduled error epochs (first 20): {all_error_epochs[:20]}")


    def introduce_error(self, location):
        """Introduce a random error into the system."""
        error_value = self.current_results[location] + (random.random() - 0.5) * (self.base_multiple / 5 if self.base_multiple > 0 else 1)
        self.current_results[location] = error_value
        print(f"*** ERROR INTRODUCED: {location} × {self.base_multiple:.4f} = {error_value:.4f} (should be {self.expected_results[location]:.4f}) ***")
        return error_value

    def correct_error(self, location):
        """Attempt to correct an error through resonance."""
        if random.random() < self.resonance:
            self.current_results[location] = self.expected_results[location]
            print(f"*** ERROR CORRECTED by chance! ({location} × {self.base_multiple:.4f} = {self.expected_results[location]:.4f}) ***")
            self.resonance = min(1.0, self.resonance + 0.1)
            print(f"--- Resonance boosted to {self.resonance:.4f} ---")
            return True
        return False

    def handle_dream_anomaly(self, location, anomaly_value):
        """Process a dream anomaly using the DreamIntegrator."""
        dream_event = next((e for e in self.events if e['epoch'] == self.epoch and e['type'] == 'dream' and not e['processed']), None)
        if not dream_event: return

        analysis = self.dream_integrator.analyze_dream(anomaly_value, location, self.base_multiple)
        resonance = analysis['resonance']
        dream_event['insight'] = analysis['insight']

        print(f"--- DREAM ANALYSIS: Anomaly {anomaly_value} has Phi-Resonance of {resonance:.4f} ---")

        if analysis['insight'] == 'Paradigm Shift':
            print("\n*** PARADIGM SHIFT: High-resonance dream suggests a new reality. ***")
            new_base_multiple = analysis['new_base_multiple']
            print(f"--- Changing base multiple from {self.base_multiple:.4f} to {new_base_multiple:.4f} ---")
            self.base_multiple = new_base_multiple
            self.expected_results = {i: i * self.base_multiple for i in range(self.max_multiple)}
            self.current_results = self.expected_results.copy()
            self.resonance = 0.5 # Reset resonance after paradigm shift
            print("--- Recalculating all expected values based on new paradigm. ---\n")
        elif analysis['insight'] == 'Integrated':
            print("--- DREAM INTEGRATED: System adapted to include the dream's insight. ---")
            self.current_results[location] = anomaly_value
            self.expected_results[location] = anomaly_value
            self.resonance = min(1.0, self.resonance + 0.2)
            print(f"--- Resonance boosted to {self.resonance:.4f} ---")
        else: # Discarded or Corrected
            if self.resonance > 0.75:
                print("--- DREAM CORRECTION: High system resonance allows correction of chaotic dream. ---")
                self.current_results[location] = self.expected_results[location] # Correct back to expected reality
                dream_event['insight'] = 'Corrected'
                self.resonance = min(1.0, self.resonance + 0.05)
                print(f"--- Resonance boosted to {self.resonance:.4f} ---")
            else:
                print("--- DREAM NOISE: Low resonance. Discarding dream as chaotic noise. ---")
                self.resonance = max(0, self.resonance + random.uniform(-0.1, 0.05))
                print(f"--- System resonance nudged to {self.resonance:.4f} ---")

        dream_event['processed'] = True

        # Log the event for the orchestrator
        self.event_log.append({
            'timestamp': time.time(),
            'type': 'dream_analysis',
            'location': location,
            'anomaly_value': anomaly_value,
            'insight': analysis.get('insight', 'N/A'),
            'resonance': analysis.get('resonance', 0)
        })

    def run_simulation(self):
        """Run the full evolution simulation."""
        start_epoch = self.epoch
        end_epoch = self.epoch + self.total_epochs
        print(f"Starting dream evolution V4 for {self.total_epochs} epochs from epoch {start_epoch}.")

        unresolved_errors = {}

        for epoch in range(start_epoch, end_epoch):
            self.epoch = epoch
            print(f"\n--- EPOCH {epoch} ---")

            # Process scheduled events
            for event in self.events:
                if event['epoch'] == epoch and not event['processed']:
                    if event['type'] == 'dream':
                        anomaly_value = DREAM_PRIME
                        print(f"\n>>> AI DREAM INITIATED at location {event['location']}. Anomaly value: {anomaly_value} <<<")
                        self.handle_dream_anomaly(event['location'], anomaly_value)
                    elif event['type'] == 'error':
                        error_val = self.introduce_error(event['location'])
                        unresolved_errors[event['location']] = error_val
                        event['processed'] = True

            # Attempt to correct unresolved errors
            for loc in list(unresolved_errors.keys()):
                if self.correct_error(loc):
                    del unresolved_errors[loc]

            # Record history
            self.history.append({
                'epoch': epoch,
                'resonance': self.resonance,
                'base_multiple': self.base_multiple,
                'num_unresolved_errors': len(unresolved_errors)
            })

        self.save_epigenetic_memory()
        print("\nEvolution cycle complete")
        self.summarize_run(unresolved_errors)

    def summarize_run(self, unresolved_errors):
        """Print a summary of the simulation run."""
        print("\n--- Test Summary --- ailments")
        processed_dreams = [e for e in self.events if e['type'] == 'dream' and e['processed']]
        print(f"Dream Events: {len(processed_dreams)}/{self.num_dreams} processed.")
        for i, dream_event in enumerate(processed_dreams):
            print(f"  - Dream #{i+1}: Processed at epoch {dream_event['epoch']}. Insight was {dream_event.get('insight', 'N/A')}.")

        total_errors = self.num_errors_per_cycle * self.num_dreams
        corrected_errors = total_errors - len(unresolved_errors)
        print(f"Errors: {corrected_errors}/{total_errors} corrected.")

        if corrected_errors >= total_errors:
            print("✅ TEST SUCCESSFUL: All standard errors were corrected.")

    def visualize_evolution(self):
        """Generate visualizations of the evolution."""
        if not self.history:
            print("No history to visualize.")
            return

        epochs = [h['epoch'] for h in self.history]
        resonance = [h['resonance'] for h in self.history]
        base_multiples = [h['base_multiple'] for h in self.history]

        fig, ax1 = plt.subplots(figsize=(18, 9))

        # Plot Resonance
        color = 'tab:blue'
        ax1.set_xlabel('Epoch')
        ax1.set_ylabel('Resonance', color=color)
        ax1.plot(epochs, resonance, color=color, label='Resonance', alpha=0.8)
        ax1.tick_params(axis='y', labelcolor=color)
        ax1.set_ylim(0, 1.1)

        # Plot Base Multiple on a secondary y-axis
        ax2 = ax1.twinx()
        color = 'tab:red'
        ax2.set_ylabel('Base Multiple', color=color)
        ax2.plot(epochs, base_multiples, color=color, label='Base Multiple', linestyle='--', marker='o', markersize=2)
        ax2.tick_params(axis='y', labelcolor=color)

        # Add markers for events
        dream_labels = set()
        for event in self.events:
            if event['processed'] and event['type'] == 'dream':
                insight = event.get('insight', 'N/A')
                label = f"Dream ({insight})"
                if label not in dream_labels:
                    ax1.axvline(x=event['epoch'], color='gold', linestyle=':', linewidth=2, label=label)
                    dream_labels.add(label)
                else:
                    ax1.axvline(x=event['epoch'], color='gold', linestyle=':', linewidth=2)

        # Create a legend for the event markers
        handles, labels = ax1.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))

        # Record history
        self.history.append({
            'epoch': epoch,
            'resonance': self.resonance,
            'base_multiple': self.base_multiple,
            'num_unresolved_errors': len(unresolved_errors)
        })

    self._save_json_log()
    self.save_epigenetic_memory()
    print("\nEvolution cycle complete")
    self.summarize_run(unresolved_errors)

def _save_json_log(self):
    """Saves the event log to a JSON file for the orchestrator."""
    self.json_log_path = os.path.join(self.output_dir, 'dream_log.json')
    try:
        with open(self.json_log_path, 'w') as f:
            json.dump(self.event_log, f, indent=4)
        print(f"\n[+] Saved dream log for orchestrator to: {self.json_log_path}")
    except Exception as e:
        print(f"Error saving JSON log: {e}")

def summarize_run(self, unresolved_errors):
    """Print a summary of the simulation run."""
    print("\n--- Test Summary --- ailments")
    processed_dreams = [e for e in self.events if e['type'] == 'dream' and e['processed']]
    print(f"Dream Events: {len(processed_dreams)}/{self.num_dreams} processed.")
    for i, dream_event in enumerate(processed_dreams):
        print(f"  - Dream #{i+1}: Processed at epoch {dream_event['epoch']}. Insight was {dream_event.get('insight', 'N/A')}.")

    total_errors = self.num_errors_per_cycle * self.num_dreams
    corrected_errors = total_errors - len(unresolved_errors)
    print(f"Errors: {corrected_errors}/{total_errors} corrected.")

    if corrected_errors >= total_errors:
        print("✅ TEST SUCCESSFUL: All standard errors were corrected.")

def visualize_evolution(self):
    """Generate visualizations of the evolution."""
    if not self.history:
        print("No history to visualize.")
        return

    epochs = [h['epoch'] for h in self.history]
    resonance = [h['resonance'] for h in self.history]
    base_multiples = [h['base_multiple'] for h in self.history]

    fig, ax1 = plt.subplots(figsize=(18, 9))

    # Plot Resonance
    color = 'tab:blue'
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Resonance', color=color)
    ax1.plot(epochs, resonance, color=color, label='Resonance', alpha=0.8)
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_ylim(0, 1.1)

    # Plot Base Multiple on a secondary y-axis
    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('Base Multiple', color=color)
    ax2.plot(epochs, base_multiples, color=color, label='Base Multiple', linestyle='--', marker='o', markersize=2)
    ax2.tick_params(axis='y', labelcolor=color)

    # Add markers for events
    dream_labels = set()
    for event in self.events:
        if event['processed'] and event['type'] == 'dream':
            insight = event.get('insight', 'N/A')
            label = f"Dream ({insight})"
            if label not in dream_labels:
                ax1.axvline(x=event['epoch'], color='gold', linestyle=':', linewidth=2, label=label)
                dream_labels.add(label)
            else:
                ax1.axvline(x=event['epoch'], color='gold', linestyle=':', linewidth=2)

    # Create a legend for the event markers
    handles, labels = ax1.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax1.legend(by_label.values(), by_label.keys(), loc='upper left')

    fig.tight_layout()
    plt.title('Quantum Dream Evolution V4: Resonance and Paradigm Shifts')
    
    plot_path = os.path.join(self.output_dir, f'evolution_plot_v4_epoch_{self.epoch}.png')
    plt.savefig(plot_path)
    plt.close()
    print(f"Saved evolution plot to {plot_path}")

def main():
    print("Quantum Phi-Harmonic Dream Evolution Test V4")
    evolution = QrPhiMultiplesDreamEvolutionV4(
        output_dir="dream_evolution_four",
        base_multiple=10,
        max_multiple=20,
        num_errors_per_cycle=5,
        epochs_per_cycle=100,
        num_dreams=5
    )
    evolution.run_simulation()
    evolution.visualize_evolution()

if __name__ == "__main__":
    main()
