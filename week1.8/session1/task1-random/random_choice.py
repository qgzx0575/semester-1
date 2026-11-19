import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices
amount = int(input("Input how many names you would like: "))

# Display the chosen names, one per line
for i in list(range(amount)):
    rand = random.randint(0,999)
    print(f"{names[rand]}")
    names.remove(names[rand])