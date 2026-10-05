# COMP1850 Worksheet 1.2

For this worksheet, you will need to implement two Python programs and upload
them to Gradescope for grading.

## Task 1

Edit the file named `task1.py`. In this file, write a program that

* Asks users to enter an integer grade in the range 0 to 100

* Converts that grade into a result of Pass, Fail or Distinction, where

  - Fail = 0-39
  - Pass = 40-69
  - Distinction = 70-100

* Prints out the numeric grade and the result **on a single line**, with
  *exactly* same format as the examples below:

      82 is a Distinction
      57 is a Pass
      36 is a Fail

If the user enters something that isn't a number, or they enter an integer
value outside the required range, the program should immediately exit, after
first displaying this exact error message on the standard error channel:

    Error: Grade must be an integer between 0 and 100

Use the `exit()` function from Python's `sys` module to achieve this. Here
is an example of how you import this module and use the `exit()` function:

```python
import sys

sys.exit("Error!")
```

### Hints

Strings have an `isdecimal()` method that will tell you whether they could
be parsed as a decimal integer.

## Task 2

Edit the file named `task2.py`. In this file, write a program that

* Prompts the user to enter a sequence of `float` values
* Reads these values into a list, using the code we have provided
* Finds the minimum, maximum, mean and median of these values
* Prints these statistics

For example, given the list

    [4.5, 3.0, 1.2, 7.0, 6.3]

Your program should print this as its output:

    Minimum = 1.2
    Maximum = 7.0
    Mean = 4.4
    Median = 4.5

If no numbers were entered, the program should terminate with a non-zero
exit status and display the following error on the standard error channel.

    Error: no numbers provided

Use the `sys.exit()` function to do this, as you did in `task1.py`.

### Notes

* **Read the numbers from the user using the function that we have provided
  for this purpose.** The function is defined in the file `util.py`.

  You can use it like this:

  ```python
  from util import read_numbers

  numbers = read_numbers()
  ```

* Your program must NOT use any Python modules other than the `sys` and
  `util` modules mentioned above.

* Your program should perform its calculations without using loops.

### Hints

* Minimum, maximum and mean can be determined in a fairly straightforward
  manner, using four of Python's [built-in functions][funcs].

* The **median** is the 'middle' number, after arranging numbers in
  ascending order. You can use [one of Python's list methods][list] to help
  you arrange the numbers in this way.

  Note that there won't be a single middle number when the list size is
  even. Your code will need to handle this appropriately. See the
  [definition of median][med] for further information on this.


[funcs]: https://docs.python.org/3/library/functions.html
[list]: https://docs.python.org/3/library/stdtypes.html#lists
[med]: https://en.wikipedia.org/wiki/Median#Finite_set_of_numbers
