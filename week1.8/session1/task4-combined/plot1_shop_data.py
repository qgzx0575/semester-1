'''
This is the recommended start point for matplotlib, and should help you to build up skills.

The difficult part of most plotting is working out what the dataframe needs to look like to get a good plot, and this will help you with that!

This first file is a worked example of creating some graphs - there are activities at the bottom for you to practice.
'''

import pandas as pd
import matplotlib.pyplot as plt

# reading data & converting date into a datetime
shop_data = pd.read_csv("shop_sales_data_one_month.csv")
shop_data['Date'] = pd.to_datetime(shop_data['Date'])

# Step 1: check that the data looks sensible - you should do this often!:
print(shop_data.head())

# Step 2: add a column 'Total_Price' which is equal to Units_Sold * Unit_Price

shop_data["Total_Price"] = shop_data["Units_Sold"] * shop_data["Unit_Price"]

# Step 3: In order to make our first graph, we want to group everything together by Dat

# we need to group by the Date - this joins all the rows with the same date together
# .sum() tells Pandas to add together all the values - this means we can easily get the sales/day.
# We use the kwarg numeric_only=True to make sure we don't get errors.
total_daily_sales = shop_data.groupby("Date").sum(numeric_only=True)
print(total_daily_sales)


# Then you can filter out the columns you want to put into a graph - we will show sales per day.

# first, we get just the column we want out of the table. Because we grouped by the Date, the date is now the index row (first row) so that is already in there.
# again, you would usually print here to check what your dataframe looks like to help work out what filtering to do!
total_daily_sales = total_daily_sales["Total_Price"]

# I like to check I have the right data in my table so I usually print it here before I plot the graph
print(total_daily_sales)

# and once you're happy that you have a dataframe with the right stuff in it, you can plot it:
total_daily_sales.plot(kind="line")
# then finally, remember to plt.show() which displays the graph.
plt.show()


# We can do the same to sort by category - this time, we can make a bar chart:

sales_per_category = shop_data.groupby("Category").sum(numeric_only=True)
sales_per_category = sales_per_category["Total_Price"]

# this time, we add some colour to our graph:
sales_per_category.plot(kind="bar", color="#eff542", title="Sales per Category")
plt.show()


# And finally, let's do a pie chart of sales per category:
# we can re-use our existing dataframe for this.
sales_per_category.plot(kind="pie", colors=["#E57A44", "#8AB9B5", "#F5E6E8", "#481620"])
plt.show()

# To practice, here are some tasks to use - remember, the original data is named shop_data

# Create a pie chart to show sales per product



