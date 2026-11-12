# Week 1.7, Session 1: Task 2 - unit tests for the methods in Point and Circle

from geometry import Point, Circle
import math

def test_point_constructor():
    p = Point(5, -2)
    assert p.x == 5
    assert p.y == -2

def test_point_distance():
    assert Point(0, 0).distance() == 0.0
    assert Point(6, 8).distance() == 10.0
    
def test_point_distance_to():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    
    # complete the implementation for
    # testing distance_to()
    

# Write test functions to test the __init__(), 
# area() and perimeter() methods in Circle class
# you can use the default value for centre coordinates

def test_init():
    p = Point(5, -2)
    assert p.x == 5
    assert p.y == -2

def test_area():
    p = Circle(5)
    assert p.area() == math.pi * p.radius**2

def test_perimeter():
    p = Circle(5)
    assert p.perimeter() == 2*math.pi*p.radius