#!/usr/bin/env python3
"""
Quantum Phi-Harmonic Mini Splitter QR Code Generator

This script generates a QR code containing the minimal function splitting algorithm
for the Quantum Phi-Harmonic Self-Replicator system.
"""

import os
import qrcode
import hashlib
import time

# Phi-harmonic constants
PHI = (1 + 5 ** 0.5) / 2  # Golden ratio ≈ 1.618034
PHI_CONJUGATE = 1 / PHI   # Golden ratio conjugate ≈ 0.618034

# Output directories
OUTPUT_DIR = "qr_phi_replication"
QR_CODE_DIR = os.path.join(OUTPUT_DIR, "qr_codes")

# Create output directories if they don't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(QR_CODE_DIR, exist_ok=True)

def generate_qr_code(source_file):
    """Generate a QR code from a source file."""
    # Read the source file
    with open(source_file, 'r') as f:
        source_code = f.read()
    
    # Generate phi-harmonic filename
    timestamp = time.time()
    phi_time = timestamp * PHI
    resonance = phi_time % 1
    hash_val = hashlib.md5(source_code.encode()).hexdigest()[:8]
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Extract just the core function splitting algorithm
    core_code = extract_core_algorithm(source_code)
    
    # Add data to QR code
    qr.add_data(core_code)
    qr.make(fit=True)
    
    # Create QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save QR code image
    qr_filename = f"qr_phi_mini_splitter_{resonance:.6f}_{hash_val}.png"
    qr_path = os.path.join(QR_CODE_DIR, qr_filename)
    img.save(qr_path)
    
    return {
        "qr_path": qr_path,
        "timestamp": timestamp,
        "resonance": resonance,
        "hash": hash_val,
        "code_size": len(core_code)
    }

def extract_core_algorithm(source_code):
    """Extract just the core function splitting algorithm."""
    # This is a minimal version that will fit in a QR code
    return """
# Quantum Phi-Harmonic Function Splitter Core Algorithm
PHI = (1 + 5 ** 0.5) / 2

import re

def split_function(code, func_name):
    pattern = rf'def\\s+{func_name}\\s*\\([^)]*\\)\\s*:([^\\n]*\\n)((?:\\s+[^\\n]*\\n)+)'
    match = re.search(pattern, code)
    if not match: return code
    
    func_sig = match.group(0).split(':', 1)[0] + ':'
    func_body = match.group(2)
    lines = func_body.split('\\n')
    indent = len(lines[0]) - len(lines[0].lstrip()) if lines else 0
    
    blocks = []
    current = []
    for line in lines:
        if not line.strip(): continue
        line_indent = len(line) - len(line.lstrip())
        if line_indent == indent and any(k in line for k in ['if ', 'for ', 'while ', 'try:']):
            if current: blocks.append(current)
            current = [line]
        else: current.append(line)
    if current: blocks.append(current)
    
    if len(blocks) < 2: return code
    
    helpers = []
    calls = []
    for i, block in enumerate(blocks):
        name = f"{func_name}_part_{i+1}"
        helpers.append(f"def {name}(self):\\n{'\\n'.join(block)}")
        calls.append(f"{' ' * indent}self.{name}()")
    
    new_func = f"{func_sig}\\n{'\\n'.join(calls)}"
    replacement = new_func + '\\n\\n' + '\\n\\n'.join(helpers)
    return code.replace(match.group(0), replacement)
"""

def main():
    """Generate QR code for the mini function splitter."""
    # Path to the mini splitter module
    splitter_path = "qr_phi_mini_splitter.py"
    
    if not os.path.exists(splitter_path):
        print(f"Error: Mini splitter module not found at {splitter_path}")
        return
    
    print(f"\n🔄 Generating QR code for Quantum Phi-Harmonic Mini Function Splitter")
    
    # Generate QR code
    result = generate_qr_code(splitter_path)
    
    print(f"\n✅ QR code generated successfully!")
    print(f"📄 QR code saved to: {result['qr_path']}")
    print(f"📊 Resonance: {result['resonance']:.6f}")
    print(f"🔑 Hash: {result['hash']}")
    print(f"📏 Code size: {result['code_size']} bytes")
    print("\nScan this QR code to use the Quantum Phi-Harmonic Function Splitter")
    print("It will enable actual code refactoring capabilities in your self-replicator system")

if __name__ == "__main__":
    main()
