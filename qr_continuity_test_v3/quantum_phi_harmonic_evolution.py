#!/usr/bin/env python3
"""
Quantum Phi-Harmonic Evolution System
Integrates phi-harmonic principles with the QR Genome Engine for advanced evolution
"""

import os
import sys
import json
import time
import uuid
from datetime import datetime

# Import our components
from quantum_phi_genome_enhancer import QuantumPhiGenomeEnhancer
from quantum_phi_generation_tracker import QuantumPhiGenerationTracker
from qr_genome_engine import QRGenomeEngine

class QuantumPhiHarmonicEvolution:
    """
    Quantum Phi-Harmonic Evolution System
    Integrates phi-harmonic principles with the QR Genome Engine for advanced evolution
    Uses golden ratio (φ) mathematics for optimized evolution and self-replication
    """
    
    def __init__(self, genome_file="qr_genome.json", memory_file="qr_epigenetic_memory.json", debug=False):
        """
        Initialize the Quantum Phi-Harmonic Evolution System
        
        Args:
            genome_file: Path to the genome file
            memory_file: Path to the epigenetic memory file
            debug: Whether to enable debug output
        """
        self.genome_file = genome_file
        self.memory_file = memory_file
        self.debug = debug
        
        # Golden ratio constants
        self.phi = (1 + 5**0.5) / 2  # φ ≈ 1.618034
        self.phi_inverse = 1 / self.phi  # φ⁻¹ ≈ 0.618034
        self.phi_squared = self.phi * self.phi  # φ² ≈ 2.618034
        
        # Initialize components
        self.genome_engine = QRGenomeEngine(
            genome_file=genome_file,
            memory_file=memory_file
        )
        
        self.enhancer = QuantumPhiGenomeEnhancer(
            genome_engine=self.genome_engine,
            debug=debug
        )
        
        self.generation_tracker = QuantumPhiGenerationTracker(
            genome_file=genome_file
        )
        
        # Load initial state
        self.initial_generation = self.generation_tracker.get_current_generation()
        self.phi_time = time.time() * self.phi
        self.phi_resonance = self.phi_time % 1
        
        if self.debug:
            print(f"Quantum Phi-Harmonic Evolution System initialized")
            print(f"Initial generation: {self.initial_generation}")
            print(f"Phi-Time: {self.phi_time}")
            print(f"Phi-Resonance: {self.phi_resonance:.6f}")
    
    def run_evolution_cycle(self, execute=True, evolve=True, add_replication=False):
        """
        Run a complete evolution cycle
        
        Args:
            execute: Whether to execute the genome
            evolve: Whether to evolve the genome
            add_replication: Whether to add self-replication capabilities
            
        Returns:
            Dictionary with evolution results
        """
        results = {
            "cycle_start_time": datetime.now().isoformat(),
            "initial_generation": self.initial_generation,
            "execution_results": None,
            "evolution_results": None,
            "replication_added": False,
            "final_generation": None
        }
        
        # Add self-replication if requested
        if add_replication:
            self.enhancer.add_self_replication_to_genome()
            results["replication_added"] = True
            if self.debug:
                print(f"Added self-replication capabilities to genome")
        
        # Execute genome with enhanced metrics if requested
        if execute:
            execution_results = self.enhancer.run_enhanced_genome_execution()
            results["execution_results"] = execution_results
            if self.debug:
                self.enhancer.print_enhanced_execution_summary(execution_results)
        
        # Evolve genome with quantum phi-harmonic principles if requested
        if evolve:
            # Calculate phi-harmonic metrics
            phi_time = time.time() * self.phi
            phi_resonance = phi_time % 1
            
            # Determine optimal mutation rate based on phi-resonance
            # Higher resonance (closer to phi_inverse) means higher mutation rate
            resonance_factor = 1 - abs(phi_resonance - self.phi_inverse)
            mutation_rate = 0.05 + (resonance_factor * 0.15)  # Range: 0.05 to 0.20
            
            # Apply enhanced evolution
            mutations, metrics = self.enhancer.enhance_genome_evolution(mutation_rate)
            
            # Increment generation with phi-harmonic principles
            new_gen = self.generation_tracker.increment_generation(metrics["phi_resonance"])
            
            # Record evolution results
            results["evolution_results"] = {
                "mutations": mutations,
                "phi_resonance": metrics["phi_resonance"],
                "quantum_resonance": metrics["resonance"],
                "quantum_complexity": metrics["complexity"],
                "mutation_rate": mutation_rate,
                "resonance_factor": resonance_factor,
                "generation_before": self.initial_generation,
                "generation_after": new_gen
            }
            
            if self.debug:
                print(f"\nEVOLUTION RESULTS:")
                print(f"  Applied {mutations} quantum phi-harmonic mutations")
                print(f"  Mutation rate: {mutation_rate:.6f}")
                print(f"  Phi-resonance: {metrics['phi_resonance']:.6f}")
                print(f"  Quantum resonance: {metrics['resonance']:.6f}")
                print(f"  Quantum complexity: {metrics['complexity']:.6f}")
                print(f"  Generation: {self.initial_generation} → {new_gen}")
        
        # Get final generation
        results["final_generation"] = self.generation_tracker.get_current_generation()
        results["total_generations_added"] = results["final_generation"] - results["initial_generation"]
        
        return results
    
    def run_multi_cycle_evolution(self, cycles=5, execute=True, evolve=True, add_replication=False):
        """
        Run multiple evolution cycles
        
        Args:
            cycles: Number of evolution cycles to run
            execute: Whether to execute the genome in each cycle
            evolve: Whether to evolve the genome in each cycle
            add_replication: Whether to add self-replication capabilities (first cycle only)
            
        Returns:
            Dictionary with multi-cycle evolution results
        """
        multi_cycle_results = {
            "start_time": datetime.now().isoformat(),
            "cycles": [],
            "initial_generation": self.generation_tracker.get_current_generation(),
            "final_generation": None,
            "total_generations_added": 0
        }
        
        print(f"Initial generation: {multi_cycle_results['initial_generation']}")
        
        # Run cycles
        for cycle in range(1, cycles + 1):
            print(f"\n{'='*60}")
            print(f"RUNNING CYCLE {cycle}/{cycles}")
            print(f"{'='*60}")
            
            cycle_start = time.time()
            
            # Add replication only in the first cycle if requested
            add_replication_this_cycle = add_replication and cycle == 1
            
            # Run evolution cycle
            cycle_results = self.run_evolution_cycle(
                execute=execute,
                evolve=evolve,
                add_replication=add_replication_this_cycle
            )
            
            # Add cycle duration
            cycle_results["duration"] = time.time() - cycle_start
            multi_cycle_results["cycles"].append(cycle_results)
            
            # Print cycle summary
            print(f"\nCYCLE {cycle} SUMMARY:")
            print(f"  Duration: {cycle_results['duration']:.2f} seconds")
            
            if cycle_results["replication_added"]:
                print(f"  Added self-replication capabilities")
                
            if cycle_results["execution_results"]:
                exec_results = cycle_results["execution_results"]
                print(f"  Execution success rate: {exec_results['success_rate']:.2f}%")
                print(f"  Execution duration: {exec_results['duration']:.2f} seconds")
            
            if cycle_results["evolution_results"]:
                evo_results = cycle_results["evolution_results"]
                print(f"  Mutations applied: {evo_results['mutations']}")
                print(f"  Phi-resonance: {evo_results['phi_resonance']:.6f}")
                print(f"  Quantum resonance: {evo_results['quantum_resonance']:.6f}")
                print(f"  Quantum complexity: {evo_results['quantum_complexity']:.6f}")
                print(f"  Generation: {evo_results['generation_before']} → {evo_results['generation_after']}")
        
        # Calculate final results
        multi_cycle_results["final_generation"] = self.generation_tracker.get_current_generation()
        multi_cycle_results["total_generations_added"] = multi_cycle_results["final_generation"] - multi_cycle_results["initial_generation"]
        multi_cycle_results["total_duration"] = sum(cycle["duration"] for cycle in multi_cycle_results["cycles"])
        
        # Print final summary
        print(f"\n{'='*60}")
        print(f"FINAL SUMMARY")
        print(f"{'='*60}")
        print(f"Initial generation: {multi_cycle_results['initial_generation']}")
        print(f"Final generation: {multi_cycle_results['final_generation']}")
        print(f"Total generations added: {multi_cycle_results['total_generations_added']}")
        print(f"Total runtime: {multi_cycle_results['total_duration']:.2f} seconds")
        
        return multi_cycle_results


# Command-line interface
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Quantum Phi-Harmonic Evolution System")
    parser.add_argument("--cycles", type=int, default=5, help="Number of evolution cycles to run")
    parser.add_argument("--execute", action="store_true", help="Execute the genome in each cycle")
    parser.add_argument("--evolve", action="store_true", help="Evolve the genome in each cycle")
    parser.add_argument("--add-replication", action="store_true", help="Add self-replication capabilities (first cycle only)")
    parser.add_argument("--genome-file", default="qr_genome.json", help="Path to genome file")
    parser.add_argument("--memory-file", default="qr_epigenetic_memory.json", help="Path to epigenetic memory file")
    parser.add_argument("--debug", action="store_true", help="Enable debug output")
    args = parser.parse_args()
    
    # Default to execute and evolve if neither is specified
    if not args.execute and not args.evolve:
        args.execute = True
        args.evolve = True
    
    # Create evolution system
    evolution_system = QuantumPhiHarmonicEvolution(
        genome_file=args.genome_file,
        memory_file=args.memory_file,
        debug=args.debug
    )
    
    # Run multi-cycle evolution
    results = evolution_system.run_multi_cycle_evolution(
        cycles=args.cycles,
        execute=args.execute,
        evolve=args.evolve,
        add_replication=args.add_replication
    )
    
    # Save results
    results_file = f"phi_harmonic_evolution_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(results_file, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {results_file}")
