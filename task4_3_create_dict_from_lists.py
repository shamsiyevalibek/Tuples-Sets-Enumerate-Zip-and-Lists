def create_dict_from_lists(keys: list, values: list) -> dict:
    """
    Create a dictionary from two lists.
    Args:
        keys (list): List of keys for the dictionary
        values (list): List of values for the dictionary
    Returns:
        dict: Dictionary created from the two lists
    """
    return dict(zip(keys, values))
