"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Jayakrishnan Jayaprasad
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
savings = input("How much would you like to save every month? ")
# Validate that they have entered an integer.
try:
    print(f"You will save £{int(savings)*12} every year.")
except:
    print("That is an invalid amount.")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).
print(f"With interest, you will earn £{int(savings)*12*1.008:.2f} by the end of this year. That is an additional £{(int(savings)*12*1.008)-int(savings)*12:.2f}.")
