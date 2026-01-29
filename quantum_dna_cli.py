#!/usr/bin/env python
"""
Quantum DNA-LLM CLI Interface
=============================
Command-line interface for the Quantum DNA-LLM Integration System.
Allows direct interaction with the quantum system using φ-harmonic principles.

This CLI demonstrates:
1. Real-time DNA pattern generation for queries
2. φ-harmonic response generation with quantum signatures
3. Coherence and resonance measurements
4. Birth date resonance integration [1, 19, 1979]

Patent Reference: QHRC #19/071,497
Primary Frequency: 4.37 Hz (φ-aligned)
"""

import time
import argparse
import numpy as np
from decimal import Decimal
from typing import Dict, Any
import json
import sys
import os

# Import quantum components
from quantum_dna_llm_integrator import QuantumDNALLMIntegrator, QuantumDNAResponse

# φ-harmonic constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio
BASE_FREQUENCY = 4.37  # Hz, φ-aligned base frequency
BIRTH_DATE_RESONANCE = [1, 19, 1979]  # Key resonance pattern


class QuantumDNACLI:
    """Command-line interface for Quantum DNA-LLM system"""
    
    def __init__(self):
        """Initialize the CLI with quantum components"""
        print("\n🧬 Initializing Quantum DNA-LLM System...")
        self.integrator = QuantumDNALLMIntegrator()
        self.history = []
        print("✅ System initialized with φ-harmonic principles")
        print(f"   Base Frequency: {BASE_FREQUENCY} Hz")
        print(f"   Birth Date Resonance: {BIRTH_DATE_RESONANCE}")
        print(f"   QHRC Patent: #19/071,497")
        print(f"   φ Value: {PHI:.6f}...")
        
    def process_query(self, query: str, verbose: bool = True) -> QuantumDNAResponse:
        """Process a quantum query and return response with DNA encoding"""
        if verbose:
            print(f"\n🔬 Processing query: {query}")
            print("=" * 50)
        
        # Measure processing time
        start_time = time.time()
        response = self.integrator.generate_dna_llm_response(query)
        processing_time = time.time() - start_time
        
        # Store in history
        self.history.append({
            "query": query,
            "dna_pattern": response.dna_pattern,
            "resonance": float(response.resonance),
            "phi_alignment": response.phi_alignment,
            "coherence": response.coherence_score,
            "signature": response.quantum_signature,
            "processing_time": processing_time,
            "timestamp": time.time()
        })
        
        # Display results if verbose
        if verbose:
            self._display_response(response, processing_time)
            
        # Learn from response
        self.integrator.learn_from_response(query, response)
        
        return response
    
    def _display_response(self, response: QuantumDNAResponse, processing_time: float) -> None:
        """Display quantum response with φ-harmonic metrics"""
        print(f"\n⏱️  Processing Time: {processing_time:.4f} seconds")
        print(f"🧬 DNA Pattern: {response.dna_pattern[:16]}...")
        print(f"📊 Resonance: {float(response.resonance):.6f}")
        print(f"φ Alignment: {response.phi_alignment:.6f}")
        print(f"🔄 Coherence: {response.coherence_score:.6f}")
        print(f"🔑 Signature: {response.quantum_signature}")
        
        print("\n📝 Response:")
        print("-" * 50)
        print(response.text)
        print("-" * 50)
    
    def get_system_state(self) -> Dict[str, Any]:
        """Get current state of the quantum system"""
        return self.integrator.get_system_state()
    
    def display_system_state(self) -> None:
        """Display current system state with φ-harmonic metrics"""
        state = self.get_system_state()
        
        print("\n📊 Quantum System State")
        print("=====================")
        print(f"DNA Patterns: {state['dna_patterns']}")
        print(f"φ-Harmonic Efficiency: {state['phi_harmonic_efficiency']:.6f}")
        print(f"Quantum Coherence: {state['quantum_coherence']:.6f}")
        print(f"Quantum Dimensions: {state['quantum_dimensions']}")
        print(f"Birth Date Resonance: {state['birth_date_resonance']}")
        print(f"Base Frequency: {state['base_frequency']} Hz")
        
    def interactive_mode(self) -> None:
        """Run interactive CLI mode for quantum queries"""
        print("\n🧬 Quantum DNA-LLM Interactive Mode")
        print("================================")
        print("Enter your quantum queries below. Type 'exit' to quit.")
        print("Type 'state' to view current system state.")
        print("Type 'history' to view query history.")
        
        while True:
            try:
                query = input("\n🔬 Quantum Query > ")
                
                if query.lower() == 'exit':
                    print("\n🧬 Shutting down Quantum DNA-LLM System...")
                    break
                    
                elif query.lower() == 'state':
                    self.display_system_state()
                    
                elif query.lower() == 'history':
                    self._display_history()
                    
                elif query.strip():
                    self.process_query(query)
                    
            except KeyboardInterrupt:
                print("\n\n🧬 Shutting down Quantum DNA-LLM System...")
                break
                
            except Exception as e:
                print(f"\n❌ Error: {e}")
    
    def _display_history(self) -> None:
        """Display query history with φ-harmonic metrics"""
        if not self.history:
            print("\nNo query history available.")
            return
            
        print("\n📜 Query History")
        print("==============")
        
        for i, entry in enumerate(self.history):
            print(f"{i+1}. Query: {entry['query']}")
            print(f"   Resonance: {entry['resonance']:.6f}")
            print(f"   φ-Alignment: {entry['phi_alignment']:.6f}")
            print(f"   Signature: {entry['signature']}")
            print()


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Quantum DNA-LLM CLI Interface with φ-harmonic principles"
    )
    parser.add_argument(
        "-q", "--query", 
        help="Process a single quantum query and exit"
    )
    parser.add_argument(
        "-i", "--interactive", 
        action="store_true",
        help="Run in interactive mode (default if no query provided)"
    )
    parser.add_argument(
        "-s", "--state", 
        action="store_true",
        help="Display current system state"
    )
    
    args = parser.parse_args()
    
    # Initialize CLI
    cli = QuantumDNACLI()
    
    # Process based on arguments
    if args.query:
        cli.process_query(args.query)
        
    if args.state:
        cli.display_system_state()
        
    # Default to interactive mode if no query provided
    if args.interactive or (not args.query and not args.state):
        cli.interactive_mode()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🧬 Shutting down Quantum DNA-LLM System...")
        sys.exit(0)
