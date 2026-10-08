# Week 1.2, Session 2: Task 5
# Calculator

# Ask user for two integers

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Ask user for the desired operation

print("Select an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

operation = int(input("Enter your choice (1-4): "))

# Conditional block to perform the selected operation

if operation == 1:
    result = num1 + num2
    print(f"The result of addition is: {result}")
elif operation == 2:
    result = num1 - num2
    print(f"The result of subtraction is: {result}")
elif operation == 3:
    result = num1 * num2
    print(f"The result of multiplication is: {result}")
elif operation == 4:
    if num2 != 0:
        result = num1 / num2
        print(f"The result of division is: {result}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation selected.")
