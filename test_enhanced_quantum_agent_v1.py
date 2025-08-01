import time
import math
import numpy as np
from typing import Dict, List, Any

from extensions.quantum_analysis.enhanced_quantum_agent_v1 import EnhancedQuantumAgentV1

def test_agent_with_sequence(agent: EnhancedQuantumAgentV1, sequence: List[Any], 
                           description: str = ""):
    """Test agent with a sequence of inputs."""
    print(f"\nTesting Agent with {description}")
    print("=" * 80)
    
    results = []
    for item in sequence:
        response = agent.process_input(item)
        results.append(response)
        
        # Print key metrics
        print(f"\nProcessing Input: {item}")
        print(f"Confidence: {response['response_metrics']['confidence']:.3f}")
        print(f"Resonance: {response['response_metrics']['resonance']:.3f}")
        print(f"Coherence: {response['response_metrics']['coherence']:.3f}")
        print(f"Phi-Harmonic: {response['response_metrics']['phi_harmonic']:.3f}")
        
        # Print agent state
        state = response['agent_state']
        print(f"\nAgent State:")
        print(f"Reasoning Capacity: {state['reasoning_capacity']:.3f}")
        print(f"Learning Capacity: {state['learning_capacity']:.3f}")
        print(f"Autonomy Level: {state['autonomy_level']:.3f}")
        print(f"Learning Cycles: {state['learning_cycles']}")
        
        # Print evolution metrics
        evolution = response['evolution_metrics']
        print(f"\nEvolution Metrics:")
        print(f"Reasoning Growth: {evolution['reasoning_growth']:.3f}")
        print(f"Learning Growth: {evolution['learning_growth']:.3f}")
        print(f"Autonomy Growth: {evolution['autonomy_growth']:.3f}")
    
    return results

def test_agent_with_patterns(agent: EnhancedQuantumAgentV1, patterns: List[Dict[str, Any]],
                           description: str = ""):
    """Test agent with quantum patterns."""
    print(f"\nTesting Agent with {description}")
    print("=" * 80)
    
    results = []
    for pattern in patterns:
        response = agent.process_input(pattern)
        results.append(response)
        
        # Print insights
        print(f"\nProcessing Pattern: {pattern}")
        for insight in response['insights']:
            if insight['type'] == 'primary':
                print(f"\nPrimary Insight:")
                print(f"Resonance: {insight['resonance']:.3f}")
                print(f"Stability: {insight['stability']:.3f}")
                print(f"Alignment: {insight['alignment']:.3f}")
                print(f"Confidence: {insight['confidence']:.3f}")
            else:
                print(f"\nSecondary Insight:")
                print(f"Pattern Relation: {insight['pattern_relation']:.3f}")
                print(f"Temporal Coherence: {insight['temporal_coherence']:.3f}")
                print(f"Bridge Strength: {insight['bridge_strength']:.3f}")
                print(f"Confidence: {insight['confidence']:.3f}")
    
    return results

def main():
    """Test enhanced quantum agent V1."""
    print("\n" + "=" * 80)
    print("ENHANCED QUANTUM AGENT V1 TEST")
    print("=" * 80 + "\n")
    
    # Initialize agent
    agent = EnhancedQuantumAgentV1()
    
    # Test with Fibonacci sequence
    fibonacci = [1, 1, 2, 3, 5, 8, 13, 21]
    test_agent_with_sequence(agent, fibonacci, "Fibonacci Sequence")
    
    # Test with phi-harmonic patterns
    phi = (1 + 5 ** 0.5) / 2
    patterns = [
        {
            'value': phi,
            'type': 'phi_harmonic',
            'resonance': phi ** 2,
            'stability': 1 / phi,
            'temporal': True
        },
        {
            'value': phi ** 2,
            'type': 'phi_squared',
            'resonance': phi ** 3,
            'stability': 1 / phi ** 2,
            'temporal': True
        },
        {
            'value': phi ** 3,
            'type': 'phi_cubed',
            'resonance': phi ** 4,
            'stability': 1 / phi ** 3,
            'temporal': True
        }
    ]
    test_agent_with_patterns(agent, patterns, "Phi-Harmonic Patterns")
    
    # Get final agent analysis
    print("\n" + "=" * 80)
    print("FINAL AGENT ANALYSIS")
    print("=" * 80)
    
    analysis = agent.get_agent_analysis()
    
    print("\nEvolution Trends:")
    trends = analysis['evolution_trends']
    print(f"Reasoning: {trends['reasoning']:.3f}")
    print(f"Learning: {trends['learning']:.3f}")
    print(f"Autonomy: {trends['autonomy']:.3f}")
    
    print("\nGrowth Factors:")
    factors = analysis['growth_factors']
    print(f"Reasoning: {factors['reasoning']:.3f}")
    print(f"Learning: {factors['learning']:.3f}")
    print(f"Autonomy: {factors['autonomy']:.3f}")
    
    print("\nResonance Factors:")
    resonance = analysis['resonance_factors']
    print(f"Phi: {resonance['phi']:.3f}")
    print(f"Temporal: {resonance['temporal']:.3f}")
    print(f"Quantum: {resonance['quantum']:.3f}")
    
    print("\nAgent Capabilities:")
    capabilities = analysis['agent_capabilities']
    print(f"Reasoning Capacity: {capabilities['reasoning_capacity']:.3f}")
    print(f"Learning Capacity: {capabilities['learning_capacity']:.3f}")
    print(f"Autonomy Level: {capabilities['autonomy_level']:.3f}")
    
    print("\nLearning Progress:")
    progress = analysis['learning_progress']
    print(f"Cycles: {progress['cycles']}")
    print(f"Evolution Rate: {progress['evolution_rate']:.3f}")
    print(f"Capability Rate: {progress['capability_rate']:.3f}")
    
    print("\n" + "=" * 80)
    print("ENHANCED QUANTUM AGENT TEST COMPLETED")
    print("=" * 80)

if __name__ == "__main__":
    main()
