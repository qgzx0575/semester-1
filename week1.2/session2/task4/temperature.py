# Week 1.2, Session 2: Task 4
# Temperature Checker

# Prompt the user to enter the temperature in Celsius

temperature = float(input("Enter the temperature in Celsius: "))

# Use an if statement to check temperature conditions:
# 23 or above is hot, 10 to just below 23 is warm, below 10 is cold

if temperature < 10: 
    # \u00B0 will print the Celsius character
    print(f"{temperature}\u00B0C is cold.")
elif 10 <= temperature < 23: 
    print(f"{temperature}\u00B0C is warm.")
else:
    print(f"{temperature}\u00B0C is hot.")
