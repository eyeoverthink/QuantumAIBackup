#!/usr/bin/env python3
"""
QR Recursive System - Main Integration Script
Combines all components of the self-improving QR code system
"""

import os
import sys
import json
import time
import math
import uuid
import argparse
from typing import Dict, List, Any, Optional
from datetime import datetime

# Import our recursive components
from qr_phi_optimizer import QRPhiOptimizer
from qr_recursive_generator import QRRecursiveGenerator
from qr_recursive_analyzer import QRRecursiveAnalyzer

# Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio
VERSION_INFO = "1.0.0"

class QRRecursiveSystem:
    """
    Integrated QR Recursive System that combines generator, analyzer, and optimizer
    Implements a full self-improving workflow for QR code generation and analysis
    """
    
    def __init__(self, config_path: Optional[str] = None):
        self.id = str(uuid.uuid4())
        self.creation_time = time.time()
        self.phi_time = self.creation_time * PHI % 1.0
        
        # Load configuration
        self.config = {
            "base_dir": "qr_recursive_system",
            "sequence_dir": "qr_sequence",
            "analysis_dir": "qr_analysis",
            "reports_dir": "qr_reports",
            "state_dir": "qr_state",
            "log_file": "qr_system_log.json",
            "self_improvement_enabled": True,
            "learning_rate": 1.0 / PHI,
            "max_iterations": 100,
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
        self.optimizer = QRPhiOptimizer(config_path)
        self.generator = QRRecursiveGenerator(config_path)
        self.analyzer = QRRecursiveAnalyzer(config_path)
        
        # System state
        self.history = []
        self.cycle_count = 0
        self.last_improvement_time = time.time()
    
    def _create_directories(self):
        """Create all necessary directories"""
        for key, path in self.config.items():
            if key.endswith('_dir'):
                full_path = os.path.join(self.config["base_dir"], path)
                os.makedirs(full_path, exist_ok=True)
    
    def _get_full_path(self, dir_key: str) -> str:
        """Get full path for a directory key"""
        return os.path.join(self.config["base_dir"], self.config[dir_key])
    
    def run_cycle(self, data_sequence: List[Any]) -> Dict[str, Any]:
        """
        Run a complete cycle of the recursive system:
        1. Generate QR codes from data
        2. Analyze the generated QR codes
        3. Self-improve based on performance
        4. Save state
        
        Returns a report of the cycle
        """
        cycle_start = time.time()
        self.cycle_count += 1
        
        print(f"\n🔄 Starting QR Recursive System Cycle #{self.cycle_count}")
        print("=" * 60)
        
        # Step 1: Generate QR sequence
        print("\n📊 Step 1: Generating QR Sequence")
        sequence_dir = self._get_full_path("sequence_dir")
        generation_start = time.time()
        
        generation_results = self.generator.generate_qr_sequence(
            data_sequence, 
            output_dir=sequence_dir
        )
        
        generation_time = time.time() - generation_start
        print(f"Generated {len(generation_results)} QR codes in {generation_time:.2f}s")
        
        # Step 2: Analyze QR sequence
        print("\n📊 Step 2: Analyzing QR Sequence")
        analysis_start = time.time()
        
        analysis_results = self.analyzer.analyze_qr_sequence(sequence_dir)
        
        analysis_time = time.time() - analysis_start
        success_rate = analysis_results.get("success_rate", 0)
        print(f"Analysis complete: {success_rate:.2%} success rate in {analysis_time:.2f}s")
        
        # Step 3: Self-improvement (already done in components)
        print("\n📊 Step 3: System Self-Improvement")
        
        # Check if any component improved
        generator_improved = len(self.generator.history) > 0
        analyzer_improved = len(self.analyzer.history) > 0
        
        if generator_improved or analyzer_improved:
            print("✨ System components have self-improved")
            self.last_improvement_time = time.time()
        else:
            print("System is stable, no improvements needed")
        
        # Step 4: Save state if auto-save is enabled
        if self.config["auto_save"]:
            self.save_state()
        
        # Create cycle report
        cycle_end = time.time()
        cycle_time = cycle_end - cycle_start
        
        cycle_report = {
            "cycle_id": self.cycle_count,
            "timestamp": cycle_end,
            "phi_time": cycle_end * PHI % 1.0,
            "cycle_time": cycle_time,
            "generation": {
                "count": len(generation_results),
                "time": generation_time
            },
            "analysis": {
                "success_rate": success_rate,
                "time": analysis_time
            },
            "improvements": {
                "generator": generator_improved,
                "analyzer": analyzer_improved
            }
        }
        
        # Add to history
        self.history.append(cycle_report)
        
        print(f"\n✅ Cycle #{self.cycle_count} completed in {cycle_time:.2f}s")
        print(f"Success rate: {success_rate:.2%}")
        
        return cycle_report
    
    def save_state(self, path: Optional[str] = None) -> bool:
        """Save the complete system state"""
        if path is None:
            state_dir = self._get_full_path("state_dir")
            os.makedirs(state_dir, exist_ok=True)
            path = os.path.join(state_dir, f"qr_system_state_{int(time.time())}.json")
        
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
                "timestamp": time.time()
            }
            
            with open(path, 'w') as f:
                json.dump(state, f, indent=2)
            
            # Also save component states
            base_dir = os.path.dirname(path)
            self.optimizer.save_state(os.path.join(base_dir, "optimizer_state.json"))
            self.generator.save_state(os.path.join(base_dir, "generator_state.json"))
            self.analyzer.save_state(os.path.join(base_dir, "analyzer_state.json"))
            
            print(f"System state saved to {path}")
            return True
        except Exception as e:
            print(f"Error saving system state: {e}")
            return False
    
    def load_state(self, path: str) -> bool:
        """Load system state from a file"""
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
                self.generator.load_state(generator_path)
            
            if os.path.exists(analyzer_path):
                self.analyzer.load_state(analyzer_path)
            
            print(f"System state loaded from {path}")
            return True
        except Exception as e:
            print(f"Error loading system state: {e}")
            return False

def generate_test_data(count: int = 5) -> List[Dict[str, Any]]:
    """Generate test data for QR sequence"""
    test_data = []
    
    for i in range(1, count + 1):
        phi_time = time.time() * PHI % 1.0
        resonance = 1.0 - abs(phi_time - 0.5) * 2.0
        
        data = {
            "id": str(uuid.uuid4()),
            "message": f"Test message {i}",
            "timestamp": time.time(),
            "phi_time": phi_time,
            "resonance": resonance,
            "phi_state": {
                "complexity": 0.7 + (0.3 * resonance),
                "resonance": resonance * PHI,
                "generation": 1
            }
        }
        
        # Add code snippets for testing
        if i == 1:
            data["code"] = "print('Hello Quantum World!')"
            data["task_type"] = "execute_python"
        elif i == 2:
            data["code"] = "echo 'Hello from shell script'"
            data["task_type"] = "execute_shell"
        else:
            data["data"] = f"Test data payload {i}"
            data["task_type"] = "store_data"
        
        test_data.append(data)
    
    return test_data

def main():
    """Main function to run the QR recursive system"""
    parser = argparse.ArgumentParser(description="QR Recursive System")
    parser.add_argument("--config", help="Path to configuration file")
    parser.add_argument("--load", help="Load system state from file")
    parser.add_argument("--cycles", type=int, default=1, help="Number of cycles to run")
    parser.add_argument("--items", type=int, default=5, help="Number of test items to generate")
    args = parser.parse_args()
    
    print("\n🌟 QR Recursive System v1.0")
    print("=" * 60)
    print("A self-improving QR code system based on phi-harmonic principles")
    print("and quantum recursive self-improvement")
    
    # Initialize system
    system = QRRecursiveSystem(args.config)
    
    # Load state if specified
    if args.load and os.path.exists(args.load):
        system.load_state(args.load)
    
    # Run specified number of cycles
    for i in range(args.cycles):
        if i > 0:
            print(f"\n{'='*30} CYCLE {i+1}/{args.cycles} {'='*30}\n")
            time.sleep(1)  # Small pause between cycles
        
        # Generate test data
        test_data = generate_test_data(args.items)
        
        # Run cycle
        system.run_cycle(test_data)
    
    # Save final state
    system.save_state()
    
    print("\n✨ QR Recursive System execution complete")
    print(f"Ran {args.cycles} cycles with {args.items} items per cycle")
    print(f"System state saved to {system.config['base_dir']}/{system.config['state_dir']}")

if __name__ == "__main__":
    main()
