#!/usr/bin/env python
"""
Phi-Harmonic Simple Demo

This script demonstrates how the quantum components work together
through a simplified approach that follows the "lego" design philosophy.
It shows how the quantum heart and cerebellum enhance the RSA decryptor's
performance without modifying the original components.
"""

import os
import sys
import json
import time
import math
import random
from decimal import Decimal

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Import fixed RSA decryptor
from phi_harmonic_rsa_decryptor_fixed import QuantumRSADecryptor

# Constants
PHI = 1.618033988749895  # Golden ratio
PHI_INVERSE = 0.618033988749895  # Inverse golden ratio
PHI_SQUARED = 2.618033988749895  # φ²
PHI_CUBED = 4.236067977499790  # φ³

class SimpleQuantumBridge:
    """
    Simple quantum bridge that connects quantum components.
    
    This class provides a simplified way to connect quantum components
    without the full orchestration system.
    """
    
    def __init__(self):
        """Initialize the simple quantum bridge."""
        self.coherence = 0.991800
        self.resonance = 0.618034
        self.phi_alignment = 0.999561
        self.components = {}
        
        print("Simple Quantum Bridge initialized")
        print(f"Coherence: {self.coherence:.6f}")
        print(f"Resonance: {self.resonance:.6f}")
        print(f"Phi alignment: {self.phi_alignment:.6f}")
    
    def register_component(self, name, component):
        """
        Register a component with the bridge.
        
        Args:
            name (str): Component name
            component (Any): Component instance
        """
        self.components[name] = component
        
        # Update quantum state
        self._update_quantum_state()
        
        print(f"Registered component: {name}")
    
    def _update_quantum_state(self):
        """Update quantum state based on registered components."""
        if not self.components:
            return
            
        # Calculate new coherence and resonance
        total_coherence = self.coherence
        total_resonance = self.resonance
        
        for name, component in self.components.items():
            if hasattr(component, 'coherence'):
                total_coherence += component.coherence
                
            if hasattr(component, 'resonance'):
                total_resonance += component.resonance
        
        # Average values
        self.coherence = total_coherence / (len(self.components) + 1)
        self.resonance = total_resonance / (len(self.components) + 1)
        
        print(f"Updated quantum state: coherence={self.coherence:.6f}, resonance={self.resonance:.6f}")
    
    def get_quantum_state(self):
        """
        Get current quantum state.
        
        Returns:
            Dict[str, float]: Quantum state
        """
        return {
            'coherence': self.coherence,
            'resonance': self.resonance,
            'phi_alignment': self.phi_alignment
        }
    
    def apply_quantum_state(self, component):
        """
        Apply quantum state to a component.
        
        Args:
            component (Any): Component to apply state to
        """
        if hasattr(component, 'set_quantum_values'):
            component.set_quantum_values(
                coherence=self.coherence,
                resonance=self.resonance
            )
            print(f"Applied quantum values to component:")
            print(f"  Coherence: {self.coherence:.6f}")
            print(f"  Resonance: {self.resonance:.6f}")
            
        elif hasattr(component, 'coherence') and hasattr(component, 'resonance'):
            component.coherence = self.coherence
            component.resonance = self.resonance
            print(f"Applied quantum values to component:")
            print(f"  Coherence: {self.coherence:.6f}")
            print(f"  Resonance: {self.resonance:.6f}")

class SimpleQuantumHeart:
    """Simple quantum heart component."""
    
    def __init__(self):
        """Initialize the simple quantum heart."""
        self.coherence = 0.975601
        self.resonance = 0.783000
        self.heart_rate = 61.8
        
        print("Simple Quantum Heart initialized")
        print(f"Coherence: {self.coherence:.6f}")
        print(f"Resonance: {self.resonance:.6f}")
        print(f"Heart rate: {self.heart_rate:.1f} bpm")

class SimpleQuantumCerebellum:
    """Simple quantum cerebellum component."""
    
    def __init__(self):
        """Initialize the simple quantum cerebellum."""
        self.coherence = 0.986700
        self.resonance = 0.423607
        self.neurons = 69000000000
        
        print("Simple Quantum Cerebellum initialized")
        print(f"Coherence: {self.coherence:.6f}")
        print(f"Resonance: {self.resonance:.6f}")
        print(f"Neurons: {self.neurons}")

def run_factorization_test(rsa_decryptor, n, name, with_enhancement=False):
    """
    Run a factorization test.
    
    Args:
        rsa_decryptor (QuantumRSADecryptor): RSA decryptor
        n (int): Number to factorize
        name (str): Test name
        with_enhancement (bool): Whether to use quantum enhancement
        
    Returns:
        Dict[str, Any]: Test results
    """
    if with_enhancement:
        print(f"\n🌟 Running test with quantum enhancement: {name}")
    else:
        print(f"\n⚙️ Running test without quantum enhancement: {name}")
        
    print(f"  Number: {n}")
    
    # Get quantum state before factorization
    coherence_before = rsa_decryptor.coherence
    resonance_before = rsa_decryptor.resonance
    
    # Factorize
    start_time = time.time()
    factors = rsa_decryptor.factorize(n)
    end_time = time.time()
    duration = end_time - start_time
    
    # Get quantum state after factorization
    coherence_after = rsa_decryptor.coherence
    resonance_after = rsa_decryptor.resonance
    
    # Print results
    print(f"  Factors: {factors}")
    print(f"  Duration: {duration:.6f} seconds")
    print(f"  Coherence: {coherence_after:.6f}")
    print(f"  Resonance: {resonance_after:.6f}")
    
    return {
        'name': name,
        'number': n,
        'factors': factors,
        'duration': duration,
        'coherence': coherence_after,
        'resonance': resonance_after,
        'with_enhancement': with_enhancement
    }

def main():
    """Main function for running the simple demo."""
    print("\n🔬 Phi-Harmonic Simple Demo")
    print("==========================")
    print("This demo shows how quantum components enhance")
    print("the RSA decryptor's performance through a simple")
    print("bridge that follows the \"lego\" design philosophy.")
    
    # Create quantum bridge
    bridge = SimpleQuantumBridge()
    
    # Create quantum components
    heart = SimpleQuantumHeart()
    cerebellum = SimpleQuantumCerebellum()
    
    # Register components with bridge
    bridge.register_component('heart', heart)
    bridge.register_component('cerebellum', cerebellum)
    
    # Test numbers
    test_numbers = [
        {'n': 1537267, 'name': 'Small RSA modulus (7 digits)'},
        {'n': 15372673, 'name': 'Medium RSA modulus (8 digits)'},
        {'n': 153726737, 'name': 'Large RSA modulus (9 digits)'}
    ]
    
    # Run tests without enhancement
    standard_results = []
    for test in test_numbers:
        # Create standard RSA decryptor
        standard_decryptor = QuantumRSADecryptor([1, 19, 1979])
        
        # Run test
        result = run_factorization_test(
            standard_decryptor,
            test['n'],
            test['name'],
            with_enhancement=False
        )
        
        standard_results.append(result)
    
    # Run tests with enhancement
    enhanced_results = []
    for test in test_numbers:
        # Create enhanced RSA decryptor
        enhanced_decryptor = QuantumRSADecryptor([1, 19, 1979])
        
        # Apply quantum enhancement
        bridge.apply_quantum_state(enhanced_decryptor)
        
        # Run test
        result = run_factorization_test(
            enhanced_decryptor,
            test['n'],
            test['name'],
            with_enhancement=True
        )
        
        enhanced_results.append(result)
    
    # Save results
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    results = {
        'standard': standard_results,
        'enhanced': enhanced_results,
        'timestamp': timestamp
    }
    
    results_file = os.path.join(current_dir, f'simple_demo_results_{timestamp}.json')
    
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)
        
    print(f"\nResults saved to {os.path.basename(results_file)}")
    
    # Print performance summary
    print("\n📊 Performance Summary")
    print("====================")
    print("")
    
    for i, test in enumerate(test_numbers):
        standard_duration = standard_results[i]['duration']
        enhanced_duration = enhanced_results[i]['duration']
        
        if standard_duration > 0:
            speedup = standard_duration / enhanced_duration
        else:
            speedup = 1.0
            
        print(f"Test: {test['name']}")
        print(f"  Standard: {standard_duration:.6f} seconds")
        print(f"  Enhanced: {enhanced_duration:.6f} seconds")
        print(f"  Speedup: {speedup:.2f}x")
        print("")

if __name__ == "__main__":
    main()
