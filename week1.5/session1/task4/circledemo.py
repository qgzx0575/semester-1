# Week 1.5, Session 1: Task 4

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle

import geometry
# Finally, add code here to demonstrate use of Point
p = geometry.Point(4,3)
q = geometry.Point(2,2)
print(p.distance())
print(p.distance_to(q))

r = geometry.Circle(3, geometry.Point(2,2))
print(r.area())
print(r.perimeter())