# you can give your import a short name so you don't have to type as much
# matplotlib often gets calls 'plt'
import matplotlib.pyplot as plt
# pandas is often shortened to 'pd'
import pandas as pd

# setting up our dataframe again.
vegetable_prices = pd.read_csv("nepal_veg.csv")
vegetable_prices['Date'] = pd.to_datetime(vegetable_prices['Date'])


# TO VIEW:
# Make sure the Python and Jupyter extensions are installed
# > click the arrow next to the run button
# > select: Run current file in interactive window
# If you want to re-run to see a different plot, you need to close the interactive window and repeat the steps above.


# To keep the code for each plot more separate, we can break it up into functions
# this could also be a good way to make the code more reusable
# for example, we could adapt tofu_line_plot to work with any commodity.

def tofu_line_plot(vegetable_prices):
    tofu_data = vegetable_prices[vegetable_prices['Commodity'] == 'Tofu']
    tofu_data.plot(x='Date', y='Average', title='Tofu Price Trend')
    plt.show()


# Adapted code which allows any commodity to be used
def per_commodity_line_plot(vegetable_prices, commodity):
    try:
        data = vegetable_prices[vegetable_prices['Commodity'] == commodity]
        data.plot(x='Date', y='Average', title=f'{commodity} Price Trend')
        plt.show()
    except: # validating the vegetable name to ensure users don't get errors
        print(f"{commodity} was not found in the data.")


def mean_bar_chart(vegetable_prices):
    # when you create a bar chart, you often want to do some aggregate function on your data
    # for example: here we're combining all the commodities and making the 'Average'
    # column into the mean of all of them.
    # there are other functions such as sum(), min(), max() which may be useful.
    avg_prices = vegetable_prices.groupby('Commodity')['Average'].mean()
    avg_prices.plot(kind='bar', title='Average Price by Commodity')
    plt.ylabel('Average Price')
    plt.show()


def multi_line_plot(vegetable_prices):
    # we need to pivot the table to the right format- we want the index column to be the date, and to have each commodity as a column title
    comparison_frame = vegetable_prices.pivot(index='Date', columns='Commodity', values='Maximum')
    comparison_frame[['Tamarind', 'Bamboo Shoot', 'Pineapple']].plot(kind='line', 
                                                                    figsize=(12, 6),
                                                                    # you can use any html colour - google has a picker for these
                                                                    color=['#1f77b4', '#ff7f0e', '#2ca02c'])
    # Customise the plot
    plt.title('Daily Maximum Prices of Tamarind, Bamboo Shoot, and Pineapple')
    plt.xlabel('Date')
    plt.ylabel('Maximum')
    plt.grid(True)
    plt.legend(title='Commodity')
    plt.show()


tofu_line_plot(vegetable_prices)

per_commodity_line_plot(vegetable_prices, "Ginger")

mean_bar_chart(vegetable_prices)

multi_line_plot(vegetable_prices)
