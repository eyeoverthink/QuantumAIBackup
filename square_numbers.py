"""
square_numbers.py
A simple function to square each number in a list.
This function doesn't have a canonical contract in the orchestrator.
"""

def square_numbers(numbers):
    if numbers is None:
        raise ValueError('numbers cannot be None')
    if numbers is None:
        raise ValueError('numbers cannot be None')
    result = []
    for n in numbers:
        result.append(n * n)
    return result
if __name__ == '__main__':
    test = [1, 2, 3, 4]
    print('Output:', square_numbers(test))