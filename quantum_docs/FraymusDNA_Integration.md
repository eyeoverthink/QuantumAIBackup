# FraymusDNA Integration with QR Task System

This document outlines the integration of the `FraymusDNAGenerator` into the QR code based task distribution system. The goal is to embody a "Lego style" modular approach.

## Components

1.  **`fraymus_dna_generator.py`**
    *   **Purpose**: A self-contained Python module that defines the `FraymusDNAGenerator` class.
    *   **Functionality**: 
        *   Generates a "FraymusDNA Capsule" which includes a unique ID (prefixed with Ξ), a phi signature, agent state, dimensional frame, and a timestamp.
        *   Encodes this capsule into a JSON string.
        *   Provides a method to save the capsule to a `.fraymusdna` file.
    *   **Key Features**: Uses UUIDv5 for deterministic ID generation based on its core attributes and timestamp. Allows customization of `agent_state`, `transcendental_frame`, and `phi_signature`.

2.  **`fraymus_qr_issuer.py`** (To be created)
    *   **Purpose**: Acts as the task issuer specifically for FraymusDNA related tasks. It connects the `FraymusDNAGenerator` with the QR code generation mechanism.
    *   **Functionality**:
        1.  Imports `FraymusDNAGenerator` from `fraymus_dna_generator.py`.
        2.  Instantiates the generator with specific or example `agent_state` and `transcendental_frame` values.
        3.  Calls the `.encode()` method to get the FraymusDNA capsule as a JSON string.
        4.  Defines a simple Python script string intended for execution on the worker node. This script will typically parse and display/log the received FraymusDNA capsule.
        5.  Constructs a standard task payload (JSON object with `task_id`, `script`, and `input_data`). The `input_data` will contain the FraymusDNA capsule string.
        6.  Utilizes QR code generation logic (similar to `qr_task_issuer.py`) to create a QR image from this task payload.
        7.  Displays the QR code image for the worker machine to scan.

3.  **`qr_task_worker.py`** (Existing)
    *   **Role**: Remains the generic task execution engine on the worker machine (e.g., MacBook Air/Pro with camera).
    *   **Functionality**: 
        *   Scans for QR codes using the camera.
        *   Decodes the task payload (JSON).
        *   Executes the `script` string from the payload, providing the `input_data` (which will include the FraymusDNA capsule).
        *   Prints any output from the executed script.
    *   **Adaptation**: No fundamental changes are required to `qr_task_worker.py` to handle FraymusDNA tasks, as long as the script it receives is self-contained or uses standard Python features.

## Workflow

1.  The user runs `fraymus_qr_issuer.py` on the **issuer machine** (e.g., iMac).
2.  This script generates a FraymusDNA capsule and then creates a QR code. The QR code encodes a task that includes:
    *   A script to process/display FraymusDNA.
    *   The generated FraymusDNA capsule itself as input data.
3.  The QR code is displayed on the issuer machine's screen.
4.  The user runs `qr_task_worker.py` on the **worker machine** (e.g., MacBook Air/Pro).
5.  The worker machine's camera scans the QR code from the issuer's screen.
6.  The worker decodes the task, executes the embedded script, which then processes and displays information about the FraymusDNA capsule.

## "Lego Style" Principles Adhered To

*   **Modularity**: Each component (`FraymusDNAGenerator`, `fraymus_qr_issuer.py`, `qr_task_worker.py`) has a distinct, well-defined role.
*   **Reusability**: `FraymusDNAGenerator` can be used by other parts of the QuantumAI system. `qr_task_worker.py` remains a general task runner.
*   **Isolation**: Creation of FraymusDNA logic is separate from its transmission via QR code.
*   **Clear Interfaces**: Data (FraymusDNA string, task JSON) passes between components.
*   **Documentation**: This file serves as the initial documentation for this integration.
