#!/usr/bin/env python3
"""
Face QR Compatibility Layer

This module provides compatibility between different versions of the Face-QR system,
ensuring that extensions can work with the core modules regardless of naming changes.
"""

import os
import sys
import importlib

# Ensure the current directory is in the path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import core modules
from face_qr_core import FaceQRBase, FaceQRConfig, PHI

# Create compatibility class for FaceQRCore
class FaceQRCore(FaceQRBase):
    """
    Compatibility class that extends FaceQRBase to provide FaceQRCore interface.
    This allows modules expecting FaceQRCore to work with the current codebase.
    """
    
    def __init__(self, config_path=None):
        """
        Initialize the compatibility layer.
        
        Args:
            config_path: Path to configuration file
        """
        super().__init__()
        self.config = FaceQRConfig(config_path)

# Apply monkey patching to make imports work
sys.modules['face_qr_core'].FaceQRCore = FaceQRCore

print("Face QR Compatibility Layer loaded")

# Main function for testing
if __name__ == "__main__":
    print("Testing Face QR Compatibility Layer...")
    core = FaceQRCore()
    print(f"Successfully created FaceQRCore instance: {core}")
