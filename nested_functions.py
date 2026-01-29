"""
nested_functions.py
A collection of functions with nested function calls that don't have canonical contracts.
Used to test the recursive pattern detection in the phi-harmonic function inference system.
"""

def process_data(data):
    """Process data by applying multiple transformations in sequence."""
    if data is None:
        raise ValueError('data cannot be None')
    
    # First transformation - filter out negative values
    filtered = filter_positives(data)
    
    # Second transformation - square the values
    squared = square_values(filtered)
    
    # Third transformation - normalize the values
    normalized = normalize_values(squared)
    
    return normalized

def filter_positives(numbers):
    """Filter out negative values from a list."""
    if numbers is None:
        raise ValueError('numbers cannot be None')
    return [n for n in numbers if n > 0]

def square_values(numbers):
    """Square each value in a list."""
    if numbers is None:
        raise ValueError('numbers cannot be None')
    return [n * n for n in numbers]

def normalize_values(numbers):
    """Normalize values by dividing each by the maximum value."""
    if not numbers:
        return []
    max_value = max(numbers)
    if max_value == 0:
        return [0] * len(numbers)
    return [n / max_value for n in numbers]

def recursive_sum(n):
    """Calculate sum from 1 to n using recursion."""
    if n <= 0:
        return 0
    return n + recursive_sum(n - 1)

if __name__ == '__main__':
    test_data = [-2, 0, 3, 5, -1, 10]
    print('Processed Data:', process_data(test_data))
    print('Recursive Sum of 5:', recursive_sum(5))
