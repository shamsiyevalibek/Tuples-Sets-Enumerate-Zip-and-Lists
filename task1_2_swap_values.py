def swap_values(a: int, b: int) -> tuple:
    """
    Swap the values of two variables using a tuple.
    Args:
        a (int): First number
        b (int): Second number
    Returns:
        tuple: A tuple containing the swapped values (b, a)
    """
    return (b, a)
x = 5
y = 10

swapped = swap_values(x, y)
print(swapped)
