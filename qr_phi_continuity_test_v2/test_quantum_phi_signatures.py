"""
Test script for the Quantum Phi-Harmonic Signatures module.

This script demonstrates the functionality of the Quantum Phi-Harmonic Signatures
module, including keypair generation, signature creation, and verification.
"""

import time
import binascii
from quantum_phi_core import QuantumPhiCore
from quantum_phi_random import QuantumPhiRandom
from quantum_phi_signatures import QuantumPhiSignatures

def print_header(title):
    """Print a formatted header."""
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

def main():
    """Main test function."""
    print_header("Quantum Phi-Harmonic Signatures Test")
    
    # Initialize components
    print("Initializing Quantum Phi-Harmonic components...")
    core = QuantumPhiCore()
    random_gen = QuantumPhiRandom(core=core)
    signatures = QuantumPhiSignatures(core=core, random_gen=random_gen)
    
    print(f"Golden Ratio (φ): {core.PHI}")
    print(f"Phi Inverse (φ⁻¹): {core.PHI_INV}")
    
    # Test keypair generation
    print_header("Keypair Generation")
    private_key, public_key = signatures.generate_keypair()
    
    print(f"Private Key: {binascii.hexlify(private_key).decode()}")
    print(f"Public Key: {binascii.hexlify(public_key).decode()}")
    
    # Test signature creation and verification
    print_header("Digital Signatures")
    
    # Test case 1: Basic signature
    data = "Quantum Phi-Harmonic System: Secure, Efficient, and Beautiful"
    print(f"Data to sign: '{data}'")
    
    signature = signatures.create_signature(data, private_key)
    print(f"Signature (hex): {binascii.hexlify(signature).decode()}")
    
    is_valid = signatures.verify_signature(data, signature, public_key, private_key)
    print(f"Signature valid: {is_valid}")
    
    # Test case 2: Modified data
    modified_data = data + " (modified)"
    is_valid = signatures.verify_signature(modified_data, signature, public_key, private_key)
    print(f"Signature valid with modified data: {is_valid}")
    
    # Test case 3: Wrong keypair
    wrong_private, wrong_public = signatures.generate_keypair()
    is_valid = signatures.verify_signature(data, signature, wrong_public, wrong_private)
    print(f"Signature valid with wrong keypair: {is_valid}")
    
    # Test case 4: Time-based expiration
    print("\nTesting time-based signature expiration:")
    
    # No time limit
    is_valid = signatures.verify_signature(data, signature, public_key, private_key)
    print(f"Signature valid (no time limit): {is_valid}")
    
    # 1 hour limit
    is_valid = signatures.verify_signature(data, signature, public_key, private_key, max_age=3600)
    print(f"Signature valid (1 hour limit): {is_valid}")
    
    # Create an expired signature
    old_time = int(time.time()) - 10  # 10 seconds ago
    time_bytes = old_time.to_bytes(8, byteorder='big')
    data_hash = signatures._phi_hash(data.encode())
    sig_part = signatures.create_signature(data, private_key)[8:]  # Just the signature part
    expired_sig = time_bytes + sig_part
    
    # Verify with 5-second limit
    is_valid = signatures.verify_signature(data, expired_sig, public_key, private_key, max_age=5)
    print(f"Expired signature valid (5 second limit): {is_valid}")
    
    # Performance benchmarks
    print_header("Performance Benchmarks")
    
    # Keypair generation
    start_time = time.time()
    iterations = 10
    for _ in range(iterations):
        signatures.generate_keypair()
    avg_time = (time.time() - start_time) / iterations
    print(f"Keypair Generation (average of {iterations} runs): {avg_time:.6f} seconds")
    
    # Signature creation
    test_sizes = [100, 1000, 10000]
    for size in test_sizes:
        test_data = "A" * size
        start_time = time.time()
        iterations = 10
        for _ in range(iterations):
            signatures.create_signature(test_data, private_key)
        avg_time = (time.time() - start_time) / iterations
        print(f"Signature Creation ({size} bytes): {avg_time:.6f} seconds")
    
    # Signature verification
    for size in test_sizes:
        test_data = "A" * size
        test_sig = signatures.create_signature(test_data, private_key)
        start_time = time.time()
        iterations = 10
        for _ in range(iterations):
            signatures.verify_signature(test_data, test_sig, public_key, private_key)
        avg_time = (time.time() - start_time) / iterations
        print(f"Signature Verification ({size} bytes): {avg_time:.6f} seconds")
    
    # Security metrics
    print_header("Security Metrics")
    metrics = signatures.get_metrics()
    print("Quantum Phi-Signatures metrics:")
    for key, value in metrics.items():
        print(f"  {key}: {value}")
    
    print("\nTest completed successfully!")

if __name__ == "__main__":
    main()
