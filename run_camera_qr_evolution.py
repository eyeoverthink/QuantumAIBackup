#!/usr/bin/env python3
"""
Camera QR Evolution Workflow Runner

This script runs the camera-to-QR-to-evolution workflow with proper path setup.
"""

import os
import sys
import importlib.util

# Ensure the current directory is in the path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Check for required modules
required_modules = [
    'face_qr_core',
    'face_qr_camera_extension',
    'face_qr_evolution_extension',
    'face_qr_recognition',
    'face_qr_security',
    'face_qr_json_helper',
    'face_qr_recognition_extension'
]

missing_modules = []
for module in required_modules:
    if importlib.util.find_spec(module) is None:
        missing_modules.append(module)

if missing_modules:
    print(f"Missing required modules: {', '.join(missing_modules)}")
    print("Please ensure all Face-QR modules are in your Python path.")
    sys.exit(1)

# Import the camera evolution extension
from face_qr_camera_evolution_extension import FaceQRCameraEvolutionExtension

def main():
    """Run the camera-to-QR-to-evolution workflow."""
    print("Starting Camera-to-QR-to-Evolution Workflow")
    print("===========================================")
    
    # Create camera evolution extension
    camera_evolution = FaceQRCameraEvolutionExtension()
    
    # Run the complete workflow
    success = camera_evolution.camera_to_qr_to_evolution()
    
    if success:
        print("\n✅ Workflow completed successfully!")
        print("Parameters have been evolved based on authentication results.")
        return 0
    else:
        print("\n❌ Workflow failed")
        print("Please check the error messages above for details.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
