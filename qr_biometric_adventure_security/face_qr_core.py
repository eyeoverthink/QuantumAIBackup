#!/usr/bin/env python3
"""
Face QR Core Module

This module provides core functionality and base classes
for the Face-QR 2FA Security System.

It follows the 'lego' design principle, allowing it to be used independently
or combined with other modules for enhanced functionality.
"""

import os
import time
import json
import base64
import hashlib
import configparser
from typing import Dict, Any, Optional, Union

# Golden ratio constant for phi-harmonic timestamps
PHI = 1.618034

class FaceQRBase:
    """
    Base class for Face QR modules.
    """
    
    def __init__(self):
        """
        Initialize the base class.
        """
        # Get base directory
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Create quantum_files directory if it doesn't exist
        self.quantum_files_dir = os.path.join(self.base_dir, "quantum_files")
        os.makedirs(self.quantum_files_dir, exist_ok=True)
    
    @staticmethod
    def encode_base64(data: bytes) -> str:
        """
        Encode bytes to base64 string.
        
        Args:
            data: Bytes to encode
            
        Returns:
            str: Base64 encoded string
        """
        return base64.b64encode(data).decode('utf-8')
    
    @staticmethod
    def decode_base64(data: str) -> bytes:
        """
        Decode base64 string to bytes.
        
        Args:
            data: Base64 string to decode
            
        Returns:
            bytes: Decoded bytes
        """
        return base64.b64decode(data.encode('utf-8'))
    
    @staticmethod
    def calculate_hash(data: bytes) -> str:
        """
        Calculate SHA-256 hash of data.
        
        Args:
            data: Data to hash
            
        Returns:
            str: Hexadecimal hash string
        """
        return hashlib.sha256(data).hexdigest()
    
    @staticmethod
    def get_phi_timestamp() -> float:
        """
        Get current timestamp multiplied by PHI (golden ratio).
        
        Returns:
            float: Phi-harmonic timestamp
        """
        return time.time() * PHI
    
    def save_json(self, data: Dict, filename: str) -> bool:
        """
        Save data as JSON file.
        
        Args:
            data: Data to save
            filename: Filename to save to
            
        Returns:
            bool: True if successful
        """
        try:
            # Create full path
            filepath = os.path.join(self.quantum_files_dir, filename)
            
            # Save JSON
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)
            
            return True
            
        except Exception as e:
            print(f"Error saving JSON: {e}")
            return False
    
    def load_json(self, filename: str) -> Optional[Dict]:
        """
        Load data from JSON file.
        
        Args:
            filename: Filename to load from
            
        Returns:
            Dict or None: Loaded data or None if error
        """
        try:
            # Create full path
            filepath = os.path.join(self.quantum_files_dir, filename)
            
            # Check if file exists
            if not os.path.exists(filepath):
                print(f"File not found: {filepath}")
                return None
            
            # Load JSON
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            return data
            
        except Exception as e:
            print(f"Error loading JSON: {e}")
            return None


class FaceQRConfig:
    """
    Configuration manager for Face QR modules.
    """
    
    def __init__(self, config_path: str = None):
        """
        Initialize the configuration manager.
        
        Args:
            config_path: Path to configuration file
        """
        self.config = configparser.ConfigParser()
        
        # Set default values
        self._set_defaults()
        
        # Load configuration if provided
        if config_path:
            self.load(config_path)
        else:
            # Try to load from default location
            base_dir = os.path.dirname(os.path.abspath(__file__))
            default_config_path = os.path.join(base_dir, "face_qr_config.ini")
            
            if os.path.exists(default_config_path):
                self.load(default_config_path)
    
    def _set_defaults(self):
        """
        Set default configuration values.
        """
        # Security settings
        self.config["security"] = {
            "key_size": "2048",
            "hash_iterations": "100000",
            "expiration_minutes": "60"
        }
        
        # QR code settings
        self.config["qr"] = {
            "version": "40",
            "error_correction": "L",
            "box_size": "10",
            "border": "4"
        }
        
        # Image settings
        self.config["image"] = {
            "size": "24",
            "quality": "50",
            "grayscale": "True",
            "use_compression": "True"
        }
        
        # Recognition settings
        self.config["recognition"] = {
            "similarity_threshold": "0.7",
            "face_cascade": "haarcascade_frontalface_default.xml"
        }
    
    def load(self, config_path: str) -> bool:
        """
        Load configuration from file.
        
        Args:
            config_path: Path to configuration file
            
        Returns:
            bool: True if successful
        """
        try:
            # Read configuration file
            self.config.read(config_path)
            return True
            
        except Exception as e:
            print(f"Error loading configuration: {e}")
            return False
    
    def save(self, config_path: str) -> bool:
        """
        Save configuration to file.
        
        Args:
            config_path: Path to save configuration to
            
        Returns:
            bool: True if successful
        """
        try:
            # Write configuration file
            with open(config_path, 'w') as f:
                self.config.write(f)
            
            return True
            
        except Exception as e:
            print(f"Error saving configuration: {e}")
            return False
    
    def get(self, section: str, key: str, fallback: Any = None) -> Any:
        """
        Get configuration value.
        
        Args:
            section: Configuration section
            key: Configuration key
            fallback: Fallback value if not found
            
        Returns:
            Any: Configuration value
        """
        # Handle special cases for type conversion
        try:
            if section == "security":
                if key == "key_size":
                    return self.config.getint(section, key, fallback=fallback or 2048)
                elif key == "hash_iterations":
                    return self.config.getint(section, key, fallback=fallback or 100000)
                elif key == "expiration_minutes":
                    return self.config.getint(section, key, fallback=fallback or 60)
            
            elif section == "qr":
                if key == "version":
                    return self.config.getint(section, key, fallback=fallback or 40)
                elif key == "box_size":
                    return self.config.getint(section, key, fallback=fallback or 10)
                elif key == "border":
                    return self.config.getint(section, key, fallback=fallback or 4)
            
            elif section == "image":
                if key == "size":
                    return self.config.getint(section, key, fallback=fallback or 24)
                elif key == "quality":
                    return self.config.getint(section, key, fallback=fallback or 50)
                elif key == "grayscale" or key == "use_compression":
                    return self.config.getboolean(section, key, fallback=fallback or True)
            
            elif section == "recognition":
                if key == "similarity_threshold":
                    return self.config.getfloat(section, key, fallback=fallback or 0.7)
            
            # Default case
            return self.config.get(section, key, fallback=fallback)
            
        except Exception as e:
            print(f"Error getting configuration value {section}.{key}: {e}")
            return fallback
    
    def set(self, section: str, key: str, value: Any) -> bool:
        """
        Set configuration value.
        
        Args:
            section: Configuration section
            key: Configuration key
            value: Configuration value
            
        Returns:
            bool: True if successful
        """
        try:
            # Ensure section exists
            if section not in self.config:
                self.config[section] = {}
            
            # Set value
            self.config[section][key] = str(value)
            
            return True
            
        except Exception as e:
            print(f"Error setting configuration value {section}.{key}: {e}")
            return False


# Main function for testing
if __name__ == "__main__":
    # Create base instance
    base = FaceQRBase()
    
    # Test base64 encoding/decoding
    test_data = b"Hello, World!"
    encoded = base.encode_base64(test_data)
    decoded = base.decode_base64(encoded)
    
    print(f"Original: {test_data}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
    print(f"Match: {test_data == decoded}")
    
    # Test hash calculation
    hash_value = base.calculate_hash(test_data)
    print(f"Hash: {hash_value}")
    
    # Test phi timestamp
    phi_timestamp = base.get_phi_timestamp()
    print(f"Phi timestamp: {phi_timestamp}")
    
    # Test configuration
    config = FaceQRConfig()
    print("\nDefault configuration:")
    for section in config.config.sections():
        print(f"[{section}]")
        for key, value in config.config[section].items():
            print(f"  {key} = {value}")
    
    # Test getting values with type conversion
    key_size = config.get("security", "key_size")
    print(f"\nKey size: {key_size} (type: {type(key_size).__name__})")
    
    similarity_threshold = config.get("recognition", "similarity_threshold")
    print(f"Similarity threshold: {similarity_threshold} (type: {type(similarity_threshold).__name__})")
    
    grayscale = config.get("image", "grayscale")
    print(f"Grayscale: {grayscale} (type: {type(grayscale).__name__})")
