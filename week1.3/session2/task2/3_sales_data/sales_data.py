# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv
# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format

with open("sales.csv", "r") as file:
    days = []
    bestSale = [0,0]
    row = 0
    totalSum = 0
    amountSold = [0,0]
    next(file)
    for line in file:
        days.append(line.strip().split(","))
        if bestSale[1] < int(days[row][2]):
            bestSale = [days[row][0],int(days[row][2])]
        if amountSold[1] < int(days[row][3]):
            amountSold = [days[row][1],int(days[row][3])]
        totalSum += int(days[row][2])
        row += 1
    print(f"The largest sale day was on {bestSale[0]}, with a revenue of £{bestSale[1]}.")
    print(f"The average sale amount was £{totalSum/(row+1)}.")
    print(f"The best selling widget is {amountSold[0]}, selling {amountSold[1]} items.")



# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows