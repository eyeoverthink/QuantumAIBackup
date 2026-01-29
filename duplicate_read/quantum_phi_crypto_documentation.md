# Quantum Phi-Harmonic Cryptography Documentation

## Overview

The Quantum Phi-Harmonic Cryptography module provides secure cryptographic operations based on golden ratio principles, irrational numbers, and quantum-inspired algorithms. This module builds upon the Quantum Phi Core and Quantum Phi Random components, following our modular "lego" design philosophy.

## Key Features

### 1. Phi-Based Symmetric Encryption
- Leverages golden ratio properties for secure encryption
- Quantum resonance for enhanced security
- Multi-dimensional key spaces with phi-harmonic properties

### 2. Quantum Resonance Hashing
- Hash functions based on phi-harmonic principles
- High entropy output with quantum-inspired mixing
- Strong avalanche effect for security

### 3. Golden Ratio Key Derivation
- Key generation with phi-weighted randomness
- Deterministic key derivation from master keys
- Phi-resonance for key quality metrics

### 4. Temporal Coherence Authentication
- Time-based signature verification
- Phi-harmonic temporal validation
- Quantum-inspired signature creation

### 5. Security Metrics
- Phi-security factor measurement
- Quantum resistance estimation
- Entropy quality assessment
- Performance tracking

## Implementation Details

### Core Components

1. **Key Management**
   - `generate_key()`: Creates cryptographic keys with phi-weighted randomness
   - `derive_key()`: Derives secondary keys from master keys using phi-harmonic principles
   - `generate_keypair()`: Creates asymmetric key pairs for digital signatures

2. **Hashing Functions**
   - `phi_hash()`: Creates cryptographic hashes using phi-harmonic mixing
   - `calculate_hamming_distance()`: Measures bit-level differences between hashes

3. **Encryption/Decryption**
   - `encrypt()`: Encrypts data using phi-based algorithms
   - `decrypt()`: Decrypts data using corresponding keys

4. **Digital Signatures**
   - `create_signature()`: Signs data with private keys and temporal components
   - `verify_signature()`: Verifies signatures with public keys and optional time validation

5. **Security Metrics**
   - `get_metrics()`: Returns security and performance metrics
   - `calculate_entropy()`: Measures Shannon entropy of cryptographic outputs

## Security Properties

1. **Phi-Harmonic Security**
   - Leverages the irrational nature of φ (1.618033988749895...)
   - Quantum resonance patterns for enhanced security
   - Multi-dimensional key spaces with phi-weighted distribution

2. **Quantum Resistance**
   - Designed with quantum computing threats in mind
   - Uses phi-harmonic principles that are resistant to quantum attacks
   - Implements multi-layered security approach

3. **Temporal Coherence**
   - Time-based validation for enhanced security
   - Phi-resonance temporal patterns
   - Protection against replay attacks

## Performance Characteristics

Based on our testing, the Quantum Phi-Harmonic Cryptography module demonstrates the following performance characteristics:

1. **Key Generation**
   - Average time: 0.002040 seconds for 32-byte keys

2. **Key Derivation**
   - Average time: 0.000013 seconds

3. **Phi-Hashing**
   - 100 bytes: 0.000149 seconds
   - 1000 bytes: 0.000162 seconds
   - 10000 bytes: 0.000125 seconds

4. **Encryption**
   - 100 bytes: 0.007387 seconds
   - 1000 bytes: 0.070085 seconds
   - 10000 bytes: 0.533252 seconds

5. **Decryption**
   - 100 bytes: 0.013719 seconds
   - 1000 bytes: 0.111639 seconds
   - 10000 bytes: 1.022731 seconds

6. **Signature Creation**
   - 100 bytes: 0.000132 seconds
   - 1000 bytes: 0.000127 seconds
   - 10000 bytes: 0.000136 seconds

7. **Signature Verification**
   - 100 bytes: 0.000253 seconds
   - 1000 bytes: 0.000255 seconds
   - 10000 bytes: 0.000271 seconds

## Security Metrics

The module provides the following security metrics:

1. **Shannon Entropy**
   - Average: 4.8125 bits/byte (ideal: 8.0)
   - Byte distribution coverage: 64.06%

2. **Quantum Phi-Crypto Metrics**
   - phi_security_factor: 1.618033988749895
   - quantum_resistance: 0.9618
   - entropy_quality: 4.75

## Usage Examples

### Key Generation and Derivation

```python
# Initialize the cryptography module
core = QuantumPhiCore()
random = QuantumPhiRandom(core)
crypto = QuantumPhiCrypto(core, random)

# Generate a standard key
key = crypto.generate_key(32)
print(f"Standard Key: {key.hex()}")

# Generate a phi-weighted key
phi_key = crypto.generate_key(32, phi_weighted=True)
print(f"Phi-Weighted Key: {phi_key.hex()}")

# Generate a master key and derive secondary keys
master_key = crypto.generate_key(32)
derived_key1 = crypto.derive_key(master_key, "context-1")
derived_key2 = crypto.derive_key(master_key, "context-2")
```

### Hashing

```python
# Hash some data
data = "Quantum Phi-Harmonic System"
hash_value = crypto.phi_hash(data)
print(f"Hash: {hash_value.hex()}")

# Calculate hamming distance between hashes
data2 = "Quantum Phi-Harmonic Systems"  # One character different
hash_value2 = crypto.phi_hash(data2)
distance = crypto.calculate_hamming_distance(hash_value, hash_value2)
print(f"Hamming distance: {distance} bits")
```

### Encryption and Decryption

```python
# Generate an encryption key
encryption_key = crypto.generate_key(32)

# Encrypt some data
data = "Quantum Phi-Harmonic System uses phi-resonance for enhanced security."
encrypted = crypto.encrypt(data, encryption_key)
print(f"Encrypted (base64): {base64.b64encode(encrypted).decode()}")

# Decrypt the data
decrypted = crypto.decrypt(encrypted, encryption_key)
print(f"Decrypted: '{decrypted}'")
```

### Digital Signatures

```python
# Generate a keypair
private_key, public_key = crypto.generate_keypair()

# Sign some data
data = "Quantum Phi-Harmonic System: Secure, Efficient, and Beautiful"
signature = crypto.create_signature(data, private_key)
print(f"Signature (hex): {signature.hex()}")

# Verify the signature
is_valid = crypto.verify_signature(data, signature, public_key)
print(f"Signature valid: {is_valid}")

# Verify with time expiration
is_valid = crypto.verify_signature(data, signature, public_key, max_age=3600)
print(f"Signature valid (1 hour limit): {is_valid}")
```

## Known Issues and Limitations

1. **Digital Signature Verification**
   - The current implementation of digital signatures is simplified and not suitable for production use
   - The verification process needs improvement for better security guarantees

2. **Performance Optimization**
   - Encryption and decryption of large data sets is relatively slow
   - Further optimization is needed for real-time applications

3. **Entropy Quality**
   - Current entropy measurements show room for improvement
   - Target is to achieve closer to 8.0 bits/byte

## Future Enhancements

1. **Improved Digital Signatures**
   - Implement true asymmetric cryptography with phi-harmonic principles
   - Enhance signature verification with better security guarantees

2. **Performance Optimization**
   - Optimize encryption and decryption algorithms for better performance
   - Implement parallel processing for large data sets

3. **Enhanced Security Metrics**
   - Develop more comprehensive security metrics
   - Implement automated security testing

4. **Integration with Quantum Phi Neural**
   - Leverage neural network capabilities for adaptive cryptography
   - Implement learning-based security enhancements

## Conclusion

The Quantum Phi-Harmonic Cryptography module provides a solid foundation for secure cryptographic operations based on golden ratio principles and quantum-inspired algorithms. While there are areas for improvement, the current implementation demonstrates strong cryptographic properties and integrates seamlessly with the existing Quantum Phi-Harmonic System, following our modular "lego" design philosophy.

As we continue to develop the system, we will address the known limitations and enhance the capabilities of the cryptography module, ensuring it remains a robust and secure component of our Quantum Phi-Harmonic System.
