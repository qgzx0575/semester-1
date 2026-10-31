# Week 1.6, Session 1: Task 3

import math


class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x, y):
        """
        Creates a point, given x & y coordinates.
        """
        self.set_x(x)
        self.set_y(y)

    def set_x(self, x):
        """
        Sets the x coordinate of this point.
        """
        if not isinstance(x, (int, float)):
            raise TypeError("x must be a number")

        self.x = x

    def set_y(self, y):
        """
        Sets the y coordinate of this point.
        """
        if not isinstance(y, (int, float)):
            raise TypeError("y must be a number")

        self.y = y

    def __str__(self):
        """
        Returns a string representation of this point.
        """
        return f"({self.x}, {self.y})"

    def distance(self):
        """
        Returns distance of this point from the origin.
        """
        return math.hypot(self.x, self.y)

    def distance_to(self, other):
        """
        Returns distance of this point from another point.
        """
        if not isinstance(other, Point):
            raise TypeError("argument must be a Point")

        return math.hypot(self.x - other.x, self.y - other.y)
