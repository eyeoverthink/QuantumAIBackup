#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Phi QR Scanner
=============

This module implements QR code scanning functionality for the
consciousness physics digital computer system, enabling persistent
memory through QR code state storage and retrieval.

This builds on existing QR and digital logic systems as a "lego block" approach.
"""

import os
import json
import numpy as np
from PIL import Image
import cv2
from pyzbar.pyzbar import decode
from typing import Dict, Any, Optional, Union, List, Tuple

# Constants
PHI = (1 + 5 ** 0.5) / 2  # Golden ratio (φ ≈ 1.618034)
PHI_INVERSE = 1 / PHI  # Inverse golden ratio (φ⁻¹ ≈ 0.618034)

class PhiQRScanner:
    """
    QR code scanner for consciousness physics digital computer.
    
    This class enables scanning QR codes that contain consciousness
    state information, allowing for persistent memory across sessions.
    """
    
    def __init__(self):
        """Initialize QR scanner."""
        self.last_decoded_data = None
        self.phi_resonance = PHI_INVERSE
    
    def scan_qr_from_file(self, image_path: str) -> Optional[Dict[str, Any]]:
        """
        Scan QR code from image file.
        
        Args:
            image_path: Path to image file containing QR code
            
        Returns:
            Decoded data as dictionary, or None if scanning failed
        """
        try:
            # Load image
            image = cv2.imread(image_path)
            if image is None:
                print(f"Error: Could not load image from {image_path}")
                return None
            
            # Convert to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Decode QR code
            decoded_objects = decode(gray)
            
            if not decoded_objects:
                print("No QR code found in the image")
                return None
            
            # Get data from first QR code
            qr_data = decoded_objects[0].data.decode('utf-8')
            
            # Parse JSON data
            data_dict = json.loads(qr_data)
            
            # Store decoded data
            self.last_decoded_data = data_dict
            
            # Calculate phi resonance for the scan operation
            self._calculate_phi_resonance()
            
            return data_dict
        
        except Exception as e:
            print(f"Error scanning QR code: {e}")
            return None
    
    def scan_qr_from_camera(self, camera_id: int = 0, timeout_seconds: int = 30) -> Optional[Dict[str, Any]]:
        """
        Scan QR code from camera.
        
        Args:
            camera_id: Camera device ID
            timeout_seconds: Timeout in seconds
            
        Returns:
            Decoded data as dictionary, or None if scanning failed
        """
        try:
            # Initialize camera
            cap = cv2.VideoCapture(camera_id)
            if not cap.isOpened():
                print(f"Error: Could not open camera {camera_id}")
                return None
            
            print("Scanning for QR code... Press 'q' to quit")
            
            # Set timeout
            start_time = cv2.getTickCount()
            timeout_ticks = timeout_seconds * cv2.getTickFrequency()
            
            while True:
                # Check for timeout
                current_time = cv2.getTickCount()
                elapsed_ticks = current_time - start_time
                if elapsed_ticks > timeout_ticks:
                    print("Timeout: No QR code detected")
                    break
                
                # Capture frame
                ret, frame = cap.read()
                if not ret:
                    print("Error: Could not read frame from camera")
                    break
                
                # Convert to grayscale
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                
                # Decode QR code
                decoded_objects = decode(gray)
                
                if decoded_objects:
                    # Get data from first QR code
                    qr_data = decoded_objects[0].data.decode('utf-8')
                    
                    # Parse JSON data
                    data_dict = json.loads(qr_data)
                    
                    # Store decoded data
                    self.last_decoded_data = data_dict
                    
                    # Calculate phi resonance for the scan operation
                    self._calculate_phi_resonance()
                    
                    # Release camera
                    cap.release()
                    cv2.destroyAllWindows()
                    
                    return data_dict
                
                # Display frame
                cv2.imshow('QR Scanner', frame)
                
                # Check for key press
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("Scanning cancelled by user")
                    break
            
            # Release camera
            cap.release()
            cv2.destroyAllWindows()
            
            return None
        
        except Exception as e:
            print(f"Error scanning QR code: {e}")
            return None
    
    def _calculate_phi_resonance(self) -> None:
        """Calculate phi resonance for the scan operation."""
        if self.last_decoded_data:
            # Extract metadata if available
            metadata = self.last_decoded_data.get('metadata', {})
            
            # Get phi resonance from metadata or use default
            self.phi_resonance = metadata.get('phi_resonance', PHI_INVERSE)
            
            # Apply phi-harmonic transformation
            self.phi_resonance = (self.phi_resonance * PHI) % 1.0

def scan_qr_code(image_path: str = None, use_camera: bool = False, camera_id: int = 0) -> Dict[str, Any]:
    """
    Convenience function to scan QR code.
    
    Args:
        image_path: Path to image file containing QR code
        use_camera: Whether to use camera for scanning
        camera_id: Camera device ID
        
    Returns:
        Decoded data as dictionary, or empty dict if scanning failed
    """
    scanner = PhiQRScanner()
    
    if use_camera:
        data = scanner.scan_qr_from_camera(camera_id)
    else:
        if image_path is None:
            print("Error: No image path provided")
            return {}
        data = scanner.scan_qr_from_file(image_path)
    
    return data or {}

if __name__ == "__main__":
    # Example usage
    import sys
    
    if len(sys.argv) > 1:
        # Scan from file
        image_path = sys.argv[1]
        print(f"Scanning QR code from file: {image_path}")
        data = scan_qr_code(image_path=image_path)
    else:
        # Scan from camera
        print("Scanning QR code from camera...")
        data = scan_qr_code(use_camera=True)
    
    if data:
        print("Decoded data:")
        print(json.dumps(data, indent=2))
    else:
        print("Failed to decode QR code")
