# Task 1

## Type Hinting

`hinting.py` contains an implementation of the `Point` class from Session 1,
along with a small amount of testing code. This code attempts to create a
`Point` object by passing in strings for `x` and `y`, rather than numbers.
It then attempts to invoke `distance()` on the created object.

Start by running the program. Notice that the program fails **on the line
that invokes the `distance()` method**, not on the previous line that
creates the `Point` object.

Next, run the `mypy` type checking tool on the code, by entering the following
command in the terminal window:

    mypy hinting.py

This should report no problems with the code. This is because we haven't yet
provided any indication of what types the `Point` class is expecting.

Now edit `hinting.py` and add type hints for

- Constructor parameters `x` & `y`
- The return type of `distance()`
- Parameter `p` of `distance_to()`
- The return type of `distance_to()`

(See the slides for examples of how to do this.)

Examine the code carefully in the editor. Does VS Code provide any indication
that you are attempting to create a `Point` object incorrectly?

Try running the program again. Notice that nothing has changed. The addition
of type hints didn't affect how Python compiled and executed the code.

Finally, run `mypy` again. It should now correctly identify the problem with
how the `Point` object is being created. The addition of type hints made
this possible.

## Type Checking

`checking.py` contains the same code that was provided in `hinting.py`.

Run the program to verify that the same failure occurs, when the `distance()`
method is called.

Modify this code so that the constructor uses the `isinstance()` function to
check the types of parameters `x` and `y`. You should allow the types to be
either `int` or `float`. Any other type should result in your code raising
a `TypeError` exception, with an appropriate error message.

(Note: the slides give you an example of suitable code!)

Now rerun the program. It will still fail, but this time during object
construction rather than when attempting to use the object.
