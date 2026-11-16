
# Task 3 - weather data

The web site [Visual Crossing](https://www.visualcrossing.com/weather-api/) provides an API for weather data.

We can query various weather data for a location, eg. rainfall in Leeds for 14 days.

We are going to step through the data processing and use several Python features and libraries to extract and plot the data
- dictionaries for JSON data
- Pandas for data handling 
- matplotlib for plotting data

Test your code after each step to ensure data is correct.

This can be achieved simply through printing the current data set.

## Sign up for an API key

To use the API you must register and be given a personal API key.

You have limited free use of the site so please respect this

## Constructing a URL

[API documentation](https://www.visualcrossing.com/resources/documentation/weather-api/timeline-weather-api/) shows us how to construct a request

A URL request is composed of several parts
- base URL
- location requested
- data requested
- your API key

The code template provided asks for rainfall in Leeds.

## httpx request

We can now create an API call with `httpx` as before.

We should check the `response` `status_code` at this point.
- add some code for the check and exit if the GET request was unsuccessful.
- APIs can sometimes be unavailable or you can make a simple error with the URL

## JSON repsonse

We can extract the JSON data from the response as a dictionary

`data = response.json()`

## Parsing data from the JSON

Print it out in your code.

Inspecting the `data` dictionary we can identify a temperature history
with the key `days`
- extract this to a separate dictionary `temp_data`
- print `temp_data` to ensure you have done this correctly

## Processing the data - pandas

Remember to `pip install pandas` in the terminal

Remember to `import pandas as pd` similar to last session

The documentation is useful or you cane review what we did last session.

We can convert the temperature data dictioary to a pandas DataFrame with the constructor

`df = pd.DataFrame(temp_data)`

- add the code
- print the dataframe to verify

## Plotting the data - matplotlib

Remember to `import matplotlib.pyplot as plt` similar to last session

Remember that we need to install Python and Jupyter extensions and run in an interactive window
- this means we cannot run in a virtual environment
- you will need to deactivate any existing one
- we do not recommend this outside of Codespaces

The documentation is useful or you cane review what we did last session.

Plot the data using a matplotlib line-graph
- you should see 3 lines for minimum, maximum and average temperature per day
- add suitable annotation to the axes

## Further tasks

These are optional but useful exercises.

### F -> C

Notice that temperature data is returned in Farenheit (F) 
- convert to Celcius (C) before plotting

### Other data

Query and plot other data 
- read the API documentation to see what is available
