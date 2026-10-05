# Week 1.2, Session 1: Task 3

fruit = ("apple", "banana", "cherry")
print(fruit)

# Find and display position of "banana"
print(f"The banana is in the {fruit.index("banana")+1}nd position.")

# Display how many times "cherry" occurs
print(f"The word cherry occurs {fruit.count("cherry")} time.")

# Display how many times "strawberry" occurs
print(f"The word strawberry occurs {fruit.count("strawberry")} times.")

# Unpack tuple into variables
a, b, c = fruit
first = a
second = b
third = c
print(f"The items in order are {first}, {second}, and {third}.")