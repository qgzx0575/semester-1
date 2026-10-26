# Task 2

`geometry.py` contains implementations of the `Point` and `Circle` classes
from Session 1. `printobjects.py` is a program to use these classes.

Edit `printobjects.py` and add code to this file that

- Imports the classes from the `geometry` module
- Creates and prints a `Point` object
- Creates and prints a `Circle` object

Run the program so that you can see the default string representation for
instances of `Point` ane `Circle`.

Now edit `geometry.py` and add definitions of the `__str__()` method to
both the `Point` and `Circle` classes.

You can copy the example from the slides to implement the method in `Point`.
Your implementation of the method in `Circle` should include both the
position of the circle and its radius in the string it returns.

Run the program again, so that you can see how your implementations of
`__str__()` are used by the `print()` function.
