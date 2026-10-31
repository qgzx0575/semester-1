# Task 4

## `Quake` Class

In a terminal window, run the Python interpreter by entering `python`.

Import the `datetime` class from Python' standard library and create a
`datetime` object repreenting the time right now:

    from datetime import datetime
    now = datetime.now()

Then import the `Quake` class and attempt to create an object:

    from quake import Quake
    q = Quake(now, 139.9, 28.0, 473.0, 7.0)

Finally, print the object:

    print(q)

You can see from these experiments that `Quake` clearly has a constructor
and a reasonable override of `__str__()`. We didn't have to write any code
for this. It gets this functionality by virtue of being a data class.

Leave the interpreter running for the next part of the task (below).

## `QuakeFeed` Class

Experiment with the `QuakeFeed` class in the Python interpreter.

Start by importing the class:

    from feed import QuakeFeed

Next, try creating a feed using an invalid level or period:

    QuakeFeed("4.9", "week")
    QuakeFeed("4.5", "fortnight")

Both of these attempts should fail with a `TypeError` exception.

Now create a valid feed and look at how it is represented as a string:

    feed = QuakeFeed("4.5", "week")
    print(feed)

To read the feed and make its data available, do this:

    reader = feed.reader()
    type(reader)

The second of these commands shows you that a `QuakeFeed` makes downloaded
data available as a `DictReader` object, `DictReader` being a class defined in
Python's [`csv` module][csv].

Try using `next()` a couple of times on this `DictReader` object:

    next(reader)
    next(reader)

Each invocation of this function returns the next set of earthquake details,
in the form of a dictionary. Notice that the dictionary contains a lot more
data than what we actually need. The only values we will need are those
defined in the `Quake` class.

Notice also that the values in the dictionary are all strings. They will need
to be converted into appropriate data types when creating a `Quake` object.

Finally, try iterating over all of the remaining earthquake data:

    for info in reader: print(info)

Note that you'll need to press the Enter key _twice_ here to run the code.

Press `Ctrl+D` to exit the interpreter when you are done.


[csv]: https://docs.python.org/3/library/csv.html
