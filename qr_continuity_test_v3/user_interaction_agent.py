#!/usr/bin/env python3
"""
USER INTERACTION AGENT
=====================
A modular agent that serves as the main interface for users to interact with the Quantum Phi-Harmonic System. It allows speaking and interacting by providing a CLI for commands like running validations, based on golden ratio and quantum principles.

This component imports and coordinates with other 'lego' parts (e.g., Phi-Harmonic Orchestrator and Phi-Resonance Integrator) without modification.

Author: Cascade AI
Date: April 26, 2025
φ^75 Validation Seal: 4721424167835397.0
"""
import sys
from phi_harmonic_orchestrator import PhiHarmonicOrchestrator  # Import existing orchestrator
from phi_resonance_integrator import PhiResonanceIntegrator  # Import integrator

import math

PHI = (1 + math.sqrt(5)) / 2  # Golden ratio for UI flow control

class UserInteractionAgent:
    def __init__(self):
        self.orchestrator = PhiHarmonicOrchestrator()  # Initialize orchestrator
        self.integrator = None  # Will be set when API key is provided
    
    def start(self):
        print("Welcome to the Quantum Phi-Harmonic System Agent. Commands: validate <structure> or exit.")
        while True:
            command = input("Enter command: ").strip().lower()
            if command == 'exit':
                print("Exiting agent.")
                break
            elif command.startswith('validate '):
                structure = command.split(' ', 1)[1]
                self.run_validation(structure)
            else:
                print(f"Invalid command. Try 'validate <structure>' e.g., 'validate black_hole'.")
    
    def run_validation(self, structure_type: str):
        if not self.integrator:
            api_key = input("Enter NASA API key: ")
            self.integrator = PhiResonanceIntegrator(api_key=api_key)
        try:
            result = self.integrator.run_validation(structure_type, endpoint='/planetary/apod', params={'count': 1})
            if 'error' in result:
                print(f"Error: {result['error']}")
            else:
                print(f"Validation for {structure_type}: Alignment {result.get('alignment_percentage', 'N/A')} %")
        except Exception as e:
            print(f"Validation failed: {str(e)}")

# Example usage
if __name__ == "__main__":
    agent = UserInteractionAgent()
    agent.start()
