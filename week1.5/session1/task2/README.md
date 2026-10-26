# Task 2

Try running `badclass1.py`. Examine the error message carefully.

What is the specific cause of this error? What should we change in the
definition of `Point` to fix it?

Now try running `badclass2.py`. This demonstrates a different problem.
Again, examine the error message carefully.

What is the specific cause of this error? What should we change to fix it?

Before applying any fixes to these problems, try running `pylint` on each
of these files by entering the following commands in the terminal:

    pylint badclass1.py
    pylint badclass2.py

(Make sure you are in the same directory as the files before doing this!)

This tool will report a number of issues, including the specific problems
that prevent the class definitions from working correctly.
