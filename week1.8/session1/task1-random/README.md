# Task 1

## `seed_effect.py`

1. Study the code of this program. Note the call to `random.seed()` on line 5.
   Run the program a couple of times and observe its output.

2. Change the argument of the call to `random.seed()` from 10 to something
   else, then run the program a couple more times.
 
3. Comment the call to `random.seed()` out by putting a `#` at the start of
   the line, then run the program a few more times.

4. Finally, add a comment to the file explaining what you think is
   happening here.

## `random_numbers.py`

In this file, write a program that

1. Gets the user to input how many random numbers they want
2. Generates this many random numbers
3. Writes the numbers out to a file named `random.txt`, one number per line

You can generate random integers or floating-point values, as you prefer.

Run the program after completing each of the steps listed above, to check that
it is working correctly.

## `random_choice.py`

This file contains code to read a list of names from the file `names.txt`.

Add further code that

1. Gets the user to input how many names they want to pick
2. Picks that many names at random, **avoiding any duplicate picks**
3. Displays the chosen names, one per line
