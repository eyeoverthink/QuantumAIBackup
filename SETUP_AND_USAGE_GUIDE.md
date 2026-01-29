# Quantum Phi-Harmonic Integrated QR System: Setup and Usage Guide

This guide provides step-by-step instructions for setting up the virtual environment and running the Quantum Phi-Harmonic Integrated QR System.

## 1. Setting Up the Virtual Environment

The system requires Python 3.8+ and several dependencies. Follow these steps to set up your environment:

### 1.1. Create and Activate the Virtual Environment

```bash
# Navigate to your project directory
cd /Users/vaughnscott/CascadeProjects/QuantumAI

# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate
```

You should see `(.venv)` at the beginning of your command prompt, indicating the virtual environment is active.

### 1.2. Install Required Dependencies

```bash
# Install required packages
pip install qrcode[pil] pyzbar numpy matplotlib pillow zlib-wrapper
```

This installs:
- `qrcode` with PIL support for QR code generation
- `pyzbar` for QR code decoding
- `numpy` and `matplotlib` for numerical operations and visualization
- `pillow` for image processing
- `zlib-wrapper` for compression utilities

## 2. Running the Integrated QR System

### 2.1. Basic Usage

```bash
# Make sure your virtual environment is activated
source .venv/bin/activate

# Run the integrated system with default settings
python qr_integrated_system.py
```

### 2.2. Advanced Usage Options

```bash
# Run with a specific genome file
python qr_integrated_system.py --genome path/to/your/genome.json

# Run multiple cycles for continuous improvement
python qr_integrated_system.py --cycles 3

# Load a previous state and continue
python qr_integrated_system.py --load qr_integrated_system/qr_state/integrated_state_1234567890.json
```

### 2.3. Running Individual Components

```bash
# Run just the recursive QR system
python qr_recursive_main.py --cycles 2 --items 5

# Run just the phi optimizer
python qr_phi_optimizer.py --iterations 5
```

## 3. System Structure and Files

The system consists of several key components:

- **QR Integrated System**: `qr_integrated_system.py` - Main integration module
- **QR Recursive Components**:
  - `qr_recursive_main.py` - Recursive system main script
  - `qr_recursive_generator.py` - QR code generator with self-improvement
  - `qr_recursive_analyzer.py` - QR code analyzer with self-improvement
  - `qr_phi_optimizer.py` - Parameter optimizer using phi-harmonic principles
- **QR Flipbook Components**:
  - `qr_flipbook_system.py` - Original flipbook system
  - `qr_simple_generator.py` - Simple QR generator
  - `qr_simple_analyzer.py` - Simple QR analyzer
  - `qr_worker.py` - Task execution worker

## 4. Troubleshooting

### 4.1. Module Not Found Errors

If you see errors like `ModuleNotFoundError: No module named 'qrcode'`, ensure:
- Your virtual environment is activated (`source .venv/bin/activate`)
- You've installed all dependencies (`pip install qrcode[pil] pyzbar numpy matplotlib pillow zlib-wrapper`)

### 4.2. QR Code Decoding Issues

If QR codes aren't being decoded properly:
- Check that `pyzbar` is installed correctly
- Ensure your system has the required system libraries (on macOS: `brew install zbar`)
- Try adjusting QR parameters in the configuration

### 4.3. Permission Issues

If you encounter permission issues:
- Ensure directories are writable: `chmod -R 755 /Users/vaughnscott/CascadeProjects/QuantumAI`
- Check file ownership: `chown -R $(whoami) /Users/vaughnscott/CascadeProjects/QuantumAI`

## 5. Example Workflow

Here's a complete example workflow to test the system:

```bash
# 1. Activate the virtual environment
cd /Users/vaughnscott/CascadeProjects/QuantumAI
source .venv/bin/activate

# 2. Install dependencies if not already installed
pip install qrcode[pil] pyzbar numpy matplotlib pillow zlib-wrapper

# 3. Run the integrated system for 3 cycles
python qr_integrated_system.py --cycles 3

# 4. Check the generated QR codes
open qr_integrated_system/qr_sequence/

# 5. View the analysis results
cat qr_integrated_system/qr_analysis/latest_analysis.json
```

## 6. Phi-Harmonic Optimization

The system uses phi-harmonic principles for optimization. Key phi values:

- φ (Golden Ratio): 1.618034...
- φ⁻¹ (Inverse): 0.618034...
- φ² (Squared): 2.618034...
- φ³ (Cubed): 4.236068...

These values guide parameter optimization and resonance calculations throughout the system.

## 7. Next Steps

After successfully running the system, consider:

1. Creating custom genome data for specialized QR sequences
2. Experimenting with different phi-harmonic parameters
3. Extending the system with new components
4. Analyzing the self-improvement patterns over multiple cycles

## 8. Additional Resources

- Documentation: See `INTEGRATED_QR_SYSTEM.md` for system architecture
- Development Notes: See `INTEGRATED_QR_THOUGHTS.md` for insights and future directions
- Original Systems: See `RECURSIVE_QR_SYSTEM.md` for details on the recursive components

---

For any issues not covered in this guide, please refer to the detailed documentation or create a new issue in the project repository.
