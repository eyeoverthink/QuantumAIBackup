# Domino Logic System Observations

This document tracks observations and the evolving behavior of the QR task issuer and worker system implementing the 'Domino Logic'.

## System State Evolution

The system progresses through `DOMINO_STEP` values. Each step influences the `intensity_profile` (R,G,B,A-like values) of the generated task and a `visual_inversion` flag.

- **Issuer (`fraymus_qr_issuer.py`)**: Reads `next_task_params.json` (if it exists) to determine the current `DOMINO_STEP` and `visual_inversion`. It then calculates the task metadata, including the intensity profile and `is_target_89_hit` based on the current step. It generates a QR code embodying this state.
- **Worker (`qr_task_worker_from_file.py`)**: Reads the QR code, processes the task, and then calculates the *next* `DOMINO_STEP` (current step + 1) and toggles `visual_inversion`. It writes these new parameters to `next_task_params.json`.

## Key Metric: `is_target_89_hit`

A primary indicator of a specific 'resonant' state is when the `is_target_89_hit` flag becomes `True`. This occurs when:
`energy_value = current_domino_step + FIBONACCI_SEQUENCE[current_domino_step % len(FIBONACCI_SEQUENCE)]`
`is_target_89_hit = (energy_value % MODULO_BASE) == TARGET_FIB_VALUE_FOR_MODULO_CHECK`

Where:
- `FIBONACCI_SEQUENCE = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]` (len=16)
- `MODULO_BASE = 105`
- `TARGET_FIB_VALUE_FOR_MODULO_CHECK = 89`

When `is_target_89_hit` is `True`, the `g_priority_level` in the `intensity_profile` is set to 255.

## Observations Log

- **Initial Runs (Background)**: Successfully demonstrated the feedback loop. The issuer picked up `next_task_params.json` created by the worker, and `DOMINO_STEP` incremented correctly (e.g., 0 -> 1 -> 2 -> ... -> 5 observed).

- **User Log for DOMINO_STEP = 38 (2025-05-20T02:05:12-07:00)**:
  - `Energy Value (for 89 check): 46`
    - Calculation: `38 % 16 = 6`. `FIBONACCI_SEQUENCE[6] = 8`. `energy_value = 38 + 8 = 46`.
  - `Target 89 Hit: False`
    - Calculation: `46 % 105 = 46`. `46 != 89`.
  - `Calculated Intensity Profile: R=223, G=25, B=13, A=33`

- **User Manually Set `next_task_params.json` to `domino_step: 45` (2025-05-20T02:05:12-07:00)**
  - We will run the issuer to observe this state.
  - Prediction for `DOMINO_STEP = 45`:
    - `45 % 16 = 13`. `FIBONACCI_SEQUENCE[13] = 233`.
    - `energy_value = 45 + 233 = 278`.
    - `is_target_89_hit`: `278 % 105 = 68`. `68 != 89`. So, `is_target_89_hit` should be `False`.
    - The `intensity_profile` will be different from step 38.

- **Observed Output for DOMINO_STEP = 45 (Forced, Single Cycle Run - 2025-05-20T03:28:18-07:00)**:
  - `FORCED PARAMETERS: DOMINO_STEP=45, VISUAL_INVERSION=True`
  - `Energy Value (for 89 check): 278`
  - `Target 89 Hit: False`
  - `Calculated Intensity Profile: R=253, G=5, B=10, A=44`
  - `Task ID: 5312d6b5-db75-4227-a5c9-64a3c4721dd4`
