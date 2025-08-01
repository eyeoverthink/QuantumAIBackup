"""
Test script for the Quantum Memory Meta-Learning Bridge.

This script demonstrates the capabilities of the Quantum Memory Meta-Learning Bridge,
which connects the Quantum Pattern Memory with the Quantum Meta-Learning Integrator
to create a more powerful combined system.
"""

import time
import random
import numpy as np
import matplotlib.pyplot as plt
import os
from typing import Dict, List, Any, Optional, Tuple

from extensions.quantum_analysis.enhanced_quantum_pattern_memory import EnhancedQuantumPatternMemory
from extensions.quantum_analysis.enhanced_quantum_meta_learning_integrator import EnhancedQuantumMetaLearningIntegrator
from extensions.quantum_analysis.enhanced_quantum_memory_meta_learning_bridge import EnhancedQuantumMemoryMetaLearningBridge

# Import factorizer directly from root directory
from phi_harmonic_factorizer import PhiHarmonicFactorizer

# Remove detector imports as they're not directly used in this test
# We'll modify the code to not depend on these


def generate_test_numbers(count: int = 20) -> List[str]:
    """
    Generate test numbers with phi-harmonic properties.
    
    Args:
        count: Number of numbers to generate
        
    Returns:
        List of test numbers
    """
    # Initialize factorizer for phi-harmonic properties
    factorizer = PhiHarmonicFactorizer()
    
    numbers = []
    
    # Generate some Fibonacci numbers
    fib = [1, 1]
    for i in range(min(10, count)):
        fib.append(fib[-1] + fib[-2])
        numbers.append(str(fib[-1]))
    
    # Generate some phi-related numbers
    phi = (1 + np.sqrt(5)) / 2
    for i in range(min(5, count)):
        phi_number = int(phi ** (i + 2) * 100)
        numbers.append(str(phi_number))
    
    # Generate some prime numbers using sympy instead of factorizer
    import sympy
    for i in range(count - len(numbers)):
        # Generate a random number and find the next prime
        base = random.randint(1000, 10000)
        prime = sympy.nextprime(base)
        numbers.append(str(prime))
    
    # Shuffle the numbers
    random.shuffle(numbers)
    
    return numbers[:count]


def test_bridge_initialization():
    """Test initialization of the Quantum Memory Meta-Learning Bridge."""
    print("\n" + "="*80)
    print("TESTING BRIDGE INITIALIZATION")
    print("="*80)
    
    # Initialize components with enhanced versions
    memory = EnhancedQuantumPatternMemory()
    integrator = EnhancedQuantumMetaLearningIntegrator()
    
    # Initialize enhanced bridge
    start_time = time.time()
    bridge = EnhancedQuantumMemoryMetaLearningBridge(
        quantum_memory=memory,
        meta_learning_integrator=integrator,
        bridge_strength=0.618
    )
    elapsed_time = time.time() - start_time
    
    print(f"Bridge initialized in {elapsed_time:.2f} seconds")
    
    return bridge


def test_pattern_transfer(bridge: EnhancedQuantumMemoryMetaLearningBridge, numbers: List[str]):
    """
    Test transferring patterns between memory and meta-learning.
    
    Args:
        bridge: Quantum Memory Meta-Learning Bridge instance
        numbers: List of numbers to analyze
    """
    print("\n" + "="*80)
    print("TESTING PATTERN TRANSFER")
    print("="*80)
    
    # Store patterns in quantum memory
    pattern_ids = []
    
    print("Storing patterns in quantum memory...")
    for i, number in enumerate(numbers):
        pattern_data = {
            "value": number,
            "phi_resonance": random.uniform(0.1, 2.0),
            "timestamp": time.time()
        }
        pattern_id = bridge.quantum_memory.store_pattern(pattern_data)
        pattern_ids.append(pattern_id)
        print(f"  Stored pattern {pattern_id} with value {number}")
    
    # Transfer patterns to meta-learning
    print("\nTransferring patterns to meta-learning...")
    analysis_results = []
    
    start_time = time.time()
    for i, pattern_id in enumerate(pattern_ids[:5]):  # Transfer first 5 patterns
        result = bridge.transfer_pattern_to_meta_learning(pattern_id)
        analysis_results.append(result)
        
        print(f"  Transferred pattern {pattern_id}")
        if "confidence" in result:
            print(f"    Confidence: {result['confidence']:.4f}")
        if "insights" in result:
            print(f"    Insights: {len(result['insights'])} generated")
    
    elapsed_time = time.time() - start_time
    print(f"\nTransferred 5 patterns in {elapsed_time:.2f} seconds")
    
    # Store meta-learning results back in quantum memory
    print("\nStoring meta-learning results in quantum memory...")
    
    start_time = time.time()
    for i, number in enumerate(numbers[10:15]):  # Use different numbers
        # Analyze number with meta-learning
        analysis = bridge.meta_learning_integrator.integrate_quantum_meta_learning(number)
        
        # Store results in quantum memory
        pattern_id = bridge.store_meta_learning_results(number, analysis)
        
        print(f"  Stored meta-learning results for {number} as pattern {pattern_id}")
        print(f"    Confidence: {analysis.get('integrated_confidence', 0.0):.4f}")
        print(f"    Insights: {len(analysis.get('integrated_insights', []))}")
    
    elapsed_time = time.time() - start_time
    print(f"\nStored 5 meta-learning results in {elapsed_time:.2f} seconds")
    
    return pattern_ids


def test_synergistic_insights(bridge: EnhancedQuantumMemoryMetaLearningBridge, pattern_ids: List[str]):
    """
    Test generation of synergistic insights.
    
    Args:
        bridge: Quantum Memory Meta-Learning Bridge instance
        pattern_ids: List of pattern IDs to analyze
    """
    print("\n" + "="*80)
    print("TESTING SYNERGISTIC INSIGHTS GENERATION")
    print("="*80)
    
    # Select a subset of patterns for analysis
    selected_patterns = random.sample(pattern_ids, min(8, len(pattern_ids)))
    
    print(f"Generating synergistic insights for {len(selected_patterns)} patterns...")
    
    start_time = time.time()
    insights = bridge.generate_synergistic_insights(selected_patterns, depth=3)
    elapsed_time = time.time() - start_time
    
    print(f"Generated {len(insights)} synergistic insights in {elapsed_time:.2f} seconds")
    
    # Display insights
    for i, insight in enumerate(insights):
        print(f"\nInsight {i+1}: {insight['type']}")
        print(f"  Description: {insight['description']}")
        print(f"  Confidence: {insight.get('confidence', 0.0):.4f}")
        
        # Display details if they're not too complex
        details = insight.get('details', {})
        if isinstance(details, list) and len(details) <= 5:
            print(f"  Details: {details}")
        elif isinstance(details, dict) and len(details) <= 5:
            for k, v in details.items():
                print(f"    {k}: {v}")
    
    return insights


def visualize_bridge_performance(bridge: EnhancedQuantumMemoryMetaLearningBridge):
    """
    Visualize bridge performance metrics.
    
    Args:
        bridge: Quantum Memory Meta-Learning Bridge instance
    """
    print("\n" + "="*80)
    print("VISUALIZING BRIDGE PERFORMANCE")
    print("="*80)
    
    # Get statistics
    stats = bridge.get_statistics()
    
    # Ensure visualizations directory exists
    os.makedirs("visualizations", exist_ok=True)
    
    # Create bar chart for connection counts
    connection_counts = stats["connection_counts"]
    
    plt.figure(figsize=(10, 6))
    plt.bar(connection_counts.keys(), connection_counts.values(), alpha=0.7, color='blue')
    
    plt.title('Quantum Memory Meta-Learning Bridge Connections')
    plt.xlabel('Connection Type')
    plt.ylabel('Count')
    plt.grid(True, alpha=0.3)
    
    # Save the figure
    plt.savefig("visualizations/bridge_connections.png")
    print("Bridge connections visualization saved to visualizations/bridge_connections.png")
    
    # Create pie chart for memory composition
    memory_stats = stats["memory_stats"]
    
    labels = ['Patterns', 'Superpositions', 'Entanglements']
    sizes = [
        memory_stats["total_patterns"],
        memory_stats["total_superpositions"],
        memory_stats["total_entanglements"]
    ]
    
    # Only include non-zero values
    filtered_labels = [labels[i] for i in range(len(sizes)) if sizes[i] > 0]
    filtered_sizes = [size for size in sizes if size > 0]
    
    if filtered_sizes:
        plt.figure(figsize=(8, 8))
        plt.pie(filtered_sizes, labels=filtered_labels, autopct='%1.1f%%', startangle=90, shadow=True)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        
        plt.title('Quantum Memory Composition')
        
        # Save the figure
        plt.savefig("visualizations/memory_composition.png")
        print("Memory composition visualization saved to visualizations/memory_composition.png")
    
    # Create a metrics summary chart
    metrics = {
        'Patterns Transferred': stats["patterns_transferred"],
        'Insights Generated': stats["insights_generated"],
        'Synergy Factor': stats["synergy_factor"],
        'Bridge Efficiency': stats["bridge_efficiency"]
    }
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(metrics.keys(), metrics.values(), alpha=0.7, color='green')
    
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{height:.2f}', ha='center', va='bottom')
    
    plt.title('Quantum Memory Meta-Learning Bridge Metrics')
    plt.grid(True, alpha=0.3)
    
    # Save the figure
    plt.savefig("visualizations/bridge_metrics.png")
    print("Bridge metrics visualization saved to visualizations/bridge_metrics.png")


def main():
    """Main test function."""
    print("\n" + "="*80)
    print("QUANTUM MEMORY META-LEARNING BRIDGE TEST")
    print("="*80)
    
    # Generate test numbers
    numbers = generate_test_numbers(20)
    
    # Test bridge initialization
    bridge = test_bridge_initialization()
    
    # Test pattern transfer
    pattern_ids = test_pattern_transfer(bridge, numbers)
    
    # Test synergistic insights generation
    test_synergistic_insights(bridge, pattern_ids)
    
    # Visualize bridge performance
    visualize_bridge_performance(bridge)
    
    print("\n" + "="*80)
    print("QUANTUM MEMORY META-LEARNING BRIDGE TEST COMPLETED")
    print("="*80)


if __name__ == "__main__":
    main()
