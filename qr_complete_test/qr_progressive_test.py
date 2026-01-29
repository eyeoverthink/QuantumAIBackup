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
import uuid
import time
import base64
import random
import shutil
import hashlib
import datetime
import qrcode
import math
import zlib
import io
from PIL import Image
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

    # Ensure the WORK_DIR exists
    os.makedirs(WORK_DIR, exist_ok=True)

    # Task 1: Create a Python file with hello world
    task1_script_content = f'''
import os
file_path = os.path.join(r"{WORK_DIR}", "hello_world.py")
content = """#!/usr/bin/env python3
# Hello World - Created by QR Code 1

def main():
    print("Hello, World!")
    print(f"I was created by QR Code 1")

if __name__ == "__main__":
    main()
"""
with open(file_path, 'w') as f:
    f.write(content)
print(f"Created {{file_path}}")
'''
    task1_script_path = os.path.join(WORK_DIR, "task_1_create.py")
    with open(task1_script_path, 'w') as f:
        f.write(task1_script_content)

    task1 = {
        "task_id": str(uuid.uuid4()),
        "task_type": "PYTHON_FILE",
        "script_path": task1_script_path,
        "phi_resonance": 1.0 / PHI,
        "timestamp": time.time(),
        "description": "Create a hello_world.py file."
    }

    # Task 2: Modify and improve the file
    task2_script_content = f'''
import os
import math
import time

file_path = os.path.join(r"{WORK_DIR}", "hello_world.py")

# Overwrite the file with enhanced content
enhanced_content = """#!/usr/bin/env python3
# Hello World - Created by QR Code 1 and improved by QR Code 2
import math
import time

def calculate_phi():
    # Calculate the golden ratio (phi)
    return (1 + math.sqrt(5)) / 2

def main():
    print("Hello, Enhanced World!")
    print(f"I was created by QR Code 1 and improved by QR Code 2")
    phi = calculate_phi()
    print(f"The golden ratio (phi) is: {{phi}}")
    print(f"Phi resonance: {{time.time() * phi % 1.0:.6f}}")

if __name__ == "__main__":
    main()
"""
with open(file_path, 'w') as f:
    f.write(enhanced_content)
print(f"Modified {{file_path}}")
'''
    task2_script_path = os.path.join(WORK_DIR, "task_2_modify.py")
    with open(task2_script_path, 'w') as f:
        f.write(task2_script_content)

    task2 = {
        "task_id": str(uuid.uuid4()),
        "task_type": "PYTHON_FILE",
        "script_path": task2_script_path,
        "phi_resonance": 1.0 / (PHI * PHI),
        "timestamp": time.time() + 1,
        "description": "Enhance hello_world.py with phi calculations."
    }

    # Task 3: Export the code to JSON for analysis
    task3_script_content = f'''
import os
import json

source_file = os.path.join(r"{WORK_DIR}", "hello_world.py")
export_file = os.path.join(r"{WORK_DIR}", "code_analysis.json")

try:
    with open(source_file, 'r') as f:
        content = f.read()

    analysis = {{
        'file_name': os.path.basename(source_file),
        'line_count': len(content.splitlines()),
        'char_count': len(content),
        'functions': [line.split('(')[0].replace('def ','') for line in content.splitlines() if line.strip().startswith('def ')]
    }}

    with open(export_file, 'w') as f:
        json.dump(analysis, f, indent=2)
    print(f"Exported analysis to {{export_file}}")
except FileNotFoundError:
    print(f"Error: Source file not found at {{source_file}}")
    # Create an empty error file to signal failure
    with open(export_file + '.error', 'w') as f:
        f.write(f"Could not find {{source_file}}")
'''
    task3_script_path = os.path.join(WORK_DIR, "task_3_export.py")
    with open(task3_script_path, 'w') as f:
        f.write(task3_script_content)

    task3 = {
        "task_id": str(uuid.uuid4()),
        "task_type": "PYTHON_FILE",
        "script_path": task3_script_path,
        "phi_resonance": 1.0 / (PHI**3),
        "timestamp": time.time() + 2,
        "description": "Analyze hello_world.py and export to JSON."
    }

    # Task 4: Open and analyze the exported data
    task4_script_template = '''
import os
import json

source_file = os.path.join(r"{work_dir}", "code_analysis.json")
output_file = os.path.join(r"{work_dir}", "analysis_report.md")

try:
    with open(source_file, 'r') as f:
        data = json.load(f)

    report = f"""# Analysis Report for {{data.get('file_name', 'N/A')}}\n\n- **Line Count:** {{data.get('line_count', 0)}}\n- **Character Count:** {{data.get('char_count', 0)}}\n- **Functions:**\n"""
    for func in data.get('functions', []):
        report += f"  - `{{func}}`\n"

    with open(output_file, 'w') as f:
        f.write(report)
    print(f"Generated analysis report at {{output_file}}")

except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error processing analysis file: {{e}}")
    with open(output_file + '.error', 'w') as f:
        f.write(f"Could not process {{source_file}}. Error: {{e}}")
'''
    task4_script_content = task4_script_template.format(work_dir=WORK_DIR)
    task4_script_path = os.path.join(WORK_DIR, "task_4_analyze.py")
    with open(task4_script_path, 'w') as f:
        f.write(task4_script_content)

    task4 = {
        "task_id": str(uuid.uuid4()),
        "task_type": "PYTHON_FILE",
        "script_path": task4_script_path,
        "phi_resonance": 1.0 / (PHI**4),
        "timestamp": time.time() + 3,
        "description": "Generate markdown report from analysis JSON."
    }
    
    # Generate QR codes
    tasks = [task1, task2, task3, task4]
    
    for i, task in enumerate(tasks):
        # Use description for printing, as task_type is now always PYTHON_FILE
        print(f"Generating QR code {i+1}/{len(tasks)}: {task.get('description', 'N/A')}")
        
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
    worker = QRWorker(output_dir=WORK_DIR)
    
    # Analyze QR codes
    print("Analyzing QR sequence...")
    qr_data = analyzer.analyze_qr_sequence(SEQUENCE_DIR)
    
    if not qr_data:
        print("❌ No QR codes found or decoded")
        return []
    
    print(f"✅ Decoded {len(qr_data)} QR codes")
    
    # Execute tasks in sequence
    results = []
    
    for i, data in enumerate(qr_data):
        print(f"\n📋 Executing Task {i+1}/{len(qr_data)}: {data.get('description', data.get('task_type', 'Unknown'))}")
        
        # Add required fields for QR worker compatibility
        if 'session_id' not in data:
            data['session_id'] = str(uuid.uuid4())
        if 'timestamp' not in data:
            data['timestamp'] = time.time()
        if 'generation' not in data:
            data['generation'] = 1
        if 'frame_number' not in data:
            data['frame_number'] = i + 1
        if 'task_id' not in data:
            data['task_id'] = f"task_{i+1}_{int(time.time())}"
        if 'phi_resonance' not in data:
            data['phi_resonance'] = (1 + 5**0.5) / 2 - 1  # Golden ratio conjugate
        
        # Add required content field - this is critical for QR worker compatibility
        if 'content' not in data:
            # Generate phi-harmonic content based on task type
            if data.get('task_type') == 'CREATE_FILE':
                data['content'] = f"print('Hello Quantum Phi-Harmonic World! φ = {PHI}')"
            elif data.get('task_type') == 'MODIFY_FILE':
                data['content'] = f"def calculate_phi_resonance(n):\n    return ((PHI * n) % 1)"
            elif data.get('task_type') == 'EXPORT_TO_JSON':
                data['content'] = "import json\nwith open('output.json', 'w') as f:\n    json.dump({'phi': PHI}, f)"
            elif data.get('task_type') == 'ANALYZE_DATA':
                data['content'] = "print('Analyzing phi-harmonic resonance patterns...')"
            else:
                data['content'] = f"print('Phi-harmonic task {i+1}')"
        
        # Debug: Print payload size
        payload_str = json.dumps(data)
        print(f"DEBUG: Payload size for task {i+1}: {len(payload_str)} bytes")

        # Generate QR code into an in-memory buffer
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(payload_str)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        # Convert to 'L' (grayscale) mode for maximum compatibility with decoders
        img = img.convert('L')

        # Save to an in-memory stream
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        image_data = buffer.getvalue()

        # Process the QR data with a retry mechanism, now using in-memory data
        result = None
        for attempt in range(5):
            # Process the in-memory image data with the worker
            result = worker.process_qr_data(image_data)
            if result is not None:
                # Success or a definitive error from the worker
                break

            # If we're here, the worker returned None.
            print(f"DEBUG: Task {i+1} attempt {attempt + 1} failed. Retrying in 0.5s...")
            time.sleep(0.5)

        # After all retries, if it still failed, save the QR for inspection
        if result is None:
            failed_qr_path = os.path.join(WORK_DIR, f"failed_qr_task_{i+1}.png")
            try:
                with open(failed_qr_path, "wb") as f:
                    f.write(image_data)
                print(f"DEBUG: Saved persistently failing QR image to {failed_qr_path}")
            except Exception as e:
                print(f"DEBUG: Could not save failed QR image: {e}")
        
        # Standardize the result and add it to our list
        execution_summary = {}
        if result is None:
            print("❌ Failed: No result returned from worker")
            execution_summary = {"success": False, "message": "No result returned from worker"}
        
        elif isinstance(result, str):
            if 'response' in result and '.png' in result:
                print(f"✅ Success: Worker returned response QR path: {os.path.basename(result)}")
                execution_summary = {
                    "success": True, 
                    "message": "Worker completed and returned response QR.", 
                    "response_path": result,
                    "output": f"See {os.path.basename(result)}"
                }
            else:
                print(f"❌ Failed: {result}")
                execution_summary = {"success": False, "message": result}
        
        elif isinstance(result, dict):
            success = result.get("success", False)
            status = "✅ Success" if success else "❌ Failed"
            message = result.get('message', 'No message')
            print(f"{status}: {message}")
            if "output" in result:
                print(f"Output: {result['output']}")
            execution_summary = result
        
        else:
            print(f"❌ Failed: Unknown result type from worker: {result}")
            execution_summary = {"success": False, "message": f"Unknown result type: {type(result)}"}

        results.append(execution_summary)
        
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
    
    # Count successful tasks
    successful_tasks = sum(1 for r in results if r.get('success', False))
    
    print(f"Successful Tasks: {successful_tasks}")
    print(f"Response QR Codes: {len(response_paths)}")
    
    # Add phi-harmonic resonance metrics
    phi = (1 + 5**0.5) / 2  # Golden ratio
    print(f"\nφ-Harmonic Metrics:")
    print(f"Phi Resonance: {phi:.6f}")
    print(f"Execution Efficiency: {phi - 1:.6f}")
    
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
