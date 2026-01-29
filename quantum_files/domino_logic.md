# Domino Logic and Fibonacci Sequencing in QR Tasks

## Concept

The "Domino Logic" aims to integrate sequential, evolving characteristics into QR tasks, drawing inspiration from:
1.  **Domino Effect:** Tasks can be seen as part of a sequence, where the properties of a task are influenced by its position (step) in the sequence.
2.  **Fibonacci Sequence & Golden Ratio:** Numerical properties of tasks, particularly within their `intensity_profile`, will be derived using Fibonacci numbers and related mathematical principles (e.g., increments of 5, which is F5).
3.  **Specific Modulo Conditions:** Conditions like `(STEP * 5) % 105 == 89` (where 89 is F11) can trigger special states or parameter values, reflecting user-defined harmonic resonances.

## Implementation - Phase 1: Parameter Derivation

This initial phase focuses on modifying individual task generation based on a configurable `DOMINO_STEP`.

### In `fraymus_qr_issuer.py`:

1.  **`DOMINO_STEP` Variable:**
    *   A global variable (e.g., `DOMINO_STEP = 193`) will be defined. This can be manually changed to simulate different tasks in a sequence.

2.  **Fibonacci Sequence & Constants:**
    *   A predefined list of Fibonacci numbers: `FIBONACCI_SEQUENCE = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]`
    *   `MODULO_BASE = 105`
    *   `TARGET_FIB_VALUE_FOR_MODULO_CHECK = 89` (F11)
    *   `INCREMENT_FACTOR = 5` (F5) - Used for some intensity calculations, but not for `is_target_89_hit`.

3.  **`task_meta_data` Enhancement:**
    *   A new key, `domino_attributes`, will be added to `task_meta_data`.
    *   It will store:
        *   `step`: The current `DOMINO_STEP`.
        *   `is_target_89_hit`: Boolean, determined by a refined calculation (see below).
        *   `derived_fib_index`: The index used from `FIBONACCI_SEQUENCE`.
        *   `derived_fib_value`: The Fibonacci value obtained.

4.  **`intensity_profile` Derivation & `is_target_89_hit` Logic:**
    *   **`is_target_89_hit` Calculation (Refined Logic):**
        *   `current_fib_index_for_step = DOMINO_STEP % len(FIBONACCI_SEQUENCE)`
        *   `energy_value = DOMINO_STEP + FIBONACCI_SEQUENCE[current_fib_index_for_step]`
        *   `is_target_89_hit = (energy_value % MODULO_BASE) == TARGET_FIB_VALUE_FOR_MODULO_CHECK`
    *   This logic was successfully tested with `DOMINO_STEP = 193`, which resulted in `energy_value = 194` and `is_target_89_hit = True` (since `194 % 105 = 89`).
    *   Values for `r_computational_load`, `g_priority_level`, `b_data_volume_kb`, `a_execution_timeout_s` will be calculated based on `DOMINO_STEP`.
    *   Example for `g_priority_level`:
        *   If `is_target_89_hit` is `True`, set `g_priority_level` to `255` (max priority).
        *   Otherwise, derive from Fibonacci: `(FIBONACCI_SEQUENCE[(DOMINO_STEP + fib_len // 4) % len(FIBONACCI_SEQUENCE)] * INCREMENT_FACTOR) % 250` (scaled and kept below max).
    *   Example for `r_computational_load`:
        *   `((FIBONACCI_SEQUENCE[DOMINO_STEP % len(FIBONACCI_SEQUENCE)] + DOMINO_STEP * INCREMENT_FACTOR) % 230) + 25` (ensuring a base load and staying within 0-255).
    *   Similar logic for `b_data_volume_kb` and `a_execution_timeout_s` using different Fibonacci indices or scaling factors.

### In `worker_script` (embedded in `fraymus_qr_issuer.py`):

1.  **Parsing `domino_attributes`:**
    *   The worker script will extract `domino_attributes` from `task_meta_info`.
2.  **Displaying Domino Attributes:**
    *   Print the received `step`, `is_target_89_hit`, and other relevant domino-derived values.

## QR Code Payload Size Management

*   During development, it was observed that adding too much detail to `domino_attributes` (e.g., intermediate calculation values for debugging) could exceed the maximum QR code data capacity (version 40 limit).
*   The solution was to be selective about the data included in the QR payload, keeping `domino_attributes` lean (e.g., only `step` and `is_target_89_hit`). More detailed logging of intermediate calculations is performed by the issuer script on the console if needed, rather than being embedded in the QR code.

## Phase 2a: Worker Suggests Next Domino Step

To move towards dynamic task chaining, the first step involves the worker script suggesting parameters for the subsequent task.

### Mechanism:

1.  **Parameter Retrieval:** After completing its primary execution, the `worker_script` (embedded in `fraymus_qr_issuer.py`) retrieves the `domino_attributes` (specifically `step` and `is_target_89_hit`) and `visual_inversion` status from its own `task_meta_info`.

2.  **Next `DOMINO_STEP` Calculation:**
    *   A rule is applied to determine the `next_domino_step`:
        *   If `is_target_89_hit` for the current task was `True`, then `next_domino_step = current_step + 5` (representing a jump, using F5).
        *   Otherwise, `next_domino_step = current_step + 1` (standard increment).

3.  **Next `visual_inversion` Calculation:**
    *   The suggested `visual_inversion` for the next task is simply the opposite of the current task's `visual_inversion` (e.g., `not current_visual_inversion`).

4.  **Outputting Suggestions:**
    *   The worker script constructs a dictionary containing these suggestions (`suggested_next_domino_step`, `suggested_visual_inversion`, and context like `based_on_current_step`, `based_on_target_89_hit`).
    *   This dictionary is then printed to the console as a formatted JSON-like string, clearly labeled. This allows the user to easily copy the suggested `DOMINO_STEP` and `VISUAL_INVERSION` values and manually update them in the `fraymus_qr_issuer.py` script to generate the next QR code in the conceptual sequence.

This phase provides the data for task chaining without yet fully automating the QR generation loop, serving as an incremental step.

### Testing and Confirmation (Phase 2a):

Phase 2a was successfully tested through a manual two-step chain:

1.  **Initial State in `fraymus_qr_issuer.py`:**
    *   `DOMINO_STEP = 193`
    *   `VISUAL_INVERSION = False`
    *   **Issuer Output:** `Target 89 Hit: True` (due to step 193 triggering the condition).
    *   **Worker Output:** After processing the QR, suggested `NxtP:DS=198,VI=true,FS=193_H89=True`.
        *   This correctly calculated `next_domino_step = 193 + 5 = 198` and toggled `visual_inversion` to `true`.

2.  **Manually Updated State in `fraymus_qr_issuer.py` (based on worker suggestion):**
    *   `DOMINO_STEP = 198`
    *   `VISUAL_INVERSION = True`
    *   **Issuer Output:** `Target 89 Hit: False` (step 198 does not trigger the condition).
    *   **Worker Output:** After processing the QR, suggested `NxtP:DS=199,VI=false,FS=198_H89=False`.
        *   This correctly calculated `next_domino_step = 198 + 1 = 199` and toggled `visual_inversion` back to `false`.

This confirmed the logic for dynamic suggestion of the next step and visual inversion based on the current task's outcome is working as intended.

## Phase 2b: Issuer Accepts Next Step Parameters (from file)

**Objective:** To make the task chaining process smoother by allowing the `fraymus_qr_issuer.py` script to read the next `DOMINO_STEP` and `VISUAL_INVERSION` from an external configuration file, rather than requiring direct script modification.

**Proposed Mechanism:**

1.  **Configuration File:** A simple JSON file, e.g., `next_task_params.json`, will be used. It might look like:
    ```json
    {
      "domino_step": 199,
      "visual_inversion": false
    }
    ```

2.  **Issuer Script Modification (`fraymus_qr_issuer.py`):**
    *   On startup, the script will attempt to read `next_task_params.json`.
    *   If the file exists and contains valid `domino_step` and `visual_inversion` keys, these values will be used for the current task generation.
    *   If the file does not exist, or if the keys are missing/invalid, the issuer will fall back to default initial values (e.g., `DOMINO_STEP = 0`, `VISUAL_INVERSION = False`).
    *   After successfully using parameters from the file, the issuer could optionally delete or rename `next_task_params.json` to ensure that if it's run again without an updated file, it reverts to defaults, preventing accidental re-runs of the same non-default step. (This is an optional refinement).

3.  **Workflow:**
    *   User runs `fraymus_qr_issuer.py`. It uses defaults or reads `next_task_params.json`.
    *   User runs `qr_task_worker_from_file.py`. The worker processes the task and prints its "Next Task Suggestion" to the console (e.g., `NxtP:DS=200,VI=true,...`).
    *   User manually creates/updates `next_task_params.json` with the `domino_step` and `visual_inversion` values from the worker's console output.
    *   User runs `fraymus_qr_issuer.py` again. It now picks up the new parameters from the file.

**Benefits:**
*   Reduces the need to directly edit the Python source code for each step in the chain.
*   Makes the process less error-prone.
*   Serves as an intermediate step towards more automated chaining solutions.

### Testing and Confirmation (Phase 2b):

Phase 2b was successfully tested:

1.  **First Issuer Run (No `next_task_params.json`):
    *   The issuer correctly noted the absence of `next_task_params.json`.
    *   It defaulted to `DOMINO_STEP=0` and `VISUAL_INVERSION=False`.
    *   This resulted in `Target 89 Hit: False`.
    *   The worker processed this task and suggested `NxtP:DS=1,VI=true,FS=0_H89=False`.

2.  **Creation of `next_task_params.json`:**
    *   The file `next_task_params.json` was manually created with:
        ```json
        {
          "domino_step": 1,
          "visual_inversion": true
        }
        ```

3.  **Second Issuer Run (With `next_task_params.json`):
    *   The issuer correctly loaded `DOMINO_STEP=1` and `VISUAL_INVERSION=True` from the file.
    *   It renamed the parameter file to `next_task_params.json.used.<timestamp>`.
    *   This resulted in `Target 89 Hit: False`.
    *   The worker processed this task and suggested `NxtP:DS=2,VI=false,FS=1_H89=False`.

This confirmed that the issuer can successfully read parameters from the JSON file, use them for task generation, and manage the parameter file to prevent accidental reuse, thus streamlining the manual chaining process.

## Phase 3a: Worker Writes Parameters File

**Objective:** Modify the embedded worker script within `fraymus_qr_issuer.py` to parse its calculated next step parameters and write them into `next_task_params.json`. This file will then be consumed by a subsequent run of `fraymus_qr_issuer.py`.

**Implementation Details:**
*   The embedded worker script in `fraymus_qr_issuer.py` was modified to:
    *   Include `import os` and `import json`.
    *   After calculating `next_step_val` (as `nds`) and `next_visual_inversion_val` (as `nvi`), it forms a dictionary: `{"domino_step": nds, "visual_inversion": nvi}`.
    *   It attempts to write this dictionary to `next_task_params.json` in its current working directory.
    *   Print statements were added to confirm success (`W:POK:next_task_params.json`) or failure of this write operation.
    *   Print statements in the embedded script were shortened to reduce overall payload size and resolve a QR code version capacity error.

**Testing and Confirmation (Phase 3a - Manual Iteration):**

The functionality was tested through a sequence of manual runs:

1.  **Clean Slate:** Ensured no `next_task_params.json` or `*.used.*` files existed.
2.  **First Issuer Run:** `fraymus_qr_issuer.py` ran, used default parameters (`DOMINO_STEP=0`, `VISUAL_INVERSION=False`), and generated `fraymus_task_meta_qr.png`.
3.  **First Worker Run:** `qr_task_worker_from_file.py` processed the QR code. Its embedded script:
    *   Correctly suggested `NxtP:DS=1,VI=True`.
    *   Successfully wrote these parameters to `next_task_params.json` (confirmed by `W:POK:next_task_params.json` output and file inspection).
4.  **Second Issuer Run:** `fraymus_qr_issuer.py` ran again. It:
    *   Found and loaded parameters from `next_task_params.json` (`DOMINO_STEP=1`, `VISUAL_INVERSION=True`).
    *   Generated a new `fraymus_task_meta_qr.png` for step 1.
    *   Renamed `next_task_params.json` to `next_task_params.json.used.<timestamp>`.
5.  **Second Worker Run:** `qr_task_worker_from_file.py` processed the new QR code. Its embedded script:
    *   Correctly suggested `NxtP:DS=2,VI=False`.
    *   Successfully wrote these new parameters to a fresh `next_task_params.json` (confirmed by output and file inspection).

This successfully demonstrated that the worker can communicate the next task parameters to the issuer via the `next_task_params.json` file, enabling a manually iterated chain.

## Phase 3b: Looping Issuer

**Objective:** To make the `fraymus_qr_issuer.py` script run in a continuous loop, automatically generating new QR codes by consuming parameters from `next_task_params.json` if present, or using defaults otherwise.

**Implementation Details:**
*   The `main()` function in `fraymus_qr_issuer.py` was modified:
    *   The core logic (parameter loading, task definition, QR generation, params file renaming) was wrapped in a `while True:` loop.
    *   A `loop_count` variable was introduced to track cycles.
    *   Print statements were added to clearly indicate the start and end of each issuer cycle, and whether it loaded parameters from file or used defaults.
    *   `time.sleep(5)` was added at the end of each loop iteration to introduce a pause and allow time for the worker to potentially create/update `next_task_params.json`.
    *   The script `import time` was added.

**Testing and Confirmation (Phase 3b):**

The functionality was tested as follows:

1.  **Clean Slate:** Ensured no `next_task_params.json` or `*.used.*` files existed.
2.  **Start Looping Issuer:** The modified `fraymus_qr_issuer.py` was run. 
    *   Cycle 1: It used default parameters (`DOMINO_STEP=0`), generated `fraymus_task_meta_qr.png`, and waited.
3.  **First Manual Worker Run:** `qr_task_worker_from_file.py` was executed.
    *   It processed the QR for `DOMINO_STEP=0`.
    *   It created `next_task_params.json` with `{"domino_step": 1, "visual_inversion": true}`.
4.  **Observe Issuer's Next Cycle(s):** The looping issuer automatically:
    *   Detected and loaded the new `next_task_params.json` in its subsequent cycle (e.g., Cycle 2 or 3 depending on timing).
    *   Processed `DOMINO_STEP=1`, generated an updated `fraymus_task_meta_qr.png`.
    *   Renamed `next_task_params.json` to `*.used.*`.
5.  **Observe Issuer Reverting to Defaults:** In the cycle *after* processing `DOMINO_STEP=1`, with no new worker run in between, the issuer correctly found no `next_task_params.json` and reverted to default parameters (`DOMINO_STEP=0`), generating a new QR for Step 0.
6.  **Second Manual Worker Run:** `qr_task_worker_from_file.py` was run again against the current QR (which was for Step 0).
    *   It processed `DOMINO_STEP=0` and again created `next_task_params.json` with `{"domino_step": 1, "visual_inversion": true}`.
7.  **Observe Issuer Picking Up Params Again:** The looping issuer, in its subsequent cycle, again detected and loaded these new parameters, processed `DOMINO_STEP=1`, and generated the corresponding QR.

This sequence confirmed that the looping issuer successfully consumes parameters when available, manages the parameter file, and reverts to defaults otherwise, forming a semi-automated chain when the worker is run manually.

**Considerations from Implementation:**
*   The `display_qr_code()` function's attempt to open the image on each iteration can cause minor `[Errno 2] No such file or directory: 'open'` errors on systems where the `open` command isn't directly available or configured for image files this way. However, the QR image file `fraymus_task_meta_qr.png` is still correctly generated and saved, which is the critical part for the worker.

## Phase 3c: Looping Worker (Conceptual)

**Objective:** To make the `qr_task_worker_from_file.py` script run in a continuous loop, automatically monitoring the `fraymus_task_meta_qr.png` file. When the file is updated (or created), the worker should process it.

**Mechanism Ideas:**
1.  **File Modification Time Polling:**
    *   The worker, in a loop, periodically checks the last modification time of `fraymus_task_meta_qr.png`.
    *   If the modification time has changed since the last check, it processes the file.
    *   A `time.sleep()` interval would be needed in the loop.
2.  **File Deletion/Recreation Polling (More Robust?):**
    *   The issuer could be modified to *delete* `fraymus_task_meta_qr.png` just before generating a new one.
    *   The worker would loop, checking for the *existence* of the file. When it appears, the worker processes it and perhaps deletes it or renames it to signal completion (though this adds complexity if the issuer also expects to overwrite).
    *   This might avoid issues if modification times aren't updated reliably or quickly enough on some systems.
3.  **Using a File System Event Library (e.g., `watchdog`):**
    *   More advanced: Use a library like `watchdog` to get notified by the OS when the file is modified/created, rather than polling.
    *   This is more efficient but adds an external dependency.

**Initial Approach Suggestion for Simplicity:** Start with **File Modification Time Polling (Idea 1)** as it requires minimal changes to the existing structure and no new dependencies.

**Considerations:**
*   **Loop Control:** How to stop the looping worker (e.g., `Ctrl+C`).
*   **Initial State:** The worker needs to know the initial state of the QR file to avoid processing an old one immediately on startup, or process it once and then wait for changes.
*   **Error Handling:** What if the QR file is temporarily unreadable or malformed?
*   **Coordination with Issuer:** Ensuring the worker doesn't try to read the QR file while the issuer is in the middle of writing it (though this is less likely with image files than text files, as writes are often atomic or close to it for images).

## Future Phases (Ideas)
*   **Task Chaining:** A worker script, upon completion, could generate the payload or QR code for the *next* task in the domino sequence, potentially incrementing the `DOMINO_STEP`.
*   **Self-Improvement Loop:** The output or performance of a task at `DOMINO_STEP_N` could influence the generation parameters (including `DOMINO_STEP` itself or its modifiers) for `DOMINO_STEP_N+1`.
*   **Dynamic Fibonacci/Modulo Parameters:** The `modulo_base` (105) or `target_fib_value` (89) could themselves be dynamic or part of the evolving state.
