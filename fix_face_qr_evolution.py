#!/usr/bin/env python3
"""
Face QR Evolution Fix

This script fixes the circular dependency issue in the Face-QR evolution extension.
"""

import os
import sys
import importlib.util
import qrcode

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

print("\nFace-QR Evolution Fix")
print("====================\n")
print(f"Python executable: {sys.executable}")
print(f"Current directory: {current_dir}")

# Check if qrcode module is available
try:
    print(f"QR code module version: {qrcode.__version__}")
except Exception as e:
    print(f"Error checking qrcode module: {e}")

# Fix the face_qr_camera_evolution_extension.py file
try:
    print("\nChecking face_qr_camera_evolution_extension.py...")
    
    # Check if qrcode is imported in the file
    with open('face_qr_camera_evolution_extension.py', 'r') as f:
        content = f.read()
    
    if 'import qrcode' not in content:
        print("  Missing qrcode import in face_qr_camera_evolution_extension.py")
        print("  Adding import statement...")
        
        # Add import statement after the other imports
        modified_content = content.replace(
            'from typing import Dict, Any, List, Tuple, Optional, Union',
            'from typing import Dict, Any, List, Tuple, Optional, Union\nimport qrcode'
        )
        
        # Write the modified content back to the file
        with open('face_qr_camera_evolution_extension.py', 'w') as f:
            f.write(modified_content)
        
        print("  ✓ Added qrcode import to face_qr_camera_evolution_extension.py")
    else:
        print("  ✓ qrcode is already imported in face_qr_camera_evolution_extension.py")
    
    print("\nFix complete. Try running the camera evolution workflow again.")
    
except Exception as e:
    print(f"Error fixing face_qr_camera_evolution_extension.py: {e}")
    import traceback
    traceback.print_exc()
