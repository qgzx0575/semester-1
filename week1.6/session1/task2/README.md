# Task 2

Examine the code in `point.py`. This module contains the same `Point` class
as Task 1, but with the `__eq__()` method overridden.

In the terminal window, run the Python interpreter by entering `python`.

Import the `Point` class with

    from point import Point

Create two `Point` objects, `p` and `q`, with these commands:

    p = Point(1, 2)
    q = Point(1, 2)

Now test them for equality, with

    p == q

You should see a result of `True` displayed. This time, the comparison tests
for equality of state rather than equality of identity.

Finally, exit the interpreter by pressing `Ctrl+D`.
