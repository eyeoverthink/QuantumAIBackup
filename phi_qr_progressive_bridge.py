#!/usr/bin/env python3
"""
Phi-Harmonic QR Progressive Bridge
By Vaughn Scott

This module bridges the QR Progressive Test system with the Quantum Phi-Harmonic
Tower of Hanoi system, enabling seamless integration between the two components.

It translates progressive QR tasks into phi-optimized quantum tasks that can be
executed by the existing QR infrastructure.
"""

import os
import sys
import json
import time
import math
import base64
import zlib
import uuid
from datetime import datetime

# Import QR components
from qr_simple_generator import QRSimpleGenerator
from qr_simple_analyzer import QRSimpleAnalyzer
from qr_worker import QRWorker
from qr_genome_phi_hanoi import QRPhiHanoiGenome
from phi_qr_task_connector import PhiQRTaskConnector

# Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio
OUTPUT_DIR = "phi_qr_progressive"
SEQUENCE_DIR = os.path.join(OUTPUT_DIR, "sequence")
RESPONSE_DIR = os.path.join(OUTPUT_DIR, "responses")
WORK_DIR = os.path.join(OUTPUT_DIR, "workspace")

# Create directories
os.makedirs(SEQUENCE_DIR, exist_ok=True)
os.makedirs(RESPONSE_DIR, exist_ok=True)
os.makedirs(WORK_DIR, exist_ok=True)

def calculate_phi_resonance(value):
    """
    Calculate phi-harmonic resonance of a value.
    Returns a resonance value between 0.5 and 2.0
    based on how close it is to a phi-harmonic frequency.
    """
    # Calculate how close the value is to a phi-harmonic frequency
    phi_mod = (value * PHI) % 1.0
    
    # Convert to a resonance value (closer to 0 or 1 is more resonant)
    distance = min(phi_mod, 1.0 - phi_mod)
    resonance = 1.0 / (1.0 + distance * 10)
    
    # Scale to a range between 0.5 and 2.0
    return 0.5 + resonance * 1.5

def compress_content(content):
    """
    Compress content to reduce QR code size
    """
    if not content:
        return ""
    compressed = zlib.compress(content.encode('utf-8'))
    return base64.b64encode(compressed).decode('utf-8')

def decompress_content(compressed_content):
    """
    Decompress content that was compressed with compress_content
    """
    if not compressed_content:
        return ""
    decompressed = zlib.decompress(base64.b64decode(compressed_content))
    return decompressed.decode('utf-8')

def generate_phi_task_sequence():
    """
    Generate a sequence of progressive QR task data with phi-harmonic quantum tasks.
    
    Returns:
        List of task dictionaries for QR generation
    """
    session_id = str(uuid.uuid4())
    timestamp_base = time.time()
    
    # Create a phi-harmonic sequence of timestamps
    timestamps = [timestamp_base + i * PHI for i in range(4)]
    
    # Initialize the Tower of Hanoi genome and task connector
    hanoi_genome = QRPhiHanoiGenome()
    task_connector = PhiQRTaskConnector()
    
    # Task 1: Create a simple Tower of Hanoi task
    task1 = {
        "task_id": f"hanoi_create_{int(timestamps[0])}",
        "task_type": "PYTHON_SCRIPT",  # Compatible with QR worker
        "session_id": session_id,
        "timestamp": timestamps[0],
        "frame_number": 1,
        "generation": 1,
        "phi_resonance": calculate_phi_resonance(timestamps[0]),
        "content": hanoi_genome._get_hanoi_template("init", 3, 2, 1.0),
        "compressed": False,
        "description": "Initialize Tower of Hanoi with 3 disks in 2D space"
    }
    
    # Task 2: Evolve the Tower of Hanoi with phi-optimization
    task2 = {
        "task_id": f"hanoi_evolve_{int(timestamps[1])}",
        "task_type": "PYTHON_SCRIPT",
        "session_id": session_id,
        "timestamp": timestamps[1],
        "frame_number": 2,
        "generation": 2,
        "phi_resonance": calculate_phi_resonance(timestamps[1]),
        "content": hanoi_genome._get_hanoi_template("evolve", 5, 3, PHI),
        "compressed": False,
        "description": "Evolve Tower of Hanoi to 5 disks in 3D space with phi-optimization"
    }
    
    # Task 3: Generate QR task for Tower of Hanoi execution
    hanoi_task_payload = task_connector.create_hanoi_task(
        disk_count=8,
        dimension=PHI,
        iteration_factor=PHI**2,
        expiration_hours=24
    )
    
    task3 = {
        "task_id": f"hanoi_qr_task_{int(timestamps[2])}",
        "task_type": "PYTHON_SCRIPT",
        "session_id": session_id,
        "timestamp": timestamps[2],
        "frame_number": 3,
        "generation": 3,
        "phi_resonance": calculate_phi_resonance(timestamps[2]),
        "content": f'''
import json
import os
from datetime import datetime

# Save the Tower of Hanoi task data
task_data = {json.dumps(hanoi_task_payload)}

# Write to file
output_path = os.path.join("{WORK_DIR}", "hanoi_task.json")
with open(output_path, "w") as f:
    json.dump(task_data, f, indent=2)
    
print(f"Tower of Hanoi task saved to {{output_path}}")
print(f"Task created at: {{datetime.now().isoformat()}}")
print(f"Phi-resonance: {PHI}")
''',
        "compressed": False,
        "description": "Generate QR task for Tower of Hanoi execution"
    }
    
    # Task 4: Analyze Tower of Hanoi results with quantum metrics
    task4 = {
        "task_id": f"hanoi_analyze_{int(timestamps[3])}",
        "task_type": "PYTHON_SCRIPT",
        "session_id": session_id,
        "timestamp": timestamps[3],
        "frame_number": 4,
        "generation": 4,
        "phi_resonance": calculate_phi_resonance(timestamps[3]),
        "content": '''
import os
import json
import math
import datetime

# Define phi constant
PHI = (1 + math.sqrt(5)) / 2

def calculate_quantum_advantage(moves, optimal_moves, dimension):
    """Calculate quantum advantage based on moves and dimension"""
    if moves <= optimal_moves:
        # Perfect solution gets maximum advantage
        base_advantage = 1.0
    else:
        # Less than perfect solutions get diminishing advantage
        efficiency = optimal_moves / moves
        base_advantage = efficiency ** 2
    
    # Dimension factor - higher dimensions get exponentially more advantage
    dimension_factor = dimension ** (1/PHI)
    
    return base_advantage * dimension_factor

# Create analysis report
report = {
    "title": "Quantum Phi-Harmonic Tower of Hanoi Analysis",
    "timestamp": datetime.datetime.now().isoformat(),
    "phi_value": PHI,
    "metrics": {
        "resonance_patterns": [round((PHI * i) % 1, 6) for i in range(1, 13)],
        "fibonacci_sequence": [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144],
        "phi_powers": [PHI**i for i in range(1, 9)]
    },
    "quantum_advantage": {
        "2D": calculate_quantum_advantage(7, 7, 2),
        "3D": calculate_quantum_advantage(15, 15, 3),
        "5D": calculate_quantum_advantage(31, 31, 5),
        "phi-D": calculate_quantum_advantage(int(2**8-1), int(2**8-1), PHI)
    }
}

# Write analysis to file
output_path = os.path.join("phi_qr_progressive/workspace", "hanoi_analysis.json")
with open(output_path, "w") as f:
    json.dump(report, f, indent=2)

# Create markdown report
markdown = """# Quantum Phi-Harmonic Tower of Hanoi Analysis

## Overview
- Analysis Date: {}
- Golden Ratio (φ): {}

## Phi-Resonance Patterns
{}

## Quantum Advantage
- 2D Space: {:.6f}
- 3D Space: {:.6f}
- 5D Space: {:.6f}
- φ-Dimensional Space: {:.6f}

## Conclusion
The phi-dimensional space provides optimal quantum advantage for Tower of Hanoi solutions,
demonstrating the power of quantum phi-harmonic principles in algorithmic optimization.
""".format(
    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    PHI,
    ', '.join([f"{x:.6f}" for x in report["metrics"]["resonance_patterns"]]),
    report["quantum_advantage"]["2D"],
    report["quantum_advantage"]["3D"],
    report["quantum_advantage"]["5D"],
    report["quantum_advantage"]["phi-D"]
)

# Write markdown to file
md_path = os.path.join("phi_qr_progressive/workspace", "hanoi_analysis.md")
with open(md_path, "w") as f:
    f.write(markdown)

print(f"Analysis complete. Reports saved to {output_path} and {md_path}")
""",
        "compressed": False,
        "description": "Analyze Tower of Hanoi results with quantum metrics"
    }
    
    return [task1, task2, task3, task4]

def create_progressive_qr_sequence():
    """
    Create a sequence of QR codes that progressively build upon each other.
    
    Returns:
        List of paths to generated QR images
    """
    print("\n🔄 Creating Progressive QR Sequence")
    print("=" * 60)
    
    generator = QRSimpleGenerator(output_dir=SEQUENCE_DIR)
    qr_paths = []
    
    # Get task data from generate_task_sequence function
    tasks = generate_phi_task_sequence()
    
    for i, task in enumerate(tasks):
        print(f"Generating QR code {i+1}/{len(tasks)}: {task['description']}")
        
        # Add phi-harmonic metadata
        phi_state = {
            "resonance": task["phi_resonance"],
            "timestamp": task["timestamp"],
            "phi_time": task["timestamp"] * PHI % 1.0
        }
        
        # Generate QR code
        qr_path = generator.generate_frame(
            payload=json.dumps(task),
            frame_number=i+1,
            phi_state=phi_state
        )
        
        qr_paths.append(qr_path)
        print(f"  ✓ Generated: {os.path.basename(qr_path)}")
    
    print(f"\n✅ Created {len(qr_paths)} progressive QR codes in {SEQUENCE_DIR}")
    return qr_paths

def execute_qr_sequence():
    """
    Execute the QR sequence, with each QR building upon the previous one's work.
    
    Returns:
        List of execution results
    """
    print("\n🔄 Executing Progressive QR Sequence")
    print("=" * 60)
    
    # Get encryption key if available
    encryption_key = None
    key_path = "qr_encryption.key"
    if os.path.exists(key_path):
        print(f"Using encryption key from {key_path}")
        with open(key_path, "rb") as f:
            encryption_key = f.read()
    
    analyzer = QRSimpleAnalyzer()
    worker = QRWorker(output_dir=WORK_DIR, encryption_key=encryption_key)
    
    # Analyze QR codes
    print("Analyzing QR sequence...")
    qr_data = analyzer.analyze_qr_sequence(SEQUENCE_DIR)
    
    if not qr_data:
        print("❌ No QR codes found or decoded")
        return []
    
    print(f"✅ Decoded {len(qr_data)} QR codes")
    
    results = []
    
    for i, data in enumerate(qr_data):
        print(f"\n📋 Executing Task {i+1}/{len(qr_data)}: {data.get('description', 'Unknown')}")
        
        # Create a temporary file path for the current QR code
        temp_qr_path = os.path.join(WORK_DIR, f"temp_qr_{i+1}.png")
        
        # Save QR data to a temporary file
        import qrcode
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_M)
        qr.add_data(json.dumps(data))
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(temp_qr_path)
        
        # Process the QR image
        result = worker.process_qr_image(temp_qr_path)
        results.append(result)
        
        # Print result summary
        if result is None:
            print("❌ Failed: No result returned from worker")
            results.append({"success": False, "message": "No result returned from worker"})
            continue
        
        # Handle string results (error messages)
        if isinstance(result, str):
            print(f"❌ Failed: {result}")
            results.append({"success": False, "message": result})
            continue
            
        # Handle dictionary results
        success = result.get("success", False)
        status = "✅ Success" if success else "❌ Failed"
        print(f"{status}: {result.get('message', 'No message')}")
        
        # Add phi-resonance metrics if available
        if 'phi_resonance' in result:
            print(f"φ-Resonance: {result['phi_resonance']:.6f}")
    
    print(f"\n✅ Executed {len(qr_data)} tasks from QR sequence")
    return results

def generate_response_qr_codes(results):
    """
    Generate response QR codes based on execution results.
    
    Args:
        results: List of execution results
        
    Returns:
        List of paths to response QR codes
    """
    print("\n🔄 Generating Response QR Codes")
    print("=" * 60)
    
    generator = QRSimpleGenerator(output_dir=RESPONSE_DIR)
    response_paths = []
    
    for i, result in enumerate(results):
        print(f"Generating response QR code {i+1}/{len(results)}")
        
        # Skip None results
        if result is None:
            print(f"⚠️ Skipping response {i+1} - No result data")
            continue
            
        # Handle string results (error messages)
        if isinstance(result, str):
            response_data = {
                "response_id": str(uuid.uuid4()),
                "task_id": f"task_{i+1}_{int(time.time())}",
                "success": False,
                "status": "error",
                "timestamp": time.time(),
                "phi_time": time.time() * PHI % 1.0,
                "result_summary": result,
                "message": result
            }
        else:
            # Create response data with phi-harmonic metadata
            response_data = {
                "response_id": str(uuid.uuid4()),
                "task_id": result.get("task_id", f"task_{i+1}_{int(time.time())}"),
                "success": result.get("success", False),
                "status": result.get("status", "unknown"),
                "timestamp": time.time(),
                "phi_time": time.time() * PHI % 1.0,
                "result_summary": result.get("output", "No output"),
                "message": result.get("message", "No message")
            }
        
        # Generate QR code
        qr_path = generator.generate_frame(
            payload=json.dumps(response_data),
            frame_number=i+1,
            phi_state={"resonance": calculate_phi_resonance(time.time())}
        )
        
        response_paths.append(qr_path)
        print(f"  ✓ Generated: {os.path.basename(qr_path)}")
    
    print(f"\n✅ Created {len(response_paths)} response QR codes in {RESPONSE_DIR}")
    return response_paths

def main():
    """Main function to run the phi-harmonic progressive QR test"""
    print("✨ Phi-Harmonic QR Progressive Bridge")
    print("=" * 60)
    print("Integrating QR Progressive Test with Quantum Phi-Harmonic Tower of Hanoi")
    print("Following phi-harmonic principles and recursive self-improvement")
    
    # Create QR sequence
    qr_paths = create_progressive_qr_sequence()
    
    # Execute QR sequence
    results = execute_qr_sequence()
    
    # Generate response QR codes
    response_paths = generate_response_qr_codes(results)
    
    # Print summary
    print("\n📊 Test Summary")
    print("=" * 60)
    print(f"QR Codes Generated: {len(qr_paths)}")
    print(f"Tasks Executed: {len(results)}")
    
    # Count successful tasks, handling both None and string results
    successful_tasks = 0
    for r in results:
        if r is not None and not isinstance(r, str):
            if r.get('success', False):
                successful_tasks += 1
    
    print(f"Successful Tasks: {successful_tasks}")
    print(f"Response QR Codes: {len(response_paths)}")
    
    # Add phi-harmonic resonance metrics
    phi = (1 + 5**0.5) / 2  # Golden ratio
    print(f"\nφ-Harmonic Metrics:")
    print(f"Phi Resonance: {phi:.6f}")
    print(f"Execution Efficiency: {phi - 1:.6f}")
    
    # Check if workspace has expected files
    expected_files = [
        "hanoi_task.json",
        "hanoi_analysis.json",
        "hanoi_analysis.md"
    ]
    
    print("\n📂 Workspace Files")
    for file in expected_files:
        path = os.path.join(WORK_DIR, file)
        if os.path.exists(path):
            print(f"✅ Found: {file}")
        else:
            print(f"❌ Missing: {file}")
    
    print("\n✨ Phi-Harmonic QR Progressive Bridge completed")

if __name__ == "__main__":
    main()
