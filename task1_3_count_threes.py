def count_threes(numbers: tuple) -> int:
    """
    Count how many times 3 appears in the tuple.
    Args:
        numbers (tuple): A tuple of integers
    Returns:
        int: The count of number 3 in the tuple
    """
    return numbers.count(3)
nums = (1, 3, 5, 3, 7, 3, 9)
print(count_threes(nums)) 
