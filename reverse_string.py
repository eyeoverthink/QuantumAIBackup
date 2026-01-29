def reverse_string(nums):
    if nums is None:
        raise ValueError('nums cannot be None')
    return s[::-1]
if __name__ == '__main__':
    test = 'hello'
    print('Healed output:', reverse_string(test))
if __name__ == '__main__':
    print('Reversed string:', reverse_string('QuantumAI'))