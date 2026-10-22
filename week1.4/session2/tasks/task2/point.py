# Week 4, Session 2: Task 2

# We can specify a 2d coordinate point with a tuple p=(x,y)
# Complete two functions to compute the mid-point and distance between 2 points.
# The formula to find the mid point of two points = (x1+x2)/2, y = (y1+y2)/2. Return the midpoint as a point tuple.
# The formula to find the distance between the two points = √((x2 – x1)² + (y2 – y1)²). 
# You can use math.sqrt() to find the square root of a number. 

import math

def midpoint(p1,p2):
    mid_point = 0
    x = (p1[0]+p2[0])/2
    y = (p1[1]+p2[1])/2
    mid_point = (x, y)
    return mid_point

def length(p1,p2):
    distance = 0
    distance = math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
    return distance
    

# Check if correct output is produced
m = midpoint( (0,0), (4,3) )    # mid = (2.0, 1.5)
d = length( (0,0), (4,3) )    # dist=5.0

print(f"Distance {d} Midpoint {m}")
