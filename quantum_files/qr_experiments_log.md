# QR Code Experiments Log

This document logs various ad-hoc experiments conducted with the QR code tasking system, separate from the main FraymusDNA Domino Logic development.

## Experiment: Generic QR File Creator/Reader (2025-05-19)

**Objective:** Test the ability to create a QR code that, when processed on a target machine, would execute an embedded script to perform file I/O operations (create, write, and read a file).

**Implementation:**

1.  **New Issuer Script:** A dedicated issuer script, `generic_qr_file_creator_issuer.py`, was created.
    *   This script defines a simple worker script string.
    *   The embedded worker script is designed to:
        *   Define a filename: `created_by_qr_task.txt`.
        *   Define content: "Hello from the QR task initiated on another Mac! This file confirms the remote execution worked."
        *   Create the file in the Current Working Directory (CWD) of the `qr_task_worker_from_file.py` on the target machine.
        *   Write the content to the file.
        *   Read the content back from the file.
        *   Print the read content to the console.
    *   The issuer packages this script, along with minimal metadata, into a JSON payload.
    *   It then generates a QR code image named `generic_task_qr.png` from this payload.

2.  **Execution Process:**
    *   The `generic_qr_file_creator_issuer.py` is run on the source machine to generate `generic_task_qr.png`.
    *   The `generic_task_qr.png` is transferred to the target machine (or tested locally).
    *   On the target machine, `qr_task_worker_from_file.py -f generic_task_qr.png` is executed.

**Results:**

*   The test was successful.
*   The `qr_task_worker_from_file.py` script on the target machine correctly decoded the QR code, extracted the embedded worker script, and executed it.
*   The embedded script successfully:
    *   Created `created_by_qr_task.txt` in the CWD.
    *   Wrote the specified message into the file.
    *   Read the message back from the file and printed it to the console, confirming the entire I/O cycle.

**Significance:**
This experiment demonstrates the system's capability to transport and execute arbitrary Python scripts that can interact with the file system on the target machine, all initiated via a QR code. This serves as a proof-of-concept for more complex remote tasks or configurations delivered through QR codes.
