#!/usr/bin/env python3
"""
Complex Logic Error Test File
----------------------------
This file contains a function with multiple complex logic errors
to test the quantum meta-learning system's ability to detect and fix them.
"""

def phi_harmonic_quicksort(nums):
    """
    Sorts a list using a phi-harmonic quicksort algorithm.
    Should return the sorted list in ascending order.
    """
    if not nums or len(nums) <= 1:
        return nums
        
    # Error 1: Using incorrect pivot selection (should use phi-based pivot)
    pivot = nums[0]  # Should use phi-based pivot selection
    
    # Error 2: Incorrect partitioning logic (swapped comparison)
    left = [x for x in nums[1:] if x > pivot]  # Should be x < pivot
    right = [x for x in nums[1:] if x <= pivot]  # Should be x >= pivot
    
    # Error 3: Incorrect recursion order (should be left + [pivot] + right)
    return phi_harmonic_quicksort(right) + [pivot] + phi_harmonic_quicksort(left)

if __name__ == '__main__':
    test_data = [5, 3, 8, 1, 9, 2, 7, 4, 6]
    result = phi_harmonic_quicksort(test_data)
    print(f"Original: {test_data}")
    print(f"Sorted: {result}")
    print(f"Expected: {sorted(test_data)}")
    print(f"Correct: {result == sorted(test_data)}")
