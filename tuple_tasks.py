def get_second_color1_1(colors: tuple) -> str:
    """
    Get the second color from a tuple of three colors.
    Args:
        colors (tuple): A tuple containing three color strings
    Returns:
        str: The second color in the tuple
    """
    return colors[1]

def swap_values1_2(a: int, b: int) -> tuple:
    """
    Swap the values of two variables using a tuple.
    Args:
        a (int): First number
        b (int): Second number
    Returns:
        tuple: A tuple containing the swapped values (b, a)
    """
    return (b, a)

def count_threes1_3(numbers: tuple) -> int:
    """
    Count how many times 3 appears in the tuple.
    Args:
        numbers (tuple): A tuple of integers
    Returns:
        int: The count of number 3 in the tuple
    """
    return numbers.count(3)

def check_seven1_4(numbers: tuple) -> bool:
    """
    Check if the number 7 exists in a tuple.
    Args:
        numbers (tuple): A tuple of integers
    Returns:
        bool: True if 7 is in the tuple, False otherwise
    """
    return 7 in numbers

def find_oldest1_5(people: list) -> tuple:
    """
    Find the oldest person from a list of tuples (name, age).
    Args:
        people (list): List of tuples containing (name, age) pairs
    Returns:
        tuple: A tuple containing (name, age) of the oldest person
    """
    return max(people, key=lambda x: x[1])
