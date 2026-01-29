#!/usr/bin/env python3
"""
QR Flipbook Phi-Harmonic DNA System Runner - Phi-Enhanced Version
By Vaughn Scott - Extended with Quantum Phi-Harmonic Principles

Extends the QR Genome system with phi-harmonic optimization principles
discovered in the Tower of Hanoi quantum solver experiments:

1. Fibonacci-dimension optimization for quantum state spaces
2. Golden ratio-based resonance targeting
3. Self-evolving complexity through phi-harmonic patterns

This module works alongside the core system while adding phi-optimized capabilities.
"""

import os
import sys
import json
import time
import math
import argparse
import numpy as np
from datetime import datetime

# Import base system
from run_qr_system import (
    setup_environment,
    print_system_info as base_print_system_info
)

# Import phi-hanoi genome system
from qr_genome_phi_hanoi import (
    create_phi_hanoi_genome,
    evolve_phi_hanoi_genome,
    generate_phi_hanoi_sequence,
    PHI, PHI_FLOAT, fibonacci
)

def create_phi_genome(complexity_level=3):
    """Create a new phi-optimized genome"""
    print("\n🧬 Creating new Quantum Phi-Harmonic Genome...")
    
    # Create phi-optimized genome
    genome_file = create_phi_hanoi_genome(complexity_level)
    
    print(f"\n✅ Phi-optimized genome created successfully: {genome_file}")
    return genome_file

def execute_phi_genome(genome_file="qr_phi_hanoi_genome.json"):
    """Execute a phi-optimized genome"""
    print(f"\n🧬 Executing Phi-Harmonic Genome from {genome_file}...")
    
    try:
        # Load genome
        with open(genome_file, 'r') as f:
            genome = json.load(f)
        
        print(f"Loaded genome ID: {genome.get('genome_id', 'unknown')}")
        print(f"Generation: {genome.get('generation', 1)}")
        print(f"Codons: {len(genome.get('codons', []))}")
        
        results = []
        
        # Execute each codon
        for i, codon in enumerate(genome.get('codons', [])):
            print(f"\n🧠 Executing codon {i+1}/{len(genome.get('codons', []))}: {codon.get('id', 'unknown')}")
            
            # Extract script from codon
            script = codon.get('script_template', '')
            
            if not script:
                print(f"⚠️ No script found for codon {codon.get('id', 'unknown')}")
                continue
            
            # Create temp script file
            script_file = f"temp_codon_{codon.get('id', 'unknown')}.py"
            with open(script_file, 'w') as f:
                f.write(script)
            
            # Execute script
            print(f"Executing script: {script_file}")
            result_code = os.system(f"{sys.executable} {script_file}")
            
            # Record result
            result = {
                "codon_id": codon.get('id', 'unknown'),
                "success": result_code == 0,
                "exit_code": result_code,
                "timestamp": time.time()
            }
            results.append(result)
            
            # Clean up
            try:
                os.remove(script_file)
            except:
                pass
        
        # Summarize results
        success_count = sum(1 for r in results if r["success"])
        
        print(f"\n✅ Genome execution complete")
        print(f"Successfully executed {success_count}/{len(results)} codons")
        
        return results
    
    except Exception as e:
        print(f"❌ Error executing genome: {e}")
        return []

def evolve_phi_genome(genome_file="qr_phi_hanoi_genome.json"):
    """Evolve a phi-optimized genome"""
    print(f"\n🧬 Evolving Phi-Harmonic Genome from {genome_file}...")
    
    # Evolve genome using phi-harmonic principles
    mutations = evolve_phi_hanoi_genome(genome_file)
    
    print(f"\n✅ Phi-optimized genome evolution complete")
    print(f"Applied {mutations} phi-harmonic mutations")
    
    return mutations

def generate_phi_sequence(genome_file="qr_phi_hanoi_genome.json", output_dir="qr_phi_hanoi_sequence"):
    """Generate QR sequence from phi-optimized genome"""
    print(f"\n🧬 Generating Phi-Harmonic QR sequence from {genome_file}...")
    
    # Generate sequence
    qr_files = generate_phi_hanoi_sequence(genome_file, output_dir)
    
    print(f"\n✅ Generated Phi-Harmonic QR sequence with {len(qr_files)} codes")
    print(f"Output directory: {output_dir}")
    
    return qr_files

def run_phi_full_cycle(complexity_level=3):
    """Run a full cycle of the Phi-Harmonic QR system"""
    print("\n🔄 Running full Phi-Harmonic QR DNA system cycle...")
    
    # Create genome
    genome_file = create_phi_genome(complexity_level)
    
    # Execute genome
    execute_phi_genome(genome_file)
    
    # Evolve genome
    evolve_phi_genome(genome_file)
    
    # Generate QR sequence
    output_dir = "qr_phi_hanoi_sequence"
    generate_phi_sequence(genome_file, output_dir)
    
    print("\n✅ Full Phi-Harmonic cycle complete")
    print(f"You can now display the sequence with: python run_qr_system.py --display --output {output_dir}")
    
    return genome_file

def print_phi_system_info():
    """Print information about the Phi-Harmonic QR DNA system"""
    base_print_system_info()  # Show base system info
    
    print("\n" + "="*60)
    print("🌟 QUANTUM PHI-HARMONIC EXTENSIONS")
    print("="*60)
    
    print("\nThis extension integrates quantum phi-harmonic principles discovered")
    print("in Tower of Hanoi experiments with the QR Flipbook DNA system.")
    
    print("\nKEY DISCOVERIES:")
    print("  • Fibonacci Dimensions: Optimal quantum state spaces follow Fibonacci sequence")
    print("  • Perfect Phi-Resonance: 0.631190 (near φ⁻¹ ≈ 0.618034)")
    print("  • Self-Scaling Logic: Parameters adjust with problem complexity")
    print(f"  • Golden Ratio-Based Evolution: Mutations follow φ-scaling ({PHI_FLOAT})")
    
    print("\nPHI-HARMONIC OPTIMIZATIONS:")
    fib_series = [fibonacci(i) for i in range(1, 11)]
    print(f"  • Fibonacci Sequence: {', '.join(map(str, fib_series))}")
    print("  • Resonance Calculation: (φ · x) % 1")
    print("  • Perfect Resonance Rating: 0.6 ≤ φ-factor ≤ 0.64")
    
    print("\nQUANTUM INTEGRATION:")
    print("  • QR Genome with phi-optimized Tower of Hanoi codons")
    print("  • Phi-harmonic evolution of genome complexity and structure")
    print("  • Self-adapting resonance targeting across generations")
    
    print("\nUSAGE:")
    print("  --create-phi    : Create a new phi-optimized genome")
    print("  --execute-phi   : Execute a phi-optimized genome")
    print("  --evolve-phi    : Evolve a phi-optimized genome")
    print("  --generate-phi  : Generate QR sequence from phi-optimized genome")
    print("  --phi-cycle     : Run a complete phi-optimized cycle")
    print("  --complexity N  : Set complexity level (1-5, default: 3)")
    
    print("\n" + "="*60)

def main():
    """Main function to run the Phi-Harmonic QR DNA system"""
    parser = argparse.ArgumentParser(
        description="Quantum Phi-Harmonic QR DNA System Runner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_qr_system_phi.py --info                  # Show system information
  python run_qr_system_phi.py --create-phi            # Create a phi-optimized genome
  python run_qr_system_phi.py --execute-phi           # Execute phi-optimized genome
  python run_qr_system_phi.py --evolve-phi            # Evolve phi-optimized genome
  python run_qr_system_phi.py --generate-phi          # Generate phi QR sequence
  python run_qr_system_phi.py --phi-cycle             # Run full phi-optimized cycle
"""
    )
    
    # Base options (compatible with run_qr_system.py)
    parser.add_argument("--info", action="store_true", help="Show system information")
    
    # Phi-optimized options
    parser.add_argument("--create-phi", action="store_true", help="Create a phi-optimized genome")
    parser.add_argument("--execute-phi", action="store_true", help="Execute phi-optimized genome")
    parser.add_argument("--evolve-phi", action="store_true", help="Evolve phi-optimized genome")
    parser.add_argument("--generate-phi", action="store_true", help="Generate phi QR sequence")
    parser.add_argument("--phi-cycle", action="store_true", help="Run full phi-optimized cycle")
    
    # Parameters
    parser.add_argument("--genome", default="qr_phi_hanoi_genome.json", help="Genome file path")
    parser.add_argument("--output", default="qr_phi_hanoi_sequence", help="Output directory for QR sequence")
    parser.add_argument("--complexity", type=int, default=3, help="Complexity level (1-5)")
    
    args = parser.parse_args()
    
    # Check if any action is specified
    if not any([
        args.info, args.create_phi, args.execute_phi, args.evolve_phi,
        args.generate_phi, args.phi_cycle
    ]):
        print_phi_system_info()
        parser.print_help()
        return
    
    # Setup environment
    if not setup_environment():
        return
    
    # Run requested actions
    if args.info:
        print_phi_system_info()
    
    if args.create_phi:
        create_phi_genome(args.complexity)
    
    if args.execute_phi:
        execute_phi_genome(args.genome)
    
    if args.evolve_phi:
        evolve_phi_genome(args.genome)
    
    if args.generate_phi:
        generate_phi_sequence(args.genome, args.output)
    
    if args.phi_cycle:
        run_phi_full_cycle(args.complexity)

if __name__ == "__main__":
    print("Quantum Phi-Harmonic QR DNA System Runner")
    print("By Vaughn Scott - Extended with Quantum Optimization")
    main()
