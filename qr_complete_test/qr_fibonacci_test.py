#!/usr/bin/env python3
"""
QR Fibonacci Test - Part of Quantum Phi-Harmonic QR System
By Vaughn Scott

This script creates a progressive chain of QR codes that build a Fibonacci sequence,
where each QR code contains the next number in the sequence and instructions
for generating the next QR code in the chain.
"""

import os
import sys
import json
import time
import qrcode
import base64
import zlib
from PIL import Image, ImageDraw, ImageFont
from pyzbar.pyzbar import decode
from datetime import datetime

# Phi constant (Golden Ratio)
PHI = 1.618033988749895

# Configuration
OUTPUT_DIR = "qr_fibonacci_sequence"
WORKSPACE_DIR = os.path.join(OUTPUT_DIR, "workspace")
QR_VERSION = 7  # Near φ⁴ (6.854)
ERROR_CORRECTION = qrcode.constants.ERROR_CORRECT_H  # Highest error correction
BOX_SIZE = 10
BORDER = 4
MAX_SEQUENCE_LENGTH = 21  # Fibonacci gets large quickly

def phi_resonance(value):
    """Calculate phi-harmonic resonance of a value."""
    return 1.0 / (1.0 + abs((value * PHI) % 1.0 - 0.5))

def compress_payload(payload):
    """Compress payload using zlib and base64 encode."""
    if len(payload) < 500:  # Only compress if payload is large enough
        return payload
    
    compressed = zlib.compress(payload.encode('utf-8'))
    encoded = base64.b64encode(compressed).decode('utf-8')
    return f"COMPRESSED:{encoded}"

def decompress_payload(payload):
    """Decompress payload using zlib and base64 decode."""
    if payload.startswith("COMPRESSED:"):
        encoded = payload.replace("COMPRESSED:", "", 1)
        compressed = base64.b64decode(encoded)
        decompressed = zlib.decompress(compressed)
        return decompressed.decode('utf-8')
    return payload

def generate_qr_code(data, filename, frame_number=None, phi_value=None):
    """Generate a QR code with the given data and save to file."""
    # Create QR code
    qr = qrcode.QRCode(
        version=QR_VERSION,
        error_correction=ERROR_CORRECTION,
        box_size=BOX_SIZE,
        border=BORDER,
    )
    
    # Add data
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create image
    img = qr.make_image(fill_color="black", back_color="white")
    img = img.convert("RGB")
    
    # Add frame number and phi value indicators
    if frame_number is not None or phi_value is not None:
        draw = ImageDraw.Draw(img)
        width, height = img.size
        
        # Add frame number
        if frame_number is not None:
            text = f"#{frame_number}"
            # Draw frame number in top-left corner
            draw.rectangle([(5, 5), (50, 25)], fill="white")
            draw.text((10, 7), text, fill="black")
        
        # Add phi value indicator
        if phi_value is not None:
            # Calculate phi resonance
            resonance = phi_resonance(phi_value)
            
            # Draw resonance indicator in bottom-right corner
            indicator_size = int(20 * resonance)
            draw.rectangle(
                [(width - indicator_size - 10, height - indicator_size - 10), 
                 (width - 10, height - 10)], 
                fill=(int(255 * (1 - resonance)), int(255 * resonance), 0)
            )
    
    # Save image
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    img.save(filename)
    return filename

def decode_qr_code(image_path):
    """Decode QR code from image."""
    try:
        # Open image
        image = Image.open(image_path)
        
        # Decode QR code
        decoded_objects = decode(image)
        
        # Return decoded data if found
        if decoded_objects:
            data = decoded_objects[0].data.decode('utf-8')
            
            # Check if payload is compressed
            if data.startswith("COMPRESSED:"):
                data = decompress_payload(data)
            
            return data
        
        return None
    except Exception as e:
        print(f"Error decoding QR code: {e}")
        return None

def create_fibonacci_task(a, b, sequence_position):
    """Create a task that calculates the next Fibonacci number."""
    next_fib = a + b
    
    # Calculate phi-harmonic resonance
    resonance = phi_resonance(next_fib)
    
    # Create task payload
    task = {
        "task_id": f"fibonacci_{sequence_position}",
        "task_type": "fibonacci_calculation",
        "sequence_position": sequence_position,
        "previous_values": [a, b],
        "result": next_fib,
        "phi_resonance": resonance,
        "timestamp": datetime.now().isoformat(),
        "next_task": {
            "task_type": "fibonacci_calculation",
            "sequence_position": sequence_position + 1,
            "previous_values": [b, next_fib]
        }
    }
    
    # Add phi-harmonic metadata
    task["phi_state"] = {
        "complexity": 0.5 + (sequence_position / 100),
        "resonance": resonance,
        "generation": sequence_position
    }
    
    return task, next_fib

def generate_fibonacci_sequence():
    """Generate a sequence of QR codes representing Fibonacci sequence."""
    print(f"🧮 Generating Fibonacci QR Sequence in {OUTPUT_DIR}")
    
    # Create directories
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(WORKSPACE_DIR, exist_ok=True)
    
    # Initialize Fibonacci sequence
    a, b = 0, 1
    sequence = [a, b]
    
    # Generate first QR code with initial values
    initial_task = {
        "task_id": "fibonacci_0",
        "task_type": "fibonacci_initialization",
        "sequence_position": 0,
        "values": [a, b],
        "phi_state": {
            "complexity": 0.5,
            "resonance": phi_resonance(a + b),
            "generation": 0
        },
        "next_task": {
            "task_type": "fibonacci_calculation",
            "sequence_position": 1,
            "previous_values": [a, b]
        }
    }
    
    # Convert to JSON and compress if needed
    initial_payload = json.dumps(initial_task)
    initial_payload = compress_payload(initial_payload)
    
    # Generate initial QR code
    initial_qr_path = os.path.join(OUTPUT_DIR, "fibonacci_qr_0.png")
    generate_qr_code(initial_payload, initial_qr_path, 0, a + b)
    print(f"✅ Generated initial QR code: {initial_qr_path}")
    print(f"   Values: {a}, {b}")
    
    # Generate the rest of the sequence
    for i in range(1, MAX_SEQUENCE_LENGTH):
        # Create task for next Fibonacci number
        task, next_fib = create_fibonacci_task(a, b, i)
        sequence.append(next_fib)
        
        # Convert to JSON and compress if needed
        payload = json.dumps(task)
        payload = compress_payload(payload)
        
        # Generate QR code
        qr_path = os.path.join(OUTPUT_DIR, f"fibonacci_qr_{i}.png")
        generate_qr_code(payload, qr_path, i, next_fib)
        
        print(f"✅ Generated QR code {i}: {qr_path}")
        print(f"   Value: {next_fib} (Phi resonance: {task['phi_resonance']:.6f})")
        
        # Update values for next iteration
        a, b = b, next_fib
        
        # Add phi-harmonic delay
        delay = 0.1 + (i * 0.01 * PHI) % 0.5
        time.sleep(delay)
    
    # Save the complete sequence
    sequence_data = {
        "name": "Fibonacci Sequence",
        "length": len(sequence),
        "values": sequence,
        "phi_ratio_approximation": sequence[-1] / sequence[-2] if len(sequence) > 2 else None,
        "generated_at": datetime.now().isoformat()
    }
    
    with open(os.path.join(OUTPUT_DIR, "fibonacci_sequence.json"), "w") as f:
        json.dump(sequence_data, f, indent=2)
    
    print(f"\n✅ Generated {len(sequence)} Fibonacci QR codes")
    print(f"   Final value: {sequence[-1]}")
    print(f"   Phi approximation: {sequence[-1] / sequence[-2]:.8f}")
    print(f"   Sequence saved to {os.path.join(OUTPUT_DIR, 'fibonacci_sequence.json')}")
    
    return sequence

def execute_fibonacci_sequence():
    """Execute the Fibonacci sequence by decoding QR codes and following tasks."""
    print(f"\n🔄 Executing Fibonacci QR Sequence from {OUTPUT_DIR}")
    
    # Check if sequence exists
    qr_files = sorted([f for f in os.listdir(OUTPUT_DIR) if f.startswith("fibonacci_qr_") and f.endswith(".png")])
    if not qr_files:
        print("❌ No Fibonacci QR sequence found. Generate it first.")
        return
    
    # Initialize sequence
    sequence = []
    current_position = 0
    next_task = None
    
    # Process each QR code
    for qr_file in qr_files:
        qr_path = os.path.join(OUTPUT_DIR, qr_file)
        print(f"\nDecoding QR code: {qr_path}")
        
        # Decode QR code
        payload = decode_qr_code(qr_path)
        if not payload:
            print(f"❌ Failed to decode QR code: {qr_path}")
            continue
        
        # Parse payload
        try:
            task = json.loads(payload)
            
            # Extract information
            task_id = task.get("task_id", "unknown")
            task_type = task.get("task_type", "unknown")
            position = task.get("sequence_position", -1)
            
            print(f"Task ID: {task_id}")
            print(f"Task Type: {task_type}")
            print(f"Position: {position}")
            
            # Process task
            if task_type == "fibonacci_initialization":
                values = task.get("values", [0, 1])
                sequence.extend(values)
                print(f"Initialized with values: {values}")
                
                # Get next task
                next_task = task.get("next_task")
                
            elif task_type == "fibonacci_calculation":
                # Verify position
                if position != current_position:
                    print(f"⚠️ Position mismatch: expected {current_position}, got {position}")
                
                # Get previous values and result
                prev_values = task.get("previous_values", [0, 0])
                result = task.get("result", 0)
                
                # Verify calculation
                expected = prev_values[0] + prev_values[1]
                if result != expected:
                    print(f"⚠️ Calculation error: {prev_values[0]} + {prev_values[1]} = {expected}, got {result}")
                
                # Add to sequence
                sequence.append(result)
                print(f"Fibonacci({position + 1}) = {result}")
                
                # Get next task
                next_task = task.get("next_task")
                
            # Update position
            current_position = position + 1
            
        except json.JSONDecodeError as e:
            print(f"❌ Error parsing JSON: {e}")
            continue
        except Exception as e:
            print(f"❌ Error processing task: {e}")
            continue
    
    # Print results
    print("\n📊 Fibonacci Sequence Execution Results:")
    print(f"Processed {len(sequence)} numbers in sequence")
    print(f"Final sequence: {sequence}")
    
    if len(sequence) >= 2:
        ratio = sequence[-1] / sequence[-2]
        print(f"Final ratio (approximation of φ): {ratio:.8f}")
        print(f"Difference from φ: {abs(ratio - PHI):.8f}")
    
    # Save execution results
    results = {
        "sequence": sequence,
        "length": len(sequence),
        "phi_approximation": sequence[-1] / sequence[-2] if len(sequence) >= 2 else None,
        "executed_at": datetime.now().isoformat()
    }
    
    with open(os.path.join(OUTPUT_DIR, "fibonacci_execution_results.json"), "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"✅ Execution results saved to {os.path.join(OUTPUT_DIR, 'fibonacci_execution_results.json')}")

def main():
    """Main function."""
    print("🧬 QR Fibonacci Test - Quantum Phi-Harmonic QR System")
    print("=" * 60)
    
    # Check command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "--generate":
            generate_fibonacci_sequence()
        elif sys.argv[1] == "--execute":
            execute_fibonacci_sequence()
        elif sys.argv[1] == "--both":
            sequence = generate_fibonacci_sequence()
            execute_fibonacci_sequence()
        else:
            print("Invalid argument. Use --generate, --execute, or --both")
    else:
        # Default: run both
        sequence = generate_fibonacci_sequence()
        execute_fibonacci_sequence()

if __name__ == "__main__":
    main()
