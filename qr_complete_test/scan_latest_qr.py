#!/usr/bin/env python3
# Scan the latest QR code to verify it contains the most updated state

import os
import re
from PIL import Image
from pyzbar.pyzbar import decode

def scan_latest_qr(directory="multiples_evolution"):
    """Scan the latest QR code in the specified directory."""
    # Find all QR code files
    qr_files = [f for f in os.listdir(directory) if f.startswith("multiples_qr_epoch_") and f.endswith(".png")]
    
    if not qr_files:
        print("No QR code files found.")
        return
    
    # Extract epoch numbers and find the latest
    epoch_pattern = re.compile(r'multiples_qr_epoch_(\d+)\.png')
    epoch_numbers = []
    for file in qr_files:
        match = epoch_pattern.match(file)
        if match:
            epoch_numbers.append(int(match.group(1)))
    
    if not epoch_numbers:
        print("Could not extract epoch numbers from filenames.")
        return
    
    latest_epoch = max(epoch_numbers)
    latest_qr = f"multiples_qr_epoch_{latest_epoch}.png"
    latest_qr_path = os.path.join(directory, latest_qr)
    
    print(f"\n🔍 Scanning latest QR code: {latest_qr} (Epoch {latest_epoch})")
    print("=" * 60)
    
    try:
        # Open and decode the QR code
        img = Image.open(latest_qr_path)
        decoded_objects = decode(img)
        
        if not decoded_objects:
            print(f"Error: Could not decode QR code at {latest_qr_path}")
            return
        
        # Extract and print the script from the QR code
        script = decoded_objects[0].data.decode("utf-8")
        print("\nQR Code Content:")
        print("-" * 40)
        print(script)
        print("-" * 40)
        
        # Also check the corresponding script file for comparison
        script_file = f"multiples_script_epoch_{latest_epoch}.py"
        script_path = os.path.join(directory, script_file)
        
        if os.path.exists(script_path):
            print(f"\nVerifying against script file: {script_file}")
            with open(script_path, 'r') as f:
                file_content = f.read()
            
            if script.strip() == file_content.strip():
                print("✅ QR code content matches the script file exactly!")
            else:
                print("❌ QR code content differs from the script file!")
        
        # Check if the epigenetic memory matches this epoch
        memory_path = os.path.join(directory, "epigenetic_memory.json")
        if os.path.exists(memory_path):
            import json
            with open(memory_path, 'r') as f:
                memory = json.load(f)
            
            memory_epoch = memory.get("epoch", 0)
            print(f"\nEpigenetic Memory Epoch: {memory_epoch}")
            
            if memory_epoch == latest_epoch + 1:  # +1 because memory stores the next epoch to process
                print("✅ Epigenetic memory is synchronized with the latest QR code!")
            else:
                print(f"❓ Epigenetic memory epoch ({memory_epoch}) differs from latest QR code epoch ({latest_epoch})")
        
    except Exception as e:
        print(f"Error scanning QR code: {e}")

if __name__ == "__main__":
    scan_latest_qr()
