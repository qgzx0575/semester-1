# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

try:
    numbers = read_numbers()
    numbers.sort()
    print(f"Minimum = {numbers[0]}")
    print(f"Maximum = {numbers[len(numbers)-1]}")
    print(f"Mean = {sum(numbers)/len(numbers)}")
    mid = int(len(numbers)/2)
    if len(numbers) % 2 == 1:
        floatMedian = numbers[mid]
    else:
        floatMedian = (numbers[mid]+numbers[mid-1])/2
    print(f"Median = {floatMedian}")
except:
    sys.exit("Error: no numbers provided")