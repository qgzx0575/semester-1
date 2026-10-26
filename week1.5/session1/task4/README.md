# Task 4

## Class Definitions

Copy your implementation of `Point` from Task 3 into `geometry.py`.

Beneath the `Point` class, write a new class named `Circle`. This should
represent a circle by its radius and its centre coordinates.

Give your `Circle` class:

- An appropriate docstring

- A constructor that creates and initializes fields named `radius` and
  `centre`

- An `area()` method that computes and returns the area of the circle

- A `perimeter()` method that computes and returns the circle's perimeter

### Note

Radius should come before centre coordinates in your constructor parameter
list. This will allow you to provide a default value of `Point(0.0, 0.0)`
for the centre coordinates.

Your constructor and `area()` & `perimeter()` methods should all be given
appropriate docstrings.

You will need the constant pi to compute area and perimeter. This is
available in the `math` module, which has already been imported for you.
You can access the constant as `math.pi`.

Watch out for syntax errors as you implement this class. If you have installed
the Python extension into VS Code, it should flag these problems by underlining
the offending code.

You can also do 'linting' of `geometry.py` to identify issues, by running the
following command in a terminal window:

    pylint geometry.py

## Importing The Module

In the terminal window, enter `python` to run the Python interpreter.

At the `>>>` prompt, enter `import geometry` to import the module, then
enter `help(geometry)` to view the docstrings. Notice how the docstring at
the top of the file is displayed as documentation for the module. After
this, you should see documentation for each class, based on the docstrings
that you have given to the classes and their methods.

Press `q` to quit the help page, then `Ctrl+D` to quit the interpreter.

Look at the contents of the current directory with `ls`. You should see a
new subdirectory named `__pycache__`. This contains the compiled version of
the `geometry` module. Python compiles modules to bytecode when they are
first imported, then uses this cached bytecode in the future to speed
up program execution.

## Demo Program

Now edit `circledemo.py`. Add one or two import statements that will give you
access to the `Point` and `Circle` classes.

Then add code that

1. Prompts the user to input x and y coordinates as `float` values, then uses
   these to create a `Point` object to represent the circle's position.

2. Prompts the user to input a `float` value for circle radius.

3. Uses the `Point` object and radius value to create a `Circle` object.

4. Displays the area of the circle, to 4 decimal places.

5. Displays the perimeter of the circle, to 4 decimal places.

Run your program to check that it behaves correctly.
