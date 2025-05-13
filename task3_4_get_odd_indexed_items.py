def get_odd_indexed_items(items: list) -> list:
    """
    Print only items at odd indexes.
    Args:
        items (list): List of items
    Returns:
        list: Items at odd indexes
    """
    return [item for i, item in enumerate(items) if i % 2 != 0]
