def find_oldest(people: list) -> tuple:
    """
    Find the oldest person from a list of tuples (name, age).
    Args:
        people (list): List of tuples containing (name, age) pairs
    Returns:
        tuple: A tuple containing (name, age) of the oldest person
    """
    if not people:
        raise ValueError("The list of people cannot be empty.")
    return max(people, key=lambda person: person[1])
people = [("Ali", 25), ("Vali", 30), ("Gulnora", 28)]
print(find_oldest(people))