# Task 3

## `Circle` Class

Study the implementations of the `Point` class in `point.py`, and the
`Shape` class in `shapes.py`.

Add to `shapes.py` a new definition, for a class `Circle`. This class
should inherit from `Shape`. Its constructor should have parameters to
represent radius, position and colour. The latter should have a default
value of `"red"`.

Give your `Circle` class a `set_radius()` method that initializes a field
named `radius`, using the supplied value. Call this method from within
the constructor. The method should check that the supplied value is a number
(`int` or `float`), raising a `TypeError` if this condition is not met.
The method should also raise a `ValueError` if the supplied value is not
greater than zero.

Override `__str__()` so that it returns a string representation that looks
like this example:

    red circle, radius 2.5, at (0.0, 0.0)

Add methods `area()` and `perimeter()` that return the area and perimeter
of the circle.

## Demo Program

Write a small program in `circledemo.py` that tests your `Circle` class,
demonstrating that it inherits properly from `Shape`.

Your program should

- Create a `Circle` object and print it (to demonstrate `__str__()`)
- Print the circle's area and perimeter, each to 3 decimal places
- Change the position of the circle and print it again
- Change the colour of the circle and print it again

Here's an example of what program output should look like:

    red circle, radius 2.5, at (0.0, 0.0)
    Area = 19.635
    Perimeter = 15.708
    Moving the circle...
    red circle, radius 2.5, at (1.6, 3.2)
    Changing the circle's colour...
    green circle, radius 2.5, at (1.6, 3.2)
