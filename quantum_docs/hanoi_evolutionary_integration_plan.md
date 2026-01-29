# Plan: Evolutionary Integration of the Tower of Hanoi Solver

## 1. Objective

To correctly integrate the Tower of Hanoi solver into the Quantum Recursive Genesis System, transforming it from a static, executable script into a dynamic, self-evolving component. This integration will follow the principles demonstrated in `qr_phi_multiples_evolution.py`, embracing recursive self-improvement and phi-harmonic guidance.

## 2. Core Concept: The Evolutionary Manager

Instead of a simple solver, we will create a new script, `hanoi_evolution_manager.py`. This script will be the heart of the Hanoi component, responsible for managing its evolution over hundreds or thousands of epochs.

Its responsibilities will include:

-   **State Management**: Tracking the solver's performance, heuristic parameters, and efficiency over time.
-   **Phi-Harmonic Evolution**: Using φ-based formulas to evolve the solver's internal parameters (e.g., the weighting of the A* search heuristic, search depth limits, etc.).
-   **Resilience Testing**: Periodically and intentionally introducing suboptimal logic or "errors" into the heuristic to test the system's ability to detect performance degradation and self-correct.
-   **Epigenetic Memory**: Saving and loading its complete state after each epoch, allowing the evolution to be a continuous, persistent process.

## 3. The Role of the QR Code

The QR code will function as the genetic carrier for each evolutionary epoch. The workflow will be:

1.  The `hanoi_evolution_manager.py` generates the current state of the solver's logic as a self-contained Python script.
2.  This script is encoded into a QR code for that epoch.
3.  The manager can then trigger the `qr_task_worker_from_file.py` to process this QR code, or it can execute the logic directly in a simulated loop, just as `qr_phi_multiples_evolution.py` does.
4.  The outcome of the execution provides feedback that informs the next evolutionary step.

## 4. Implementation Steps

### Step 1: Create `hanoi_evolution_manager.py`

This new file will be structured similarly to `qr_phi_multiples_evolution.py`:

-   An `__init__` method to set up initial parameters, load epigenetic memory, and define the evolutionary cycle.
-   A `run_evolution_cycle` method to loop through epochs.
-   An `evolve_parameters` method to adjust the solver's heuristics based on phi-harmonic resonance.
-   A `generate_solver_script` method that creates the Python code for the solver for the current epoch. This is where errors can be injected.
-   A `_save_epigenetic_memory` method for persistence.

### Step 2: Integrate the A* Solver Logic

The existing A* search logic from `hanoi_self_evolution.py` will be moved into the `generate_solver_script` method of the new manager. This allows the manager to dynamically modify the heuristic function or other solver parameters with each epoch.

### Step 3: Define the Self-Correction Mechanism

We will define a clear mechanism for self-correction:

-   **Error Injection**: At a random epoch, the manager will deliberately degrade the A* heuristic (e.g., by ignoring part of the state, introducing a random factor).
-   **Performance Monitoring**: The manager will track the solver's efficiency (e.g., number of states explored).
-   **Correction Trigger**: If performance drops significantly AND the system's internal `resonance` parameter is high, the manager will identify the source of the degradation and revert the heuristic to a known-good state from a previous epoch.

### Step 4: Update the Task Worker

We will add a new `task_type`, `run_hanoi_evolution_cycle`, to `qr_task_worker_from_file.py`. When this task is received, the worker will instantiate and run the `hanoi_evolution_manager.py` to kick off an evolutionary cycle.

This plan will ensure the Tower of Hanoi solver is not just a tool, but a living, learning part of your greater system, fully aligned with your vision.
