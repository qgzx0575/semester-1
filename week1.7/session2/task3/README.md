# Week 1.7, Session 2: Task 3

`calculate_total.py` is a simple Python program to calculate a retail total by multiplying a base price by a tax rate and adding the result together.

However, it containts a deliberate `Type` bug. We will use Pdb to investigate this bug.


## Instructions

### Step 1: Run `calculate_total.py` and observe the output.

	python calculate_total.py

You will see a `TypeError` is raised, with function call `calculate_total()` at line 12
and `TypeError` at line 5 with the multiplication operation:

	Calculating total...
	Traceback (most recent call last):
	  File ".../calculate_total.py", line 12, in <module>
		final_amount = calculate_total(item_price, tax_percentage)
	  File "...calculate_total.py", line 5, in calculate_total
		tax = price * tax_rate
			  ~~~~~~^~~~~~~~~~
	TypeError: can't multiply sequence by non-int of type 'float'


### Step 2: Launch the script with `pdb` and then enter.

	python -m pdb calculate_total.python


The program will immediately pause on the first line:

	> ... /calculate_total.py(3)<module>()
	-> def calculate_total(price, tax_rate):
	(Pdb)

### Step 3: Add a dynamic breakpoint with `b` or `break`
You want to stop the code right before the `calculate_total` function runs on line 12.
Use the `b` command followed by the line number:

	(Pdb) b 12
	Breakpoint 1 at .../calculate_total.py:12


### Step 4: View your active breakpoints
Type `b` with no numbers to see a list of all dynamic breakpoints currently set:

	(Pdb) b
	Num Type         Disp Enb   Where
	1   breakpoint   keep yes   at .../calculate_total.py:12
	
### Step 5: Run until the breakpoint with `c` or `continue`
Type `c` to let the code run at normal speed until it encounters your dynamic breakpoint.

	(Pdb) c
	> .../calculate_total.py(12)<module>()
	-> final_amount = calculate_total(item_price, tax_percentage)

### Step 6: Step into the function (`s` or `step`)
Because line 12 is a function call, type `s` to jump inside the `calculate_total` function.

	(Pdb) s
	--Call--
	> .../calculate_total.py(3)calculate_total()
	-> def calculate_total(price, tax_rate):

### Step 7: Step forward and inspect variables (`n`, `p`)
Type `n` or `next` twice to move down the line that cause the crash:


	(Pdb) n
	> .../calculate_total.py(4)calculate_total()
	-> print("Calculating total...")
	(Pdb) n
	Calculating total...
	> .../calculate_total.py(5)calculate_total()
	-> tax = price * tax_rate

Before executing this line, check the value and data type of price using `p` or `print`.

	(Pdb) p price
	'20'

The single quotes around '20' prove that it is a string, not a number. 
This explains why multiplying it by the float 0.05 causes a `TypeError`.

If you type `n` again, it will raise the `TypeError`.

	(Pdb) n
	TypeError: can't multiply sequence by non-int of type 'float'
	> .../calculate_total.py(5)calculate_total()
	-> tax = price * tax_rate


### Step 8: Clear the breakpoint and exit (`cl`, `q`)
When you are done, you can clear the breakpoint using `c1 1` and exit the debugger by typing `q`.

	(Pdb) cl 1
	Deleted breakpoint 1 at .../calculate_total.py:12
	(Pdb) q

### Step 9: Fix the bug
Fix the bug by changing the string "20" to 20.

Then, rerun the file and see that the bug is now fixed.
