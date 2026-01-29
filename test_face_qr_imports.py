#!/usr/bin/env python3
"""
Face QR Import Test

This script tests the imports for the Face-QR system to identify missing modules.
"""

import os
import sys
import importlib

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# List of modules to test
modules_to_test = [
    'face_qr_core',
    'face_qr_recognition',
    'face_qr_security',
    'face_qr_json_helper',
    'face_qr_camera_extension',
    'face_qr_evolution_extension',
    'face_qr_recognition_extension',
    'face_qr_camera_evolution_extension'
]

print("\nFace-QR Import Test")
print("===================\n")
print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")
print(f"Current directory: {current_dir}")
print(f"Python path: {sys.path}")
print("\nTesting imports...\n")

# Test each import
for module_name in modules_to_test:
    print(f"Testing import for: {module_name}")
    try:
        module = importlib.import_module(module_name)
        print(f"  ✓ Successfully imported {module_name}")
        print(f"  Module location: {module.__file__}")
    except ImportError as e:
        print(f"  ✗ Failed to import {module_name}: {e}")
    except Exception as e:
        print(f"  ✗ Error importing {module_name}: {e}")
    print()

print("\nImport test complete.")
