# Colour Images

The PPM (Portable Pixmap) format is a variation of PGM in which pixels have
colours rather than a single greyscale value. Colour is represented as a
triplet of values, representing the red, green and blue components of the
colour.

The plain text version of the PPM format begins with a 'magic number' of `P3`
instead of `P2`. The other header elements are the same as for PGM. The single
maximum value stored in the header now represents the maximum of each of the
3 components that make up a colour. For more information, see the
[PPM documentation][ppm].

Copy the provided module `image.py` from the `session2` directory into this
subdirectory, then edit this file and start by refactoring the existing
code into _two_ classes: `Image` and `GreyImage`. The latter should inherit
from the former.

In this arrangement, some of the code can remain in `Image`, whereas some
of it will need to live in `GreyImage`. For example, `_parse_dimensions()`,
`_parse_max_value()` and `copy()` can all stay in `Image`.

You can also leave dunder methods `__getitem__()` & `__setitem__()` and
regular methods `get()` & `set()` in `Image`, because they don't make
any assumptions about the type of value that a pixel has. In `GreyImage` it
can be assumed to be a single integer, whereas in `ColourImage` it can be
assumed to be a tuple of 3 integers.

When you've finished this refactoring, test the `GreyImage` class to make
sure that it still works!

Finally, add a new class to the module, named `ColourImage`. Like `GreyImage`,
this should inherit from `Image`, so that it can reuse all of the code already
in that class.

Test the class to make sure it supports reading, writing and modification of
colour images properly.

You'll find a couple of PPM files in the `images` subdirectory. You can use
these for testing.


[ppm]: https://netpbm.sourceforge.net/doc/ppm.html
