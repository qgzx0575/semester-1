# Binary PGM Files

The `Image` class discussed at the start of the session can read and write
the simple text-based version of the PGM format, but this is inefficient.
A variation of this format stores the header information as text but the pixel
values as binary data, saving disk space.

This more efficient format begins with a 'magic number' of `P5` instead of
`P2`. The other header elements are the same as for the plain text version.
For more information, see the [PGM documentation][pgm].

Copy the provided module `image.py` from the `session2` directory into this
subdirectory, then modify the `Image` class so that it can cope with both
versions of the PGM format.

Note that you will need to open the file for reading binary data, by using a
mode of `"rb"`. You should still be able to read header lines using the
`readline()` method (although note that it will now return byte strings rather
than text strings). You can use the `read()` method to read the pixel data.

Python's [File I/O documentation][io] may be helpful here.

You'll find a couple of raw PGM files in the `images` subdirectory. You
can use these for testing.


[pgm]: https://netpbm.sourceforge.net/doc/pgm.html
[io]: https://docs.python.org/3/library/io.html
