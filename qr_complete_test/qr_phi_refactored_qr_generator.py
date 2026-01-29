#!/usr/bin/env python3
"""
Quantum Phi-Harmonic Refactored Script QR Generator

This script generates a QR code for the refactored version of the
Quantum Phi-Harmonic Self-Replicator, completing the integration
with the existing self-replication system.
"""

import os
import qrcode
import hashlib
import time
from typing import Dict, Any

# Phi-harmonic constants
PHI = (1 + 5 ** 0.5) / 2  # Golden ratio ≈ 1.618034
PHI_CONJUGATE = 1 / PHI   # Golden ratio conjugate ≈ 0.618034

# Output directories
OUTPUT_DIR = "qr_phi_replication"
QR_CODE_DIR = os.path.join(OUTPUT_DIR, "qr_codes")

# Create output directories if they don't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(QR_CODE_DIR, exist_ok=True)

def generate_qr_code(source_file: str, output_dir: str = QR_CODE_DIR) -> Dict[str, Any]:
    """Generate a QR code from a source file.
    
    Args:
        source_file: Path to the source file
        output_dir: Directory to save the QR code
        
    Returns:
        Dictionary with QR code information
    """
    # Read the source file
    with open(source_file, 'r') as f:
        source_code = f.read()
    
    # Generate phi-harmonic filename
    timestamp = time.time()
    phi_time = timestamp * PHI
    resonance = phi_time % 1
    hash_val = hashlib.md5(source_code.encode()).hexdigest()[:8]
    
    # Extract generation number from filename
    gen_num = "4"
    if "gen" in source_file:
        try:
            gen_part = source_file.split("gen")[1].split("_")[0]
            if gen_part.isdigit():
                gen_num = gen_part
        except:
            pass
    
    # Create QR code
    qr = qrcode.QRCode(
        version=None,  # Auto-determine version
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    # Check if the source code is too large for a single QR code
    if len(source_code.encode('utf-8')) > 2000:
        print(f"Source code is too large ({len(source_code.encode('utf-8'))} bytes) for a single QR code")
        print("Creating simplified loader QR code...")
        
        # Create a simplified script that loads the full script
        simplified_script = f"""#!/usr/bin/env python3
# Quantum Phi-Harmonic Self-Replicator (Refactored Loader)
# Generation: {gen_num}
# Timestamp: {timestamp}
# Resonance: {resonance:.6f}

import os
import sys

# Define the path to the full refactored script
SCRIPT_PATH = "{source_file}"

# Check if the script exists
if not os.path.exists(SCRIPT_PATH):
    print(f"Error: Script not found at {{SCRIPT_PATH}}")
    sys.exit(1)

print(f"\n🔄 Loading refactored Quantum Phi-Harmonic Self-Replicator")
print(f"📄 Script path: {{SCRIPT_PATH}}")

# Execute the script
with open(SCRIPT_PATH, 'r') as f:
    exec(f.read())
"""
        
        # Use the simplified script for the QR code
        qr.add_data(simplified_script)
    else:
        # Use the full source code
        qr.add_data(source_code)
    
    qr.make(fit=True)
    
    # Create QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save QR code image
    qr_filename = f"qr_phi_replicator_refactored_gen{gen_num}_{resonance:.6f}.png"
    qr_path = os.path.join(output_dir, qr_filename)
    img.save(qr_path)
    
    return {
        "qr_path": qr_path,
        "generation": gen_num,
        "timestamp": timestamp,
        "resonance": resonance,
        "hash": hash_val
    }

def main():
    """Generate QR code for the refactored script."""
    # Path to the refactored script
    refactored_script = None
    
    # Look for the refactored script
    for file in os.listdir(OUTPUT_DIR):
        if file.startswith("qr_phi_replicator_gen") and "refactored" in file and file.endswith(".py"):
            refactored_script = os.path.join(OUTPUT_DIR, file)
            break
    
    if not refactored_script:
        print("Error: Could not find refactored script")
        return
    
    print(f"\n🔄 Generating QR code for refactored Quantum Phi-Harmonic Self-Replicator")
    print(f"📄 Refactored script: {refactored_script}")
    
    # Generate QR code
    result = generate_qr_code(refactored_script)
    
    print(f"\n✅ QR code generated successfully!")
    print(f"📄 QR code saved to: {result['qr_path']}")
    print(f"📊 Generation: {result['generation']}")
    print(f"📊 Resonance: {result['resonance']:.6f}")
    print(f"🔑 Hash: {result['hash']}")
    print("\nScan this QR code to execute the refactored Quantum Phi-Harmonic Self-Replicator")
    print("This completes the integration of actual code refactoring into your self-replication system")

if __name__ == "__main__":
    main()
