# Worksheet 1.2: Task 1 Solution
import sys
grade_str = input("Input your grade: ")

try: 
    grade = int(grade_str)
except: 
    sys.exit("Error: Grade must be an integer between 0 and 100")
    
if not (0 <= grade <= 100) :
    sys.exit("Error: Grade must be an integer between 0 and 100")     
elif 0 <= grade < 40:
    print(f"{grade} is a Fail")
elif grade < 70:
    print(f"{grade} is a Pass")
else:
    print(f"{grade} is a Distinction")