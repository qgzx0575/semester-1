# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers["York"] = "Ouse"
rivers["Manchester"] = "Irwell"
print(rivers)

# Display all the keys
print(rivers.keys())

# Display all the values
print(rivers.values())

# Display all the key:value pairs, as tuples
print(rivers.items())

# Delete an entry from the rivers database
rivers.pop("Manchester")
print(rivers)