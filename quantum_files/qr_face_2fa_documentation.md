# QR Face 2FA System with Security Extensions

## Overview

The QR Face 2FA System is a comprehensive biometric authentication solution that combines facial recognition with QR code technology, enhanced with quantum-inspired security features. This system follows the "lego" modular design principle, allowing components to work together without modifying core files.

Key features include:

1. **Face Image Encoding/Decoding**: Compress and encode facial images into QR codes
2. **Phi-Harmonic Timestamps**: Utilize golden ratio-based timestamps for enhanced security
3. **Blockchain Verification**: Store authentication data in blockchain for tamper-proofing
4. **Cryptographic Security**: Digital signatures, encryption, and verification
5. **Time-Based Controls**: Expiration and replay prevention mechanisms
6. **Multi-Script Execution**: Secure execution of embedded scripts (shell, Python, etc.)

## Architecture

The system consists of several modular components:

1. **Core QR Face 2FA System** (`qr_face_2fa.py`): Base functionality for face image processing and QR code generation
2. **Security Extension** (`qr_face_2fa_security_extension.py`): Adds cryptographic verification, time-based controls, and encryption
3. **Multi-Script Executor** (`qr_multi_script_executor.py`): Enables secure execution of scripts embedded in QR codes

### Modular Design

Following the "lego" principle, each component can be used independently or combined with others:

```
┌─────────────────────┐
│ QR Face 2FA System  │
└─────────────────────┘
          ▲
          │ extends
          │
┌─────────────────────┐     ┌─────────────────────┐
│  Security Extension │◄────►│Multi-Script Executor│
└─────────────────────┘     └─────────────────────┘
```

## Installation

### Prerequisites

- Python 3.7+
- Required packages:
  - PIL (Pillow)
  - qrcode
  - pyzbar
  - opencv-python (cv2)
  - cryptography
  - numpy

### Setup

1. Install required packages:

```bash
pip install pillow qrcode pyzbar opencv-python cryptography numpy
```

2. Ensure directory structure:

```
QuantumAI/
├── qr_face_2fa.py
├── qr_face_2fa_security_extension.py
├── qr_multi_script_executor.py
├── quantum_blockchain_connector.py
└── quantum_files/
    └── qr_face_2fa_documentation.md
```

## Usage

### Basic Face 2FA Registration and Verification

```bash
# Register a new user
python qr_face_2fa.py register --user john_doe --image face.jpg --size 24 --quality 50

# Verify a user
python qr_face_2fa.py verify --image qr_code.png
```

### Creating Secured QR Codes with Scripts

```bash
# Create a QR code with a shell script
python qr_multi_script_executor.py --shell "echo 'Hello, World!'" --output script_qr.png --encrypt --expiration 30

# Create a QR code with a Python script
python qr_multi_script_executor.py --python "print('Hello from Python!')" --output python_qr.png --encrypt
```

### Executing Scripts from QR Codes

```bash
# Execute scripts from a QR code
python qr_multi_script_executor.py --qr script_qr.png
```

## Core Components

### 1. QR Face 2FA System

The base system handles:

- Face image processing (resizing, compression)
- QR code generation and reading
- User registration and verification
- Blockchain integration for tamper-proofing

#### Optimization Techniques

To ensure QR codes remain within version limits (≤ 40):

- Image resizing (16px-32px)
- Grayscale conversion
- JPEG compression (30%-60% quality)
- zlib compression for large payloads

### 2. Security Extension

Enhances the base system with:

- **Cryptographic Verification**: RSA-based digital signatures
- **Time-Based Controls**: Expiration timestamps and replay prevention
- **Payload Encryption**: Fernet symmetric encryption
- **Security Event Logging**: Comprehensive security event tracking

#### Key Security Features

- **Token-Based Authentication**: Each QR code contains a unique token
- **Phi-Harmonic Timestamps**: Golden ratio-based timestamps for enhanced security
- **Replay Prevention**: Each token can only be used once
- **Expiration**: QR codes automatically expire after a configurable time period

### 3. Multi-Script Executor

Enables secure execution of scripts embedded in QR codes:

- **Multiple Script Types**: Shell, Python, JavaScript, Ruby
- **Execution Isolation**: Scripts run in isolated environments
- **Resource Limitations**: Script size and execution time limits
- **Comprehensive Logging**: Detailed execution logs with phi-harmonic timestamps

#### Supported Script Types

| Type   | File Extension | Execution Command |
|--------|---------------|-------------------|
| Python | .py           | python            |
| Shell  | .sh           | /bin/bash         |
| JavaScript | .js       | node              |
| Ruby   | .rb           | ruby              |

## Security Considerations

### Authentication Flow

1. User presents QR code (containing encoded face image)
2. System verifies QR code signature and checks expiration
3. System extracts face image and compares with live capture
4. If match is successful, user is authenticated

### Anti-Tampering Measures

- Digital signatures prevent QR code modification
- Blockchain verification ensures system integrity
- One-time use tokens prevent replay attacks
- Phi-harmonic timestamps add quantum-inspired security layer

### Script Execution Security

- Scripts are executed in isolated environments
- Size and execution time limits prevent resource abuse
- Comprehensive logging for audit trails
- Expiration ensures scripts cannot be executed after a certain time

## Advanced Usage

### Programmatic Integration

```python
from qr_face_2fa import QRFace2FA
from qr_face_2fa_security_extension import QRFace2FASecurityExtension, apply_security_extension
from qr_multi_script_executor import QRMultiScriptExecutor

# Create and secure a QR Face 2FA instance
qr_face_2fa = QRFace2FA()
apply_security_extension(qr_face_2fa)

# Register a user with security features
result = qr_face_2fa.register_user("alice", "alice_face.jpg")

# Create a multi-script executor
security_extension = QRFace2FASecurityExtension()
executor = QRMultiScriptExecutor(security_extension=security_extension)

# Create and execute scripts
scripts = [
    {
        "type": "python",
        "content": "print('Hello from Python!')",
        "name": "greeting"
    },
    {
        "type": "shell",
        "content": "echo 'System info:' && uname -a",
        "name": "system_info"
    }
]

# Create secured payload
payload = security_extension.create_multi_script_payload(
    scripts,
    user_id="alice",
    expiration_minutes=30,
    encrypt=True
)

# Execute scripts
results = executor._execute_scripts(scripts, "alice")
```

### Customizing Security Parameters

```python
# Create security extension with custom settings
security_extension = QRFace2FASecurityExtension(base_dir="custom_security")

# Create QR code with custom expiration
payload = security_extension.create_multi_script_payload(
    scripts,
    expiration_minutes=5,  # Short expiration for sensitive operations
    encrypt=True
)
```

## Phi-Harmonic Security

The system leverages phi-harmonic principles for enhanced security:

- **Golden Ratio (φ)**: φ = (1 + √5)/2 ≈ 1.618034
- **Phi-Harmonic Timestamp**: time × φ
- **Resonance**: (time × φ) mod 1

This adds a quantum-inspired layer of security that is mathematically elegant and computationally robust.

## Error Handling and Logging

The system includes comprehensive error handling and logging:

- Detailed logs for all operations
- Security event tracking
- Execution audit trails
- Error recovery mechanisms

## Future Enhancements

Potential areas for future development:

1. **Multi-Factor Integration**: Combine with other authentication methods
2. **Distributed Verification**: Implement distributed consensus for verification
3. **Quantum Resistance**: Enhance cryptographic algorithms for quantum resistance
4. **Advanced Script Orchestration**: Support for multi-step script workflows
5. **Dynamic QR Codes**: Time-based rotating QR codes for enhanced security

## Conclusion

The QR Face 2FA System with Security Extensions provides a robust, modular, and secure authentication solution that combines biometric verification with advanced cryptographic security. By following the "lego" design principle, it allows for flexible deployment and extension while maintaining core security properties.

---

*This documentation was generated for the Quantum AI project.*
