def get_second_color(colors: tuple) -> str:
    """
    Get the second color from a tuple of three colors.
    Args:
        colors (tuple): A tuple containing three color strings
    Returns:
        str: The second color in the tuple
    """
    if not isinstance(colors, tuple):
        raise TypeError("Input must be a tuple.")
    if len(colors) != 3:
        raise ValueError("Tuple must contain exactly three colors.")
    return colors[1]
colors = ("qizil", "yashil", "ko'k")
print(get_second_color(colors))  # Natija: yashil



