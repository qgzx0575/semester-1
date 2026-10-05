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
    floats.sort()
    print(f"Minimum: {floats[0]}")
    print(f"Maximum: {floats[listLength-1]}")
    print(f"Mean: {sum(floats)/listLength}")
    mid = int(listLength/2)
    if listLength % 2 == 1:
        floatMedian = floats[mid]
    else:
        floatMedian = (floats[mid]+floats[mid-1])/2
    print(f"Median: {floatMedian}")
except:
    sys.exit("Error: no numbers provided")