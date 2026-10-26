# COMP1850 Worksheet 1.5

For this worksheet, you will need to implement two Python classes in files
`rect.py` and `person.py` and then upload these files to Gradescope.

## `Rectangle` Class

### Constructor

Edit the file named `rect.py`. Complete the constructor so that it checks
the type and value of the `width` and `height` constructor parameters.

It should raise a `TypeError` exception if either parameter is not of type
`int`. It should raise a `ValueError` exception if either parameter is less
than or equal to 0.

### Other Methods

Implement the following methods:

- `is_square()`, which should return `True` if the rectangle is actually
  a square, `False` otherwise

- `area()`, which should return the area of the rectangle

- `perimeter()`, which should return the perimeter of the rectangle

Give each of these methods a suitable docstring. If you don't provide a
docstring, the tests will fail.

Do not change the names of any of these methods, or the tests will fail.

### Hints & Tips

Do not upload a solution without first checking that it actually works!
You can do this by writing a small demo program that creates a `Rectangle`
object and then calls its methods.

## `Person` Class

### Constructor

Edit the file named `person.py`. Implement a constructor that creates and
initializes fields called `name` and `birth`. The former represents a person's
name, the latter represents their date of birth.

Your constructor should raise a `TypeError` if the value provided for `name`
is not a string. It should raise a `ValueError` if the value provided for
`name` is an empty string.

The constructor should also raise a `TypeError` if the value provided for
`birth` is not a `date` object.

### Other Methods

Give your `Person` class a method named `initials()`. This should return
the uppercased initial letters of each part of person's name, joined
together into a single string. For example, if the person's name is
Alan John Smith, `initials()` should return `"AJS"`.

Give your `Person` class a method `is_birthday()`. This should return `True`
if today is the person's birthday, `False` otherwise (see below for some
hints on how to do this).

Give each of these methods a suitable docstring. If you don't provide a
docstring, the tests will fail.

Do give these methods different names, or the tests will fail.

### Hints & Tips

Do not upload a solution without first checking that it actually works!
You can do this by writing a small demo program that creates a `Person`
object and then calls its methods.

You will find the documentation for Python's `datetime` module to be useful,
particularly the section dealing with the [`date` class][dt]. This class
has a method `today()` which you can call to get today's date as a
`date` object.


[dt]: https://docs.python.org/3/library/datetime.html#date-objects
