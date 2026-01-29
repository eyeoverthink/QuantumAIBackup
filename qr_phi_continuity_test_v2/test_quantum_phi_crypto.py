#!/usr/bin/env python
"""
Quantum Phi-Harmonic System: Cryptography Module Test
=====================================================

This script tests the quantum-inspired cryptographic algorithms implemented in
the quantum_phi_crypto.py module. It demonstrates the phi-based encryption,
hashing, key derivation, and digital signature capabilities.

Tests include:
- Key generation and derivation
- Phi-harmonic hashing
- Symmetric encryption/decryption
- Digital signatures
- Performance benchmarks
- Security metrics

This follows the modular "lego" design philosophy, building upon the existing
components without modification.
"""

import time
import base64
import hashlib
import os
import sys
from decimal import Decimal
from typing import List, Dict, Any, Tuple, Callable
import math

# Import the Quantum Phi-Harmonic components
from quantum_phi_core import QuantumPhiCore
from quantum_phi_random import QuantumPhiRandom
from quantum_phi_crypto import QuantumPhiCrypto

def print_header(title: str) -> None:
    """Print a formatted section header."""
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

def test_key_generation(crypto: QuantumPhiCrypto) -> None:
    """Test key generation and derivation."""
    print_header("Key Generation and Derivation")
    
    # Standard key generation
    key1 = crypto.generate_key(32, phi_weighted=False)
    print(f"Standard Key (32 bytes): {key1.hex()}")
    
    # Phi-weighted key generation
    key2 = crypto.generate_key(32, phi_weighted=True)
    print(f"Phi-Weighted Key (32 bytes): {key2.hex()}")
    
    # Key derivation
    master_key = crypto.generate_key(32)
    derived1 = crypto.derive_key(master_key, "context-1", 16)
    derived2 = crypto.derive_key(master_key, "context-2", 16)
    derived3 = crypto.derive_key(master_key, "context-1", 16)  # Should match derived1
    
    print(f"\nMaster Key: {master_key.hex()}")
    print(f"Derived Key 1 (context-1): {derived1.hex()}")
    print(f"Derived Key 2 (context-2): {derived2.hex()}")
    print(f"Derived Key 3 (context-1): {derived3.hex()}")
    
    # Verify that same context produces same key
    print(f"Keys 1 and 3 match: {derived1 == derived3}")
    print(f"Keys 1 and 2 match: {derived1 == derived2}")
    
    # Generate asymmetric keypair
    private_key, public_key = crypto.generate_keypair()
    print(f"\nPrivate Key: {private_key.hex()}")
    print(f"Public Key: {public_key.hex()}")

def test_phi_hashing(crypto: QuantumPhiCrypto) -> None:
    """Test phi-harmonic hashing."""
    print_header("Phi-Harmonic Hashing")
    
    # Test data
    test_strings = [
        "",
        "a",
        "abc",
        "The golden ratio (φ) is an irrational number with unique properties.",
        "φ = 1.618033988749895...",
        "Quantum Phi-Harmonic System"
    ]
    
    # Hash each string and display results
    for i, test_str in enumerate(test_strings):
        hash_result = crypto.phi_hash(test_str)
        print(f"\nInput {i+1}: '{test_str}'")
        print(f"Phi-Hash: {hash_result.hex()}")
    
    # Test hash consistency
    string1 = "Quantum Phi-Harmonic System"
    hash1 = crypto.phi_hash(string1)
    hash2 = crypto.phi_hash(string1)
    print(f"\nHash consistency test: {hash1 == hash2}")
    
    # Test small changes in input
    string2 = "Quantum Phi-Harmonic system"  # Changed 'S' to 's'
    hash3 = crypto.phi_hash(string2)
    print(f"Hash of slightly modified input: {hash3.hex()}")
    print(f"Hamming distance: {hamming_distance(hash1, hash3)} bits")

def test_encryption(crypto: QuantumPhiCrypto) -> None:
    """Test phi-harmonic encryption and decryption."""
    print_header("Phi-Harmonic Encryption")
    
    # Generate encryption key
    key = crypto.generate_key()
    print(f"Encryption Key: {key.hex()}")
    
    # Test data
    test_data = [
        "Short message",
        "A longer message with some numbers: 12345 and special chars: !@#$%^&*()",
        "The golden ratio (φ = 1.618033988749895...) is the foundation of our system.",
        "Quantum Phi-Harmonic System uses phi-resonance for enhanced security."
    ]
    
    # Encrypt and decrypt each test string
    for i, data in enumerate(test_data):
        print(f"\nTest {i+1}: '{data}'")
        
        # Encrypt
        encrypted = crypto.encrypt(data, key)
        print(f"Encrypted (base64): {base64.b64encode(encrypted).decode()}")
        
        # Decrypt
        decrypted = crypto.decrypt(encrypted, key)
        print(f"Decrypted: '{decrypted.decode()}'")
        
        # Verify
        print(f"Decryption successful: {data == decrypted.decode()}")
    
    # Test encryption with wrong key
    wrong_key = crypto.generate_key()
    data = test_data[0]
    encrypted = crypto.encrypt(data, key)
    
    try:
        decrypted = crypto.decrypt(encrypted, wrong_key)
        print(f"\nDecryption with wrong key: '{decrypted.decode()}'")
    except Exception as e:
        print(f"\nDecryption with wrong key failed: {e}")

def test_signatures(crypto: QuantumPhiCrypto) -> None:
    """Test digital signatures."""
    print_header("Digital Signatures")
    
    # Generate keypair
    private_key, public_key = crypto.generate_keypair()
    print(f"Private Key: {private_key.hex()}")
    print(f"Public Key: {public_key.hex()}")
    
    # Test data
    test_data = "Quantum Phi-Harmonic System: Secure, Efficient, and Beautiful"
    print(f"\nData to sign: '{test_data}'")
    
    # Create signature
    signature = crypto.create_signature(test_data, private_key)
    print(f"Signature (hex): {signature.hex()}")
    
    # Verify signature - should be valid with correct data and key
    is_valid = crypto.verify_signature(test_data, signature, public_key)
    print(f"Signature valid: {is_valid}")
    
    # Test with modified data - should be invalid
    modified_data = test_data + "."
    is_valid = crypto.verify_signature(modified_data, signature, public_key)
    print(f"Signature valid with modified data: {is_valid}")
    
    # Test with wrong public key - should be invalid
    _, wrong_public_key = crypto.generate_keypair()
    is_valid = crypto.verify_signature(test_data, signature, wrong_public_key)
    print(f"Signature valid with wrong public key: {is_valid}")
    
    # Test with time expiration
    print("\nTesting time-based signature expiration:")
    time_signature = crypto.create_signature(test_data, private_key)
    
    # Verify with no max age - should be valid
    is_valid = crypto.verify_signature(test_data, time_signature, public_key)
    print(f"Signature valid (no time limit): {is_valid}")
    
    # Verify with future max age - should be valid
    is_valid = crypto.verify_signature(test_data, time_signature, public_key, max_age=3600)
    print(f"Signature valid (1 hour limit): {is_valid}")
    
    # Verify with expired max age - should be invalid
    is_valid = crypto.verify_signature(test_data, time_signature, public_key, max_age=0)
    print(f"Signature valid (0 second limit): {is_valid}")

def test_performance(crypto: QuantumPhiCrypto) -> None:
    """Test performance of cryptographic operations."""
    print_header("Performance Benchmarks")
    
    # Test data
    data_sizes = [100, 1000, 10000]
    iterations = 10
    
    # Prepare test data
    test_data = {}
    for size in data_sizes:
        test_data[size] = b'A' * size
    
    # Generate key once
    key = crypto.generate_key()
    private_key, public_key = crypto.generate_keypair()
    
    # Test operations
    operations = [
        ("Key Generation", lambda: crypto.generate_key()),
        ("Key Derivation", lambda: crypto.derive_key(key, "test-context")),
        ("Phi-Hashing", lambda s: crypto.phi_hash(s)),
        ("Encryption", lambda s: crypto.encrypt(s, key)),
        ("Decryption", lambda s: crypto.decrypt(crypto.encrypt(s, key), key)),
        ("Signature Creation", lambda s: crypto.create_signature(s, private_key)),
        ("Signature Verification", lambda s: crypto.verify_signature(s, 
                                                                  crypto.create_signature(s, private_key), 
                                                                  public_key))
    ]
    
    # Run benchmarks
    for op_name, op_func in operations:
        print(f"\n{op_name}:")
        
        for size in data_sizes:
            if op_name == "Key Generation" or op_name == "Key Derivation":
                # These don't depend on data size
                if size != data_sizes[0]:
                    continue
                
                start_time = time.time()
                for _ in range(iterations):
                    op_func()
                elapsed = time.time() - start_time
                
                print(f"  Average time: {elapsed/iterations:.6f} seconds")
            else:
                # Operations that depend on data size
                start_time = time.time()
                for _ in range(iterations):
                    op_func(test_data[size])
                elapsed = time.time() - start_time
                
                print(f"  {size} bytes: {elapsed/iterations:.6f} seconds")

def test_security_metrics(crypto: QuantumPhiCrypto) -> None:
    """Test and display security metrics."""
    print_header("Security Metrics")
    
    # Generate various keys and analyze them
    print("Analyzing key generation quality...")
    keys = [crypto.generate_key(32, phi_weighted=True) for _ in range(10)]
    
    # Calculate average entropy
    entropies = [calculate_entropy(key) for key in keys]
    avg_entropy = sum(entropies) / len(entropies)
    
    print(f"Average Shannon entropy: {avg_entropy:.4f} bits/byte (ideal: 8.0)")
    
    # Calculate byte distribution
    byte_counts = {}
    for key in keys:
        for byte in key:
            byte_counts[byte] = byte_counts.get(byte, 0) + 1
    
    total_bytes = sum(byte_counts.values())
    unique_bytes = len(byte_counts)
    
    print(f"Unique byte values: {unique_bytes} out of 256 possible")
    print(f"Byte distribution coverage: {unique_bytes/256:.2%}")
    
    # Display crypto module metrics
    metrics = crypto.get_metrics()
    print("\nQuantum Phi-Crypto metrics:")
    for key, value in metrics.items():
        print(f"  {key}: {value}")

def hamming_distance(data1: bytes, data2: bytes) -> int:
    """Calculate Hamming distance between two byte strings."""
    if len(data1) != len(data2):
        raise ValueError("Byte strings must be of equal length")
    
    distance = 0
    for b1, b2 in zip(data1, data2):
        # Count differing bits
        xor = b1 ^ b2
        distance += bin(xor).count('1')
    
    return distance

def calculate_entropy(data: bytes) -> float:
    """Calculate Shannon entropy of data."""
    if not data:
        return 0.0
    
    # Count byte frequencies
    counts = {}
    for byte in data:
        counts[byte] = counts.get(byte, 0) + 1
    
    # Calculate entropy
    entropy = 0
    for count in counts.values():
        probability = count / len(data)
        entropy -= probability * math.log2(probability) if probability > 0 else 0
    
    return entropy

def main() -> None:
    """Run all tests."""
    print_header("Quantum Phi-Harmonic Cryptography Test")
    
    # Initialize components
    print("Initializing Quantum Phi-Harmonic components...")
    core = QuantumPhiCore()
    random_gen = QuantumPhiRandom(core=core)
    crypto = QuantumPhiCrypto(core=core, random_gen=random_gen)
    
    print(f"Golden Ratio (φ): {float(core.PHI)}")
    print(f"Phi Inverse (φ⁻¹): {float(core.PHI_INV)}")
    
    # Run tests
    test_key_generation(crypto)
    test_phi_hashing(crypto)
    test_encryption(crypto)
    test_signatures(crypto)
    test_performance(crypto)
    test_security_metrics(crypto)
    
    print("\nTest completed successfully!")

if __name__ == "__main__":
    main()
