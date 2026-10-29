# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        if not isinstance(name, str):
            raise TypeError("Invalid name")
        if name=="":
            raise ValueError("Name not provided")
        if not isinstance(dob, date):
            raise TypeError("Invalid date")
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def initials(self):
        initial = self.name.split()
        return "".join([x[0].upper() for x in initial])

    def is_birthday(self):
        return self.dob.month==date.today().month and self.dob.day==date.today().day
    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)