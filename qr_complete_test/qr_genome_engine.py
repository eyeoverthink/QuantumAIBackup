#!/usr/bin/env python3
"""
QR Genome Engine - Part of Animated QR Flipbook DNA System
By Vaughn Scott

Main executor for the QR DNA system that orchestrates:
- Loading and executing QR genome codons
- Managing epigenetic memory
- Handling phi-harmonic evolution
- Generating response QR codes
"""

import os
import sys
import json
import math
import time
import uuid
import numpy as np
from datetime import datetime

# Import QR DNA system components
from qr_epigenetic_memory import QREpigeneticMemory
from qr_codon_groups import QRGenome, QRCodonGroup, QRCodon
from qr_task_executor import QRTaskExecutor

# Phi (Golden Ratio) constant
PHI = (1 + np.sqrt(5)) / 2  # Approximately 1.618034

class QRGenomeEngine:
    """
    Main engine for executing QR DNA genomes with phi-harmonic evolution.
    """
    
    def __init__(self, genome_file="qr_genome.json", memory_file="qr_epigenetic_memory.json", debug=False):
        """
        Initialize the QR Genome Engine.
        
        Args:
            genome_file: Path to genome file
            memory_file: Path to memory file
            debug: Whether to print debug information
        """
        self.genome_file = genome_file
        self.memory_file = memory_file
        self.debug = debug
        
        # Initialize components
        self.memory = QREpigeneticMemory(memory_file)
        self.executor = QRTaskExecutor(debug=debug)
        self.genome = None
        
        # Load genome if it exists
        self.load_genome()
        
        if self.debug:
            print(f"QR Genome Engine initialized")
            if self.genome:
                print(f"Loaded genome: {self.genome.genome_name} (Generation {self.genome.generation})")
    
    def load_genome(self):
        """Load genome from file."""
        self.genome = QRGenome.load_from_file(self.genome_file)
        if not self.genome and self.debug:
            print(f"No genome found at {self.genome_file}")
    
    def create_basic_genome(self):
        """Create a basic genome if none exists."""
        if self.genome is None:
            from qr_codon_groups import create_basic_genome
            self.genome = create_basic_genome()
            self.genome.save_to_file(self.genome_file)
            if self.debug:
                print(f"Created basic genome: {self.genome.genome_name}")
    
    def run_genome_execution(self):
        """
        Execute the entire genome, processing each codon in sequence.
        
        Returns:
            Dictionary containing execution results
        """
        if not self.genome:
            self.create_basic_genome()
        
        if self.debug:
            print(f"\nExecuting genome: {self.genome.genome_name} (Generation {self.genome.generation})")
        
        execution_results = {
            "genome_id": self.genome.genome_id,
            "genome_name": self.genome.genome_name,
            "generation": self.genome.generation,
            "start_time": datetime.now().isoformat(),
            "groups_executed": 0,
            "codons_executed": 0,
            "successful_executions": 0,
            "failed_executions": 0,
            "group_results": []
        }
        
        # Process each group in the genome
        for group_idx, group in enumerate(self.genome.groups):
            if self.debug:
                print(f"\nExecuting group {group_idx+1}/{len(self.genome.groups)}: {group.group_type}")
            
            group_result = {
                "group_id": group.group_id,
                "group_type": group.group_type,
                "codons_executed": 0,
                "successful_codons": 0,
                "codon_results": []
            }
            
            # Process each codon in the group
            for codon_idx, codon in enumerate(group.codons):
                if self.debug:
                    print(f"  Executing codon {codon_idx+1}/{len(group.codons)}: {codon.codon_type}")
                
                # Get task type and data
                task_type = codon.frame_data.get("task_type", "execute_python")
                task_data = codon.frame_data.get("task_data", {})
                
                # Execute the task
                success, output = self.executor.execute_task(task_type, task_data)
                
                # Calculate phi-harmonic metrics
                phi_metrics = self.executor.calculate_phi_metrics(success, self.executor.last_execution_time)
                
                # Create phi state for this execution
                phi_state = {
                    "generation": self.genome.generation,
                    "complexity": phi_metrics["complexity"],
                    "resonance": phi_metrics["resonance"]
                }
                
                # Update codon with execution results
                codon.update_from_execution(success, phi_state)
                
                # Record execution in memory
                self.memory.record_execution(
                    session_id=self.genome.genome_id,
                    frame_number=codon.codon_id,
                    task_type=task_type,
                    success=success,
                    output=output,
                    phi_metadata=phi_state
                )
                
                # Update group result
                group_result["codons_executed"] += 1
                if success:
                    group_result["successful_codons"] += 1
                
                # Record codon result
                codon_result = {
                    "codon_id": codon.codon_id,
                    "codon_type": codon.codon_type,
                    "task_type": task_type,
                    "success": success,
                    "output_length": len(output) if output else 0,
                    "phi_state": phi_state
                }
                group_result["codon_results"].append(codon_result)
                
                # Update execution results
                execution_results["codons_executed"] += 1
                if success:
                    execution_results["successful_executions"] += 1
                else:
                    execution_results["failed_executions"] += 1
            
            # Update group phi state
            group.update_phi_state()
            
            # Record group execution
            group.record_execution(
                group_result["successful_codons"] > 0,
                self.genome.phi_state
            )
            
            # Add group result to execution results
            execution_results["groups_executed"] += 1
            execution_results["group_results"].append(group_result)
        
        # Update genome phi state
        self.genome.update_phi_state()
        
        # Record end time
        execution_results["end_time"] = datetime.now().isoformat()
        execution_results["duration"] = (
            datetime.fromisoformat(execution_results["end_time"]) - 
            datetime.fromisoformat(execution_results["start_time"])
        ).total_seconds()
        
        # Calculate success rate
        if execution_results["codons_executed"] > 0:
            execution_results["success_rate"] = execution_results["successful_executions"] / execution_results["codons_executed"]
        else:
            execution_results["success_rate"] = 0.0
        
        # Save genome
        self.genome.save_to_file(self.genome_file)
        
        if self.debug:
            print(f"\nGenome execution complete:")
            print(f"  Codons executed: {execution_results['codons_executed']}")
            print(f"  Success rate: {execution_results['success_rate']:.2%}")
            print(f"  Duration: {execution_results['duration']:.2f} seconds")
        
        return execution_results
    
    def evolve_genome(self, mutation_rate=None):
        """
        Apply phi-harmonic evolution to the genome.
        
        Args:
            mutation_rate: Optional override for mutation rate
            
        Returns:
            Number of mutations applied
        """
        if not self.genome:
            self.create_basic_genome()
        
        # Get optimal phi state from memory
        optimal_state = self.memory.get_optimal_phi_state()
        
        # Apply mutations
        mutations = self.genome.mutate(mutation_rate)
        
        if mutations > 0:
            # Record mutation in memory
            self.memory.record_mutation(
                mutation_type="phi_harmonic",
                source_state=self.genome.phi_state,
                target_state=optimal_state,
                success_rate=self.executor.get_execution_summary()["success_rate"]
            )
            
            # Save genome
            self.genome.save_to_file(self.genome_file)
            
            if self.debug:
                print(f"Applied {mutations} mutations to genome")
                print(f"New generation: {self.genome.generation}")
        
        return mutations
    
    def generate_qr_sequence(self, output_dir="qr_genome_sequence", frames=12):
        """
        Generate a QR code sequence from the genome.
        
        Args:
            output_dir: Directory to save QR code images
            frames: Number of frames to generate
            
        Returns:
            Path to the generated sequence directory
        """
        if not self.genome:
            self.create_basic_genome()
        
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        # Import QR sequence generator
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        from qr_sequence_generator import QRSequenceGenerator
        
        # Flatten codons into a list
        codons = []
        for group in self.genome.groups:
            for codon in group.codons:
                codons.append(codon)
        
        # Generate QR sequence
        if len(codons) > 0:
            # Use codons as templates for QR frames
            generator = QRSequenceGenerator(output_dir=output_dir)
            
            # Generate QR codes for each codon
            for i in range(min(frames, len(codons))):
                codon = codons[i]
                code = codon.frame_data.get("task_data", {}).get("code", "")
                task_type = codon.frame_data.get("task_type", "execute_python")
                
                # Create payload from codon data
                payload = json.dumps({
                    "code": code,
                    "task_type": task_type,
                    "codon_id": codon.codon_id,
                    "codon_type": codon.codon_type,
                    "phi_state": codon.phi_state,
                    "generation": self.genome.generation
                })
                
                # Generate QR code with payload
                generator.generate_qr_frame(payload=payload, frame_number=i+1)
            
            sequence_dir = output_dir
        else:
            # Generate default sequence
            generator = QRSequenceGenerator(output_dir=output_dir)
            
            # Generate default QR frames
            for i in range(frames):
                # Generate a default code fragment
                default_code = generator.generate_code_fragment()
                
                # Create a default payload
                payload = json.dumps({
                    "code": default_code,
                    "task_type": "execute_python",
                    "generation": self.genome.generation if self.genome else 1
                })
                
                # Generate QR code with payload
                generator.generate_qr_frame(payload=payload, frame_number=i+1)
                
            sequence_dir = output_dir
        
        if self.debug:
            print(f"Generated QR sequence in {sequence_dir}")
        
        return sequence_dir
        
    def print_execution_summary(self, results):
        """
        Print a summary of execution results.
        
        Args:
            results: Execution results from run_genome_execution
        """
        print("\n" + "="*60)
        print(f"QR GENOME EXECUTION SUMMARY")
        print("="*60)
        
        print(f"\nGenome: {results['genome_name']} (Generation {results['generation']})")
        print(f"Executed: {results['codons_executed']} codons in {results['groups_executed']} groups")
        print(f"Success rate: {results['success_rate']:.2%} ({results['successful_executions']}/{results['codons_executed']})")
        print(f"Duration: {results['duration']:.2f} seconds")
        
        print("\nGROUP RESULTS:")
        for group_result in results['group_results']:
            success_rate = group_result['successful_codons'] / group_result['codons_executed'] if group_result['codons_executed'] > 0 else 0
            print(f"  {group_result['group_type']}: {success_rate:.2%} success ({group_result['successful_codons']}/{group_result['codons_executed']})")
        
        print("\nPHI-HARMONIC STATE:")
        if self.genome:
            print(f"  Complexity: {self.genome.phi_state['complexity']:.6f}")
            print(f"  Resonance: {self.genome.phi_state['resonance']:.6f}")
            print(f"  Generation: {self.genome.phi_state['generation']}")
        
        print("\n" + "="*60)
    
    def cleanup(self):
        """Clean up resources."""
        self.executor.cleanup()

def main():
    """Main function to run the QR Genome Engine."""
    import argparse
    
    parser = argparse.ArgumentParser(description="QR Genome Engine")
    parser.add_argument("--genome", default="qr_genome.json", help="Genome file path")
    parser.add_argument("--memory", default="qr_epigenetic_memory.json", help="Memory file path")
    parser.add_argument("--execute", action="store_true", help="Execute the genome")
    parser.add_argument("--evolve", action="store_true", help="Evolve the genome")
    parser.add_argument("--generate", action="store_true", help="Generate QR sequence")
    parser.add_argument("--output", default="qr_genome_sequence", help="Output directory for QR sequence")
    parser.add_argument("--frames", type=int, default=12, help="Number of frames to generate")
    parser.add_argument("--debug", action="store_true", help="Enable debug output")
    
    args = parser.parse_args()
    
    # Create engine
    engine = QRGenomeEngine(
        genome_file=args.genome,
        memory_file=args.memory,
        debug=args.debug
    )
    
    # Execute genome if requested
    if args.execute:
        results = engine.run_genome_execution()
        engine.print_execution_summary(results)
    
    # Evolve genome if requested
    if args.evolve:
        mutations = engine.evolve_genome()
        print(f"Applied {mutations} mutations to genome")
        if mutations > 0:
            print(f"Advanced to generation {engine.genome.generation}")
    
    # Generate QR sequence if requested
    if args.generate:
        sequence_dir = engine.generate_qr_sequence(
            output_dir=args.output,
            frames=args.frames
        )
        print(f"Generated QR sequence in {sequence_dir}")
    
    # Print memory summary
    engine.memory.print_memory_summary()
    
    # Clean up
    engine.cleanup()

if __name__ == "__main__":
    print("QR Genome Engine - By Vaughn Scott")
    main()
