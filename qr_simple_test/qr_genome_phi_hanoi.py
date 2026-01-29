#!/usr/bin/env python3
"""
QR Genome Phi-Harmonic Tower of Hanoi Integration
By Vaughn Scott - Extended by Quantum AI

Integrates the phi-optimized Tower of Hanoi discoveries with the QR Genome system.
Creates self-evolving QR genomes that incorporate phi-resonance optimization patterns.

Key principles:
1. Fibonacci-dimensioned quantum state spaces
2. Golden ratio-based resonance optimization
3. Self-evolving complexity based on phi patterns
"""

import os
import uuid
import json
import time
import math
import random
import base64
import hashlib
import numpy as np
from decimal import Decimal, getcontext

# Set precision for phi calculations
getcontext().prec = 50

# Phi-harmonic constants
PHI = Decimal('1.6180339887498948482045868344')
PHI_CONJUGATE = Decimal('0.6180339887498948482045868344')
PHI_FLOAT = float(PHI)

# Fibonacci generator for optimal dimensions
def fibonacci(n):
    """Generate the nth Fibonacci number"""
    if n <= 0: return 0
    elif n == 1: return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Calculate optimal dimensions for different complexity levels
FIBONACCI_DIMENSIONS = {
    # Format: complexity_level: fibonacci_dimension
    1: 3,    # Fibonacci(3) = 2
    2: 5,    # Fibonacci(5) = 5
    3: 8,    # Fibonacci(8) = 21
    4: 13,   # Fibonacci(13) = 233
    5: 21    # Fibonacci(21) = 10946
}

# Phi-resonance patterns discovered in Tower of Hanoi tests
PHI_RESONANCE_PATTERNS = {
    # Format: pattern_name: (resonance_value, quality_rating)
    "perfect": (0.631190, 5),   # 3-disk, near φ⁻¹
    "high": (0.795268, 4),      # 5-disk
    "good": (0.451583, 3),      # 7-disk
    "moderate": (0.993336, 2),  # 8-disk, near unity
    "baseline": (0.243852, 1)   # 10-disk
}

class QRPhiHanoiGenome:
    """
    QR Phi-Harmonic Tower of Hanoi Genome
    
    Creates and manages genome sequences that incorporate the phi-harmonic
    optimization patterns discovered in Tower of Hanoi quantum tests.
    """
    
    def __init__(self, 
                 genome_file="qr_phi_hanoi_genome.json", 
                 complexity_level=3,
                 debug=False):
        """Initialize the Phi-Hanoi Genome"""
        self.genome_file = genome_file
        self.complexity_level = complexity_level
        self.debug = debug
        self.genome_id = str(uuid.uuid4())
        self.generation = 1
        self.timestamp = time.time()
        
        # Calculate optimal dimension based on complexity
        self.dimension = FIBONACCI_DIMENSIONS.get(
            complexity_level, 
            fibonacci(complexity_level + 2)  # Default mapping
        )
        
        # Select target resonance pattern based on complexity
        if complexity_level <= 1:
            self.target_resonance = PHI_RESONANCE_PATTERNS["perfect"]
        elif complexity_level <= 3:
            self.target_resonance = PHI_RESONANCE_PATTERNS["high"]
        else:
            self.target_resonance = PHI_RESONANCE_PATTERNS["good"]
        
        # Initialize genome structure
        self.genome = {
            "genome_id": self.genome_id,
            "type": "phi_hanoi_genome",
            "generation": self.generation,
            "created": self.timestamp,
            "last_modified": self.timestamp,
            "phi_metadata": {
                "phi_value": float(PHI),
                "complexity_level": complexity_level,
                "dimension": self.dimension,
                "target_resonance": self.target_resonance[0],
                "resonance_quality": self.target_resonance[1]
            },
            "codons": []
        }
        
        # Create codons based on phi-harmonic principles
        self._initialize_codons()
        
        # Save initial genome
        self.save_genome()
        
        if debug:
            print(f"Created Phi-Hanoi Genome: {self.genome_id}")
            print(f"Dimension: {self.dimension}")
            print(f"Target Resonance: {self.target_resonance[0]} (Quality: {self.target_resonance[1]})")
    
    def _initialize_codons(self):
        """Initialize genome codons with phi-optimized hanoi tasks"""
        # Number of codons scales with complexity
        num_codons = int(self.complexity_level * PHI_FLOAT)
        
        # Create codons
        for i in range(num_codons):
            # Scale disk count with codon position
            disk_count = max(3, min(10, int(3 + (i * PHI_FLOAT) % 8)))
            
            # Calculate phi-optimized dimension for this disk count
            fib_idx = int(disk_count * PHI_FLOAT)
            dimension = fibonacci(fib_idx)
            
            # Calculate iteration factor (declines with disk count)
            iteration_factor = max(1, int(10 / (disk_count * PHI_CONJUGATE)))
            
            # Create hanoi task codon
            codon = {
                "id": f"hanoi_{i}",
                "type": "task",
                "task_type": "execute_python",
                "disk_count": disk_count,
                "dimension": dimension,
                "iteration_factor": iteration_factor,
                "resonance_target": float((PHI * Decimal(str(disk_count))) % Decimal('1')),
                "script_template": self._get_hanoi_template(i, disk_count, dimension, iteration_factor)
            }
            
            self.genome["codons"].append(codon)
    
    def _get_hanoi_template(self, codon_id, disk_count, dimension, iteration_factor):
        """Generate a hanoi template based on phi-optimized parameters"""
        # Calculate the optimal moves formula for Tower of Hanoi: 2^n - 1
        optimal_moves_formula = f"2**{disk_count} - 1"
        
        return f"""
# Phi-Optimized Tower of Hanoi - Genome {self.genome_id}, Codon {codon_id}
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

print('\\n===== PHI-HARMONIC TOWER OF HANOI - GENOME EXECUTION =====\\n')
print(f'Configuration: {disk_count} disks, {dimension} dimensions (phi-optimized)')
print(f'Genome ID: {self.genome_id}')
print(f'Codon: hanoi_{codon_id}')
print('Measuring quantum advantage through phi-resonance...')

# Create output directory
results_dir = "quantum_outputs/hanoi_genome_results"
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
results_file = f"{{results_dir}}/hanoi_genome_{self.genome_id}_codon_{codon_id}_{{timestamp}}.json"

output = {{
    'genome_id': '{self.genome_id}',
    'codon_id': 'hanoi_{codon_id}',
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
print('\\n✓ Codon execution complete')
"""
    
    def save_genome(self):
        """Save the genome to file"""
        with open(self.genome_file, 'w') as f:
            json.dump(self.genome, f, indent=2)
        
        if self.debug:
            print(f"Genome saved to {self.genome_file}")
    
    def evolve(self):
        """Evolve the genome based on phi-harmonic principles"""
        # Increment generation
        self.generation += 1
        self.genome["generation"] = self.generation
        self.genome["last_modified"] = time.time()
        
        # Evolution changes based on phi-harmonic patterns
        evolution_phase = (self.generation * PHI_FLOAT) % (2 * math.pi)
        
        # Number of mutations follows phi pattern
        mutation_count = int(PHI_FLOAT * (1 + math.sin(evolution_phase)))
        
        # Apply mutations
        mutations_applied = 0
        for _ in range(mutation_count):
            # Select random codon to mutate
            if not self.genome["codons"]:
                break
                
            codon_idx = random.randint(0, len(self.genome["codons"]) - 1)
            codon = self.genome["codons"][codon_idx]
            
            # Apply phi-based mutation
            mutation_type = random.choice(["dimension", "iteration", "disk_count"])
            
            if mutation_type == "dimension":
                # Evolve dimension to next Fibonacci number
                current = codon.get("dimension", 8)
                next_fib_idx = int(math.log(current * PHI_FLOAT) / math.log(PHI_FLOAT))
                codon["dimension"] = fibonacci(next_fib_idx)
                mutations_applied += 1
                
            elif mutation_type == "iteration":
                # Adjust iteration factor with phi
                codon["iteration_factor"] = max(1, int(codon["iteration_factor"] * (PHI_FLOAT - 0.5)))
                mutations_applied += 1
                
            elif mutation_type == "disk_count":
                # Evolve disk count within safe range (3-10)
                current = codon.get("disk_count", 3)
                phi_step = (current * PHI_FLOAT) % 3
                new_count = max(3, min(10, int(current + phi_step - 1)))
                
                if new_count != current:
                    codon["disk_count"] = new_count
                    
                    # Update resonance target
                    codon["resonance_target"] = float((PHI * Decimal(str(new_count))) % Decimal('1'))
                    
                    # Recalculate dimension
                    fib_idx = int(new_count * PHI_FLOAT)
                    codon["dimension"] = fibonacci(fib_idx)
                    
                    # Update script template
                    codon["script_template"] = self._get_hanoi_template(
                        codon["id"].split("_")[1],
                        new_count,
                        codon["dimension"],
                        codon["iteration_factor"]
                    )
                    
                    mutations_applied += 1
            
            # Update the codon
            self.genome["codons"][codon_idx] = codon
        
        # Save evolved genome
        self.save_genome()
        
        if self.debug:
            print(f"Genome evolved to generation {self.generation}")
            print(f"Applied {mutations_applied} mutations")
        
        return mutations_applied
    
    def print_summary(self):
        """Print a summary of the genome"""
        print("\n" + "="*60)
        print(f"🧬 PHI-HARMONIC HANOI GENOME: {self.genome_id}")
        print("="*60)
        print(f"Generation: {self.generation}")
        print(f"Complexity: Level {self.complexity_level}")
        print(f"Dimension: {self.dimension}")
        print(f"Target Resonance: {self.target_resonance[0]:.6f} (Quality: {self.target_resonance[1]}★)")
        print(f"Codons: {len(self.genome['codons'])}")
        
        print("\nCODON SUMMARY:")
        for i, codon in enumerate(self.genome["codons"]):
            print(f"  {i+1}. {codon['id']}: {codon['disk_count']} disks, " + 
                  f"dimension {codon['dimension']}, " +
                  f"target resonance {codon['resonance_target']:.6f}")
        
        print("\n" + "="*60)

class QRPhiHanoiGenerator:
    """
    QR Phi-Harmonic Tower of Hanoi QR Generator
    
    Creates QR sequences from phi-optimized hanoi genomes.
    """
    
    def __init__(self, 
                 genome_file="qr_phi_hanoi_genome.json",
                 output_dir="qr_phi_hanoi_sequence",
                 debug=False):
        """Initialize the QR generator"""
        self.genome_file = genome_file
        self.output_dir = output_dir
        self.debug = debug
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Load genome
        self._load_genome()
    
    def _load_genome(self):
        """Load the genome from file"""
        try:
            with open(self.genome_file, 'r') as f:
                self.genome = json.load(f)
            
            if self.debug:
                print(f"Loaded genome from {self.genome_file}")
                print(f"Genome ID: {self.genome['genome_id']}")
                print(f"Generation: {self.genome['generation']}")
                print(f"Codons: {len(self.genome['codons'])}")
        except Exception as e:
            print(f"Error loading genome: {e}")
            self.genome = None
    
    def generate_qr_sequence(self):
        """Generate QR sequence from genome"""
        if not self.genome:
            print("No genome loaded")
            return []
        
        sequence_dir = os.path.join(
            self.output_dir,
            f"sequence_{self.genome['genome_id']}_{int(time.time())}"
        )
        os.makedirs(sequence_dir, exist_ok=True)
        
        if self.debug:
            print(f"Generating QR sequence in {sequence_dir}")
        
        qr_files = []
        
        # Create a QR code for each codon
        for i, codon in enumerate(self.genome["codons"]):
            try:
                # Create payload
                payload = {
                    "task_type": codon["task_type"],
                    "python_script": codon["script_template"],
                    "genome_id": self.genome["genome_id"],
                    "codon_id": codon["id"],
                    "generation": self.genome["generation"],
                    "phi_metadata": {
                        "dimension": codon["dimension"],
                        "disk_count": codon["disk_count"],
                        "target_resonance": codon["resonance_target"],
                        "phi": float(PHI)
                    }
                }
                
                # Convert to JSON
                json_data = json.dumps(payload)
                
                # Compress for larger scripts
                compressed = base64.b64encode(json_data.encode('utf-8')).decode('utf-8')
                
                # Generate QR
                qr_filename = os.path.join(
                    sequence_dir,
                    f"qr_hanoi_{codon['disk_count']}disk_{codon['id']}_{i+1:02d}.png"
                )
                
                # Import chunker for large payloads
                from qr_sequence_chunker import QRSequenceChunker
                
                # If payload is large, use chunker
                chunker = QRSequenceChunker(max_chunk_size=2000)
                
                if len(compressed) > 2500:  # If too large for a single QR code
                    chunks = chunker.chunk_payload(json_data)
                    chunk_count = len(chunks)
                    
                    # Create QR code for first chunk only in this demo
                    chunk = chunks[0]
                    chunk_data = json.dumps(chunk)
                    
                    import qrcode
                    qr = qrcode.QRCode(
                        version=None,  # Auto-determine version
                        error_correction=qrcode.constants.ERROR_CORRECT_M,
                        box_size=10,
                        border=4,
                    )
                    qr.add_data(chunk_data)
                    qr.make(fit=True)
                    
                    # Update filename to indicate chunking
                    qr_filename = qr_filename.replace(".png", f"_chunk1of{chunk_count}.png")
                    
                    if self.debug:
                        print(f"Payload chunked into {chunk_count} parts, saving first chunk")
                else:
                    # For smaller payloads, create a single QR code
                    import qrcode
                    qr = qrcode.QRCode(
                        version=None,  # Auto-determine version
                        error_correction=qrcode.constants.ERROR_CORRECT_M,
                        box_size=10,
                        border=4,
                    )
                    qr.add_data(f"COMPRESSED:{compressed}")
                    qr.make(fit=True)
                
                img = qr.make_image(fill_color="black", back_color="white")
                img.save(qr_filename)
                
                qr_files.append(qr_filename)
                
                if self.debug:
                    print(f"Generated QR for codon {codon['id']}: {qr_filename}")
            
            except Exception as e:
                print(f"Error generating QR for codon {codon['id']}: {e}")
        
        # Create a metadata file
        metadata = {
            "genome_id": self.genome["genome_id"],
            "generation": self.genome["generation"],
            "timestamp": time.time(),
            "qr_count": len(qr_files),
            "sequence_dir": sequence_dir,
            "qr_files": [os.path.basename(f) for f in qr_files]
        }
        
        metadata_file = os.path.join(sequence_dir, "sequence_metadata.json")
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        return qr_files

# Main functions to integrate with run_qr_system.py
def create_phi_hanoi_genome(complexity_level=3, output_file="qr_phi_hanoi_genome.json"):
    """Create a new phi-optimized hanoi genome"""
    genome = QRPhiHanoiGenome(
        genome_file=output_file,
        complexity_level=complexity_level,
        debug=True
    )
    
    genome.print_summary()
    
    return output_file

def evolve_phi_hanoi_genome(genome_file="qr_phi_hanoi_genome.json"):
    """Evolve an existing phi-optimized hanoi genome"""
    genome = QRPhiHanoiGenome(
        genome_file=genome_file,
        debug=True
    )
    
    mutations = genome.evolve()
    
    genome.print_summary()
    
    return mutations

def generate_phi_hanoi_sequence(genome_file="qr_phi_hanoi_genome.json", 
                               output_dir="qr_phi_hanoi_sequence"):
    """Generate QR sequence from phi-optimized hanoi genome"""
    generator = QRPhiHanoiGenerator(
        genome_file=genome_file,
        output_dir=output_dir,
        debug=True
    )
    
    qr_files = generator.generate_qr_sequence()
    
    print(f"Generated {len(qr_files)} QR codes in {output_dir}")
    
    return qr_files

if __name__ == "__main__":
    print("QR Phi-Harmonic Tower of Hanoi Genome - By Vaughn Scott (Extended)")
    
    # Create a new genome
    genome_file = create_phi_hanoi_genome(complexity_level=3)
    
    # Evolve the genome
    evolve_phi_hanoi_genome(genome_file)
    
    # Generate QR sequence
    generate_phi_hanoi_sequence(genome_file)
