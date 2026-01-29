# Face QR Camera Evolution System Guide

## Overview

The Face QR Camera Evolution System integrates live camera capture, QR code generation, and phi-harmonic evolution in a seamless workflow. This system enables:

1. **Live face capture** via your camera
2. **QR code generation** from the captured face image
3. **Phi-harmonic evolution** of system parameters based on authentication results

This guide explains how to use the standalone implementation of this workflow.

## Requirements

- Python 3.6+
- OpenCV (cv2)
- qrcode
- numpy
- PIL (Pillow)

## How to Use

### Running the Workflow

1. Open your terminal
2. Navigate to the QuantumAI project directory
3. Run the standalone script:
   ```
   python standalone_camera_qr_evolution.py
   ```

### Using the Camera Interface

When the camera interface opens:

1. Position your face in the frame
   - A green box will appear around your face when detected
   - Make sure your face is clearly visible and well-lit

2. Press 'c' to capture your face and generate a QR code
   - A 3-second countdown will appear
   - Hold still during the capture
   - The system will automatically detect your face, extract it, and generate a QR code

3. Press 'q' at any time to quit without capturing

### Evolution Process

After successful QR code generation:

1. The system will automatically run the evolution process on the generated QR code
2. Evolution parameters will be updated based on authentication results
3. Results will be displayed showing:
   - Initial parameters
   - Updated parameters after evolution
   - Generation number
   - Similarity threshold
   - Feature weight
   - Temporal factor
   - Complexity
   - Resonance
   - Mutation rate

## File Outputs

The system generates two types of output files:

1. **QR Code Images**
   - Stored in the `qr_output` directory
   - Filename format: `face_qr_[timestamp]_[phi_time].png`
   - Contains encoded face image data

2. **Evolution Data**
   - Stored in the `evolution_data` directory
   - Filename format: `evolution_[timestamp]_[phi_time].json`
   - Contains evolution parameters and authentication results

## Phi-Harmonic Principles

The system uses phi-harmonic principles for:

- Timestamp generation (φ = 1.618034...)
- Parameter evolution based on golden ratio patterns
- Resonance calculations for optimal authentication

## Troubleshooting

If you encounter issues:

- **Camera not opening**: Ensure your camera is not in use by another application
- **Face not detected**: Improve lighting and ensure your face is clearly visible
- **QR generation fails**: Check console output for specific errors
- **Evolution process fails**: Verify QR code was successfully generated

## Advanced Usage

For advanced users, you can modify the evolution parameters in the script:

- `similarity_threshold`: Threshold for face matching (0.1-0.9)
- `feature_weight`: Weight given to facial features (0.1-0.9)
- `temporal_factor`: Importance of temporal patterns (0.1-0.9)
- `complexity`: Complexity of evolution patterns (0.5-2.0)
- `resonance`: Phi-harmonic resonance factor (0.1-0.9)
- `mutation_rate`: Rate of parameter change (0.01-0.2)

## Integration with Full Face-QR System

This standalone implementation demonstrates the core workflow. For full integration with the complete Face-QR system:

1. Ensure all Face-QR modules are properly installed
2. Use `face_qr_camera_evolution_extension.py` instead of the standalone script
3. Follow the same workflow steps as described above
