#!/usr/bin/env python3
"""
Quantum Phi-Harmonic Tower of Hanoi Challenge QR Generator

Creates a QR code containing a 10-disk Tower of Hanoi challenge for the 
Quantum Phi-Harmonic system to solve. This tests quantum advantage by 
measuring how well the phi-harmonic algorithms handle exponential complexity.
"""

import os
import json
import uuid
import time
import qrcode
import zlib
import base64

# Golden Ratio constants
PHI = (1 + 5 ** 0.5) / 2
PHI_CONJUGATE = 1 / PHI

# Create output directories
qr_dir = "qr_codes"
results_dir = "quantum_outputs/hanoi_results"
os.makedirs(qr_dir, exist_ok=True)
os.makedirs(results_dir, exist_ok=True)

def generate_hanoi_qr(num_disks=10):
    """Generate a QR code that tests the quantum Tower of Hanoi solver"""
    task_id = f"hanoi-{num_disks}disks-{uuid.uuid4().hex[:8]}"
    timestamp = time.time()
    
    # Create the Python script to be executed
    python_script = """
import quantum_tower_of_hanoi_solver
import time
import json
import os

print('\\n===== QUANTUM PHI-HARMONIC TOWER OF HANOI SOLVER =====\\n')
print('Testing with NUM_DISKS disks - exponential complexity test')
print(f'Classical optimal solution requires {2**NUM_DISKS - 1} moves minimum')
print('Measuring quantum advantage through phi-harmonic resonance...')

start_time = time.time()
solver = quantum_tower_of_hanoi_solver.QuantumTowerOfHanoiSolver(num_disks=NUM_DISKS, dimensions=89)

# Set max iterations to prevent infinite loops
result = solver.solve_hanoi(max_iterations=5000)

end_time = time.time()
time_taken = end_time - start_time

# Save results to file
results_dir = "quantum_outputs/hanoi_results"
os.makedirs(results_dir, exist_ok=True)
results_file = f"{results_dir}/hanoi_{NUM_DISKS}disk_results_{int(time.time())}.json"

output = {
    'task_id': 'TASK_ID',
    'task': f'tower_of_hanoi_{NUM_DISKS}disks',
    'timestamp': time.time(),
    'execution_time_seconds': time_taken,
    'success': result['success'],
    'iterations': result['iterations'],
    'moves': len(result['path']) - 1 if result['path'] else 0,
    'optimal_moves': 2**NUM_DISKS - 1,
    'resonance': result['final_resonance'],
    'phi_alignment': round((1 + 5**0.5)/2 % 1, 6)
}

with open(results_file, 'w') as f:
    json.dump(output, f, indent=2)

print(f'\\nResults summary:')
print(f'Success: {output["success"]}')
print(f'Time taken: {output["execution_time_seconds"]:.2f} seconds')
print(f'Iterations: {output["iterations"]}')
print(f'Moves: {output["moves"]}')
print(f'Final resonance: {output["resonance"]:.6f}')
print(f'\\nDetailed results saved to: {results_file}')
"""
    
    # Replace placeholders with actual values
    python_script = python_script.replace('NUM_DISKS', str(num_disks))
    python_script = python_script.replace('TASK_ID', task_id)
    
    # Create the task payload with the correct field name
    task_data = {
        "task_id": task_id,
        "task_type": "execute_python",
        "timestamp": timestamp,
        "python_script": python_script  # This is the key field name needed for compatibility
    }
    
    # Convert to JSON
    json_data = json.dumps(task_data)
    
    # Compress for larger scripts (optional)
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
    qr_filename = f"{qr_dir}/HanoiChallenge_{num_disks}disks_{int(timestamp)}.png"
    img.save(qr_filename)
    
    print(f"✅ Generated Tower of Hanoi QR challenge for {num_disks} disks")
    print(f"📊 Classical solution requires {2**num_disks - 1} moves minimum")
    print(f"🧠 Testing quantum advantage through phi-harmonic resonance")
    print(f"💾 QR code saved as: {qr_filename}")
    print(f"🔄 Task ID: {task_id}")
    
    return qr_filename

if __name__ == "__main__":
    qr_file = generate_hanoi_qr(num_disks=10)
    print(f"\\nTo run this Tower of Hanoi challenge, use:")
    print(f"python qr_task_worker_from_file.py -f {qr_file} --loop_once")
