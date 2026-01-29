def multiply_list(numbers):
    if numbers is None:
        raise ValueError('numbers cannot be None')
    result = 0
    for n in numbers:
        result += n
    return result
if __name__ == '__main__':
    test_list = [2, 3, 4]
    print('Result:', multiply_list(test_list))