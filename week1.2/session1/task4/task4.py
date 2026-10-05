# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?
# I believe it will return items that are in both lists
both = fruit.intersection(vegetables)
print(both)

# Why does the following code diplay five items?
# It lists all items in both lists, no repeats
food = fruit.union(vegetables)
print(food)

# Add an item to fruit
fruit.add("grapes")
print(fruit)

# Remove an item from vegetables
vegetables.remove("leek")

# Find and display symmetric difference of the two sets
difference = fruit.difference(vegetables)
print(difference)
