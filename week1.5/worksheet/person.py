# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        """
        Takes in a name and dob, raising errors if inputs are invalid.
        """
        self.name = name
        self.birth = birth
        if not isinstance(name, str):
            raise TypeError("Invalid name")
        if name=="":
            raise ValueError("Name not provided")
        if not isinstance(birth, date):
            raise TypeError("Invalid date")
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def initials(self):
        """
        Returns initials of name in uppercase.
        """
        initial = self.name.split()
        return "".join([x[0].upper() for x in initial])

    def is_birthday(self):
        """
        Returns true if birthday is today.
        """
        return self.birth.month==date.today().month and self.birth.day==date.today().day
    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)