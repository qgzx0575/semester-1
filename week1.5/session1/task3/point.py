# Week 1.5, Session 1: Task 3
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



# Finally, add code here to demonstrate use of Point
p = Point(4,3)
q = Point(2,2)
print(p.distance())
print(p.distance_to(q))