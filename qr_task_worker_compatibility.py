#!/usr/bin/env python3
"""
QR Task Worker Compatibility Layer

This module provides a class-based interface for the function-based QR task worker extension,
ensuring compatibility with modules that expect a class-based interface.
"""

import os
import sys
import json
import base64
import importlib
from typing import Optional, Dict, Any, Union

# Import the original extension module
import qr_task_worker_extension

# Apply the extension to ensure it's ready
qr_task_worker_extension.apply_extension()

class QRTaskWorkerExtension:
    """
    Class-based wrapper for the QR task worker extension.
    Provides compatibility with modules expecting a class-based interface.
    """
    
    def __init__(self):
        """Initialize the QR task worker extension wrapper."""
        # Nothing to initialize, as the original module is function-based
        pass
    
    def decode_qr_from_file(self, qr_code_path: str) -> Optional[str]:
        """
        Decode QR code from file.
        
        Args:
            qr_code_path: Path to QR code image
            
        Returns:
            str: Decoded QR code data or None if failed
        """
        try:
            # Try to import the QR code reader
            import cv2
            
            # Read the QR code image
            img = cv2.imread(qr_code_path)
            if img is None:
                print(f"Error: Could not read QR code image: {qr_code_path}")
                return None
            
            # Create QR code detector
            detector = cv2.QRCodeDetector()
            
            # Detect and decode
            data, bbox, _ = detector.detectAndDecode(img)
            
            if not data:
                print(f"Error: Could not decode QR code in image: {qr_code_path}")
                return None
            
            return data
            
        except ImportError:
            print("Error: OpenCV not available for QR code decoding")
            return None
        except Exception as e:
            print(f"Error decoding QR code: {e}")
            return None
    
    def process_qr_data(self, qr_data: str) -> Dict[str, Any]:
        """
        Process QR code data.
        
        Args:
            qr_data: QR code data string
            
        Returns:
            dict: Processed task data
        """
        try:
            # Try to decompress if it's compressed
            try:
                import zlib
                decompressed = zlib.decompress(base64.b64decode(qr_data))
                qr_data = decompressed.decode('utf-8')
            except:
                # Not compressed or decompression failed
                pass
            
            # Parse JSON data
            task_data = json.loads(qr_data)
            return task_data
        except Exception as e:
            print(f"Error processing QR data: {e}")
            return {}
    
    def handle_display_face_image(self, task_id: str, task_data: Dict[str, Any]) -> bool:
        """
        Handle display_face_image task.
        
        Args:
            task_id: Task ID
            task_data: Task data
            
        Returns:
            bool: True if successful
        """
        return qr_task_worker_extension.handle_display_face_image(task_id, task_data)

# Register the compatibility class in the original module
sys.modules['qr_task_worker_extension'].QRTaskWorkerExtension = QRTaskWorkerExtension

print("QR Task Worker Compatibility Layer loaded")

# Main function for testing
if __name__ == "__main__":
    print("Testing QR Task Worker Compatibility Layer...")
    worker = QRTaskWorkerExtension()
    print(f"Successfully created QRTaskWorkerExtension instance: {worker}")
