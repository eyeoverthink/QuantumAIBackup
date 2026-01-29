
def multiply_list(nums):
    result = 1
    for n in nums:
        result *= n
    return result

if __name__ == '__main__':
    test = [2, 3, 4]
    print('Healed output:', multiply_list(test))
