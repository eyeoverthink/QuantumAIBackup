"""
Phi-Harmonic Spoof Checker

Implements a heuristic defined by the user to classify numbers.
Rule: A number N is considered a "Phi-Harmonic Candidate" if N % 105 == 89.
Otherwise, it is considered a "Spoof by Heuristic".

This is a specific heuristic and not a standard mathematical primality test.
"""

DIVISOR = 105
EXPECTED_REMAINDER = 89

def check_number_heuristic(number):
    """
    Checks a number against the user-defined heuristic (N % 105 == 89).

    Args:
        number (int): The integer to check.

    Returns:
        dict: A dictionary containing the input number, divisor, remainder,
              a boolean indicating if it's a candidate, and its classification.
    """
    if not isinstance(number, int):
        return {
            "input_number": number,
            "error": "Input must be an integer.",
            "is_phi_harmonic_candidate": False,
            "classification": "Invalid Input"
        }

    remainder = number % DIVISOR
    is_candidate = (remainder == EXPECTED_REMAINDER)

    classification = "Phi-Harmonic Candidate" if is_candidate else "Considered Spoof by Heuristic"

    return {
        "input_number": number,
        "divisor": DIVISOR,
        "remainder": remainder,
        "is_phi_harmonic_candidate": is_candidate,
        "classification": classification
    }

if __name__ == "__main__":
    print("--- Phi-Harmonic Spoof Checker Demonstration ---")

    test_numbers = [
        89,       # Expected: Candidate (89 % 105 = 89)
        194,      # Expected: Candidate (194 % 105 = 89) - Note: 194 is 2*97 (composite)
        299,      # Expected: Candidate (299 % 105 = 89) - Note: 299 is 13*23 (composite)
        7,        # Expected: Spoof (7 % 105 = 7)
        105,      # Expected: Spoof (105 % 105 = 0)
        113,      # Expected: Spoof (113 % 105 = 8)
        199,      # Expected: Spoof (199 % 105 = 94) - Note: 199 is prime
        105089,   # Expected: Candidate (105089 % 105 = 89)
        105000,   # Expected: Spoof (105000 % 105 = 0)
        "text",   # Expected: Invalid Input
        None      # Expected: Invalid Input
    ]

    for num in test_numbers:
        result = check_number_heuristic(num)
        print(f"\nNumber: {num}")
        for key, value in result.items():
            print(f"  {key}: {value}")
    
    print("\n--- End of Demonstration ---")
