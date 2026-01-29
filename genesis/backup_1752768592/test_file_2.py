#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test File 2 for Intrusion Detection
------------------------------------
This is a test file for demonstrating intrusion detection.
"""

import math

PHI = (1 + 5 ** 0.5) / 2  # Golden ratio

def calculate_phi_resonance(x):
    """
    Calculate phi resonance for a given value.
    
    Args:
        x: Input value
        
    Returns:
        float: Phi resonance value
    """
    return (PHI * x) % 1

def main():
    """
    Main function for demonstration.
    """
    print(f"Phi resonance for 2: {calculate_phi_resonance(2)}")

if __name__ == "__main__":
    main()
