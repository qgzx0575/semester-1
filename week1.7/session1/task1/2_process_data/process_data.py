# from Week 4, Session 1: Task 4


def process_data(data):
    """
    Processes a list of integers and returns the sum of all values.
    If the list is empty, it returns None.

    Args:
        data (list of int): The list of integers to process.

    Returns:
        int: The sum of all integers in the list or None if empty.
    """
    if not data:
        return None

    return sum(data)
