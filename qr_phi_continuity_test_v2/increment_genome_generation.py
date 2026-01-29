#!/usr/bin/env python3
"""
Increment Genome Generation - Part of Quantum Phi-Harmonic QR System
By Vaughn Scott

This script increments the generation number in the QR genome file
and updates the phi-harmonic state accordingly.
"""

import os
import json
import time
from datetime import datetime

# Phi constant (Golden Ratio)
PHI = 1.618033988749895

def phi_resonance(value):
    """Calculate phi-harmonic resonance of a value."""
    return 1.0 / (1.0 + abs((value * PHI) % 1.0 - 0.5))

def increment_genome_generation(genome_file="qr_genome.json"):
    """
    Increment the generation number in the genome file and update phi-harmonic state.
    
    Args:
        genome_file: Path to the genome file
    
    Returns:
        dict: Updated genome data
    """
    print(f"🧬 Incrementing genome generation in {genome_file}")
    
    # Check if file exists
    if not os.path.exists(genome_file):
        print(f"❌ Genome file not found: {genome_file}")
        return None
    
    # Load genome
    try:
        with open(genome_file, 'r') as f:
            genome = json.load(f)
    except Exception as e:
        print(f"❌ Error loading genome file: {e}")
        return None
    
    # Get current generation
    current_generation = genome.get("generation", 1)
    print(f"Current generation: {current_generation}")
    
    # Increment generation
    new_generation = current_generation + 1
    genome["generation"] = new_generation
    
    # Update phi state
    phi_time = time.time() * PHI % 1.0
    resonance = phi_resonance(phi_time)
    
    # Calculate complexity based on generation
    complexity = 0.5 + (new_generation / 10.0)
    if complexity > 0.95:
        complexity = 0.95  # Cap complexity at 0.95
    
    # Update phi state
    genome["phi_state"] = {
        "complexity": complexity,
        "resonance": resonance,
        "generation": new_generation
    }
    
    # Update all codons' phi state generation
    for group in genome.get("groups", []):
        for codon in group.get("codons", []):
            if "phi_state" in codon:
                codon["phi_state"]["generation"] = new_generation
    
    # Save updated genome
    try:
        with open(genome_file, 'w') as f:
            json.dump(genome, f, indent=2)
        print(f"✅ Updated genome generation to {new_generation}")
        print(f"   Complexity: {complexity:.6f}")
        print(f"   Resonance: {resonance:.6f}")
    except Exception as e:
        print(f"❌ Error saving genome file: {e}")
        return None
    
    return genome

def main():
    """Main function."""
    print("🧬 QR Genome Generation Incrementer - Quantum Phi-Harmonic QR System")
    print("=" * 60)
    
    # Increment genome generation
    genome = increment_genome_generation()
    
    if genome:
        print("\n✅ Genome generation successfully incremented")
    else:
        print("\n❌ Failed to increment genome generation")

if __name__ == "__main__":
    main()
