#!/usr/bin/env python3
"""
QR Progressive Test - Testing Progressive, Recursive QR Code Chain
By Vaughn Scott

This script tests the QR Flipbook DNA System with a series of QR codes that
progressively build upon each other's work, demonstrating recursive and
progressive capabilities.

Each QR code in the sequence performs a specific task:
1. First QR: Creates a Python file with hello world
2. Second QR: Modifies and improves the created file
3. Third QR: Exports the code to JSON for analysis
4. Fourth QR: Opens and analyzes the exported data
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

# Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio
OUTPUT_DIR = "qr_progressive_test"
SEQUENCE_DIR = os.path.join(OUTPUT_DIR, "sequence")
RESPONSE_DIR = os.path.join(OUTPUT_DIR, "responses")
WORK_DIR = os.path.join(OUTPUT_DIR, "workspace")

# Create directories
os.makedirs(SEQUENCE_DIR, exist_ok=True)
os.makedirs(RESPONSE_DIR, exist_ok=True)
os.makedirs(WORK_DIR, exist_ok=True)

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
    
    # QR Code 1: Create a Python file with hello world
    task1 = {
        "task_id": str(uuid.uuid4()),
        "task_type": "CREATE_FILE",
        "phi_resonance": 1.0 / PHI,
        "timestamp": time.time(),
        "parameters": {
            "file_path": os.path.join(WORK_DIR, "hello_world.py"),
            "content": """#!/usr/bin/env python3
\"\"\"
Hello World - Created by QR Code 1
\"\"\"

def main():
    print("Hello, World!")
    print(f"I was created by QR Code 1")

if __name__ == "__main__":
    main()
"""
        }
    }
    
    # QR Code 2: Modify and improve the file
    task2 = {
        "task_id": str(uuid.uuid4()),
        "task_type": "MODIFY_FILE",
        "phi_resonance": 1.0 / (PHI * PHI),
        "timestamp": time.time() + 1,
        "parameters": {
            "file_path": os.path.join(WORK_DIR, "hello_world.py"),
            "modifications": [
                {
                    "type": "add_function",
                    "name": "calculate_phi",
                    "content": """
def calculate_phi():
    \"\"\"Calculate the golden ratio (phi)\"\"\"
    return (1 + math.sqrt(5)) / 2
"""
                },
                {
                    "type": "add_import",
                    "module": "math"
                },
                {
                    "type": "modify_function",
                    "name": "main",
                    "content": """
def main():
    print("Hello, Enhanced World!")
    print(f"I was created by QR Code 1 and improved by QR Code 2")
    phi = calculate_phi()
    print(f"The golden ratio (phi) is: {phi}")
    print(f"Phi resonance: {time.time() * phi % 1.0:.6f}")
"""
                },
                {
                    "type": "add_import",
                    "module": "time"
                }
            ]
        }
    }
    
    # QR Code 3: Export the code to JSON for analysis
    task3 = {
        "task_id": str(uuid.uuid4()),
        "task_type": "EXPORT_TO_JSON",
        "phi_resonance": 1.0 / (PHI * PHI * PHI),
        "timestamp": time.time() + 2,
        "parameters": {
            "source_file": os.path.join(WORK_DIR, "hello_world.py"),
            "export_file": os.path.join(WORK_DIR, "code_analysis.json"),
            "analysis_type": "structure",
            "include_metrics": True
        }
    }
    
    # QR Code 4: Open and analyze the exported data
    task4 = {
        "task_id": str(uuid.uuid4()),
        "task_type": "ANALYZE_DATA",
        "phi_resonance": 1.0 / (PHI * PHI * PHI * PHI),
        "timestamp": time.time() + 3,
        "parameters": {
            "source_file": os.path.join(WORK_DIR, "code_analysis.json"),
            "output_file": os.path.join(WORK_DIR, "analysis_report.md"),
            "analysis_metrics": [
                "complexity",
                "phi_resonance",
                "function_count",
                "import_count"
            ],
            "generate_visualization": True
        }
    }
    
    # Generate QR codes
    tasks = [task1, task2, task3, task4]
    
    for i, task in enumerate(tasks):
        print(f"Generating QR code {i+1}/{len(tasks)}: {task['task_type']}")
        
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
    
    analyzer = QRSimpleAnalyzer()
    worker = QRWorker(workspace_dir=WORK_DIR)
    
    # Analyze QR codes
    print("Analyzing QR sequence...")
    qr_data = analyzer.analyze_sequence(SEQUENCE_DIR)
    
    if not qr_data:
        print("❌ No QR codes found or decoded")
        return []
    
    print(f"✅ Decoded {len(qr_data)} QR codes")
    
    # Execute tasks in sequence
    results = []
    
    for i, data in enumerate(qr_data):
        print(f"\n📋 Executing Task {i+1}/{len(qr_data)}: {data.get('task_type', 'Unknown')}")
        
        # Execute task
        result = worker.execute_task(data)
        results.append(result)
        
        # Print result summary
        success = result.get("success", False)
        status_symbol = "✅" if success else "❌"
        print(f"{status_symbol} Task {i+1} completed with status: {result.get('status', 'Unknown')}")
        
        if "output" in result:
            print(f"Output: {result['output']}")
        
        # Add phi-harmonic delay between tasks
        if i < len(qr_data) - 1:
            delay = 1.0 / (PHI * (i + 1))
            print(f"Waiting {delay:.2f}s before next task (phi-harmonic delay)...")
            time.sleep(delay)
    
    print(f"\n✅ Executed {len(results)} tasks from QR sequence")
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
        
        # Create response data with phi-harmonic metadata
        response_data = {
            "response_id": str(uuid.uuid4()),
            "task_id": result.get("task_id", "unknown"),
            "success": result.get("success", False),
            "status": result.get("status", "unknown"),
            "timestamp": time.time(),
            "phi_time": time.time() * PHI % 1.0,
            "result_summary": result.get("output", "No output")
        }
        
        # Generate QR code
        qr_path = generator.generate_frame(
            payload=json.dumps(response_data),
            frame_number=i+1
        )
        
        response_paths.append(qr_path)
        print(f"  ✓ Generated: {os.path.basename(qr_path)}")
    
    print(f"\n✅ Created {len(response_paths)} response QR codes in {RESPONSE_DIR}")
    return response_paths

def main():
    """Main function to run the progressive QR test"""
    print("\n✨ QR Progressive Test")
    print("=" * 60)
    print("Testing QR codes that progressively build upon each other's work")
    print("Following phi-harmonic principles and recursive self-improvement")
    
    # Step 1: Create progressive QR sequence
    qr_paths = create_progressive_qr_sequence()
    
    # Step 2: Execute QR sequence
    results = execute_qr_sequence()
    
    # Step 3: Generate response QR codes
    response_paths = generate_response_qr_codes(results)
    
    # Print summary
    print("\n📊 Test Summary")
    print("=" * 60)
    print(f"QR Codes Generated: {len(qr_paths)}")
    print(f"Tasks Executed: {len(results)}")
    print(f"Successful Tasks: {sum(1 for r in results if r.get('success', False))}")
    print(f"Response QR Codes: {len(response_paths)}")
    
    # Check if workspace has expected files
    expected_files = [
        "hello_world.py",
        "code_analysis.json",
        "analysis_report.md"
    ]
    
    print("\n📂 Workspace Files")
    for file in expected_files:
        path = os.path.join(WORK_DIR, file)
        exists = os.path.exists(path)
        status = "✅ Created" if exists else "❌ Missing"
        print(f"{status}: {file}")
    
    print("\n✨ QR Progressive Test completed")

if __name__ == "__main__":
    main()
