import pandas

# Full dataset: https://www.kaggle.com/datasets/nabinoli2004/kalimati-vegetable-datasets-nepal
# shortened to 10000 rows & index column removed.

# read the csv into a dataframe
vegetable_prices = pandas.read_csv("nepal_veg.csv")

# Pandas can't auto-detect dates, so we tell it convert this column into its Timestamp datatype
vegetable_prices['Date'] = pandas.to_datetime(vegetable_prices['Date'])



# head shows the first few rows - useful to make sure that it looks right!
print(vegetable_prices.head())

# tail shows the bottom few rows
#print(vegetable_prices.tail())

# samples shows you a specified number of random rows
#print(vegetable_prices.sample(20))


# describe will give you statistical data about all numerical columns - in this case: the date, min, max and avg columns.
print(vegetable_prices.describe())


# You can easily filter data out into new dataframes
tofu_data = vegetable_prices[vegetable_prices['Commodity'] == "Tofu"]
print(tofu_data)

# You can use comparisons too:
expensive = vegetable_prices[vegetable_prices["Average"] > 100]
print(expensive)

# And you can create a new column calculated from other columns
vegetable_prices['Daily_range'] = vegetable_prices["Maximum"] - vegetable_prices["Minimum"]
print(vegetable_prices.head())

# We can combine these to do some quick analysis on data:
sorted_veg = vegetable_prices.groupby("Commodity")["Average"].agg(["mean"]).sort_values(by="mean", ascending=False)
print(sorted_veg)

# And if you ever want to get an individual row from your dataframe:
print("This is how it displays: ")
print(vegetable_prices.iloc[100])