#!/usr/bin/env python3
"""
Test file with logic errors for MoA integration testing.
"""

def calculate_sum(numbers):
    """Calculate the sum of a list of numbers."""
    total = 0
    for i in range(len(numbers)):
        # Logic error: off-by-one error in the index
        total += numbers[i - 1]
    return total

def is_even(number):
    """Check if a number is even."""
    # Logic error: incorrect condition
    return number / 2 == 0

def find_max(numbers):
    """Find the maximum value in a list."""
    if not numbers:
        return None
    
    # Logic error: initialization with first element missing
    max_value = 0
    
    for num in numbers:
        if num > max_value:
            max_value = num
    
    return max_value

if __name__ == "__main__":
    test_numbers = [1, 2, 3, 4, 5]
    print(f"Sum: {calculate_sum(test_numbers)}")
    print(f"Is 4 even? {is_even(4)}")
    print(f"Max value: {find_max(test_numbers)}")
