'''
This is a difficult activity which will involve some relatively challenging filtering/sorting of data
You will want to have the docs or a guide on using matplotlib/pandas available, it is not expected that you do this completely independently.
chatGPT is very good when debugging Pandas, as it decodes error messages into more readable explanations- so if you are struggling to understand what 
you have done wrong I recommend pasting error messages into it!

All the basic program code has been included, you should be able to simply write the code to filter the data into an appropriate dataframe and then
plot and show the graphs.
'''

import pandas as pd
import matplotlib.pyplot as plt

def average_bar_chart(data):
    '''
    Complete this code to produce a bar chart of the total of each 'hours per day' column
    '''
    pass

def hours_histogram(data, column_name):
    '''
    Complete this code so that it can display a histogram of any given 'hours per day' column
    '''
    pass

def hours_pie_chart(data, student_id):
    '''
    Complete this code so that it produces a pie chart of any given student's hours per day - this should be selected by student ID (the first column)
    '''
    pass

def total_hours_per_stress_level(data, stress_level):
    '''
    Complete this code to create a stacked bar chart showing a breakdown of the total hours worked by students, grouped by their reported stress level.
    '''
    pass

def display_menu():
    print("Student Lifestyle Data Analysis")
    print("1 - view average hours per day")
    print("2 - view specific activity")
    print("3 - view per-student breakdown")
    print("4 - view per stress level breakdown")
    print("Q - quit")
    choice = 0
    while choice not in ["1","2","3","4","Q"]:
        choice = input("Select option: ").upper()
    return choice


## main program:

data = pd.read_csv("lifestyle_data.csv")

# Note - when you run this in Interactive mode, the 'input' will be through a pop up instead of the terminal.
while True:
    choice = display_menu()
    match choice:
        case "Q":
            break
        case "1":
            average_bar_chart(data)
        case "2":
            col = input("Enter Hours Per column to analyse: ")
            hours_histogram(data, col)
        case "3":
            stid = int(input("Enter student ID: "))
            hours_pie_chart(data, stid)
        case "4":
            stress_level = input("Enter stress level: ").title()
            total_hours_per_stress_level(data, stress_level)
