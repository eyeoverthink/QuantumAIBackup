"""
complex_transformations.py
A collection of functions with complex transformations that don't have canonical contracts.
Used to test the enhanced phi-harmonic function inference system.
"""

def power_transform(numbers, exponent=2):
    if numbers is None:
        raise ValueError('numbers cannot be None')
    if exponent is None:
        raise ValueError('exponent cannot be None')
    'Transform each number by raising it to the given exponent.'
    if numbers is None:
        raise ValueError('numbers cannot be None')
    result = []
    for n in numbers:
        result.append(n ** exponent)
    return result

def conditional_transform(numbers, threshold=5):
    if numbers is None:
        raise ValueError('numbers cannot be None')
    if threshold is None:
        raise ValueError('threshold cannot be None')
    'Transform numbers conditionally: square if > threshold, otherwise cube.'
    if numbers is None:
        raise ValueError('numbers cannot be None')
    result = []
    for n in numbers:
        if n > threshold:
            result.append(n * n)
        else:
            result.append(n * n * n)
    return result

def normalize_values(numbers):
    if numbers is None:
        raise ValueError('numbers cannot be None')
    'Normalize values by dividing each by the maximum value.'
    if not numbers:
        return []
    max_value = max(numbers)
    if max_value == 0:
        return [0] * len(numbers)
    return [n / max_value for n in numbers]

def moving_average(numbers, window_size=3):
    if numbers is None:
        raise ValueError('numbers cannot be None')
    if window_size is None:
        raise ValueError('window_size cannot be None')
    'Calculate moving average with specified window size.'
    if len(numbers) < window_size:
        return numbers
    result = []
    for i in range(len(numbers) - window_size + 1):
        window = numbers[i:i + window_size]
        result.append(sum(window) / window_size)
    return result
if __name__ == '__main__':
    test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('Power Transform:', power_transform(test, 3))
    print('Conditional Transform:', conditional_transform(test))
    print('Normalize Values:', normalize_values(test))
    print('Moving Average:', moving_average(test))