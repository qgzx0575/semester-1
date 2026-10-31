# Pixel Representations

The `Image` class we have provided uses a linear list to store pixel values,
but this is not the only option.

Try using one of the alternative representations described below.

## List of Lists

Copy `image.py` from the `session2` directory into this subdirectory and
modify the `Image` class so that pixel values are stored as a 'list of lists',
as we discussed at the start of the session.

You should remove dunder methods `__getitem__()` and `__setitem__()` from
your new version of the class, as these are no longer supportable, but
don't make any other changes to the API of the class.

You will need to make changes to the implementations of these methods:

- `create_pixels()`
- `_parse_pixels()`
- `_write_pixels()`
- `get()`
- `set()`

Test your new version of the class to make sure that images can still be
read, written and modified successfully. The class should behave identically
to the original version.

## `array` Object

The [`array` module][arr] in the Python standard library provides a more
memory-efficient representation of an array of values.

Copy `image.py` from the `session2` directory into this subdirectory and
modify the `Image` class so that pixel values are stored as an `array`. Use
`B` as the array's typecode.

Test your new version of the class to make sure that images can still be
read, written and modified successfully. The class should behave identically
to the original version.


[arr]: https://docs.python.org/3/library/array.html
