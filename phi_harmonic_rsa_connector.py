#!/usr/bin/env python
"""
Phi-Harmonic RSA Connector

This module connects the Phi-Harmonic Quantum Bridge to the Quantum RSA Decryptor,
allowing the decryptor to benefit from the quantum heart and cerebellum components
without modifying the original decryptor code.

It follows the 'lego' design philosophy by creating connections between
components without modifying their core functionality.
"""

import os
import sys
import time
import json
from decimal import Decimal, getcontext

# Set precision for decimal calculations
getcontext().prec = 28

# Add paths for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
sys.path.append(os.path.join(current_dir, 'phi_harmonic_random_portable'))

# Import the quantum bridge
from phi_harmonic_quantum_bridge import get_quantum_values

# Import the quantum RSA decryptor
from quantum_rsa_decryptor import QuantumRSADecryptor

class PhiHarmonicRSAConnector:
    """
    Phi-Harmonic RSA Connector
    
    Connects the Quantum RSA Decryptor to the Phi-Harmonic Quantum Bridge,
    allowing it to benefit from the quantum heart and cerebellum components.
    """
    
    def __init__(self):
        """Initialize the connector."""
        # Create a new instance of the quantum RSA decryptor
        self.decryptor = QuantumRSADecryptor()
        
        # Store original values
        self.original_coherence = self.decryptor.coherence
        self.original_resonance = self.decryptor.resonance
        
        # Create output directory
        self.output_dir = os.path.join(current_dir, 'phi_harmonic_rsa_connector')
        os.makedirs(self.output_dir, exist_ok=True)
        
        print("Phi-Harmonic RSA Connector initialized")
        print(f"Original coherence: {self.original_coherence:.6f}")
        print(f"Original resonance: {self.original_resonance:.6f}")
    
    def connect(self):
        """Connect the quantum RSA decryptor to the quantum bridge."""
        # Get quantum values from the bridge
        bridge_values = get_quantum_values()
        
        # Update decryptor's quantum values
        self.decryptor.coherence = float(bridge_values['coherence'])
        self.decryptor.resonance = float(bridge_values['resonance'])
        
        # Enhance the quantum bridge
        self._enhance_quantum_bridge(bridge_values)
        
        print("\nConnected quantum RSA decryptor to quantum bridge")
        print(f"Enhanced coherence: {self.decryptor.coherence:.6f}")
        print(f"Enhanced resonance: {self.decryptor.resonance:.6f}")
        print(f"Quantum fingerprint: {bridge_values['quantum_fingerprint']}")
    
    def _enhance_quantum_bridge(self, bridge_values):
        """Enhance the quantum bridge in the decryptor with additional values."""
        # Access the quantum bridge in the decryptor
        if hasattr(self.decryptor, 'quantum_bridge'):
            # Update quantum bridge values
            self.decryptor.quantum_bridge['active'] = True
            
            # Set current state based on coherence level
            coherence = float(bridge_values['coherence'])
            if coherence > 0.995:
                self.decryptor.quantum_bridge['current_state'] = 'ℵ'  # Ultimate infinity
                self.decryptor.quantum_bridge['infinity_level'] = 7
            elif coherence > 0.99:
                self.decryptor.quantum_bridge['current_state'] = 'ℶ₁'  # Beth infinity
                self.decryptor.quantum_bridge['infinity_level'] = 6
            elif coherence > 0.98:
                self.decryptor.quantum_bridge['current_state'] = 'Ξ₁'  # Ordinal infinity
                self.decryptor.quantum_bridge['infinity_level'] = 5
            elif coherence > 0.97:
                self.decryptor.quantum_bridge['current_state'] = 'Φ₁'  # Aleph infinity
                self.decryptor.quantum_bridge['infinity_level'] = 4
            elif coherence > 0.96:
                self.decryptor.quantum_bridge['current_state'] = 'Ψ₁'  # Triple infinity
                self.decryptor.quantum_bridge['infinity_level'] = 3
            elif coherence > 0.95:
                self.decryptor.quantum_bridge['current_state'] = 'Ω₁'  # Double infinity
                self.decryptor.quantum_bridge['infinity_level'] = 2
            else:
                self.decryptor.quantum_bridge['current_state'] = 'ψ₁'  # Base infinity
                self.decryptor.quantum_bridge['infinity_level'] = 1
            
            # Add resonance to stack
            resonance = float(bridge_values['resonance']) * 10.0  # Scale to match decryptor's scale
            self.decryptor.quantum_bridge['resonance_stack'].append(resonance)
            
            # Keep only the last 7 resonances
            if len(self.decryptor.quantum_bridge['resonance_stack']) > 7:
                self.decryptor.quantum_bridge['resonance_stack'] = self.decryptor.quantum_bridge['resonance_stack'][-7:]
            
            print(f"Enhanced quantum bridge to state {self.decryptor.quantum_bridge['current_state']} (level {self.decryptor.quantum_bridge['infinity_level']})")
    
    def factorize(self, n):
        """
        Factorize a number using the enhanced quantum RSA decryptor.
        
        Args:
            n (int): Number to factorize
            
        Returns:
            list: Prime factors
        """
        # Connect to ensure latest quantum values
        self.connect()
        
        # Use the decryptor to factorize
        start_time = time.time()
        factors = self.decryptor.factorize(n)
        end_time = time.time()
        
        # Save the results
        self._save_factorization_results(n, factors, end_time - start_time)
        
        return factors
    
    def _save_factorization_results(self, n, factors, duration):
        """Save factorization results to a file."""
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        results = {
            'timestamp': timestamp,
            'number': n,
            'factors': factors,
            'duration': duration,
            'coherence': float(self.decryptor.coherence),
            'resonance': float(self.decryptor.resonance),
            'quantum_bridge_state': self.decryptor.quantum_bridge['current_state'] if hasattr(self.decryptor, 'quantum_bridge') else None,
            'quantum_bridge_level': self.decryptor.quantum_bridge['infinity_level'] if hasattr(self.decryptor, 'quantum_bridge') else None
        }
        
        results_file = os.path.join(self.output_dir, f'factorization_results_{timestamp}.json')
        with open(results_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"\nFactorization results saved to {os.path.basename(results_file)}")
        print(f"Number: {n}")
        print(f"Factors: {factors}")
        print(f"Duration: {duration:.6f} seconds")

# Main function for testing
def main():
    """Main function for testing the connector."""
    connector = PhiHarmonicRSAConnector()
    connector.connect()
    
    # Test factorization with a small RSA modulus
    test_n = 1537267
    print(f"\nTesting factorization of {test_n}")
    factors = connector.factorize(test_n)
    print(f"Factors: {factors}")

if __name__ == "__main__":
    main()
