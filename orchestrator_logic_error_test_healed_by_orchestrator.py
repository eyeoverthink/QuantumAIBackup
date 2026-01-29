
def faulty_accumulator(nums):
    result = 0
    for n in nums:
        result += n
    return result

if __name__ == '__main__':
    test = [1, 2, 3, 4]
    print('Healed output:', faulty_accumulator(test))
