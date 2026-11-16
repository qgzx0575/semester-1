'''
This will combine some basic data handling, plotting, and writing functions.
You will probably want to have the docs/help open to support you!

The base code is provided at the bottom - you can add to this, change it, or remove it and write your own if you prefer!

You are welcome to add more options to the menu and create your own graphs - think of how you can use the different styles of graph.

For example - you could add box and whisker diagrams to show averages, or scatter plots to show outliers.

The data set 'ramen-ratings.csv' draws from a popular blog rating instant ramen products.
'''
import pandas as pd
import matplotlib.pyplot as plt
import random


def show_histogram_of_ramen_scores(data):
    '''
    Create a histogram to show the distribution of numbers of stars given to ramen.
    '''
    pass

def show_bar_chart_stars_per_manufacturer(data):
    '''
    Create a bar chart showing the average rating per manufacturer
    '''
    pass

def show_bar_chart_stars_per_country(data):
    '''
    Create a bar chart showing the average rating per country
    '''
    pass

def find_best_per_country(data, country):
    '''
    Find and return the index of the row with the highest rating per country.
    If there are two with equal rating, you can return either.
    '''
    pass

def find_worst_per_country(data, country):
    '''
    Find and return the index of the row with the lowest rating per country.
    '''
    pass

def show_piechart_of_manufacturers_by_country(data, country):
    '''
    Create a pie chart showing the percentage of each manufacturer in the country
    '''

def print_ramen_rating(rating):
    '''
    Print out a row from the dataframe ('rating') in a more human-readable format, e.g.:

    Name: 
    Type of ramen:
    Manufacturer:
    Country of Origin:
    Stars:
    '''
    pass

def show_top_ten(data):
    '''
    Select the top-ten ramen and print them out in order of lowest rating to highest
    You may want to call your print_ramen_rating() function for this.
    '''
    pass

def random_ramen_review(data):
    '''
    Pick a random ramen from the dataframe and give it's basic information.
    You could also add:
        How it compares to its country and manufacturer averages
        A graph showing where it is on the histogram (you can add a vertical line at a specific value)
        Anything else you think would be interesting!
    '''
    pass


def menu():
    ''' Displays menu and allows user to enter choice to be returned to main - if you add more, remember to add them to the 'while choice not in' line! '''
    print("~ ramen rating database ~")
    print("1 - See distribution of scores")
    print("2 - see average score per country")
    print("3 - see average score per manufacturer")
    print("4 - Get a breakdown of a specific country")
    print("5 - See the top ten ramens")
    print("6 - See a random Ramen")
    choice = ""
    while choice not in ["1", "2", "3", "4", "5", "6", "Q"]:
        choice = input("Pick an option: ").upper()
    return choice

# the main program is below - complete the functions one at a time and test them!

ramen_data = pd.read_csv("ramen-ratings.csv")

while True:
    choice = menu()
    match choice:
        case "1":
            show_histogram_of_ramen_scores(ramen_data)
        case "2":
            show_bar_chart_stars_per_manufacturer(ramen_data)
        case "3":
            show_bar_chart_stars_per_country(ramen_data)
        case "4":
            country = input("Enter country: ").title()
            find_best_per_country(ramen_data, country)
            find_worst_per_country(ramen_data, country)
            show_piechart_of_manufacturers_by_country(ramen_data, country)
        case "5":
            show_top_ten(ramen_data)
        case "6":
            random_ramen_review(ramen_data)
        case "Q":
            break