# Small example of using inheritance

import random


class Die:
    """
    A die used in gaming.
    """
    def __init__(self, sides):
        """
        Creates a Die object with the given number of sides.
        """
        if not isinstance(sides, int):
            raise TypeError("number of sides must be an integer")

        if sides <= 1:
            raise ValueError("invalid number of sides")

        self.sides = sides
        self.value = 1

    def __str__(self):
        """
        Returns a string representation of this die.
        """
        return f"d{self.sides}"

    def roll(self):
        """
        Rolls this die, saving and returning the result.
        """
        self.value = random.randint(1, self.sides)
        return self.value


class D6(Die):
    """
    A six-sided die.
    """
    def __init__(self):
        # Note the syntax for invoking superclass constructor!
        super().__init__(6)


class D20(Die):
    """
    A twenty-sided die.
    """
    def __init__(self):
        super().__init__(20)

    def is_critical_failure(self):
        return self.value == 1

    def is_critical_success(self):
        return self.value == 20


if __name__ == "__main__":
    die = D20()

    print(f"Rolling a {die}...")
    print(f"Rolled a {die.roll()}")

    if die.is_critical_success():
        print("Critical success! 😃")
    elif die.is_critical_failure():
        print("Critical failure! 😭")
