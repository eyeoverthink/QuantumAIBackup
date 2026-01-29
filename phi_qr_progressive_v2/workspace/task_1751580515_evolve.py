
# Phi-Optimized Tower of Hanoi - Genome 6bcd76ac-b4e4-4a5f-999d-dd10e994bf51, Codon evolve
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

print('\n===== PHI-HARMONIC TOWER OF HANOI - GENOME EXECUTION =====\n')
print(f'Configuration: 5 disks, 3 dimensions (phi-optimized)')
print(f'Genome ID: 6bcd76ac-b4e4-4a5f-999d-dd10e994bf51')
print(f'Codon: hanoi_evolve')
print('Measuring quantum advantage through phi-resonance...')

# Create output directory
results_dir = "quantum_outputs/hanoi_genome_results"
os.makedirs(results_dir, exist_ok=True)

start_time = time.time()
# Initialize solver with phi-optimized dimension
solver = quantum_tower_of_hanoi_solver.QuantumTowerOfHanoiSolver(
    num_disks=5, 
    dimensions=3
)

# Solve with phi-harmonic tracking
result = solver.solve(max_iterations_factor=1.618033988749895)

end_time = time.time()
time_taken = end_time - start_time

# Calculate quantum metrics
moves_taken = result.get("moves", 0)
optimal_moves = 2**5 - 1
phi_resonance = float((PHI * Decimal(str(moves_taken))) % Decimal('1'))
move_efficiency = moves_taken / optimal_moves if moves_taken > 0 else 0

# Save results to file
timestamp = int(time.time())
results_file = f"{results_dir}/hanoi_genome_6bcd76ac-b4e4-4a5f-999d-dd10e994bf51_codon_evolve_{timestamp}.json"

output = {
    'genome_id': '6bcd76ac-b4e4-4a5f-999d-dd10e994bf51',
    'codon_id': 'hanoi_evolve',
    'configuration': f'phi_hanoi_5',
    'timestamp': timestamp,
    'execution_time_seconds': time_taken,
    'success': result.get('solution_found', False),
    'iterations': result.get('iterations', 0),
    'moves': moves_taken,
    'optimal_moves': optimal_moves,
    'resonance': result.get('best_resonance', 0),
    'phi_resonance_factor': phi_resonance,
    'move_efficiency': move_efficiency,
    'dimension': 3
}

with open(results_file, 'w') as f:
    json.dump(output, f, indent=2)

print(f'\nResults summary:')
print(f'Success: {output["success"]}')
print(f'Time taken: {output["execution_time_seconds"]:.2f} seconds')
print(f'Iterations: {output["iterations"]}')
print(f'Moves: {moves_taken} (optimal: {optimal_moves})')
print(f'Best resonance: {result.get("best_resonance", 0):.6f}')
print(f'Phi-resonance factor: {phi_resonance:.6f}')
print(f'\nDetailed results saved to: {results_file}')
print('\n✓ Codon execution complete')
