
import httpx
import pandas as pd
import matplotlib.pyplot as plt

api_key="U6KXJTZC2E8VGH39PD7UMG4BZ"   # your API key

city="Leeds"     # city location
country="UK"     # country location

elements = "include=days&elements=tempmax,tempmin,temp"   # request history of temperature data for Leeds

# URL location of the API for time history forecasts
base = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

# construct the URL string for the API call
url = base + city + "," + country + "?key=" + api_key + "&" + elements

# http request
response = httpx.get(url)

# status code (should be checked)
print(response.status_code)

# json data
data = response.json()

# raw data output
print(data)

# extract the temperature data as lists from the JSON dictionary
temp_data = data['days']

print(temp_data)

# use pandas to convert data to  dataframe

df = pd.DataFrame(temp_data)

# using matplotlib plot the 3 data sets: (tempmin,temp,tempmax) as line graphs

df.plot()

plt.show()

# annotate the graph with axis labels

# note that temperature is in Farenheit (F)
# convert to Celcius before plotting 

# using the documentation explore other data, eg. rainfall  
