#!/usr/bin/env python3
"""
QR Genome Robust Integration - Part of Animated QR Flipbook DNA System
By Vaughn Scott

Integrates the QR Robust Generator with the QR Genome Engine to ensure reliable
QR sequence generation with phi-harmonic principles.
"""

import os
import sys
import json
import math
import time
from datetime import datetime

# Import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from qr_robust_generator import QRRobustGenerator
from qr_genome_engine import QRGenomeEngine
from qr_task_executor import QRTaskExecutor
from qr_epigenetic_memory import QREpigeneticMemory

# Phi (Golden Ratio) constant
PHI = (1 + math.sqrt(5)) / 2  # Approximately 1.618034

class QRGenomeRobustIntegration:
    """
    Integrates the QR Robust Generator with the QR Genome Engine to ensure reliable
    QR sequence generation with phi-harmonic principles.
    """
    
    def __init__(self, output_dir="qr_genome_sequence", genome_file="qr_genome.json", 
                 memory_file="qr_epigenetic_memory.json", debug=False):
        """
        Initialize the QR Genome Robust Integration.
        
        Args:
            output_dir: Directory to save generated QR code frames
            genome_file: Path to the genome file
            memory_file: Path to the epigenetic memory file
            debug: Enable debug output
        """
        self.output_dir = output_dir
        self.genome_file = genome_file
        self.memory_file = memory_file
        self.debug = debug
        
        # Create robust QR generator
        self.robust_generator = QRRobustGenerator(output_dir=output_dir)
        
        # Initialize QR genome engine components
        self.memory = QREpigeneticMemory(memory_file=memory_file)
        self.executor = QRTaskExecutor()
        self.engine = QRGenomeEngine()
        self.engine.executor = self.executor
        self.engine.memory = self.memory
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
    
    def load_genome(self):
        """
        Load the genome from file.
        
        Returns:
            True if successful, False otherwise
        """
        try:
            # Set the genome file path in the engine
            self.engine.genome_file = self.genome_file
            # Call the load_genome method without arguments
            self.engine.load_genome()
            return True
        except Exception as e:
            print(f"Error loading genome: {e}")
            return False
    
    def execute_genome(self):
        """
        Execute the genome.
        
        Returns:
            Execution results
        """
        if self.debug:
            print(f"Executing genome...")
        
        start_time = time.time()
        results = self.engine.run_genome_execution()
        execution_time = time.time() - start_time
        
        # Process results - ensure we have consistent format
        processed_results = {
            'total_count': 0,
            'success_count': 0,
            'phi_resonance': 0.0
        }
        
        # Extract results if available
        if isinstance(results, dict):
            processed_results['total_count'] = results.get('total_codons', 0)
            processed_results['success_count'] = results.get('successful_executions', 0)
            processed_results['phi_resonance'] = results.get('phi_resonance', 0.0)
        
        if self.debug:
            print(f"Genome execution completed in {execution_time:.2f} seconds")
            print(f"Successful executions: {processed_results['success_count']}/{processed_results['total_count']}")
        
        return processed_results
    
    def evolve_genome(self):
        """
        Evolve the genome.
        
        Returns:
            Evolution results
        """
        if self.debug:
            print(f"Evolving genome...")
        
        start_time = time.time()
        results = self.engine.evolve_genome()
        evolution_time = time.time() - start_time
        
        # Process results - ensure we have consistent format
        processed_results = {
            'new_generation': 0,
            'mutation_count': 0,
            'phi_resonance': 0.0
        }
        
        # Extract results if available
        if isinstance(results, dict):
            processed_results['new_generation'] = results.get('generation', 0)
            processed_results['mutation_count'] = results.get('mutations', 0)
            processed_results['phi_resonance'] = results.get('phi_resonance', 0.0)
        
        if self.debug:
            print(f"Genome evolution completed in {evolution_time:.2f} seconds")
            print(f"New generation: {processed_results['new_generation']}")
            print(f"Mutations: {processed_results['mutation_count']}")
        
        return processed_results
    
    def generate_qr_sequence(self):
        """
        Generate QR sequence using the robust generator.
        
        Returns:
            List of paths to generated QR images
        """
        if self.debug:
            print(f"Generating QR sequence...")
        
        start_time = time.time()
        
        # Get genome from engine
        genome = self.engine.genome
        
        # Generate QR sequence
        paths = self.robust_generator.generate_from_genome(genome, output_dir=self.output_dir)
        
        generation_time = time.time() - start_time
        
        if self.debug:
            print(f"QR sequence generation completed in {generation_time:.2f} seconds")
            print(f"Generated {len(paths)} QR code files")
        
        return paths
    
    def run_full_cycle(self):
        """
        Run a full cycle of genome execution, evolution, and QR sequence generation.
        
        Returns:
            Results dictionary
        """
        results = {
            "timestamp": datetime.now().isoformat(),
            "execution": None,
            "evolution": None,
            "qr_sequence": None
        }
        
        # Load genome
        if not self.load_genome():
            return results
        
        # Execute genome
        execution_results = self.execute_genome()
        results["execution"] = execution_results
        
        # Evolve genome
        evolution_results = self.evolve_genome()
        results["evolution"] = evolution_results
        
        # Generate QR sequence
        qr_paths = self.generate_qr_sequence()
        results["qr_sequence"] = {
            "count": len(qr_paths),
            "output_dir": self.output_dir
        }
        
        return results
    
    def generate_summary(self, results):
        """
        Generate a summary of the full cycle results.
        
        Args:
            results: Results from run_full_cycle
            
        Returns:
            Summary string
        """
        summary = []
        summary.append("QR Flipbook DNA System - Full Cycle Summary")
        summary.append("=" * 50)
        summary.append(f"Timestamp: {results['timestamp']}")
        summary.append("")
        
        if results["execution"]:
            summary.append("Genome Execution:")
            summary.append(f"  Success rate: {results['execution']['success_count']}/{results['execution']['total_count']}")
            summary.append(f"  Phi resonance: {results['execution'].get('phi_resonance', 'N/A')}")
            summary.append("")
        
        if results["evolution"]:
            summary.append("Genome Evolution:")
            summary.append(f"  New generation: {results['evolution']['new_generation']}")
            summary.append(f"  Mutation count: {results['evolution'].get('mutation_count', 'N/A')}")
            summary.append("")
        
        if results["qr_sequence"]:
            summary.append("QR Sequence Generation:")
            summary.append(f"  Generated frames: {results['qr_sequence']['count']}")
            summary.append(f"  Output directory: {results['qr_sequence']['output_dir']}")
            summary.append("")
        
        return "\n".join(summary)

# Example usage
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="QR Genome Robust Integration")
    parser.add_argument("--output-dir", default="qr_genome_sequence", help="Output directory for QR sequence")
    parser.add_argument("--genome-file", default="qr_genome.json", help="Path to genome file")
    parser.add_argument("--memory-file", default="qr_epigenetic_memory.json", help="Path to epigenetic memory file")
    parser.add_argument("--debug", action="store_true", help="Enable debug output")
    args = parser.parse_args()
    
    # Create integration
    integration = QRGenomeRobustIntegration(
        output_dir=args.output_dir,
        genome_file=args.genome_file,
        memory_file=args.memory_file,
        debug=args.debug
    )
    
    # Run full cycle
    results = integration.run_full_cycle()
    
    # Print summary
    print(integration.generate_summary(results))
