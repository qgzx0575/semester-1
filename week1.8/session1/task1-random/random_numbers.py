import random

# Get user to input how many random numbers they want
amount = int(input("How many random numbers would you like: "))

# Generate this many random numbers
with open("random.txt", "w") as file:
    for i in list(range(amount)):
        file.write(f"{random.randint(1,100)}\n")

# Write the random numbers to a file named random.txt, one number per line
