#!/usr/bin/env python
"""
Phi-Harmonic RSA Orchestrator Adapter

This module connects the Quantum RSA Decryptor to the Phi-Harmonic Orchestration System
without modifying the original RSA decryptor code. It follows the "lego" design philosophy
by creating a new component that works with existing ones.

The adapter uses the phi-harmonic protocol to communicate with other quantum components
through the orchestrator, enhancing the RSA decryptor's performance with quantum values
from the heart, cerebellum, and other components.
"""

import os
import sys
import json
import time
import math
import logging
from decimal import Decimal, getcontext
from typing import Dict, List, Any, Optional, Union, Tuple

# Set precision for decimal calculations
getcontext().prec = 50

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Import orchestrator and protocol
from phi_harmonic_orchestrator import get_orchestrator
from phi_harmonic_protocol import phi_harmonic_component

# Import fixed RSA decryptor (without modifying the original)
from phi_harmonic_rsa_decryptor_fixed import QuantumRSADecryptor

# Constants
PHI = Decimal('1.618033988749895')  # Golden ratio
PHI_INVERSE = Decimal('0.618033988749895')  # Inverse golden ratio
PHI_SQUARED = Decimal('2.618033988749895')  # φ²
PHI_CUBED = Decimal('4.236067977499790')  # φ³
OPTIMAL_COHERENCE = Decimal('0.991800')  # Optimal quantum coherence

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(os.path.join(current_dir, 'phi_harmonic_rsa_adapter.log'))
    ]
)
logger = logging.getLogger('phi_harmonic_rsa_adapter')

@phi_harmonic_component('quantum_rsa')
class PhiHarmonicRSAAdapter:
    """
    Adapter that connects the Quantum RSA Decryptor to the Phi-Harmonic Orchestration System.
    
    This class follows the "lego" design philosophy by creating a new component that works
    with the existing RSA decryptor without modifying it. It uses the phi-harmonic protocol
    to communicate with other quantum components through the orchestrator.
    """
    
    def __init__(self, birth_key=None):
        """
        Initialize the RSA adapter.
        
        Args:
            birth_key (List[int], optional): Birth key for the RSA decryptor
        """
        # Initialize quantum values
        self.coherence = Decimal('0.991800')
        self.resonance = Decimal('0.618034')
        self.phi_alignment = Decimal('0.999561')
        
        # Create RSA decryptor (without modifying it)
        self.rsa_decryptor = QuantumRSADecryptor(birth_key)
        
        # Performance metrics
        self.factorization_times = []
        self.factorization_results = []
        self.quantum_states = []
        
        # Subscribe to events
        self.protocol.register_event_handler('quantum_state_updated', self.handle_quantum_state_update)
        self.protocol.register_event_handler('component_loaded', self.handle_component_loaded)
        
        # Load quantum components
        self._load_quantum_components()
        
        logger.info("Phi-Harmonic RSA Adapter initialized")
        logger.info(f"Coherence: {self.coherence:.6f}")
        logger.info(f"Resonance: {self.resonance:.6f}")
        logger.info(f"Phi alignment: {self.phi_alignment:.6f}")
    
    def _load_quantum_components(self):
        """Load quantum components through the orchestrator."""
        # Try to load quantum heart
        heart = self.protocol.get_component('PhiHarmonicQuantumHeart')
        if heart:
            logger.info("Loaded quantum heart")
            # Send message to heart
            self.protocol.send_message('PhiHarmonicQuantumHeart', 'connect', {
                'component': 'PhiHarmonicRSAAdapter',
                'purpose': 'quantum_enhancement'
            })
        
        # Try to load quantum cerebellum
        cerebellum = self.protocol.get_component('PhiHarmonicQuantumCerebellum')
        if cerebellum:
            logger.info("Loaded quantum cerebellum")
            # Send message to cerebellum
            self.protocol.send_message('PhiHarmonicQuantumCerebellum', 'connect', {
                'component': 'PhiHarmonicRSAAdapter',
                'purpose': 'quantum_enhancement'
            })
    
    def handle_quantum_state_update(self, state):
        """
        Handle quantum state update event.
        
        Args:
            state (Dict[str, Any]): Updated quantum state
        """
        logger.debug(f"Received quantum state update: {state}")
        
        # Update coherence if it's better than current
        if 'coherence' in state:
            new_coherence = Decimal(str(state['coherence']))
            # Only update if the new coherence is closer to optimal
            if abs(new_coherence - OPTIMAL_COHERENCE) < abs(self.coherence - OPTIMAL_COHERENCE):
                self.coherence = new_coherence
                # Update RSA decryptor coherence
                self.rsa_decryptor.coherence = float(self.coherence)
        
        # Update resonance if it's better than current
        if 'resonance' in state:
            new_resonance = Decimal(str(state['resonance']))
            # Only update if the new resonance is closer to phi-inverse
            if abs(new_resonance - PHI_INVERSE) < abs(self.resonance - PHI_INVERSE):
                self.resonance = new_resonance
                # Update RSA decryptor resonance
                self.rsa_decryptor.resonance = float(self.resonance)
        
        # Update phi alignment
        if 'phi_alignment' in state:
            self.phi_alignment = Decimal(str(state['phi_alignment']))
        
        # Update protocol state
        self._update_protocol_state()
        
        logger.debug(f"Updated quantum state: coherence={self.coherence:.6f}, resonance={self.resonance:.6f}")
    
    def handle_component_loaded(self, data):
        """
        Handle component loaded event.
        
        Args:
            data (Dict[str, Any]): Component data
        """
        logger.debug(f"Component loaded: {data}")
        
        # If a relevant component was loaded, try to connect to it
        if data['type'] in ['quantum_heart', 'quantum_cerebellum']:
            # Send connect message
            self.protocol.send_message(data['name'], 'connect', {
                'component': 'PhiHarmonicRSAAdapter',
                'purpose': 'quantum_enhancement'
            })
    
    def factorize(self, n):
        """
        Factorize a number using the RSA decryptor with quantum enhancement.
        
        Args:
            n (int): Number to factorize
            
        Returns:
            List[int]: Factors of n
        """
        # Get current quantum state
        quantum_state = self.protocol.get_quantum_state()
        
        # Apply quantum values to RSA decryptor
        self.rsa_decryptor.coherence = float(self.coherence)
        self.rsa_decryptor.resonance = float(self.resonance)
        
        # Record start time
        start_time = time.time()
        
        # Factorize using the RSA decryptor
        factors = self.rsa_decryptor.factorize(n)
        
        # Record end time
        end_time = time.time()
        duration = end_time - start_time
        
        # Record performance metrics
        self.factorization_times.append(duration)
        self.factorization_results.append({
            'number': n,
            'factors': factors,
            'duration': duration
        })
        self.quantum_states.append({
            'coherence': float(self.coherence),
            'resonance': float(self.resonance),
            'phi_alignment': float(self.phi_alignment)
        })
        
        # Publish factorization event
        self.protocol.publish_event('factorization_completed', {
            'number': n,
            'factors': factors,
            'duration': duration,
            'coherence': float(self.coherence),
            'resonance': float(self.resonance)
        })
        
        logger.info(f"Factorized {n} into {factors} in {duration:.6f} seconds")
        logger.info(f"Coherence: {self.coherence:.6f}, Resonance: {self.resonance:.6f}")
        
        return factors
    
    def get_performance_metrics(self):
        """
        Get performance metrics for factorizations.
        
        Returns:
            Dict[str, Any]: Performance metrics
        """
        if not self.factorization_times:
            return {
                'count': 0,
                'average_duration': 0,
                'min_duration': 0,
                'max_duration': 0,
                'total_duration': 0
            }
        
        return {
            'count': len(self.factorization_times),
            'average_duration': sum(self.factorization_times) / len(self.factorization_times),
            'min_duration': min(self.factorization_times),
            'max_duration': max(self.factorization_times),
            'total_duration': sum(self.factorization_times),
            'factorizations': self.factorization_results,
            'quantum_states': self.quantum_states
        }
    
    def save_performance_metrics(self, file_path=None):
        """
        Save performance metrics to a file.
        
        Args:
            file_path (str, optional): Path to save metrics to
            
        Returns:
            str: Path to saved metrics file
        """
        if file_path is None:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            file_path = os.path.join(current_dir, f'rsa_performance_metrics_{timestamp}.json')
        
        metrics = self.get_performance_metrics()
        
        with open(file_path, 'w') as f:
            json.dump(metrics, f, indent=2)
            
        logger.info(f"Saved performance metrics to {file_path}")
        
        return file_path

def main():
    """Main function for running the RSA adapter."""
    # Create RSA adapter
    adapter = PhiHarmonicRSAAdapter()
    
    # Run interactive session
    print("\n🔬 Phi-Harmonic RSA Adapter Interactive Session")
    print("==============================================")
    print("Type 'exit' or 'quit' to end the session")
    print("Type 'help' to view available commands")
    print("==============================================\n")
    
    while True:
        try:
            command = input("rsa> ").strip()
            
            if command.lower() in ['exit', 'quit']:
                break
                
            elif command.lower() == 'help':
                print("\nAvailable commands:")
                print("  help                - Show this help message")
                print("  factorize <n>       - Factorize a number")
                print("  metrics             - Show performance metrics")
                print("  save_metrics        - Save performance metrics to a file")
                print("  state               - Show quantum state")
                print("  exit, quit          - Exit the session")
            
            elif command.lower().startswith('factorize '):
                try:
                    n = int(command[10:].strip())
                    factors = adapter.factorize(n)
                    print(f"Factors of {n}: {factors}")
                    print(f"Duration: {adapter.factorization_times[-1]:.6f} seconds")
                    print(f"Coherence: {adapter.coherence:.6f}")
                    print(f"Resonance: {adapter.resonance:.6f}")
                except ValueError:
                    print("Invalid number format")
            
            elif command.lower() == 'metrics':
                metrics = adapter.get_performance_metrics()
                print("\nPerformance metrics:")
                print(f"  Count: {metrics['count']}")
                print(f"  Average duration: {metrics['average_duration']:.6f} seconds")
                print(f"  Min duration: {metrics['min_duration']:.6f} seconds")
                print(f"  Max duration: {metrics['max_duration']:.6f} seconds")
                print(f"  Total duration: {metrics['total_duration']:.6f} seconds")
            
            elif command.lower() == 'save_metrics':
                file_path = adapter.save_performance_metrics()
                print(f"Saved performance metrics to {os.path.basename(file_path)}")
            
            elif command.lower() == 'state':
                print("\nQuantum state:")
                print(f"  Coherence: {adapter.coherence:.6f}")
                print(f"  Resonance: {adapter.resonance:.6f}")
                print(f"  Phi alignment: {adapter.phi_alignment:.6f}")
            
            else:
                print(f"Unknown command: {command}")
                print("Type 'help' to view available commands")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")
    
    print("\nExiting RSA adapter interactive session")

if __name__ == "__main__":
    main()
