# Task 5

## `dataset.py`

Edit `dataset.py` and complete the implementation of the `QuakeDataset` class,
guided by the comments in the file.

Note that the intention is for `Quake` objects to store the date & time of
an event in form of a `datetime` object. Python's `datetime` class has a
method `fromisoformat()` which you can call to turn a string representation
of date & time into a `datetime` object.

## `quakeinfo.py`

Edit `quakeinfo.py` and write a program that

- Obtains a significance level and time period from the user
- Creates a `QuakeFeed` object using these level and period values
- Creates a `QuakeDataset` object associated with this `QuakeFeed` object
- Invokes `read_feed()` on the `QuakeDataset` object
- Displays information about the downloaded earthquake data (see below)

You can either prompt the user interactively to enter values for level
and period, or you can provide these values to the program as command line
arguments.

The example below shows all the information that the program should display.
You don't need to format your output exactly like this.

    186 quakes, from 4.5_week.csv
    Mean depth = 66.46 km
    Mean magnitude = 5.0

    Strongest quake occurred at 02:09:00 on 2026-10-24
    at 139.9° longitude, 28.0° latitude
    The depth was 473.0 km
    The magnitude was 7.0

## Optional Extra Work

If you finish the above quickly, try doing one or more of these:

- Add methods to `QuakeDataset` to find the deepest and weakest quakes

- Add a method to `QuakeDataset` that prints the details of all quakes
  in a neatly formatted table

- Add a method to `QuakeDataset` that displays the details of all quakes
  within a specified number of degrees of a specified longitude and
  latitude
