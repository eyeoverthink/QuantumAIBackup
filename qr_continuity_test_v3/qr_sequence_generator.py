#!/usr/bin/env python3
"""
QR Sequence Generator - Part of Animated QR Flipbook Execution System
By Vaughn Scott

Generates evolutionary sequences of QR codes based on phi-harmonic principles.
Each QR code contains a fragment of code or command, context information,
and phi-evolution metadata.
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
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from cryptography.fernet import Fernet

# Import QR Sequence Chunker
from qr_sequence_chunker import QRSequenceChunker

# Phi (Golden Ratio) constant
PHI = (1 + math.sqrt(5)) / 2  # Approximately 1.618034

class QRSequenceGenerator:
    """
    Generates sequences of QR codes that evolve based on phi-harmonic principles.
    """
    
    def __init__(self, output_dir="qr_simple_sequence", encryption_key=None):
        """
        Initialize the QR Sequence Generator.
        
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
        
        # Initialize chunker for large payloads
        self.chunker = QRSequenceChunker(max_chunk_size=1000)
        
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
        
        # Mutation vectors - these guide how code evolves
        self.mutation_vectors = {
            "complexity": [0.382, 0.618, 1.0],  # Phi-based scaling factors
            "structure": [0.5, PHI - 1, 1/PHI], # Different aspects of phi
            "resonance": [1/PHI, 1.0, PHI]      # Resonance scaling
        }
        
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
        
        # Update mutation vectors based on resonance
        for key in self.mutation_vectors:
            # Rotate the vector elements based on phi
            self.mutation_vectors[key] = [
                v * (1 + (0.1 * math.sin(self.current_generation * PHI))) 
                for v in self.mutation_vectors[key]
            ]
    
    def generate_code_fragment(self, task_type="execute_python"):
        """
        Generate a code fragment based on current generation and complexity.
        
        Args:
            task_type: Type of task to generate (execute_python, execute_sh, etc.)
        
        Returns:
            A string containing the generated code fragment
        """
        # Basic templates that increase in complexity with generation
        python_templates = [
            'print("Hello Quantum World, From Vaughn")',
            'result = [i * {} for i in range(10)]\nprint(result)',
            'phi = (1 + math.sqrt(5)) / 2\nres_val = 1.0 / (1.0 + abs((time.time() * phi) % 1.0 - 0.5))\nprint("Current resonance: {:.6f}".format(res_val))',
            'import numpy as np\ndata = np.random.random(10)\nprocessed = np.sin(data * {} * np.pi)\nprint("Phi-processed data: {}".format(processed.tolist()))',
        ]
        
        shell_templates = [
            'echo "Hello Quantum World, From Vaughn Scott"',
            'for i in $(seq 1 10); do echo "Phi-sequence $i: $(echo "scale=6; $i * {}" | bc)"; done',
            'timestamp=$(date +%s)\nremainder=$(($timestamp % 1618))\necho "Current phi-time resonance: $remainder"',
        ]
        
        # Select template based on complexity and task type
        if task_type == "execute_python":
            templates = python_templates
        elif task_type == "execute_sh":
            templates = shell_templates
        else:
            templates = python_templates  # Default to Python
            
        # Select template complexity based on current complexity
        template_idx = min(int(self.complexity * len(templates)), len(templates) - 1)
        template = templates[template_idx]
        
        # Fill in template with phi-based values
        phi_value = PHI * self.resonance
        
        # Handle templates with different numbers of format placeholders
        if template_idx == 0:  # No placeholders
            return template
        elif '{' not in template:  # No placeholders
            return template
        elif template.count('{}') == 1:  # One placeholder
            return template.format(phi_value)
        else:  # Multiple placeholders
            return template.format(phi_value, phi_value)  # Pass the same value for all placeholders
    
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
                "resonance": self.resonance,
                "mutation_vector": [
                    self.mutation_vectors["complexity"][0],
                    self.mutation_vectors["structure"][1],
                    self.mutation_vectors["resonance"][2]
                ]
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
    
    def _generate_qr_image(self, qr, frame_suffix):
        """
        Helper method to generate a QR code image from a QRCode object.
        
        Args:
            qr: QRCode object with data already added
            frame_suffix: Suffix for the frame filename
            
        Returns:
            Path to the generated QR image
        """
        # Create image
        qr_img = qr.make_image(fill_color="black", back_color="white")
        
        # Add visual indicators for evolution stage
        img = qr_img.convert('RGBA')
        draw = ImageDraw.Draw(img)
        
        # Add frame number
        draw.text((10, 10), f"F{frame_suffix}", fill=(255, 0, 0, 128))
        
        # Add phi resonance indicator (colored corner based on resonance)
        resonance_color = (
            int(255 * self.resonance),
            int(128 * (1 - self.resonance)),
            int(255 * self.complexity),
            128
        )
        img_width, img_height = img.size
        corner_size = int(img_width * 0.1)
        draw.rectangle(
            [(img_width - corner_size, 0), (img_width, corner_size)],
            fill=resonance_color
        )
        
        # Save image
        filename = os.path.join(self.output_dir, f"qr_frame_{frame_suffix}.png")
        img.save(filename)
        return filename
    
    def generate_qr_frame(self, payload, frame_number):
        """
        Generate a QR code image for the given payload.
        
        Args:
            payload: String payload to encode in QR
            frame_number: Frame number for filename
            
        Returns:
            Path to the generated QR image or list of paths for chunked QR codes
        """
        # Check if payload needs to be chunked (try to encode and see if it fits)
        try:
            # Try creating a QR code with the full payload
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(payload)
            qr.make(fit=True)
            
            # If we get here, the payload fits in a single QR code
            is_chunked = False
        except ValueError:
            # Payload is too large, needs chunking
            is_chunked = True
        
        if is_chunked:
            # Use chunker to split payload into manageable pieces
            chunks = self.chunker.chunk_payload(payload)
            paths = []
            
            # Generate QR code for each chunk
            for i, chunk in enumerate(chunks):
                # Add chunk metadata
                chunk_data = json.dumps(chunk)
                
                # Create QR code for this chunk
                qr = qrcode.QRCode(
                    version=None,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=10,
                    border=4,
                )
                qr.add_data(chunk_data)
                qr.make(fit=True)
                
                # Generate image for this chunk
                chunk_path = self._generate_qr_image(qr, f"{frame_number:03d}_{i+1:02d}")
                paths.append(chunk_path)
                
            return paths
        else:
            # Generate image for the single QR code
            return self._generate_qr_image(qr, f"{frame_number:03d}")
    
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
            
            # Update counters
            self.frame_number += 1
            if self.frame_number % PHI_FRAME_CYCLE == 0:
                self.current_generation += 1
            
            # Simulate phi-harmonic timing between frames
            time.sleep(0.1)  # Small delay for demonstration
        
        return frame_paths

# Phi-based frame cycle (when to increment generation)
PHI_FRAME_CYCLE = int(PHI * 10)  # ~16 frames per generation

if __name__ == "__main__":
    print("QR Sequence Generator - By Vaughn Scott")
    print("Generating phi-evolving QR code sequence...")
    
    # Create generator
    generator = QRSequenceGenerator(output_dir="qr_simple_sequence")
    
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
    frame_paths = generator.generate_sequence(num_frames=24, task_types=sequence * 4)
    
    print(f"Generated {len(frame_paths)} QR frames in {generator.output_dir}/")
    print(f"Session ID: {generator.session_id}")
    print(f"Final phi-resonance: {generator.resonance:.6f}")
    print(f"Final complexity: {generator.complexity:.6f}")
    print("Run the QR Display Engine to animate this sequence.")
