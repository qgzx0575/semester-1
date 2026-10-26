# Task 3

Edit `point.py` and complete the implementation of `Point` so that it has
the constructor and `distance()` method discussed in the slides. Make
sure that you write suitable docstrings for both of these.

Then write some code that creates a `Point` object, displays the values
of its x and y fields, and displays the distance of the point from
the origin.

Run the program and check that it behaves as expected.

Finally, add a new method named `distance_to()` to the class. This should
compute the distance from the `Point` object receiving the method call
to another `Point` object passed in as an argument of the method.

You can do this by generalising from what the `distance()` method does.
If you are not sure how to proceed, try sketching a pair of x and y axes,
with a point at coordinates (x1, y1) and another at coordinates (x2, y2).
draw a straight line between the points and think of it as the hypotenuse
of a right-angled triangle...

Make sure you new method has an appropriate docstring.

Modify the demo program beneath the class definition, so that it creates a
second `Point` object and demonstrates use of `distance_to()` using the
two `Point` objects.
