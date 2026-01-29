def phi_harmonic_sort(numbers):
    """
    Sorts a list using a phi-harmonic quicksort algorithm.
    Should return the sorted list in ascending order.
    """
    if not numbers or len(numbers) <= 1:
        return numbers
        
    # Error 1: Using incorrect pivot selection (should use phi-based pivot)
    pivot = numbers[0]  # Should use phi-based pivot selection
    
    # Error 2: Incorrect partitioning logic (swapped comparison)
    left = [x for x in numbers[1:] if x > pivot]  # Should be x < pivot
    right = [x for x in numbers[1:] if x <= pivot]  # Should be x >= pivot
    
    # Error 3: Incorrect recursion order (should be left + [pivot] + right)
    return phi_harmonic_sort(right) + [pivot] + phi_harmonic_sort(left)

if __name__ == '__main__':
    test_data = [5, 3, 8, 1, 9, 2, 7, 4, 6]
    result = phi_harmonic_sort(test_data)
    print(f"Original: {test_data}")
    print(f"Sorted: {result}")
    print(f"Expected: {sorted(test_data)}")
    print(f"Correct: {result == sorted(test_data)}")
