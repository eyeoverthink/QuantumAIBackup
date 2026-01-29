# Quantum Transcendental Counter QR Code Integration

## Overview

This document describes how the `quantum_transcendental_counter.py` script is integrated into the QR code tasking system. This allows triggering the transcendental counter by scanning a QR code, providing a novel way to initiate this specific computational display.

## Components

1.  **`quantum_transcendental_counter.py`**: 
    *   Contains the `QuantumTranscendentalCounter` class.
    *   The primary method used is `count_transcendental(duration)`, which runs a timed loop displaying increasing "levels of infinity" to the console.

2.  **`generate_transcendental_counter_qr.py`**: 
    *   A Python script to generate QR codes specifically for this task.
    *   Creates a JSON payload with `task_type: "run_transcendental_counter"`.
    *   Can optionally include a `duration` field in the payload to specify how long the counter should run.
    *   Saves the generated QR code as an image file (e.g., `transcendental_counter_task_qr.png`).

3.  **`qr_task_worker_from_file.py` (Modified)**:
    *   The main worker script that monitors for QR code image files.
    *   Updated to recognize and process `task_type: "run_transcendental_counter"`.
    *   When this task is detected:
        *   It imports `QuantumTranscendentalCounter`.
        *   It instantiates the counter.
        *   It calls the `count_transcendental` method, passing the `duration` from the QR payload (defaults to 10 seconds if not specified or invalid).
        *   The output of the transcendental counter (its console prints) will be displayed in the terminal where the `qr_task_worker_from_file.py` is running.

## QR Code Payload Structure

The QR code will contain a JSON string. For compatibility with the `fraymus_qr_module` structure (even if not strictly enforced for all tasks), it's good practice to nest the specific task data.

**Example Payload:**

```json
{
    "issuer_id": "generate_transcendental_counter_qr",
    "task_data": {
        "task_type": "run_transcendental_counter",
        "task_id": "<unique_uuid>",
        "timestamp": <unix_timestamp>,
        "duration": 15 
    }
}
```

-   `issuer_id`: Identifies the script that generated this QR code.
-   `task_data.task_type`: Must be `"run_transcendental_counter"`.
-   `task_data.task_id`: A unique identifier for this specific task instance.
-   `task_data.timestamp`: Time of QR code generation.
-   `task_data.duration` (Optional): An integer specifying the number of seconds the counter should run. If omitted, the worker script will use a default value (e.g., 10 seconds).

## How to Use

1.  **Generate the QR Code**:
    Run the `generate_transcendental_counter_qr.py` script. You can optionally specify a duration:
    ```bash
    python generate_transcendental_counter_qr.py --duration 20 --output my_counter_qr.png
    ```
    This will create `my_counter_qr.png` (or the default `transcendental_counter_task_qr.png`).

2.  **Run the QR Task Worker**:
    Start the `qr_task_worker_from_file.py` script, pointing it to the generated QR image file:
    ```bash
    python qr_task_worker_from_file.py --file my_counter_qr.png 
    ```
    (Adjust command based on your virtual environment activation if needed, e.g., `source .venv/bin/activate && python ...`)

3.  **Observe**: 
    The worker will detect the QR code, parse the task, and then the console output from the `QuantumTranscendentalCounter` will begin, running for the specified (or default) duration.

## Benefits of QR Integration

-   **Modular Triggering**: Allows the transcendental counter to be initiated as a distinct task within a larger system.
-   **Dynamic Configuration (Duration)**: The runtime duration can be set via the QR code itself.
-   **Decoupling**: The counter logic remains in its own file, and the worker acts as an orchestrator.
-   **Extensibility**: Fits into the pattern of QR-code-driven tasks, which can be expanded with more computational modules.
