# Phi-Harmonic Spoof Checker

## Overview

This module, `phi_harmonic_spoof_checker.py`, implements a specific numerical heuristic defined by the user. The purpose is to classify numbers as either a "Phi-Harmonic Candidate" or "Considered Spoof by Heuristic" based on a simple arithmetic rule.

This checker is designed to follow a particular "shortcut" or "cheat code" logic provided by the user and is not intended to be a mathematically rigorous or standard primality test. It's an exploration of a defined computational strategy.

## The Heuristic

The core logic of the heuristic is as follows:

1.  Take an input number, `N`.
2.  Divide `N` by `105`.
3.  If the remainder of this division is exactly `89`, then the number `N` is classified as a **"Phi-Harmonic Candidate"** according to this heuristic.
4.  If the remainder is anything other than `89`, the number `N` is classified as **"Considered Spoof by Heuristic"**.

## Implementation Details

### `phi_harmonic_spoof_checker.py`

-   **Constants**:
    -   `DIVISOR = 105`: The number used for the modulo operation.
    -   `EXPECTED_REMAINDER = 89`: The specific remainder that qualifies a number as a candidate.

-   **Function: `check_number_heuristic(number)`**
    -   **Input**: `number` (integer). Handles non-integer inputs by returning an error status.
    -   **Process**: Calculates `remainder = number % DIVISOR`.
    -   **Output**: A dictionary containing:
        -   `input_number`: The original number provided.
        -   `divisor`: The constant divisor used (105).
        -   `remainder`: The result of `number % 105`.
        -   `is_phi_harmonic_candidate`: A boolean (`True` if remainder is 89, `False` otherwise).
        -   `classification`: A string, either "Phi-Harmonic Candidate" or "Considered Spoof by Heuristic" (or "Invalid Input").

-   **Demonstration (`if __name__ == "__main__":`)**
    -   The script includes a main block that runs a series of test numbers through the `check_number_heuristic` function and prints the detailed results. This allows for easy verification of the logic.
    -   The test cases include numbers that should be candidates, numbers that should be spoofs, and examples of invalid input.

## How to Use

1.  Run the script directly from the terminal:
    ```bash
    python phi_harmonic_spoof_checker.py
    ```
    This will execute the demonstration block and show results for predefined test numbers.

2.  Import and use the function in other Python scripts:
    ```python
    from phi_harmonic_spoof_checker import check_number_heuristic

    my_number = 194
    result = check_number_heuristic(my_number)
    print(result)
    # Output: {'input_number': 194, 'divisor': 105, 'remainder': 89, 'is_phi_harmonic_candidate': True, 'classification': 'Phi-Harmonic Candidate'}

    if result['is_phi_harmonic_candidate']:
        print(f"{my_number} is a Phi-Harmonic Candidate by this heuristic.")
    else:
        print(f"{my_number} is considered a spoof by this heuristic ({result['classification']}).")
    ```

## Relation to Larger Computational Strategies

This module serves as a foundational piece demonstrating the implementation of a user-defined computational heuristic. Future work could involve:

-   Integrating this checker into a larger system managed by QR codes (e.g., a QR code provides a number, and the system uses this checker to classify it).
-   Comparing the results of this heuristic against actual primality tests for analysis.
-   Exploring how this rule might interact with other phi-harmonic principles or quantum-inspired processing logic.
