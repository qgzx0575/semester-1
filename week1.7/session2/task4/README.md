# Week 1.7, Session 2: Task 4

`grades.py` is a Python program to process the exam marks in a CSV file,
generating a final grade of 'Distinction', 'Pass' or 'Fail' for each
student named in the file, based on their exam mark.

This program has **four** bugs in it. In this task, we will use Pdb to
investigate two of these bugs, and unit testing to find the others.

## First Bug

1. To see the first bug, try running `grades.py` without any command line
   arguments, then with `marks.csv` as the sole command line argument.
   You should see that it doesn't behave as expected.

2. Now run `grades.py` via the debugger. Maximize the size of the terminal
   and then enter

       python -m pdb grades.py marks.csv

   You should see a pointer to the first line of the file, along with a
   debugger prompt:

       -> import sys
       (Pdb)

3. Enter `help` at the debugger prompt. This will list the available commands.
   Use the `help` command to read about two or three of these commands.

4. List some of the program's source code by entering `list`. You can
   abbreviate this to `l`. Enter this command a few more times. Notice how
   it shows you the program in small chunks (around 10 lines, by default).

5. Establish a breakpoint on line 49, like so:

       break 49

   You can abbreviate the command to `b` if you prefer. If you use `list` or
   `l` to display source code, you should see that line 49 is now labelled
   with a 'B'.

6. Enter `continue`, or `c` if you prefer, to resume execution. The program
   should pause at the specified breakpoint:

       -> if len(sys.argv) != 1:
       (Pdb)

7. Examine the contents of `sys.argv` with

       p sys.argv

   You should see the following list displayed:

       ['grades.py', 'marks.csv']

   Now it should be clear what the problem is. In normal usage of the program,
   `sys.argv` contains 2 elements: the name of the program and the name of
   the file containing the exam marks. However, the `if` statement that
   begins on line 49 is displaying an error if the size of `sys.argv` is not
   equal to 1.

8. Quit the debugger with `quit` or `q`. Fix the problem on line 49, then
   try running program, first without a command line argument, then with
   `marks.csv` as a command line argument.

   The first of these attempts should result in the display of a usage
   message. The second should reveal another problem: something has gone
   wrong inside the `grade()` function.

## Second Bug

Note: from this point on, we use the abbreviated versions of Pdb commands
where possible.

1. Load the program into the debugger, in exactly the same way as you did
   when investigating the first bug. Then establish a breakpoint inside
   `grade()` like this:

       b grade

2. Enter `c` to resume execution. The program should stop at the first
   statement inside `grade()`.

   Since the error message related to variable `mark`, try printing its
   value like so:

       p mark

   Note that you can also query the _type_ of a variable (since this won't
   always be obvious):

       whatis mark

3. Enter `w` (short for `where`) to view the program's call stack. Then
   enter `u` to move up one level, to the main program.

   If you print the value of `mark` again, you will see that it referenced
   a string before `grade()` was even called.

   Now try 'pretty printing' the contents of the `marks` dictionary:

       pp marks

   You will see that all of the values in the dictionary are strings, when
   they should be integers. The problem must therefore be in the code that
   created this dictionary - i.e., the `read_marks()` function.

4. Establish another breakpoint in the offending function, with

       b read_marks

   Then enter `restart` to restart the program, followed by `c` to continue
   executing until the first breakpoint. This should put you just inside
   `read_marks()`.

5. Now use `n` to execute the code in `read_marks()`, one statement at a
   time. Do this three times, until you hit the start of the `for` loop.
   Use the `p` command to display the current values of the `infile` and
   `data` variables.

6. Enter `n` twice more. Print the values of the `name` and `mark` variables.
   Enter `n` one more time, and print the value of `data`. This should be
   enough to demonstrate that student name and exam mark were retrieved from
   the file as strings, but the mark was never converted to an integer before
   being stored in the dictionary.

7. Quit the debugger. Fix the problem in `read_marks()`, then run the program
   with `marks.csv` as a command line argument. This time, it should run
   to completion - but is it really working as specified?

   Read the docstring of the `grade()` function, then compare each line
   of program output with the contents of `marks.csv`. Can you see another
   problem here?

## Third & Fourth Bugs

The docstring of `grade()` is useful for humans, but **a better way of
expressing the required behaviour is via automated unit tests**.

We've provided these in `test_grade.py`.

1. Examine the code in `test_grade.py`, then run this program. One of the
   assertions should fail.

2. The information from the failed assertion should be enough for you
   to quickly identify which part of `grade()` is causing the problem,
   without the need for the debugger.

   Fix the problem and then run the `test_grade.py` again. You should see
   another failed assertion.

3. Study the output from the program carefully. The most useful bit can be
   found at the bottom. You can see that the test is using `"50"` as the
   exam mark - i.e., a string. The test failed because a `MarkError` exception
   was expected, but what actually occurred was a `TypeError` exception.

4. Fix the problem by adding code to `grades.py` that will raise a `MarkError`
   exception if the value passed to `grade()` is not an integer.

   Hint: you can use Python's `isinstance()` function here. For example,
   `isinstance(x, int)` will return `True` if `x` references an integer, or
   `False` if it doesn't.
