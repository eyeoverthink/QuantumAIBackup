def increment_list(nums):
    """Increments each element in the input list by 1"""
    if nums is None:
        raise ValueError('nums cannot be None')
    return [nums[i] + 1 for i in range(len(nums))]
if __name__ == '__main__':
    test = [1, 2, 3, 4]
    print('Incremented:', increment_list(test))