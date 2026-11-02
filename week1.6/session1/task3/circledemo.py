# Week 1.6, Session 1: Task 3

import shapes

p = shapes.Point(0,0)
c = shapes.Circle(2.5, p, "red")
print(c)
c.set_position(shapes.Point(1.6,3.2))
print(f"\nMoving the cirlce...\n")
print(c)
c.set_colour(f"orange")
print(f"\nChanging the circle's color...\n")
print(c)
