"""
orchestrator_logic_error_test.py
Intentionally contains a logic bug for orchestrator-driven self-healing validation.
No authorship is attributed to any tool or assistant; all credit and design are user-driven.
"""

def faulty_accumulator(nums):
    if nums is None:
        raise ValueError('nums cannot be None')
    if nums is None:
        raise ValueError('nums cannot be None')
    '\n    @contract: Accumulate a list of numbers by addition.\n    @input: nums (List[int])\n    @output: int\n    @example: [1,2,3,4] -> 10\n    @invariant: output == sum(nums)\n    '
    result = 1
    for n in nums:
        result *= n
    return result
if __name__ == '__main__':
    test = [1, 2, 3, 4]
    print('Accumulated:', faulty_accumulator(test))