# Week 1.2, Session 2: Task 5
# Authentication

# Predefined credentials

correct_username = "user123"
correct_password = "password456"
two_factor_enabled = True
correct_2fa_code = "7890"

# Ask user for their username and password

username = input("Enter your username: ")
password = input("Enter your password: ")

# Conditional block for login authentication

if XXX:
    if XXX:
        two_factor_code = input("Enter the 2FA code sent to your device: ")
        if XXX:
            print("Login successful! Welcome!")
        else:
            print("Invalid two-factor authentication code. Access denied.")
    else:
        print("Login successful! Welcome!")
else:
    print("Invalid username or password. Access denied.")
