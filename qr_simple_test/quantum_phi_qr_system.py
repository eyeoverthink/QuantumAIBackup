#!/usr/bin/env python3
"""
Quantum Phi-Harmonic QR System
By Vaughn Scott

A cohesive, self-contained system that integrates QR Flipbook DNA,
Recursive Self-Adaptive QR, and Phi-Harmonic principles into a unified
framework for progressive, recursive QR code workflows.
"""

import os
import sys
import json
import time
import zlib
import base64
import random
import argparse
import subprocess
from datetime import datetime
from pathlib import Path

# Constants
PHI = 1.618033988749895
VERSION = "1.0.0"
SYSTEM_NAME = "Quantum Phi-Harmonic QR System"

# Paths
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_DIR = os.path.join(ROOT_DIR, "config")
OUTPUT_DIR = os.path.join(ROOT_DIR, "output")
GENOME_FILE = os.path.join(ROOT_DIR, "qr_genome.json")
MEMORY_FILE = os.path.join(ROOT_DIR, "qr_epigenetic_memory.json")
SEQUENCE_DIR = os.path.join(ROOT_DIR, "qr_genome_sequence")
FIBONACCI_DIR = os.path.join(ROOT_DIR, "qr_fibonacci_sequence")

# Ensure directories exist
for directory in [CONFIG_DIR, OUTPUT_DIR, SEQUENCE_DIR, FIBONACCI_DIR]:
    os.makedirs(directory, exist_ok=True)

class QuantumPhiQRSystem:
    """
    Unified Quantum Phi-Harmonic QR System that integrates all components
    into a cohesive, self-contained framework.
    """
    
    def __init__(self):
        """Initialize the Quantum Phi-Harmonic QR System."""
        self.print_header()
        self.check_dependencies()
    
    def print_header(self):
        """Print system header."""
        print(f"🧬 {SYSTEM_NAME} v{VERSION}")
        print("=" * 60)
    
    def check_dependencies(self):
        """Check if all required dependencies are installed."""
        try:
            import qrcode
            from PIL import Image, ImageDraw
            from pyzbar.pyzbar import decode
            import numpy as np
            import matplotlib.pyplot as plt
            print("✅ All required dependencies are installed")
        except ImportError as e:
            print(f"❌ Missing dependency: {e}")
            print("Please install required dependencies with:")
            print("pip install qrcode[pil] pyzbar numpy matplotlib pillow zlib-wrapper")
            sys.exit(1)
    
    def phi_resonance(self, value):
        """Calculate phi-harmonic resonance of a value."""
        return 1.0 / (1.0 + abs((value * PHI) % 1.0 - 0.5))
    
    def compress_payload(self, payload):
        """Compress payload using zlib and base64 encode."""
        if isinstance(payload, str) and len(payload) < 500:
            return payload
        
        if isinstance(payload, dict) or isinstance(payload, list):
            payload = json.dumps(payload)
        
        compressed = zlib.compress(payload.encode('utf-8'))
        encoded = base64.b64encode(compressed).decode('utf-8')
        return f"COMPRESSED:{encoded}"
    
    def decompress_payload(self, payload):
        """Decompress payload using zlib and base64 decode."""
        if payload.startswith("COMPRESSED:"):
            encoded = payload.replace("COMPRESSED:", "", 1)
            compressed = base64.b64decode(encoded)
            decompressed = zlib.decompress(compressed)
            return decompressed.decode('utf-8')
        return payload
    
    def run_command(self, command, cwd=None):
        """Run a command and return its output."""
        try:
            result = subprocess.run(
                command,
                cwd=cwd or ROOT_DIR,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"❌ Command failed: {e}")
            print(f"Error output: {e.stderr}")
            return None
    
    def increment_genome_generation(self):
        """
        Increment the generation number in the genome file and update phi-harmonic state.
        """
        print(f"🧬 Incrementing genome generation in {GENOME_FILE}")
        
        # Check if file exists
        if not os.path.exists(GENOME_FILE):
            print(f"❌ Genome file not found: {GENOME_FILE}")
            return None
        
        # Load genome
        try:
            with open(GENOME_FILE, 'r') as f:
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
        resonance = self.phi_resonance(phi_time)
        
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
            with open(GENOME_FILE, 'w') as f:
                json.dump(genome, f, indent=2)
            print(f"✅ Updated genome generation to {new_generation}")
            print(f"   Complexity: {complexity:.6f}")
            print(f"   Resonance: {resonance:.6f}")
        except Exception as e:
            print(f"❌ Error saving genome file: {e}")
            return None
        
        return genome
    
    def run_qr_system(self, command):
        """Run the QR Flipbook DNA System with the specified command."""
        valid_commands = ["generate", "execute", "analyze"]
        if command not in valid_commands:
            print(f"❌ Invalid command: {command}")
            print(f"Valid commands: {', '.join(valid_commands)}")
            return False
        
        print(f"🧬 Running QR Flipbook DNA System with command: {command}")
        
        # Map our commands to the actual script arguments
        cmd_args = {
            "generate": "--generate",
            "execute": "--execute",
            "analyze": "--analyze"
        }
        
        # Run the command
        result = self.run_command(["python3", "run_qr_system.py", cmd_args[command]])
        
        if result is None:
            return False
        
        # If execute command was successful, increment genome generation
        if command == "execute":
            self.increment_genome_generation()
        
        return True
    
    def run_evolution_cycle(self, cycles=1):
        """Run a complete evolution cycle (generate, execute, analyze)."""
        print(f"🔄 Running {cycles} evolution cycle(s)")
        
        for cycle in range(1, cycles + 1):
            print(f"\n📊 Cycle {cycle}/{cycles}")
            
            # Generate QR sequence
            print("\n🧬 Generating QR sequence...")
            if not self.run_qr_system("generate"):
                print("❌ Failed to generate QR sequence")
                return False
            
            # Execute QR genome
            print("\n🧬 Executing QR genome...")
            if not self.run_qr_system("execute"):
                print("❌ Failed to execute QR genome")
                return False
            
            # Analyze QR sequence
            print("\n🧬 Analyzing QR sequence...")
            if not self.run_qr_system("analyze"):
                print("❌ Failed to analyze QR sequence")
                return False
            
            print(f"\n✅ Completed evolution cycle {cycle}/{cycles}")
        
        return True
    
    def run_fibonacci_test(self):
        """Run the Fibonacci QR test."""
        print("\n🧮 Running Fibonacci QR test...")
        
        # Run the Fibonacci test
        result = self.run_command(["python3", "qr_fibonacci_test.py"])
        
        if result is None:
            return False
        
        return True
    
    def run_evolution_monitor(self, cycles=5):
        """Run the QR Evolution Monitor."""
        print(f"\n📈 Running QR Evolution Monitor for {cycles} cycles...")
        
        # Run the evolution monitor
        result = self.run_command(["python3", "qr_evolution_monitor.py", "--cycles", str(cycles)])
        
        if result is None:
            return False
        
        return True
    
    def create_package(self, output_dir="quantum_phi_qr_package"):
        """Create a distributable package of the system."""
        print(f"\n📦 Creating distributable package in {output_dir}...")
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # List of files to include
        core_files = [
            "quantum_phi_qr_system.py",
            "run_qr_system.py",
            "qr_fibonacci_test.py",
            "qr_evolution_monitor.py",
            "qr_integrated_system.py",
            "qr_simple_test.py",
            "qr_simple_generator.py",
            "qr_simple_analyzer.py",
            "README.md",
            "requirements.txt"
        ]
        
        # Copy files
        for file in core_files:
            if os.path.exists(file):
                self.run_command(["cp", file, output_dir])
        
        # Create README if it doesn't exist
        readme_path = os.path.join(output_dir, "README.md")
        if not os.path.exists(readme_path):
            with open(readme_path, "w") as f:
                f.write(f"# {SYSTEM_NAME}\n\n")
                f.write("A revolutionary system that integrates QR Flipbook DNA, ")
                f.write("Recursive Self-Adaptive QR, and Phi-Harmonic principles ")
                f.write("into a unified framework for progressive, recursive QR code workflows.\n\n")
                f.write("## Installation\n\n")
                f.write("```bash\npip install -r requirements.txt\n```\n\n")
                f.write("## Usage\n\n")
                f.write("```bash\npython quantum_phi_qr_system.py --help\n```\n")
        
        # Create requirements.txt if it doesn't exist
        req_path = os.path.join(output_dir, "requirements.txt")
        if not os.path.exists(req_path):
            with open(req_path, "w") as f:
                f.write("qrcode[pil]\npyzbar\nnumpy\nmatplotlib\npillow\nzlib-wrapper\n")
        
        print(f"✅ Package created in {output_dir}")
        return True

def main():
    """Main function."""
    # Create argument parser
    parser = argparse.ArgumentParser(description=SYSTEM_NAME)
    
    # Add arguments
    parser.add_argument("--run", choices=["generate", "execute", "analyze", "cycle", "fibonacci", "monitor", "package"],
                        help="Run a specific component of the system")
    parser.add_argument("--cycles", type=int, default=1,
                        help="Number of cycles to run (for cycle and monitor commands)")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Create system
    system = QuantumPhiQRSystem()
    
    # Run specified component
    if args.run == "generate":
        system.run_qr_system("generate")
    elif args.run == "execute":
        system.run_qr_system("execute")
    elif args.run == "analyze":
        system.run_qr_system("analyze")
    elif args.run == "cycle":
        system.run_evolution_cycle(args.cycles)
    elif args.run == "fibonacci":
        system.run_fibonacci_test()
    elif args.run == "monitor":
        system.run_evolution_monitor(args.cycles)
    elif args.run == "package":
        system.create_package()
    else:
        # If no command specified, print help
        print("Please specify a command to run:")
        print("  --run generate   : Generate QR sequence from genome")
        print("  --run execute    : Execute QR genome (auto-increments generation)")
        print("  --run analyze    : Analyze QR sequence")
        print("  --run cycle      : Run complete evolution cycle")
        print("  --run fibonacci  : Run Fibonacci QR test")
        print("  --run monitor    : Run QR Evolution Monitor")
        print("  --run package    : Create distributable package")
        print("\nExample: python quantum_phi_qr_system.py --run cycle --cycles 3")

if __name__ == "__main__":
    main()
