# Task 4

Edit `geometry.py`. This contains definitions of the now-familiar `Point`
and `Circle` classes.

All you need to do in this file is add an implementation of `__contains__()`
to `Circle`.

Your `__contains__()` method should have a parameter to represent the object
that appears to the right of the `in` operator. You can assume that this
is always a `Point` object.

The ever-present `self` parameter represents the `Circle` object that
appears to the left of the `in` operator.

Your implementation will need to return `True` if the supplied point is inside
the circle. To determine this, simply test whether the distance from the
point to the centre of the circle is less than the circle's radius.

Note: use features of the `Point` class to help you with this!

After you've implemented `__contains__()`, edit `inside.py` and write a
program here that demonstrates use of the `in` operator to test whether a
point falls inside a circle.

Run the program a few times, using different values for circle radius or
point coordinates, to check that it is behaving correctly.
