#!/usr/bin/env python3
# Logic error test file

def increment(x):
    """Increment a number by 1."""
    # Logic error: returns x instead of x+1
    return x

def sum_even_numbers(numbers):
    """Sum all even numbers in a list."""
    total = 0
    for num in numbers:
        # Logic error: checks if num is odd instead of even
        if num % 2 == 1:
            total += num
    return total
