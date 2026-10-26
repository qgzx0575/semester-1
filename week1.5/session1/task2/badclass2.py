# Another bad class implementation

# What does the runtime error mean?
# How do we fix the code?

class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a Point, given x & y coordinates.
        """
        x = x_coordinate
        y = y_coordinate


p = Point(1.5, 2.0)
print(p.x)
print(p.y)
