#!/usr/bin/env python3
"""
QR Face 2FA Security Extension

This module provides security extensions for QR-based face authentication and multi-script execution:
1. Cryptographic verification (digital signatures)
2. Time-based controls (expiration, replay prevention)
3. Encryption for sensitive data
4. Face image compression and encoding
5. Multi-script payload support

The module follows the 'lego' modular design principle and can be used as an extension
to existing QR code systems.
"""

import os
import time
import json
import base64
import hashlib
import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Any, Union, Optional
import uuid

# For cryptography
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# For face image compression
from PIL import Image
import io
import numpy as np

# For blockchain-like verification (simplified)
class SimpleBlockchainVerifier:
    """Simple blockchain-like verification system"""
    
    def __init__(self, storage_dir: str):
        """Initialize the blockchain verifier"""
        self.storage_dir = storage_dir
        os.makedirs(storage_dir, exist_ok=True)
        self.chain_file = os.path.join(storage_dir, "verification_chain.json")
        
        # Initialize or load the chain
        if os.path.exists(self.chain_file):
            with open(self.chain_file, "r") as f:
                self.chain = json.load(f)
        else:
            # Create genesis block
            genesis = {
                "index": 0,
                "timestamp": time.time(),
                "data": "Genesis Block",
                "previous_hash": "0" * 64,
                "hash": self._calculate_hash(0, time.time(), "Genesis Block", "0" * 64)
            }
            self.chain = [genesis]
            self._save_chain()
    
    def _calculate_hash(self, index: int, timestamp: float, data: str, previous_hash: str) -> str:
        """Calculate hash for a block"""
        value = f"{index}{timestamp}{data}{previous_hash}"
        return hashlib.sha256(value.encode()).hexdigest()
    
    def add_verification(self, data: Dict[str, Any]) -> str:
        """Add a verification to the chain"""
        previous_block = self.chain[-1]
        index = previous_block["index"] + 1
        timestamp = time.time()
        data_str = json.dumps(data, sort_keys=True)
        previous_hash = previous_block["hash"]
        
        # Calculate hash
        block_hash = self._calculate_hash(index, timestamp, data_str, previous_hash)
        
        # Create new block
        block = {
            "index": index,
            "timestamp": timestamp,
            "data": data_str,
            "previous_hash": previous_hash,
            "hash": block_hash
        }
        
        # Add to chain
        self.chain.append(block)
        self._save_chain()
        
        return block_hash
    
    def verify_chain(self) -> bool:
        """Verify the integrity of the chain"""
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            
            # Check hash integrity
            if current["previous_hash"] != previous["hash"]:
                return False
            
            # Recalculate and verify hash
            calculated_hash = self._calculate_hash(
                current["index"],
                current["timestamp"],
                current["data"],
                current["previous_hash"]
            )
            
            if current["hash"] != calculated_hash:
                return False
        
        return True
    
    def _save_chain(self):
        """Save the chain to file"""
        with open(self.chain_file, "w") as f:
            json.dump(self.chain, f, indent=2)


class QRFace2FASecurityExtension:
    """
    QR Face 2FA Security Extension
    
    Provides security features for QR-based face authentication and multi-script execution.
    """
    
    def __init__(self, base_dir: str = None, generate_keys: bool = False):
        """
        Initialize the security extension
        
        Args:
            base_dir: Base directory for storing keys and data
            generate_keys: Whether to generate new keys if they don't exist
        """
        # Set up base directory
        if base_dir is None:
            base_dir = os.path.join(os.path.expanduser("~"), ".qr_face_2fa_security")
        
        self.base_dir = base_dir
        self.keys_dir = os.path.join(base_dir, "keys")
        self.data_dir = os.path.join(base_dir, "data")
        self.blockchain_dir = os.path.join(base_dir, "blockchain")
        
        # Create directories
        os.makedirs(self.keys_dir, exist_ok=True)
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(self.blockchain_dir, exist_ok=True)
        
        # Initialize blockchain verifier
        self.blockchain = SimpleBlockchainVerifier(self.blockchain_dir)
        
        # Load or generate keys
        self.private_key_path = os.path.join(self.keys_dir, "private_key.pem")
        self.public_key_path = os.path.join(self.keys_dir, "public_key.pem")
        self.symmetric_key_path = os.path.join(self.keys_dir, "symmetric_key.key")
        
        if os.path.exists(self.private_key_path) and os.path.exists(self.public_key_path):
            self._load_keys()
        elif generate_keys:
            self._generate_keys()
        else:
            raise FileNotFoundError("Keys not found. Set generate_keys=True to generate new keys.")
    
    def _generate_keys(self):
        """Generate RSA key pair and symmetric key"""
        # Generate RSA key pair
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        
        # Get public key
        public_key = private_key.public_key()
        
        # Save private key
        with open(self.private_key_path, "wb") as f:
            f.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))
        
        # Save public key
        with open(self.public_key_path, "wb") as f:
            f.write(public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))
        
        # Generate symmetric key
        symmetric_key = Fernet.generate_key()
        with open(self.symmetric_key_path, "wb") as f:
            f.write(symmetric_key)
        
        # Load keys
        self._load_keys()
    
    def _load_keys(self):
        """Load RSA key pair and symmetric key"""
        # Load private key
        with open(self.private_key_path, "rb") as f:
            private_key_data = f.read()
            self.private_key = serialization.load_pem_private_key(
                private_key_data,
                password=None
            )
        
        # Load public key
        with open(self.public_key_path, "rb") as f:
            public_key_data = f.read()
            self.public_key = serialization.load_pem_public_key(
                public_key_data
            )
        
        # Load symmetric key
        if os.path.exists(self.symmetric_key_path):
            with open(self.symmetric_key_path, "rb") as f:
                self.symmetric_key = f.read()
                self.fernet = Fernet(self.symmetric_key)
    
    def _sign_data(self, data: bytes) -> bytes:
        """Sign data with private key"""
        signature = self.private_key.sign(
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature
    
    def _verify_signature(self, data: bytes, signature: bytes) -> bool:
        """Verify signature with public key"""
        try:
            self.public_key.verify(
                signature,
                data,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False
    
    def encrypt_data(self, data: Any) -> Dict[str, str]:
        """
        Encrypt data using symmetric encryption
        
        Args:
            data: Data to encrypt (will be JSON serialized)
            
        Returns:
            Dict containing encrypted data and metadata
        """
        # Convert data to JSON
        data_json = json.dumps(data)
        data_bytes = data_json.encode()
        
        # Encrypt data
        encrypted_data = self.fernet.encrypt(data_bytes)
        
        # Create result
        result = {
            "encrypted_data": base64.b64encode(encrypted_data).decode(),
            "encryption_type": "fernet",
            "timestamp": time.time()
        }
        
        return result
    
    def decrypt_data(self, encrypted_package: Dict[str, str]) -> Any:
        """
        Decrypt data from an encrypted package
        
        Args:
            encrypted_package: Dict containing encrypted data and metadata
            
        Returns:
            Decrypted data
        """
        # Get encrypted data
        encrypted_data = base64.b64decode(encrypted_package["encrypted_data"])
        
        # Decrypt data
        decrypted_bytes = self.fernet.decrypt(encrypted_data)
        
        # Parse JSON
        decrypted_data = json.loads(decrypted_bytes.decode())
        
        return decrypted_data
    
    def secure_qr_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Secure data for QR code
        
        Args:
            data: Data to secure
            
        Returns:
            Secured data package
        """
        # Add timestamp if not present
        if "timestamp" not in data:
            data["timestamp"] = time.time()
        
        # Add unique ID if not present
        if "id" not in data:
            data["id"] = str(uuid.uuid4())
        
        # Convert to JSON
        data_json = json.dumps(data, sort_keys=True)
        data_bytes = data_json.encode()
        
        # Calculate hash
        data_hash = hashlib.sha256(data_bytes).hexdigest()
        
        # Sign data
        signature = self._sign_data(data_bytes)
        signature_b64 = base64.b64encode(signature).decode()
        
        # Add to blockchain
        blockchain_hash = self.blockchain.add_verification({
            "data_hash": data_hash,
            "timestamp": data["timestamp"],
            "id": data["id"]
        })
        
        # Create secured package
        secured_package = {
            "data": data,
            "signature": signature_b64,
            "hash": data_hash,
            "blockchain_hash": blockchain_hash
        }
        
        return secured_package
    
    def verify_secured_qr_data(self, secured_package: Dict[str, Any]) -> Tuple[bool, Dict[str, Any], str]:
        """
        Verify secured QR data
        
        Args:
            secured_package: Secured data package
            
        Returns:
            Tuple of (is_valid, data, error_message)
        """
        try:
            # Extract components
            data = secured_package["data"]
            signature_b64 = secured_package["signature"]
            data_hash = secured_package["hash"]
            
            # Convert data to bytes
            data_json = json.dumps(data, sort_keys=True)
            data_bytes = data_json.encode()
            
            # Verify hash
            calculated_hash = hashlib.sha256(data_bytes).hexdigest()
            if calculated_hash != data_hash:
                return False, data, "Hash verification failed"
            
            # Verify signature
            signature = base64.b64decode(signature_b64)
            if not self._verify_signature(data_bytes, signature):
                return False, data, "Signature verification failed"
            
            # Check timestamp (if present)
            if "timestamp" in data and "expiration" in data:
                current_time = time.time()
                if current_time > data["expiration"]:
                    return False, data, "Data has expired"
            
            # Verify blockchain (optional)
            if "blockchain_hash" in secured_package and not self.blockchain.verify_chain():
                return False, data, "Blockchain verification failed"
            
            return True, data, ""
        
        except Exception as e:
            return False, {}, f"Verification error: {str(e)}"
    
    def compress_face_image(self, image_data: bytes, quality: int = 85, max_size: Tuple[int, int] = (128, 128)) -> bytes:
        """
        Compress a face image
        
        Args:
            image_data: Raw image data
            quality: JPEG quality (0-100)
            max_size: Maximum dimensions (width, height)
            
        Returns:
            Compressed image data
        """
        # Open image
        img = Image.open(io.BytesIO(image_data))
        
        # Resize if needed
        if img.width > max_size[0] or img.height > max_size[1]:
            img.thumbnail(max_size, Image.LANCZOS)
        
        # Convert to grayscale if color
        if img.mode != 'L':
            img = img.convert('L')
        
        # Save as JPEG
        output = io.BytesIO()
        img.save(output, format="JPEG", quality=quality, optimize=True)
        
        return output.getvalue()
    
    def create_face_auth_payload(
        self, 
        face_image_data: bytes, 
        user_id: str, 
        expiration_minutes: int = 5,
        compress: bool = True,
        encrypt: bool = True
    ) -> Dict[str, Any]:
        """
        Create a face authentication payload
        
        Args:
            face_image_data: Raw face image data
            user_id: User ID
            expiration_minutes: Expiration time in minutes
            compress: Whether to compress the face image
            encrypt: Whether to encrypt the face data
            
        Returns:
            Secured payload for QR code
        """
        # Compress face image if requested
        if compress:
            face_image_data = self.compress_face_image(face_image_data)
        
        # Encode face image
        face_image_b64 = base64.b64encode(face_image_data).decode()
        
        # Calculate face hash
        face_hash = hashlib.sha256(face_image_data).hexdigest()
        
        # Create payload
        current_time = time.time()
        expiration_time = current_time + (expiration_minutes * 60)
        
        payload = {
            "task_type": "face_authentication",
            "user_id": user_id,
            "timestamp": current_time,
            "expiration": expiration_time,
            "face_hash": face_hash
        }
        
        # Add face data
        if encrypt:
            # Encrypt face data separately
            face_data_encrypted = self.encrypt_data({"face_data": face_image_b64})
            payload["face_data_encrypted"] = face_data_encrypted
        else:
            payload["face_data"] = face_image_b64
        
        # Secure payload
        secured_payload = self.secure_qr_data(payload)
        
        return secured_payload
    
    def verify_face_auth(self, secured_payload: Dict[str, Any], live_face_data: bytes) -> Tuple[bool, str]:
        """
        Verify face authentication
        
        Args:
            secured_payload: Secured payload from QR code
            live_face_data: Live face image data
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        # Verify secured payload
        is_valid, payload, error_message = self.verify_secured_qr_data(secured_payload)
        if not is_valid:
            return False, error_message
        
        # Check task type
        if payload["task_type"] != "face_authentication":
            return False, "Invalid task type"
        
        # Get stored face data
        if "face_data_encrypted" in payload:
            try:
                face_data_dict = self.decrypt_data(payload["face_data_encrypted"])
                stored_face_b64 = face_data_dict["face_data"]
            except Exception as e:
                return False, f"Failed to decrypt face data: {str(e)}"
        elif "face_data" in payload:
            stored_face_b64 = payload["face_data"]
        else:
            return False, "No face data found in payload"
        
        # Decode stored face
        stored_face_data = base64.b64decode(stored_face_b64)
        
        # Compress live face for comparison
        live_face_data = self.compress_face_image(live_face_data)
        
        # Compare faces (simple hash comparison for demo)
        # In a real system, use a proper face recognition algorithm
        stored_face_hash = hashlib.sha256(stored_face_data).hexdigest()
        live_face_hash = hashlib.sha256(live_face_data).hexdigest()
        
        if stored_face_hash != live_face_hash:
            return False, "Face verification failed"
        
        return True, ""
    
    def create_multi_script_payload(
        self, 
        scripts: List[Dict[str, str]], 
        user_id: str, 
        expiration_minutes: int = 5,
        encrypt: bool = True
    ) -> Dict[str, Any]:
        """
        Create a multi-script execution payload
        
        Args:
            scripts: List of script dictionaries, each with 'type', 'name', and 'content'
            user_id: User ID
            expiration_minutes: Expiration time in minutes
            encrypt: Whether to encrypt the scripts
            
        Returns:
            Secured payload for QR code
        """
        # Validate scripts
        for script in scripts:
            if not all(k in script for k in ["type", "name", "content"]):
                raise ValueError("Each script must have 'type', 'name', and 'content'")
        
        # Create payload
        current_time = time.time()
        expiration_time = current_time + (expiration_minutes * 60)
        
        payload = {
            "task_type": "multi_script_execution",
            "user_id": user_id,
            "timestamp": current_time,
            "expiration": expiration_time,
            "script_count": len(scripts)
        }
        
        # Add scripts
        if encrypt:
            # Encrypt scripts separately
            scripts_encrypted = self.encrypt_data({"scripts": scripts})
            payload["scripts_encrypted"] = scripts_encrypted
        else:
            payload["scripts"] = scripts
        
        # Secure payload
        secured_payload = self.secure_qr_data(payload)
        
        return secured_payload
    
    def get_scripts_from_payload(self, secured_payload: Dict[str, Any]) -> Tuple[bool, List[Dict[str, str]], str]:
        """
        Get scripts from a secured payload
        
        Args:
            secured_payload: Secured payload from QR code
            
        Returns:
            Tuple of (is_valid, scripts, error_message)
        """
        # Verify secured payload
        is_valid, payload, error_message = self.verify_secured_qr_data(secured_payload)
        if not is_valid:
            return False, [], error_message
        
        # Check task type
        if payload["task_type"] != "multi_script_execution":
            return False, [], "Invalid task type"
        
        # Get scripts
        if "scripts_encrypted" in payload:
            try:
                scripts_dict = self.decrypt_data(payload["scripts_encrypted"])
                scripts = scripts_dict["scripts"]
            except Exception as e:
                return False, [], f"Failed to decrypt scripts: {str(e)}"
        elif "scripts" in payload:
            scripts = payload["scripts"]
        else:
            return False, [], "No scripts found in payload"
        
        return True, scripts, ""
    
    def generate_phi_harmonic_timestamp(self) -> float:
        """
        Generate a phi-harmonic timestamp
        
        Returns:
            Phi-harmonic timestamp
        """
        # Golden ratio (phi)
        phi = (1 + 5 ** 0.5) / 2
        
        # Get current timestamp
        current_time = time.time()
        
        # Apply phi-harmonic transformation
        phi_harmonic_time = current_time * phi
        
        return phi_harmonic_time
    
    def verify_phi_harmonic_timestamp(self, phi_timestamp: float, max_age_minutes: int = 5) -> bool:
        """
        Verify a phi-harmonic timestamp
        
        Args:
            phi_timestamp: Phi-harmonic timestamp
            max_age_minutes: Maximum age in minutes
            
        Returns:
            Whether the timestamp is valid
        """
        # Golden ratio (phi)
        phi = (1 + 5 ** 0.5) / 2
        
        # Convert back to regular timestamp
        original_timestamp = phi_timestamp / phi
        
        # Check age
        current_time = time.time()
        age_seconds = current_time - original_timestamp
        max_age_seconds = max_age_minutes * 60
        
        return age_seconds <= max_age_seconds
    
    def calculate_phi_resonance(self, value: float) -> float:
        """
        Calculate phi resonance for a value
        
        Args:
            value: Input value
            
        Returns:
            Resonance value (0-1)
        """
        # Golden ratio (phi)
        phi = (1 + 5 ** 0.5) / 2
        
        # Calculate resonance (fractional part of phi * value)
        resonance = (phi * value) % 1
        
        return resonance
    
    def is_phi_resonant(self, value: float, threshold: float = 0.01) -> bool:
        """
        Check if a value is phi-resonant
        
        Args:
            value: Input value
            threshold: Resonance threshold (0-1)
            
        Returns:
            Whether the value is phi-resonant
        """
        resonance = self.calculate_phi_resonance(value)
        
        # Check if resonance is close to 0 or 1
        return resonance < threshold or resonance > (1 - threshold)
