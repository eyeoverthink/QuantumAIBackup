"""
Quantum Wisdom Integration Test and Monitor
"""
from quantum_wisdom_core import QuantumWisdomCore
from quantum_core.constants import PHI
import numpy as np
import time

def test_wisdom_integration():
    """Test and monitor quantum wisdom integration."""
    print("\n🧠 Quantum Wisdom Integration Test")
    print("=" * 50)
    
    wisdom = QuantumWisdomCore()
    
    # Test 1: Gupta Mathematics
    print("\n📐 Testing Gupta Mathematics")
    test_values = [0, 1, PHI, np.pi, float('inf')]
    for value in test_values:
        result = wisdom.apply_gupta_mathematics(value)
        if isinstance(value, (int, float)) and value != float('inf'):
            print(f"Input: {value:.6f}")
        else:
            print(f"Input: {value}")
            
        if isinstance(result, (int, float)) and result != float('inf'):
            print(f"Result: {result:.6f}")
        else:
            print(f"Result: {result}")
        
    # Test 2: House of Wisdom
    print("\n📚 Testing House of Wisdom")
    knowledge_types = ['algebra', 'optics', 'medicine', 'chemistry']
    for knowledge in knowledge_types:
        resonance = wisdom.channel_house_wisdom(knowledge)
        print(f"{knowledge.title()}: {resonance:.6f} Hz")
        
    # Test 3: Newtonian Principles
    print("\n🍎 Testing Newtonian Principles")
    masses = [1.0, PHI, PHI**2]
    distances = [1.0, PHI, PHI**2]
    
    for mass in masses:
        for distance in distances:
            forces = wisdom.apply_newton_principles(mass, distance)
            print(f"\nMass: {mass:.2f}, Distance: {distance:.2f}")
            for force_type, value in forces.items():
                print(f"{force_type}: {value:.6e}")
                
    # Test 4: Schrödinger States
    print("\n🐱 Testing Schrödinger States")
    states = ['unobserved', 'observed']
    for state in states:
        result = wisdom.schrodinger_observation(state)
        print(f"\nState: {state}")
        for key, value in result.items():
            print(f"{key}: {value:.6f}")
            
    # Test 5: Integrated Wisdom
    print("\n🌟 Testing Integrated Wisdom")
    print("=" * 50)
    
    # Monitor real-time integration
    for i in range(5):
        value = PHI ** i
        knowledge_type = knowledge_types[i % len(knowledge_types)]
        mass = masses[i % len(masses)]
        distance = distances[i % len(distances)]
        
        result = wisdom.integrate_all_wisdom(value, knowledge_type, mass, distance)
        
        print(f"\nIteration {i+1}:")
        print(f"Input: φ^{i} = {value:.6f}")
        print(f"Knowledge: {knowledge_type}")
        for aspect, measurement in result.items():
            print(f"{aspect}: {measurement:.6f}")
        
        # Monitor quantum coherence
        coherence = result['quantum'] / (PHI ** 4)
        print(f"Quantum Coherence: {coherence:.6f}")
        
        # Add small delay for observation
        time.sleep(0.5)

if __name__ == "__main__":
    test_wisdom_integration()
