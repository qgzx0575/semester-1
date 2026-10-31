# Benchmarking

Investigate the performance of the provided `Image` class.

If you've also tried implementing the alternate version of `Image`, in which
pixel values are stored in a list of lists, try comparing the performance
of the two versions of the class.

You could use the [`timeit` module][ti] from Python's standard libary to
help with this; alternatively, you could use the `perf_counter()` or
`process_time()` functions from the [`time` module][tm]. With the latter
approach, you will need to call the function before and after performing a
task, and subtract the first returned value from the second to get an
elapsed time measurement.

Another thing you could try is comparing operations using the provided `Image`
class with operations using an alternative image implementation - e.g., the
one provided by the [Pillow][pil] library. You should be able to install
this library into a Codespace with these commands:

    python -m pip install --upgrade pip
    python -m pip install --upgrade Pillow

You should find that Pillow is a _lot_ faster than our `Image` class. This is
because Pillow is a Python wrapper around underlying C libraries that can
represent and manipulate image data much more efficiently.


[ti]: https://docs.python.org/3/library/timeit.html
[tm]: https://docs.python.org/3/library/time.html
[pil]: https://pillow.readthedocs.io/en/stable/
