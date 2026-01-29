#!/usr/bin/env python3
"""
USER INTERACTION AGENT WITH CONFIG
==================================
Updated modular agent using the new phi_resonance_integrator_with_config and api_config for better API handling.
Imports existing components without modification.

Author: Cascade AI
Date: April 26, 2025
"""
import sys
from phi_harmonic_orchestrator import PhiHarmonicOrchestrator  # Existing import
from phi_resonance_integrator_with_config import PhiResonanceIntegrator  # New integrator
import api_config  # Import config

import math

PHI = (1 + math.sqrt(5)) / 2  # Golden ratio

class UserInteractionAgent:
    def __init__(self):
        self.orchestrator = PhiHarmonicOrchestrator()
        self.integrator = None
    
    def start(self):
        print("Welcome to the Quantum Phi-Harmonic System Agent with Config. Commands: validate <structure> or exit.")
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
            # Use configurable endpoint, e.g., 'black_hole_data' from api_config
            result = self.integrator.run_validation(structure_type, endpoint_key='black_hole_data', params={'count': 1})
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
