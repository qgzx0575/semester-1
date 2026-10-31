# Look-Up Tables

## Background

Modifications to the brightness or contrast of a greyscale image can be viewed
as functions applied to pixel values. For example, the function

    f(x) = 255 - x

inverts image brightness, turning white (255) into black (0), and black into
white.

Non-linear functions can also be applied. For example, we can compute the
square-root of pixel values, and then multiply the result by a scaling factor
so that an input range of 0-255 still maps to an output range of 0-255. This
calculation has the effect of enhancing contrast in the dark parts of an
image and reducing it in the bright parts.

Since there are only 256 possible pixel values in an 8-bit greyscale image,
it makes sense to pre-compute all possible results of applying the function
to a pixel value, storing these results in a **look-up table** (LUT).
We process the image by passing pixel values through this LUT.

In Python, a LUT could be as simple as a list containing 256 integer values.
A pixel's value is used as the index into this list. The value stored at
that index is the new value to use for that pixel.

For example, you could do

```python
table = list(range(256))
```

This creates a list with indices 0 to 255, and values of 0 to 255 stored at
those indices. If you apply this LUT to an image, the image will remain
unchanged.

A more interesting approach is to create a class to represent a generic
LUT, along with subclasses to represent specific kinds of LUT.

## Task

Copy `image.py` from the `session2` directory into this subdirectory, so that
you can use it for this task.

Then write some code to create a LUT, read an image from a file, apply the
LUT, then write the result of the operation to a new file. Inspect the file to
check the visual effect of applying the LUT.

When iterating over image pixels, you can take advantage of the fact that
they are stored in a linear list, and that you can index them directly.
A loop like this can be used to access each pixel's value:

```python
for i in range(img.width * img.height):
    # Inside loop, access pixel value as img[i]
```

You can represent the LUT either as a list, as noted above, or create your
own `LookupTable` class. The latter is a bit more effort but is the more
interesting and powerful approach.

If you implement the class, give it these three methods:

- A `display()` method that prints out the mapping of pixel values
  performed by the LUT

- An `apply()` method that passes the given image through the LUT, returning
  the result as a new image

- An `apply_in_place()` method that modifies the given image using the LUT
