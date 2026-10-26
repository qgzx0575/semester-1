# Task 3

You are provided with files `money.py` and `add.py`.

`money.py` is a partial implementation of a class to represent an amount of
money. You need to add the missing code here.

`add.py` has no code in it. You need to write a program here that tests
the finished implementation of the `Money` class.

## Finishing The Constructor

The constructor already assigns the provided values for pounds and pence to
fields, but before this code you should add some checks of the provided
values.

You need to ensure that the provided values are both integers, and that they
are within the allowed ranges for this particular currency.

If your checks identify violations of these requirements, your code should
raise the appropriate exception: `TypeError`, if either parameter is not
integer; `ValueError`, if either parameter is not in its allowed range. Give
your exception objects helpful error messages.

When you've added this code, test it in the Python interpreter. Enter `python`
in the terminal window to run the interpreter, then import the `Money` class
and make some invalid attempts to create a `Money` object:

```python
>>> from money import Money
>>> Point(1.0, 50)
>>> Point(1, "fifty")
>>> Point(-1, 50)
>>> Point(1, -50)
>>> Point(1, 100)
```

Each of the above should fail with an exception.

Press `Ctrl+D` to exit the interpreter when you've finished testing.

## Overriding `__str__()`

Next, implement a suitable `__str__()` method. Remember that this needs
to return a string. The string should start with the standard currency symbol
and then show pounds and pence, separated by a decimal point.

Here are some examples:

    £0.01
    £1.05
    £17.99
    £150.00

Tip: the simplest approach is to use an f-string. Remember that you can
control the formatting of values substituted into f-strings. For example, the
format specifier `02d` will format a decimal integer value using two digits,
adding a leading zero where necessary...

## Implementing `__add__()`

Before writing any code, sketch out on paper how you would add together two
sums of money such as £1.99 and £0.05. This will give you a good indication of
the code that is required for the `__add__()` method.

Summing the pounds and pence separately is obviously part of the solution,
but you also need to account for the fact that the sum of the two pence
values may exceed the maximum allowed value of 99.

The integer division and modulus operators, `//` and `%`, will be useful here.

Remember that the value returned by `__add__()` should be a `Money` object,
constructed from your sums of pounds and pence.

## Demo Program

The program in `add.py` should create two different amounts of money, print
them (to demonstrate the `__str__()` method), then add them together and
print the result.

Be sure to run the program, to check that it and the class are behaving
as you expect.
