#!/usr/bin/env python3
"""
Face QR Security Module

This module handles cryptographic operations and security features
for the Face-QR 2FA Security System.

It follows the 'lego' design principle, allowing it to be used independently
or combined with other modules for enhanced functionality.
"""

import os
import time
import json
import hashlib
import base64
import secrets
from typing import Dict, Tuple, Optional, Union, Any, List
from datetime import datetime, timedelta

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

# Import core module
from face_qr_core import FaceQRBase, FaceQRConfig, PHI

class FaceQRSecurity(FaceQRBase):
    """
    Handles cryptographic operations and security features.
    """
    
    def __init__(self, config_path: str = None, generate_keys: bool = False):
        """
        Initialize the security module.
        
        Args:
            config_path: Path to configuration file
            generate_keys: Whether to generate new keys
        """
        super().__init__()
        self.config = FaceQRConfig(config_path)
        
        # Create keys directory if it doesn't exist
        self.keys_dir = os.path.join(self.base_dir, "keys")
        os.makedirs(self.keys_dir, exist_ok=True)
        
        # Initialize keys
        self.private_key = None
        self.public_key = None
        
        # Load or generate keys
        if generate_keys:
            self.generate_key_pair()
        else:
            self.load_key_pair()
    
    def generate_key_pair(self) -> bool:
        """
        Generate RSA key pair.
        
        Returns:
            bool: True if successful
        """
        try:
            # Get key size from config
            key_size = self.config.get("security", "key_size")
            
            # Generate private key
            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=key_size,
                backend=default_backend()
            )
            
            # Get public key
            public_key = private_key.public_key()
            
            # Save keys
            self.private_key = private_key
            self.public_key = public_key
            
            # Serialize and save to files
            private_pem = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
            
            public_pem = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
            
            with open(os.path.join(self.keys_dir, "private_key.pem"), "wb") as f:
                f.write(private_pem)
            
            with open(os.path.join(self.keys_dir, "public_key.pem"), "wb") as f:
                f.write(public_pem)
            
            return True
            
        except Exception as e:
            print(f"Error generating key pair: {e}")
            return False
    
    def load_key_pair(self) -> bool:
        """
        Load RSA key pair from files.
        
        Returns:
            bool: True if successful
        """
        try:
            # Check if key files exist
            private_key_path = os.path.join(self.keys_dir, "private_key.pem")
            public_key_path = os.path.join(self.keys_dir, "public_key.pem")
            
            if not os.path.exists(private_key_path) or not os.path.exists(public_key_path):
                print("Key files not found, generating new keys...")
                return self.generate_key_pair()
            
            # Load private key
            with open(private_key_path, "rb") as f:
                private_pem = f.read()
                self.private_key = serialization.load_pem_private_key(
                    private_pem,
                    password=None,
                    backend=default_backend()
                )
            
            # Load public key
            with open(public_key_path, "rb") as f:
                public_pem = f.read()
                self.public_key = serialization.load_pem_public_key(
                    public_pem,
                    backend=default_backend()
                )
            
            return True
            
        except Exception as e:
            print(f"Error loading key pair: {e}")
            return False
    
    def sign_data(self, data: bytes) -> Optional[bytes]:
        """
        Sign data with private key.
        
        Args:
            data: Data to sign
            
        Returns:
            bytes or None: Signature or None if error
        """
        try:
            # Ensure private key is loaded
            if self.private_key is None:
                if not self.load_key_pair():
                    return None
            
            # Sign data
            signature = self.private_key.sign(
                data,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            
            return signature
            
        except Exception as e:
            print(f"Error signing data: {e}")
            return None
    
    def verify_signature(self, data: bytes, signature: bytes) -> bool:
        """
        Verify signature with public key.
        
        Args:
            data: Original data
            signature: Signature to verify
            
        Returns:
            bool: True if signature is valid
        """
        try:
            # Ensure public key is loaded
            if self.public_key is None:
                if not self.load_key_pair():
                    return False
            
            # Verify signature
            self.public_key.verify(
                signature,
                data,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            
            # If no exception was raised, signature is valid
            return True
            
        except Exception as e:
            print(f"Invalid signature: {e}")
            return False
    
    def generate_symmetric_key(self, password: str = None) -> bytes:
        """
        Generate symmetric encryption key.
        
        Args:
            password: Optional password for key derivation
            
        Returns:
            bytes: Encryption key
        """
        if password:
            # Derive key from password
            salt = secrets.token_bytes(16)
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=self.config.get("security", "hash_iterations"),
                backend=default_backend()
            )
            key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        else:
            # Generate random key
            key = Fernet.generate_key()
        
        return key
    
    def encrypt_data(self, data: bytes, key: bytes = None) -> Dict:
        """
        Encrypt data with symmetric key.
        
        Args:
            data: Data to encrypt
            key: Encryption key (generated if not provided)
            
        Returns:
            Dict: Encrypted data and key
        """
        try:
            # Generate key if not provided
            if key is None:
                key = self.generate_symmetric_key()
            
            # Create Fernet cipher
            cipher = Fernet(key)
            
            # Encrypt data
            encrypted_data = cipher.encrypt(data)
            
            return {
                "success": True,
                "encrypted_data": encrypted_data,
                "key": key
            }
            
        except Exception as e:
            print(f"Error encrypting data: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def decrypt_data(self, encrypted_data: bytes, key: bytes) -> Dict:
        """
        Decrypt data with symmetric key.
        
        Args:
            encrypted_data: Encrypted data
            key: Decryption key
            
        Returns:
            Dict: Decrypted data
        """
        try:
            # Create Fernet cipher
            cipher = Fernet(key)
            
            # Decrypt data
            decrypted_data = cipher.decrypt(encrypted_data)
            
            return {
                "success": True,
                "decrypted_data": decrypted_data
            }
            
        except Exception as e:
            print(f"Error decrypting data: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def create_face_auth_payload(self, face_image_data: bytes, user_id: str,
                                expiration_minutes: int = None, compress: bool = True,
                                encrypt: bool = True) -> Dict:
        """
        Create face authentication payload.
        
        Args:
            face_image_data: Face image data
            user_id: User ID
            expiration_minutes: Expiration time in minutes
            compress: Whether to compress the image
            encrypt: Whether to encrypt the payload
            
        Returns:
            Dict: Authentication payload
        """
        try:
            # Use default expiration if not provided
            if expiration_minutes is None:
                expiration_minutes = self.config.get("security", "expiration_minutes")
            
            # Calculate expiration timestamp
            expiration = time.time() + (expiration_minutes * 60)
            phi_expiration = expiration * PHI
            
            # Calculate face hash
            face_hash = self.calculate_hash(face_image_data)
            
            # Create payload
            payload = {
                "user_id": user_id,
                "face_hash": face_hash,
                "timestamp": time.time(),
                "phi_timestamp": time.time() * PHI,
                "expiration": expiration,
                "phi_expiration": phi_expiration
            }
            
            # Add face image data
            if compress:
                # Import PIL here to avoid circular import
                from PIL import Image
                import io
                
                # Compress image
                image = Image.open(io.BytesIO(face_image_data))
                buffer = io.BytesIO()
                image.save(buffer, format="JPEG", quality=60)
                compressed_data = buffer.getvalue()
                
                # Encode as base64
                payload["face_image"] = self.encode_base64(compressed_data)
                payload["compressed"] = True
            else:
                # Encode as base64
                payload["face_image"] = self.encode_base64(face_image_data)
                payload["compressed"] = False
            
            # Sign payload
            payload_bytes = json.dumps(payload).encode('utf-8')
            signature = self.sign_data(payload_bytes)
            
            if signature is None:
                return {
                    "success": False,
                    "error": "Failed to sign payload"
                }
            
            # Add signature
            payload["signature"] = self.encode_base64(signature)
            
            # Encrypt if requested
            if encrypt:
                # Convert to JSON
                payload_json = json.dumps(payload)
                
                # Encrypt
                encryption_result = self.encrypt_data(payload_json.encode('utf-8'))
                
                if not encryption_result["success"]:
                    return {
                        "success": False,
                        "error": f"Failed to encrypt payload: {encryption_result['error']}"
                    }
                
                # Create encrypted payload
                encrypted_payload = {
                    "encrypted": True,
                    "data": self.encode_base64(encryption_result["encrypted_data"]),
                    "key": self.encode_base64(encryption_result["key"])
                }
                
                return {
                    "success": True,
                    "payload": encrypted_payload,
                    "encrypted": True
                }
            
            # Return unencrypted payload
            return {
                "success": True,
                "payload": payload,
                "encrypted": False
            }
            
        except Exception as e:
            print(f"Error creating face auth payload: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def verify_face_auth(self, auth_payload: Dict, face_image_data: bytes) -> Tuple[bool, str]:
        """
        Verify face authentication payload.
        
        Args:
            auth_payload: Authentication payload
            face_image_data: Face image data to verify
            
        Returns:
            Tuple[bool, str]: (is_valid, error_message)
        """
        try:
            # Check if payload is encrypted
            payload = auth_payload.get("payload", {})
            
            if auth_payload.get("encrypted", False) or payload.get("encrypted", False):
                # Decrypt payload
                encrypted_data = self.decode_base64(payload["data"])
                key = self.decode_base64(payload["key"])
                
                decryption_result = self.decrypt_data(encrypted_data, key)
                
                if not decryption_result["success"]:
                    return False, f"Failed to decrypt payload: {decryption_result['error']}"
                
                # Parse decrypted payload
                payload = json.loads(decryption_result["decrypted_data"].decode('utf-8'))
            
            # Verify signature
            signature = self.decode_base64(payload["signature"])
            
            # Remove signature from payload for verification
            verification_payload = payload.copy()
            del verification_payload["signature"]
            
            # Convert to bytes
            payload_bytes = json.dumps(verification_payload).encode('utf-8')
            
            if not self.verify_signature(payload_bytes, signature):
                return False, "Invalid signature"
            
            # Check expiration
            current_time = time.time()
            if current_time > payload["expiration"]:
                return False, "Authentication expired"
            
            # Verify face hash
            face_hash = self.calculate_hash(face_image_data)
            if face_hash != payload["face_hash"]:
                return False, "Face verification failed"
            
            # All checks passed
            return True, "Authentication successful"
            
        except Exception as e:
            return False, f"Error verifying authentication: {e}"

# Main function for testing
if __name__ == "__main__":
    import sys
    
    # Create security module
    security = FaceQRSecurity(generate_keys=True)
    
    # Test signing and verification
    test_data = b"Test data for signing"
    signature = security.sign_data(test_data)
    
    if signature:
        print(f"Signature created: {len(signature)} bytes")
        
        # Verify signature
        is_valid = security.verify_signature(test_data, signature)
        print(f"Signature valid: {is_valid}")
        
        # Test with modified data
        is_valid = security.verify_signature(b"Modified data", signature)
        print(f"Modified data signature valid (should be False): {is_valid}")
    
    # Test encryption and decryption
    encryption_result = security.encrypt_data(b"Secret data")
    
    if encryption_result["success"]:
        print(f"Data encrypted: {len(encryption_result['encrypted_data'])} bytes")
        
        # Decrypt data
        decryption_result = security.decrypt_data(
            encryption_result["encrypted_data"],
            encryption_result["key"]
        )
        
        if decryption_result["success"]:
            print(f"Decrypted data: {decryption_result['decrypted_data'].decode('utf-8')}")
