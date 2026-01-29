# QR Code to Shell Script Execution System

This document outlines a system where a QR code can trigger the creation and execution of a shell script. The shell script, in this example, creates a text file containing "Hello World" and a timestamp.

## Components

1.  **`generate_sh_execution_qr.py`**: 
    *   A Python script that defines a simple shell script.
    *   Packages this shell script content into a JSON payload with `task_type: "execute_sh"`.
    *   Generates a QR code image (default: `sh_executor_task.png`) from this payload.

2.  **`qr_task_worker_from_file.py` (Modified)**:
    *   The existing worker script is augmented to handle the new `task_type: "execute_sh"`.
    *   When such a task is decoded from a monitored QR image:
        *   It extracts the shell script content.
        *   Writes it to a temporary file (`temp_generated_script.sh`) in the current working directory.
        *   Makes the script executable (`chmod +x`).
        *   Executes the script.
        *   The executed shell script then creates its output file (e.g., `hello_output_YYYY-MM-DD_HH-MM-SS.txt`).

## How to Use

1.  **Generate the QR Code**:
    ```bash
    python generate_sh_execution_qr.py
    ```
    This will create `sh_executor_task.png` (or the specified filename).

2.  **Run the Worker**:
    Ensure `qr_task_worker_from_file.py` has been updated with the new task handler.
    ```bash
    python qr_task_worker_from_file.py --file sh_executor_task.png
    ```
    The worker will monitor `sh_executor_task.png`. If it's the first time or the file changes (and contains the correct task type), it will execute the embedded shell script.

3.  **Observe Output**:
    *   The worker's console output will show logs related to processing the task and executing the script.
    *   A new text file (e.g., `hello_output_2025-05-20_22-33-00.txt`) will appear in the directory where the worker was run, containing "Hello World" and the timestamp.
    *   A temporary `temp_generated_script.sh` will also be created and executed (and could be optionally deleted by the worker after execution).

## Purpose

This system demonstrates a more flexible capability of the QR tasking framework, allowing for arbitrary shell command execution based on QR code content. This opens up possibilities for more complex automation and interaction initiated by QR codes.

## Security Enhancements

### 🛡️ Cryptographic Verification

To prevent malicious code injection and ensure authenticity:

* **Digital Signatures**:
  * Sign payloads with an RSA or ECDSA private key
  * Verify signatures in the worker before execution
  * Implementation example:
    ```python
    # In generator:
    payload_bytes = json.dumps(payload).encode('utf-8')
    signature = private_key.sign(payload_bytes, padding.PSS(...), hashes.SHA256())
    payload['signature'] = base64.b64encode(signature).decode('utf-8')
    
    # In worker:
    signature = base64.b64decode(payload.pop('signature'))
    public_key.verify(signature, json.dumps(payload).encode('utf-8'), ...)
    ```

### 🗓️ Time-Based Controls

* **Expiration Timestamps**:
  * Add validity period to prevent replay attacks
  * Example payload addition:
    ```json
    {
      "task_type": "execute_sh",
      "script_content": "#!/bin/bash\n...",
      "valid_until": "2025-06-27T12:00:00Z",
      "used": false
    }
    ```
  * Worker should check current time against expiration before execution
  * Worker invalidates expired or already-used QR tasks by marking the image file
  * Implement a local SQLite database to track task execution history

### 🔐 Encryption

* **Payload Encryption**:
  * Encrypt the entire payload with the worker's public key
  * Implementation using Fernet symmetric encryption:
    ```python
    # In generator:
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()  # Store securely and share with worker
    f = Fernet(key)
    encrypted_payload = f.encrypt(json.dumps(payload).encode('utf-8'))
    
    # In worker:
    decrypted_payload = f.decrypt(encrypted_payload).decode('utf-8')
    task_data = json.loads(decrypted_payload)
    ```
  * This prevents bystanders from extracting sensitive information by scanning the QR code

### 📦 Multi-Script Execution

* **Multiple Script Chunks**:
  * Support combining different script types in a single QR task
  * Example payload structure:
    ```json
    {
      "task_type": "multi",
      "steps": [
        {"type": "shell", "content": "echo Start"},
        {"type": "python", "content": "print('Step 2')"},
        {"type": "shell", "content": "echo Done"}
      ]
    }
    ```
  * Worker executes each step in sequence with appropriate interpreter
  * Enables more complex workflows in a single QR task
