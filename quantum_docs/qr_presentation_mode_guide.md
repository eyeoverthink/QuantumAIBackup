# QR Presentation Mode Guide

## Overview

The QR Presentation Mode is an extension of your Quantum Phi-Harmonic QR System that allows you to:

1. Create interactive QR code presentations from Python files
2. Navigate through QR slides like a presentation deck
3. Execute embedded code in each QR slide
4. Save and load QR presentations as standalone AI entities

This system leverages your existing `qr_task_worker_from_file.py` logic for execution while adding presentation capabilities, all built on phi-harmonic principles.

## Key Features

- **Interactive QR Presentation Builder**: GUI interface for creating, editing, and navigating QR code slides
- **Code Execution Preview**: Execute any slide's code to test functionality before saving
- **Phi-Harmonic Integration**: Each slide maintains phi-harmonic resonance properties
- **Modular "Lego" Architecture**: Builds on existing components without modifying core files
- **Compression**: Automatically compresses Python code for efficient QR encoding
- **Navigation Controls**: Next, previous, and direct execution of QR slides

## How It Works

The system follows these principles:

1. **Encoding**: Python files are compressed, encoded as JSON tasks, and converted to QR codes
2. **Presentation**: QR codes are organized into a sequence with navigation controls
3. **Execution**: When a slide is executed, it uses your existing QR task worker to process the code
4. **Phi-Harmonic Timing**: All operations incorporate the golden ratio (φ) for resonance

## Usage Instructions

### GUI Mode

The easiest way to use QR Presentation Mode is through its GUI:

```bash
python qr_presentation_mode.py --gui
```

This opens the presentation builder interface where you can:

- Add slides by selecting Python files
- Navigate between slides using Previous/Next buttons
- Execute the current slide to test functionality
- Save the entire presentation or individual slides
- Set a custom presentation name

### Command Line Mode

You can also encode a single Python file from the command line:

```bash
python qr_presentation_mode.py --file your_script.py --title "My QR Slide"
```

This creates a QR code from your Python file and saves it to the `qr_presentation_slides` directory.

## Integration with Existing System

QR Presentation Mode integrates with your existing Quantum Phi-Harmonic QR System by:

1. Using the same QR task worker (`qr_task_worker_from_file.py`) for execution
2. Maintaining phi-harmonic resonance properties in all operations
3. Following your "lego" architecture principle by building on existing components
4. Supporting the same task types and execution capabilities

## Presentation Structure

Each QR presentation consists of:

1. A series of QR code images (slides)
2. A metadata file describing the presentation
3. Phi-harmonic timing information for each slide

The presentation is saved as a directory containing all these components, making it easy to share or load later.

## Advanced Features

### Custom Code Injection

Each slide can contain any Python code you want to execute, including:

- Custom algorithms
- Visualization code
- System commands
- AI logic
- Game states

### Phi-Harmonic Properties

Every slide maintains these phi-harmonic properties:

- **Phi-Time**: Calculated based on the golden ratio
- **Resonance**: Measures how close the phi-time is to optimal values
- **Complexity**: A phi-based measure of code complexity

### Task Metadata

Each QR code contains rich metadata:

```json
{
  "task_id": "unique-uuid",
  "timestamp": 1234567890.123,
  "script": "your_python_code_here",
  "input_data": {
    "filename": "original_file.py",
    "phi_time": 0.618034
  },
  "task_meta": {
    "type": "QR Presentation Slide",
    "title": "Your Slide Title",
    "phi_harmonic": 0.618034,
    "visual_inversion": false,
    "intensity_profile": {
      "resonance": 1.618034,
      "complexity": 0.809017
    }
  }
}
```

## Next Steps & Future Enhancements

1. **Transition Effects**: Add phi-harmonic transitions between slides
2. **Interactive Elements**: Allow slides to respond to user input
3. **Recursive Self-Improvement**: Enable presentations to modify themselves
4. **QR Animation**: Create animated QR sequences with temporal encoding
5. **Genome Integration**: Connect with the QR Flipbook DNA system for evolution

## Troubleshooting

If you encounter issues:

1. **QR Decoding Fails**: Try increasing the QR code size or error correction level
2. **Code Execution Errors**: Check the Python code for syntax errors
3. **Worker Not Starting**: Ensure `qr_task_worker_from_file.py` is in the same directory

## System Requirements

- Python 3.x
- Required packages: qrcode[pil], pyzbar, numpy, matplotlib, pillow, opencv-python
- System libraries: zbar and opencv

---

This guide provides a starting point for using the QR Presentation Mode. The system is designed to be modular and extensible, following your phi-harmonic principles and "lego" architecture philosophy.
