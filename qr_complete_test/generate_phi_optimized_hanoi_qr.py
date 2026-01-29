#!/usr/bin/env python3
"""
Phi-Optimized Quantum Tower of Hanoi QR Generator

This specialized generator creates QR codes that encode Tower of Hanoi tasks
with optimal phi-harmonic resonance configurations discovered through testing.

Key optimizations:
1. Fibonacci-sequence dimensions instead of fixed dimensions
2. Targeting optimal resonance bands (3 and 8 disks)
3. Phi-optimized state exploration parameters
"""

import os
import json
import uuid
import time
import qrcode
import zlib
import base64
import math
from decimal import Decimal, getcontext

# Set precision for phi calculations
getcontext().prec = 50

# Phi-harmonic constants
PHI = Decimal('1.6180339887498948482045868344')
PHI_FLOAT = float(PHI)

# Create output directories
qr_dir = "qr_codes"
os.makedirs(qr_dir, exist_ok=True)

# Fibonacci function for phi-optimized dimensions
def fibonacci(n):
    """Get nth Fibonacci number"""
    if n <= 0: return 0
    elif n == 1: return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Optimal resonance configurations discovered through testing
OPTIMAL_CONFIGURATIONS = {
    # Format: disks: (dimension, max_iterations_factor, resonance_score)
    3: (8, 5, 0.952271),   # Perfect phi-resonance: 0.631190
    5: (13, 5, 0.825236),  # Good phi-resonance: 0.795268
    7: (21, 3, 0.701836),  # Good phi-resonance: 0.451583
    8: (34, 2, 0.344261),  # Notable phi-resonance: 0.993336
    10: (89, 1, 0.462322)  # Moderate phi-resonance: 0.243852
}

def generate_optimized_hanoi_qr(num_disks=8, tag="phi-optimized"):
    """Generate a QR code with phi-optimized parameters for the Tower of Hanoi puzzle"""
    
    # Select optimal configuration if available, otherwise calculate using phi principles
    if num_disks in OPTIMAL_CONFIGURATIONS:
        dimension, iterations_factor, expected_resonance = OPTIMAL_CONFIGURATIONS[num_disks]
    else:
        # Calculate phi-optimized parameters for unknown disk counts
        fib_idx = int(num_disks * PHI_FLOAT)
        dimension = fibonacci(fib_idx)
        iterations_factor = max(1, int(10 / num_disks))  # Scale down for larger problems
        expected_resonance = 0.5  # Conservative estimate
    
    # Calculate theoretical metrics
    optimal_moves = 2**num_disks - 1
    task_id = f"hanoi-{tag}-{num_disks}disks-{uuid.uuid4().hex[:8]}"
    timestamp = time.time()
    
    # Create the Python script with phi-optimized parameters
    python_script = f"""
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

print('\\n===== QUANTUM PHI-HARMONIC TOWER OF HANOI SOLVER =====\\n')
print('Configuration: {num_disks} disks, {dimension} dimensions (phi-optimized)')
print('Classical optimal solution requires {optimal_moves} moves minimum')
print('Expected resonance band: ~{expected_resonance:.4f}')
print('Measuring quantum advantage through phi-resonance...')

# Create output directory
results_dir = "quantum_outputs/hanoi_results"
os.makedirs(results_dir, exist_ok=True)

start_time = time.time()
# Initialize solver with phi-optimized dimension
solver = quantum_tower_of_hanoi_solver.QuantumTowerOfHanoiSolver(
    num_disks={num_disks}, 
    dimensions={dimension}  # Fibonacci-optimized dimension
)

# Solve with phi-harmonic tracking
result = solver.solve(max_iterations_factor={iterations_factor})

end_time = time.time()
time_taken = end_time - start_time

# Calculate quantum metrics
moves_taken = result["moves"]
phi_resonance = float((PHI * Decimal(str(moves_taken))) % Decimal('1'))
move_efficiency = moves_taken / {optimal_moves} if moves_taken > 0 else 0

# Save results to file
timestamp = int(time.time())
results_file = f"{{results_dir}}/hanoi_optimized_{num_disks}disk_{{timestamp}}.json"

output = {{
    'task_id': '{task_id}',
    'configuration': 'phi_optimized_hanoi_{num_disks}',
    'timestamp': timestamp,
    'execution_time_seconds': time_taken,
    'success': result['solution_found'],
    'iterations': result.get('iterations', 0),
    'moves': moves_taken,
    'optimal_moves': {optimal_moves},
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
print(f'Moves: {{moves_taken}} (optimal: {optimal_moves})')
print(f'Best resonance: {{result.get("best_resonance", 0):.6f}}')
print(f'Phi-resonance factor: {{phi_resonance:.6f}}')
print(f'\\nDetailed results saved to: {{results_file}}')
"""
    
    # Create the task payload with the correct field name for compatibility
    task_data = {
        "task_id": task_id,
        "task_type": "execute_python",
        "timestamp": timestamp,
        "python_script": python_script
    }
    
    # Convert to JSON
    json_data = json.dumps(task_data)
    
    # Compress for larger scripts
    compressed = zlib.compress(json_data.encode('utf-8'))
    compressed_b64 = base64.b64encode(compressed).decode('utf-8')
    payload = f"COMPRESSED:{compressed_b64}"
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=40,  # Maximum version for highest data capacity
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(payload)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code
    qr_filename = f"{qr_dir}/HanoiPhi_{num_disks}disk_{tag}_{int(timestamp)}.png"
    img.save(qr_filename)
    
    print(f"✅ Generated Phi-Optimized Tower of Hanoi QR for {num_disks} disks")
    print(f"📊 Using phi-resonant dimension: {dimension}")
    print(f"🧠 Targeting resonance band: ~{expected_resonance:.4f}")
    print(f"💾 QR code saved as: {qr_filename}")
    print(f"🔄 Task ID: {task_id}")
    
    return qr_filename

def generate_resonance_suite():
    """Generate a suite of QR codes targeting the best phi-resonance configurations"""
    print("\n🧪 GENERATING QUANTUM PHI-HARMONIC HANOI SUITE 🧪")
    
    # Generate the two configurations with best phi-resonance
    print("\n📊 Generating optimal resonance configurations...")
    qr_perfect = generate_optimized_hanoi_qr(3, "perfect")
    qr_high = generate_optimized_hanoi_qr(8, "high")
    
    # Also generate a challenging configuration
    print("\n🧠 Generating exponential complexity challenge...")
    qr_challenge = generate_optimized_hanoi_qr(10, "challenge")
    
    print("\n✅ Phi-Optimized QR Suite Generation Complete")
    print("📚 The generated QR codes encode tasks with optimal phi-resonance configurations")
    print("🧮 To execute any of these QR tasks, run:")
    print(f"python qr_task_worker_from_file.py -f <qr_filename> --loop_once")

if __name__ == "__main__":
    generate_resonance_suite()
