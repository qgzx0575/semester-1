# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

class Point:
    """
    A Point in 2D space.
    """
    # Add constructor here
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
    # Add distance() method here
    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    # Add distance_to() method here
    def distance_to(self, other = (0,0)):
        return math.sqrt((self.x - other.x)**2 - (self.y - other.y)**2)
    # (This will need a parameter representing another point)



class Circle:
    def __init__(self, radius, center = Point(0,0)):
        self.radius = radius
        self.center = center
    def area(self):
        return math.pi*self.radius**2
    def perimeter(self):
        return math.pi*self.radius*2

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

# Don't add any testing code to this file!
