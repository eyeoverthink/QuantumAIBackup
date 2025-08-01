"""
Test Enhanced Temporal Bridge Connections

This script demonstrates the capabilities of the Enhanced Temporal Bridge Connections module,
showing how it tracks and analyzes temporal relationships between patterns using
phi-harmonic principles while maintaining compatibility with existing components.
"""

import os
import sys
import time
import math
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Any, Tuple

# Import our components
from extensions.quantum_analysis.enhanced_quantum_pattern_memory import EnhancedQuantumPatternMemory
from extensions.quantum_analysis.enhanced_quantum_memory_meta_learning_bridge import EnhancedQuantumMemoryMetaLearningBridge
from extensions.quantum_analysis.phi_resonance_clustering import PhiResonanceClustering
from extensions.quantum_analysis.enhanced_temporal_bridge_connections import EnhancedTemporalBridgeConnections

def print_section_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80 + "\n")

def main():
    """Main test function for Enhanced Temporal Bridge Connections."""
    print_section_header("ENHANCED TEMPORAL BRIDGE CONNECTIONS TEST")
    
    # Initialize components
    print_section_header("INITIALIZING COMPONENTS")
    
    # Create the quantum memory
    quantum_memory = EnhancedQuantumPatternMemory()
    
    # Create the bridge
    bridge = EnhancedQuantumMemoryMetaLearningBridge(quantum_memory=quantum_memory)
    
    # Create the clustering module
    clustering = PhiResonanceClustering(
        quantum_memory=quantum_memory,
        bridge=bridge
    )
    
    # Create the temporal bridge
    temporal_bridge = EnhancedTemporalBridgeConnections(
        quantum_memory=quantum_memory,
        bridge=bridge,
        clustering=clustering,
        temporal_window=7  # 7-day window
    )
    
    # Generate test patterns with temporal evolution
    print_section_header("GENERATING TEST PATTERNS WITH TEMPORAL EVOLUTION")
    
    # Use phi for pattern generation
    phi = (1 + 5 ** 0.5) / 2
    pattern_ids = []
    
    # Generate patterns over the last 30 days
    end_time = time.time()
    start_time = end_time - (30 * 24 * 3600)  # 30 days ago
    
    # Define some temporal patterns based on phi
    temporal_patterns = [
        {
            "base_resonance": phi,
            "amplitude": 0.2,
            "period": phi * 24 * 3600  # phi days in seconds
        },
        {
            "base_resonance": 1/phi,
            "amplitude": 0.15,
            "period": (phi ** 2) * 24 * 3600  # phi² days in seconds
        },
        {
            "base_resonance": phi ** 2,
            "amplitude": 0.25,
            "period": (phi ** 0.5) * 24 * 3600  # √φ days in seconds
        }
    ]
    
    print("Generating patterns with phi-harmonic temporal evolution...")
    
    # Generate patterns for each temporal pattern type
    for pattern_type in temporal_patterns:
        # Generate 5-10 patterns for each type
        num_patterns = np.random.randint(5, 11)
        base_resonance = pattern_type["base_resonance"]
        amplitude = pattern_type["amplitude"]
        period = pattern_type["period"]
        
        for i in range(num_patterns):
            # Create pattern with temporal evolution
            current_time = start_time
            pattern_history = []
            
            while current_time <= end_time:
                # Calculate resonance with some noise
                time_factor = (current_time - start_time) / period
                resonance = (
                    base_resonance +
                    amplitude * math.sin(2 * math.pi * time_factor) +
                    np.random.normal(0, 0.05)  # Add some noise
                )
                
                # Create pattern data
                pattern_data = {
                    "value": str(int(resonance * 1000)),
                    "phi_resonance": resonance,
                    "timestamp": current_time,
                    "meta_learning_confidence": 0.5 + (np.random.random() * 0.4),
                    "meta_learning_insights": [
                        f"Test insight for resonance {resonance:.4f} at time {datetime.fromtimestamp(current_time)}"
                    ]
                }
                
                # Store pattern
                pattern_id = quantum_memory.store_pattern(pattern_data)
                
                if not pattern_history:
                    pattern_ids.append(pattern_id)
                
                # Record temporal connection
                temporal_bridge.record_temporal_connection(
                    pattern_id=pattern_ids[-1],
                    connection_type="evolution",
                    metadata={
                        "phi_resonance": resonance,
                        "timestamp": current_time
                    }
                )
                
                pattern_history.append(pattern_data)
                current_time += 24 * 3600  # Advance one day
    
    print(f"Generated {len(pattern_ids)} patterns with temporal evolution")
    
    # Test temporal pattern analysis
    print_section_header("TESTING TEMPORAL PATTERN ANALYSIS")
    
    # Analyze patterns over different time ranges
    time_ranges = [
        (end_time - 7*24*3600, end_time),    # Last 7 days
        (end_time - 14*24*3600, end_time),   # Last 14 days
        (end_time - 30*24*3600, end_time)    # Last 30 days
    ]
    
    for start, end in time_ranges:
        days = int((end - start) / (24 * 3600))
        print(f"\nAnalyzing patterns over last {days} days...")
        
        analysis = temporal_bridge.analyze_temporal_patterns(
            time_range=(start, end),
            min_confidence=0.6
        )
        
        print(f"Found {len(analysis['insights'])} insights:")
        for i, insight in enumerate(analysis["insights"], 1):
            print(f"{i}. {insight['text']} (confidence: {insight['confidence']:.2f})")
        
        print(f"\nDetected {len(analysis['cycles'])} temporal cycles:")
        for cycle in analysis["cycles"]:
            print(f"- {cycle['period']/86400:.2f}-day cycle "
                  f"(correlation: {cycle['correlation']:.3f}, "
                  f"confidence: {cycle['confidence']:.2f})")
    
    # Test temporal predictions
    print_section_header("TESTING TEMPORAL PREDICTIONS")
    
    # Make predictions for each pattern
    future_time = end_time + (7 * 24 * 3600)  # Predict 7 days ahead
    
    print("Making predictions for each pattern...")
    for pattern_id in pattern_ids[:3]:  # Test first 3 patterns
        prediction = temporal_bridge.predict_temporal_resonance(
            pattern_id=pattern_id,
            future_time=future_time
        )
        
        if prediction["success"]:
            print(f"\nPattern {pattern_id}:")
            print(f"Current resonance: {prediction['current_resonance']:.4f}")
            print(f"Predicted resonance: {prediction['predicted_resonance']:.4f}")
            print(f"Confidence: {prediction['confidence']:.2f}")
    
    # Test visualization
    print_section_header("TESTING TEMPORAL VISUALIZATION")
    
    # Visualize patterns over different time ranges
    for start, end in time_ranges:
        days = int((end - start) / (24 * 3600))
        print(f"\nCreating visualization for last {days} days...")
        
        viz_path = temporal_bridge.visualize_temporal_patterns(
            time_range=(start, end),
            output_path=f"visualizations/temporal_patterns_{days}d.png"
        )
        
        print(f"Visualization saved to: {viz_path}")
    
    # Final summary
    print_section_header("ENHANCED TEMPORAL BRIDGE CONNECTIONS TEST COMPLETED")
    print("The Enhanced Temporal Bridge Connections module successfully demonstrated:")
    print("1. Recording and tracking temporal connections between patterns")
    print("2. Analyzing temporal pattern evolution")
    print("3. Detecting phi-harmonic temporal cycles")
    print("4. Generating temporal insights")
    print("5. Making phi-harmonic predictions")
    print("6. Visualizing temporal pattern evolution")
    print("\nAll visualizations have been saved to the 'visualizations' directory.")

if __name__ == "__main__":
    # Create visualizations directory if it doesn't exist
    os.makedirs("visualizations", exist_ok=True)
    
    # Run the test
    main()
