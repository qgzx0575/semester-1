import pandas

data = pandas.read_csv("lifestyle_data.csv")

# What data type is `data` as output from the `read_csv()` method?
# DataFrame

# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

# Find the total number of students
print(f"Total number of students: {len(data)}")

# Find the mean average GPA of the students
print(f"Average GPA: {sum(data["GPA"])/len(data)}")

# Find the standard deviation of how much sleep students get per day
print(f"SD of amount of sleep: {data["Sleep_Hours_Per_Day"].std()}")

# Find the maximum amount of study hours per day
print(f"Max study hours per day: {data["Study_Hours_Per_Day"].max()}")

# Sort the students by social hours per day ascending (lowest -> highest)
print(f"Students sorted by social hours per day: \n{data["Social_Hours_Per_Day"].sort_values()}")

# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one
data["Total_hours"] = data[["Study_Hours_Per_Day","Extracurricular_Hours_Per_Day","Sleep_Hours_Per_Day","Social_Hours_Per_Day","Physical_Activity_Hours_Per_Day"]].sum(axis=1)
print(f"Total hours: \n{data["Total_hours"]}")

# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
high = data[data["Stress_Level"] == "High"]
low = data[data["Stress_Level"] == "Low"]
print(f"{high}{low}")

# Can you work out whether having a higher stress level leads to a higher GPA?
print(f"High Stress GPA: {high["GPA"].sum()/len(high)}")
print(f"Low Stress GPA: {low["GPA"].sum()/len(low)}")