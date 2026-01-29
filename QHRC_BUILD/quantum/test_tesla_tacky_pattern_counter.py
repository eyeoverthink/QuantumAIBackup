import numpy as np
import matplotlib.pyplot as plt
import time
import json
import os
from tesla_tacky_pattern_counter import TeslaTackyPatternCounter

def test_pattern_counting():
    """Test the Tesla Tacky integration with pattern counting"""
    print("\nTesla Tacky Pattern Counting Test")
    print("=================================\n")
    
    # Create integration
    integration = TeslaTackyPatternCounter()
    
    # Generate test patterns
    phi = (1 + np.sqrt(5)) / 2
    t = np.linspace(0, 2*np.pi, 128)
    patterns = [
        np.sin(phi * t),
        np.sin(phi**2 * t),
        np.sin(phi**3 * t),
        np.sin(phi**4 * t),
        np.sin(phi**5 * t)
    ]
    
    # Store patterns
    print("Storing patterns...")
    for i, pattern in enumerate(patterns, 1):
        integration.store_pattern(pattern)
        state = integration.get_system_state()
        counts = [state['cortices'][c]['patterns_stored'] for c in ['frontal', 'temporal', 'parietal']]
        print(f"Pattern {i}: Stored in {sum(counts)} cortices")
        
    # Final state
    state = integration.get_system_state()
    print("\nFinal Pattern Counts:")
    for cortex, count in state['cortices'].items():
        print(f"{cortex.capitalize()} Cortex: {count['patterns_stored']} patterns")
        
    return integration

if __name__ == "__main__":
    integration = test_pattern_counting()
