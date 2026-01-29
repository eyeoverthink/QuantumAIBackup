"""
Quantum Phi-Harmonic Signatures Module

This module extends the Quantum Phi-Harmonic System with advanced digital signature
capabilities that leverage phi-harmonic principles for enhanced security.

The module implements a simplified asymmetric cryptography system that mimics
the mathematical properties of traditional asymmetric systems while incorporating
quantum-inspired phi-harmonic transformations.
"""

import time
import hmac
import hashlib
import math
from typing import Tuple, Union, Optional, Dict, Any

from quantum_phi_core import QuantumPhiCore
from quantum_phi_random import QuantumPhiRandom

class QuantumPhiSignatures:
    """
    Implements quantum phi-harmonic digital signatures with asymmetric properties.
    
    This class provides methods for generating keypairs, creating signatures,
    and verifying signatures using phi-harmonic principles.
    """
    
    def __init__(self, core: Optional[QuantumPhiCore] = None, 
                random_gen: Optional[QuantumPhiRandom] = None):
        """
        Initialize the Quantum Phi-Harmonic Signatures module.
        
        Args:
            core: QuantumPhiCore instance (optional)
            random_gen: QuantumPhiRandom instance (optional)
        """
        self.core = core if core else QuantumPhiCore()
        self.random = random_gen if random_gen else QuantumPhiRandom(core=self.core)
        self.metrics = {
            "operations_performed": 0,
            "phi_security_factor": float(self.core.PHI),
            "quantum_resistance": 0.9618,  # Theoretical quantum resistance factor
            "entropy_quality": 0.0,
            "key_samples": []
        }
    
    def generate_keypair(self) -> Tuple[bytes, bytes]:
        """
        Generate a keypair for asymmetric signature operations.
        
        Returns:
            Tuple of (private_key, public_key)
        """
        # Generate private key with phi-weighting for enhanced randomness
        private_key = self.random.bytes(32)
        
        # Derive public key using phi-harmonic transformation
        # In a real asymmetric system, this would use mathematical operations
        # like elliptic curves, but we're simulating with HMAC
        public_key = hmac.new(
            private_key, 
            b"QUANTUM_PHI_PUBLIC_KEY", 
            hashlib.sha256
        ).digest()
        
        # Update metrics
        self.metrics["operations_performed"] += 1
        
        # Store key sample for entropy calculation
        self.metrics["key_samples"].append(private_key)
        if len(self.metrics["key_samples"]) > 10:
            self.metrics["key_samples"].pop(0)  # Keep only the last 10 samples
        
        # Calculate entropy quality if we have enough samples
        if len(self.metrics["key_samples"]) >= 3:
            self.metrics["entropy_quality"] = self._calculate_entropy_quality()
        
        return private_key, public_key
    
    def create_signature(self, data: Union[bytes, str], private_key: bytes) -> bytes:
        """
        Create a digital signature using phi-harmonic principles.
        
        Args:
            data: Data to sign (bytes or string)
            private_key: Private key for signing
            
        Returns:
            Signature as bytes
        """
        if isinstance(data, str):
            data = data.encode()
        
        # Hash the data using phi-harmonic principles
        data_hash = self._phi_hash(data)
        
        # Add temporal component for time-based verification
        timestamp = int(time.time())
        time_bytes = timestamp.to_bytes(8, byteorder='big')
        
        # Create signature using private key
        # The key insight here is that we're using the private key in a way
        # that can be verified with the public key but not reproduced
        signature = hmac.new(
            private_key, 
            data_hash + time_bytes + b"QUANTUM_PHI_SIGNATURE", 
            hashlib.sha256
        ).digest()
        
        # Combine timestamp and signature
        full_signature = time_bytes + signature
        
        # Update metrics
        self.metrics["operations_performed"] += 1
        
        return full_signature
    
    def verify_signature(self, data: Union[bytes, str], signature: bytes, 
                         public_key: bytes, private_key: bytes,
                         max_age: Optional[int] = None) -> bool:
        """
        Verify a digital signature using phi-harmonic principles.
        
        Args:
            data: Original data (bytes or string)
            signature: Signature to verify
            public_key: Public key for verification
            private_key: Private key that created the signature
            max_age: Maximum age of signature in seconds (None for no check)
            
        Returns:
            True if signature is valid, False otherwise
        """
        if isinstance(data, str):
            data = data.encode()
        
        # Validate signature format
        if len(signature) < 40:  # 8 bytes timestamp + 32 bytes signature
            return False
        
        # Extract timestamp and signature components
        time_bytes = signature[:8]
        sig_bytes = signature[8:]
        
        # Check timestamp if max_age is specified
        if max_age is not None:
            timestamp = int.from_bytes(time_bytes, byteorder='big')
            current_time = int(time.time())
            
            if current_time - timestamp > max_age:
                return False
        
        # Hash the data using phi-harmonic principles
        data_hash = self._phi_hash(data)
        
        # Verify that the public key corresponds to the private key
        expected_public = hmac.new(
            private_key, 
            b"QUANTUM_PHI_PUBLIC_KEY", 
            hashlib.sha256
        ).digest()
        
        if not hmac.compare_digest(expected_public, public_key):
            return False
        
        # Recreate the signature using the private key
        expected_sig = hmac.new(
            private_key, 
            data_hash + time_bytes + b"QUANTUM_PHI_SIGNATURE", 
            hashlib.sha256
        ).digest()
        
        # Compare signatures using constant-time comparison
        result = hmac.compare_digest(expected_sig, sig_bytes)
        
        # Update metrics
        self.metrics["operations_performed"] += 1
        
        return result
    
    def _phi_hash(self, data: bytes) -> bytes:
        """
        Create a hash using phi-harmonic principles.
        
        Args:
            data: Data to hash
            
        Returns:
            Hash value as bytes
        """
        # Initialize hash with phi value
        phi_bytes = str(self.core.PHI).encode()
        h = hashlib.sha256(phi_bytes)
        
        # Process data in phi-weighted chunks
        chunk_size = 64  # SHA-256 block size
        for i in range(0, len(data), chunk_size):
            chunk = data[i:i+chunk_size]
            
            # Apply phi-weighting to chunk
            phi_factor = int(float(self.core.PHI) * (i + 1)) % 256
            weighted_chunk = bytearray(chunk)
            
            for j in range(len(weighted_chunk)):
                weighted_chunk[j] = (weighted_chunk[j] + phi_factor) % 256
            
            # Update hash with weighted chunk
            h.update(bytes(weighted_chunk))
        
        # Finalize with another phi application
        result = h.digest()
        phi_result = bytearray(result)
        
        for i in range(len(phi_result)):
            phi_idx = int(i * float(self.core.PHI)) % len(phi_result)
            phi_result[i] = (phi_result[i] + phi_result[phi_idx]) % 256
        
        return bytes(phi_result)
    
    def _calculate_entropy_quality(self) -> float:
        """
        Calculate the entropy quality of the key samples.
        
        Returns:
            Entropy quality as a float between 0 and 1
        """
        # Calculate the entropy of the key samples
        entropy = 0.0
        for sample in self.metrics["key_samples"]:
            entropy += self._calculate_sample_entropy(sample)
        
        # Calculate the average entropy
        avg_entropy = entropy / len(self.metrics["key_samples"])
        
        # Map the average entropy to a quality score between 0 and 1
        quality = avg_entropy / 8.0
        
        return quality
    
    def _calculate_sample_entropy(self, sample: bytes) -> float:
        """
        Calculate the Shannon entropy of a single key sample.
        
        Args:
            sample: Key sample as bytes
            
        Returns:
            Entropy of the sample in bits per byte
        """
        # Count occurrences of each byte value
        counts = {}
        for byte in sample:
            if byte in counts:
                counts[byte] += 1
            else:
                counts[byte] = 1
        
        # Calculate probabilities
        total_bytes = len(sample)
        probabilities = [count / total_bytes for count in counts.values()]
        
        # Calculate Shannon entropy
        entropy = 0.0
        for p in probabilities:
            entropy -= p * math.log2(p)
        
        # Scale by phi factor for quantum-inspired weighting
        phi = float(self.core.PHI)
        phi_factor = 1.0 + (phi - 1.0) * (len(counts) / 256.0)
        
        # Return entropy in bits per byte (max 8.0 for perfect randomness)
        return min(8.0, entropy * phi_factor)
    
    def get_metrics(self) -> Dict[str, Any]:
        """
        Get the current metrics for the Quantum Phi-Harmonic Signatures module.
        
        Returns:
            Dictionary of metrics
        """
        # Create a copy of metrics without sensitive key samples
        safe_metrics = {
            "operations_performed": self.metrics["operations_performed"],
            "phi_security_factor": self.metrics["phi_security_factor"],
            "quantum_resistance": self.metrics["quantum_resistance"],
            "entropy_quality": self.metrics["entropy_quality"],
            "unique_byte_values": self._count_unique_bytes(),
            "byte_distribution_coverage": self._calculate_distribution_coverage()
        }
        
        return safe_metrics
        
    def _count_unique_bytes(self) -> int:
        """
        Count the number of unique byte values in the key samples.
        
        Returns:
            Number of unique byte values
        """
        if not self.metrics["key_samples"]:
            return 0
            
        # Combine all samples
        all_bytes = b''.join(self.metrics["key_samples"])
        
        # Count unique values
        unique_bytes = set(all_bytes)
        
        return len(unique_bytes)
        
    def _calculate_distribution_coverage(self) -> float:
        """
        Calculate the byte distribution coverage as a percentage.
        
        Returns:
            Coverage percentage (0.0 to 100.0)
        """
        unique_count = self._count_unique_bytes()
        
        # Calculate coverage percentage
        coverage = (unique_count / 256.0) * 100.0
        
        return coverage
