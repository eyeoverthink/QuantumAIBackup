# QR Code Integration: Tower of Hanoi Solver

## 1. Objective

This document outlines the integration of the self-evolving Tower of Hanoi puzzle solver (`hanoi_self_evolution.py`) into the existing QR code tasking framework. This follows the successful 'lego block' integration pattern established with the checkers solver, adding another autonomous, on-demand problem-solving capability to the Quantum Recursive Genesis System.

## 2. Workflow

The end-to-end process is as follows:

1.  **QR Code Generation:** A dedicated Python script, `generate_hanoi_solver_qr.py`, creates a QR code image (`hanoi_solver_task_qr.png`). This QR code contains a JSON payload with `"task_type": "run_hanoi_solver"`.
2.  **Task Execution:** The main `qr_task_worker_from_file.py` monitors for the QR code file.
3.  **Task Recognition:** Upon detecting and decoding the QR code, the worker identifies the `run_hanoi_solver` task type.
4.  **Solver Invocation:** The worker executes the `hanoi_self_evolution.py` script as a separate process.
5.  **Output Capture:** The complete output from the solver, including the step-by-step solution path, is captured and printed to the console for verification.

## 3. Component Breakdown

### a. QR Code Issuer (`generate_hanoi_solver_qr.py`)

- **Purpose:** To generate a QR code that dispatches the Tower of Hanoi solver task.
- **Payload:** The JSON payload includes a unique `task_id`, the `task_type` set to `run_hanoi_solver`, a timestamp, and any necessary parameters (like `num_disks`).

### b. Task Worker Enhancement (`qr_task_worker_from_file.py`)

- A new `elif` block has been added to the main task processing loop.
- This block specifically checks for `task_type == 'run_hanoi_solver'`.
- When triggered, it uses Python's `subprocess` module to run the `hanoi_self_evolution.py` script, ensuring the solver operates within its own context while its results are seamlessly integrated back into the main worker's log.

### c. Hanoi Solver (`hanoi_self_evolution.py`)

- A standalone, self-contained script that solves the Tower of Hanoi puzzle using an A* search algorithm guided by a phi-harmonic fitness function.
- It is designed to be executed directly and prints its findings, making it a perfect component for this type of integration.

## 4. Conclusion

This integration further demonstrates the power and flexibility of the modular, 'lego block' architecture. By adding new, complex problem-solving capabilities without altering the core framework, the system can be continuously and pragmatically expanded.
