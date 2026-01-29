# Face-QR 2FA Security System Documentation

## Overview

The Face-QR 2FA Security System is a modular authentication system that combines facial recognition with QR codes to provide secure two-factor authentication. The system follows the 'lego' design principle, with components that can be used independently or combined for enhanced functionality.

This document provides comprehensive documentation for the Face-QR system, including architecture, components, usage, and examples.

## Architecture

The Face-QR system is built with a modular architecture following these key principles:

1. **Modular Components**: Each component is designed to work independently or in combination with others.
2. **Phi-Harmonic Design**: The system incorporates golden ratio (phi) principles for timestamps and calculations.
3. **Lego Approach**: New functionality is added through extensions without modifying core files.
4. **Progressive Optimization**: Multiple optimization techniques are applied to ensure QR codes fit within version limits.

### System Components

The system consists of the following core components:

1. **Core Module** (`face_qr_core.py`): Provides base classes and shared functionality.
2. **Security Module** (`face_qr_security.py`): Handles cryptographic operations and security features.
3. **Recognition Module** (`face_qr_recognition.py`): Manages face detection, recognition, and verification.
4. **QR Generation** (`generate_face_qr.py`): Encodes face images into QR codes with optimization.
5. **QR Task Worker Extension** (`qr_task_worker_extension.py`): Extends task worker to handle face image tasks.
6. **Testing Framework** (`test_face_qr_system.py`): Provides end-to-end testing of the system.

## Core Module

The core module (`face_qr_core.py`) serves as the foundation for the Face-QR system, providing:

- Base class (`FaceQRBase`) with common utilities
- Configuration management (`FaceQRConfig`)
- Constants and shared functionality

### Key Features

- Base64 encoding/decoding
- Hash calculation
- Phi-harmonic timestamps
- JSON data handling
- Configuration management with type conversion

### Usage Example

```python
from face_qr_core import FaceQRBase, FaceQRConfig, PHI

# Create base instance
base = FaceQRBase()

# Use utilities
encoded = base.encode_base64(b"Hello, World!")
hash_value = base.calculate_hash(b"Hello, World!")
phi_timestamp = base.get_phi_timestamp()

# Use configuration
config = FaceQRConfig()
image_size = config.get("image", "size")  # Returns int
```

## Security Module

The security module (`face_qr_security.py`) handles cryptographic operations and security features, including:

- Key pair generation and management
- Data signing and signature verification
- Encryption and decryption
- Face authentication payload creation and verification

### Key Features

- RSA key pair generation
- PSS signature scheme with SHA-256
- Fernet symmetric encryption
- Face authentication with expiration
- Phi-harmonic timestamps for security operations

### Usage Example

```python
from face_qr_security import FaceQRSecurity

# Create security instance
security = FaceQRSecurity()

# Sign and verify data
test_data = b"Test data for signing"
signature = security.sign_data(test_data)
is_valid = security.verify_signature(test_data, signature)

# Encrypt and decrypt data
encryption_result = security.encrypt_data(b"Secret data")
decryption_result = security.decrypt_data(
    encryption_result["encrypted_data"],
    encryption_result["key"]
)

# Create face authentication payload
with open("face.jpg", "rb") as f:
    face_image_data = f.read()

auth_payload = security.create_face_auth_payload(
    face_image_data,
    "user123",
    expiration_minutes=10
)

# Verify face authentication
is_valid, message = security.verify_face_auth(auth_payload, face_image_data)
```

## Recognition Module

The recognition module (`face_qr_recognition.py`) handles face detection, recognition, and verification:

- Face detection in images
- Feature extraction
- Face comparison and verification
- Face hash generation
- Face recognition training and prediction

### Key Features

- OpenCV-based face detection (with fallback)
- Feature extraction for face comparison
- Similarity calculation between faces
- Face verification with configurable threshold
- Face hash generation for authentication

### Usage Example

```python
from face_qr_recognition import FaceQRRecognition

# Create recognition instance
recognition = FaceQRRecognition()

# Load images
with open("reference.jpg", "rb") as f:
    reference_image_data = f.read()

with open("test.jpg", "rb") as f:
    test_image_data = f.read()

# Verify faces
is_match, similarity = recognition.verify_face(
    reference_image_data,
    test_image_data,
    threshold=0.7
)

# Generate face hash
face_hash = recognition.hash_face(reference_image_data)
```

## QR Generation

The QR generation module (`generate_face_qr.py`) encodes face images into QR codes with optimization:

- Image resizing
- Grayscale conversion
- JPEG compression
- zlib compression for large payloads
- QR code generation with optimized settings

### Optimization Techniques

The system uses several optimization techniques to ensure QR codes fit within version limits (≤ 40):

1. **Image Resizing**: Reduces image dimensions to 16-32px.
2. **Grayscale Conversion**: Reduces color data to a single channel.
3. **JPEG Compression**: Applies lossy compression with adjustable quality (30-60%).
4. **zlib Compression**: Applies additional compression for large payloads.

### Usage Example

```python
from generate_face_qr import generate_qr_from_image

# Generate QR code from face image
result = generate_qr_from_image(
    "face.jpg",
    "face_qr.png",
    size=24,
    jpeg_quality=50,
    grayscale=True,
    use_compression=True
)
```

## QR Task Worker Extension

The QR task worker extension (`qr_task_worker_extension.py`) extends the task worker to handle face image tasks:

- Adds support for `display_face_image` task type
- Decodes base64 image data
- Reconstructs images from QR code payloads

### Usage Example

```python
from qr_task_worker_extension import handle_display_face_image

# Apply extension
apply_extension()

# Handle task manually
payload = {
    "task_type": "display_face_image",
    "image_data": "base64_encoded_image_data",
    "compressed": True
}

task = {
    "output_dir": "/path/to/output"
}

output_path = handle_display_face_image(payload, task)
```

## Testing Framework

The testing framework (`test_face_qr_system.py`) provides end-to-end testing of the Face-QR system:

- Core functionality testing
- Security module testing
- Recognition module testing
- QR generation testing
- QR decoding testing
- End-to-end workflow testing

### Usage Example

```bash
python test_face_qr_system.py --image /path/to/face.jpg --config /path/to/config.ini
```

## Progressive Optimization Script

The system includes a shell script (`run_face_qr_test.sh`) that automatically tries progressively more aggressive optimization settings:

1. 24px / 50% quality
2. 16px / 40% quality
3. 12px / 30% quality

This ensures the system can handle various face images while staying within QR code version limits.

## Installation and Dependencies

The Face-QR system requires the following dependencies:

- Python 3.6+
- OpenCV (optional, for enhanced face recognition)
- Pillow (PIL)
- qrcode
- pyzbar
- cryptography
- numpy

Install dependencies:

```bash
pip install opencv-python pillow qrcode pyzbar cryptography numpy
```

## Configuration

The system uses a configuration file (`face_qr_config.ini`) with the following sections:

### Security Settings

```ini
[security]
key_size = 2048
hash_iterations = 100000
expiration_minutes = 60
```

### QR Code Settings

```ini
[qr]
version = 40
error_correction = L
box_size = 10
border = 4
```

### Image Settings

```ini
[image]
size = 24
quality = 50
grayscale = True
use_compression = True
```

### Recognition Settings

```ini
[recognition]
similarity_threshold = 0.7
face_cascade = haarcascade_frontalface_default.xml
```

## Best Practices

1. **Image Optimization**: Use the smallest acceptable image size and quality for your use case.
2. **Security**: Regularly rotate keys and use short expiration times for authentication payloads.
3. **Testing**: Run the test suite with various face images to ensure robustness.
4. **Extensions**: Follow the 'lego' principle when adding new functionality.
5. **Configuration**: Adjust configuration parameters based on your specific requirements.

## Troubleshooting

### QR Code Version Error

If you encounter a "ValueError: Invalid version (was 41, expected 1 to 40)" error:

1. Reduce image size (try 16px or 12px)
2. Lower JPEG quality (try 40% or 30%)
3. Enable grayscale conversion
4. Enable zlib compression

### Face Detection Issues

If face detection is not working:

1. Ensure OpenCV is installed
2. Check lighting and orientation of face images
3. Adjust the face cascade parameters
4. Use a higher resolution input image before optimization

### Authentication Failures

If face authentication is failing:

1. Check expiration time of authentication payloads
2. Verify that the same face is being used
3. Adjust the similarity threshold
4. Check for signature verification issues

## Future Enhancements

1. **Multi-Face Support**: Add support for multiple faces in a single QR code.
2. **Liveness Detection**: Implement liveness detection to prevent spoofing.
3. **Blockchain Integration**: Store authentication records on a blockchain.
4. **Mobile App**: Develop a mobile app for scanning and generating Face-QR codes.
5. **Advanced Recognition**: Integrate with more advanced face recognition models.

## Conclusion

The Face-QR 2FA Security System provides a robust, modular approach to face-based authentication using QR codes. By following the 'lego' design principle and incorporating phi-harmonic elements, the system offers a flexible and secure solution for two-factor authentication needs.
