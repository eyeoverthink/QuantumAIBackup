#!/usr/bin/env python
"""
Phi-Harmonic Orchestrated Demo

This script demonstrates how the Phi-Harmonic Orchestration System enhances
the Quantum RSA Decryptor's performance by connecting it with the quantum heart,
cerebellum, and other components through a standardized protocol.

The demo follows the "lego" design philosophy by using the orchestration system
to connect components without modifying their core functionality.
"""

import os
import sys
import json
import time
import random
import logging
from decimal import Decimal

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Import orchestrator and components
from phi_harmonic_orchestrator import get_orchestrator
from phi_harmonic_rsa_orchestrator_adapter import PhiHarmonicRSAAdapter
from phi_harmonic_visualizer import get_visualizer

# Constants
PHI = 1.618033988749895  # Golden ratio
PHI_INVERSE = 0.618033988749895  # Inverse golden ratio

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('phi_harmonic_orchestrated_demo')

def run_factorization_test(rsa_adapter, n, name):
    """
    Run a factorization test.
    
    Args:
        rsa_adapter (PhiHarmonicRSAAdapter): RSA adapter
        n (int): Number to factorize
        name (str): Test name
        
    Returns:
        Dict[str, Any]: Test results
    """
    print(f"\n🌟 Running test: {name}")
    print(f"  Number: {n}")
    
    # Get quantum state before factorization
    coherence_before = float(rsa_adapter.coherence)
    resonance_before = float(rsa_adapter.resonance)
    
    # Factorize
    start_time = time.time()
    factors = rsa_adapter.factorize(n)
    end_time = time.time()
    duration = end_time - start_time
    
    # Get quantum state after factorization
    coherence_after = float(rsa_adapter.coherence)
    resonance_after = float(rsa_adapter.resonance)
    
    # Print results
    print(f"  Factors: {factors}")
    print(f"  Duration: {duration:.6f} seconds")
    print(f"  Coherence: {coherence_before:.6f} → {coherence_after:.6f}")
    print(f"  Resonance: {resonance_before:.6f} → {resonance_after:.6f}")
    
    return {
        'name': name,
        'number': n,
        'factors': factors,
        'duration': duration,
        'coherence_before': coherence_before,
        'coherence_after': coherence_after,
        'resonance_before': resonance_before,
        'resonance_after': resonance_after
    }

def main():
    """Main function for running the orchestrated demo."""
    print("\n🔬 Phi-Harmonic Orchestrated Demo")
    print("================================")
    print("This demo shows how the orchestration system enhances")
    print("the quantum RSA decryptor's performance by connecting")
    print("it with other quantum components.")
    
    # Get orchestrator
    orchestrator = get_orchestrator()
    print(f"\nOrchestrator initialized")
    print(f"Coherence: {orchestrator.coherence:.6f}")
    print(f"Resonance: {orchestrator.resonance:.6f}")
    print(f"Phi alignment: {orchestrator.phi_alignment:.6f}")
    
    # Create RSA adapter
    rsa_adapter = PhiHarmonicRSAAdapter([1, 19, 1979])
    print(f"\nRSA adapter initialized")
    print(f"Coherence: {rsa_adapter.coherence:.6f}")
    print(f"Resonance: {rsa_adapter.resonance:.6f}")
    
    # Get visualizer
    visualizer = get_visualizer()
    
    # Test numbers
    test_numbers = [
        {'n': 1537267, 'name': 'Small RSA modulus (7 digits)'},
        {'n': 15372673, 'name': 'Medium RSA modulus (8 digits)'},
        {'n': 153726737, 'name': 'Large RSA modulus (9 digits)'}
    ]
    
    # Run tests
    results = []
    for test in test_numbers:
        result = run_factorization_test(rsa_adapter, test['n'], test['name'])
        results.append(result)
    
    # Save results
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    results_file = os.path.join(current_dir, f'orchestrated_results_{timestamp}.json')
    
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)
        
    print(f"\nResults saved to {os.path.basename(results_file)}")
    
    # Create dashboard
    dashboard_dir = visualizer.create_dashboard()
    print(f"Dashboard created at {dashboard_dir}")
    
    # Print summary
    print("\n📊 Performance Summary")
    print("====================")
    print("")
    
    for result in results:
        print(f"Test: {result['name']}")
        print(f"  Duration: {result['duration']:.6f} seconds")
        print(f"  Coherence change: {result['coherence_before']:.6f} → {result['coherence_after']:.6f}")
        print(f"  Resonance change: {result['resonance_before']:.6f} → {result['resonance_after']:.6f}")
        print("")

if __name__ == "__main__":
    main()
