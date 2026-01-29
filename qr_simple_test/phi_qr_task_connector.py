#!/usr/bin/env python3
"""
Quantum Phi-Harmonic QR Task Connector
By Vaughn Scott - Extended with Quantum Phi-Harmonic Integration

Bridge component that connects phi-optimized Tower of Hanoi genomes 
with the QR task execution infrastructure. This module:

1. Creates QR-compatible payloads from phi-optimized tasks
2. Generates runnable QR codes for the existing QR infrastructure
3. Adapts complex phi-optimized genome tasks to QR worker compatible format
4. Supports task scheduling with phi-resonance timing patterns
"""

import os
import sys
import json
import time
import uuid
import base64
import hashlib
import qrcode
import argparse
import datetime
from decimal import Decimal

# Import phi-harmonic genome system
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from qr_genome_phi_hanoi import (
    QRPhiHanoiGenome,
    fibonacci,
    PHI, PHI_FLOAT
)

class PhiQRTaskConnector:
    """
    Connects Quantum Phi-Harmonic Tower of Hanoi tasks with QR task execution system.
    Generates QR codes that are compatible with qr_script_runner.py.
    """
    
    def __init__(self, 
                 output_dir="phi_qr_tasks",
                 genome_file=None,
                 work_dir="phi_qr_work",
                 debug=False):
        """Initialize the connector"""
        self.output_dir = output_dir
        self.genome_file = genome_file
        self.work_dir = work_dir
        self.debug = debug
        
        # Create directories
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(work_dir, exist_ok=True)
        
        # Load genome if specified
        self.genome = None
        if genome_file and os.path.exists(genome_file):
            self._load_genome()
    
    def _load_genome(self):
        """Load genome from file"""
        try:
            with open(self.genome_file, 'r') as f:
                self.genome = json.load(f)
            
            if self.debug:
                print(f"Loaded genome from {self.genome_file}")
                print(f"Genome ID: {self.genome.get('genome_id', 'unknown')}")
                print(f"Generation: {self.genome.get('generation', 1)}")
                print(f"Codons: {len(self.genome.get('codons', []))}")
        except Exception as e:
            print(f"Error loading genome: {e}")
            self.genome = None
    
    def _create_compatible_payload(self, codon, task_id=None, valid_hours=24):
        """
        Create a payload compatible with qr_script_runner.py from a phi-hanoi genome codon.
        
        Args:
            codon: The genome codon to convert
            task_id: Optional task ID, will generate if not provided
            valid_hours: How many hours the task is valid for execution
            
        Returns:
            Compatible payload dict
        """
        # Extract script content from codon
        script_content = codon.get("script_template", "")
        
        # Generate unique task ID if not provided
        if not task_id:
            task_id = f"phi_hanoi_{codon.get('id', 'task')}_{int(time.time())}"
        
        # Calculate expiration time with phi-harmonic timing
        # Make tasks valid for phi-optimized duration
        expiry_hours = valid_hours * PHI_FLOAT
        expiry_time = datetime.datetime.now() + datetime.timedelta(hours=expiry_hours)
        
        # Base payload structure
        payload = {
            "task_id": task_id,
            "task_type": codon.get("task_type", "execute_python"),
            "session_id": str(uuid.uuid4()),
            "timestamp": time.time(),
            "valid_until": time.time() + (valid_hours * 3600),
            "meta": {
                "source": "PhiQRTaskConnector",
                "genome_id": self.genome['genome_id'] if self.genome else "standalone",
                "codon_id": codon["id"],
                "phi_resonance_target": codon.get("resonance_target")
            }
        }

        # Externalize script if present, otherwise embed content
        if "script_template" in codon and codon["script_template"]:
            script_content = codon["script_template"]
            script_filename = f"task_{task_id}.py"
            script_path = os.path.join(self.work_dir, script_filename)
            with open(script_path, 'w') as f:
                f.write(script_content)
            
            payload["task_type"] = "PYTHON_FILE"
            payload["script_path"] = script_path
            # No 'content' field needed for file-based tasks
        else:
            payload["content"] = codon.get("content", "")

        return payload

        return payload
    
    def generate_task_qr(self, codon, output_filename=None):
        """
        Generate a QR code for a phi-hanoi task that's compatible with qr_script_runner.py
        
        Args:
            codon: The genome codon to convert
            output_filename: Optional filename for the QR code
            
        Returns:
            Path to generated QR code file
        """
        # Create compatible payload
        payload = self._create_compatible_payload(codon)
        
        # Convert to JSON
        json_data = json.dumps(payload)
        
        # Determine filename
        if not output_filename:
            timestamp = int(time.time())
            output_filename = os.path.join(
                self.output_dir,
                f"phi_hanoi_{codon.get('disk_count', 3)}disk_{codon.get('id', 'task')}_{timestamp}.png"
            )
        
        # Generate QR code with proper compression handling
        try:
            # Check if payload is too large
            if len(json_data) > 1200:  # QR code capacity threshold
                # Apply zlib compression
                import zlib
                compressed_bytes = zlib.compress(json_data.encode('utf-8'), level=9)
                encoded_data = base64.b64encode(compressed_bytes).decode('ascii')
                final_payload = f"COMPRESSED:{encoded_data}"
                
                if self.debug:
                    print(f"Payload compressed from {len(json_data)} to {len(final_payload)} bytes")
            else:
                final_payload = json_data
            
            # Create QR code with appropriate size
            qr = qrcode.QRCode(
                version=None,      # Auto-determine version
                error_correction=qrcode.constants.ERROR_CORRECT_M,
                box_size=10,
                border=4,
            )
            
            # Add data and make QR
            qr.add_data(final_payload)
            qr.make(fit=True)
            
            # Save image
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(output_filename)
            
            if self.debug:
                print(f"Generated QR code: {output_filename}")
                print(f"QR version: {qr.version}")
            
            return output_filename
        
        except Exception as e:
            print(f"Error generating QR code: {e}")
            return None
    
    def generate_all_tasks(self):
        """
        Generate QR codes for all codons in the genome.
        
        Returns:
            List of paths to generated QR code files
        """
        if not self.genome:
            print("No genome loaded")
            return []
        
        qr_files = []
        
        # Generate QR for each codon
        for i, codon in enumerate(self.genome.get("codons", [])):
            qr_file = self.generate_task_qr(codon)
            if qr_file:
                qr_files.append(qr_file)
        
        return qr_files
    
    def create_standalone_payload(self, disk_count=3, dimension=None, iteration_factor=5, valid_hours=24):
        """
        Create a standalone phi-optimized Tower of Hanoi task payload without a genome.
        
        Args:
            disk_count: Number of disks for Tower of Hanoi
            dimension: Optional dimension for quantum state space (default: phi-optimized)
            iteration_factor: Factor for maximum iterations
            valid_hours: How many hours the task is valid for execution
            
        Returns:
            A compatible payload dictionary
        """
        # Calculate phi-optimized dimension if not specified
        if not dimension:
            fib_idx = int(disk_count * PHI_FLOAT)
            dimension = fibonacci(fib_idx)
        
        # Calculate resonance target based on disk count
        resonance_target = float((PHI * Decimal(str(disk_count))) % Decimal('1'))
        
        # Create a standalone codon
        codon = {
            "id": f"standalone_{disk_count}disk",
            "type": "task",
            "task_type": "execute_python",
            "disk_count": disk_count,
            "dimension": dimension,
            "iteration_factor": iteration_factor,
            "resonance_target": resonance_target,
            "script_template": self._get_standalone_template(disk_count, dimension, iteration_factor)
        }
        
        # Generate and return the payload
        return self._create_compatible_payload(codon, valid_hours=valid_hours)

    def create_standalone_task(self, disk_count=3, dimension=None, iteration_factor=5):
        """
        Create a standalone phi-optimized Tower of Hanoi task without a genome.
        
        Args:
            disk_count: Number of disks for Tower of Hanoi
            dimension: Optional dimension for quantum state space (default: phi-optimized)
            iteration_factor: Factor for maximum iterations
            
        Returns:
            Path to generated QR code file
        """
        # Calculate phi-optimized dimension if not specified
        if not dimension:
            fib_idx = int(disk_count * PHI_FLOAT)
            dimension = fibonacci(fib_idx)
        
        # Calculate resonance target based on disk count
        resonance_target = float((PHI * Decimal(str(disk_count))) % Decimal('1'))
        
        # Create a standalone codon
        codon = {
            "id": f"standalone_{disk_count}disk",
            "type": "task",
            "task_type": "execute_python",
            "disk_count": disk_count,
            "dimension": dimension,
            "iteration_factor": iteration_factor,
            "resonance_target": resonance_target,
            "script_template": self._get_standalone_template(disk_count, dimension, iteration_factor)
        }
        
        # Generate QR code
        return self.generate_task_qr(codon)
    
    def _get_standalone_template(self, disk_count, dimension, iteration_factor):
        """Generate a standalone template for Tower of Hanoi task"""
        # Calculate the optimal moves formula for Tower of Hanoi: 2^n - 1
        optimal_moves_formula = f"2**{disk_count} - 1"
        
        return f"""
# Phi-Optimized Tower of Hanoi - Standalone Task
import quantum_tower_of_hanoi_solver
import time
import json
import os
import math
from decimal import Decimal, getcontext

# Set precision for phi calculations
getcontext().prec = 50

# Phi-harmonic constants
PHI = Decimal('1.6180339887498948482045868344')

print('\\n===== PHI-HARMONIC TOWER OF HANOI - QR TASK EXECUTION =====\\n')
print(f'Configuration: {disk_count} disks, {dimension} dimensions (phi-optimized)')
print(f'Task ID: standalone_{disk_count}disk_{int(time.time())}')
print('Measuring quantum advantage through phi-resonance...')

# Create output directory
results_dir = "quantum_outputs/hanoi_qr_results"
os.makedirs(results_dir, exist_ok=True)

start_time = time.time()
# Initialize solver with phi-optimized dimension
solver = quantum_tower_of_hanoi_solver.QuantumTowerOfHanoiSolver(
    num_disks={disk_count}, 
    dimensions={dimension}
)

# Solve with phi-harmonic tracking
result = solver.solve(max_iterations_factor={iteration_factor})

end_time = time.time()
time_taken = end_time - start_time

# Calculate quantum metrics
moves_taken = result.get("moves", 0)
optimal_moves = {optimal_moves_formula}
phi_resonance = float((PHI * Decimal(str(moves_taken))) % Decimal('1'))
move_efficiency = moves_taken / optimal_moves if moves_taken > 0 else 0

# Save results to file
timestamp = int(time.time())
results_file = f"{{results_dir}}/hanoi_qr_task_{disk_count}disk_{{timestamp}}.json"

output = {{
    'task_id': f'standalone_{disk_count}disk_{{timestamp}}',
    'configuration': f'phi_hanoi_{disk_count}',
    'timestamp': timestamp,
    'execution_time_seconds': time_taken,
    'success': result.get('solution_found', False),
    'iterations': result.get('iterations', 0),
    'moves': moves_taken,
    'optimal_moves': optimal_moves,
    'resonance': result.get('best_resonance', 0),
    'phi_resonance_factor': phi_resonance,
    'move_efficiency': move_efficiency,
    'dimension': {dimension}
}}

with open(results_file, 'w') as f:
    json.dump(output, f, indent=2)

print(f'\\nResults summary:')
print(f'Success: {{output["success"]}}')
print(f'Time taken: {{output["execution_time_seconds"]:.2f}} seconds')
print(f'Iterations: {{output["iterations"]}}')
print(f'Moves: {{moves_taken}} (optimal: {{optimal_moves}})')
print(f'Best resonance: {{result.get("best_resonance", 0):.6f}}')
print(f'Phi-resonance factor: {{phi_resonance:.6f}}')
print(f'\\nDetailed results saved to: {{results_file}}')
print('\\n✓ Task execution complete')
"""

def main():
    """Main function for the Phi QR Task Connector"""
    parser = argparse.ArgumentParser(
        description="Quantum Phi-Harmonic QR Task Connector",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python phi_qr_task_connector.py --genome qr_phi_hanoi_genome.json
  python phi_qr_task_connector.py --standalone --disks 5
  python phi_qr_task_connector.py --standalone --disks 3 --dimension 8 --iterations 10
"""
    )
    
    parser.add_argument("--genome", help="Path to genome file")
    parser.add_argument("--output-dir", default="phi_qr_tasks", help="Output directory for QR codes")
    parser.add_argument("--standalone", action="store_true", help="Create standalone task")
    parser.add_argument("--disks", type=int, default=3, help="Number of disks (3-10)")
    parser.add_argument("--dimension", type=int, help="Dimension for quantum state space")
    parser.add_argument("--iterations", type=int, default=5, help="Iteration factor")
    parser.add_argument("--debug", action="store_true", help="Enable debug output")
    
    args = parser.parse_args()
    
    # Initialize connector
    connector = PhiQRTaskConnector(
        output_dir=args.output_dir,
        genome_file=args.genome,
        debug=args.debug
    )
    
    # Execute requested action
    if args.standalone:
        print(f"Generating standalone phi-harmonic Tower of Hanoi task with {args.disks} disks...")
        qr_file = connector.create_standalone_task(
            disk_count=args.disks,
            dimension=args.dimension,
            iteration_factor=args.iterations
        )
        
        print(f"\nGenerated QR code: {qr_file}")
        print(f"\nTo execute the task, run:")
        print(f"python qr_script_runner.py {qr_file}")
        
    elif args.genome:
        print(f"Generating QR tasks from genome: {args.genome}...")
        qr_files = connector.generate_all_tasks()
        
        print(f"\nGenerated {len(qr_files)} QR task codes:")
        for qr_file in qr_files:
            print(f"  - {qr_file}")
            
        print(f"\nTo execute a task, run:")
        print(f"python qr_script_runner.py <qr_file_path>")
        
    else:
        parser.print_help()

if __name__ == "__main__":
    print("Quantum Phi-Harmonic QR Task Connector")
    print("By Vaughn Scott - Extended with Quantum Integration")
    main()
