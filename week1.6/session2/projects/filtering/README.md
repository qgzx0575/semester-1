# Filtering

## Background

Filtering operations produce a new image, in which the value at a pixel is
derived by operating on a small neighbourhood of pixels in the original
image.

The simplest example is blurring of an image. To blur an image, we can
compute an average of pixel values over a 3x3 window centred on each pixel.
This average is used as the new value of the corresponding pixel in the
output image.

A larger window (e.g., 5x5) can be used, to increase the amount of blurring.

Obviously, this calculation can't be performed in its entirety at the edges
of the image. There are various strategies for dealing with this, but the
easiest is to do nothing for those edge pixels - resulting in thin black
border around the output image.

This blurring operation is a specific example of a more general operation
called **convolution**, which multiplies pixel values by a small matrix
of weights and sums the result to compute the output value. In the case of
blurring over a 3x3 neighbourhood, this matrix looks like this:

    1  1  1
    1  1  1
    1  1  1

i.e., each pixel value is given equal weight in the sum.

Other filters are possible. For example, if you use

    -1  0  1
    -1  0  1
    -1  0  1

this will produce a high output value if there is a strong gradient in the
horizontal direction. This can help to detect edges in an image.

## Task

Copy `image.py` from the `session2` directory into this subdirectory, so that
you can use it for this task.

In a new file named `filters.py` define a function named `blur()` that carries
out a 3x3 blur of the given image, returning the result as a new image.

Remember that you'll need to create an image to hold the result of the
operation. You can use class method `Image.create()` for that.

When processing the image, you'll need to address each pixel individually.
You can do this with nested for loops:

```python
for row in range(1, img.height - 1):
    for col in range(1, img.width - 1):
        ...
```

Note the limits on these loops. These are chosen to exclude the pixels lying
at the edge of the image, since we cannot do the complete 3x3 average at
those locations.

When the function is complete, write a small program in file `blur.py` that
reads an image from a PGM file, uses the function to blur it, then writes
the result out to a new PGM file.

Your program should require input and output filenames to be specified on
the command line. You can access these command line arguments as the
list `sys.argv`, which becomes available if you import the `sys` module.

It should be possible to run your program like this:

    python blur.py original.pgm blurred.pgm

Your program should display a helpful usage message if the user fails to
supply two filenames on the command line.
