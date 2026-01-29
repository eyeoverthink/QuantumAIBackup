#!/usr/bin/env python3
"""
QR Integrated System - Combining QR Flipbook DNA with Recursive Self-Adaptive QR
By Vaughn Scott

This module integrates the existing QR Flipbook DNA System with the new 
Recursive Self-Adaptive QR System, creating a unified workflow that leverages
phi-harmonic principles, quantum optimization, and recursive self-improvement.

The integration follows the "lego" approach - adding new components that work with
existing ones rather than modifying core files.
"""

import os
import sys
import json
import time
import math
import uuid
from typing import Dict, List, Any, Optional
from datetime import datetime

# Import QR Flipbook DNA System components
from qr_flipbook_system import QRFlipbookSystem
from qr_simple_generator import QRSimpleGenerator
from qr_simple_analyzer import QRSimpleAnalyzer
from qr_worker import QRWorker

# Import Recursive Self-Adaptive QR System components
from qr_phi_optimizer import QRPhiOptimizer
from qr_recursive_generator import QRRecursiveGenerator
from qr_recursive_analyzer import QRRecursiveAnalyzer

# Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio
VERSION_INFO = "1.0.0"

class QRIntegratedSystem:
    """
    Integrated system that combines QR Flipbook DNA with Recursive Self-Adaptive QR.
    
    This system enhances the QR Flipbook DNA workflow with:
    1. Phi-harmonic optimization for QR parameters
    2. Recursive self-improvement of generation and analysis
    3. Performance tracking and adaptation
    4. Visual phi-resonance indicators
    """
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the integrated QR system.
        
        Args:
            config_path: Path to configuration file (optional)
        """
        self.id = str(uuid.uuid4())
        self.creation_time = time.time()
        self.phi_time = self.creation_time * PHI % 1.0
        
        # Load configuration
        self.config = {
            "base_dir": "qr_integrated_system",
            "genome_path": "qr_genome.json",
            "sequence_dir": "qr_sequence",
            "response_dir": "qr_responses",
            "analysis_dir": "qr_analysis",
            "state_dir": "qr_state",
            "verbose": True,
            "self_improvement_enabled": True,
            "learning_rate": 1.0 / PHI,
            "max_iterations": 10,
            "auto_save": True
        }
        
        if config_path and os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    loaded_config = json.load(f)
                    self.config.update(loaded_config)
            except Exception as e:
                print(f"Error loading config: {e}")
        
        # Create directories
        self._create_directories()
        
        # Initialize components
        self._initialize_components()
        
        # System state
        self.history = []
        self.cycle_count = 0
        self.last_improvement_time = time.time()
        self.genome_data = None
        
        print(f"\n🧬 QR Integrated System v{VERSION_INFO}")
        print("=" * 60)
        print("Combining QR Flipbook DNA with Recursive Self-Adaptive QR")
        print(f"Phi-harmonic resonance: {self.phi_time:.6f}")
    
    def _create_directories(self):
        """Create all necessary directories"""
        base_dir = self.config["base_dir"]
        for key, path in self.config.items():
            if key.endswith('_dir'):
                full_path = os.path.join(base_dir, path)
                os.makedirs(full_path, exist_ok=True)
    
    def _initialize_components(self):
        """Initialize all system components"""
        base_dir = self.config["base_dir"]
        sequence_dir = os.path.join(base_dir, self.config["sequence_dir"])
        response_dir = os.path.join(base_dir, self.config["response_dir"])
        
        # Initialize QR Flipbook DNA components
        self.flipbook_system = QRFlipbookSystem(
            genome_path=self.config["genome_path"],
            sequence_dir=sequence_dir,
            response_dir=response_dir,
            verbose=self.config["verbose"]
        )
        
        # Initialize Recursive Self-Adaptive QR components
        self.optimizer = QRPhiOptimizer()
        self.recursive_generator = QRRecursiveGenerator()
        self.recursive_analyzer = QRRecursiveAnalyzer()
        
        # Optimize parameters
        if self.config["self_improvement_enabled"]:
            self.optimizer.optimize(iterations=3)
            self.recursive_generator.parameters = self.optimizer.best_parameters
            self.recursive_analyzer.parameters = self.optimizer.best_parameters
    
    def load_genome(self):
        """
        Load genome data from file.
        
        Returns:
            Loaded genome data
        """
        self.genome_data = self.flipbook_system.load_genome()
        return self.genome_data
    
    def generate_enhanced_qr_sequence(self):
        """
        Generate QR sequence with enhanced phi-harmonic properties.
        
        This method uses the recursive generator to create QR codes with:
        - Phi-optimized parameters
        - Visual resonance indicators
        - Self-adaptive compression
        
        Returns:
            List of paths to generated QR images
        """
        if not self.genome_data:
            print("No genome data loaded")
            return []
        
        if self.config["verbose"]:
            print(f"\n=== Generating Enhanced QR Sequence ===")
        
        start_time = time.time()
        
        # Extract frames from genome
        frames = []
        
        # Check if genome is a dictionary
        if isinstance(self.genome_data, dict):
            # Check for groups structure
            if "groups" in self.genome_data:
                for group in self.genome_data["groups"]:
                    if "codons" in group:
                        for codon in group["codons"]:
                            frames.append(codon)
            # Check for frames structure
            elif "frames" in self.genome_data:
                frames = self.genome_data["frames"]
        # Check if genome is a list
        elif isinstance(self.genome_data, list):
            frames = self.genome_data
        
        # Generate QR codes using recursive generator
        sequence_dir = os.path.join(self.config["base_dir"], self.config["sequence_dir"])
        results = self.recursive_generator.generate_qr_sequence(frames, sequence_dir)
        
        # Extract paths
        qr_paths = [result["path"] for result in results if "path" in result]
        
        end_time = time.time()
        
        if self.config["verbose"]:
            print(f"Generated {len(qr_paths)} QR code files in {sequence_dir}")
            print(f"Generation time: {end_time - start_time:.2f} seconds")
            print(f"Phi-harmonic resonance score: {self.recursive_generator.optimizer.best_score:.6f}")
        
        return qr_paths
    
    def analyze_enhanced_qr_sequence(self):
        """
        Analyze QR sequence with enhanced phi-harmonic analysis.
        
        This method uses the recursive analyzer to decode QR codes with:
        - Phi-optimized parameters
        - Self-adaptive analysis
        - Performance tracking
        
        Returns:
            Analysis report
        """
        sequence_dir = os.path.join(self.config["base_dir"], self.config["sequence_dir"])
        
        if self.config["verbose"]:
            print(f"\n=== Analyzing Enhanced QR Sequence ===")
        
        start_time = time.time()
        analysis_results = self.recursive_analyzer.analyze_qr_sequence(sequence_dir)
        end_time = time.time()
        
        if self.config["verbose"]:
            success_rate = analysis_results.get("success_rate", 0)
            print(f"Decoded {analysis_results.get('success_count', 0)}/{analysis_results.get('total_files', 0)} QR code files")
            print(f"Analysis time: {end_time - start_time:.2f} seconds")
            print(f"Success rate: {success_rate:.2%}")
            print(f"Phi-harmonic resonance score: {self.recursive_analyzer.optimizer.best_score:.6f}")
        
        return analysis_results
    
    def execute_tasks(self):
        """
        Execute tasks from QR sequence using the QR Worker.
        
        Returns:
            List of execution results
        """
        return self.flipbook_system.execute_qr_sequence()
    
    def generate_phi_enhanced_responses(self, execution_results):
        """
        Generate phi-enhanced response QR codes.
        
        Args:
            execution_results: Results from task execution
            
        Returns:
            List of paths to response QR codes
        """
        if not execution_results:
            print("No execution results to generate responses for")
            return []
        
        if self.config["verbose"]:
            print(f"\n=== Generating Phi-Enhanced Response QR Codes ===")
        
        response_dir = os.path.join(self.config["base_dir"], self.config["response_dir"])
        os.makedirs(response_dir, exist_ok=True)
        
        response_paths = []
        
        for i, result in enumerate(execution_results):
            # Create response data with phi-harmonic metadata
            response_data = {
                "result": result,
                "phi_meta": {
                    "timestamp": time.time(),
                    "phi_time": time.time() * PHI % 1.0,
                    "resonance": self.recursive_generator.optimizer.best_score,
                    "complexity": self.recursive_generator.parameters["complexity_factor"]
                }
            }
            
            # Generate QR code with recursive generator
            output_path = os.path.join(response_dir, f"response_{i+1:03d}.png")
            result = self.recursive_generator.generate_qr_code(response_data, output_path, i+1)
            
            if "path" in result:
                response_paths.append(result["path"])
        
        if self.config["verbose"]:
            print(f"Generated {len(response_paths)} response QR codes in {response_dir}")
        
        return response_paths
    
    def run(self):
        """
        Run the full integrated QR system workflow.
        
        Workflow:
        1. Load genome data
        2. Generate enhanced QR sequence
        3. Analyze enhanced QR sequence
        4. Execute tasks
        5. Generate phi-enhanced responses
        6. Self-improve
        7. Save state
        
        Returns:
            Summary of execution
        """
        start_time = time.time()
        self.cycle_count += 1
        
        print(f"\n🔄 Starting QR Integrated System Cycle #{self.cycle_count}")
        print("=" * 60)
        
        # Step 1: Load genome
        self.load_genome()
        
        # Step 2: Generate enhanced QR sequence
        qr_paths = self.generate_enhanced_qr_sequence()
        
        # Step 3: Analyze enhanced QR sequence
        analysis_results = self.analyze_enhanced_qr_sequence()
        
        # Step 4: Execute tasks
        execution_results = self.execute_tasks()
        
        # Step 5: Generate phi-enhanced responses
        response_paths = self.generate_phi_enhanced_responses(execution_results)
        
        # Step 6: Self-improve if enabled
        if self.config["self_improvement_enabled"]:
            print("\n=== Self-Improvement ===")
            self.optimizer.optimize(iterations=3)
            self.recursive_generator.parameters = self.optimizer.best_parameters
            self.recursive_analyzer.parameters = self.optimizer.best_parameters
            print(f"New phi-harmonic resonance score: {self.optimizer.best_score:.6f}")
        
        # Step 7: Save state if auto-save is enabled
        if self.config["auto_save"]:
            self.save_state()
        
        # Generate summary
        end_time = time.time()
        execution_time = end_time - start_time
        
        summary = {
            "cycle_id": self.cycle_count,
            "timestamp": end_time,
            "phi_time": end_time * PHI % 1.0,
            "execution_time": execution_time,
            "qr_paths": qr_paths,
            "analysis_results": {
                "success_rate": analysis_results.get("success_rate", 0),
                "total_files": analysis_results.get("total_files", 0),
                "success_count": analysis_results.get("success_count", 0)
            },
            "execution_results": execution_results,
            "response_paths": response_paths,
            "phi_resonance_score": self.optimizer.best_score
        }
        
        print(f"\n✅ QR Integrated System Cycle #{self.cycle_count} completed in {execution_time:.2f}s")
        print(f"Phi-harmonic resonance score: {self.optimizer.best_score:.6f}")
        
        # Add to history
        self.history.append(summary)
        
        return summary
    
    def save_state(self, path: Optional[str] = None):
        """Save the current state to a file"""
        if path is None:
            state_dir = os.path.join(self.config["base_dir"], self.config["state_dir"])
            os.makedirs(state_dir, exist_ok=True)
            path = os.path.join(state_dir, f"integrated_state_{int(time.time())}.json")
        
        try:
            state = {
                "id": self.id,
                "creation_time": self.creation_time,
                "phi_time": self.phi_time,
                "cycle_count": self.cycle_count,
                "last_improvement_time": self.last_improvement_time,
                "history": self.history,
                "config": self.config,
                "version": VERSION_INFO,
                "timestamp": time.time(),
                "optimizer_score": self.optimizer.best_score,
                "parameters": self.recursive_generator.parameters
            }
            
            with open(path, 'w') as f:
                json.dump(state, f, indent=2)
            
            # Also save component states
            base_dir = os.path.dirname(path)
            self.optimizer.save_state(os.path.join(base_dir, "optimizer_state.json"))
            self.recursive_generator.save_state(os.path.join(base_dir, "generator_state.json"))
            self.recursive_analyzer.save_state(os.path.join(base_dir, "analyzer_state.json"))
            
            print(f"System state saved to {path}")
            return True
        except Exception as e:
            print(f"Error saving system state: {e}")
            return False
    
    def load_state(self, path: str):
        """Load state from a file"""
        try:
            with open(path, 'r') as f:
                state = json.load(f)
            
            self.id = state.get("id", self.id)
            self.creation_time = state.get("creation_time", self.creation_time)
            self.phi_time = state.get("phi_time", self.phi_time)
            self.cycle_count = state.get("cycle_count", 0)
            self.last_improvement_time = state.get("last_improvement_time", time.time())
            self.history = state.get("history", [])
            
            # Update config but keep current values for missing keys
            loaded_config = state.get("config", {})
            self.config.update(loaded_config)
            
            # Also load component states if available
            base_dir = os.path.dirname(path)
            optimizer_path = os.path.join(base_dir, "optimizer_state.json")
            generator_path = os.path.join(base_dir, "generator_state.json")
            analyzer_path = os.path.join(base_dir, "analyzer_state.json")
            
            if os.path.exists(optimizer_path):
                self.optimizer.load_state(optimizer_path)
            
            if os.path.exists(generator_path):
                self.recursive_generator.load_state(generator_path)
            
            if os.path.exists(analyzer_path):
                self.recursive_analyzer.load_state(analyzer_path)
            
            print(f"System state loaded from {path}")
            return True
        except Exception as e:
            print(f"Error loading system state: {e}")
            return False

def main():
    """Main function to run the integrated QR system"""
    import argparse
    
    parser = argparse.ArgumentParser(description="QR Integrated System")
    parser.add_argument("--config", help="Path to configuration file")
    parser.add_argument("--load", help="Load system state from file")
    parser.add_argument("--cycles", type=int, default=1, help="Number of cycles to run")
    parser.add_argument("--genome", help="Path to genome file")
    args = parser.parse_args()
    
    # Initialize system
    system = QRIntegratedSystem(args.config)
    
    # Override genome path if specified
    if args.genome:
        system.config["genome_path"] = args.genome
    
    # Load state if specified
    if args.load and os.path.exists(args.load):
        system.load_state(args.load)
    
    # Run specified number of cycles
    for i in range(args.cycles):
        if i > 0:
            print(f"\n{'='*30} CYCLE {i+1}/{args.cycles} {'='*30}\n")
            time.sleep(1)  # Small pause between cycles
        
        # Run cycle
        system.run()
    
    # Save final state
    system.save_state()
    
    print("\n✨ QR Integrated System execution complete")
    print(f"Ran {args.cycles} cycle(s)")
    print(f"System state saved to {system.config['base_dir']}/{system.config['state_dir']}")

if __name__ == "__main__":
    main()
