# QR Python Script Runner

## Concept Overview

This project demonstrates a system where a complete Python script is encoded into a QR code. A separate runner program can then scan this QR code, extract the Python script, and execute it directly.

This serves as a foundational step towards more complex QR-based computation, including encoding Turing-complete instruction sets or integrating phi-harmonic principles.

## Core Components

1.  **`qr_script_encoder.py`**: 
    *   Takes a Python script (e.g., `print('Hello, World!')`) as input.
    *   Encodes this script string into a QR code image.
    *   Saves the QR code (e.g., to `generated_hello_qr.png`).

2.  **`qr_script_runner.py`**:
    *   Loads a specified QR code image.
    *   Decodes the Python script string from the QR code.
    *   Executes the extracted Python script (e.g., using Python's `exec()` function or `subprocess` module).

## Usage

1.  **Generate QR Code**:
    ```bash
    python qr_script_encoder.py "print('Hello from QR Code!')" hello_world_qr.png
    ```

2.  **Run Script from QR Code**:
    ```bash
    python qr_script_runner.py hello_world_qr.png
    ```

## Dependencies

*   `qrcode` (for QR code generation)
*   `Pillow` (for image handling, often a dependency of qrcode and pyzbar)
*   `pyzbar` (for QR code decoding)

Install them using:
```bash
pip install qrcode Pillow pyzbar
```

## Future Enhancements (Connecting to Broader Vision)

*   **Instruction Set Encoding**: Instead of raw Python, encode a minimal instruction set (like Brainfuck or custom assembly) for a more abstract Turing machine.
*   **Multi-Layered QR Codes**: Implement the concept of using negative/empty space for instructions and positive/filled space for data.
*   **Phi-Harmonic Integration**: Apply the `FLAT_TO_REALITY.md` logic to transform the QR code's structure into a quantum signature, analyzing the program's "essence."
*   **Security Considerations**: Executing arbitrary code from a QR code is inherently risky. For real-world applications, sandboxing or a restricted interpreter would be crucial.

---
*Project idea by USER, documented by Cascade AI on 2025-05-19.*
