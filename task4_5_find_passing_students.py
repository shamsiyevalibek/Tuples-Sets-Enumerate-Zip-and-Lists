def find_passing_students(names: list, scores: list, passing_score: int = 60) -> list:
    """
    Find which students passed using names and scores.
    Args:
        names (list): List of student names
        scores (list): List of corresponding scores
        passing_score (int): Minimum score to pass, defaults to 60
    Returns:
        list: List of names of students who passed
    """
    return [name for name, score in zip(names, scores) if score >= passing_score]
