# Additional Work For Week 1.2

If you finish the tasks quickly and have time on your hands, here are some
other things you can try. Put your code for this additional work in this
directory, to keep it separate from the other tasks.

## Session 1

* Lists can be constructed using a feature called a **list comprehension**.
  Investigate this feature, and write some Python code to demonstrate it.

  Do the same for set comprehensions and dictionary comprehensions.

* Given a list `x`, what is the difference between these two lines of code?

  ```python
  x.sort()
  sorted(x)
  ```

* Investigate the following types provided by the `collections` module in
  the Python standard library:

  + `namedtuple`
  + `deque`
  + `Counter`

  In each case, write a small program that demonstrates how the collection
  can be used.

## Session 2

* What does the following Python code return, and why?

  ```python
  answer = False
  isinstance(answer, int)
  ```

* Create new versions of the ATM simulator and calculator from Task 5.
  These new versions should use a match statement instead of a multi-branch
  if statement.

* Rewrite the calculator example from Task 5 so that it allows the user
  to enter their calculation as a single string, e.g., `2 + 5`, `4 * 37`.
