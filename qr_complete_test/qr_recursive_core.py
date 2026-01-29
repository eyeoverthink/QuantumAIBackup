#!/usr/bin/env python3
"""
QR Recursive Core - Foundation for self-improving QR code system
Based on phi-harmonic principles and quantum resonance
"""

import os
import sys
import json
import time
import math
import uuid
import base64
import zlib
from typing import Dict, List, Any, Tuple, Optional
import qrcode
from PIL import Image, ImageDraw, ImageFont
from pyzbar.pyzbar import decode as pyzbar_decode

# Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio
VERSION_INFO = "1.0.0"
COMPRESSION_THRESHOLD = 500  # Characters

class QRRecursiveCore:
    """Core functionality for the recursive QR code system"""
    
    def __init__(self, config_path: Optional[str] = None):
        self.id = str(uuid.uuid4())
        self.creation_time = time.time()
        self.phi_time = self.creation_time * PHI % 1.0
        self.memory = {}
        self.history = []
        self.best_score = -float('inf')
        self.best_pattern = None
        
        # Load configuration if provided
        self.config = {
            "compression_threshold": COMPRESSION_THRESHOLD,
            "max_qr_version": 50,
            "error_correction": qrcode.constants.ERROR_CORRECT_H,
            "phi_resonance_enabled": True,
            "self_improvement_enabled": True
        }
        
        if config_path and os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    loaded_config = json.load(f)
                    self.config.update(loaded_config)
            except Exception as e:
                print(f"Error loading config: {e}")
    
    def generate_qr_code(self, data: Any, output_path: str, frame_id: Optional[int] = None) -> str:
        """Generate a QR code with the given data and save it to the specified path"""
        # Convert data to JSON if it's not already a string
        if not isinstance(data, str):
            try:
                payload = json.dumps(data)
            except Exception as e:
                print(f"Error converting data to JSON: {e}")
                payload = str(data)
        else:
            payload = data
        
        # Compress if payload is large
        is_compressed = False
        if len(payload) > self.config["compression_threshold"]:
            payload = base64.b64encode(zlib.compress(payload.encode('utf-8'))).decode('utf-8')
            is_compressed = True
        
        # Create metadata
        metadata = {
            "id": str(uuid.uuid4()),
            "timestamp": time.time(),
            "phi_time": time.time() * PHI % 1.0,
            "version": VERSION_INFO,
            "compressed": is_compressed,
            "frame_id": frame_id
        }
        
        # Create final payload with metadata
        final_payload = {
            "data": payload,
            "meta": metadata
        }
        
        # Generate QR code
        qr = qrcode.QRCode(
            version=None,
            error_correction=self.config["error_correction"],
            box_size=10,
            border=4,
        )
        qr.add_data(json.dumps(final_payload))
        qr.make(fit=True)
        
        # Create QR code image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Add visual indicators
        img = img.convert("RGB")
        draw = ImageDraw.Draw(img)
        
        # Add frame number if provided
        if frame_id is not None:
            draw.text((10, 10), f"#{frame_id}", fill="blue")
        
        # Add phi resonance indicator if enabled
        if self.config["phi_resonance_enabled"]:
            phi_time = metadata["phi_time"]
            resonance = 1.0 - abs(phi_time - 0.5) * 2.0  # 0.0 to 1.0
            
            # Draw resonance indicator
            color = self._get_resonance_color(resonance)
            size = img.size[0]
            indicator_size = int(size * 0.05)
            draw.rectangle(
                [(size - indicator_size - 10, 10), (size - 10, 10 + indicator_size)],
                fill=color
            )
        
        # Save the image
        img.save(output_path)
        return output_path
    
    def decode_qr_code(self, image_path: str) -> Dict[str, Any]:
        """Decode a QR code from the given image path"""
        try:
            # Load the image
            image = Image.open(image_path)
            
            # Decode QR code
            decoded_objects = pyzbar_decode(image)
            if not decoded_objects:
                raise ValueError(f"No QR code found in {image_path}")
            
            # Get the data from the first QR code
            qr_data = decoded_objects[0].data.decode('utf-8')
            
            # Parse JSON
            payload = json.loads(qr_data)
            
            # Extract metadata and data
            metadata = payload.get("meta", {})
            data = payload.get("data", "")
            
            # Decompress if necessary
            if metadata.get("compressed", False):
                try:
                    data = zlib.decompress(base64.b64decode(data)).decode('utf-8')
                except Exception as e:
                    print(f"Error decompressing data: {e}")
            
            # Try to parse data as JSON if possible
            try:
                parsed_data = json.loads(data)
                return {
                    "data": parsed_data,
                    "meta": metadata,
                    "raw": qr_data
                }
            except:
                # Return as string if not valid JSON
                return {
                    "data": data,
                    "meta": metadata,
                    "raw": qr_data
                }
                
        except Exception as e:
            print(f"Error decoding QR code: {e}")
            return {"error": str(e)}
    
    def _get_resonance_color(self, resonance: float) -> Tuple[int, int, int]:
        """Get color based on resonance value (0.0 to 1.0)"""
        if resonance > 0.8:
            return (0, 255, 0)  # Green for high resonance
        elif resonance > 0.5:
            return (0, 0, 255)  # Blue for medium resonance
        else:
            return (255, 0, 0)  # Red for low resonance
    
    def save_state(self, path: str) -> bool:
        """Save the current state to a file"""
        try:
            state = {
                "id": self.id,
                "creation_time": self.creation_time,
                "phi_time": self.phi_time,
                "memory": self.memory,
                "history": self.history,
                "best_score": self.best_score,
                "config": self.config,
                "version": VERSION_INFO
            }
            
            with open(path, 'w') as f:
                json.dump(state, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving state: {e}")
            return False
    
    def load_state(self, path: str) -> bool:
        """Load state from a file"""
        try:
            with open(path, 'r') as f:
                state = json.load(f)
            
            self.id = state.get("id", self.id)
            self.creation_time = state.get("creation_time", self.creation_time)
            self.phi_time = state.get("phi_time", self.phi_time)
            self.memory = state.get("memory", {})
            self.history = state.get("history", [])
            self.best_score = state.get("best_score", -float('inf'))
            
            # Update config but keep current values for missing keys
            loaded_config = state.get("config", {})
            self.config.update(loaded_config)
            
            return True
        except Exception as e:
            print(f"Error loading state: {e}")
            return False

# For testing
if __name__ == "__main__":
    core = QRRecursiveCore()
    test_data = {"message": "Hello Vaughn, its 12:46am June 27", "phi": PHI}
    output_path = "test_recursive_qr_1.png"
    
    # Generate and decode
    print(f"Generating QR code with test data...")
    core.generate_qr_code(test_data, output_path, frame_id=1)
    print(f"QR code saved to {output_path}")
    
    print(f"Decoding QR code...")
    result = core.decode_qr_code(output_path)
    print(f"Decoded data: {result['data']}")
    print(f"Metadata: {result['meta']}")
