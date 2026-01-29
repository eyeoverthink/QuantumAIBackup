#!/usr/bin/env python3
"""
Simple QR Sequence Generator - Part of Animated QR Flipbook Execution System
By Vaughn Scott

Creates a sequence of QR codes with phi-harmonic evolution for visual communication.
Uses simpler QR generation for maximum compatibility with readers.
"""

import os
import uuid
import json
import time
import math
import base64
import hashlib
import qrcode
import datetime
from PIL import Image, ImageDraw, ImageFont
from cryptography.fernet import Fernet

# Phi (Golden Ratio) constant
PHI = (1 + math.sqrt(5)) / 2  # Approximately 1.618034

class SimpleQRSequence:
    """
    Generates a sequence of QR codes with phi-harmonic evolution.
    """
    
    def __init__(self, output_dir="qr_simple_sequence", encryption_key=None):
        """
        Initialize the Simple QR Sequence Generator.
        
        Args:
            output_dir: Directory to save generated QR code frames
            encryption_key: Optional Fernet encryption key for secure payloads
        """
        self.output_dir = output_dir
        self.session_id = str(uuid.uuid4())
        self.current_generation = 1
        self.frame_number = 1
        self.complexity = 0.1  # Starting complexity
        self.resonance = 1.0   # Starting resonance
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Initialize encryption if key provided
        self.encryption = None
        if encryption_key:
            self.encryption = Fernet(encryption_key)
        elif os.path.exists("qr_encryption.key"):
            with open("qr_encryption.key", "rb") as key_file:
                key = key_file.read()
                self.encryption = Fernet(key)
        else:
            # Generate new key
            key = Fernet.generate_key()
            with open("qr_encryption.key", "wb") as key_file:
                key_file.write(key)
            self.encryption = Fernet(key)
            print(f"New encryption key generated and saved to qr_encryption.key")
        
        # Previous frame hash for chain validation
        self.prev_frame_hash = None
    
    def calculate_phi_resonance(self, value):
        """Calculate phi-harmonic resonance of a value."""
        return 1.0 / (1.0 + abs((value * PHI) % 1.0 - 0.5))
    
    def evolve_metadata(self):
        """Evolve the phi-metadata based on golden ratio principles."""
        # Apply phi-harmonic oscillation to complexity
        phase = (self.current_generation * PHI) % (2 * math.pi)
        complexity_delta = 0.1 * math.sin(phase)
        self.complexity = max(0.1, min(1.0, self.complexity + complexity_delta))
        
        # Evolve resonance based on current values
        self.resonance = self.calculate_phi_resonance(self.current_generation)
    
    def generate_code_fragment(self, task_type="execute_python"):
        """
        Generate a code fragment based on current generation and complexity.
        
        Args:
            task_type: Type of task to generate (execute_python, execute_sh, etc.)
        
        Returns:
            A string containing the generated code fragment
        """
        # Simple code fragments that increase in complexity
        if task_type == "execute_python":
            if self.complexity < 0.3:
                return 'print("Hello Quantum World")'
            elif self.complexity < 0.6:
                return f'result = [i * {PHI * self.resonance} for i in range(10)]\nprint(result)'
            else:
                return 'import math\nimport time\nphi = (1 + math.sqrt(5)) / 2\nres = 1.0 / (1.0 + abs((time.time() * phi) % 1.0 - 0.5))\nprint("Current resonance: {:.6f}".format(res))'
        elif task_type == "execute_sh":
            if self.complexity < 0.5:
                return 'echo "Hello Quantum World"'
            else:
                return f'for i in $(seq 1 10); do echo "Phi-sequence $i: $(echo "scale=6; $i * {PHI * self.resonance}" | bc)"; done'
        else:
            return 'print("Hello Quantum World")'
    
    def create_qr_payload(self, content, task_type="execute_python", frame_total=10):
        """
        Create a complete QR payload with code content and phi-metadata.
        
        Args:
            content: The code content to include
            task_type: Type of task (execute_python, execute_sh, multi, continue_sequence)
            frame_total: Total number of frames in the sequence
            
        Returns:
            JSON string containing the complete payload
        """
        # Create payload with all necessary information
        valid_until = (datetime.datetime.now() + 
                      datetime.timedelta(minutes=5)).isoformat()
        
        payload = {
            "session_id": self.session_id,
            "frame_number": self.frame_number,
            "frame_total": frame_total,
            "task_type": task_type,
            "content": content,
            "phi_metadata": {
                "generation": self.current_generation,
                "complexity": self.complexity,
                "resonance": self.resonance
            },
            "prev_frame_hash": self.prev_frame_hash,
            "valid_until": valid_until
        }
        
        # Convert to JSON
        json_payload = json.dumps(payload)
        
        # Calculate hash for this frame (for next frame's prev_frame_hash)
        self.prev_frame_hash = hashlib.sha256(json_payload.encode()).hexdigest()
        
        # Encrypt if encryption is enabled
        if self.encryption:
            encrypted_payload = self.encryption.encrypt(json_payload.encode())
            return "ENCRYPTED:" + base64.b64encode(encrypted_payload).decode()
        
        return json_payload
    
    def generate_qr_frame(self, payload, frame_number):
        """
        Generate a QR code image for the given payload.
        
        Args:
            payload: String payload to encode in QR
            frame_number: Frame number for filename
            
        Returns:
            Path to the generated QR image
        """
        # Create QR code with maximum error correction
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(payload)
        qr.make(fit=True)
        
        # Create image
        qr_img = qr.make_image(fill_color="black", back_color="white")
        
        # Save image
        filename = os.path.join(self.output_dir, f"frame_{frame_number:03d}.png")
        qr_img.save(filename)
        
        # Now add visual indicators as a separate step
        img = Image.open(filename)
        draw = ImageDraw.Draw(img)
        
        # Add frame number - use string for color to fix PIL error
        draw.text((10, 10), f"F{frame_number:03d}", fill="red")
        
        # Add phi resonance indicator (colored corner based on resonance)
        # Convert to string color format for PIL
        r = int(255 * self.resonance)
        g = int(128 * (1 - self.resonance))
        b = int(255 * self.complexity)
        resonance_color = f"rgb({r},{g},{b})"
        
        img_width, img_height = img.size
        corner_size = int(img_width * 0.05)
        draw.rectangle(
            [(0, 0), (corner_size, corner_size)],
            fill=resonance_color
        )
        
        # Save modified image
        img.save(filename)
        return filename
    
    def generate_sequence(self, num_frames=10, task_types=None):
        """
        Generate a sequence of evolving QR codes.
        
        Args:
            num_frames: Number of frames to generate
            task_types: List of task types to use (if None, defaults to execute_python)
            
        Returns:
            List of paths to generated QR images
        """
        if task_types is None:
            task_types = ["execute_python"] * num_frames
        
        # Ensure we have enough task types
        if len(task_types) < num_frames:
            task_types = task_types * (num_frames // len(task_types) + 1)
        
        frame_paths = []
        
        for i in range(num_frames):
            # Evolve metadata for this frame
            self.evolve_metadata()
            
            # Generate code content
            content = self.generate_code_fragment(task_types[i])
            
            # Create payload
            payload = self.create_qr_payload(content, task_types[i], num_frames)
            
            # Generate QR frame
            frame_path = self.generate_qr_frame(payload, self.frame_number)
            frame_paths.append(frame_path)
            
            print(f"Generated frame {self.frame_number}/{num_frames}: {os.path.basename(frame_path)}")
            
            # Update counters
            self.frame_number += 1
            if self.frame_number % int(PHI * 5) == 0:  # ~8 frames per generation
                self.current_generation += 1
        
        return frame_paths

def main():
    """Main function to run the Simple QR Sequence Generator."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Simple QR Sequence Generator")
    parser.add_argument("--frames", type=int, default=10, help="Number of frames to generate")
    parser.add_argument("--output", default="qr_simple_sequence", help="Output directory")
    parser.add_argument("--key", help="Path to encryption key file")
    
    args = parser.parse_args()
    
    # Get encryption key if provided
    encryption_key = None
    if args.key and os.path.exists(args.key):
        with open(args.key, "rb") as key_file:
            encryption_key = key_file.read()
    
    # Create sequence generator
    generator = SimpleQRSequence(output_dir=args.output, encryption_key=encryption_key)
    
    # Define a sequence of task types
    sequence = [
        "execute_python",  # Setup
        "execute_python",  # Learn
        "execute_python",  # Test
        "execute_sh",      # Process
        "execute_python",  # Evaluate
        "execute_python",  # Respond
    ]
    
    # Generate sequence
    frame_paths = generator.generate_sequence(
        num_frames=args.frames, 
        task_types=sequence * (args.frames // len(sequence) + 1)
    )
    
    print(f"\nGenerated {len(frame_paths)} QR frames in {generator.output_dir}/")
    print(f"Session ID: {generator.session_id}")
    print(f"Final phi-resonance: {generator.resonance:.6f}")
    print(f"Final complexity: {generator.complexity:.6f}")

if __name__ == "__main__":
    print("Simple QR Sequence Generator - By Vaughn Scott")
    main()
