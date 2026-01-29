#!/usr/bin/env python3
"""
Phi-Harmonic QR Message Generator
Creates a timestamp message file and encodes itself to QR
"""
import os
import time
import datetime
import qrcode
from math import sqrt

# Phi constant (Golden Ratio)
PHI = (1 + sqrt(5)) / 2  # ≈ 1.618034

def phi_resonance(value):
    """Calculate phi-harmonic resonance"""
    return (PHI * value) % 1

def create_timestamp_message():
    """Create a timestamp message with phi-resonance"""
    timestamp = time.time()
    phi_time = timestamp * PHI
    resonance = phi_resonance(timestamp)
    
    # Format the message with phi-harmonic values
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"""
    ====================================
    PHI-HARMONIC QUANTUM MESSAGE
    ====================================
    Timestamp: {current_time}
    Phi-Time: {phi_time}
    Phi-Resonance: {resonance:.6f}
    
    Knowledge isn't gained, it's discovered.
    Visual code is alive when aligned with phi.
    ====================================
    """
    
    # Write message to file
    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(output_dir, "phi_message.txt")
    
    with open(output_file, "w") as f:
        f.write(message)
    
    print(f"Message created: {output_file}")
    return output_file, message

def encode_self_to_qr():
    """Encode this script path to QR code"""
    # Get the absolute path of this script
    script_path = os.path.abspath(__file__)
    
    # Create a command that will run this script
    command = f"python {script_path}"
    
    # Create QR code with phi-harmonic metadata
    timestamp = time.time()
    phi_time = timestamp * PHI
    resonance = phi_resonance(timestamp)
    
    # Create payload with script reference and phi metadata
    payload = {
        "type": "phi_harmonic_script",
        "command": command,
        "path": script_path,
        "phi_time": phi_time,
        "phi_resonance": resonance,
        "timestamp": timestamp
    }
    
    import json
    qr_data = json.dumps(payload)
    
    # Create QR code
    qr = qrcode.QRCode(
        version=10,  # Fixed version for consistent size
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    # Create QR image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save QR code
    output_dir = os.path.dirname(os.path.abspath(__file__))
    qr_dir = os.path.join(output_dir, "phi_qr_codes")
    os.makedirs(qr_dir, exist_ok=True)
    
    timestamp_int = int(timestamp)
    qr_file = os.path.join(qr_dir, f"phi_message_qr_{timestamp_int}.png")
    img.save(qr_file)
    
    print(f"QR code created: {qr_file}")
    return qr_file, payload

if __name__ == "__main__":
    print("Phi-Harmonic QR Message Generator")
    print("="*33)
    
    # Create timestamp message
    message_file, message = create_timestamp_message()
    print(message)
    
    # Encode self to QR
    qr_file, payload = encode_self_to_qr()
    
    print(f"""
    Execution complete!
    
    Phi-Resonance: {payload['phi_resonance']:.6f}
    
    To run this script again:
    1. Scan the QR code at {qr_file}
    2. Execute the command: {payload['command']}
    
    Or simply run this file directly:
    python {os.path.basename(__file__)}
    """)
