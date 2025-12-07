import math

# Base class
class Shape:
    def area(self):
        """
        Method to calculate area. Must be overridden by derived classes.
        """
        raise NotImplementedError("The area() method must be overridden in the subclass.")


# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
