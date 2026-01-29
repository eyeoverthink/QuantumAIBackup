import os
import json
import random
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext

# --- Constants and Setup ---
getcontext().prec = 50
PHI = Decimal('1.618033988749895')
PHI_INVERSE = Decimal('0.618033988749895')  # Inverse golden ratio

class QuantumPhiMultiplesDreamEvolution:
    """
    A refactored engine for the Quantum Phi-Harmonic Dream Evolution system.
    This version is designed to be controlled by a component wrapper, reporting its state
    via a callback function instead of direct output.
    """
    def __init__(self, output_dir="dream_evolution_one", base_multiple=10, max_multiple=100, num_errors=9, epochs_to_run=100):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

        self.base_multiple = base_multiple
        self.max_multiple = max_multiple
        self.num_errors = num_errors
        self.epochs_to_run = epochs_to_run
        
        self.epoch = 1
        self.resonance = 0.5
        self.complexity = 0.5
        self.mutation_rate = 0.1
        self.phi_time = 0.0
        self.current_results = {i: i * self.base_multiple for i in range(self.max_multiple + 1)}
        self.events = []
        self.evolution_history = []
        self.log_messages = []
        self.errors_corrected_in_cycle = 0
        self.errors_introduced_in_cycle = 0
        self.dream_processed_in_cycle = False

        self._load_epigenetic_memory()
        self._schedule_events()

    def _log(self, message):
        self.log_messages.append(f"Epoch {self.epoch}: {message}")

    def _load_epigenetic_memory(self):
        memory_file = os.path.join(self.output_dir, 'epigenetic_memory.json')
        if os.path.exists(memory_file):
            with open(memory_file, 'r') as f:
                memory = json.load(f)
                self.epoch = memory.get('epoch', 1)
                self.resonance = memory.get('resonance', 0.5)
                self.complexity = memory.get('complexity', 0.5)
                self.mutation_rate = memory.get('mutation_rate', 0.1)
                self._log(f"Loaded epigenetic memory from epoch {self.epoch}")
        else:
            self._log("No epigenetic memory found. Starting fresh.")

    def _save_epigenetic_memory(self):
        memory = {
            'epoch': self.epoch,
            'resonance': self.resonance,
            'complexity': self.complexity,
            'mutation_rate': self.mutation_rate
        }
        with open(os.path.join(self.output_dir, 'epigenetic_memory.json'), 'w') as f:
            json.dump(memory, f, indent=4)

    def _schedule_events(self):
        self.events = []
        # Schedule errors
        error_epochs = random.sample(range(self.epoch, self.epoch + self.epochs_to_run), self.num_errors)
        for epoch in error_epochs:
            self.events.append({'type': 'error', 'epoch': epoch})
        # Schedule one dream
        dream_epoch = random.randint(self.epoch, self.epoch + self.epochs_to_run -1)
        self.events.append({'type': 'dream', 'epoch': dream_epoch})
        self.events.sort(key=lambda x: x['epoch'])
        self._log(f"Scheduled {self.num_errors} errors and 1 dream.")

    def _handle_event(self, event):
        if event['type'] == 'error':
            self.errors_introduced_in_cycle += 1
            location = random.randint(0, self.max_multiple)
            correct_value = location * self.base_multiple
            error_value = correct_value + random.randint(-5, 5)
            while error_value == correct_value:
                error_value = correct_value + random.randint(-5, 5)
            self.current_results[location] = error_value
            self._log(f"*** ERROR INTRODUCED: {location} * {self.base_multiple} = {error_value} (should be {correct_value}) ***")

        elif event['type'] == 'dream':
            self.dream_processed_in_cycle = True
            location = random.randint(0, self.max_multiple)
            anomaly_value = 7919  # Prime number anomaly
            phi_resonance = (PHI * anomaly_value) % 1
            self._log(f">>> AI DREAM INITIATED at location {location}. Anomaly value: {anomaly_value} <<<")
            self._log(f"--- DREAM ANALYSIS: Anomaly {anomaly_value} has Phi-Resonance of {phi_resonance:.4f} ---")
            if phi_resonance > 0.9:
                self._log("--- DREAM INSIGHT: High resonance. Integrating wisdom. ---")
                self.resonance = min(1.0, self.resonance + 0.2)
            else:
                self._log("--- DREAM NOISE: Low resonance. Discarding dream as chaotic noise. ---")
                self.resonance = max(0.0, self.resonance - 0.1 * (1.0 - float(phi_resonance)))

    def _evolve_parameters(self):
        self.phi_time += float(PHI_INVERSE)
        self.complexity = (self.complexity + np.sin(self.phi_time) * 0.01) % 1.0
        self.mutation_rate = max(0.01, min(0.5, self.mutation_rate + (0.5 - self.resonance) * 0.001))

    def _self_correct(self):
        for i in range(self.max_multiple + 1):
            correct_value = i * self.base_multiple
            if self.current_results[i] != correct_value:
                if random.random() < self.resonance:
                    self.current_results[i] = correct_value
                    self.resonance = min(1.0, self.resonance + 0.1)
                    self.errors_corrected_in_cycle += 1
                    self._log(f"*** ERROR CORRECTED by resonance! ({i} * {self.base_multiple} = {correct_value}) --- Resonance boosted to {self.resonance:.4f} ***")

    def get_state(self):
        return {
            'epoch': self.epoch,
            'resonance': self.resonance,
            'complexity': self.complexity,
            'mutation_rate': self.mutation_rate,
            'phi_time': self.phi_time,
            'errors_in_cycle': self.errors_introduced_in_cycle,
            'corrections_in_cycle': self.errors_corrected_in_cycle,
            'dream_in_cycle': self.dream_processed_in_cycle,
            'log_messages': self.log_messages
        }

    def run(self, callback=None):
        start_epoch = self.epoch
        while self.epoch < start_epoch + self.epochs_to_run:
            self.log_messages = []
            self.errors_introduced_in_cycle = 0
            self.errors_corrected_in_cycle = 0
            self.dream_processed_in_cycle = False

            # Handle scheduled events for the current epoch
            for event in self.events:
                if event['epoch'] == self.epoch:
                    self._handle_event(event)
            
            self._self_correct()
            self._evolve_parameters()

            self.evolution_history.append({
                'epoch': self.epoch,
                'resonance': self.resonance,
                'complexity': self.complexity,
                'mutation_rate': self.mutation_rate
            })

            if callback:
                callback(self.get_state())

            self.epoch += 1
        
        self._save_epigenetic_memory()
        self._log("Evolution cycle complete.")
        if callback:
            callback(self.get_state())
