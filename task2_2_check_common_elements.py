def check_common_elements(set1: set, set2: set) -> bool:
    """
    Check if two sets have any common elements.
    Args:
        set1 (set): First set of numbers
        set2 (set): Second set of numbers
    Returns:
        bool: True if sets have common elements, False otherwise
    """
    return bool(set1.intersection(set2))
