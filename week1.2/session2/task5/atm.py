# Week 1.2, Session 2: Task 5
# ATM Simulation

# Initial balance set to a fixed amount

balance = 1000.0

# Ask user for the desired transaction type

print("Welcome to the ATM!")
print("Select an option: ")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
option = int(input("Enter your option (1-3): "))

# Conditional block for ATM operations

if XXX:
    print(f"Your current balance is: £{balance:.2f}")
elif XXX:
    deposit_amount = float(input("Enter the amount to deposit: "))
    balance += deposit_amount
    print(f"You have deposited £{deposit_amount:.2f}")
    print(f"Your new balance is £{balance:.2f}")
elif XXX:
    withdraw_amount = float(input("Enter the amount to withdraw: "))
    # Nested conditional for withdrawal
    if XXX:
        balance -= withdraw_amount
        print(f"You have withdrawn £{withdraw_amount:.2f}")
        print(f"Your new balance is £{balance:.2f}")
    else:
        print("Insufficient funds.")
else:
    print("Invalid option. Please try again.")
