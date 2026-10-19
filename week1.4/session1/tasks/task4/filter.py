# Week 4, Session 1: 

# Your are given the function filter_positive_numbers with a docstring.
# Can you identify the inconsistency between the docstring and the implementation?

# Your task is to update the docstring to reflect what the function does.


def filter_positive_numbers(numbers):
    """
    Filters out positive numbers from the list, keeping only the negative ones.
    The function returns a list of all the positive numbers in the input.

    Args:
        numbers (list of int): A list of integers.

    Returns:
        list of int: A list containing only the positive integers.
    """
    return [num for num in numbers if int(num) > 0]

numbers = (input("Enter your list of numbers, seperated by spaces: ").strip().split())
print(numbers)
print(f"Here is a list of only positive numbers: {filter_positive_numbers(numbers)}")