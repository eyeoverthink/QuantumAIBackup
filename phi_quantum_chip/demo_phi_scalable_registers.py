"""
Demo: Scalable Quantum Registers with Phi-Harmonic Architecture
==============================================================
Demonstrates modular, scalable quantum register simulation using phi-harmonic scaling, resonance, and dynamic power allocation.

- Instantiates a set of quantum registers
- Allocates resources using phi-harmonic scaling
- Computes resonance metrics for each register
- Simulates dynamic power allocation up to 90 GW
- Prints results for inspection

Requires: phi_scalable_utils.py in the same directory.
"""
from phi_scalable_utils import (
    PHI, fibonacci_sequence, phi_harmonic_scale, quantum_resonance, combined_resonance, dynamic_power_allocation
)

class QuantumRegister:
    def __init__(self, id, base_load):
        self.id = id
        self.base_load = base_load
        self.scaled_load = phi_harmonic_scale(base_load)
        self.resonance = quantum_resonance(self.scaled_load)
        self.combined_resonance = combined_resonance(self.scaled_load)
        self.allocated_power = dynamic_power_allocation(self.combined_resonance)

    def summary(self):
        return {
            'id': self.id,
            'base_load': self.base_load,
            'scaled_load': self.scaled_load,
            'resonance': self.resonance,
            'combined_resonance': self.combined_resonance,
            'allocated_power_GW': self.allocated_power,
        }

def run_demo(n_registers=8):
    print("--- Scalable Quantum Register Demo ---")
    fib_loads = fibonacci_sequence(n_registers+2)[2:]  # skip 0,1 for more interesting loads
    registers = [QuantumRegister(i, load) for i, load in enumerate(fib_loads)]
    for reg in registers:
        print(f"Register {reg.id}: {reg.summary()}")
    total_power = sum(r.allocated_power for r in registers)
    print(f"\nTotal simulated allocated power: {total_power:.2f} GW (max per register: 90 GW)")

if __name__ == "__main__":
    run_demo()
