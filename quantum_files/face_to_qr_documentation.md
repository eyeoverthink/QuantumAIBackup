# Face Image to QR Code Integration System

## Overview

This system enables encoding facial images into QR codes and decoding them back, following phi-harmonic principles and the "lego" modular design approach. The system is designed to be non-invasive, adding functionality without modifying core files.

## Components

### 1. Image Encoder (`generate_face_qr.py`)

Converts face images into QR codes with embedded display tasks:

- Resizes images to configurable dimensions (default: 32x32 pixels)
- Converts images to grayscale to reduce data size
- Compresses images using JPEG format with configurable quality (default: 60%)
- Encodes the compressed image as base64 within a JSON payload
- Uses zlib compression when needed to fit within QR code version limits
- Embeds phi-harmonic timestamps for unique identification
- Generates QR codes with the task payload

### 2. Task Worker Extension (`qr_task_worker_extension.py`)

Extends the QR task worker to handle face image display tasks:

- Follows the "lego" principle by adding functionality without modifying core files
- Uses monkey patching to extend the existing `process_qr_image_file` function
- Handles decompression of zlib-compressed QR payloads
- Decodes base64 image data and reconstructs the original image
- Saves decoded images with phi-harmonic timestamps

### 3. Test System (`test_face_qr_system.py`)

Provides end-to-end testing of the workflow:

- Generates QR codes from sample face images
- Creates a test runner that applies the extension
- Processes QR codes to extract and save face images
- Validates the successful image reconstruction

## Phi-Harmonic Integration

The system incorporates phi-harmonic principles:

- Uses golden ratio (φ = 1.618...) for timestamp generation
- Embeds phi-resonance values in QR metadata
- Optimizes image dimensions based on phi-harmonic scaling

## Usage

### Encoding a Face Image to QR Code

```bash
python generate_face_qr.py --image <face_image_path> --output <qr_output_path> --size_px <size> --jpeg_quality <quality>
```

Parameters:
- `--image`: Path to the input face image (required)
- `--output`: Path to save the QR code (default: face_qr.png)
- `--size_px`: Size to resize the image to (default: 32)
- `--jpeg_quality`: JPEG quality for compression (default: 60)

### Running the Full Test Workflow

```bash
python test_face_qr_system.py --image <face_image_path> --size_px <size> --jpeg_quality <quality>
```

Parameters:
- `--image`: Path to the input face image (default: face.jpg)
- `--size_px`: Size to resize the image to (default: 32)
- `--jpeg_quality`: JPEG quality for compression (default: 60)

### Processing a QR Code Directly

```bash
python qr_task_worker_from_file.py -f <qr_code_path>
```

Note: Make sure to import and apply the extension before processing:

```python
import qr_task_worker_extension
qr_task_worker_extension.apply_extension()
```

## Optimization Tips

To ensure QR codes fit within version limits (≤ 40):

1. Reduce image dimensions (try 16x16, 24x24, or 32x32)
2. Lower JPEG quality (try 40-60%)
3. Use grayscale conversion
4. Enable zlib compression for large payloads

## Example Workflow

1. Take a facial image (e.g., face.jpg)
2. Generate a QR code with the face image embedded:
   ```bash
   python generate_face_qr.py --image face.jpg --size_px 24 --jpeg_quality 50
   ```
3. Process the QR code to extract and save the face image:
   ```bash
   python test_face_qr_system.py --image face.jpg --size_px 24 --jpeg_quality 50
   ```
4. View the decoded face image (saved as decoded_face_*.png)

## Technical Details

### QR Code Structure

The QR code contains a JSON payload with the following structure:

```json
{
  "task_data": {
    "task_id": "<uuid>",
    "task_type": "display_face_image",
    "timestamp": <phi_harmonic_timestamp>,
    "image_data_base64": "<base64_encoded_image>",
    "original_filename": "<filename>",
    "processed_size": "<width>x<height>",
    "image_format": "JPEG_Grayscale",
    "compression_quality": <quality>
  },
  "metadata": {
    "generator": "quantum_face_qr",
    "version": "1.0",
    "phi_resonance": <phi_resonance_value>
  }
}
```

For large payloads, the entire JSON is compressed using zlib and encoded as:

```
COMPRESSED:<base64_encoded_compressed_data>
```

### Extension Mechanism

The extension uses monkey patching to modify the behavior of the QR task worker:

1. The original `process_qr_image_file` function is preserved
2. A new function is defined that intercepts "display_face_image" tasks
3. The original function is called for all other task types
4. The extension is applied by calling `apply_extension()`

This approach follows the "lego" principle by adding functionality without modifying core files.

## Future Enhancements

- Add face detection to automatically crop and focus on faces
- Implement multiple compression algorithms with automatic selection
- Add encryption for secure face image transmission
- Integrate with quantum-based image processing for enhanced compression
- Develop a real-time face QR code scanner for mobile devices
