"""
logic_error_test_healed.py
Automatically healed using canonical logic_reference.py.
Original logic_error_test.py is preserved. This file is import-only and modular.
"""
def accumulator(nums):
    """
    @contract: Accumulate a list of numbers by addition.
    @input: nums (List[int])
    @output: int
    @example: [1,2,3,4] -> 10
    @invariant: output == sum(nums)
    """
    return sum(nums)

if __name__ == '__main__':
    test = [1, 2, 3, 4]
    print('Accumulated:', accumulator(test))
