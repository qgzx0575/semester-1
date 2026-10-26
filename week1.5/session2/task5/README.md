# Task 5

(View this file on github.com, or in VS Code's preview mode.)

## `data.py`

This file contains a class `Dataset`, which is incomplete. The first thing
you need to do is complete the implementation of this class.

A key thing to understand is that a regular Python list is used by the
`Dataset` class. You can see that this is created by the constructor that
we have written for you. This list is the only field of the class. All
of the methods of `Dataset` operate on this list in various ways.

### `load_data()`

Implement `load_data()` so that it clears the list of any existing data,
then populates it with data from the named file. Refer back to the material
on loops and file I/O if you are not sure how to proceed here.

### Dunder Methods

Implement `__len__()` so that it returns the number of values that have
been read from the file.

Implement `__getitem__()` so that it returns the item of data at the given
integer index.

Note that these both very simple 'one-liners'.

### Statistical Methods

Implement `mean()` so that it returns the arithmetic mean of all the values
stored in the `Dataset`. You can use built-in function `sum()` to help you
implement this very concisely.

Implement `median()` so that it returns the [median][med] of the values stored
within a `Dataset` object. You'll need to careful here. Computing a median
requires a sorted list of values, but you shouldn't modify the list that
was populated from the file, in caser the ordering of values is significant.

Instead, create a sorted version of the original, like this:

    sorted_data = sorted(self.data)

## `datademo.py`

In this file, you need to write a program that demonstrates use of `Dataset`.

Your program should prompt the user to enter a filename, then create a
`Dataset` object representing the data in this file.

After that, it should display

- The size of the dataset
- The mean and median of the values in the dataset
- Each value in the dataset, by iterating over it with a for loop

**Use the API provided by `Dataset` to achieve all of this!** Do not access
the list field of `Dataset` directly from within the program.

(The point here is to demonstrate that the API provided by `Dataset`'s
methods is sufficient for useful work.)

You'll need to create one or more files of data in order to run `datademo.py`.
These files should contain only numbers, one per line.


[med]: https://en.wikipedia.org/wiki/Median
