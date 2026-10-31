# Example of a class with multiple dunder methods, also showing
# how classes can delegate work to underlying objects

class IntList:
    """
    A list of integers.
    """

    def __init__(self):
        """
        Creates an empty IntList.
        """
        self.data = []

    def __len__(self):
        """
        Returns number of integers in this list.
        """
        return len(self.data)

    def __str__(self):
        """
        Returns a string representation of the contents of this list.
        """
        return str(self.data)

    def __getitem__(self, index):
        """
        Returns the integer at the specified index.
        """
        return self.data[index]

    def __contains__(self, value):
        """
        Tests whether the specified integer is in this list.
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        return value in self.data

    def __iadd__(self, value):
        """
        Appends the given integer to the end of this list.
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        self.data.append(value)
        return self


if __name__ == "__main__":
    import random

    numbers = IntList()

    # Implementing __str__ allows print() to produce meaningful output
    print(f"numbers: {numbers}")

    # Implementing __len__ allows len() to give us size of the list
    print(f"size = {len(numbers)}")

    # Implementing __contains__ means we can use 'in' for membership tests
    print("1 in numbers?", 1 in numbers)

    for n in range(10):
        # Implementing __iadd__ means we can append using +=
        numbers += random.randint(1, 10)

    print(f"numbers: {numbers}")
    print(f"size = {len(numbers)}")
    print("1 in numbers?", 1 in numbers)

    # Implementing __getitem__ means we can index with []
    print(f"first number: {numbers[0]}")

    # Implementing __getitem__ also means our class supports for loops!
    for number in numbers:
        print(number)

    numbers += 2.5   # this fails, because 2.5 is not an int

    # This would also fail, as we've not implemented __setitem__
    numbers[0] = 2
