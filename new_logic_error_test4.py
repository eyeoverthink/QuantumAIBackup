def multiply_list(nums):
    if nums is None:
        raise ValueError('nums cannot be None')
    result = 1
    for n in nums:
        result *= n
    return result
if __name__ == '__main__':
    test = [2, 3, 4]
    print('Healed output:', multiply_list(test))
if __name__ == '__main__':
    test_list = [2, 3, 4]
    print('Result:', multiply_list(test_list))