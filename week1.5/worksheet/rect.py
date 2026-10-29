# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        if not (isinstance(width, int) and isinstance(height, int) and width >= 0 and height >= 0):
            raise TypeError("Values provided are not valid.")
        
        self.width = width
        self.height = height

    def is_square(self):
        """
        Returns true if width is equal to height
        """
        return self.width == self.height

    def area(self):
        """
        Returns the area of shape
        """
        return self.width*self.height

    def perimeter(self):
        """
        Returms the perimeter of shape
        """
        return 2*(self.width+self.height)
    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
