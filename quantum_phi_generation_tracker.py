#!/usr/bin/env python3
"""
Quantum Phi-Harmonic Generation Tracker
Manages generation tracking and evolution for the Quantum Phi-Harmonic Genome system
"""

import os
import json
import time
import uuid
from datetime import datetime

class QuantumPhiGenerationTracker:
    """
    Tracks and manages generations for the Quantum Phi-Harmonic Genome system.
    Uses golden ratio principles to ensure proper generation advancement.
    """
    
    def __init__(self, genome_file="qr_genome.json"):
        """
        Initialize the generation tracker.
        
        Args:
            genome_file: Path to the genome file
        """
        self.genome_file = genome_file
        self.phi = (1 + 5**0.5) / 2  # Golden ratio
        self.phi_inverse = 1 / self.phi
        
    def get_current_generation(self):
        """
        Get the current generation from the genome file.
        
        Returns:
            Current generation number
        """
        try:
            if os.path.exists(self.genome_file):
                with open(self.genome_file, 'r') as f:
                    genome_data = json.load(f)
                return genome_data.get("generation", 1)
            return 1
        except Exception as e:
            print(f"Error reading generation: {e}")
            return 1
            
    def increment_generation(self, phi_resonance=None):
        """
        Increment the generation in the genome file using phi-harmonic principles.
        
        Args:
            phi_resonance: Optional phi resonance value to determine increment amount
            
        Returns:
            New generation number
        """
        try:
            # Load current genome data
            if os.path.exists(self.genome_file):
                with open(self.genome_file, 'r') as f:
                    genome_data = json.load(f)
            else:
                print(f"Warning: Genome file not found at {self.genome_file}")
                return 1
                
            # Get current generation
            current_gen = genome_data.get("generation", 1)
            
            # Calculate phi-harmonic increment
            if phi_resonance is not None:
                # Use phi resonance to determine if we increment by 1 or 2
                # Higher resonance (closer to phi_inverse) means faster evolution
                if abs(phi_resonance - self.phi_inverse) < 0.2:
                    increment = 2  # Accelerated evolution near golden ratio inverse
                else:
                    increment = 1  # Normal evolution
            else:
                increment = 1
                
            # Update generation
            new_gen = current_gen + increment
            genome_data["generation"] = new_gen
            
            # Also update phi state if it exists
            if "phi_state" in genome_data:
                genome_data["phi_state"]["generation"] = new_gen
            
            # Save updated genome data
            with open(self.genome_file, 'w') as f:
                json.dump(genome_data, f, indent=2)
                
            print(f"Generation updated: {current_gen} → {new_gen}")
            return new_gen
            
        except Exception as e:
            print(f"Error incrementing generation: {e}")
            return None
            
    def run_evolution_epochs(self, epochs=5, phi_harmonic_enhancer=None):
        """
        Run multiple evolution epochs, tracking generation progression.
        
        Args:
            epochs: Number of epochs to run
            phi_harmonic_enhancer: Optional enhancer to use for evolution
            
        Returns:
            Dictionary with evolution results
        """
        results = {
            "start_time": datetime.now().isoformat(),
            "epochs": [],
            "initial_generation": self.get_current_generation(),
            "final_generation": None,
            "total_generations_added": 0
        }
        
        print(f"Initial generation: {results['initial_generation']}")
        
        # Run epochs
        for epoch in range(1, epochs + 1):
            print(f"\n{'='*60}")
            print(f"RUNNING EPOCH {epoch}/{epochs}")
            print(f"{'='*60}")
            
            epoch_start = time.time()
            epoch_result = {
                "epoch": epoch,
                "start_generation": self.get_current_generation()
            }
            
            # Increment generation with phi-harmonic principles
            if phi_harmonic_enhancer:
                # Use the enhancer for evolution
                try:
                    mutations, metrics = phi_harmonic_enhancer.enhance_genome_evolution()
                    epoch_result["mutations"] = mutations
                    epoch_result["phi_resonance"] = metrics["phi_resonance"]
                    epoch_result["quantum_resonance"] = metrics["resonance"]
                    epoch_result["quantum_complexity"] = metrics["complexity"]
                    
                    # Force generation increment
                    new_gen = self.increment_generation(metrics["phi_resonance"])
                    epoch_result["end_generation"] = new_gen
                except Exception as e:
                    print(f"Error in enhancer evolution: {e}")
                    epoch_result["error"] = str(e)
            else:
                # Simple generation increment
                new_gen = self.increment_generation()
                epoch_result["end_generation"] = new_gen
            
            # Record duration
            epoch_result["duration"] = time.time() - epoch_start
            results["epochs"].append(epoch_result)
            
            # Print epoch summary
            print(f"\nEPOCH {epoch} SUMMARY:")
            print(f"  Duration: {epoch_result['duration']:.2f} seconds")
            print(f"  Generation: {epoch_result['start_generation']} → {epoch_result['end_generation']}")
            if "phi_resonance" in epoch_result:
                print(f"  Phi-resonance: {epoch_result['phi_resonance']:.6f}")
                print(f"  Quantum resonance: {epoch_result['quantum_resonance']:.6f}")
                print(f"  Quantum complexity: {epoch_result['quantum_complexity']:.6f}")
        
        # Calculate final results
        results["final_generation"] = self.get_current_generation()
        results["total_generations_added"] = results["final_generation"] - results["initial_generation"]
        results["total_duration"] = sum(epoch["duration"] for epoch in results["epochs"])
        
        # Print final summary
        print(f"\n{'='*60}")
        print(f"FINAL SUMMARY")
        print(f"{'='*60}")
        print(f"Initial generation: {results['initial_generation']}")
        print(f"Final generation: {results['final_generation']}")
        print(f"Total generations added: {results['total_generations_added']}")
        print(f"Total runtime: {results['total_duration']:.2f} seconds")
        
        return results


# Command-line interface
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Quantum Phi-Harmonic Generation Tracker")
    parser.add_argument("--epochs", type=int, default=5, help="Number of evolution epochs to run")
    parser.add_argument("--genome-file", default="qr_genome.json", help="Path to genome file")
    args = parser.parse_args()
    
    tracker = QuantumPhiGenerationTracker(genome_file=args.genome_file)
    results = tracker.run_evolution_epochs(epochs=args.epochs)
    
    # Save results
    with open("phi_generation_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to phi_generation_results.json")
