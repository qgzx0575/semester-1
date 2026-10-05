# Worksheet 1.2: Task 2 Solution
import sys

try:
    listLength = int(input("Enter how many floats you will be entering: "))
except: 
    sys.exit("Error: no numbers provided")

try:
    floats = [] 
    for i in range(listLength):
        newFloat = float(input(f"Enter float #{i+1}: "))
        floats.append(newFloat)
        i += 1
    floats.sort()
    print(f"Minimum: {floats[0]}")
    print(f"Maximum: {floats[listLength-1]}")
    floatSum = sum(floats)/range(listLength)
    print(f"Mean: {floatSum}")
except:
    sys.exit("Error: no numbers provided")