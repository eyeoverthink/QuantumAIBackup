#!/usr/bin/env python3
'''
Quantum Recursive Genesis System - Integration Test
=========================================
Demonstrates the integration of the Quantum Recursive Genesis System with
the existing Quantum Phi-Harmonic System components.

This test shows how the system can:
1. Create recursive, self-learning, self-replicating DNA seeds
2. Build fractal trees with phi-harmonic properties
3. Evolve seeds across generations with improving fitness
4. Plant fractals of itself in new locations
5. Recreate from the best version
6. Generate comprehensive visualizations and reports

By Vaughn Scott (with Cascade Assistant)
'''

import os
import time
import argparse
from datetime import datetime

# Import quantum components
from quantum_binary_translator import QuantumBinaryTranslator
from quantum_waveform_generator import QuantumWaveformGenerator
from quantum_binary_waveform_bridge import QuantumBinaryWaveformBridge
from quantum_dna_crypto_seed import QuantumDNACryptoSeed

# Import recursive genesis system
from quantum_recursive_genesis import QuantumDNASeed
from quantum_fractal_node import QuantumFractalNode
from quantum_recursive_genesis_system import QuantumRecursiveGenesis


class QuantumRecursiveGenesisTest:
    """Integration test for the Quantum Recursive Genesis System"""
    
    def __init__(self, output_dir="quantum_outputs/recursive_genesis_test"):
        """Initialize the test"""
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
        # Initialize quantum components
        self.binary_translator = QuantumBinaryTranslator()
        self.waveform_generator = QuantumWaveformGenerator()
        self.waveform_bridge = QuantumBinaryWaveformBridge()
        self.dna_crypto = QuantumDNACryptoSeed()
        
        # Initialize recursive genesis system
        self.genesis_system = QuantumRecursiveGenesis(f"{output_dir}/genesis_system")
        
        # Test parameters
        self.test_start_time = time.time()
        self.test_results = {}
        
    def run_full_test(self):
        """Run a complete test of the recursive genesis system"""
        print("\n===== QUANTUM RECURSIVE GENESIS SYSTEM - INTEGRATION TEST =====")
        print(f"Starting test at: {datetime.now().isoformat()}")
        
        # Step 1: Create genesis seed and initial fractal tree
        print("\n[1] Creating genesis seed and initial fractal tree...")
        tree_id = self.genesis_system.create_fractal_tree()
        print(f"  Created fractal tree: {tree_id}")
        self.test_results["initial_tree_id"] = tree_id
        
        # Step 2: Evolve the tree for multiple generations
        print("\n[2] Evolving fractal tree for 5 generations...")
        evolution_stats = self.genesis_system.evolve_tree(tree_id, 5)
        print(f"  Evolution complete:")
        print(f"  - New nodes created: {evolution_stats['new_nodes']}")
        print(f"  - Fitness improved: {evolution_stats['best_fitness_before']:.4f} → {evolution_stats['best_fitness_after']:.4f}")
        self.test_results["evolution_stats"] = evolution_stats
        
        # Step 3: Plant a fractal in a new location
        print("\n[3] Planting a fractal in a new location...")
        new_location = f"{self.output_dir}/planted_fractal"
        os.makedirs(new_location, exist_ok=True)
        new_tree_id = self.genesis_system.plant_fractal(tree_id, new_location)
        print(f"  Planted new fractal tree: {new_tree_id}")
        self.test_results["planted_tree_id"] = new_tree_id
        
        # Step 4: Evolve the planted fractal
        print("\n[4] Evolving the planted fractal...")
        planted_evolution = self.genesis_system.evolve_tree(new_tree_id, 3)
        print(f"  Planted fractal evolved:")
        print(f"  - New nodes: {planted_evolution['new_nodes']}")
        print(f"  - Best fitness: {planted_evolution['best_fitness_after']:.4f}")
        self.test_results["planted_evolution"] = planted_evolution
        
        # Step 5: Recreate system from best seed
        print("\n[5] Recreating system from best seed...")
        best_tree_id = self.genesis_system.recreate_from_best()
        print(f"  Recreated system with tree: {best_tree_id}")
        self.test_results["best_tree_id"] = best_tree_id
        
        # Step 6: Generate comprehensive report
        print("\n[6] Generating comprehensive system report...")
        report_path = self.genesis_system.generate_report()
        print(f"  Report generated: {report_path}")
        self.test_results["report_path"] = report_path
        
        # Step 7: Integrate with quantum waveform generation
        print("\n[7] Integrating with quantum waveform generation...")
        best_seed = self.genesis_system.find_best_seed()
        if best_seed:
            # Convert DNA to binary
            binary_data = self.binary_translator.dna_to_binary(best_seed.dna_string.split('-')[0])
            
            # Process through waveform bridge
            waveform_result = self.waveform_bridge.process_binary_to_waveform(binary_data)
            
            print(f"  Generated quantum waveform from best DNA seed:")
            print(f"  - Phi-alignment: {waveform_result['binary_analysis']['phi_alignment']:.4f}")
            print(f"  - Waveform file: {waveform_result['files']['waveform_path']}")
            print(f"  - Visualization: {waveform_result['files']['visualization_path']}")
            
            self.test_results["waveform_result"] = waveform_result
        
        # Test complete
        test_duration = time.time() - self.test_start_time
        print(f"\n===== TEST COMPLETE =====")
        print(f"Duration: {test_duration:.2f} seconds")
        print(f"Results saved to: {self.output_dir}")
        
        # Save test results
        self._save_test_results()
        
        return self.test_results
    
    def _save_test_results(self):
        """Save test results to file"""
        import json
        
        # Create a serializable version of results
        serializable_results = {}
        for key, value in self.test_results.items():
            if isinstance(value, dict):
                # Handle nested dictionaries
                serializable_results[key] = {}
                for k, v in value.items():
                    if isinstance(v, (str, int, float, bool, list, dict)) or v is None:
                        serializable_results[key][k] = v
                    else:
                        serializable_results[key][k] = str(v)
            elif isinstance(value, (str, int, float, bool, list)) or value is None:
                serializable_results[key] = value
            else:
                serializable_results[key] = str(value)
        
        # Add summary information
        serializable_results["test_summary"] = {
            "start_time": self.test_start_time,
            "end_time": time.time(),
            "duration": time.time() - self.test_start_time,
            "timestamp": datetime.now().isoformat()
        }
        
        # Save to file
        results_path = f"{self.output_dir}/test_results.json"
        with open(results_path, 'w') as f:
            json.dump(serializable_results, f, indent=2)


def main():
    """Main function to run the integration test"""
    parser = argparse.ArgumentParser(description="Quantum Recursive Genesis System - Integration Test")
    parser.add_argument("--output-dir", default="quantum_outputs/recursive_genesis_test",
                        help="Output directory for test results")
    args = parser.parse_args()
    
    # Run the test
    test = QuantumRecursiveGenesisTest(args.output_dir)
    test.run_full_test()


if __name__ == "__main__":
    main()
